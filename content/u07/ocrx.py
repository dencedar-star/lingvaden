"""Помощники для текстов из OCR модулей 7–9: аудиоскрипт из нескольких областей, статья в колонках, списки с маркерами."""
import re
from ocrtext import lines, fixed, _fix, K


def _rows(regions):
    out = []
    for p, box in regions:
        out += [fixed(p, _fix(l["t"])).strip() for l in lines(p, box)]
    return out


def script2(regions, speakers):
    """Аудиоскрипт из областей [(стр, box), …] подряд: [(говорящий, реплика)], ('#', заголовок).
    speakers — буквы говорящих (OCR путает «P:» и «P.»)."""
    sp = re.compile(rf"^([{speakers}])\s*[:.;]\s*(.*)$")
    out = []
    for t in _rows(regions):
        if re.match(r"^Conversation \d+$", t):
            out.append(("#", t))
            continue
        if re.match(r"^[A-Z]\s*=\s*[A-Z]\w+", t):  # «D = Daniel, P = Paulina»
            continue
        m = sp.match(t)
        if m:
            out.append((m.group(1), m.group(2)))
        elif out and out[-1][0] != "#":
            s, prev = out[-1]
            out[-1] = (s, prev[:-1] + t if prev.endswith("-") and not prev.endswith(" -") else prev + " " + t)
    return out


def numbered_script(regions):
    """Аудиоскрипт из пронумерованных предложений: [('1', текст), …]."""
    out = []
    for t in _rows(regions):
        m = re.match(r"^(\d+)\s+(.*)$", t)
        if m:
            out.append([m.group(1), m.group(2)])
        elif out:
            out[-1][1] += " " + t
    return [tuple(x) for x in out]


def col_paras(p, boxes, indent=8, heads=()):
    """Абзацы статьи, идущей по нескольким колонкам: новый абзац — строка с отступом; колонка без отступа продолжает абзац.
    heads — подзаголовки: выводятся как '#текст', после них начинается новый абзац."""
    paras, after_head = [], False
    for box in boxes:
        ls = lines(p, box)
        if not ls:
            continue
        left = min(l["x"] for l in ls)
        for l in ls:
            t = fixed(p, _fix(l["t"])).strip()
            if t in heads:
                paras.append("#" + t)
                after_head = True
                continue
            if l["x"] - left > indent * K or not paras or after_head:
                paras.append(t)
                after_head = False
            elif paras[-1].endswith("-") and not paras[-1].endswith(" -"):
                paras[-1] = paras[-1][:-1] + t
            else:
                paras[-1] += " " + t
    return [s if s.startswith("#") else fixed(p, s) for s in paras]


def bullets(p, box, mark="•"):
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip()
        if t.startswith(mark):
            out.append(t.lstrip(mark + " "))
        elif out:
            out[-1] += " " + t
    return out
