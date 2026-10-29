"""Страница «Тесты»: упражнения Grammar reference p. 152 (ключи — Grammar Reference, 13) и итоговый тест."""
from lib import G, C, EX, OL, REVEAL
from . import shared as X


def tc1():
    items = [("If you’d asked me earlier, I could come yesterday, but I didn’t have time to rearrange my meeting.",
              "I could have come"),
             ("If we would set off at nine, we would’ve missed the rush hour.", "If we had (set off)"),
             ("It would’ve been worse if she wasn’t wearing a seatbelt.", "If she hadn’t been wearing"),
             ("I don’t know what I would’ve did if I hadn’t come here.", "I would’ve done"),
             ("If it hadn’t been for that long journey, we might never have got to know each other.", "correct"),
             ("If there’d been a traffic jam, I might’ve got there on time.", "If there hadn’t been"),
             ("We wouldn’t have got lost if we’d given better directions by the conference organisers.", "If we’d been given"),
             ("I wouldn’t be alive today if I hadn’t had that operation.", "correct")]
    return EX("t13-tc1", "1", "Correct the six mistakes in the sentences below. Mark each sentence as correct or wrong.",
              OL([f"{s}<br>{C('Correct' if k == 'correct' else 'Wrong', 'Correct', 'Wrong')}" +
                  ("" if k == "correct" else REVEAL(k, "Исправление (ключ)")) for s, k in items]))


def tc2():
    rows = [f"I {G('would have called')} you last night if I {G('had had')} your number. (call, had)",
            f"I {G('would have come')} if I {G('had known')} she was going to be here. (come, know)",
            f"If you {G('hadn’t left')} your bag in such a stupid place, I {G('wouldn’t have tripped')} over it. (leave, trip)",
            f"If he {G('had paid')} more attention instead of talking on his mobile, he {G('wouldn’t have crashed')}. "
            "(pay, crash)",
            f"If there hadn’t been so much traffic, I {G('would have caught')} that plane which crashed, and I "
            f"{G('wouldn’t be')} alive today! (catch, be)"]
    return EX("t13-tc2", "2", "Complete the sentences with the verbs in brackets.", OL(rows))


def sh1():
    rows = [("It’s crazy! They {} let so many people onto the ferry.", "should never have", "should’ve"),
            ("Look at the traffic! I knew we {} taken the train.", "should’ve", "shouldn’t have"),
            ("I don’t know whose fault it is, but we {} been told earlier about the change.", "should’ve", "shouldn’t have"),
            ("It’s my own fault. I {} tried to overtake on a blind corner.", "shouldn’t have", "should’ve"),
            ("It’s your own fault. You {} been watching where you were going!", "should’ve", "shouldn’t have"),
            ("It’s my fault. I {} been so stupid.", "shouldn’t have", "should’ve")]
    return EX("t13-sh1", "1", "Choose the correct form.",
              OL([t.format(C(a, "should’ve", "should never have" if i == 0 else "shouldn’t have"))
                  for i, (t, a, b) in enumerate(rows)]))


def sh2():
    rows = [("We didn’t set off early enough.", "We {} earlier.", "should’ve set off|should have set off"),
            ("I wish I hadn’t left it till the last minute.", "I {} till the last minute.",
             "shouldn’t have left it|should not have left it"),
            ("It’s a shame you didn’t get here earlier. It was great.", "You {}. It was great.",
             "should’ve got here earlier|should have got here earlier"),
            ("I wish we hadn’t gone there. It was a rip-off.", "We {} somewhere else. It was a rip-off.",
             "should’ve gone|should have gone"),
            ("I could’ve helped if you’d told me.", "You {} me you needed help.", "should’ve told|should have told"),
            ("If you hadn’t been in such a rush, you wouldn’t have crashed.", "You {} in such a rush.",
             "shouldn’t have been|should not have been")]
    return EX("t13-sh2", "2", "Rewrite the sentences using <i>should have / shouldn’t have</i>.",
              OL([f"{a}<br>{b.format(G(k))}" for a, b, k in rows]))


def build():
    part1 = ('<article class="page" id="t152a"><span class="page-no">Учебник, с. 152</span>'
             '<h2>Grammar reference: Third conditionals</h2>'
             '<p><a href="theory.html#gr152">Правило — в разделе «Теория»</a></p>' + tc1() + tc2() + "</article>")
    part2 = ('<article class="page" id="t152b"><span class="page-no">Учебник, с. 152</span>'
             '<h2>Grammar reference: Should have</h2>'
             '<p><a href="theory.html#gr152">Правило — в разделе «Теория»</a></p>' + sh1() + sh2() + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 92–97, 132–133</span>'
             '<h2>Итоговый тест по модулю 13</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.travel_sort("t13-f1", "1") + X.travel_nouns("t13-f2", "2") + X.phrasal("t13-f3", "3") +
             X.particles("t13-f4", "4") + X.third_box("t13-f5", "5", "Complete the explanation of third conditionals with one "
                                                                    "word in each space.") +
             X.third_match("t13-f6", "6") + X.strong_match("t13-f7", "7") +
             X.mistakes("t13-f8", "8", "Complete the phrases from <i>Listening</i> 13.3 about the mistakes each person made.") +
             X.blame("t13-f9", "9") + X.trends("t13-f10", "10") + X.as_such("t13-f11", "11") + "</article>")
    toc = ('<nav class="toc"><a href="#t152a">Third conditionals</a><a href="#t152b">Should have</a>'
           '<a href="#final">Итоговый тест</a></nav>')
    return toc + part1 + part2 + final
