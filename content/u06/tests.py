"""Страница «Тесты»: упражнения Grammar reference p. 145 (ключи — Grammar Reference, 06) и итоговый тест."""
from lib import G, EX, OL
from . import shared as X

M_BOX = ["ask", "get", "keep", "forget", "reply", "remember", "visit", "let", "tell", "buy"]


def mu1():
    rows = [f"I really must {G('visit')} China sometime soon. It just looks amazing.",
            f"I must {G('get')} a haircut sometime soon. It’s getting long!",
            f"That reminds me. I must {G('ask')} someone in my class if I can borrow their notes from the lesson I missed "
            "yesterday.",
            f"Remind me later I must {G('reply')} to Milo’s email.",
            f"I must {G('remember')} to give you back that CD you lent me.",
            f"Whatever I do, I mustn’t {G('forget')} to take the tickets with me!",
            f"I should go. I mustn’t {G('keep')} my friends waiting.",
            f"I must just {G('let')} my boss know I can’t attend the meeting tomorrow.",
            f"I really mustn’t {G('buy')} anything else on the Internet for a while. I don’t want to go into overdraft.",
            f"I must just {G('tell')} you what happened to me while I was shopping yesterday. You won’t believe it!"]
    return EX("t6-mu1", "1", "Complete the sentences with the verbs in the box.", X.wordbox(M_BOX) + OL(rows))


SOFT = [("You mustn’t pay the first price they ask. (don’t)", "Don’t pay the first price they ask."),
        ("You must take out travel insurance. (If / you / would)", "If I were you, I would take out travel insurance.|"
         "If I were you, I’d take out travel insurance.|I would take out travel insurance if I were you.|"
         "I’d take out travel insurance if I were you."),
        ("You must pay in cash, I’m afraid. (have to)", "I’m afraid you have to pay in cash.|You have to pay in cash, I’m afraid."),
        ("You mustn’t smoke in the building. (allowed)", "You’re not allowed to smoke in the building.|"
         "You aren’t allowed to smoke in the building."),
        ("You mustn’t make any personal calls from the office. (supposed)",
         "You’re not supposed to make any personal calls from the office.|"
         "You aren’t supposed to make any personal calls from the office."),
        ("You must wear a suit to the meeting instead of those old jeans. (be better)",
         "You’d be better off wearing a suit to the meeting instead of those old jeans.|"
         "You would be better off wearing a suit to the meeting instead of those old jeans."),
        ("You must change some money before you go. The rates are much better here. (be better)",
         "You’d be better off changing some money before you go. The rates are much better here.|"
         "You’d be better off changing some money before you go.")]


def mu2():
    return EX("t6-mu2", "2", "Rewrite the sentences using the words in brackets so that they sound softer and more polite, as in "
              "the example.", '<p class="ex-line">You mustn’t go there. It’s too expensive! (wouldn’t / if / you)<br>'
              '<i>I wouldn’t go there if I were you. It’s too expensive.</i></p>' +
              OL([f"{q}<br>{G(a, 'wide')}" for q, a in SOFT], start=2))


def build():
    part1 = ('<article class="page" id="t145"><span class="page-no">Учебник, с. 145</span>'
             '<h2>Grammar reference: <i>must</i></h2>'
             '<p><a href="theory.html#gr145">Правило — в разделе «Теория»</a></p>' + mu1() + mu2() + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 42–47, 130–131</span>'
             '<h2>Итоговый тест по модулю 6</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.souvenir_groups("t6-f1", "1") + X.souvenirs("t6-f2", "2") +
             X.phones("t6-f3", "3", "Complete the table about the two phones (<i>Listening</i> 6.2).") +
             X.phone_fix("t6-f4", "4") + X.ones("t6-f5", "5") + X.odd_one("t6-f6", "6") + X.must_rules("t6-f7", "7") +
             X.must_uses("t6-f8", "8") + X.must_gaps("t6-f9", "9") + X.rec_order("t6-f10", "10") +
             X.facilities("t6-f11", "11") + X.referring("t6-f12", "12") + "</article>")
    toc = '<nav class="toc"><a href="#t145">must</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part1 + final
