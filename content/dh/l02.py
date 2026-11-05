"""Desperate Housewives · Урок 2: At the wake (поминки Мэри Элис). Модальные глаголы в прошлом. Перенесён из ProgressMe."""
from lib import G, S, EX, OL, SEC, IMG, REVEAL, VOICE, WRITER, PLAYER, GAPS
from .l01 import SAY, info, vk_player, shadow_intro

N = "2"
TITLE = "At the wake"
LEAD = ("Соседки собираются на поминках Мэри Элис и пытаются понять, что с ней случилось. Слова go over, go through, "
        "can't face doing; модальные глаголы в прошлом: should have, must have, would have, could have.")
TOPICS = "Warm up · Vocabulary · Listening · Should have / Must have · Would have / Could have · Speaking · Dictation · Shadowing"
IMG_DIR = "../assets/img/dh-l02/"
VK = "https://vkvideo.ru/video_ext.php?oid=-51337713&id=456239207&hash=7c40b182f9f202c1&hd=3"
AUDIO = "/media/dh/l02.mp3"   # звук сцены целиком (0:49)
CLIP = {n: f"/media/dh/l02-{n}.mp3" for n in range(1, 6)}   # пять реплик сцены — для грамматики, диктанта и shadowing

SECTIONS = [("warm-up", "Warm up"), ("vocabulary", "Vocabulary"), ("listening", "Listening"), ("grammar", "Grammar: should / must have"),
            ("grammar-2", "Grammar 2: would / could have"), ("speaking", "Speaking"), ("dictation", "Dictation"), ("shadowing", "Shadowing")]

LINES = ["Susan, I was just saying Paul wants to go over on Friday.",
         "If Mary Alice was having problems she should have come to us, she should have let us help her.",
         "What kind of problems could she have had?",
         "No. If Mary Alice was having some sort of crisis we'd have known.",
         "Gabby, the woman killed herself. Something must have been going on."]

SCENE = [("Bree", "Susan! I was just saying Paul wants us to {go over} on Friday. He needs us to {go through} Mary Alice's {closet} "
                  "and help pack up her things. He said he {can't face doing} it by himself."),
         ("Gabby", "Sure, that's fine."),
         ("Bree", "Are you okay?"),
         ("Susan", "Yeah. I'm just so angry. If Mary Alice was having problems, she should have come to us. She should have let us "
                   "help her."),
         ("Gabby", "What kind of problems could she have had? She was healthy, had a great home, a nice family. Her life was…"),
         ("Lynette", "Our life."),
         ("Gabby", "No, if Mary Alice was having some sort of crisis, we'd have known. She lives 50 feet away, {for God's sakes}."),
         ("Susan", "Gabby, the woman killed herself. Something must have been going on.")]

VOCAB = [("to go over", "пойти к кому-то, зайти в гости", "I'm <b>going over</b> to Eddie's house, Mom — see you later!", "to visit some place"),
         ("to go through", "внимательно изучать, просматривать вещи",
          "I need to <b>go through</b> these old boxes in the attic to find my childhood photos.",
          "to look at or examine something thoroughly, often in a careful or methodical way"),
         ("closet", "шкаф", "He hung his jacket in the <b>closet</b> next to his shirts and trousers.",
          "a small room or enclosed space used for storing clothes or other items"),
         ("can't face doing", "не быть в состоянии заставить себя делать что-то",
          "After such a long day, I just <b>can’t face doing</b> the dishes tonight.",
          "to be unable to mentally or emotionally handle or accept the idea of doing something"),
         ("for God's sakes", "ради бога", "<b>For God’s sakes</b>, turn down the music! It’s midnight!",
          "an exclamation used to express frustration, surprise, or emphasis, often asking someone to do something urgently or "
          "pleadingly")]


def scene(mark):
    """Сцена; mark — 'u' (подчеркнуть слова урока), 'b' (жирным) или '' (без выделения)."""
    out = ""
    for sp, t in SCENE:
        for w in [x.split("}")[0] for x in t.split("{")[1:]]:
            t = t.replace("{" + w + "}", f"<{mark}>{w}</{mark}>" if mark else w)
        out += f'<p><b class="sp sp-{sp.lower()}">{sp}:</b> {t}</p>'
    return f'<div class="scene script-p">{out}</div>'


def rule(modal):
    opts = [modal, "past participle"]
    return f'<p>I/we/they/you/he/she/it {S(modal, opts)} + {S("past participle", opts)}</p>'


ANSWERS = ("1. Susan initially says, “Yeah. I’m just so angry,” rather than admitting she’s not okay. <i>(She masks her grief with "
           "anger.)</i><br>2. Paul, Mary Alice's husband, wants to organize packing the woman’s things on Friday. <i>(Evidence: “Paul "
           "wants to go over on Friday… help pack up her things.”)</i><br>3. Paul needs help because he “can’t face doing it by "
           "himself.” <i>(He’s emotionally unable to handle the task alone.)</i><br>4. Gabby says Mary Alice was “healthy, had a "
           "great home, a nice family” and lived nearby, so they’d have known if she was in crisis. <i>(She assumes outward signs of "
           "stability mean no hidden struggles.)</i><br>5. Susan concludes, “The woman killed herself. Something must have been going "
           "on.” <i>(She insists Mary Alice’s suicide implies unseen problems.)</i>")

# should have / must have: [подсказка/ответ]
SM_FILL = ["Mary Alice [come/should have come] to her friends if she was struggling. They would’ve helped her.",
           "The revolver was unused, so she [buy/must have bought] it recently. It looks old.",
           "Paul is devastated. We [help/should have helped] him pack Mary Alice’s things sooner.",
           "Gabby said, “We [know/should have known] about her crisis — we lived so close!”",
           "Susan thinks Mary Alice [hide/must have hidden] her pain very well."]
SM_REWRITE = [("Mary Alice didn’t ask for help, but it was the right thing to do.", "Mary Alice [should have asked] for help."),
              ("It’s obvious that she was suffering in silence.", "She [must have suffered/must have been suffering] in silence."),
              ("Paul didn’t check on her, and now he regrets it.", "Paul [should have checked] on her."),
              ("The neighbors didn’t notice anything strange, which is surprising.", "The neighbors [should have noticed] something strange."),
              ("The revolver was unused, so she probably bought it long ago.", "She [must have bought] the revolver long ago."),
              ("Gabby and Susan feel guilty because they didn’t realize Mary Alice was in pain.",
               "They [should have realized/should have realised] Mary Alice was in pain."),
              ("The fact that she killed herself means she was extremely desperate.", "She [must have been] extremely desperate."),
              ("It was irresponsible of them to ignore the warning signs.", "They [should have paid] attention to the warning signs."),
              ("The way she hid her feelings suggests she was a very private person.", "She [must have been] a very private person."),
              ("Her family didn’t support her, and that was a mistake.", "Her family [should have supported] her.")]
# would have / could have: [подсказка/ответ]
WC_TEXT = ("Mary Alice was feeling very lonely. She [reach/could have reached] out to a friend to feel better. She [call/could have called] "
           "Bree or Gaby, but she didn’t do it. If she had asked for help earlier, she [be/would have been] able to prevent her heavy "
           "feelings.</p><p>Paul also reflected a lot about the past. He knew he [do/could have done] something better to avoid problems, "
           "but he didn’t decide to act. He [leave/could have left] town to escape the consequences of his decisions.")
WSC = [("I [buy/could have bought] bread but I didn't know we needed it.", "past possibility"),
       ("We [not invite/shouldn't have invited] so many people to our party! I'm worried that we won't have enough room for everyone.",
        "past negative advice / regret"),
       ("I [start/should have started] saving money years ago!", "past advice / regret"),
       ("We [join/would have joined] you at the restaurant, but we couldn't get a babysitter.", "past willingness"),
       ("The weather [not be/couldn't have been] any worse!", "past negative possibility"),
       ("I [not arrive/couldn't have arrived] on time, even if I'd left earlier. There were dreadful traffic jams all the way.",
        "past negative possibility"),
       ("They [win/could have won] the football match, but John hurt his ankle.", "past possibility"),
       ("Amanda [finish/would have finished] the work, but she felt ill and had to go home.", "past willingness"),
       ("Lucy [leave/should have left] earlier. She missed her flight.", "past advice / regret"),
       ("We [not finish/couldn't have finished] the game, even if we'd wanted to. It was raining very hard and we had to stop.",
        "past negative possibility"),
       ("I [not eat/shouldn't have eaten] so much chocolate! I feel sick!", "past negative advice / regret"),
       ("Luke [pass/could have passed] the exam if he'd studied a bit more.", "past possibility"),
       ("John [call/would have called] Amy, but he didn't have her number.", "past willingness"),
       ("You [not be/shouldn't have been] rude to him. He's going to be really angry now.", "past negative advice / regret"),
       ("She [come/could have come] to the restaurant if she'd left work earlier.", "past possibility"),
       ("You [not take/shouldn't have taken] this job. I can see you're not enjoying it.", "past negative advice / regret"),
       ("The race was really difficult. She [not win/couldn't have won] because she's not fit enough.", "past negative possibility"),
       ("Our neighbours [not cut/shouldn't have cut] down the tree in their garden. It was a really beautiful tree.",
        "past negative advice / regret"),
       ("The children [do/should have done] their homework last night. Then they wouldn't be panicking on the way to school.",
        "past advice / regret"),
       ("I'm really cold! I [bring/should have brought] my coat.", "past advice / regret"),
       ("I [come/would have come] to see you! I didn't know you were ill.", "past willingness"),
       ("Andrew [go/could have gone] to Cambridge University, but he decided to travel instead.", "past possibility"),
       ("They [not be/couldn't have been] kinder to me. They were absolutely lovely.", "past negative possibility"),
       ("You [buy/should have bought] some milk at the shops. We don't have any milk.", "past advice / regret"),
       ("They [come/would have come] to have breakfast with us, but they went to bed too late the night before.", "past willingness")]
# Shadowing: подсказки к произношению каждой реплики
SHADOW_NOTES = ["Фраза “I was just saying” произносится “Iwzjusayin”.",
                "Зачёркнутые звуки: “was” — “wz”, “should have” — “shdev”. “To us” — две гласные соединяются между собой призвуком /w/.",
                "“Kind of” произносится слитно. Зачёркнутые буквы редуцируются: “what” — “wt”, “could” — “kd”, “have” — “ev”.",
                "Габи тоже говорит почти без пауз. “Sort of” произносится слитно. “Was” — “wz”, “we'd have” — “weedev”.",
                "Зачёркнутые буквы редуцируются: “the” — “th”, “killed herself” — “kilderself”, “must have” — “mustev”, “going on” — "
                "“goinon”."]


def build():
    # ---------- Warm up ----------
    warm = SEC("Warm up", "",
               '<div class="voc"><div class="voc-w"><b>wake</b><span>поминки</span><button type="button" class="say" data-say="wake" '
               'title="Послушать" aria-label="Послушать">🔊</button></div></div>' +
               EX("dh2-w1", "1.1", "Neighbors and friends come to Mary Alice's wake. How do you think they feel?",
                  IMG(IMG_DIR + "poster.jpg", "At the wake") + SAY + VOICE("dh2-w1-v") + WRITER("dh2-w1")), id="warm-up")

    # ---------- Vocabulary ----------
    defs = sorted(d for *_, d in VOCAB)
    words = "".join(f'<div class="voc"><div class="voc-w"><b>{w}</b><span>{tr}</span><button type="button" class="say" data-say="{w}" '
                    f'title="Послушать" aria-label="Послушать">🔊</button></div><ul class="voc-ex"><li>{ex}</li></ul></div>'
                    for w, tr, ex, _ in VOCAB)
    fill = ["[For God's sakes/For God’s sakes/For God's sake/For God’s sake], be careful with that antique vase!",
            "They want to [go over] to the office to check the documents.",
            "She [can’t face/cannot face/couldn’t face] cleaning the messy garage today.",
            "My shoes are in the [closet] next to the door.",
            "She had to [go through] all her emails to find the important message."]
    vocab = SEC("Vocabulary", "",
                EX("dh2-v1", "1.1", "Study the examples. What do the words in bold mean?", f'<div class="voc-list">{words}</div>') +
                EX("dh2-v2", "1.2", "Complete the boxes with the words from exercise 1.1.",
                   '<div class="pic-grid">' +
                   f'<figure class="pic"><img src="{IMG_DIR}closet.jpg" alt="" loading="lazy"><figcaption>{G("closet")}</figcaption></figure>' +
                   f'<figure class="pic"><img src="{IMG_DIR}go-through.jpg" alt="" loading="lazy"><figcaption>'
                   f'{G("go through|to go through")}</figcaption></figure></div>') +
                EX("dh2-v3", "1.3", "Match the phrases with the definitions.", OL([f"<b>{w}</b> — {S(d, defs)}" for w, _, _, d in VOCAB])) +
                EX("dh2-v4", "1.4", "Complete the sentences with phrases from 1.1.", OL([GAPS(x) for x in fill])), id="vocabulary")

    # ---------- Listening ----------
    listen = SEC("Listening", "",
                 EX("dh2-l1", "1.1", "At the wake. Watch the video. Why does Susan feel angry?",
                    vk_player(VK, "Desperate Housewives — At the wake") + SAY + VOICE("dh2-l1-v", 60) + WRITER("dh2-l1")) +
                 EX("dh2-l2", "1.2", "Watch the video again and answer the questions.",
                    OL(["Who is organizing the task of packing Mary Alice's things, and when?",
                        "Why does that person need help with the task?"]) + SAY + VOICE("dh2-l2-v", 60) + WRITER("dh2-l2")) +
                 EX("dh2-l3", "1.3", "Watch again, read the script below and translate the underlined phrases.",
                    PLAYER(AUDIO, "At the wake · 0:49") + scene("u") + SAY + VOICE("dh2-l3-v", 90) + WRITER("dh2-l3")) +
                 EX("dh2-l4", "1.4", "Answer the questions.",
                    OL(["What reason does Gabby give for believing Mary Alice couldn’t have been in crisis?",
                        "What final point does Susan make about Mary Alice’s death?"]) + SAY + VOICE("dh2-l4-v", 60) + WRITER("dh2-l4") +
                    REVEAL(ANSWERS, "Suggested answers (1.1–1.4)")), id="listening")

    # ---------- Grammar: should have / must have ----------
    grammar = SEC("Grammar", "Should have / Must have",
                  IMG(IMG_DIR + "susan.jpg", "Susan", cls="fig-small2") +
                  EX("dh2-g1", "1.1", "Listen and complete the gaps.",
                     PLAYER(CLIP[2], "Susan · 0:05") +
                     "<p>" + GAPS("If Mary Alice was having problems she [should have come] to us, she [should have let] us help her.") +
                     "</p>" + rule("should have")) +
                  info("1. Should have", "<p>Выражает критику по поводу невыполненных обязательств или сожаление об ошибках в прошлом.</p>"
                       "<p><b>Examples:</b><br>Mary Alice <b>should have come</b> to us for help. (But she didn’t.) <span class=\"tr\">Мэри "
                       "Элис надо было обратиться к нам за помощью.</span><br>We <b>should have noticed</b> she was struggling. (But we "
                       "failed to.) <span class=\"tr\">Жаль, что мы не заметили, что ей плохо.</span></p><p><b>Key contexts:</b><br>"
                       "✔️ <b>Criticism:</b> You <b>should have told</b> me the truth! <span class=\"tr\">Мог бы тогда сказать мне правду!"
                       "</span><br>✔️ <b>Regret:</b> I <b>should have listened</b> to her. <span class=\"tr\">Эх, надо было послушать её!"
                       "</span></p>", "g") +
                  EX("dh2-g2", "1.2", "Listen and complete the gaps.",
                     PLAYER(CLIP[5], "Susan · 0:04") +
                     "<p>" + GAPS("Gabby, the woman killed herself. Something [must have been] going on.") + "</p>" + rule("must have")) +
                  info("2. Must have", "<p>Позволяет делать логические выводы о прошлых событиях (определённость, основанная на "
                       "доказательствах). Выражает высокую вероятность какого-то события или состояния («Я убеждён, что так оно и было»)."
                       "</p><p><b>Examples:</b><br>She <b>must have been</b> in terrible pain. (Deduction from her suicide.) "
                       "<span class=\"tr\">Должно быть, она ужасно страдала.</span><br>They <b>must have known</b> something was wrong. "
                       "<span class=\"tr\">Они, скорее всего, знали, что что-то не так.</span></p><p><b>Key contexts:</b><br>"
                       "✔️ <b>Deduction:</b> The revolver <b>must have been</b> hidden for years. <span class=\"tr\">Должно быть, револьвер "
                       "прятали много лет.</span><br>✔️ <b>Certainty:</b> Paul <b>must have felt</b> devastated. <span class=\"tr\">Должно "
                       "быть, Пол был раздавлен.</span></p>", "g") +
                  scene("") +
                  EX("dh2-g3", "1.3", "Fill in the gaps with <i>should have</i> or <i>must have</i> and the correct form of the verb in "
                     "brackets.", OL([GAPS(x) for x in SM_FILL])) +
                  EX("dh2-g4", "1.4", "Rewrite the sentences using <i>should have</i> or <i>must have</i>.",
                     OL([f"{a}<br>{GAPS(b)}" for a, b in SM_REWRITE]) +
                     REVEAL("<b>Should have</b> — criticism, regret or unfulfilled duty (sentences 1, 3, 4, 6, 8, 10).<br>"
                            "<b>Must have</b> — logical conclusions (sentences 2, 5, 7, 9).", "Answer key")), id="grammar")

    # ---------- Grammar 2: would have / could have ----------
    grammar2 = SEC("Grammar 2", "Would have / Could have",
                   EX("dh2-h1", "1.1", "Listen and complete the gaps.",
                      PLAYER(CLIP[4], "Gabby · 0:03") +
                      "<p>" + GAPS("No. If Mary Alice was having some sort of crisis we [’d have known/would have known].") + "</p>" +
                      rule("would have")) +
                   info("3. Would have", "<p>Описывает гипотетические, несостоявшиеся события в прошлом, сожаление об упущенных "
                        "возможностях. Употребляется в условном предложении третьего типа («Если бы я знал, я бы пришёл»).</p>"
                        "<p><b>Examples:</b><br>“If Martha Huber had known the consequences, she <b>wouldn’t have sent</b> a note to Mary "
                        "Alice.” <span class=\"tr\">Если бы Марта Хубер знала о последствиях, она не отправила бы записку Мэри Элис.</span>"
                        "<br>“If it had been warmer, we <b>would have gone</b> for a swim.” <span class=\"tr\">Если бы было теплее, мы бы "
                        "пошли плавать.</span></p><p><b>Key contexts:</b><br>✔️ Past regrets or missed opportunities: “She <b>would have "
                        "reached out</b> for help if she had realized how close she was to breaking.” <span class=\"tr\">Она бы обратилась за "
                        "помощью, если бы поняла, что скоро сорвётся.</span><br>✔️ Hypothetical past in reported speech: “Her friends "
                        "<b>would have tried</b> to help her if they had known how much she was suffering.” <span class=\"tr\">Её друзья "
                        "попытались бы помочь ей, если бы они знали, как сильно она страдала.</span></p>", "g") +
                   EX("dh2-h2", "1.2", "Listen and complete the gaps.",
                      PLAYER(CLIP[3], "Gabby · 0:02") + "<p>" + GAPS("What kind of problems [could she have had]?") + "</p>" +
                      rule("could have")) +
                   info("4. Could have done", "<p>Используется для нереализованных возможностей, гипотетических сценариев событий в "
                        "прошлом или предположений о них. Оно также может выражать идею, что у кого-то был потенциал для достижения "
                        "чего-либо, но этого не произошло.</p><p><b>Examples:</b><br>I <b>could have studied</b> harder, but I was too lazy. "
                        "<span class=\"tr\">Я мог бы учиться лучше, но мне было лень.</span><br>Mary Alice <b>could have told</b> someone "
                        "about her feelings if she had felt comfortable enough. <span class=\"tr\">Мэри Элис могла бы рассказать кому-то о "
                        "своих переживаниях, если бы чувствовала доверие.</span><br>Paul <b>could have left</b> town before the incident "
                        "happened. <span class=\"tr\">Пол мог уехать из города до того, как это случилось.</span><br>She <b>could have "
                        "seen</b> something suspicious but chose not to mention it. <span class=\"tr\">Она могла видеть что-то "
                        "подозрительное, но решила не упоминать об этом.</span></p><p><b>Key contexts:</b><br>✔️ Unrealized past "
                        "opportunity/ability: She <b>could have married</b> him, but she didn't want to. <span class=\"tr\">Она могла бы "
                        "выйти за него замуж, но не захотела.</span><br>Paul <b>could have confessed</b> his true intentions if he had been "
                        "honest from the start. <span class=\"tr\">Пол мог бы признаться в своих намерениях, если бы с самого начала был "
                        "честен.</span><br>✔️ Past possibility/speculation: Why did Mary Alice seem so upset? She <b>could have found out</b> "
                        "something terrible. <span class=\"tr\">Почему Мэри Элис выглядела такой расстроенной? Возможно, она узнала что-то "
                        "ужасное.</span><br>They <b>could have been arguing</b> just before everything happened. <span class=\"tr\">Возможно, "
                        "они поругались как раз перед тем, как это случилось.</span><br>✔️ <i>Couldn't have done</i> (negative form): Mary "
                        "Alice <b>couldn't have predicted</b> her fate; it was beyond her control. <span class=\"tr\">Мэри Элис не могла "
                        "предугадать свою судьбу; это было не в её силах.</span><br>Paul <b>couldn't have known</b> that his actions would "
                        "lead to such consequences. <span class=\"tr\">Пол не мог знать, что его поступки приведут к таким последствиям."
                        "</span></p>", "g") +
                   scene("b") +
                   EX("dh2-h3", "1.3", "Complete the text with <i>could have</i> or <i>would have</i> + past participle of the verb in "
                      "brackets.", f"<p>{GAPS(WC_TEXT)}</p>") +
                   EX("dh2-h4", "1.4", "Complete the gaps with <i>would / should / could</i> and the correct form of the verbs in brackets.",
                      OL([f'{GAPS(x)} <span class="tr">({k})</span>' for x, k in WSC])), id="grammar-2")

    # ---------- Speaking ----------
    speak = SEC("Speaking", "",
                EX("dh2-s1", "1.1", "Complete the gaps with the words from the box: <i>For God's sakes, go over, closet, face, go through</i>.",
                   IMG(IMG_DIR + "closet-peek.jpg", "", cls="fig-small2") +
                   OL([GAPS(x) for x in ["The detective will [go through/go over] the evidence carefully.",
                                         "Can you [go over] to Finance and drop this paperwork off to Mary?",
                                         "There's a ladder in the [closet] to reach the upper shelves.",
                                         "After hearing the bad news, he couldn't [face] telling his family.",
                                         "Can you please stop arguing? [For God's sakes/For God’s sakes/For God's sake/For God’s sake], "
                                         "we're trying to have a peaceful dinner."]])) +
                EX("dh2-s2", "1.2", "Discuss the following questions.",
                   OL(["Have you ever needed to go over your notes before a test? Why?",
                       "Can you tell me about a time when you had to go through a lot of paperwork or emails?",
                       "Have you ever found something surprising in your closet?",
                       "Is there anything you can't face doing because it makes you uncomfortable or upset?",
                       "When do you think people might say “for God's sakes”? Can you give an example?"]) +
                   SAY + VOICE("dh2-s2-v") + WRITER("dh2-s2", "", 6)), id="speaking")

    # ---------- Dictation ----------
    dict_gaps = ["Susan, [I was just saying] Paul [wants to go over on Friday].",
                 "If [Mary Alice was having problems] she [should have come to us], she [should have let us help her].",
                 "What [kind of problems could she have had]?",
                 "No. If [Mary Alice was having some sort of crisis] we [’d have known/would have known].",
                 "Gabby, [the woman killed herself]. Something [must have been going on]."]
    dictation = SEC("Dictation", "",
                    '<p class="note-s">Прослушайте запись несколько раз и напечатайте то, что слышите. На каждое задание — 3 попытки.</p>' +
                    "".join(EX(f"dh2-d{i + 1}", f"1.{i + 1}", "Listen and type in what you hear.",
                               PLAYER(CLIP[i + 1], f"Dictation {i + 1}") + f"<p>{GAPS(x, 'wide')}</p>")
                            for i, x in enumerate(dict_gaps)), id="dictation")

    # ---------- Shadowing ----------
    legend = info("Условные обозначения", "<p>Красные вертикальные линии означают паузы. На слова, подчёркнутые красным, падает смысловое "
                  "ударение.</p><p>Слоги, подчёркнутые оранжевым, читаются долго.</p><p>Зелёные дуги, соединяющие слова, означают, что "
                  "эти слова читаются слитно. Зелёные квадраты, объединяющие 2 соседних слова, означают, что последний звук первого слова "
                  "и первый звук второго слова сливаются в один.</p>", "y")
    shadow = SEC("Shadowing", "",
                 shadow_intro() + legend +
                 "".join(EX(f"dh2-sh{i + 1}", f"1.{i + 1}", "Listen to the track, then repeat the sentence trying to copy the rhythm and "
                            "intonation of the original.",
                            f'<p class="quote">{line}</p>' + PLAYER(CLIP[i + 1], f"Shadowing {i + 1}") +
                            IMG(IMG_DIR + f"shadow-{i + 1}.jpg", "", SHADOW_NOTES[i]) + VOICE(f"dh2-sh{i + 1}-v", 30))
                         for i, line in enumerate(LINES)), id="shadowing")

    toc = '<nav class="toc">' + "".join(f'<a href="#{a}">{t}</a>' for a, t in SECTIONS) + "</nav>"
    return toc + "".join(f'<article class="page">{x}</article>' for x in (warm, vocab, listen, grammar, grammar2, speak, dictation, shadow))
