"""Текст учебника из OCR (sources/ocr/pNN.json). Координаты областей — в масштабе скана 794x1123."""
import json, re
from functools import lru_cache
from pathlib import Path

OCR = Path(__file__).resolve().parent / "sources" / "ocr"
K = 2481 / 794  # OCR сделан с рендера 300 dpi


@lru_cache(None)
def _page(p):
    return json.loads((OCR / f"p{p}.json").read_text())


def lines(p, box):
    x0, y0, x1, y1 = [v * K for v in box]
    ls = [l for l in _page(p) if x0 <= l["x"] + 2 and l["x"] + l["w"] <= x1 + 40 and y0 <= l["y"] and l["y"] + l["h"] <= y1 + 10]
    ls.sort(key=lambda l: (l["y"], l["x"]))
    return ls


def _fix(s):
    s = s.replace("'", "’").replace("’’", "”")
    s = re.sub(r'(^|[\s(])"', r"\1“", s)
    s = s.replace('"', "”")
    s = re.sub(r"(^|\s)’", r"\1‘", s)
    return s


def paras(p, box, indent=18, gap=1.7):
    """Абзацы: новый абзац при отступе первой строки или большом вертикальном интервале."""
    ls = lines(p, box)
    if not ls:
        return []
    left = min(l["x"] for l in ls)
    out, cur, prev = [], [], None
    for l in ls:
        new = prev is not None and (l["x"] - left > indent * K / 3.125 * 3.125 / K * K if False else l["x"] - left > indent
                                    or l["y"] - (prev["y"] + prev["h"]) > gap * prev["h"])
        if new and cur:
            out.append(cur); cur = []
        cur.append(l["t"]); prev = l
    if cur:
        out.append(cur)
    res = []
    for c in out:
        s = ""
        for t in c:
            if s.endswith("-") and not s.endswith(" -"):
                s = s[:-1] + t
            else:
                s = (s + " " + t).strip()
        res.append(_fix(s))
    return res


def text(p, box):
    return " ".join(paras(p, box, indent=10**6, gap=10**6))


# ---- исправления ошибок распознавания (страница -> [(было, стало)]) ----
FIX = {}


def fixed(p, s):
    for a, b in FIX.get(p, []) + FIX.get("*", []):
        s = s.replace(a, b)
    return s


# ---- цвет строки: синий текст правил в справочнике ----
_imgs = {}


def _img(p):
    if p not in _imgs:
        import subprocess, tempfile
        from PIL import Image
        src = Path(__file__).resolve().parent / "sources" / "Outcomes_Intermediate_SB.pdf"
        d = tempfile.mkdtemp()
        subprocess.run(["pdfimages", "-f", str(p), "-l", str(p), "-png", str(src), d + "/i"], check=True)
        _imgs[p] = Image.open(d + "/i-000.png").convert("RGB")
    return _imgs[p]


def is_blue(p, l):
    im = _img(p)
    box = (int(l["x"] / K), int(l["y"] / K), int((l["x"] + l["w"]) / K), int((l["y"] + l["h"]) / K))
    px = [c for c in im.crop(box).getdata() if sum(c) < 400]
    if not px:
        return False
    return sum(b - r for r, g, b in px) / len(px) > 35


def styled(p, box):
    """Строки области с признаком цвета: [(текст, синий?)]."""
    return [(fixed(p, _fix(l["t"])), is_blue(p, l)) for l in lines(p, box)]


def script(p, box):
    """Аудиоскрипт: [(говорящий, реплика)] и ('#', номер) для пронумерованных диалогов."""
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip()
        if re.match(r"^Conversation \d+$", t):
            out.append(("#", t))
            continue
        if re.match(r"^[A-Z]\s*[=-]\s*[A-Z]\w+,", t):  # «R = Ryan, C = Clara»
            continue
        m = re.match(r"^(\d+)\s+([A-Z]):\s*(.*)$", t)
        if m:
            out.append(("#", m.group(1)))
            out.append((m.group(2), m.group(3)))
            continue
        m = re.match(r"^([A-Z]):\s*(.*)$", t)
        if m:
            out.append((m.group(1), m.group(2)))
        elif out and out[-1][0] != "#":
            sp, prev = out[-1]
            out[-1] = (sp, prev + " " + t)
    return out
