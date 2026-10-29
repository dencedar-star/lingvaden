"""Страница «Тесты»: упражнения Grammar reference p. 154 (ключи — Grammar Reference, 15) и итоговый тест."""
from lib import G, C, EX, OL, DLG
from ocrtext import lines, fixed, _fix
from . import shared as X


def rs1():
    rows = [DLG(("A", "He’s suffering from depression."),
                ("B", f"Really? He told me he {G('suffers|suffered')} from a hormonal condition.")),
            DLG(("A", "She’s having an operation to sort out the problem."),
                ("B", f"I thought she said she {G('had had')} one already.")),
            DLG(("A", "He’s looking really well, isn’t he?"),
                ("B", f"I know, it’s amazing! The doctors told him it {G('would take')} him years to recover.")),
            DLG(("A", "He’s got his final exams next month."), ("B", f"I thought he said he {G('had taken')} them already.")),
            DLG(("A", "I feel guilty because we didn’t help."),
                ("B", f"You shouldn’t. We did offer, but he said he {G('would be')} fine.")),
            DLG(("A", "Can you pass me the sugar?"),
                ("B", f"I thought the doctor said you {G('shouldn’t take|should not take|couldn’t take|weren’t to take')} sugar "
                      "in your coffee anymore."))]
    return EX("t15-rs1", "1", "Complete the reported speech by adding the verbs in the box in the correct form. You may need to "
              "use a modal verb.", X.wordbox(["be", "have", "qualify", "not want", "take", "suffer"]) + OL(rows))


def rs2():
    rows = [("I’m not surprised you’re ill. I did {} you not eat the food at that place!", "warn", "threaten"),
            ("My dad has finally {} to go and have a check-up at the doctor’s.", "agreed", "insisted"),
            ("My dentist {} me to start brushing my tongue – as well as my teeth!", "told", "suggested"),
            ("The doctor {} that I cut down on salt and caffeine.", "recommended", "said"),
            ("I’ve finally managed to {} my grandmother to get a hearing aid!", "persuade", "advise"),
            ("My girlfriend has {} to leave me unless I stop smoking.", "threatened", "offered"),
            ("You {} to pick up my prescription for me! How could you forget?", "promised", "suggested"),
            ("I asked if I could be moved to another hospital, but they {} to even talk about it!", "refused", "denied")]
    order = [("warn", "threaten"), ("insisted", "agreed"), ("suggested", "told"), ("said", "recommended"),
             ("advise", "persuade"), ("threatened", "offered"), ("promised", "suggested"), ("refused", "denied")]
    return EX("t15-rs2", "2", "Choose the correct verb.", OL([t.format(C(a, *o)) for (t, a, _), o in zip(rows, order)]))


def gloss(p, box):
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip()
        if t.startswith("Glossary") or set(t) <= set(". "):
            continue
        head = t.split(":", 1)[0]
        if ":" in t and len(head) < 30 and head[:1].islower():
            out.append([head, t.split(":", 1)[1].strip()])
        elif out:
            out[-1][1] += " " + t
    return '<div class="glossary"><h4>Glossary</h4>' + "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in out) + "</div>"


def build():
    part1 = ('<article class="page" id="t154"><span class="page-no">Учебник, с. 154</span>'
             '<h2>Grammar reference: Reported speech, reporting verbs</h2>'
             '<p><a href="theory.html#gr154">Правило — в разделе «Теория»</a></p>' + rs1() + rs2() +
             gloss(154, (400, 870, 702, 1058)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 104–109</span>'
             '<h2>Итоговый тест по модулю 15</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.comments("t15-f1", "1") + X.any_q("t15-f2", "2") +
             X.myths("t15-f3", "3", "Are these statements true or myths, according to the website <i>Fact or myth?</i>") +
             X.forms("t15-f4", "4") + X.causes("t15-f5", "5") + X.accidents("t15-f6", "6") +
             X.events("t15-f7", "7", "Put the events from Dan’s story (<i>Listening</i> 15.2) in order.") +
             X.past_forms("t15-f8", "8") + "</article>")
    toc = '<nav class="toc"><a href="#t154">Reported speech</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part1 + final
