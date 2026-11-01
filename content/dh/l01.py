"""Desperate Housewives · Урок 1: Mary Alice (пилотная серия, монолог рассказчицы). Перенесён из ProgressMe."""
from lib import G, S, C, EX, OL, SEC, IMG, REVEAL, VOICE, WRITER, PLAYER, GAPS

N = "1"
TITLE = "Mary Alice"
LEAD = ("Начало сериала: Мэри Элис Янг рассказывает о своём последнем дне на Wisteria Lane. Слова о домашних делах, "
        "Past Perfect, диктант и shadowing.")
TOPICS = "Warm up · Vocabulary · Listening · Speaking · Past Perfect · Dictation · Shadowing"
IMG_DIR = "../assets/img/dh-l01/"
VK = None   # видео сцены (Listening): ссылка на плеер VK — от владельца
CLIP_A = "/media/dh/l01-a.mp3"   # «When you read this morning's paper …» (0:06)
CLIP_B = "/media/dh/l01-b.mp3"   # «That's why it was so astonishing …» (0:16)

SECTIONS = [("warm-up", "Warm up"), ("vocabulary", "Vocabulary"), ("listening", "Listening"),
            ("practice", "Vocabulary practice & Speaking"), ("grammar", "Grammar: Past Perfect"), ("dictation", "Dictation"),
            ("shadowing", "Shadowing")]

SAY = '<p class="note-s">🎙 Запишите ответ голосом или напишите его — преподаватель увидит и услышит.</p>'

SCRIPT = ("My name is Mary Alice Young. When you read this morning's paper, you may {come across} an article about the unusual "
          "day I had last week. Normally, there's never anything {newsworthy} about my life, but that all changed last Thursday. "
          "Of course, everything seemed quite normal at first. I made breakfast for my family. I {performed my chores}. "
          "I completed my projects. I {ran my errands}. In truth, I spent the day as I spent every other day, quietly polishing "
          "the routine of my life until it {gleamed} with perfection. That's why it was so {astonishing} when I decided to go "
          "to my hallway closet and {retrieve} a revolver that had never been used.")

VOCAB = [("to perform chores", "выполнять домашние дела", "to do routine household tasks"),
         ("can't face doing", "не мочь заставить себя делать (что-либо), не решаться делать",
          "feeling unable to handle a particular task, situation"),
         ("newsworthy", "примечательный, заслуживающий внимания", "interesting and important"),
         ("to come across", "натолкнуться случайно, случайно найти", "to find by chance"),
         ("to gleam", "блестеть", "to shine"),
         ("astonishing", "поразительный, удивительный", "very surprising"),
         ("to run errands", "бегать по делам", "to go out to complete small tasks"),
         ("to retrieve", "доставать, забирать", "to get back from a place where it was stored")]


def script(mark):
    """Монолог; mark — как выделить слова урока: 'b' (жирным), 'u' (подчеркнуть) или '' (без выделения)."""
    t = SCRIPT
    for w in [x.split("}")[0] for x in t.split("{")[1:]]:
        t = t.replace("{" + w + "}", f"<{mark}>{w}</{mark}>" if mark else w)
    return f'<p class="script-p">{t}</p>'


def video():
    if not VK:
        return '<p class="note-s">▶ Видео к уроку появится здесь.</p>'
    return (f'<figure class="vid yt"><div class="yt-box"><iframe src="{VK.replace("&", "&amp;")}" title="Desperate Housewives — Mary Alice" '
            'loading="lazy" allowfullscreen allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock"></iframe>'
            '</div></figure>')


def info(title, body, kind="i"):
    return f'<div class="rule rule-{kind}">' + (f"<h4>{title}</h4>" if title else "") + f"{body}</div>"


def build():
    # ---------- Warm up ----------
    warm = SEC("Warm up", "",
               EX("dh1-w1", "1.1", "Read the descriptions of this picture and choose the correct one. Then answer the questions.",
                  IMG(IMG_DIR + "poster.jpg", "Wisteria Lane") +
                  '<p><b>A.</b> A busy downtown street scene with tall buildings, people rushing to work, and cars stuck in traffic. '
                  'There are street vendors and advertisements everywhere.</p>'
                  '<p><b>B.</b> A peaceful suburban street is shown from above, with families and neighbors going about their day. '
                  'Several people are outside doing chores, walking, and talking near brightly colored houses and neatly kept lawns.</p>'
                  '<p><b>C.</b> A quiet beachside town where people are relaxing on the sand enjoying the ocean view. '
                  'Surfboards and towels are scattered around.</p>'
                  f'<p>The correct description: {S("B", ["A", "B", "C"])}</p>') +
               EX("dh1-w2", "1.2", "Do you like houses like these? Why? Do you think it’s comfortable to live there? Why?",
                  SAY + VOICE("dh1-w2-v") + WRITER("dh1-w2")) +
               info("", "<b>Wisteria Lane</b> is a fictional street at the center of U.S. television drama series "
                        "<i>Desperate Housewives</i>."), id="warm-up")

    # ---------- Vocabulary ----------
    defs = sorted(d for _, _, d in VOCAB)
    rows = "".join(f'<div class="voc"><div class="voc-w"><b>{w}</b><span>{tr}</span>'
                   f'<button type="button" class="say" data-say="{w}" title="Послушать" aria-label="Послушать">🔊</button></div></div>'
                   for w, tr, _ in VOCAB)
    vocab = SEC("Vocabulary", "",
                EX("dh1-v1", "1.1", "Study the words.",
                   IMG(IMG_DIR + "chores.jpg", "to perform/do chores", "to perform/do chores", cls="fig-small2") +
                   f'<div class="voc-list">{rows}</div>') +
                EX("dh1-v2", "1.2", "Read the text and figure out the meaning of the words in bold. Match the words with their meanings.",
                   script("b") + OL([f"<b>{w}</b> — {S(d, defs)}" for w, _, d in VOCAB])) +
                '<p class="note-s">Сохраните фразы в свой словарь или перепишите их в тетрадь.</p>', id="vocabulary")

    # ---------- Listening ----------
    qs = OL(["What is the name of the narrator (рассказчик)?", "List three routine activities she performed on that day.",
             "What shocking action did she take at the end of the passage?"])
    ans13 = ("1. The narrator’s name is Mary Alice Young.<br>2. Three routine activities she performed:<br>— Made breakfast for her "
             "family.<br>— Performed her chores.<br>— Ran her errands.<br>3. She retrieved an unused revolver from her hallway "
             "closet and killed herself.")
    disc = ("1. Before last Thursday, her life was normally uneventful — there was “never anything newsworthy” about it.<br>"
            "2. She describes her typical approach as meticulously maintaining her daily routine, comparing it to “quietly "
            "polishing the routine of my life until it gleamed with perfection.”")
    listen = SEC("Listening", "",
                 EX("dh1-l0", "1.1", "Glossary.", IMG(IMG_DIR + "closet.jpg", "Closet", "<b>closet</b> — стенной шкаф, гардеробная",
                                                     cls="fig-small2")) +
                 EX("dh1-l1", "1.2", "Watch the video. What did the woman take out of her hallway closet?",
                    video() + f"<p>She took out {G('a revolver|revolver|a gun|gun')}.</p>") +
                 EX("dh1-l2", "1.3", "Watch the video again and answer the questions.",
                    qs + SAY + VOICE("dh1-l2-v", 30) + WRITER("dh1-l2") + REVEAL(ans13, "Suggested answers")) +
                 EX("dh1-l3", "2.1", "Watch again and read the script below.", script("")) +
                 EX("dh1-l4", "2.2", "Vocabulary focus. Translate the underlined phrases.",
                    script("u") + SAY + VOICE("dh1-l4-v") + WRITER("dh1-l4")) +
                 EX("dh1-l5", "2.3", "Discuss the questions.",
                    OL(["How does the narrator describe her typical approach to daily life?",
                        "Do you think the narrator planned this action, or was it impulsive?"]) +
                    SAY + VOICE("dh1-l5-v") + WRITER("dh1-l5") + REVEAL(disc, "Suggested answers")), id="listening")

    # ---------- Vocabulary practice & Speaking ----------
    fill = ["Waking up early on Saturday to [perform chores] like laundry and dishes feels exhausting.",
            "After that pop quiz today, I just [can’t face doing/cannot face doing] my math homework right now — maybe after "
            "some YouTube time.",
            "When I finally beat the final level of that impossible game, my friends said it was totally [newsworthy] — like I "
            "should be on a gaming livestream!",
            "I was scrolling online when I [came across] a meme that made me laugh so hard I cried!",
            "After hours of cleaning, my sneakers had such a [gleam] that they looked brand new.",
            "It was [astonishing] when my teacher actually remembered every student’s birthday this year — we thought she had a "
            "secret spreadsheet!",
            "Mom made me [run errands] all afternoon — first to return library books, then to buy milk, and finally to pick up my "
            "little sister from dance class.",
            "I had to [retrieve] my backpack from the lost-and-found after leaving it on the bus — again!"]
    talk = ["Have you ever come across something surprising or interesting online or in real life? What was it?",
            "What’s the most newsworthy event you’ve heard about recently? Why did it catch your attention?",
            "What chores do you usually perform at home? Which one do you dislike the most, and why?",
            "Do you often run errands for your family or yourself? What’s the most annoying errand you’ve had to do?",
            "Can you think of a time when you saw something gleam (like jewelry, a car, or even someone’s eyes)? What was it?",
            "What’s the most astonishing fact or achievement you’ve ever heard? Why did it amaze you?",
            "Have you ever had to retrieve something important that you lost? How did you feel when you found it?"]
    words = ", ".join(f"<i>{w}</i>" for w, _, _ in VOCAB)
    practice = SEC("Vocabulary practice & Speaking", "",
                   EX("dh1-p1", "1.1", f"Fill in the blanks with target vocabulary: {words}.", OL([GAPS(x) for x in fill])) +
                   EX("dh1-p2", "1.2", "Discuss the following questions.", OL(talk) + SAY + VOICE("dh1-p2-v") + WRITER("dh1-p2", "", 6)) +
                   EX("dh1-p3", "1.3", "Make up your own sentences with the target vocabulary.", WRITER("dh1-p3", "", 6)) +
                   EX("dh1-p4", "1.4", "Imagine a newspaper article describing your unusual day. What details would reporters "
                      "focus on?", WRITER("dh1-p4", "", 6)), id="practice")

    # ---------- Grammar ----------
    theory = info("Past Perfect",
                  "<p>Прошедшее совершенное время обозначает действие, завершившееся до определённого момента или другого "
                  "действия в прошлом.</p><p><b>Употребление:</b></p>"
                  "<p>Действие до другого действия в прошлом:<br>The train <b>had left</b> when I arrived. <span class=\"tr\">Поезд уже "
                  "ушёл (<i>раньше</i>), когда я пришёл (<i>позже</i>).</span></p>"
                  "<p>Действие к определённому моменту в прошлом (маркеры <i>by, by the time</i>):<br>She’d <b>learned</b> English "
                  "by the age of 20. <span class=\"tr\">Она выучила английский к 20 годам. <i>Сначала она выучила английский, а потом "
                  "ей исполнилось 20 лет.</i></span></p>"
                  "<p><b>Причина в прошлом:</b><br>He was tired because he <b>had worked</b> all day. <span class=\"tr\">Он устал, "
                  "потому что весь день работал. <i>Сначала он работал, именно поэтому он потом устал.</i></span></p>"
                  "<p>В условных предложениях 3-го типа (нереальное прошлое):<br>If I had known, I would have told you. "
                  "<span class=\"tr\">Если бы я знал (<i>тогда</i>), я бы сказал.</span></p>"
                  "<p><b>Слова-маркеры:</b><br>Before — перед тем как<br>After — после того как<br>By — к какому-то времени<br>"
                  "By the time — к тому времени как</p>", "g")
    ps_pp = ('<table class="tbl form-tbl"><thead><tr><th></th><th>Past Simple</th><th>Past Perfect</th></tr></thead><tbody>'
             '<tr><th>Последовательность</th><td>I <b>came</b> home and <b>cooked</b> dinner. <span class="tr">(Сначала пришёл, потом '
             'готовил)</span></td><td>I <b>had cooked</b> dinner when he came home. <span class="tr">(Сначала приготовил, а потом он '
             'пришёл)</span></td></tr>'
             '<tr><th>Причина</th><td>I <b>was</b> tired because I <b>worked</b> a lot. <span class="tr">(Два действия рядом)</span></td>'
             '<td>I <b>was</b> tired because I <b>had worked</b> a lot. <span class="tr">(Устал, потому что раньше много работал)'
             '</span></td></tr>'
             '<tr><th>Пример</th><td>The movie <b>started</b> at 8 p.m.</td><td>The movie <b>had started</b> before we arrived.</td></tr>'
             '</tbody></table>')
    pres_pp = ("<p><b>Present Perfect:</b><br><i>I have lost my keys.</i> <span class=\"tr\">Я потерял ключи (и поэтому не могу "
               "войти <u>сейчас</u>).</span><br><i>She has already had dinner.</i> <span class=\"tr\">Она уже поужинала (и поэтому "
               "<u>сейчас</u> сыта).</span></p><p><b>Past Perfect:</b><br><i>I had lost my keys, so I couldn’t get in.</i> "
               "<span class=\"tr\">Я не смог <u>тогда</u> войти, потому что потерял ключи (<i>до этого</i>).</span><br>"
               "<i>She had already eaten dinner when I arrived.</i> <span class=\"tr\">Она поужинала <u>до</u> моего прихода.</span></p>")
    sentence = "That's why it was so astonishing when I decided to go to my hallway closet and retrieve a revolver that "
    correct = ["I didn’t eat by the time I had left home.<br>Correct: I [hadn’t eaten] by the time I [left] home.",
               "When I had arrived home, my sister already made lunch.<br>Correct: When I [arrived] home, my sister [had] already "
               "[made] lunch.",
               "I had woken up late because I forgot to set my alarm clock.<br>Correct: I [woke] up late because I [/’d forgotten/had "
               "forgotten] to set my alarm clock."]
    q22 = ["[Had] he [live/lived] in New York before he [move/moved] to Los Angeles?",
           "[Had] you [eat/eaten] anything before you [go/went] to the theatre?",
           "[Had] the plane [arrive/arrived] by that time?",
           "[Had] she [do/done] her homework before her sister [come/came] home?",
           "[Had] they [sell/sold] everything before they [move/moved] to Manchester?",
           "Why [not/hadn’t] you [clean/cleaned] the flat by the time the guests [arrive/arrived]?",
           "What [had] you [do/done] by 6 o’clock?",
           "Where [had] she [work/worked] before she [graduate/graduated] from University?",
           "What [had] you [do/done] before you [go/went] to the supermarket?",
           "What [had] Harry [know/known] about for a while?"]
    q23 = ["You went to Sue’s house, but she wasn’t there. (she / go / out)<br><i>She had gone out.</i>",
           "You went back to your home town after many years. It wasn’t the same as before. (it / change / a lot)<br>"
           "It [had changed] a lot.",
           "I invited Rachel to the party, but she couldn’t come. (she / arrange / to do something else)<br>"
           "She [/’d arranged/had arranged] to do something else.",
           "You went to the cinema last night. You got to the cinema late. (the film / already / begin)<br>"
           "The film [had already begun].",
           "It was nice to see Dan again after such a long time. (I / not / see / him for five years)<br>"
           "I [hadn’t seen/had not seen] him for five years.",
           "I offered Sue something to eat, but she wasn’t hungry. (she / just / have / breakfast)<br>"
           "She [/’d just had/had just had] breakfast."]
    q24 = ["The man sitting next to you on the plane was very nervous. It was his first flight. (fly)<br><i>He’d never flown "
           "before.</i>",
           "A woman walked into the room. She was a complete stranger to me. (see)<br>I [/’d never seen/had never seen] her before.",
           "Sam played tennis yesterday. He wasn’t very good at it because it was his first game. (play)<br>"
           "He [/’d never played/had never played] tennis before.",
           "Last year we went to Denmark. It was our first time there. (be there)<br>We [/’d never been/had never been] there "
           "before."]
    q25 = ["‘Was Paul at the party when you arrived?’ ‘No, he <i>had gone</i> (go) home.’",
           "I felt very tired when I got home, so I [go/went] straight to bed.",
           "The house was very quiet when I got home. Everybody [go/had gone] to bed.",
           "Sorry I’m late. The car [break/broke] down on my way here.",
           "We were driving along the road when we [see/saw] a car which [break/had broken] down, so we [stop/stopped] to help."]
    grammar = SEC("Grammar", "Past Perfect",
                  IMG(IMG_DIR + "mary-alice.jpg", "Mary Alice Young", cls="fig-small2") +
                  EX("dh1-g1", "1.1", "Listen and complete the rule.",
                     PLAYER(CLIP_B, "That's why it was so astonishing… · 0:16") +
                     info("", f"<p>{sentence}<b>had never been</b> used.</p>") +
                     f'<p>I/we/they/you/he/she/it {S("had", ["had", "past participle"])} + {S("past participle", ["had", "past participle"])}</p>') +
                  EX("dh1-g2", "1.2", "Study the example and answer the question: Which event happened first?",
                     IMG(IMG_DIR + "sequence.jpg", "Past Perfect: sequence of events") +
                     f'<p>{C("I had lost the ticket", "I missed the train", "I had lost the ticket")}</p>') +
                  theory +
                  EX("dh1-g3", "1.3", "Complete the rule.",
                     f"<p>She had learned English = she<b>’d learned</b> English</p><p>had = ’{G('d')}</p>" +
                     info("", f"<p>{sentence}<b>had never been</b> used.</p><p class=\"tr\"><i>Она достала револьвер, который до того "
                              "момента никто никогда не использовал.</i></p>")) +
                  '<h3 class="sub">1.4 Past Simple vs Past Perfect</h3>' + ps_pp +
                  '<h3 class="sub">1.5 Present Perfect vs Past Perfect</h3>' + pres_pp +
                  EX("dh1-g4", "2.1", "Correct the mistakes.", OL([GAPS(x) for x in correct])) +
                  EX("dh1-g5", "2.2", "Complete the gaps with the correct form of the verb in brackets.", OL([GAPS(x) for x in q22])) +
                  EX("dh1-g6", "2.3", "Read the situations and make up sentences with the prompts.", OL([GAPS(x) for x in q23])) +
                  EX("dh1-g7", "2.4", "Write a sentence with <i>never … before</i>. Use the verb in brackets.", OL([GAPS(x) for x in q24])) +
                  EX("dh1-g8", "2.5", "Put the verb into the correct form, past perfect (I had done) or past simple (I did).",
                     OL([GAPS(x) for x in q25])), id="grammar")

    # ---------- Dictation ----------
    dict_ = SEC("Dictation", "",
                '<p class="note-s">Прослушайте запись несколько раз и напечатайте то, что слышите. На каждое задание — 3 попытки.</p>' +
                EX("dh1-d1", "1.1", "Listen and type in what you hear.",
                   PLAYER(CLIP_A, "Dictation 1 · 0:06") +
                   "<p>" + GAPS("When [you read this morning's paper], you [may come across an article] about "
                                "[the unusual day I had last week].", "wide") + "</p>") +
                EX("dh1-d2", "1.2", "Listen and type in what you hear.",
                   PLAYER(CLIP_B, "Dictation 2 · 0:16") +
                   "<p>" + GAPS("That's [why it was so astonishing] when [I decided to go to my hallway closet] and "
                                "[retrieve a revolver] that [had never been used].", "wide") + "</p>"), id="dictation")

    # ---------- Shadowing ----------
    how = ("<p>В идеале вы синхронно или с отставанием в 1–2 секунды повторяете за диктором его речь, имитируя интонацию, темп и "
           "произношение. Основная цель — натренировать речевой аппарат и мозг, как у ребёнка, осваивающего родную речь, без "
           "акцента на грамматике.</p><p>Если повторять синхронно слишком сложно, то сначала прослушайте оригинал, затем повторите "
           "в своём темпе, стараясь копировать интонацию, паузы, ударения и особенности произношения.</p><p>Это задание сложное: "
           "мозгу приходится контролировать одновременно много непривычных для себя аспектов. Утомляемость наступает через 5–15 "
           "минут. Как только заметили, что дикция стала хуже и вы стали выполнять упражнение вполсилы, остановитесь.</p>"
           "<p>Не стремитесь к идеалу, сдавайте задание как есть. В конце курса вы сможете вернуться, выполнить его снова и "
           "проанализировать свой прогресс.</p><p><a href=\"https://skyeng.ru/magazine/kak-metod-tenevogo-povtora-pomozhet-"
           "uluchshit-proiznoshenie/\" target=\"_blank\" rel=\"noopener\">Узнайте больше о методе теневого повторения из статьи "
           "Skyeng ↗</a></p>")
    shadow = SEC("Shadowing", "",
                 info("Shadowing", "<p>Это техника обучения, при которой вы слушаете аудиозапись на иностранном языке и максимально "
                      "быстро, практически одновременно, повторяете слова, интонацию и темп за диктором, следуя за ним, как тень "
                      "(от англ. <i>shadow</i> — тень). Этот метод «теневого повтора» предназначен для тренировки произношения, "
                      "слитной речи и улучшения восприятия на слух.</p>") +
                 info("Цель", "<p>Развитие беглости речи, имитация акцента и интонации носителей, преодоление языкового барьера.</p>", "y") +
                 info("Как выполнять shadowing", how, "g") +
                 EX("dh1-sh1", "1.1", "Listen to the track, then repeat the sentence trying to copy the rhythm and intonation of the "
                    "original.",
                    "<p class=\"quote\">When you read this morning's paper, you may come across an article about the unusual day I had "
                    "last week.</p>" + PLAYER(CLIP_A, "Shadowing 1 · 0:06") +
                    IMG(IMG_DIR + "shadow-1.jpg", "", "Вертикальные линии означают паузы. На подчёркнутые слова падает смысловое ударение.") +
                    IMG(IMG_DIR + "shadow-2.jpg", "", "Подчёркнутые гласные читаются долго, все остальные — коротко, что создаёт "
                        "музыкальный ритм английской речи.") +
                    IMG(IMG_DIR + "shadow-3.jpg", "", "Если слово заканчивается на согласную, а следующее начинается на гласную, они "
                        "звучат без паузы: “whenyou” (when you). Когда рядом стоят d/t и th, то часто d/t проглатывается: “reathis” "
                        "(read this).") +
                    VOICE("dh1-sh1-v", 30)) +
                 EX("dh1-sh2", "1.2", "Listen and repeat.",
                    "<p class=\"quote\">That's why it was so astonishing when I decided to go to my hallway closet and retrieve a "
                    "revolver that had never been used.</p>" + PLAYER(CLIP_B, "Shadowing 2 · 0:16") +
                    IMG(IMG_DIR + "shadow-4.jpg", "", "Если соседние слова заканчиваются и начинаются на одну и ту же согласную, они "
                        "сливаются: “waso” (was so).") +
                    VOICE("dh1-sh2-v", 60)), id="shadowing")

    toc = '<nav class="toc">' + "".join(f'<a href="#{a}">{t}</a>' for a, t in SECTIONS) + "</nav>"
    return toc + "".join(f'<article class="page">{x}</article>' for x in (warm, vocab, listen, practice, grammar, dict_, shadow))
