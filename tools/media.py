"""Медиа курса из sources/: аудио учебника (CD 1, CD 2), аудио рабочей тетради (WB Audio), видео (Video 1).
Номер записи (1.1, Review 2.2 …) берётся из её начала: диктор называет его вслух (распознавание — mlx-whisper).
Треки без номера — продолжение предыдущей записи (части 1, 2, 3 …): склеиваются в один mp3, границы частей — в parts.
Результат: media/{sb,wb,video}/… и media/index.json. Запуск: python3 tools/media.py"""
import json, os, re, sys
from pathlib import Path
import av, numpy as np

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "sources", ROOT / "media"
CACHE = ROOT / "sources" / "asr"          # распознанный текст треков (кеш)
RATE = 22050
W = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen".split())}


def load(path, rate=16000):
    c = av.open(str(path)); r = av.AudioResampler(format="s16", layout="mono", rate=rate); buf = []
    for fr in c.decode(audio=0):
        buf += [f.to_ndarray().reshape(-1) for f in r.resample(fr)]
    buf += [f.to_ndarray().reshape(-1) for f in r.resample(None)]
    return np.concatenate(buf)


def asr(path, model="mlx-community/whisper-small.en-mlx"):
    key = CACHE / (re.sub(r"[^\w.-]+", "_", f"{path.parent.name}__{path.name}__{model.split('/')[-1]}") + ".json")
    if key.exists():
        return json.loads(key.read_text())
    import mlx_whisper
    a = load(path).astype(np.float32) / 32768
    r = mlx_whisper.transcribe(a, path_or_hf_repo=model, condition_on_previous_text=False)
    d = {"dur": len(a) / 16000, "text": r["text"].strip()}
    CACHE.mkdir(exist_ok=True); key.write_text(json.dumps(d, ensure_ascii=False))
    print(path.name, model.split("/")[-1], d["text"][:60], flush=True)
    return d


def label(t):
    m = re.match(r"(Review\s+)?(\d+)\.\s?(\d+)\b", t)
    if m:
        return ("R" if m.group(1) else "") + f"{m.group(2)}.{m.group(3)}"
    m = re.match(r"(Review\s+)?(\w+)\s+point\s+(\w+)", t, re.I)
    if m and m.group(2).lower() in W and m.group(3).lower() in W:
        return ("R" if m.group(1) else "") + f"{W[m.group(2).lower()]}.{W[m.group(3).lower()]}"


def groups(dirs):
    out = []
    for d in dirs:
        for f in sorted((SRC / d).glob("*.mp3"), key=lambda p: int(re.findall(r"\d+", p.name)[0])):
            t = asr(f)["text"]
            if re.search(r"Published|Deller|Workbook by", t[:120]):
                continue                       # заставка диска
            L = label(t)
            if L:
                out.append([L, []])
            assert out, f"первый трек без номера: {f}"
            out[-1][1].append(f)
    return out


def encode(parts, dst):
    pcm = [load(p, RATE) for p in parts]
    offs, t = [], 0.0
    for x in pcm:
        offs.append(round(t, 2)); t += len(x) / RATE
    if dst.exists():
        return offs, round(t, 1)
    o = av.open(str(dst), "w"); s = o.add_stream("libmp3lame", rate=RATE); s.layout = "mono"; s.bit_rate = 64000
    data = np.concatenate(pcm)
    for i in range(0, len(data), RATE):
        fr = av.AudioFrame.from_ndarray(data[i:i + RATE].reshape(1, -1), format="s16", layout="mono"); fr.sample_rate = RATE
        for p in s.encode(fr): o.mux(p)
    for p in s.encode(None): o.mux(p)
    o.close()
    return offs, round(t, 1)


def remux(src, dst):
    if dst.exists():
        return
    i = av.open(str(src)); o = av.open(str(dst), "w", options={"movflags": "+faststart"})
    m = {s.index: o.add_stream_from_template(s) for s in (i.streams.video[0], i.streams.audio[0])}
    for pk in i.demux(*[i.streams.video[0], i.streams.audio[0]]):
        if pk.dts is None: continue
        pk.stream = m[pk.stream.index]; o.mux(pk)
    o.close()


def fname(L):
    return L.replace("R", "r").replace(".", "-") + ".mp3"


def main():
    idx = {"sb": {}, "wb": {}, "video": {}}
    for kind, dirs in (("sb", ["Outcomes Intermediate CD 1", "Outcomes Intermediate CD 2"]),
                       ("wb", ["Outcomes Intеrmediate WB Audio"])):      # в имени папки WB кириллическая «е»
        (OUT / kind).mkdir(parents=True, exist_ok=True)
        for L, parts in groups(dirs):
            assert L not in idx[kind], f"повтор записи {kind} {L}"
            offs, dur = encode(parts, OUT / kind / fname(L))
            e = {"f": f"{kind}/{fname(L)}", "dur": dur, "parts": offs if len(offs) > 1 else []}
            if kind == "wb":
                f = OUT / kind / fname(L)
                e["text"] = asr(f, "mlx-community/whisper-large-v3-turbo")["text"]
                e["text2"] = " ".join(asr(p)["text"] for p in parts)
            idx[kind][L] = e
            print(kind, L, dur, len(parts), flush=True)
    (OUT / "video").mkdir(parents=True, exist_ok=True)
    seen = set()
    for f in sorted((SRC / "Outcomes Intermediate Video 1").glob("*.flv"), key=lambda p: int(re.findall(r"\d+", p.name)[0])):
        t = asr_video(f)
        if t in seen:
            print("дубликат видео:", f.name); continue       # (6) — тот же ролик, что (5)
        seen.add(t)
        n = len(idx["video"]) + 1
        remux(f, OUT / "video" / f"v{n}.mp4")
        idx["video"][str(n)] = {"f": f"video/v{n}.mp4", "dur": round(float(av.open(str(f)).duration) / 1e6), "src": f.name}
    (OUT / "index.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1))


def asr_video(f):
    return asr(f)["text"]


if __name__ == "__main__":
    main()
