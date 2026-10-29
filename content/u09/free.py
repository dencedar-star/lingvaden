"""Страница «Письмо» модуля 9: в учебнике 8 уроков письма, к юниту 09 отдельного урока нет — письменные задания по юниту."""
from lib import EX, UL, SEC, PAGE_BOX, IMG


def build():
    note = ('<div class="note"><p>В учебнике <i>Outcomes Intermediate</i> восемь уроков письма (Writing 01–08), и к юниту 09 '
            'отдельного урока нет. Ниже — письменные задания на лексику и грамматику этого юнита. Автоматической проверки у них '
            'нет: текст сохраняется, и его может посмотреть преподаватель.</p></div>')
    advert = SEC("Writing", "An advert for a room",
                 EX("w9-a", "A", "Look again at the adverts for host families on p. 69. Write an advert for a room in your flat or "
                    "house (or an imaginary one). Use the language from <i>Describing where you live</i> (p. 64) and "
                    "<i>Describing areas</i> (p. 68).", UL([
                        "What is the room like? (<i>spacious, compact, bright …</i>)", "What is the area like? (<i>lively, green, "
                        "residential, convenient …</i>)", "What is included? How much does it cost?", "Are there any rules?"]) +
                    '<div class="writer" data-target="60–90" data-id="u09-advert"><textarea placeholder="Bright, spacious room in '
                    '…"></textarea><div class="cnt"></div></div>'))
    changes = SEC("Writing", "How my area has changed",
                  EX("w9-b", "B", "Write a short text about the town or area where you live: what it is like now and how it has "
                     "changed. Compare the past with now (p. 68) and use the language for describing changes (p. 66).", UL([
                         "<i>It’s far more … than it used to be.</i>", "<i>There’s nowhere near as much … as there was …</i>",
                         "<i>There are fewer and fewer …</i>", "<i>House prices have risen dramatically over the last few years.</i>"]) +
                     '<div class="writer" data-target="150–180" data-id="u09-area"><textarea placeholder="I live in …"></textarea>'
                     '<div class="cnt"></div></div>'))
    return PAGE_BOX("64–69", IMG("../assets/img/unit09/p65-building.jpg", "", cls="md") + note + advert + changes)
