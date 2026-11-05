"""Desperate Housewives · Урок 3: Susan meets Mike (знакомство на поминках). Second Conditional, I wish. Перенесён из ProgressMe."""
from pathlib import Path

from lib import S, EX, OL, SEC, IMG, REVEAL, VOICE, WRITER, PLAYER, GAPS
from .l01 import SAY, info, vk_player, shadow_intro
from .l02 import scene as _scene

N = "3"
TITLE = "Susan meets Mike"
LEAD = ("На поминках Сьюзан знакомится с новым соседом — сантехником Майком Дельфино. Слова screw up, I get that a lot, "
        "be very big with; Second Conditional и I wish.")
TOPICS = "Warm up · Vocabulary · Listening · Second Conditional · I wish · Speaking · Dictation · Shadowing"
IMG_DIR = "../assets/img/dh-l03/"
VK = "https://vkvideo.ru/video_ext.php?oid=-51337713&id=456239226&hash=487d66aa280ab2cd&hd=3"
AUDIO = "/media/dh/l03.mp3"   # звук сцены целиком — из записи владельца
MEDIA = Path(__file__).resolve().parents[2] / "media" / "dh"

SECTIONS = [("warm-up", "Warm up"), ("vocabulary", "Vocabulary"), ("listening", "Listening"), ("grammar", "Grammar: Second Conditional"),
            ("speaking", "Speaking"), ("dictation", "Dictation"), ("shadowing", "Shadowing")]

LINES = ["I wouldn't eat that if I were you.",
         "No, I just refuse to believe that anybody can screw up macaroni and cheese.",
         "Oh my God. How did you… It tastes like it's burned and undercooked.",
         "Thanks. I'm Mike Delfino. I just started renting the Sims house next door.",
         "Yeah, I'm very big with the under five set.",
         "Now that everybody's seen that I brought something, I should probably just throw this out."]

SCENE = [("Susan", "I wouldn't eat that if I were you."),
         ("Mike", "Why?"),
         ("Susan", "I made it, trust me. Hey, hey, do you have a death wish?"),
         ("Mike", "No, I just refuse to believe that anybody can {screw up} macaroni and cheese. Oh my God. How did you… It tastes "
                  "like it's burned and undercooked."),
         ("Susan", "Yeah, {I get that a lot}. {Here you go}."),
         ("Mike", "Thanks. I'm Mike Delfino. I just started renting the Sims house next door."),
         ("Susan", "Susan Mayer. I live across the street."),
         ("Mike", "Mrs. Huber told me about you. Said you illustrate children's books."),
         ("Susan", "Yeah, I'm {very big with} the under five set. What do you do?"),
         ("Mike", "{Plumber}. So if you ever have a {clog}… or something."),
         ("Susan", "Now that everybody's seen that I brought something, I should probably just throw this out.")]

VOCAB = [("to screw up", "провалить, испортить, сделать что-то неправильно", "to fail at something"),
         ("I get that a lot", "мне это часто говорят", "people say that frequently"),
         ("here you go", "держите, вот, пожалуйста", "here is what you asked for"),
         ("be very big with", "быть очень популярным среди", "be very popular with"),
         ("a clog", "засор в трубе", "a blockage"),
         ("plumber", "сантехник", "a person whose job is to connect and repair things such as water and drainage pipes, baths, and toilets")]

ANSWERS = ("1. She throws the food away.<br>2. He says it tastes burned and undercooked at the same time.<br>3. She illustrates "
           "children’s books.<br>4. He’s a plumber. He says: “So if you ever have a clog… or something.”")
SHADOW_NOTES = [
    "Пауз нет. Звук /t/ в wouldn't исчезает. Eat that произносится как /i:ðæt/. That if превращается в thatf, причём звук /t/ "
    "невыраженный (см. ниже).",
    "В американском английском /t/ произносится невыраженно, как будто «съедается»: just refuse — jusrefuse, and cheese — ancheese. "
    "Screw up — возникает призвук /w/: /skruːwʌp/. В that anybody звук /t/ максимально расслабленный, нужный лишь для того, чтобы "
    "соединить две гласные (см. ниже).",
    "How did you произносится скороговоркой, все звуки краткие. It tastes — itastes. Like it's, and undercooked произносится в одно "
    "слово.",
    "I'm Mike Delfino — он делает небольшую паузу перед именем, чтобы выделить его. Just started — justarted, renting — rentn, next "
    "door — nexdoor.",
    "Сьюзан говорит очень монотонно, не выделяя ударные слова и практически без пауз. With the — withe.",
    "Сьюзан смущена, тараторит и делает паузы в неестественных местах (логично сделать паузу после seen). Brought, should, just — "
    "везде невыраженное /t/ или /d/. That everybody, that I — flap t для соединения с гласной."]
WISH = [("I don’t know many people (and I’m lonely).", "<i>I wish I knew more people.</i>"),
        ("I don’t have a mobile phone (and I need one).", "I wish [I had a mobile phone]."),
        ("Helen isn’t here (and I need to see her).", "I wish [Helen were here/Helen was here]."),
        ("It’s cold (and I hate cold weather).", "I wish [it weren’t cold/it wasn’t cold/it were not cold/it was not cold/it were warm/it was warm]."),
        ("I live in a big city (and I don’t like it).", "I wish [I didn’t live in a big city/I did not live in a big city]."),
        ("I can’t go to the party (and I’d like to).", "I wish [I could go to the party]."),
        ("I have to work tomorrow (but I’d like to stay in bed).",
         "I wish [I didn’t have to work tomorrow/I did not have to work tomorrow]."),
        ("I don’t know anything about cars (and my car has just broken down).",
         "I wish [I knew something about cars/I knew more about cars]."),
        ("I’m not feeling well (and it’s not nice).", "I wish [I felt better/I were feeling better/I was feeling better/I felt well].")]


def clip(n, label):
    """Реплика сцены (media/dh/l03-N.mp3); пока файла нет — пометка, что запись появится."""
    if (MEDIA / f"l03-{n}.mp3").exists():
        return PLAYER(f"/media/dh/l03-{n}.mp3", label)
    return '<p class="note-s">♪ Аудиозапись появится здесь.</p>'


def scene(mark):
    return _scene(mark, SCENE)


def build():
    # ---------- Warm up ----------
    warm = SEC("Warm up", "",
               EX("dh3-w1", "1.1", "Meet the characters.",
                  '<div class="pic-grid">'
                  f'<figure class="pic"><img src="{IMG_DIR}susan.jpg" alt="" loading="lazy"><figcaption><b>Susan Mayer</b></figcaption></figure>'
                  f'<figure class="pic"><img src="{IMG_DIR}mike.jpg" alt="" loading="lazy"><figcaption><b>Mike Delfino</b></figcaption></figure>'
                  "</div>") +
               EX("dh3-w2", "1.2", "What can you tell about each character? If you haven't seen the show, share your guesses.",
                  SAY + VOICE("dh3-w2-v") + WRITER("dh3-w2")) +
               EX("dh3-w3", "1.3", "Describe the picture.",
                  IMG(IMG_DIR + "wake.jpg", "", "Susan and Mike meet at the wake. Susan has brought macaroni and cheese as a contribution.") +
                  SAY + VOICE("dh3-w3-v", 60) + WRITER("dh3-w3")), id="warm-up")

    # ---------- Vocabulary ----------
    defs = sorted(d for *_, d in VOCAB)
    words = "".join(f'<div class="voc"><div class="voc-w"><b>{w}</b><span>{tr}</span><button type="button" class="say" data-say="{w}" '
                    f'title="Послушать" aria-label="Послушать">🔊</button></div></div>' for w, tr, _ in VOCAB)
    dialog = ("<p><b>Tom:</b> Hi, Mike. What's up?</p><p><b>Mike:</b> Oh, hi, Tom. Ugh, I've been trying to fix my bike, but I totally "
              "<b>screwed up</b> and broke the chain. Now I don’t know what to do. Could you give me that wrench (гаечный ключ)?</p>"
              "<p><b>Tom:</b> Sure, <b>here you go</b>.</p><p><b>Mike:</b> Thanks. I hope I can get it done now. My bike <b>is very big "
              "with</b> the kids in the neighborhood — they all love riding it!</p><p><b>Tom:</b> I know.</p><p><b>Mike:</b> How are things "
              "with you, buddy?</p><p><b>Tom:</b> Actually, I’ve got a <b>clog</b> in my drain at home. It’s such a pain. Could you take a "
              "look at it sometime?</p><p><b>Mike:</b> Yeah, sure.</p>")
    fill = ["I really [screwed up] the presentation by forgetting my notes.",
            "A: “You look like Marilyn Monroe.” — B: “Yeah, I [get that a lot].”",
            "[Here you go], your coffee.",
            "His music isn’t famous, but he [is very big with/’s very big with] college students.",
            "There’s [a clog] in the sink — we need to call a [plumber].",
            "The [plumber] seems more interested in his coffee and his phone."]
    vocab = SEC("Vocabulary", "",
                EX("dh3-v1", "1.1", "Read the dialogue and figure out the meaning of the words in bold.",
                   IMG(IMG_DIR + "bike.jpg", "", cls="fig-small2") + f'<div class="script-p">{dialog}</div>') +
                EX("dh3-v2", "1.2", "Add these words to your dictionary.", f'<div class="voc-list">{words}</div>') +
                EX("dh3-v3", "1.3", "Match the words with their definitions.", OL([f"<b>{w}</b> — {S(d, defs)}" for w, _, d in VOCAB])) +
                EX("dh3-v4", "1.4", "Fill in the gaps with appropriate vocabulary using correct grammar: <i>here you go, screw up, get "
                   "that a lot, be very big with, a clog, plumber</i>.", OL([GAPS(x) for x in fill])), id="vocabulary")

    # ---------- Listening ----------
    choice = [("A", "He believes that macaroni and cheese is too simple for anyone to ruin, but he realizes she completely forgot to add "
                    "cheese or salt."),
              ("B", "He thinks she is joking to be polite, only to find out that she accidentally used spoiled ingredients that made "
                    "the food inedible."),
              ("C", "He initially assumes she is exaggerating her lack of culinary skills, but he quickly discovers that she managed to "
                    "make the dish taste both burnt and undercooked."),
              ("D", "He suspects her cooking might be bland, but he discovers that she used too many spices and made it overly salty.")]
    audio = PLAYER(AUDIO, "Susan meets Mike") if (MEDIA / "l03.mp3").exists() else ""
    listen = SEC("Listening", "",
                 EX("dh3-l1", "1.1", "Susan meets Mike. Watch the video. What does Susan do at the end?",
                    vk_player(VK, "Desperate Housewives — Susan meets Mike") + SAY + VOICE("dh3-l1-v", 30) + WRITER("dh3-l1")) +
                 EX("dh3-l2", "1.2", "Watch again and choose the best answer. How does Mike's reaction to Susan's warning about the "
                    "dish reveal his initial perception of her cooking, and what does he discover instead?",
                    "".join(f"<p><b>{k})</b> {t}</p>" for k, t in choice) + f"<p>The best answer: {S('C', ['A', 'B', 'C', 'D'])}</p>") +
                 EX("dh3-l3", "1.3", "Watch again, read the script below and translate the underlined phrases.",
                    audio + scene("u") + SAY + VOICE("dh3-l3-v", 90) + WRITER("dh3-l3")) +
                 EX("dh3-l4", "1.4", "Answer the questions.",
                    OL(["How does Mike describe the macaroni and cheese?", "What does Susan Mayer do for work?",
                        "What is Mike Delfino’s job? And what help does he offer Susan?"]) + SAY + VOICE("dh3-l4-v", 60) +
                    WRITER("dh3-l4") + REVEAL(ANSWERS, "Suggested answers (1.1, 1.4)")), id="listening")

    # ---------- Grammar ----------
    opts = ["past simple", "would/could/might", "base verb"]
    grammar = SEC("Grammar", "Second Conditional",
                  EX("dh3-g1", "1.1", "Listen to what Susan says.", IMG(IMG_DIR + "susan-mike.jpg", "Susan and Mike", cls="fig-small2") +
                     clip(1, "Susan · 0:01")) +
                  EX("dh3-g2", "1.2", "Listen and complete the gaps.",
                     clip(1, "Susan · 0:01") + "<p>" + GAPS("I [wouldn't eat/would not eat] that if I [were] you.") + "</p>" +
                     f'<p>If + {S("past simple", opts)}, {S("would/could/might", opts)} + {S("base verb", opts)}</p>') +
                  info("Second Conditional", "<p><b>Second Conditional</b> используется, чтобы говорить о нереальных или невероятных/"
                       "гипотетических ситуациях в настоящем или будущем и их воображаемых результатах.</p><p><b>Examples:</b><br>"
                       "<b>If I won the lottery, I would travel the world.</b> (Unlikely, but imagining the result.) <span class=\"tr\">Если "
                       "бы я выиграл деньги, я бы поехал путешествовать по миру.</span><br><b>If she studied harder, she could pass the "
                       "exam.</b> (She isn’t studying hard now, so passing is unlikely.) <span class=\"tr\">Если бы она лучше училась, она "
                       "бы сдала экзамен.</span><br><b>If it rained tomorrow, we might stay home.</b> (It probably won’t rain, but if it "
                       "did, we would stay home.) <span class=\"tr\">Если бы завтра пошёл дождь, мы бы могли остаться дома.</span><br>"
                       "<b>If I were you, I would apologize.</b> (Hypothetical advice — “I am not you, but if I were…”) <span class=\"tr\">"
                       "На твоём месте я бы извинился.</span><br><b>If he had more time, he would learn a new language.</b> (He doesn’t "
                       "have time now, so learning a language is unlikely.) <span class=\"tr\">Если бы у него было больше времени, он бы "
                       "выучил новый язык.</span></p><p><b>Key notes:</b><br>✔️ <b>Were</b> is often used instead of <b>was</b> (e.g., "
                       "“If I <b>were</b> rich…”).<br>✔️ The second conditional is <u>not</u> used for <u>real or possible situations</u> "
                       "(use the first conditional for those). Compare:<br>If it <b>rains</b> tomorrow, we can stay home. <span "
                       "class=\"tr\">Если завтра будет дождь, можем остаться дома.</span><br>If it <b>rained</b> tomorrow, we might stay "
                       "home. <span class=\"tr\">Если бы завтра пошёл дождь, мы могли бы остаться дома.</span></p>", "g") +
                  EX("dh3-g3", "1.3", "Rewrite the sentences starting with <i>I wish</i>.", OL([f"{a}<br>{GAPS(b, 'wide')}" for a, b in WISH])) +
                  EX("dh3-g4", "1.4", "Make up 5 sentences with your own ideas: <i>If I were you, I would…</i>",
                     SAY + VOICE("dh3-g4-v") + WRITER("dh3-g4", "", 5)), id="grammar")

    # ---------- Speaking ----------
    qs = ["If you could live anywhere in the world, where would you choose and why?",
          "What would you do if you found out you only had one year left to live?",
          "If you could change one thing about your past, what would it be?",
          "How would your life be different if social media didn’t exist?",
          "If you could instantly master any skill, what would it be?",
          "Would you still work if you didn’t need money? Why or why not?",
          "If you could have dinner with any historical figure, who would you choose?",
          "What would you do if you woke up one day and were famous?",
          "If you could solve one global problem, which one would you pick?",
          "Would you travel to space if you had the chance? Why or why not?"]
    speak = SEC("Speaking", "",
                EX("dh3-s1", "1.1", "Answer the questions.", OL(qs) + SAY + VOICE("dh3-s1-v") + WRITER("dh3-s1", "", 6)) +
                EX("dh3-s2", "1.2", "Make up your examples with the target vocabulary: <i>here you go, to screw up, get that a lot, be very "
                   "big with, a clog, plumber</i>.",
                   info("Example", "<p>You can't open the window because it screws up the air conditioning.</p>") +
                   SAY + VOICE("dh3-s2-v", 60) + WRITER("dh3-s2", "", 5)), id="speaking")

    # ---------- Dictation ----------
    dict_gaps = ["I [wouldn't eat that if I were you/would not eat that if I were you].",
                 "No, [I just refuse to believe that anybody can screw up macaroni and cheese].",
                 "Oh my God. How did you… [It tastes like it's burned and undercooked].",
                 "Thanks. I'm Mike Delfino. [I just started renting the Sims house next door].",
                 "Yeah, [I'm very big with the under five set].",
                 "Now [that everybody's seen that I brought something], I should [probably just throw this out]."]
    dictation = SEC("Dictation", "",
                    '<p class="note-s">Прослушайте запись несколько раз и напечатайте то, что слышите. На каждое задание — 3 попытки.</p>' +
                    "".join(EX(f"dh3-d{i + 1}", f"1.{i + 1}", "Listen and type in what you hear.",
                               clip(i + 1, f"Dictation {i + 1}") + f"<p>{GAPS(x, 'wide')}</p>") for i, x in enumerate(dict_gaps)),
                    id="dictation")

    # ---------- Shadowing ----------
    legend = info("Условные обозначения", "<p>Красные вертикальные линии означают паузы. На слова, подчёркнутые красным, падает смысловое "
                  "ударение.</p><p>Слоги, подчёркнутые оранжевым, читаются долго.</p><p>Зелёные дуги, соединяющие слова, означают, что "
                  "эти слова читаются слитно. Зелёные квадраты, объединяющие 2 соседних слова, означают, что последний звук первого слова "
                  "и первый звук второго слова сливаются в один.</p>", "y")
    extra = {0: info("", "<p><b>Невыраженный [t]:</b> язык принимает позицию для [t], но не производит взрывного звука, оставляя его "
                         "«съеденным».</p>", "y"),
             1: info("Flap t", "<p>«Flap t» (или «flap d») на конце слов в американском английском — это быстрое, расслабленное "
                     "произношение звука «t» как лёгкого, звонкого «d» (похожего на русский «р»), если слово заканчивается на «t», а "
                     "следующее начинается с гласной. Это сглаживает речь, убирая взрывной согласный. Этот звук возникает, когда язык "
                     "быстро ударяет по альвеолам (бугоркам за верхними зубами).</p><p>Если следующее слово начинается с согласного, «t» "
                     "обычно произносится чётко или становится глоттальным (гортанным).</p><p><b>Примеры на стыке слов:</b> <i>Get it</i> "
                     "«Гедир» (звучит почти как <i>geddit</i>), <i>What about</i> «Уо-да-баут», <i>Not at all</i> «Но-дадол».<br>"
                     "<b>Примеры в конце слов перед гласной:</b> <i>Wait a minute</i> «Уэй-да-минит», <i>Set up</i> «Се-дап».</p>", "y")}
    shadow = SEC("Shadowing", "",
                 shadow_intro() + legend +
                 "".join(EX(f"dh3-sh{i + 1}", f"1.{i + 1}", "Listen to the track, then repeat the sentence trying to copy the rhythm and "
                            "intonation of the original.",
                            f'<p class="quote">{line}</p>' + clip(i + 1, f"Shadowing {i + 1}") +
                            IMG(IMG_DIR + f"shadow-{i + 1}.jpg", "", SHADOW_NOTES[i]) + extra.get(i, "") + VOICE(f"dh3-sh{i + 1}-v", 30))
                         for i, line in enumerate(LINES)), id="shadowing")

    toc = '<nav class="toc">' + "".join(f'<a href="#{a}">{t}</a>' for a, t in SECTIONS) + "</nav>"
    return toc + "".join(f'<article class="page">{x}</article>' for x in (warm, vocab, listen, grammar, speak, dictation, shadow))
