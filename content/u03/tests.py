"""Страница «Тесты»: упражнения Grammar reference pp. 140–141 (ключи — Grammar Reference, 03) и итоговый тест."""
from lib import G, EX, OL, DLG, REVEAL
from ocrtext import lines, fixed, _fix
from . import shared as X


def pp1():
    items = [("Have you read <i>The Shadow of the Wind</i>?", "No, I haven’t, but it’s supposed to good. Is it?",
              "supposed to be good"),
             ("Have you discussed the problem with Matt?", "Yeah, he’s actually rung me about ten minutes ago to talk about it.",
              "he actually rang me"),
             ("Have you been to that new market yet?", "Yes, I have, actually. I’ve been shopping there yesterday – and guess "
              "what? I bumped into Rick while I was there.", "I went shopping there yesterday"),
             ("We went to see the musical <i>We Will Rock You</i> last night. Have you seen it?",
              "No, but I like to. I’ve heard it’s really good.", "No, but I’d like to"),
             ("We went to that Italian restaurant round the corner. Have you eaten there yet?", "No. What it’s like?",
              "No, (I haven’t), what’s it like?"),
             ("Have you ever done a parachute jump?", "No never, but I always want to ever since I was a kid.",
              "I’ve always wanted to"),
             ("Have you ever been to that fish restaurant on the high street?",
              "Yeah! I went there loads of times. It’s one of my favourite restaurants.", "I’ve been there"),
             ("Have you ever been to Seoul?", "No, but I’ll go there next week.", "I’m going there")]
    return EX("t3-pp1", "1", "Correct the mistakes in B’s answers.",
              OL([DLG(("A", a), ("B", b)) + REVEAL(k, "Исправление (ключ)") for a, b, k in items]))


def pp2():
    W = lambda a: G(a, "wide")
    rows = [DLG(("A", "I went to that bar in Hanway Street last night. " + W("Have you been there?") + " (you / be there)"),
                ("B", "Yeah, of course. " + W("I’ve been there lots of times.") + " (I / be there / lots / times)")),
            DLG(("A", W("Did you tell Agnes we’re going out?|Have you told Agnes we’re going out?") +
                 " She might want to come. (you / tell Agnes / we / go out)"),
                ("B", "Yeah, " + W("I spoke to her this afternoon.") + " She said she can’t come. (speak / her this afternoon)")),
            DLG(("A", W("Have you ever eaten wild boar?") + " (eat / wild boar)?"),
                ("B", "No, " + W("have you?") + " (you)"),
                ("A", "No, but " + W("I think I’ll order it for my main course. It’s supposed to be nice.|"
                                     "I think I’m going to order it for my main course. It’s supposed to be nice.") +
                 " (I / think / order it / my main course. / it / supposed / nice)")),
            DLG(("A", W("Have you seen the new Bond film?") + " (you / see / new Bond film)"),
                ("B", "No, " + W("I’m actually going to see it on Sunday.") + ", so don’t tell me too much about it. "
                 "(I / actually / go / see it / Sunday)"))]
    return EX("t3-pp2", "2", "Complete the dialogues by putting the words in brackets into the correct form.", OL(rows))


def fut1():
    d = DLG(("A", "What are you doing today?"),
            ("B", f"I think we’re <sup>1</sup>{G('going')} to go to the Roman ruins outside town and after that, I’m not sure. "
                  f"We <sup>2</sup>{G('might')} just go to the beach. I <sup>3</sup>{G('will')} probably be bored of sightseeing "
                  f"by then, but it <sup>4</sup>{G('depends')} on my husband – he might have other plans. What about you? "
                  "What are you doing?"),
            ("A", f"Well, we <sup>5</sup>{G('are')} leaving tomorrow."), ("B", "Already?"),
            ("A", f"Yes, unfortunately. I’ve got to go back and study, I’ve <sup>6</sup>{G('got')} some important exams in "
                  "September."),
            ("B", "Poor you."),
            ("A", f"Oh it’s OK. Anyway, we’re <sup>7</sup>{G('going')} to the main square and the market down there. We saw "
                  "some nice handicrafts, which we thought we’d take back as souvenirs and presents. Hopefully, we "
                  f"<sup>8</sup>{G('will')} have time to go to the beach one last time, though. I don’t want to spend all day "
                  "shopping!"),
            ("B", f"Well, in that case, we <sup>9</sup>{G('might')} see you down there."))
    return EX("t3-fu1", "1", "Complete the conversation below with one word in each gap.", d)


def gloss(p, box):
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip().replace(" - ", " – ")
        if t.startswith("Glossary") or set(t) <= set(". "):
            continue
        head = t.split(":", 1)[0]
        if ":" in t and len(head) < 30 and head[:1].islower():
            out.append([head, t.split(":", 1)[1].strip()])
        elif out:
            out[-1][1] += " " + t
    return '<div class="glossary"><h4>Glossary</h4>' + "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in out) + "</div>"


def build():
    part1 = ('<article class="page" id="t140"><span class="page-no">Учебник, с. 140</span>'
             '<h2>Grammar reference: Present perfect questions</h2>'
             '<p><a href="theory.html#gr140">Правило — в разделе «Теория»</a></p>' + pp1() + pp2() +
             gloss(140, (405, 855, 720, 1030)) + "</article>")
    part2 = ('<article class="page" id="t141"><span class="page-no">Учебник, с. 141</span>'
             '<h2>Grammar reference: The future</h2>'
             '<p><a href="theory.html#gr141">Правило — в разделе «Теория»</a></p>' + fut1() +
             gloss(141, (445, 795, 745, 890)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 20–25, 124–125</span><h2>Итоговый тест по модулю 3</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.places("t3-f1", "1") + X.preps("t3-f2", "2") + X.recommend("t3-f3", "3", "Complete the sentences from "
                                                                          "<i>Listening</i> 3.1 (tourist and receptionist).") +
             X.conv_order("t3-f4", "4") + X.problems("t3-f5", "5") +
             X.numbers("t3-f6", "6", "What do these numbers in the article <i>Workers Can’t Bank on Holidays</i> refer to?") +
             X.weather("t3-f7", "7") + X.future_match("t3-f8", "8") + X.future_gaps("t3-f9", "9") +
             X.story_order("t3-f10", "10", "Put the sentences from the story <i>It was dangerous, but I knew I had to do it</i> "
                           "in order.") +
             X.just_match("t3-f11", "11") + X.just_rewrite("t3-f12", "12") + X.verbs_match("t3-f13", "13") +
             X.verbs_gaps("t3-f14", "14") + "</article>")
    toc = ('<nav class="toc"><a href="#t140">Present perfect questions</a><a href="#t141">The future</a>'
           '<a href="#final">Итоговый тест</a></nav>')
    return toc + part1 + part2 + final
