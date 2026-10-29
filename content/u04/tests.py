"""Страница «Тесты»: упражнения Grammar reference pp. 142–143 (ключи — Grammar Reference, 04) и итоговый тест."""
from lib import G, EX, OL, DLG
from ocrtext import lines, fixed, _fix
from . import shared as X

FREQ_FIX = [("Do you ever go swimming?", "No, hardly never. I don’t really like it.", "No, {}. I don’t really like it.",
             "hardly ever"),
            ("How often do you go out?", "Not much often. I’m very busy with my studies.", "{}. I’m very busy with my studies.",
             "Not very often|Not much"),
            ("Do you go and watch them play a lot?", "Yeah, basically once a two weeks.", "Yeah, basically {}.",
             "once or twice a week|once every two weeks"),
            ("Do you ever go to art exhibitions?", "Yeah, sometimes. Probably twice or once a year.",
             "Yeah, sometimes. Probably {}.", "once or twice a year"),
            ("Can we meet on Tuesday evening?", "I’m sorry, I can’t. Always I go to my therapist on Tuesdays.",
             "I’m sorry, I can’t. {} to my therapist on Tuesdays.", "I always go"),
            ("So how often do you go walking?", "Whenever I will get the chance.", "{}.", "Whenever I get the chance"),
            ("Do you go to the gym a lot?", "Not as much how I should.", "{}.", "Not as much as I should"),
            ("Do you do much sport?", "Not as much as I used. I had a foot injury for a while which stopped me.",
             "Not as much as {}. I had a foot injury for a while which stopped me.", "I used to")]


def fr1():
    rows = [DLG(("A", a), ("B", f"<s>{b}</s>")) + "✔ " + c.format(G(k, "wide")) for a, b, c, k in FREQ_FIX]
    return EX("t4-fr1", "1", "Correct the mistake with the frequency expression in each of these dialogues.", OL(rows))


def fr2():
    rows = [f"When I was a kid, my parents {G('never let')} me stay out late. (never let)",
            f"My brother {G('goes')} swimming every morning before I get up. (go)",
            f"I {G('don’t see|do not see')} my parents as much as I used to, now that we’ve moved. (not see)",
            f"When I was at school, I always {G('studied|used to study')} really hard, but now I’m at university I "
            f"{G('don’t need|do not need')} to. (study, not need)",
            f"I {G('used to spend')} an hour in the gym every day, but I hardly ever {G('go')} now. That’s why I’m so unfit. "
            "(spend, go)"]
    return EX("t4-fr2", "2", "Complete these sentences by putting the verbs in brackets into a correct form.", OL(rows))


HL = [("I used to live in Munich, so I know it quite well.", "you / live", "How long did you live there?"),
      ("He’s very careful. It’s the first accident he’s ever had.", "he / drive",
       "How long has he been driving?|How long has he been driving for?"),
      ("It’s my parents’ wedding anniversary today.", "they / married", "How long have they been married?"),
      ("I’m finding work very tough. I’m thinking of leaving.", "you / work / there",
       "How long have you worked there?|How long have you been working there?"),
      ("She got divorced last year.", "she / married", "How long was she married?|How long was she married for?"),
      ("He’s probably my oldest friend.", "you / know each other", "How long have you known each other?"),
      ("Are you still on the phone to your mum?", "Yeah. Why? / we / talk", "Yeah? Why, how long have we been talking?|"
       "Yeah. Why? How long have we been talking?|How long have we been talking?"),
      ("Her German is pretty good already.", "she / learn", "How long has she been learning it?|How long has she been learning?|"
       "How long has she been learning German?"),
      ("It was a nightmare getting to the airport.", "it / take you / get there", "How long did it take you to get there?")]


def du1():
    return EX("t4-du1", "1", "Write <i>how long</i> questions in response to each of the following.",
              OL([f"{s}<br>{G(a, 'wide')} ({h})" for s, h, a in HL]))


FS_BOX = ["over six hundred years", "fifty years", "2004", "his heart attack", "most of my adult life", "a few weeks now",
          "I last wrote to you", "a couple of minutes"]


def du2():
    W = lambda a: G(a, "wide")
    rows = [f"He’s not here, I’m afraid. He’s just gone out {W('for a couple of minutes')}. Shall I ask him to call you back?",
            f"It’s my grandparents’ golden wedding anniversary today. They’ve been married {W('for fifty years')}!",
            f"He’s stopped smoking and changed his diet a lot {W('since his heart attack')}. He nearly died and that was obviously "
            "a real shock.",
            f"It’s quite a historic building. There’s been a church on this site {W('for over six hundred years')}.",
            f"We moved to England when I was 12 and I’ve been here ever since, so I’ve lived here {W('for most of my adult life')}.",
            f"I’ve been following the diet {W('for a few weeks now')} and I’m feeling much better. I’ve lost almost nine kilos "
            "already!",
            f"Dear Lorraine, I know it’s been a while {W('since I last wrote to you')}, but I think about you all the time.",
            f"There’s been a ban on smoking in pubs and cafés in Ireland {W('since 2004')}."]
    return EX("t4-du2", "2", "Complete each sentence by adding <i>for</i> or <i>since</i> and the most suitable time expression "
              "in the box.", X.wordbox(FS_BOX) + OL(rows))


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
    part1 = ('<article class="page" id="t142"><span class="page-no">Учебник, с. 142</span>'
             '<h2>Grammar reference: Frequency</h2>'
             '<p><a href="theory.html#gr142">Правило — в разделе «Теория»</a></p>' + fr1() + fr2() +
             gloss(142, (25, 845, 335, 1072)) + "</article>")
    part2 = ('<article class="page" id="t143"><span class="page-no">Учебник, с. 143</span>'
             '<h2>Grammar reference: Duration</h2>'
             '<p><a href="theory.html#gr143">Правило — в разделе «Теория»</a></p>' + du1() + du2() + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 26–31, 126–127</span>'
             '<h2>Итоговый тест по модулю 4</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.endings("t4-f1", "1") + X.freq("t4-f2", "2") + X.any_good("t4-f3", "3") +
             X.rika_tf("t4-f4", "4", "Decide if these sentences about the conversation between Ian and Rika (<i>Listening</i> "
                       "4.2) are true or false.") +
             X.sport_problems("t4-f5", "5") + X.dur_mistakes("t4-f6", "6", "Find the grammatical mistakes in these sentences "
                                                              "about Rika. Correct the mistakes.") +
             X.dur_rules("t4-f7", "7", "Complete the rules.") + X.dur_choose("t4-f8", "8") + X.how_long("t4-f9", "9") +
             X.music_order("t4-f10", "10") +
             X.readers("t4-f11", "11", "Which of the people in the article <i>The playlist of your life</i>:") +
             X.article_words("t4-f12", "12") + X.requests("t4-f13", "13") + X.emails("t4-f14", "14") +
             X.as_order("t4-f15", "15") + X.as_gaps("t4-f16", "16") + "</article>")
    toc = ('<nav class="toc"><a href="#t142">Frequency</a><a href="#t143">Duration</a>'
           '<a href="#final">Итоговый тест</a></nav>')
    return toc + part1 + part2 + final
