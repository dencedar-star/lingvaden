"""Страница «Тесты»: упражнения Grammar reference p. 147 (ключи — Grammar Reference, 08) и итоговый тест."""
from lib import G, EX, OL
from ocrtext import FIX
from u03.tests import gloss
from . import shared as X

FIX.setdefault(147, []).extend([("something. you", "something, you")])


def dv(s):
    """Вариант ответа с полной формой would вместо ’d."""
    return s + "|" + s.replace("’d ", " would ") if "’d " in s else s


def tend1():
    """tend to, Exercise 1. Ключ: 1 tend to 2 tend not to / don’t tend to 3 have tended to 4 didn’t tend to / tended not to
    5 have tended not to 6 tended to."""
    rows = [f"I don’t like cooking, so I {G('tend to')} eat out a lot.",
            f"I try to eat as healthily as I can and I {G('tend not to|don’t tend to')} eat fatty or fried things, if I can help it.",
            f"I had a bad experience with oysters a few years ago and I {G('have tended to|’ve tended to')} avoid them ever since then!",
            f"When I was a kid, I {G('didn’t tend to|tended not to')} eat much foreign food, but I’ve become much more adventurous "
            "as I’ve got older.",
            f"There was a big news story about mad cow disease a few years ago and since then I {G('have tended not to|’ve tended not to')}"
            " eat much beef!",
            f"Even before I became a vegetarian, I {G('tended to')} eat a lot less meat than the rest of my family."]
    return EX("t8-g1", "1", "Complete the sentences with the correct positive or negative forms.", OL(rows))


SC = [("I will really miss eating fried chicken if I were a vegetarian!",
       dv("I’d really miss eating fried chicken if I were a vegetarian!") + "|I would really miss eating fried chicken if I was a vegetarian!"),
      ("You’d be in trouble if you had to use chopsticks all the time!", dv("You’d be in trouble if you had to use chopsticks all the time!")),
      ("I wouldn’t eat tripe even if you’d pay me!", "I wouldn’t eat tripe even if you paid me!"),
      ("You might lose weight if you didn’t drink so much!", "You might lose weight if you didn’t drink so much!"),
      ("They would can make more money if they started stocking more foreign food.",
       dv("They’d make more money if they started stocking more foreign food.")),
      ("If I would be better at cooking, I might invite people round for dinner more often.",
       "If I were better at cooking, I might invite people round for dinner more often.|"
       "If I was better at cooking, I might invite people round for dinner more often."),
      ("I’d be happy to pay for dinner sometimes – if you wanted me to!",
       dv("I’d be happy to pay for dinner sometimes – if you wanted me to!") + "|" +
       dv("I’d be happy to pay for dinner sometimes if you wanted me to!")),
      ("I would go crazy if I had to go on a diet!", dv("I’d go crazy if I had to go on a diet!")),
      ("I wouldn’t ask you if I wouldn’t really need your help.", "I wouldn’t ask you if I didn’t really need your help."),
      ("If I am you, I’d just do what it tells you to do in the book.",
       dv("If I were you, I’d just do what it tells you to do in the book.") + "|" +
       dv("If I was you, I’d just do what it tells you to do in the book."))]


def second1():
    """Second conditionals, Exercise 1. Ключ: 1 would really 2 correct 3 if you paid me 4 correct 5 would make more 6 If I were
    better at 7 correct 8 correct 9 I didn’t really need 10 If I were / was you."""
    return EX("t8-g2", "2", "Decide which six sentences are incorrect. Write all the sentences correctly (copy the correct ones).",
              OL([f"{q}<br>{G(a, 'wide')}" for q, a in SC]))


def second2():
    """Second conditionals, Exercise 2. Ключ: 1 was / were, would cancel 2 was / were, might enjoy 3 would come, wasn’t / weren’t
    4 would be, was 5 wasn’t / weren’t, would try 6 wasn’t / weren’t working, would love."""
    w = lambda v: G(f"would {v}|’d {v}")
    rows = [f"I’d love to come tonight, but I’m afraid I have to take an important client out to dinner. If it {G('was|were')} "
            f"(be) anyone else, I {w('cancel')} (cancel) it, but I really can’t. Sorry.",
            f"It’s not really my kind of place, to be honest. Perhaps if I {G('was|were')} (be) a bit younger, I "
            f"{G('might enjoy')} (enjoy) it, but it’s just a bit too trendy for me now.",
            f"Thank you so much for inviting me to dinner, but I’m afraid there’s no way I can make it. I {w('come')} (come) if I "
            f"{G('wasn’t|weren’t')} (not / be) so busy at the moment, but I honestly don’t have the time.",
            f"I {w('be')} (be) happy to have the party at our place if our flat {G('was|were')} (be) a bit bigger.",
            f"I’d love to come out with you tonight, but I really can’t. If I {G('wasn’t|weren’t')} (not / be) so broke at the "
            f"moment, I {w('try')} (try) to come along, but I really can’t afford to.",
            f"Bill said sorry, but he’s not going to be able to come tonight. He said that if he {G('wasn’t working|weren’t working')}"
            f" (not / work), he {w('love')} (love) to come, but there’s no way he can get out of it."]
    return EX("t8-g3", "3", "Complete 1–6 by putting the verbs in brackets into the correct form.", OL(rows))


def build():
    part1 = ('<article class="page" id="t147"><span class="page-no">Учебник, с. 147</span>'
             '<h2>Grammar reference: tend to · Second conditionals</h2>'
             '<p><a href="theory.html#gr147">Правило — в разделе «Теория»</a></p>' + tend1() + second1() + second2() +
             gloss(147, (455, 830, 794, 1040)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 54–59, 134–135</span>'
             '<h2>Итоговый тест по модулю 8</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.cooking("t8-f1", "1", "Which of the ways of cooking can you see in the picture of the kitchen (p. 54)?") +
             X.orders("t8-f2", "2", "Which dishes does Claes decide to order in <i>Listening</i> 8.1?") +
             X.listen81("t8-f3", "3", "Complete the sentences from <i>Listening</i> 8.1 (Aurora and Claes).") +
             X.words_c("t8-f4", "4", "Complete the sentences about the texts <i>Food for thought</i>.") +
             X.tend("t8-f5", "5") + X.restaurants("t8-f6", "6", "Choose the words that were used in the conversations in "
                                                                 "<i>Listening</i> 8.2.") +
             X.over("t8-f7", "7") + X.second_rule("t8-f8", "8", "Complete the explanation of the second conditional.") +
             X.second_c("t8-f9", "9") + X.films_a("t8-f10", "10") + X.films_b("t8-f11", "11") +
             X.while_during("t8-f12", "12") + X.after_noun("t8-f13", "13") + "</article>")
    toc = '<nav class="toc"><a href="#t147">Grammar reference</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part1 + final
