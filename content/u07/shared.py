"""Упражнения модуля 7, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, EX, OL, DLG

AH = list("abcdefgh")
NOUNS = ["deadline", "essay", "exams", "lecture", "modules", "seminar", "tutor(s)", "workload"]


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


COLL = [("write an ~ / hand in an ~ / a fifteen-hundred word ~", "essay"),
        ("dedicated and supportive ~ / my personal ~ / very helpful ~", "tutor(s)"),
        ("my end-of-year ~ / my final ~ / pass all my ~ / fail my ~", "exams"),
        ("have a weekly ~ / a group ~ / go to a ~ / ~ discussions", "seminar"),
        ("give a ~ / fall asleep in a ~ / a fascinating ~ / ~ theatre", "lecture"),
        ("a heavy ~ / a lighter ~ / increase the ~ / cope with the ~", "workload"),
        ("a very tight ~ / miss the ~ / extend a ~ / the ~ is Friday", "deadline"),
        ("choose which ~ to do / core ~ / optional ~ / the ~ are hard", "modules")]


def courses(id, letter="A", instr="Add the nouns in the box to the groups of words they go with a–h."):
    """p. 48, Vocabulary A. Ключ: a essay b tutor(s) c exams d seminar e lecture f workload g deadline h modules."""
    return EX(id, letter, instr, wordbox(NOUNS) + OL([f"{S(k, NOUNS)} — {t}" for t, k in COLL], "items alpha"))


# p. 49, Developing conversations A: (как в учебнике, правильные варианты по ключу)
DC = [("I’ve had a few ups and supportive of course, but the tutors have been very helpful and downs.",
       "I’ve had a few ups and downs of course, but the tutors have been very helpful and supportive."),
      ("Quite well, actually. The seminar can be a bit boring, but the lectures work in groups is great.",
       "Quite well, actually. The lectures can be quite boring but the seminar work in groups is great.|"
       "Quite well, actually. The lectures can be a bit boring, but the seminar work in groups is great."),
      ("OK, but I’ve got my final revision next week, so I’m having to do lots of exams at the moment.",
       "OK, but I’ve got my final exams next week, so I’m having to do lots of revision at the moment."),
      ("OK, but I’m really busy. I have to hand in an deadline next week – and if I miss the essay, I’ll fail!",
       "OK, but I’m really busy. I have to hand in an essay next week – and if I miss the deadline I’ll fail.|"
       "OK, but I’m really busy. I have to hand in an essay next week and if I miss the deadline I’ll fail."),
      ("Actually, I’m struggling at the moment. I just can’t demanding with the workload. It’s really cope.",
       "Actually I’m struggling at the moment. I just can’t cope with the workload. It’s really demanding."),
      ("To be honest, I’m finding it really term. The modules I’m doing this difficult are really hard!",
       "To be honest, I’m finding it really difficult. The modules I’m doing this term are really hard!")]


def dc_fix(id, letter="A", instr="Look at the answers 1–6 to the question <i>How’s the course going?</i> Two words in each "
           "answer are in the wrong position. Write each answer correctly."):
    """p. 49, Developing conversations A. Ответы — ключ."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in DC]))


def listen71(id, letter="A", instr='<span class="audio-ic">♪</span> 7.1 Listen and complete the questions.'):
    """p. 49, Listening A. Ключ: 1 enjoying it 2 kind of things 3 get on with 4 like 5 do you finish 6 you decided."""
    rows = [f"How’s the course going? Are you {G('enjoying it')}?",
            f"So what does that involve, then? I mean, what {G('kind of things')} do you have to study?",
            f"And what are the other students like? Do you {G('get on with')} them OK?",
            f"And what about the tutors? What are they {G('like')}?",
            f"How long does the course last? When {G('do you finish')}?",
            f"And what are you going to do once the course has finished? Have {G('you decided')} yet?"]
    return EX(id, letter, instr, OL(rows))


BOLD = [("go through", "look at and read again"), ("thick", "not very intelligent"),
        ("pushy", "strongly encourage someone to do something"), ("bright", "very intelligent, smart"),
        ("points to", "shows something as an example"), ("relevant", "important to the topic"),
        ("recite", "say something back"), ("parenthood", "to be a mother or father"),
        ("core (subject)", "a main subject"), ("rigid", "unbending")]


def bold_words(id, letter="B", instr="Match the words in bold in the article with their meanings."):
    """p. 50, Reading B. Значения — ключ."""
    opts = sorted(d for _, d in BOLD)
    return EX(id, letter, instr, OL([f"<b>{w}</b> → {S(d, opts)}" for w, d in BOLD]))


def families(id, letter="A", instr="Add the missing words to these word families. One of each of the forms is in the article."):
    """p. 50, Vocabulary A. Ключ: education, failure, achievement, calculate, appreciate, encourage, inspiration."""
    rows = [(f"state {G('education')}", "<b>educate</b> children privately"),
            (f"feel like a {G('failure')}", "<b>fail</b> your exam"),
            (f"a big {G('achievement')}", "<b>achieve</b> all your ambitions"),
            ("do a <b>calculation</b>", f"{G('calculate')} the answer in my head"),
            ("wine <b>appreciation</b>", f"{G('appreciate')} the good things in life"),
            ("give a lot of <b>encouragement</b>", f"{G('encourage')} me to work hard"),
            (f"have no {G('inspiration')}", "<b>inspire</b> me to success")]
    return EX(id, letter, instr, '<table class="voc"><tr><th>noun</th><th>verb</th></tr>' +
              "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + "</table>")


STS = [("She’s very patient.", "teacher|student", "+"), ("It’s quite rough.", "school", "−"),
       ("She’s very studious.", "student", "+"), ("He’s good at controlling the class.", "teacher", "+"),
       ("It’s got a very good reputation for sport.", "school", "+"), ("She’s quite traditional.", "teacher", "−"),
       ("He really pushes us.", "teacher", "+"), ("She never pays attention in class.", "student", "−"),
       ("Discipline is very good there.", "school", "+"), ("She thinks she knows it all.", "student|teacher", "−"),
       ("It has a very good headmaster.", "school", "+"), ("She’s very encouraging.", "teacher", "+"),
       ("He’s very bright.", "student", "+"), ("She’s in serious trouble because she keeps skipping classes.", "student", "−"),
       ("He’s lively and makes things fun.", "teacher", "+"), ("There are hardly any facilities.", "school", "−")]


def sts(id, letter="A", instr="Read sentences 1–16 and decide whether each describes a school, a teacher or a student, and "
        "if it is a positive (+) or negative (−) description."):
    """p. 52, Vocabulary A. Ключ: 1 teacher (student) + … 16 school −."""
    who = ["school", "teacher", "student"]
    return EX(id, letter, instr, OL([f"{t} → {S(w, who)} {S(pn, ['+', '−'])}" for t, w, pn in STS]))


SPEAKERS = ["a parent", "a school teacher", "a university lecturer", "an overseas student", "a postgraduate student"]


def conv72(id, letter="A", instr='<span class="audio-ic">♪</span> 7.2 Listen and decide who the main speaker is in each '
           "case. Note that there is one person you do not need to use."):
    """p. 52, Listening A. Ключ: 1 b 2 d 3 c 4 a."""
    return EX(id, letter, instr, OL(SPEAKERS, "items alpha") +
              "".join(f"<p>Conversation {i} → {S(k, AH[:5])}</p>" for i, k in zip(range(1, 5), "bdca")))


def verbs72(id, letter="C", instr="Which verbs went with these nouns in the four conversations? Complete the collocations."):
    """p. 52, Listening C. Ключ: 1 don’t pay attention; whispering to each other; gain their respect 2 misread one of the
    questions; lowered my score; re-take the test 3 miss a deadline; make an exception; accept any excuses 4 push the kids;
    skipping classes; has a very good reputation."""
    rows = [f"{G('don’t pay|pay')} attention · {G('whispering|whisper')} to each other · {G('gain')} their respect",
            f"{G('misread')} one of the questions · {G('lowered|lower')} my score · {G('re-take|retake|take')} the test",
            f"{G('miss')} a deadline · {G('make')} an exception · {G('accept')} any excuses",
            f"{G('push')} the kids · {G('skipping|skip')} classes · {G('has|have')} a very good reputation"]
    return EX(id, letter, instr, OL(rows))


COND = [("If I try to explain something, …", "they sit whispering to each other.|"
         "half of them just sit there whispering to each other.|they just sit there whispering to each other."),
        ("If they talk, …", "send them to the headmaster.|send them to the headmaster or give them a detention.|"
         "just send them to the headmaster or give them a detention."),
        ("If they don’t accept me on the course, …", "I’ll either re-take the test or I might look for another Master’s.|"
         "I’ll either re-take the test or I might look for another Masters.|I’ll either re-take the test or might look for "
         "another Master’s."),
        ("If you miss a deadline that your tutor has set, …", "you will be given a zero."),
        ("If you have any problems which are affecting your coursework, …",
         "you should contact the school counseling service.|you should contact the school counselling service.|"
         "you should contact the student counselling service.|you should contact the counselling service.")]


def cond73(id, letter="B", instr='<span class="audio-ic">♪</span> 7.3 Write down the second half of each sentence.'):
    """p. 53, Grammar A/B. Ответы — ключ и аудиоскрипт 7.3."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in COND]))


def first_cond(id, letter="C", instr="Complete the first conditional sentences with the verbs in the correct form."):
    """p. 53, Grammar C. Ключ: get / I’ll probably do; have / I’ll go; I’ll have to."""
    d = DLG(("A", "What are you going to do when you graduate?"),
            ("B", f"It depends on my grades. If I {G('get')} good grades, I{G('’ll probably do|will probably do')} a master’s in "
                  "Business Administration. (get / probably do)"),
            ("A", "And what if you don’t?"),
            ("B", f"Well it depends on how much I’m in debt. If I {G('have')} enough money, I{G('’ll go|will go')} travelling "
                  "for a while and maybe get a job abroad. (have / go)"),
            ("A", "And what if you haven’t got enough money?"),
            ("B", f"I suppose I{G('’ll have to|will have to')} get a job – and quickly! (have to)"))
    return EX(id, letter, instr, d)


# ---- Writing 07 (pp. 132–133) ----
LINKERS = ["obviously", "However", "Otherwise", "Secondly", "Firstly", "thirdly", "In conclusion", "Personally"]
TRENDS = [("Public transport {} (improve) dramatically over the last few years. Despite this, more and more people {} (drive) "
           "into the city centre to work every day.", ["has improved", "are driving"]),
          ("Crime {} (get) worse and worse at the moment. The government {} (recently / increase) the amount of money available "
           "to the police, but this has not made much difference.", ["is getting", "has recently increased"]),
          ("It is said that children’s behaviour these days {} (get) worse and worse. Many parents today seem unconcerned about "
           "these problems, whilst society as a whole {} (stop) caring about the young.", ["is getting", "has stopped"]),
          ("The number of women working {} (increase) a lot in recent years and more and more women {} (now / become) bosses.",
           ["has increased", "are now becoming"]),
          ("Over the last few years, there {} (be) several stories about people helping loved ones to die and euthanasia {} "
           "(become) a major issue. As such, several pressure groups {} (now / call) for a change in the law.",
           ["have been", "has become", "are now calling"])]


def trends(id, letter="A", instr="Complete these sentences by putting the verbs in brackets into the correct form."):
    """p. 133, Grammar A. Ключ: Writing 07 Grammar A."""
    return EX(id, letter, instr, OL([t.format(*[G(a) for a in ans]) for t, ans in TRENDS]))


SUCH = ["Many people nowadays are too busy to meet potential partners in the traditional way.",
        "The war had become one disaster after another.",
        "Over the last few years, the company has decided to do a lot more e-marketing.",
        "More and more people are suffering from depression.", "The school had the best results in the country last year."]
SUCH_END = ["As such, sales have grown dramatically.", "As such, it is important to learn from its success.",
            "As such, Internet dating is growing in popularity.", "As such, the decision was made to bring the army home.",
            "As such, research into the factors affecting happiness has become more and more important."]


def as_such(id, letter="A", instr="Match sentences 1–5 with the results / conclusions."):
    """p. 133, Keywords A. Ключ: 1 c 2 d 3 a 4 e 5 b."""
    return EX(id, letter, instr, OL([f"{q} → {S(k, AH[:5])}" for q, k in zip(SUCH, "cdaeb")]) + OL(SUCH_END, "items alpha"))
