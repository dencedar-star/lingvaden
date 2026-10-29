"""Уроки письма по оглавлению учебника: после каждых четырёх модулей — два урока (Writing 01–08).
Урок ставится в первые два модуля своего блока; в остальных модулях вкладка «Письмо» ссылается на них."""
from lib import SEC

TITLES = {1: "Introducing yourself", 2: "Short emails", 3: "Stories", 4: "Making requests",
          5: "Suggesting changes", 6: "Reports", 7: "For and against", 8: "A review"}
HOME = {1: 1, 2: 2, 3: 5, 4: 6, 5: 9, 6: 10, 7: 13, 8: 14}   # урок → модуль


def page(k):
    return 120 + 2 * (k - 1)


def note(n):
    """Карточка для модуля n без своего урока: какие уроки письма относятся к его блоку и где они."""
    b = (n - 1) // 4
    lo, hi = 4 * b + 1, 4 * b + 4
    items = "".join(
        f'<li><a href="../unit{HOME[k]:02d}/writing.html"><b>Writing {k:02d}</b> {TITLES[k]}</a> '
        f'<small>(учебник, с. {page(k)}–{page(k) + 1}) — во вкладке «Письмо» модуля {HOME[k]}</small></li>'
        for k in (2 * b + 1, 2 * b + 2))
    return SEC("Уроки письма этого блока", "",
               f'<div class="page"><p>По оглавлению учебника уроки письма идут после каждых четырёх модулей: к модулям '
               f'{lo}–{hi} относятся два урока. Своего урока письма у модуля {n} нет.</p><ul class="dots">{items}</ul></div>')
