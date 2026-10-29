"""Страница «Тесты»: упражнения Grammar reference p. 148 (ключи — Grammar Reference, 09) и итоговый тест."""
from lib import G, EX, OL
from u03.tests import gloss
from . import shared as X

MISS = [("It used to be a lot greener it is now.", "It used to be a lot greener than it is now."),
        ("It wasn’t nice as the last time we went there.", "It wasn’t as nice as the last time we went there."),
        ("There’s not as people living here as when I was a kid.", "There’s not as many people living here as when I was a kid."),
        ("It’s far multicultural than it was ten years ago.", "It’s far more multicultural than it was ten years ago."),
        ("There are more restaurants than were before.", "There are more restaurants than there were before."),
        ("The area isn’t as working class as used to be.", "The area isn’t as working class as it used to be."),
        ("There isn’t as pollution round here since the government tightened the laws.",
         "There isn’t as much pollution round here since the government tightened the laws."),
        ("There use to be as many shops here as there are now.", "There never used to be as many shops here as there are now.")]


def gr1():
    """Exercise 1. Ключ: 1 greener than it is 2 as nice 3 as many people 4 far more multicultural 5 there are (far) more… than
    there were 6 working class as it 7 as much pollution 8 there never used to be."""
    return EX("t9-g1", "1", "There is one word missing in each sentence in 1–8. Write the sentences with the word in the correct "
              "place.", OL([f"{q}<br>{G(a, 'wide')}" for q, a in MISS]))


def gr2():
    """Exercise 2. Ключ: 1 later and later 2 more and more 3 fewer and fewer 4 more and more expensive 5 more and more
    sophisticated 6 less and less."""
    rows = ["Children are leaving home <i>later and later</i>, with the average home-leaving age now over 30.",
            f"Despite the government’s attempts to reduce traffic, there are {G('more and more')} cars on the road.",
            f"{G('Fewer and fewer')} people can afford to buy a home these days as prices continue to rise.",
            f"The cost of weddings is getting {G('more and more expensive')} as people go for ever bigger parties.",
            f"Computer technology is becoming {G('more and more sophisticated')}.",
            f"As there is {G('less and less')} space available in the city, they’re having to build ever taller skyscrapers."]
    return EX("t9-g2", "2", "Complete the sentences by making ‘double’ comparatives with the words in the box, as in the example.",
              X.wordbox(["less", "late", "expensive", "more", "few", "sophisticated"]) + OL(rows))


def build():
    part1 = ('<article class="page" id="t148"><span class="page-no">Учебник, с. 148</span>'
             '<h2>Grammar reference: Comparing the past with now</h2>'
             '<p><a href="theory.html#gr148">Правило — в разделе «Теория»</a></p>' + gr1() + gr2() +
             gloss(148, (405, 915, 720, 1040)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 64–69</span>'
             '<h2>Итоговый тест по модулю 9</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.features("t9-f1", "1", "Which of these things can you see in the picture of the house on p. 64?") +
             X.meanings("t9-f2", "2", "Choose the meanings of the words in <b>bold</b>.") +
             X.endings("t9-f3", "3", "Complete the sentences from <i>Listening</i> 9.1 (Gavin and Lynn).") +
             X.sizes("t9-f4", "4") +
             X.true_false("t9-f5", "5", "Are these sentences about the article <i>Priced out of the market</i> true or false?") +
             X.article_e("t9-f6", "6", "Complete the sentences with words from the article.") +
             X.areas("t9-f7", "7") + X.compare("t9-f8", "8", "Complete the sentences from <i>Listening</i> 9.3.") +
             X.rules("t9-f9", "9") + "</article>")
    toc = '<nav class="toc"><a href="#t148">Grammar reference</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part1 + final
