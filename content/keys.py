"""Фрагменты из ключей (PDF с текстовым слоем): берём колонку по ширине из pdftotext -layout."""
import subprocess
from functools import lru_cache
from pathlib import Path

KEYS = Path(__file__).resolve().parent.parent / "sources" / "Outcomes_Intermediate_SB_keys.pdf"


@lru_cache(None)
def _layout(page):
    return subprocess.run(["pdftotext", "-layout", "-f", str(page), "-l", str(page), str(KEYS), "-"],
                          capture_output=True, text=True, check=True).stdout.splitlines()


def column(page, col, start, end, split=58):
    """Текст колонки (0 — левая, 1 — правая) между строками, начинающимися с start и end (не включая)."""
    rows = [(r[:split] if col == 0 else r[split:]).strip() for r in _layout(page)]
    out, on = [], False
    for r in rows:
        if not on and r.startswith(start):
            on = True
            continue
        if on and r.startswith(end):
            break
        if on and r:
            out.append(r)
    return out


def joined(page, col, start, end):
    return " ".join(column(page, col, start, end)).replace("’", "’")


def rows(page, col, a, b, split=58):
    """Непустые строки колонки с номерами строк макета в [a, b)."""
    out = []
    for r in _layout(page)[a:b]:
        t = (r[:split] if col == 0 else r[split:]).strip()
        if t:
            out.append(t)
    return out


def numbered(lines):
    """Склеивает перенесённые строки в пункты, начинающиеся с цифры."""
    out = []
    for r in lines:
        if r[:1].isdigit() or not out:
            out.append(r)
        else:
            out[-1] += " " + r
    return out
