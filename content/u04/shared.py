"""Упражнения модуля 4, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, TF, EX, OL, DLG, ORDER

AH = list("abcdefgh")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


# p. 26, Vocabulary A: (начало, варианты, неверный по ключу)
ENDINGS = [("I stayed in and …", ["studied", "played football", "took it easy", "tidied up"], "played football"),
           ("I played …", ["roller-blading", "on the computer", "golf", "tennis"], "roller-blading"),
           ("I went …", ["clubbing", "a run", "cycling", "walking in the country"], "a run"),
           ("I went for …", ["a meal", "a ride on my bike", "the gym", "a swim"], "the gym"),
           ("I went to …", ["the cinema", "shopping", "Karen’s house for dinner", "a bar to watch the football"], "shopping")]


def endings(id, letter="A", instr="Which of the four endings are not correct?"):
    """p. 26, Vocabulary A. Ключ: 1 played football 2 roller-blading 3 a run 4 the gym 5 shopping."""
    return EX(id, letter, instr + ' <span style="font-weight:400">Выберите неверное окончание.</span>',
              OL([f"{s}<br>{C(k, *o)}" for s, o, k in ENDINGS]))


FREQ_BOX = ["every", "used", "quite", "all", "hardly", "’d", "that"]


def freq(id, letter="A", instr="Complete the sentences with the words in the box."):
    """p. 27, Grammar A. Ключ: 1 all 2 every 3 quite 4 that 5 hardly 6 ’d 7 used to."""
    rows = [DLG(("A", "So do you read much?"), ("B", f"Yeah, {G('all')} the time. I read at least a book a week.")),
            DLG(("A", "Do you go swimming a lot?"), ("B", f"Yeah, nearly {G('every')} day, unless I’m really busy.")),
            DLG(("A", "Do you go to the cinema much?"), ("B", f"Yeah, {G('quite')} a lot. I probably go once every two weeks.")),
            DLG(("A", "How often do you play games on the computer?"),
                ("B", f"Not {G('that')} often, actually. It’s not really my kind of thing.")),
            DLG(("A", "So how often do you go to the gym?"),
                ("B", f"{G('hardly|Hardly')} ever now, to be honest. Today was the first time in ages. I used to go more often.")),
            DLG(("A", "Do you ever watch your favourite team play?"),
                ("B", f"Yeah, but not as much as I{G('’d|would')} like to. I only went four times last season.")),
            DLG(("A", "Do you eat out a lot?"),
                ("B", f"Not as much as we {G('used')} to. Before we were married, we went out all the time."))]
    return EX(id, letter, instr, wordbox(FREQ_BOX) + OL(rows))


SPORTS = ["basketball", "rollerblading", "judo", "football", "swimming", "table tennis", "tennis", "skiing"]
GOOD = [("<b>No, I’m useless</b>. I usually hit the ball out of the court or into the net.", "tennis"),
        ("No, I’m useless. I can’t even kick the ball in a straight line.", "football"),
        ("<b>No, not really</b>. I can do a hundred metres breaststroke, but that’s all. I can’t do the front crawl.", "swimming"),
        ("No, not really. I can stand up and go in a straight line, but that’s all. I can’t do turns or go backwards.",
         "rollerblading"),
        ("<b>I’m OK</b>. We had a table at home, so I used to play quite a lot.", "table tennis"),
        ("I’m OK. I can do the basic moves, but nothing complicated.", "judo"),
        ("<b>Yeah, quite good</b>. I can do black runs, but I go down them slowly!", "skiing"),
        ("Yeah, quite good. I used to be in a team. I used to be good at free throws.", "basketball")]


def any_good(id, letter="A", instr="Decide which of these activities the people are talking about in sentences 1–8."):
    """p. 27, Developing conversations A. Ключ: 1 tennis 2 football 3 swimming 4 roller-blading 5 table tennis 6 judo 7 skiing
    8 basketball."""
    opts = sorted(SPORTS)
    return EX(id, letter, instr, wordbox(SPORTS) + OL([f"{t} → {S(k, opts)}" for t, k in GOOD]))


RIKA_TF = [("Someone asked Rika to sign a piece of paper.", "T"), ("Rika won the judo tournament she entered.", "F"),
           ("You need to be tall to do judo.", "F"), ("Rika started doing judo when she was a child.", "T"),
           ("Her teachers at school persuaded her to start doing it.", "F"), ("Rika boasts about how good she is.", "F"),
           ("She hurt herself last year because she had not prepared for her fight properly.", "T"),
           ("Rika found it easy to start fighting again after her injury.", "F")]


def rika_tf(id, letter="C", instr="Decide if these sentences about the conversation are true or false."):
    """p. 28, Listening C. Ключ: 1 T 2 F 3 F 4 T 5 F 6 F 7 T 8 F."""
    return EX(id, letter, instr, OL([f"{s} {TF(k)}" for s, k in RIKA_TF]))


PROB_BOX = ["banged", "fell", "stiff", "unfit", "bloody", "broke", "beat", "pulled"]


def sport_problems(id, letter="A", instr="Complete the sentences with the words in the box."):
    """p. 28, Vocabulary A. Ключ: 1 unfit 2 stiff 3 pulled 4 beat 5 broke 6 banged 7 bloody 8 fell."""
    rows = [f"I went running with a friend, but I had to stop after ten minutes. I’m so {G('unfit')}!",
            f"We did a twenty-mile walk yesterday, so my legs are really {G('stiff')} this morning.",
            f"I didn’t really warm up before we started playing and so I {G('pulled')} a muscle in my leg.",
            f"I hadn’t played for ages, which is why he {G('beat')} me so easily.",
            f"I was playing football and {G('broke')} my leg. It was in plaster for six weeks.",
            f"I fell off my bike and {G('banged')} my head. Luckily, I was wearing a helmet.",
            f"My son kicked a ball in my face and gave me a {G('bloody')} nose.",
            f"I injured my back skating. I tried to stand up and I slipped and {G('fell')} backwards."]
    return EX(id, letter, instr, wordbox(PROB_BOX) + OL(rows))


DUR_MIST = [("Rika usually practises all the techniques during at least an hour a day.",
             "Rika usually practises all the techniques for at least an hour a day."),
            ("After her injury, Rika didn’t fight since a couple of months.",
             "After her injury, Rika didn’t fight for a couple of months."),
            ("She’s doing quite a lot of yoga for the last few months.",
             "She’s been doing quite a lot of yoga for the last few months."),
            ("She used to get into fights since she was at school.", "She used to get into fights when she was at school."),
            ("She’s been doing judo ever from she was a kid.", "She’s been doing judo ever since she was a kid.")]


def dur_mistakes(id, letter="A", instr="Find the grammatical mistakes in these sentences from the conversation in "
                 "<i>Listening</i>. Correct the mistakes."):
    """p. 29, Grammar A. Ответы — ключ."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in DUR_MIST]))


def dur_rules(id, letter="B", instr="Compare the sentences with the audioscript on pp. 162–163 and complete the rules."):
    """p. 29, Grammar B. Ключ: for, since, present perfect (continuous), past."""
    pp = "present perfect continuous|present perfect|present perfect (continuous)|present perfect simple or continuous"
    return EX(id, letter, instr,
              '<div class="box"><p><b>Rules</b></p>'
              f"<p>Use {G('for')} (not <i>during</i>) with periods of time in the past and present.</p>"
              f"<p>Use {G('since')} to show the <i>start</i> of a period of time from the past to now.</p>"
              f"<p>Use the {G(pp, 'wide')} tense to talk about periods including now.</p>"
              f"<p>Use the {G('past|past simple')} tense to talk about periods of time which are finished.</p></div>")


def dur_choose(id, letter="C", instr="Choose the correct word or words in italics."):
    """p. 29, Grammar C. Ключ: 1 since; for 2 for 3 ever since; I’ve been 4 were you 5 have you been; Since 6 did you do; Until."""
    rows = [DLG(("A", f"I’ve been doing yoga off and on {C('since', 'for', 'since')} January, but I didn’t warm up before the "
                      f"class one day and pulled a muscle, so I didn’t go {C('for', 'for', 'during')} a while."),
                ("B", "Really? You need to be careful.")),
            DLG(("A", f"I played him every week {C('for', 'from', 'for')} about five years, but only managed to beat him once!"),
                ("B", "I’m not surprised you gave up.")),
            DLG(("A", f"My brother’s been able to ski {C('ever since', 'from', 'ever since')} I can remember. He does a lot of "
                      "off-piste skiing."),
                ("B", f"Wow. That’s amazing. {C('I’ve been', 'I’m', 'I’ve been')} learning for a week now and I can only go "
                      "about 100 metres before I fall down!")),
            DLG(("A", "I think I spent too long in the gym yesterday. I’m really stiff this morning."),
                ("B", f"How long {C('were you', 'were you', 'have you been')} there for?"), ("A", "About two hours!")),
            DLG(("A", "I’ve got my judo class tonight."),
                ("B", f"How long {C('have you been', 'are you', 'have you been')} doing that?"),
                ("A", f"{C('Since', 'Since', 'For')} last year. I feel so much fitter – and I’ve also managed to lose five kilos.")),
            DLG(("A", "I used to play for a local team."),
                ("B", f"How long {C('did you do', 'did you do', 'have you been doing')} that?"),
                ("A", f"{C('Until', 'Until', 'Since')} quite recently, actually. I injured my knee really badly last season and "
                      "had to give up."))]
    return EX(id, letter, instr, OL(rows))


HOW_LONG = ["How long was your flight delayed?", "How long do you want to stay?", "How long were you waiting?",
            "How long did it take you to get home?", "How long are you going to go for?", "How long will it take to repair?",
            "How long have you been seeing Dan?", "How long does it take you to get here?"]


def how_long(id, letter="B", instr='<span class="audio-ic">♪</span> 4.4 Listen and write down the eight <i>How long …?</i> '
             "questions."):
    """p. 29, Pronunciation B. Ответы — аудиоскрипт 4.4 (с. 163); в пропуске — слабо произносимые слова из 4.3."""
    rows = []
    for q in HOW_LONG:
        w = q[9:-1].split()
        rows.append(f"How long {G(' '.join(w[:2]))} {' '.join(w[2:])}?")
    return EX(id, letter, instr + ' <span style="font-weight:400">Без аудио: вставьте пропущенные слова (<i>was your, do you, '
              "were you, did it, are you, will it, have you, does it</i>).</span>", OL(rows))


# p. 30, Developing conversations A: (реплика, номер по ключу)
MUSIC_CONV = [("Erm, I don’t know … Girls Rock!, Soul Train, <b>stuff like that</b>.", 6),
              ("<b>All sorts</b> really, <b>but mainly</b> pop music and R&amp;B.", 4),
              ("Oh right. <b>Anyone in particular?</b>", 5), ("Yeah, all the time.", 2),
              ("So <b>have</b> you bought <b>anything good recently</b>?", 7), ("<b>What kind of</b> music <b>are you into</b>?", 3),
              ("<b>Do you</b> listen to music <b>much</b>?", 1), ("Well, I downloaded this great song by K Boy. It’s fantastic.", 8)]


def music_order(id, letter="A", instr="Put the conversation into the correct order."):
    """p. 30. Порядок — по ключу (pp. 30–31, Developing Conversations A)."""
    nums = [str(i) for i in range(1, 9)]
    rows = [f'<div class="ord-row">{"<b>1</b>" if k == 1 else S(str(k), nums)} <span>{t}</span></div>' for t, k in MUSIC_CONV]
    return EX(id, letter, instr, '<div class="ord">' + "".join(rows) + "</div>")


READERS = ["Toshi", "Corina", "Kari", "Natalia", "Kevin", "Kari, Kevin"]
WHO = [("likes different kinds of music to her father?", "Natalia"), ("finds some songs drive him mad?", "Kevin"),
       ("uses the Internet to access music?", "Corina"), ("went to a concert by one of his favourite bands?", "Toshi"),
       ("predicts that one band will become famous?", "Natalia"), ("talks about special ceremonies?", "Kari, Kevin")]


def readers(id, letter="C", instr="Which of the people you read about:"):
    """p. 31, Reading C. Ключ: 1 Natalia 2 Kevin 3 Corina 4 Toshi 5 Natalia 6 Kari, Kevin."""
    return EX(id, letter, instr, OL([f"{q} {S(k, READERS)}" for q, k in WHO]))


ART_WORDS = [("I love singing", "together", "along", "with songs. I like karaoke."),
             ("I’ve seen lots of bands", "lively", "live", "."),
             ("There’s a song which really", "remembers", "reminds", "me of my father."),
             ("There’s a song I dance to whenever it", "puts", "comes|is put|comes on", "on in a club."),
             ("If I’m sad, I like to play something sad to", "same", "match", "my mood."),
             ("I like to study with music on in the", "behind", "background", "."),
             ("Classical music doesn’t", "feel", "do", "anything for me. It’s bland."),
             ("I don’t like", "sensitive", "sentimental", "songs about love and romance."),
             ("I’ve sometimes", "made", "done", "a stupid dance to some music.")]


def article_words(id, letter="D", instr="Correct the words in <i>italics</i> with words in the article."):
    """p. 31, Reading D. Ключ: 1 along 2 live 3 reminds 4 comes / is put 5 match 6 background 7 do 8 sentimental 9 done."""
    rows = [f"{a} <s><i>{w}</i></s> {G(k)}{'' if b == '.' else ' '}{b}" for a, w, k, b in ART_WORDS]
    return EX(id, letter, instr, OL(rows))


# ---- Writing 04 (pp. 126–127) ----
REQ = ["I was wondering …", "Do you think you could …", "Is there any way …", "Could you do me a favour …"]
REQ_END = ["and pay for it now and then I’ll pay you back later?",
           "if you could possibly send me some information about the French courses you offer?",
           "you could translate this letter for me?", "give him a ring and speak to him about it?"]


def requests(id, letter="A", instr="Match the sentence beginnings and endings to make requests."):
    """p. 126, Grammar A. Ключ: 1 b 2 d 3 c 4 a."""
    key = ["b", "d", "c", "a"]
    return EX(id, letter, instr, OL([f"{q} {S(k, AH[:4])}" for q, k in zip(REQ, key)]) + OL(REQ_END, "items alpha"))


def emails(id, letter="B", instr="Complete the emails with one word in each gap."):
    """pp. 126–127, Writing B. Ключ: 1 a made b think c soon 2 a say b chance c like / love 3 a busy b favour c be
    4 a let b wondering c All."""
    def mail(n, html):
        return f'<div class="note"><h4>{n}</h4>{html}</div>'
    m1 = ("<p>Dear Sir/Madam,</p>"
          f"<p>I have already <sup>a</sup>{G('made')} a reservation under the name of Rosario for the 18th–20th January. Would "
          f"it be possible to stay an extra night on Saturday 21<sup>st</sup> January? If not, do you <sup>b</sup>{G('think')} "
          f"you could inform me as <sup>c</sup>{G('soon')} as possible as I would then need to make other arrangements.</p>"
          "<p>Many thanks.</p><p>Yours faithfully,<br>Sandra Rosario</p>")
    m2 = ("<p>Hi Zarina,</p>"
          f"<p>Just a quick one to <sup>a</sup>{G('say')} thanks for the email. I love the photos! Is there any "
          f"<sup>b</sup>{G('chance')} you could print them out, though, as my printer isn’t very good and I’d "
          f"<sup>c</sup>{G('like|love')} to frame the photos and put them on my wall?</p><p>Michaele</p>")
    m3 = ("<p>Dear Margot,</p>"
          f"<p>Long time, no see. How are you? I’ve been very <sup>a</sup>{G('busy')} finishing my final dissertation for my "
          "degree, so I haven’t been out much. I’ve attached it here. As your English is so good, could you do me a big "
          f"<sup>b</sup>{G('favour')} and look through it carefully to check it’s OK? I’d <sup>c</sup>{G('be')} really "
          "grateful.</p><p>Cheers for now,<br>Olaf</p>")
    m4 = ("<p>Dear Mario,</p>"
          f"<p>Just a quick email to <sup>a</sup>{G('let')} you know when I’ll be arriving in Milan. The flight gets in at 05.10 "
          f"on Friday morning. Actually, I was <sup>b</sup>{G('wondering')} if you could possibly come and pick me up, if it’s "
          "not too much trouble? I’d be really grateful as I’ll have loads of luggage.</p>"
          f"<p><sup>c</sup>{G('All|all')} the best,<br>Andre</p>")
    return EX(id, letter, instr, mail(1, m1) + mail(2, m2) + mail(3, m3) + mail(4, m4))


AS_ORDER = [("as as possible soon", "as soon as possible"), ("as know far I as", "as far as I know"),
            ("can as quickly as you", "as quickly as you can"), ("you as soon as hear", "as soon as you hear"),
            ("arrive soon you as as", "as soon as you arrive"), ("as the concerned as is far hotel", "as far as the hotel is concerned")]


def as_order(id, letter="A", instr="Put the words in the correct order to make six expressions."):
    """p. 127, Vocabulary A. Ключ: 1 as soon as possible 2 as far as I know 3 as quickly as you can 4 as soon as you hear
    5 as soon as you arrive 6 as far as the hotel is concerned."""
    rows = [f"<i>{s}</i>" + ORDER(s, a) for s, a in AS_ORDER]
    return EX(id, letter, instr + ' <span style="font-weight:400">Нажимайте на слова по порядку; повторное нажатие возвращает '
              "слово.</span>", OL(rows))


def as_gaps(id, letter="B", instr="Complete the sentences with the expressions in exercise A."):
    """p. 127, Vocabulary B. Ключ: a as soon as you hear b as quickly as you can c as soon as you arrive
    d As far as the hotel is concerned e as soon as possible f As far as I know."""
    W = lambda a: G(a, "wide")
    rows = [f"Do you think you could email me {W('as soon as you hear')} any news as I’m a bit worried about him?",
            f"When you arrive, you need to go {W('as quickly as you can')} to Terminal B as there isn’t much time for the transfer "
            "between flights.",
            f"Give me a call {W('as soon as you arrive')} at the station and I’ll come and pick you up. Just wait outside the main "
            "entrance.",
            f"{W('As far as the hotel is concerned')}, it’s all booked and confirmed. Is there any way you could sort out the car "
            "hire, though, as I don’t have a driving licence?",
            f"Could you let me know {W('as soon as possible')} whether you can come or not as we need to make the booking?",
            f"{W('As far as I know')}, the shuttle bus runs all night, but perhaps you should ring the tourist information office "
            "to check."]
    return EX(id, letter, instr, OL(rows, "items alpha"))
