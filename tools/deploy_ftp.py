#!/usr/bin/env python3
"""Build and publish Lingvaden using handover-private/credentials.json."""
import argparse
import ftplib
import hashlib
import io
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def connect(settings):
    ftp = ftplib.FTP(timeout=60)
    ftp.connect(settings['host'], settings.get('port', 21))
    ftp.login(settings['username'], settings['password'])
    return ftp


def retrieve(settings, remote):
    for attempt in range(3):
        ftp = connect(settings)
        try:
            ftp.voidcmd('TYPE I')
            try:
                expected = ftp.size(remote)
            except ftplib.error_perm as exc:
                if str(exc).startswith('550'):
                    return None
                raise
            data = bytearray()
            try:
                ftp.retrbinary('RETR ' + remote, data.extend)
            except ConnectionResetError:
                # This hosting sometimes resets the data socket after the last byte.
                pass
            if len(data) != expected:
                raise IOError('Incomplete download: ' + remote)
            return bytes(data)
        except (OSError, ftplib.Error):
            if attempt == 2:
                raise
            time.sleep(1)
        finally:
            ftp.close()


def store(settings, remote, data):
    for attempt in range(3):
        ftp = connect(settings)
        try:
            ftp.cwd('/')
            parts = remote.strip('/').split('/')
            for part in parts[:-1]:
                try:
                    ftp.cwd(part)
                except ftplib.error_perm:
                    ftp.mkd(part)
                    ftp.cwd(part)
            ftp.storbinary('STOR ' + parts[-1], io.BytesIO(data), blocksize=131072)
            ftp.voidcmd('TYPE I')
            if ftp.size(parts[-1]) != len(data):
                raise IOError('Uploaded size mismatch: ' + remote)
            return
        except (OSError, ftplib.Error):
            if attempt == 2:
                raise
            time.sleep(1)
        finally:
            ftp.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check FTP login and www without changing server files')
    parser.add_argument('--dry-run', action='store_true', help='Build and inspect files without connecting to FTP')
    parser.add_argument('--configure', action='store_true', help='Also upload PHP config outside www, with backup')
    args = parser.parse_args()
    credentials = json.loads((ROOT / 'handover-private/credentials.json').read_text(encoding='utf-8'))
    settings = credentials['ftp']
    document_root = settings['document_root'].rstrip('/')
    if args.check:
        ftp = connect(settings)
        try:
            ftp.cwd(document_root)
            print('FTP login OK; document root:', ftp.pwd())
        finally:
            ftp.close()
        return
    subprocess.run([sys.executable, '-B', str(ROOT / 'build.py')], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    files = sorted(p for p in (ROOT / 'output').rglob('*') if p.is_file() and p.name != '.DS_Store')
    if args.dry_run:
        print('Build OK:', len(files), 'files;', sum(p.stat().st_size for p in files), 'bytes')
        print('Destination:', settings['host'], document_root)
        print('No server files changed. MySQL is not modified by this script.')
        return
    backup = ROOT / 'handover-private/backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True, mode=0o700)
    manifest_path = settings['site_directory'].rstrip('/') + '/deploy-manifest.json'
    old_manifest = retrieve(settings, manifest_path)
    old = json.loads(old_manifest.decode('utf-8')) if old_manifest else {}
    manifest = {}
    uploaded = 0
    jobs = [(p.relative_to(ROOT / 'output').as_posix(), p, document_root + '/' + p.relative_to(ROOT / 'output').as_posix()) for p in files]
    if args.configure:
        jobs.append(('_private/english_config.php', ROOT / 'handover-private/english_config.php', settings['config_path']))
    for relative, local, remote in jobs:
        data = local.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        manifest[relative] = digest
        if old.get(relative) == digest:
            continue
        previous = retrieve(settings, remote)
        if previous is not None:
            target = backup / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(previous)
            target.chmod(0o600)
            if previous == data:
                continue
        store(settings, remote, data)
        uploaded += 1
        print('Uploaded:', relative, flush=True)
    store(settings, manifest_path, (json.dumps(manifest, indent=2) + '\n').encode())
    print('Complete. Uploaded:', uploaded, '; local backups:', backup)
    print('Existing remote files are not deleted. MySQL was not modified.')


if __name__ == '__main__':
    main()
