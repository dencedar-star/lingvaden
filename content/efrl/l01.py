"""English for Real Life · Блок 1 · Урок 1: Anna's birthday cake (Frozen Fever). Перенесён из ProgressMe."""
import re
from lib import G, S, EX, OL, SEC, IMG, REVEAL, VOICE

N = "1.1"
TITLE = "Anna's birthday cake"
LEAD = ("Сцена из мультфильма «Frozen Fever»: Эльза украшает двор к дню рождения Анны. Смотрим видео, учим слова из сцены, "
        "повторяем Present Simple и Present Continuous и говорим.")
TOPICS = "Video · Vocabulary · Listening · Present Simple vs Present Continuous · Speaking"
IMG_DIR = "../assets/img/efrl-l01/"
VK = "https://vkvideo.ru/video_ext.php?oid=-51337713&id=456239140&hash=8d111684590fc355&hd=3"   # основной плеер: открывается у всех
YOUTUBE = "Zfj1ACkjAJc"
MAILRU = "https://cloud.mail.ru/public/bz53/yrnwdqu1D"
AUDIO = "/media/efrl/l01.mp3"   # звук сцены (1:15); отдаёт api/media.php только ученикам с открытым курсом

# разделы урока: (якорь, название) — оглавление страницы
SECTIONS = [("warm-up", "Warm up"), ("video", "Video. Anna's birthday cake"), ("vocabulary", "Vocabulary"),
            ("listening", "Listening"), ("grammar", "Grammar revision. Present Simple vs Present Continuous"),
            ("speaking", "Speaking")]

ROLE = {"Elsa": "Elsa", "Kristoff": "Kristoff", "Olaf": "Olaf"}

# реплики сцены (для аудирования и чтения)
SCENE = [
    ("Elsa", "So lonely. <b>Stiff</b>. I can't do that! Come on, Elsa, this is for Anna. You can do this."),
    ("Kristoff", "Relax! It looks great."),
    ("Elsa", "I just want it to be <b>perfect</b>."),
    ("Kristoff", "Speaking of <b>perfect</b>, <b>check this out</b>."),
    ("Elsa", "Kristoff, are you sure I can leave you <b>in charge</b> here?"),
    ("Kristoff", "Absolutely."),
    ("Elsa", "Because I don't want anything to happen to this <b>courtyard</b>."),
    ("Kristoff", "What could happen? It's all <b>set</b>."),
    ("Elsa", "Olaf, what are you doing?"),
    ("Olaf", "I'm not eating cake."),
    ("Elsa", "Olaf…"),
    ("Olaf", "But it's an ice cream cake!"),
    ("Elsa", "And it's for Anna."),
    ("Olaf", "And it's for Anna."),
    ("Elsa", "Oh, it's time!"),
    ("Olaf", "It's time! For what?"),
    ("Elsa", "Okay… You sure you got this?"),
    ("Kristoff", "I'm sure."),
    ("Elsa", "Don't let anyone in before we're ready."),
    ("Kristoff", "I won't."),
    ("Elsa", "And don't touch anything."),
    ("Kristoff", "I'm just gonna stand here."),
    ("Olaf", "I'm probably gonna walk around a little."),
    ("Elsa", "And <b>keep an eye on</b> that cake!"),
    ("Kristoff", "She thinks you're an idiot! Well, clearly she's wrong! What? It's fine."),
    ("Olaf", "I can't read… or spell."),
]

# сцена с ремарками (как в ProgressMe — «полный текст»)
SCENE_NOTES = """[There is a blue cake that has an ice statue of Anna on it]<br>
Elsa: So lonely. *she transforms the Anna statue into two statues of Anna and Elsa*<br>
Stiff. *she transforms the statue into a reference of "Frozen 2013" when Elsa was on Anna after Anna saved Elsa from Hans*<br>
I can't do that! *she transforms the statue into one of Anna and Elsa skating*<br>
Come on, Elsa, this is for Anna. *the camera pans out to show that the blue cake has sunflowers on it* You can do this.<br>
Kristoff: Relax! It looks great. *Sven is shown to have buckets on his antlers*<br>
Elsa: I just want it to be perfect.<br>
Kristoff: Speaking of perfect, check this out. *the camera pans out to show something that says "Happy birthday Anna"*<br>
Elsa: Kristoff, are you sure I can leave you in charge here?<br>
Kristoff: Absolutely.<br>
Elsa: Because I don't want anything to happen to this courtyard.<br>
Kristoff: What could happen? It's all set.<br>
Elsa: *gasps* Olaf, what are you doing?<br>
Olaf: *his mouth is covered in something blue* I'm not eating cake.<br>
Elsa: Olaf…<br>
Olaf: But it's an ice cream cake!<br>
Elsa: *she bends down* And it's for Anna.<br>
Olaf: And it's for Anna.<br>
Elsa: Oh, it's time!<br>
Olaf: It's time! For what?<br>
Elsa: Okay… You sure you got this?<br>
Kristoff: I'm sure. *bare arms crossed*<br>
Elsa: Don't let anyone in before we're ready.<br>
Kristoff: I won't.<br>
Elsa: And don't touch anything.<br>
Kristoff: I'm just gonna stand here.<br>
Olaf: I'm probably gonna walk around a little.<br>
Elsa: And keep an eye on that cake!<br>
Kristoff: She thinks you're an idiot! Well, clearly she's wrong! What? It's fine.<br>
Olaf: I can't read… or spell."""

VOCAB = [
    ("stiff", "напряжённый, деревянный", None,
     [("My back is always <b>stiff</b> after a long flight.", "Моя спина всегда затекает после долгого полёта."),
      ("He always looks <b>stiff</b> and nervous during interviews.", "Он всегда выглядит напряжённым и нервным во время собеседований.")]),
    ("perfect", "идеальный", None,
     [("This warm weather is <b>perfect</b> for a picnic.", "Эта тёплая погода идеальна для пикника."),
      ("She speaks <b>perfect</b> English every day.", "Она каждый день говорит на идеальном английском.")]),
    ("check this out", "взгляни на это, оцени это",
     "Это повелительное наклонение (Imperative): оно совпадает по форме с Present Simple и используется в живой речи.",
     [("<b>Check this out</b>, I have a new phone!", "Взгляни на это, у меня новый телефон!"),
      ("<b>Check this out</b>, this video is very funny!", "Оцени это, это видео очень смешное!")]),
    ("be in charge of", "быть ответственным за", None,
     [("Who <b>is in charge of</b> this kitchen?", "Кто отвечает за эту кухню?"),
      ("I <b>am in charge of</b> organizing office parties.", "Я отвечаю за организацию офисных вечеринок.")]),
    ("courtyard", "двор", None,
     [("Children often play in the hotel <b>courtyard</b>.", "Дети часто играют во дворе отеля."),
      ("Our house has a beautiful green <b>courtyard</b>.", "У нашего дома есть красивый зелёный двор.")]),
    ("set", "установленный, назначенный",
     "Здесь слово выступает в роли прилагательного после глагола to be в Present Simple.",
     [("The dinner is always <b>set</b> for 7 p.m.", "Ужин всегда назначен на 7 вечера."),
      ("Every rule in this game is <b>set</b> and clear.", "Все правила в этой игре установлены и понятны.")]),
    ("to keep an eye on", "следить за, присматривать", None,
     [("I usually <b>keep an eye on</b> my brother's dog on weekends.", "Я обычно присматриваю за собакой моего брата по выходным."),
      ("She always <b>keeps an eye on</b> the children in the park.", "Она всегда следит за детьми в парке.")]),
]

PS, PC = "Present Simple", "Present Continuous"
TENSES = [PS, PC]


def writer(wid, placeholder="", rows=4):
    ph = placeholder.replace("\n", "&#10;")
    return (f'<div class="writer" data-id="{wid}" data-target=""><textarea rows="{rows}" placeholder="{ph}"></textarea>'
            '<div class="cnt"></div></div>')


SAY = '<p class="note-s">🎙 Запишите ответ голосом или напишите его — преподаватель увидит и услышит.</p>'


def video():
    return (f'<figure class="vid yt"><div class="yt-box"><iframe src="{VK.replace("&", "&amp;")}" '
            'title="Elsa Decorates for Anna\'s Birthday Surprise | Frozen Fever" loading="lazy" allowfullscreen '
            'allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock"></iframe></div>'
            '<figcaption>Elsa Decorates for Anna\'s Birthday Surprise | Frozen Fever (Disney Kids). '
            f'Не открывается? Смотреть на <a href="https://www.youtube.com/watch?v={YOUTUBE}" target="_blank" rel="noopener">YouTube ↗</a> '
            f'или на <a href="{MAILRU}" target="_blank" rel="noopener">Облаке Mail.ru ↗</a></figcaption></figure>')


def audio():
    return (f'<div class="aud"><span class="aud-l">♪ Elsa Decorates for Anna\'s Birthday · 1:15</span>'
            f'<audio controls preload="none" controlslist="nodownload" src="{AUDIO}"></audio></div>')


def dialogue(lines):
    return '<div class="scene">' + "".join(
        f'<p><b class="sp sp-{sp.lower()}">{sp}:</b> {t}</p>' for sp, t in lines) + "</div>"


def build():
    # ---------- Warm up ----------
    pics = [("elsa", "Elsa"), ("anna", "Anna"), ("kristoff", "Kristoff"), ("sven", "Sven"), ("olaf", "Olaf")]
    names = sorted(n for _, n in pics)
    match = '<div class="pic-grid">' + "".join(
        f'<figure class="pic"><img src="{IMG_DIR}{f}.jpg" alt="" loading="lazy"><figcaption>{S(n, names)}</figcaption></figure>'
        for f, n in pics) + "</div>"
    warm = SEC("Warm up", "",
               EX("rl1-w1", "1.1", "Do you know this animated film? Do you like it? Why/why not?",
                  IMG(IMG_DIR + "poster.jpg", "Frozen II", cls="fig-poster") + SAY + VOICE("rl1-w1-v", 90) + writer("rl1-w1")) +
               EX("rl1-w2", "1.2", "Match the words with the pictures.", match), id="warm-up")

    # ---------- Video ----------
    vid = SEC("Video. Anna's birthday cake", "",
              EX("rl1-v1", "1.1", "Watch the video and answer the questions.",
                 video() + OL(["What is Elsa doing?", "What is Kristoff doing?", "What is Olaf doing?"]) + SAY + VOICE("rl1-v1-v") +
                 writer("rl1-v1")), id="video")

    # ---------- Vocabulary ----------
    rows = ""
    for w, tr, note, ex in VOCAB:
        exs = "".join(f"<li>{e} <span class=\"tr\">{r}</span></li>" for e, r in ex)
        rows += (f'<div class="voc"><div class="voc-w"><b>{w}</b><span>{tr}</span>'
                 f'<button type="button" class="say" data-say="{w}" title="Послушать" aria-label="Послушать">🔊</button></div>'
                 + (f'<p class="voc-note">{note}</p>' if note else "") + f'<ul class="voc-ex">{exs}</ul></div>')
    vocab = SEC("Vocabulary", "", IMG(IMG_DIR + "balloon.jpg", "Happy Birthday!", cls="fig-small") +
                EX("rl1-voc", "1.1", "Study the words.", f'<div class="voc-list">{rows}</div>'), id="vocabulary")

    # ---------- Listening ----------
    gaps = [
        ("Elsa", f"So lonely. <b>Stiff</b>. I {G('can’t|cannot')} do that! Come on, Elsa, this is for Anna. You can do this."),
        ("Kristoff", f"Relax! It {G('looks')} great."),
        ("Elsa", f"I just {G('want')} it to be <b>perfect</b>."),
        ("Kristoff", "Speaking of <b>perfect</b>, <b>check this out</b>."),
        ("Elsa", f"Kristoff, are you sure I can {G('leave')} you <b>in charge</b> here?"),
        ("Kristoff", "Absolutely."),
        ("Elsa", f"Because I don't want {G('anything')} to happen to this <b>courtyard</b>."),
        ("Kristoff", "What could happen? It's all <b>set</b>."),
        ("Elsa", f"Olaf, {G('what')} are you doing?"),
        ("Olaf", "I'm not eating cake."),
        ("Elsa", "Olaf…"),
        ("Olaf", f"But it's an {G('ice')} cream cake!"),
        ("Elsa", "And it's for Anna."),
        ("Olaf", "And it's for Anna."),
        ("Elsa", f"Oh, it's {G('time')}!"),
        ("Olaf", "It's time! For what?"),
        ("Elsa", "Okay… You sure you got this?"),
        ("Kristoff", "I'm sure."),
        ("Elsa", f"Don't let {G('anyone')} in before we're ready."),
        ("Kristoff", "I won't."),
        ("Elsa", f"And {G('don’t|do not')} touch anything."),
        ("Kristoff", "I'm just gonna stand here."),
        ("Olaf", "I'm probably gonna walk around a little."),
        ("Elsa", f"And <b>keep an eye on</b> that {G('cake')}!"),
        ("Kristoff", f"She {G('thinks')} you're an idiot! Well, clearly she's wrong! What? It's fine."),
        ("Olaf", f"I can't {G('read')}… or spell."),
    ]
    listen = SEC("Listening", "",
                 EX("rl1-l1", "1.1", "Watch again and complete the gaps.",
                    audio() + dialogue(gaps) +
                    REVEAL(SCENE_NOTES, "Полный текст сцены с ремарками")), id="listening")

    # ---------- Grammar ----------
    sort1 = [("I just want it to be perfect.", PS), ("It looks great.", PS), ("I can't do that.", PS),
             ("I'm not eating cake.", PC), ("Olaf, what are you doing?", PC), ("She thinks you're an idiot!", PS)]
    theory = ('<div class="rule"><h4>Present Simple</h4><p>используется для описания <u>постоянных, привычных действий</u> '
              'или <u>общеизвестных фактов</u>.</p><p><b>Elsa often sings</b> when she’s alone. <span class="tr">Эльза часто поёт, '
              'когда одна.</span><br>Kristoff <b>buys</b> supplies from the same shop. <span class="tr">Кристофф покупает товары в '
              'одном и том же магазине.</span></p></div>'
              '<div class="rule"><h4>Present Continuous</h4><p>используется для описания действий, которые происходят <u>прямо '
              'сейчас</u> или в <u>текущий период</u>.</p><p>Elsa <b>is transforming</b> the figure on the cake. <span class="tr">'
              'Эльза превращает фигурку на торте (прямо сейчас).</span><br>Anna <b>is reading</b> an interesting book today. '
              '<span class="tr">Сегодня Анна читает интересную книгу.</span></p></div>')
    form = ('<table class="tbl form-tbl"><thead><tr><th></th><th>Present Simple</th><th>Present Continuous</th></tr></thead><tbody>'
            '<tr><th>+</th><td>Subject + verb (+s)<br><i>I like cake. Prince William lives in England.</i></td>'
            '<td>Subject + <b>am/is/are</b> + verb<sub>+ing</sub><br><i>I am eating now. My Spanish friend is traveling to England.</i></td></tr>'
            '<tr><th>−</th><td>Subject + <b>don’t/doesn’t</b> + verb<br><i>I don’t eat meat. They don’t know. She doesn’t eat meat.</i></td>'
            '<td>Subject + <b>am/is/are + not</b> + verb<sub>+ing</sub><br><i>I am not eating now. They aren’t listening. She isn’t buying chocolate.</i></td></tr>'
            '<tr><th>?</th><td><b>Do/does</b> + subject + verb<br><i>Do you live here? Does she eat meat?</i></td>'
            '<td><b>Am/is/are</b> + subject + verb<sub>+ing</sub><br><i>Are you cooking? Is he buying chocolate?</i></td></tr>'
            '</tbody></table>')
    pairs = ('<p><b>1️⃣ О домашней работе</b><br><b>a) I\'m doing my homework after school.</b><br><b>Значение:</b> это ваш '
             '<b>точный план на сегодня</b>. Вы говорите о конкретном действии, которое железно планируете сделать сегодня сразу после '
             'уроков.<br><b>b) I do my homework after school.</b><br><b>Значение:</b> это ваша <b>постоянная привычка, правило или '
             'рутина</b>. Вы делаете так <i>всегда</i> или <i>обычно</i>: пришли из школы — сели за уроки.</p>'
             '<p><b>2️⃣ О процессе и общем факте</b><br><b>a) Joe is learning to drive.</b><br><b>Значение:</b> Джо находится '
             '<b>в процессе</b> обучения прямо в этот период жизни (он записался на курсы, ходит на уроки вождения в эти недели, хотя '
             'прямо в эту секунду может спать или обедать).<br><b>b) Many teenagers learn to drive when they are seventeen.</b><br>'
             '<b>Значение:</b> это <b>общий факт</b> или закономерность о жизни людей. В целом в мире/стране подростки обычно учатся '
             'водить в 17 лет.</p>'
             '<p><b>3️⃣ О хобби и действии прямо сейчас</b><br><b>a) Mark plays the guitar.</b><br><b>Значение:</b> Марк <b>умеет '
             'играть</b> на гитаре. Это его хобби или навык в жизни вообще. Сейчас гитара может просто висеть на стене.<br>'
             '<b>b) Mark is playing the guitar.</b><br><b>Значение:</b> Марк играет на гитаре <b>прямо сейчас, в эту самую '
             'секунду</b>. Вы слышите музыку из его комнаты.</p>')
    sort2 = [("Everybody knows that Elsa sings beautifully.", PS), ("Hey! Olaf is eating the cake! Stop him!", PC),
             ("Kristoff checks the list of guests every hour.", PS),
             ("Anna is busy at the moment. She is helping Kristoff with his homework.", PC),
             ("Elsa uses her powers to create snow.", PS), ("Elsa is practicing her ice powers this week.", PC),
             ("Anna drinks hot chocolate on Saturdays.", PS), ("Elsa is decorating the statue at the moment.", PC)]
    # выбор формы: [вариант/вариант] — правильный помечен *
    choose = ["Look outside! Olaf [builds/is building*] a snowman.",
              "Kristoff usually [is buying/buys*] supplies from the same shop.",
              "Sven [helps/is helping*] Kristoff with the birthday sign today.",
              "[Does/Is*] Sven [wait/waiting*] patiently for Kristoff now?",
              "Elsa [transforms/is transforming*] the ice sculpture at the moment.",
              "[Does*/Is] Olaf [love*/loving] warm hugs?",
              "Kristoff [isn't checking/doesn't check*] the boat every morning.",
              "Anna [sings/is singing*] a new song now.",
              "Elsa [doesn't like*/isn't liking] hot weather."]
    # глагол в нужной форме: [подсказка/ответ|ответ]; пустая подсказка — вспомогательный глагол
    verbs = ["Elsa always [use/uses] her powers to make snow.", "Olaf [like/likes] summer.",
             "Anna [go/goes] to the market every Saturday.", "Kristoff [not enjoy/doesn't enjoy|does not enjoy] cold weather.",
             "Elsa [prepare/is preparing] for a big winter festival now.",
             "The princesses and Olaf [sit/are sitting] near the fire at the moment.",
             "Anna [help/is helping] her sister with the decorations currently.",
             "Kristoff [carry/is carrying] a large bag of supplies today.",
             "Sometimes, Elsa [not use/doesn't use|does not use] her powers to avoid revealing herself.",
             "[/Does] Olaf [understand/understand] why everyone loves summer?",
             "[/Do] Elsa and Anna [visit/visit] their friends often?",
             "[/Are] Kristoff and Sven [work/working] together right now?",
             "Elsa [not/doesn't|does not] usually [sing/sing] in public.",
             "[/Is] Olaf [talk/talking] to a new snow friend today?",
             "Anna never [come/comes] late.", "[/Are] they [enjoy/enjoying] this party?"]

    def pick(m):
        opts = m.group(1).split("/")
        return S(next(o[:-1] for o in opts if o.endswith("*")), [o.rstrip("*") for o in opts])

    def gap(m):
        hint, ans = m.group(1).split("/", 1)
        g = G(ans)
        return g.replace("<input ", f'<input placeholder="{hint}" ', 1) if hint else g

    name = [("Everybody knows that Elsa <b>sings</b> beautifully.", PS), ("Hey! Olaf <b>is eating</b> the cake! Stop him!", PC),
            ("Kristoff <b>checks</b> the list of guests every hour.", PS),
            ("Anna is busy at the moment. She <b>is helping</b> Kristoff with his homework.", PC),
            ("Elsa <b>uses</b> her powers to create snow.", PS), ("Elsa <b>is practicing</b> her ice powers this week.", PC),
            ("Anna <b>drinks</b> hot chocolate on Saturdays.", PS), ("Elsa <b>is decorating</b> the statue at the moment.", PC)]
    grammar = SEC("Grammar revision", "Present Simple vs Present Continuous",
                  EX("rl1-g1", "1", "Sort out the sentences in the correct category.",
                     OL([f"{s} {S(a, TENSES)}" for s, a in sort1])) +
                  theory +
                  '<h3 class="sub">Present Simple vs Present Continuous: form</h3>' + form +
                  EX("rl1-g5", "2", "Sort out the sentences in the correct category.",
                     OL([f"{s} {S(a, TENSES)}" for s, a in sort2])) +
                  EX("rl1-g6", "3", "Choose the correct form from the box.",
                     OL([re.sub(r"\[([^\]]+)\]", pick, x) for x in choose])) +
                  EX("rl1-g2", "4", "Explain the difference between sentences a and b in each pair.",
                     '<p>a) I\'m doing my homework after school.<br>b) I do my homework after school.</p>'
                     '<p>a) Joe is learning to drive.<br>b) Many teenagers learn to drive when they are seventeen.</p>'
                     '<p>a) Mark plays the guitar.<br>b) Mark is playing the guitar.</p>' + SAY + VOICE("rl1-g2-v") + writer("rl1-g2")) +
                  EX("rl1-g7", "5", "Put the verb in the Present Simple or Present Continuous form.",
                     OL([re.sub(r"\[([^\]]*)\]", gap, x) for x in verbs])) +
                  REVEAL(pairs, "Разбор пар предложений (к заданию 4)") +
                  IMG(IMG_DIR + "courtyard.jpg", "Happy Birthday — the courtyard") +
                  EX("rl1-g3", "6", "Talk about Elsa and Anna. Make up affirmative (+), negative (−) and question (?) sentences "
                     "in Present Simple and Present Continuous.",
                     '<div class="cols2"><div><h4>Present Simple</h4>' + writer("rl1-g3-ps", "", 4) +
                     '</div><div><h4>Present Continuous</h4>' + writer("rl1-g3-pc", "", 4) +
                     "</div></div>") +
                  EX("rl1-g4", "7", "Read the sentences, name the tense and explain it.",
                     OL([f"{s} {S(a, TENSES)}" for s, a in name]) +
                     '<p class="note-s">🎙 Объясните голосом, почему здесь это время.</p>' + VOICE("rl1-g4-v")), id="grammar")

    # ---------- Speaking ----------
    qs = [("Stiff", "How do you relax your <b>stiff</b> muscles after a long day?"),
          ("Perfect", "What does a <b>perfect</b> weekend look like for you?"),
          ("Be in charge of", "Who <b>is</b> usually <b>in charge of</b> organizing your birthday parties?"),
          ("Courtyard", "Do you prefer to have your coffee in a <b>courtyard</b> or inside a café?"),
          ("Set", "Is there a <b>set</b> schedule for your classes, or does it change every week?")]
    speak = SEC("Speaking", "",
                EX("rl1-s1", "1.1", "Listen and read the text.",
                   audio() +
                   dialogue(SCENE)) +
                EX("rl1-s2", "1.2", "Answer the questions.",
                   "".join(f'<p class="q"><b>{h}</b><br>{q}</p>' for h, q in qs) + SAY + VOICE("rl1-s2-v") + writer("rl1-s2", "", 5)) +
                EX("rl1-s3", "1.3", "Make up your own sentences with these phrases: <i>to keep an eye on</i>, <i>check this out</i>.",
                   writer("rl1-s3", "", 3) +
                   REVEAL("<b>To keep an eye on</b><br>Can you <b>keep an eye on</b> my bag while I go to the restroom?<br><br>"
                          "<b>Check this out</b><br>Hey, <b>check this out</b>! Did you see the new design I made? Can you check this "
                          "out and tell me what you think?", "Possible answers")), id="speaking")

    toc = '<nav class="toc">' + "".join(f'<a href="#{a}">{t}</a>' for a, t in SECTIONS) + "</nav>"
    return toc + "".join(f'<article class="page">{x}</article>' for x in (warm, vid, vocab, listen, grammar, speak))
