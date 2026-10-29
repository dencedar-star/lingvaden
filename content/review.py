"""Общие детали страниц Review 01–04 (вкладка «Письмо» второго и последнего модулей каждого блока из четырёх юнитов)."""
import re
from lib import S, EX, SEC, SCRIPT
from ocrtext import lines, fixed, _fix


def unit_of_gr(p):
    """Модуль, в котором лежит страница грамматического справочника p (юниты 1–4 — по две страницы с 136, дальше по одной)."""
    return (p - 136) // 2 + 1 if p < 144 else p - 144 + 5


def gr(p):
    """«Find this difficult?» — ссылка на справочник в нужном модуле."""
    return (f'<p class="help">▶ Find this difficult? Look back at <a href="../unit{unit_of_gr(p):02d}/theory.html#gr{p}">'
            f'grammar reference p. {p}</a></p>')


def unit_of_page(p):
    """Модуль страницы учебника: юниты по 6 страниц с с. 8, после каждых четырёх — 4 страницы Review."""
    return (p - 8 - 4 * ((p >= 36) + (p >= 64) + (p >= 92))) // 6 + 1


def practice(id, items):
    """Conversation practice: [(название, страница учебника)] → ссылки на страницы юнитов."""
    links = "<br>".join(f'<a href="../unit{unit_of_page(p):02d}/book.html#p{p}">{t} p. {p}</a>' for t, p in items)
    return (EX(id, "", "Choose one of these <i>Conversation Practice</i> activities:", f"<p>{links}</p>"
               "<p><b>Two of you should do the task. The third person should listen and then give a mark of between 1 and 10 "
               "for the performance. Explain your decision. Then change roles.</b></p>"))


def sounds(id, letter, instr, cells, words, key):
    """Pronunciation: таблица звуков (cells — [(символ, слово)]) и слова, которые надо разнести по звукам."""
    tbl = '<table class="tbl sounds">' + "".join(
        "<tr>" + "".join(f'<td><span class="phon">{s}</span><br>{w}</td>' for s, w in cells[i:i + 4]) + "</tr>"
        for i in range(0, len(cells), 4)) + "</table>"
    opts = [f"{s} {w}" for s, w in cells]
    lab = {w: f"{s} {w}" for s, w in cells}
    from lib import OL
    return tbl, EX(id, letter, instr, OL([f"{w} → {S(lab[key[w]], opts)}" for w in words], "items plain"))


def numbered_script(num, parts, page):
    """Аудиоскрипт из пронумерованных монологов: parts — [(страница, box)] в порядке чтения."""
    items = []
    for p, box in parts:
        for l in lines(p, box):
            t = fixed(p, _fix(l["t"])).strip()
            if re.match(r"^\W*R\s?\d\.\d$", t) or t in ("AUDIOSCRIPT",) or t.startswith("REVIEW"):
                continue
            m = re.match(r"^(\d)\s+(.*)$", t)
            if m:
                items.append([f"Speaker {m.group(1)}", m.group(2)])
            elif items:
                items[-1][1] += " " + t
    return SCRIPT(num, "", [tuple(i) for i in items], page)


def total(n):
    return f'<p class="note-s">В учебнике за этот раздел — до {n} баллов.</p>'
