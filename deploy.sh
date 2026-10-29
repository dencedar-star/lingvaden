#!/bin/sh
# Lingvaden FTP deployment; passwords are read from handover-private/credentials.json.
set -eu
cd "$(dirname "$0")"
exec python3 tools/deploy_ftp.py "$@"
