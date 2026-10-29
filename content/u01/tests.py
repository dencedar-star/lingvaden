"""Страница «Тесты»: упражнения Grammar reference pp. 136–137 (ключи — Grammar Reference, 01) и итоговый тест."""
from lib import G, S, EX, OL, DLG
from . import shared as X

QW = list("abcdefghi")


def qf1():
    rows = [G("Where") + " are you working these days?", G("Why") + " are you laughing?",
            G("What") + " are you going to do after the course?",
            G("Who") + "’s going to look after your cats while you’re away?", G("Whose") + " coat is this?",
            G("How") + " " + G("often") + " do you visit your grandparents?",
            G("What") + " " + G("time") + " did you go to bed last night?",
            G("How") + " " + G("much") + " did you pay for your car?",
            G("How") + " " + G("long") + " have you been playing the guitar?"]
    return EX("t-qf1", "1", "Complete the questions with the correct question words.", OL(rows))


def qf2():
    qs = ["… are you working these days?", "… are you laughing?", "… are you going to do after the course?",
          "…’s going to look after your cats while you’re away?", "… coat is this?",
          "… do you visit your grandparents?", "… did you go to bed last night?", "… did you pay for your car?",
          "… have you been playing the guitar?"]
    key = "i d a f e h b c g".split()
    ans = ["I don’t really know. I still haven’t really decided yet.", "I can’t remember, but I know it was late!",
           "I got it second-hand. It was £2,000.", "It’s nothing. I just suddenly remembered something. Sorry!",
           "Oh, thanks. It’s mine. I almost forgot that!", "A friend is going to come every day and feed them.",
           "Well, I started in 1990, so it’s nearly 20 years now.", "Not as often as I should! Maybe twice a year.",
           "I’m still at the same place I was at last time, actually."]
    return EX("t-qf2", "2", "Match the questions 1–9 in exercise 1 with the answers a–i.",
              OL([f"{q} → {S(k, QW)}" for q, k in zip(qs, key)]) + OL(ans, "items alpha"))


def qf3():
    rows = [
        (("A", "What kind of films you like?"), ("B", "Anything really. The only films I don’t like are musicals and anything which is dubbed."),
         "What kind of films do you like?"),
        (("A", "How’s your part-time job go at the moment?"), ("B", "Better thanks. I’m quite enjoying it now."),
         "How’s your part-time job going at the moment?|How is your part-time job going at the moment?"),
        (("A", "You’re good at this. Did you play before?"), ("B", "No, I haven’t. It must just be beginners’ luck!"),
         "Have you played before?"),
        (("A", "Do you work on any projects at the moment?"), ("B", "Not really. It’s been quite boring at work recently."),
         "Are you working on any projects at the moment?"),
        (("A", "Are you decided where you’re going on holiday?"), ("B", "Yes, Sicily."),
         "Have you decided where you’re going on holiday?"),
        (("A", "How long is he learning Chinese, then?"), ("B", "I think about 6 years. You’ll have to ask him."),
         "How long has he been learning Chinese, then?"),
        (("A", "How did you and your wife first met?"), ("B", "That’s a long story!"),
         "How did you first meet your wife?|How did you and your wife first meet?"),
    ]
    items = [DLG(a, b) + '<span style="font-size:14px;color:var(--ink2)">Исправленный вопрос:</span>' + G(k, "wide")
             for a, b, k in rows]
    return EX("t-qf3", "3", "Correct the mistakes in all the questions in 1–7.", OL(items))


def nt1():
    starts = ["I was really surprised he failed the exam because", "I asked them to turn the music down because",
              "He didn’t post the letter because", "He didn’t post the letter, even though",
              "We were running out of petrol, so", "We ran out of petrol, so",
              "When she told us she was thinking of becoming a model,", "I think she got upset because",
              "By the time we got there, the show had already started, so", "When we got there, the show was just starting, so",
              "I met my girlfriend while", "I met my girlfriend and then"]
    ends = [("we had to look for a garage.", "5|6"), ("he’d studied a lot.", "1"), ("we went to a friend’s for dinner.", "12"),
            ("we didn’t really miss much.", "10"), ("I’d reminded him at least three times.", "4"),
            ("we were laughing at her.", "8")]
    nums = [str(i) for i in range(1, 13)]
    return EX("t-nt1", "1", "Match sentence endings a–f to six of the sentence starters 1–12.",
              OL(starts) + OL([f"{S(k, nums)} … {t}" for t, k in ends], "items alpha"))


def nt2():
    s1 = ("This embarrassing thing <sup>1</sup>" + G("happened") + " (happen) to me last week. I <sup>2</sup>" + G("went") +
          " (go) to the cinema with my best friend and her new boyfriend, who I <sup>3</sup>" + G("had never met") +
          " (never/meet) before. Anyway, we <sup>4</sup>" + G("were watching") + " (watch) a horror movie and my friend and I "
          "usually reach for each other’s hands when a scary part comes on. At one point, I <sup>5</sup>" + G("tried") +
          " (try) to grab my friend’s hand – but I <sup>6</sup>" + G("grabbed") + " (grab) her boyfriend’s instead! I felt awful about it!")
    s2 = ("It was really stupid. I <sup>7</sup>" + G("was walking") + " (walk) along the road, and I <sup>8</sup>" + G("saw") +
          " (see) a man arguing with a woman on the other side of the road, and I <sup>9</sup>" + G("stared") +
          " (stare) at them, not looking where <sup>10</sup>" + G("I was going") + " (go) and I <sup>11</sup>" + G("walked") +
          " (walk) straight into a box which someone <sup>12</sup>" + G("had left") + " (left) in the street. I <sup>13</sup>" +
          G("fell over") + " (fall over) and I <sup>14</sup>" + G("hit") + " (hit) my head really hard. The man and the woman <sup>15</sup>" +
          G("stopped") + " (stop) arguing and <sup>16</sup>" + G("started") + " (start) laughing at me. I felt like such an idiot!")
    return EX("t-nt2", "2", "Complete the stories by putting the verbs in the brackets into the correct tense.",
              f'<div class="story"><p><b>1</b> {s1}</p><p><b>2</b> {s2}</p></div>')


GLOSS136 = [("be away", "if someone is away, they are in a different town or country on business or on holiday"),
            ("second-hand", "something which someone else owned before"), ("feed", "if you feed something, you give it food"),
            ("dubbed", "if an American film is dubbed, the actors speak in a different language to English. They are dubbed into French, etc")]
GLOSS137 = [("run out of", "if you run out of something, you use it and so you have no more of it"),
            ("get upset", "if you get upset, you get angry or sad"), ("grab", "if you grab something, you take it in a quick, sudden way"),
            ("stare", "if you stare at something, you look for a long time at it")]


def gloss(rows):
    return '<div class="glossary"><h4>Glossary</h4>' + "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in rows) + "</div>"


def build():
    part1 = ('<article class="page" id="t136"><span class="page-no">Учебник, с. 136</span><h2>Grammar reference: Question formation</h2>'
             '<p><a href="theory.html#gr136">Правило — в разделе «Теория»</a></p>' + qf1() + qf2() + qf3() + gloss(GLOSS136) + "</article>")
    part2 = ('<article class="page" id="t137"><span class="page-no">Учебник, с. 137</span><h2>Grammar reference: Narrative tenses</h2>'
             '<p><a href="theory.html#gr137">Правило — в разделе «Теория»</a></p>' + nt1() + nt2() + gloss(GLOSS137) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 8–13, 121</span><h2>Итоговый тест по модулю 1</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.qform("t-f1", "1") + X.listen_choice("t-f2", "2", "Choose the correct words (Listening 1.1).") +
             X.dc_match("t-f3", "3") + X.reading_tf("t-f4", "4", "Decide if these sentences about the article on p. 10 are true or false.") +
             X.reading_words("t-f5", "5", "Match the words from the article with their meanings.") +
             X.story_gaps("t-f6", "6", "Complete Brian Willis’ story by putting the verbs in the correct tense.") +
             X.tense_usage("t-f7", "7") + X.past_cont("t-f8", "8") + X.writing_order("t-f9", "9") + "</article>")
    toc = ('<nav class="toc"><a href="#t136">Question formation</a><a href="#t137">Narrative tenses</a>'
           '<a href="#final">Итоговый тест</a></nav>')
    return toc + part1 + part2 + final
