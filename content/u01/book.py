"""Страница «Учебник»: Unit 01 My first class, pp. 8–13. Длинные тексты — из OCR и ключей."""
from lib import G, S, EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, script, FIX
from . import shared as X
from keys import column, joined

IMG_DIR = "../assets/img/unit01/"

FIX[10] = [("casier", "easier"), ("teaching,", "teaching."), ("7.?", "7.”"), (" - ", " – "), ("— ", "– ")]
FIX[11] = [(" - ", " – "), ("‘language solutions’", "‘language solutions’"), ("“language solutions’", "‘language solutions’")]
FIX[160] = [("• I’m not sure", "O: I’m not sure"), ("5o0", "500"), ("l’ve", "I’ve"), ("Yeah. seven", "Yeah, seven"),
            ("Oh OK, So how", "Oh OK. So how"), ("A- Oh right", "A: Oh right"), ("So...um...", "So ... um ..."),
            (" - ", " – ")]

ARTICLE_BOLD = ["top head teacher", "motivation", "the point", "Relying on", "evidence", "environment",
                "continuity", "progress at different speeds", "deal with", "more available"]
HEADS = ["Lack of motivation", "Lost trade", "Change to early teaching questioned"]


def _bold(s, words, once):
    for w in words:
        if w in once:
            continue
        i = s.find(" " + w + " ") + 1 or s.find(" " + w + ",") + 1 or s.find(" " + w + "?") + 1 or s.find(w + " ")
        if w == "motivation":
            i = s.find("lack motivation")
            i = i + 5 if i >= 0 else -1
        if w == "the point":
            i = s.find("the point?")
        if i > 0 or (i == 0 and s.startswith(w)):
            s = s[:i] + f"<b>{w}</b>" + s[i + len(w):]
            once.add(w)
    return s


def article():
    from ocrtext import fixed
    raw = paras(10, (0, 640, 300, 1080), indent=10**6, gap=10**6) + \
        paras(10, (292, 690, 560, 860), indent=10**6, gap=10**6) + \
        paras(10, (548, 640, 794, 860), indent=10**6, gap=10**6) + \
        paras(11, (0, 580, 380, 1060))
    text = " ".join(fixed(10, r) for r in raw).replace(" 10 OUTCOMES", "")
    quote = "“Many primary school teachers don’t have a good enough level to teach”"
    text = text.replace(quote + " ", "")
    for h in HEADS:
        text = text.replace(" " + h + " ", f"\n#{h}\n")
    # второй абзац последнего раздела
    text = text.replace(" That can be difficult,", "\nThat can be difficult,")
    once, out = set(), []
    for chunk in text.split("\n"):
        chunk = chunk.strip()
        if chunk.startswith("#"):
            out.append(f"<h5>{chunk[1:]}</h5>")
        elif chunk:
            out.append(f"<p>{_bold(chunk, ARTICLE_BOLD, once)}</p>")
    body = "".join(out).replace("<h5>Lost trade</h5>", f'<p class="pull">{quote}</p><h5>Lost trade</h5>')
    return ('<div class="article"><span class="tag">EDUCATION</span>'
            '<h3>‘Language policy a disaster’ says head teacher</h3>'
            f'<div class="colum">{body}</div>'
            + IMG(IMG_DIR + "p10-classroom.jpg", "Classroom") + "</div>")


def brian():
    from ocrtext import fixed
    ps = [fixed(11, p) for p in paras(11, (400, 60, 794, 440))]
    head, rest = ps[0].split(". ", 1) if ". " in ps[0] else (ps[0], "")
    html = f"<p><b>{head}.</b></p>" + (f"<p>{rest}</p>" if rest else "") + "".join(f"<p>{p}</p>" for p in ps[1:])
    return f'<div class="story">{html}</div>'


def S11():
    return SCRIPT("1.1", "G = Guy, O = Olga", script(160, (0, 140, 397, 600)))


def S12():
    return SCRIPT("1.2", "", script(160, (0, 620, 397, 1050)) + script(160, (397, 80, 794, 160)))


def S13():
    return SCRIPT("1.3", "M = Martin, A = Anna", script(160, (397, 190, 794, 860)))


def p8():
    speaking = SEC("Speaking", "", EX("b8-sa", "A", "Did you have an interview before you began this course? What did they ask you?", "") +
                   EX("b8-sb", "B", "Work in pairs. Interview your partner for three minutes. Find out:",
                      UL(["information about your partner’s life.", "about your partner’s work / studies.",
                          "where your partner learnt English.", "any other interesting information."])))
    box = ('<div class="box"><p><b>We generally make questions by using the auxiliary verb (<i>be / have / do</i>) + the subject '
           '(<i>you / your parents / he / they</i>) and then a noun, adjective or verb.</b></p><hr>'
           '<p class="ex-line">Are you a doctor? &nbsp;·&nbsp; Have your parents left already?</p>'
           '<p class="ex-line">What did you do yesterday? &nbsp;·&nbsp; What are you doing now?</p></div>')
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>I’m really into</i></b></p>'
              '<p>In English, people often say <i>I’m really into</i> instead of <i>I really like</i>. It is generally used when '
              'talking about music, sport, films and free-time activities. This is particularly common among young people.</p>'
              '<p><i>I’m really into cooking.<br>I’m really into jazz.</i></p></div>')
    grammar = SEC("Grammar", "Question formation", box + X.qform("b8-ga") + HELP(136))
    head = ('<div class="cols-31"><div>' + speaking + grammar + '</div><div>' +
            IMG(IMG_DIR + "p08-couple.jpg", "") + native + '</div></div>')
    return PAGE_BOX(8, head)


def p9():
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear Guy, a teacher at a language school, interviewing a new student, Olga.</p>' +
              EX("b9-la", "A", '<span class="audio-ic">♪</span> 1.1 Listen. Answer the questions.',
                 OL(["Where is Olga from?", "How long has she been studying English?",
                     "How long is she going to stay in Britain?"]) +
                 REVEAL(OL([r[2:] for r in column(1, 0, "Listening:", "B:") if r[:1].isdigit()]), "Ответы (ключ)")) +
              S11() + X.listen_choice("b9-lb"))
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p>'
                '<p class="ex-line">I’d rather not say.<br>I’d rather not.<br>I’d rather not talk about it, if you don’t mind.<br>'
                'I’d rather go somewhere else, if that’s OK with you.<br>I’d rather do something else.</p></div>')
    spk = SEC("Speaking", "", EX("b9-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "Do you think many people from other countries know your home town? Why? / Why not?",
        "Would you like to live and work abroad permanently? Why? / Why not?",
        "Is it rude to ask someone their age?",
        "Are there any other questions you should not ask when you do not know someone very well?"])))
    dc = SEC("Developing conversations", "Asking follow-up questions",
             '<div class="box"><p><b>We often follow up a question and answer by asking a related question to find out more '
             'details. Some of these questions are quite fixed.</b></p></div>' +
             EX("b9-da", "A", "Can you remember the follow-up questions the teacher asked Olga after these questions?",
                '<p><i>Where are you from?<br>How long have you been learning English?</i></p>' +
                REVEAL("Whereabouts?<br>So have you been to the UK to study before?", "Ответ (ключ)")) +
             X.dc_match("b9-db") +
             EX("b9-dc", "C", '<span class="audio-ic">♪</span> 1.2 Listen and check your answers. You will only hear one of the follow-up questions in each case.', S12()) +
             EX("b9-dd", "D", "Can you think of one more follow-up question you might ask in 1–6 in exercise B?", "") +
             EX("b9-de", "E", "Work in pairs. Have conversations using the six questions and the follow-up questions in exercise B.", ""))
    people = '<div class="people">' + "".join(
        f'<img src="{IMG_DIR}p09-person{i}.jpg" alt="Person {i}" loading="lazy">' for i in range(1, 9)) + "</div>"
    cp = SEC("Conversation practice", "",
             EX("b9-ca", "A", "Choose one of the people below. You are going to be this person. Do not tell anyone who you have "
                "chosen. Decide how to answer the questions we have looked at in this lesson.", "") +
             EX("b9-cb", "B", "Now have conversations with other students. Ask and answer the questions in the role of the person you chose.", people))
    return PAGE_BOX(9, IMG(IMG_DIR + "p09-students.jpg", "") +
                    '<div class="cols"><div>' + lis + patterns + spk + '</div><div>' + dc + cp + "</div></div>")


def p10():
    a1 = OL([
        "I’m <b>fairly fluent</b> in Spanish. I <b>can maintain conversations on a range of topics</b>.",
        "I <b>get by</b> if I’m travelling in Germany – I can do the basic things.",
        "My Japanese is <b>very basic</b> – just a few words.",
        "I’m more or less <b>bilingual</b> in English and Turkish.",
        "I can have a conversation about some things in Italian if people <b>speak slowly</b>.",
    ], "items alpha")
    qa = OL(["Do you speak any other languages? How well?" + a1,
             "How did you learn your foreign language? Did you go to classes, <b>teach yourself</b>, or just <b>pick</b> it <b>up</b> off the street?",
             "Do you find it easy to pick up a new language?", "Why are you learning English?"])
    vkey = REVEAL(UL([
        "<b>1a</b> " + "quite confident and able to speak without too much hesitation; can talk easily about different subjects",
        "<b>1b</b> survive / manage", "<b>1c</b> simple / limited",
        "<b>1d</b> speaking two languages equally well, as a native speaker", "<b>1e</b> don’t speak too fast",
        "<b>2</b> learn through self-study; learn informally"]), "Значения (ключ)")
    order = OL([f"{t} → место {S(k, list('12345'))}" for t, k in
                [("a (fairly fluent)", "2"), ("b (get by)", "4"), ("c (very basic)", "5"), ("d (bilingual)", "1"), ("e (speak slowly)", "3")]],
               "items", 1).replace('<ol class="items">', '<ol class="items" style="list-style:none;padding-left:4px">')
    voc = SEC("Vocabulary", "Learning languages",
              EX("b10-va", "A", "Work in pairs. Discuss what you think the words and phrases in <b>bold</b> mean.", qa + vkey) +
              EX("b10-vb", "B", "Look at question 1 and answers a–e in exercise A. Order the answers 1–5:<br>"
                 "1 = the person who speaks the language best.<br>5 = the person who speaks the language worst.", order) +
              EX("b10-vc", "C", "Work in groups. Answer the questions in exercise A. If you only speak English and your language, "
                 "think of someone you know who speaks several languages and answer questions about them.", ""))
    rkey = REVEAL(UL(_reading_summary()), "Ответ (ключ)")
    read = SEC("Reading", "",
               '<p class="intro">You are going to read an article about British people and foreign languages.</p>' +
               EX("b10-ra", "A", "Look at these headings from the article. Discuss with a partner what you think is going to be said.",
                  UL(["‘Language policy a disaster’ says head teacher", "Lack of motivation", "Lost trade",
                      "Change to early teaching questioned"])) +
               EX("b10-rb", "B", "Read the article and see if your ideas were correct.", rkey) +
               article() + X.reading_tf("b10-rc") +
               EX("b10-rd", "D", "Mark the text with a ✓ where you agree with what is said, a ✗ where you disagree, and a ! "
                  "where something surprises you. Then work in pairs. Discuss your ideas.", "") +
               X.reading_words("b10-re"))
    return PAGE_BOX(10, voc + read)


def _reading_summary():
    rows = [r for r in column(1, 1, "A/B:", "C:", split=54)]
    items, cur = [], ""
    for r in rows:
        if r.startswith("•"):
            if cur:
                items.append(cur)
            cur = r[1:].strip()
        else:
            cur += " " + r
    return items + ([cur] if cur else [])


def p11():
    spk = SEC("Speaking", "",
              EX("b11-sa", "A", "Read the short text about Brian Willis, the language expert from the article in <i>Reading</i>. "
                 "Do you agree with the advice he gives? Why? / Why not?", brian()) +
              EX("b11-sb", "B", "Have you ever had any embarrassing moments speaking a foreign language?", "") +
              EX("b11-sc", "C", "What are your ideas about how best to learn a language? Use the following sentence starters to "
                 "write five pieces of advice. Then work in groups. Compare your ideas.",
                 '<p class="starters">It’s important to …<br>It’s best to …<br>Don’t worry too much about …<br>'
                 'Make sure you …<br>It’s better to … than it is to …</p>'))
    lw = [
        "What is the <b>adverb</b> of <i>fluent</i>? " + G("fluently") + " And what is the <b>noun</b>? " + G("fluency"),
        "Is <i>lack</i> a <b>verb</b> or a noun or both? " + G("both"),
        "Where is the <b>stress</b> when you say <i>available</i>? " + G("second syllable|the second syllable|second|the second|on the second syllable|vai"),
        "How do you <b>pronounce</b> <i>foreign</i>? " + REVEAL("/forrin/", "Ответ"),
        "What <b>preposition</b> follows the adjective <i>worried</i>? " + G("about"),
        "What preposition follows the verb <i>rely</i>? " + G("on"),
        "Can you say two <b>phrasal verbs</b> you have learnt in this unit? " + REVEAL("pick up, get by", "Ответ"),
        "What verb <b>collocates</b> (goes) with <i>mistake</i>? " + G("make"),
        "What things can <i>improve</i>? " + REVEAL("language, your English, financial situation, housing, relationships, etc.", "Ответ"),
        "What’s the <b>opposite</b> of <i>a slight accent</i>? " + G("a strong accent|strong accent|strong"),
    ]
    voc = SEC("Vocabulary", "Language words",
              EX("b11-va", "A", "It is a good idea to ask questions about the words you learn. Discuss the answers in teams.", OL(lw)) +
              EX("b11-vb", "B", "Check with your teacher. Who had the most correct?", ""))
    return PAGE_BOX(11, '<div class="cols"><div>' + spk + '</div><div>' + IMG(IMG_DIR + "p11-cartoon.jpg", "") + "</div></div>" + voc)


def p12():
    box = ('<div class="box"><p><b>The past simple:</b> <i>I stayed in and watched TV. / I went to bed as soon as I got home. / '
           'I didn’t hear you.</i></p><hr><p><b>The past continuous:</b> <i>I was chatting to him and he suddenly walked off. / '
           'I’m sorry. I wasn’t listening.</i></p><hr><p><b>The past perfect:</b> <i>He told me he’d asked you. / In the morning, '
           'I realised I’d left my bag in the restaurant.</i></p></div>')
    gr = SEC("Grammar", "Narrative tenses",
             '<p class="ins"><b class="let">A</b> Without looking back at the article on p. 11, see if you can complete Brian '
             'Willis’ story by putting the verbs in the correct tense. You will need to use:</p>' + box +
             X.story_gaps("b12-ga", "", "") +
             EX("b12-gb", "B", "Check your answers. Did you get any wrong? Why?", "") +
             X.tense_usage("b12-gc") + HELP(137) +
             EX("b12-gd", "D", "Work in pairs. Tell your partner about one of the following occasions:",
                UL(["a time when you made a mistake.", "a time when someone didn’t understand what you said.",
                    "a time when something funny happened at school."])))
    lkey = REVEAL("<p>" + "</p><p>".join(_late_answer()) + "</p>", "Ответ (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a conversation between two English-speaking students, Martin and Anna. '
              'They are studying Spanish in Spain.</p>' +
              EX("b12-la", "A", "Work in pairs. Discuss these questions:", UL([
                  "Have you been late for a class or appointment recently?",
                  "How late were you? Why were you late? What happened when you finally arrived?",
                  "How many reasons for being late can you think of?"])) +
              EX("b12-lb", "B", '<span class="audio-ic">♪</span> 1.3 Listen to the conversation and find out why they both got to class late.', S13() + lkey) +
              EX("b12-lc", "C", "In pairs, explain in detail why each person was late to class using the three narrative tenses.", "") +
              EX("b12-ld", "D", "Look at the audioscript on p. 160. Did you use the tenses in the same way?", "") +
              EX("b12-le", "E", "Work in pairs. Would you rent the room? Why? / Why not?", ""))
    pc = SEC("Grammar", "Other uses of the past continuous",
             '<div class="box"><p><b>Sometimes we use the past continuous to emphasise an activity and the fact that it went on '
             'for a period of time.</b></p><hr><p class="ex-line">I was banging on the door and shouting, but nothing.<br>'
             'I’m looking for a flat to rent and I was phoning round a few places this morning before class.</p></div>' +
             X.past_cont("b12-pa") + HELP(137))
    return PAGE_BOX(12, gr + lis + pc)


def _late_answer():
    rows = column(2, 0, "Listening:", "Grammar:")[1:]
    text = " ".join(rows)
    i = text.find("Anna was late")
    return [text[:i].strip(), text[i:].strip()]


def p13():
    sorry = EX("b13-b", "B", "Work in pairs. Take turns saying sorry for being late. Give a different excuse each time. "
               "Reply with some of the expressions below.",
               '<p class="starters">Oh well. Never mind. At least you’re here now.<br>It’s OK. I’ve only just got here myself.<br>'
               'Don’t worry about it. I haven’t been waiting long.</p>')
    steve = REVEAL("<p>" + joined(2, 0, "A: Suggested answer", "02 FEELINGS") + "</p>", "Пример рассказа (ключ)")
    spk = SEC("Speaking", "",
              EX("b13-sa", "A", "Work in pairs. Use the pictures to help you tell the story of why Steve failed his exam.",
                 IMG(IMG_DIR + "p13-steve.jpg", "Steve’s story") + steve) +
              EX("b13-sb", "B", "Have you ever missed or been late for an exam / important meeting / date? What happened?", ""))
    frank = [t for sp, t in script(160, (397, 190, 794, 860)) if "was telling me" in t]
    dc = SEC("Developing conversations", "John was telling me …",
             '<div class="box"><p><b>We often use <i>X was telling me (that)</i> to report what someone said, and then continue '
             'the conversation by adding a comment or a question.</b></p></div>' +
             EX("b13-da", "A", "Can you remember the example of this in the conversation between Anna and Martin in "
                "<i>Listening</i>? What did they say?", REVEAL("A: " + (frank[0] if frank else ""), "Ответ (аудиоскрипт 1.3)")) +
             EX("b13-db", "B", "Work in pairs. Have conversations using the words below. Try to continue each conversation for "
                "as long as possible. For example:",
                '<p class="starters">like tennis / play much</p>' +
                DLG(("A", "John was telling me you like tennis."), ("B", "Yeah, that’s right."), ("A", "Do you play much?")) +
                OL(["lived in Germany / doing there?", "play golf / any good?", "just been on holiday / you go?",
                    "getting married / Congratulations / big day?", "looking for a flat at the moment / any luck?"])) +
             EX("b13-dc", "C", "Work in pairs. Report some of the things other students told you in the first part of this unit. "
                "Have conversations like this:",
                DLG(("A", "<i>X was telling me he / she listens to a lot of music.</i>"), ("B", "<i>Oh yeah? What kind?</i>"))))
    return PAGE_BOX(13, sorry + '<div class="cols"><div>' + spk + '</div><div>' + dc + "</div></div>")


def build():
    return p8() + p9() + p10() + p11() + p12() + p13()
