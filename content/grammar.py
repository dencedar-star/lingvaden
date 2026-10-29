"""Грамматический справочник учебника из OCR: правила (синие) и примеры (чёрные)."""
from ocrtext import styled


def grammar_ref(p, box, heads=(), skip=(), breaks=()):
    """Справочник: синие строки — правила, чёрные — примеры, заголовки — по регистру/heads.
    skip — строки (целиком), которые нужно выбросить (вставки, таблицы); breaks — синие строки, с которых начинается новое правило."""
    rows = styled(p, box)
    rows = [r for r in rows if r[0].strip() not in skip]
    rows = [r for r in rows if "OUTCOMES" not in r[0] and "GRAMMAR REFERENCE" not in r[0]]
    blocks = []  # (тип, текст)
    for i, (t, blue) in enumerate(rows):
        nxt_blue = i + 1 < len(rows) and rows[i + 1][1]
        if t in heads or not blue and (t.isupper() or nxt_blue and not t.rstrip().endswith((".", "?", "!", ")", "✓", "✗"))):
            blocks.append(["h", t])
        elif blue:
            if blocks and blocks[-1][0] == "r" and t not in breaks:
                blocks[-1][1] += " " + t
            else:
                blocks.append(["r", t])
        else:
            if blocks and blocks[-1][0] == "e" and not blocks[-1][1].rstrip().endswith(("?", "!", ".", ")", "✓", "✗")):
                blocks[-1][1] += " " + t
            else:
                blocks.append(["e", t])
    out = []
    for k, t in blocks:
        if k == "h":
            tag = "h2" if t.isupper() else "h3"
            out.append(f"<{tag}>{t.capitalize() if t.isupper() else t}</{tag}>")
        elif k == "r":
            out.append(f'<p class="rule">{t}</p>')
        else:
            out.append(f'<p class="egs"><i>{t}</i></p>')
    return "".join(out)


def gr_page(p, anchor, html, title=""):
    h = f"<h2>{title}</h2>" if title else ""
    return f'<article class="page gr" id="{anchor}"><span class="page-no">Учебник, с. {p}</span>{h}{html}</article>'
