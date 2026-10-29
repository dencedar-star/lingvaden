"""Страница «Учебник»: Unit 04 Interests, pp. 26–31 (+ Information file 6, p. 157). Длинные тексты — из OCR и ключей."""
import re
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, lines, script, fixed, _fix, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit04/"

FIX.setdefault(162, []).extend([("1: No? What", "J: No? What"), ("!: Am I", "I: Am I"), ("I Why? How", "I: Why? How"),
                                ("1: Go on", "I: Go on"), ("| liked", "I liked"), ("Yeah, It’s", "Yeah, it’s"),
                                ("| think", "I think"), ("lan!", "Ian!"),
                                ("The Lives of Others", "<i>The Lives of Others</i>")])
FIX.setdefault(163, []).extend([("1 don’t", "I don’t"), ("l: I’m speechless", "I: I’m speechless"), ("!: And this", "I: And this"),
                                ("I: Nol", "I: No!"), ("I: 1 can", "I: I can"), ("| go to", "I go to"), (" - ", " – ")])
FIX[30] = [("Bealles", "Beatles"), ("why | learnt", "why I learnt"), ("1 sometimes", "I sometimes"), (" - ", " – ")]
FIX[31] = [("‘1 love", "‘I love"), ("anything: (Kari", "anything.’ [Kari"), ("Wi Go On", "Will Go On"), ("and It’s", "and it’s"),
           (" - ", " – ")]
TITLES = ["Hey Jude", "Love Phantom", "A Little Less Conversation", "The Four Seasons", "Limón Y Sal", "I Wanna Be Like You",
          "The Jungle Book", "Underneath", "My Heart Will Go On", "The Birdie Song"]


def _ital(s):
    for t in TITLES:
        s = re.sub(r"(?<![>\w])" + re.escape(t) + r"(?!\w)", f"<i>{t}</i>", s, count=1)
    return s


def section(p, box, title, img=None):
    ps = [fixed(p, x) for x in paras(p, box, indent=12)]
    ps[0] = ps[0][len(title):].strip()
    body = "".join(f"<p>{_ital(x)}</p>" for x in ps)
    pic = IMG(IMG_DIR + img, title) if img else ""
    return f'<div class="pl"><h4>{title}</h4>{body}{pic}</div>'


def article():
    intro = fixed(30, paras(30, (340, 286, 790, 402))[0])
    parts = [section(30, (362, 435, 578, 600), "All time classics playlist", "p30-classics.jpg"),
             section(30, (362, 720, 775, 858), "That was a great year playlist", "p30-greatyear.jpg"),
             section(31, (35, 80, 362, 258), "Music when I’m down playlist", "p31-down.jpg"),
             section(31, (35, 432, 362, 608), "My family playlist", "p31-family.jpg"),
             section(31, (35, 786, 362, 915), "Music for my worst enemy playlist", "p31-enemy.jpg")]
    return ('<div class="article">' + IMG(IMG_DIR + "p30-banner.jpg", "The playlist of your life", cls="md") +
            f'<p class="lead"><b>{intro}</b></p><div class="colum">' + "".join(parts) + "</div></div>")


def S41():
    ls = [(a, b.replace("shooting I think", "shooting. I think")) for a, b in script(162, (397, 125, 794, 830))]
    return SCRIPT("4.1", "", ls, "162")


def S42():
    return SCRIPT("4.2", "I = Ian, R = Rika", script(162, (397, 845, 794, 1060)) + script(163, (0, 80, 397, 660)), "162–163")


def S44():
    return SCRIPT("4.4", "", [("#", q) for q in X.HOW_LONG], "163")


def p26():
    spk = SEC("Speaking", "", EX("b26-sa", "A", "Work in groups. Discuss these questions:", UL([
        "Look at the picture. Do you have any hobbies like these?", "What did you do at the weekend?",
        "What did you do last night?"])))
    akey = REVEAL(OL([r[2:] for r in numbered(rows(4, 1, 35, 41))]), "Неверные окончания (ключ)")
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(4, 1, 44, 55))]), "Возможные ответы (ключ)")
    voc = SEC("Vocabulary", "Evening and weekend activities", X.endings("b26-va") + akey +
              EX("b26-vb", "B", "Think of two more ways you could finish each sentence starter in exercise A.", bkey))
    lkey = REVEAL(OL([r[2:] for r in numbered(rows(5, 0, 2, 7, split=57))]), "Ответ (ключ)")
    lis = SEC("Listening", "",
              EX("b26-la", "A", '<span class="audio-ic">♪</span> 4.1 Listen to four short conversations and find out what the '
                 "speakers did and when.", lkey) +
              EX("b26-lb", "B", "Listen again. Note down the questions asked.", "") +
              EX("b26-lc", "C", "Do you remember what the answers to the questions were? Role-play the conversations.", "") + S41())
    box = ('<div class="box"><p><b>Hearing words in groups can be confusing. Fluent speakers join words together – especially '
           'when final consonants are followed by vowels.</b></p><p class="ex-line">Not as‿much as‿I used to</p><hr>'
           '<p><b>They also don’t pronounce certain letters – such as when final consonants are followed by a word beginning with '
           'another consonant.</b></p><p class="ex-line">No<s>t</s> as much as I use<s>d</s> to</p></div>')
    pr = SEC("Pronunciation", "Connected speech", box +
             EX("b26-pa", "A", '<span class="audio-ic">♪</span> 4.1 Listen to the fourth conversation (between Jason and '
                "Mohammed) again – and read the audioscript on p. 162. Notice the linking and missing sounds. Practise reading "
                "the conversation.", REVEAL(IMG(IMG_DIR + "p157-file6.jpg", "File 6: linking and missing sounds", cls="md"),
                                            "File 6, p. 157 (связки и непроизносимые звуки)")))
    return PAGE_BOX(26, IMG(IMG_DIR + "p26-banner.jpg", "04 Interests") +
                    '<div class="cols"><div>' + spk + voc + '</div><div>' + lis + pr + "</div></div>" +
                    IMG(IMG_DIR + "p26-park.jpg", ""))


def p27():
    gbox = ('<div class="box"><p><b>We can ask about frequency in the present with these patterns:</b></p><hr>'
            '<p class="ex-line"><i>Do you</i> + verb + <i>much / a lot?</i><br><i>How often do you</i> + verb?<br>'
            '<i>Do you ever</i> + verb?</p></div>')
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">Nearly every day, unless I’m really '
                'busy.<br>Most weekends, unless it’s raining.<br>I usually play on Saturdays, unless I’m away on business.<br>'
                'I never missed a lesson, unless I was really ill.<br>He used to see us every day, unless we were away.</p></div>')
    gr = SEC("Grammar", "Frequency (present and past)", gbox + X.freq("b27-ga") +
             EX("b27-gb", "B", "Underline all the frequency expressions. Translate them. Then discuss these questions.", UL([
                 "What tense do we use in English when talking about frequency in the present?",
                 "Which two structures do we use in English when talking about frequency in the past?"])) +
             patterns + EX("b27-gc", "C", "Work in groups of three or four. Ask about habits using the questions and patterns in "
                           "exercise A.", "") + HELP(142))
    dbox = ('<div class="box"><p><b>Look at this extract from the fourth conversation in <i>Listening</i>. Notice how the short '
            'answer is explained.</b></p><hr>' +
            DLG(("A", "So are you any good?"), ("B", "I’m OK. I’m quite good in defence, but I’m useless at shooting. I think the "
                                                    "last time I scored a goal was about three years ago.")) + "</div>")
    dc = SEC("Developing conversations", "Are you any good?", dbox + X.any_good("b27-da") +
             EX("b27-db", "B", "Ask each other about your abilities in sports, music etc., using <i>Are you any good …?</i> "
                "Explain your answers fully.", ""))
    cp = SEC("Conversation practice", "",
             EX("b27-ca", "A", "Have a similar conversation to the one in File 6 on p. 157, but choose a different sport or "
                "activity. Spend two minutes thinking about how to answer the questions. Start by saying <i>‘So did you have a "
                "nice weekend?’</i>", ""))
    return PAGE_BOX(27, '<div class="cols"><div>' + IMG(IMG_DIR + "p27-woman.jpg", "") + gr + '</div><div>' + dc + cp +
                    "</div></div>")


def p28():
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(5, 0, 42, 48, split=57))]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a conversation about a martial art between Ian and Rika. They are both '
              'sales reps for a large publishing company. Ian is visiting Rika in Japan.</p>' +
              EX("b28-la", "A", "Before you listen, work in pairs. Discuss these questions:", UL([
                  "Which martial arts do you know?", "Have you ever done any martial arts?",
                  "Have you ever entered any sports tournaments or competitions? How did you get on?"])) +
              EX("b28-lb", "B", '<span class="audio-ic">♪</span> 4.2 Listen and answer these questions.', OL([
                  "Why is Rika famous?", "How often does she practise her martial art?", "Why didn’t Ian know about this?"]) + bkey) +
              X.rika_tf("b28-lc", "C", "Work in pairs. Decide if these sentences about the conversation are true or false. Can "
                        "you remember what Ian and Rika actually said? Listen again and check if you need to.") + S42() +
              EX("b28-ld", "D", "Work in groups of three. Discuss these questions:", UL([
                  "Do you know anyone who does something in their free time that other people might find surprising?",
                  "Do you know anyone who was bullied at school? Why?", "Do you know anyone who is big-headed? In what way?"])))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>kind of</i></b></p>'
              '<p>People often use <i>kind of</i> to modify an adjective or a verb. It means <i>more or less, but not exactly</i>.</p>'
              '<p><i>He’s been on TV a few times, so he’s kind of famous now!<br>'
              'I didn’t really plan to do it. It just kind of happened!</i></p></div>')
    voc = SEC("Vocabulary", "Problems and sports",
              '<p class="intro">Rika hurt her back fighting in a competition. Here are some other problems you can have during or '
              'after sports activities.</p>' + X.sport_problems("b28-va") +
              EX("b28-vb", "B", "Have you ever had any of the problems in exercise A? What happened?", ""))
    return PAGE_BOX(28, '<div class="cols"><div>' + lis + native + IMG(IMG_DIR + "p28-skiing.jpg", "How was your skiing trip?",
                                                                         cls="md") +
                    '</div><div>' + voc + IMG(IMG_DIR + "p28-runners.jpg", "", cls="md") + "</div></div>")


def p29():
    gr = SEC("Grammar", "Duration", X.dur_mistakes("b29-ga") + X.dur_rules("b29-gb") + X.dur_choose("b29-gc") +
             EX("b29-gd", "D", "Work in pairs. Tell your partner about a sport or hobby you do now, and one you used to do in the "
                "past. Your partner should reply: <i>Really? How long have you been …? / Really? How long did you …?</i> Ask "
                "further questions to develop the conversation.", "") + HELP(143))
    pr = SEC("Pronunciation", "Auxiliaries",
             '<p class="intro"><i>How long</i> is used with other tenses as well as the past simple and the present perfect '
             'continuous. It is easy to mishear these questions because the auxiliary verb is pronounced very softly.</p>' +
             EX("b29-pa", "A", '<span class="audio-ic">♪</span> 4.3 Listen to these words from some questions. Repeat them.',
                '<p class="ex-line">was your · do you · were you · did it · are you · will it · have you · does it</p>') +
             X.how_long("b29-pb") + S44())
    spk = SEC("Speaking", "",
              EX("b29-sa", "A", "Work in groups of three or four. Look at the list below. Find out who ‘wins’ each category in the "
                 "list. Try to win as many categories as you can by talking about yourself or about people you know. Take turns "
                 "to start. Ask <i>How long …?</i> questions to find out extra details. For example:",
                 DLG(("A", "I think my grandparents have had the longest marriage."), ("B", "Why? How long have they been married?"),
                     ("A", "51 years!")) + UL([
                     "the longest marriage", "the shortest journey to this class today", "the longest journey to work",
                     "studying English the shortest length of time", "the longest flight", "the most time spent on their homework",
                     "the longest wait for a plane or train", "the shortest time in their current house",
                     "the longest film you have seen"])))
    return PAGE_BOX(29, '<div class="cols"><div>' + gr + '</div><div>' + pr + spk + IMG(IMG_DIR + "p29-couple.jpg", "", cls="md") +
                    "</div></div>")


def p30():
    mean = REVEAL("<p>" + "<br>".join(rows(5, 1, 33, 41, split=57)) + "</p>", "Значения выражений (ключ)")
    dc = SEC("Developing conversations", "Music, films and books",
             '<p class="intro">We often move from more general questions to more specific.</p>' + X.music_order("b30-da") + mean +
             EX("b30-db", "B", '<span class="audio-ic">♪</span> 4.5 Listen and check your answers.', "") +
             EX("b30-dc", "C", "Have similar conversations about music, books, films, and TV programmes. Try and re-use the "
                "expressions in <b>bold</b> in exercise A.", ""))
    styles = ["pop", "jazz", "blues", "heavy metal", "folk", "techno", "hip-hop", "R&amp;B / Soul", "classical", "salsa"]
    adj = ["If a song is <b>catchy</b>, you quickly want to sing it and can’t stop.",
           "If music is <b>repetitive</b>, it has the same boom, boom beat all the way through.",
           "If it’s <b>heavy</b> or loud, it’s very noisy.", "If it’s <b>soft</b>, it’s quiet.",
           "If we say the music or lyrics – the words to the song – are <b>sentimental</b>, they are romantic or sad in a bad way.",
           "If we say a song is very <b>commercial</b>, it is a negative way of saying it is written to sell lots of records.",
           "If music or songs are <b>moving</b>, they make you cry.", "If music is <b>bland</b>, it’s boring.",
           "If music is <b>uplifting</b>, it makes you happy or hopeful.", "If music is <b>depressing</b>, it makes you sad."]
    vkey = REVEAL(OL([r.split(" ", 1)[1] for r in rows(5, 1, 45, 56, split=57)]), "Возможные ответы (ключ)")
    voc = SEC("Vocabulary", "Music", X.wordbox(styles) +
              EX("b30-va", "A", "Look at the adjectives in bold in 1–10 below. Discuss which adjectives you would personally use "
                 "to describe the kinds of music in the box.", OL(adj) + vkey))
    return PAGE_BOX(30, dc + voc)


def p31():
    bkey = REVEAL("<p>" + " ".join(rows(6, 0, 2, 16, split=62)).replace(" • ", "<br>• ") + "</p>", "Ответ (ключ)")
    songs = ["<i>Hey Jude</i> (The Beatles)", "<i>Love Phantom</i> (B’z)", "<i>A Little Less Conversation</i> (Elvis Vs JXL)",
             "<i>The Four Seasons</i> (Vivaldi)", "<i>Limón Y Sal</i> (Julieta Venegas)",
             "<i>I Wanna Be Like You</i> (from The Jungle Book)", "<i>Underneath</i> (Lincoln)",
             "<i>My Heart Will Go On</i> (Céline Dion)", "<i>The Birdie Song</i> (The Tweets)"]
    read = SEC("Reading", "",
               '<p class="intro">You are going to read about some pieces of music.</p>' +
               EX("b31-ra", "A", "Before you read, work in pairs. Look at the song titles and artists. Do you know any of them? "
                  "Do you like them?", '<div class="note">' + UL(songs) + "</div>") +
               article() +
               EX("b31-rb", "B", "Read the magazine article and find out if the readers like the songs in exercise A or not – and "
                  "if they do, why.", bkey) +
               X.readers("b31-rc", "C", "Work in pairs. Discuss these questions. Which of the people you read about:") +
               X.article_words("b31-rd", "D", "Correct the words in <i>italics</i> with words in the article. Then work in pairs. "
                               "Discuss if any of the sentences are true for you."))
    spk = SEC("Speaking", "", EX("b31-sa", "A", "Work in pairs. Choose three of the following playlist titles and make a list of "
                                 "three songs you would have. Compare lists with your partner.", UL([
                                     "My current favourites", "That reminds me of …", "Party music", "Music I can’t stand",
                                     "Music for my funeral", "Music to sleep to", "Music for a romantic evening",
                                     "I can’t get it out of my head"])))
    return PAGE_BOX(31, read + spk)


def build():
    return p26() + p27() + p28() + p29() + p30() + p31()
