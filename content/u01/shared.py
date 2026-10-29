"""Упражнения модуля 1, которые выводятся и в «Учебнике», и в «Тестах» (с разными id)."""
from lib import G, S, C, TF, EX, OL, DLG, ORDER


def qform(id, letter="A", instr="Complete the questions with the correct words."):
    """p. 8, Grammar A. Ответы — ключи pp. 8–9."""
    rows = [
        (("A", "Where " + G("are you|do you come") + " from?"), ("B", "Poland.")),
        (("A", "What " + G("do you") + " do?"), ("B", "I work in an office.")),
        (("A", "What " + G("are you") + " studying?"), ("B", "Law.")),
        (("A", G("Are you") + " married?"), ("B", "Not exactly. I live with my partner, but we’re not married.")),
        (("A", G("Have you") + " studied here before?"), ("B", "Yeah, I was here last term, actually.")),
        (("A", "How long " + G("have you been") + " studying English?"), ("B", "Ages. Probably ten years on and off.")),
        (("A", "What " + G("do you") + " do when you’re not working / studying?"),
         ("B", "Oh, I’m really into surfing so I do that whenever I can. Apart from that, I like listening to music, shopping – that kind of thing.")),
        (("A", G("Have you got") + " any brothers or sisters?"), ("B", "Yeah, I’ve got one sister.")),
        (("A", "How long " + G("are you going to|are you planning to") + " study here?"), ("B", "Probably till next June.")),
        (("A", "What " + G("did you") + " do last weekend?"), ("B", "Nothing special. I went out shopping on Saturday, but that’s all really.")),
    ]
    return EX(id, letter, instr, OL([DLG(*r) for r in rows]))


def listen_choice(id, letter="B", instr="Choose the words that you heard. Then listen again to check your answers."):
    """p. 9, Listening B. Ключ: 1 Come in 2 kilometres 3 strong 4 stay 5 mind 6 top."""
    items = [
        "Hi. " + C("Come in", "Coming", "Come in") + ". Sit down. Take a seat.",
        "It’s maybe 500 " + C("kilometres", "kilometres", "miles") + " from Moscow.",
        "You haven’t got a very " + C("strong", "strange", "strong") + " accent.",
        "How long are you going to " + C("stay", "study", "stay") + " here?",
        "How old are you, if you don’t " + C("mind", "mine", "mind") + " me asking?",
        "I’m going to put you in the " + C("top", "top", "high") + " class.",
    ]
    return EX(id, letter, instr, OL(items))


DC_Q = ["What are you studying?", "Have you studied here before?", "What do you do when you’re not studying?",
        "Have you got any brothers or sisters?", "What did you do at the weekend?", "What do you do?"]
DC_F = ["Whose class were you in? / Where did you learn your English?",
        "What year are you in? / What does that involve?",
        "Older or younger? / What do they do?",
        "Where do you work? / Do you enjoy it?",
        "Did you get anything nice? / Do you do that often?",
        "How long have you been doing that? / What kind of music are you into?"]
DC_KEY = "b a f c e d".split()  # 1 b 2 a 3 f 4 c 5 e 6 d


def dc_match(id, letter="B", instr="Match the questions 1–6 with the two possible follow-up questions a–f."):
    L = list("abcdef")
    q = OL([f"{t} &nbsp;→ {S(k, L)}" for t, k in zip(DC_Q, DC_KEY)])
    f = OL(DC_F, "items alpha")
    return EX(id, letter, instr, q + f)


READ_TF = [
    ("UK students never have to study a foreign language.", "F"),
    ("Most British people only speak English.", "T"),
    ("Edward Jones’ students never try to speak a foreign language.", "F"),
    ("Britain could do more business abroad.", "T"),
    ("The Government accepted there was a problem with their policy.", "F"),
    ("Learning languages earlier is definitely more effective.", "F"),
    ("The European Commission supports early teaching.", "F"),
    ("There aren’t many opportunities for older people to learn.", "T"),
]


def reading_tf(id, letter="C", instr="Decide if these sentences about the article are true or false."):
    return EX(id, letter, instr, OL([f"{t} {TF(k)}" for t, k in READ_TF]))


# p. 10–11, Reading E: слова, выделенные в статье, и толкования из ключа
READ_WORDS = [
    ("top head teacher", "well-respected director of a school"),
    ("motivation", "desire to do something"),
    ("the point", "the purpose or reason for doing something"),
    ("Relying on", "Depending on"),
    ("evidence", "proof"),
    ("environment", "context, situation"),
    ("continuity", "linked progression"),
    ("progress at different speeds", "learn faster or more slowly"),
    ("deal with", "manage"),
    ("more available", "easier to do, offered more widely"),
]


def reading_words(id, letter="E", instr="Work in pairs. Discuss what you think the words in <b>bold</b> in the text mean."):
    opts = sorted(d for _, d in READ_WORDS)
    rows = [f"<b>{w}</b> — {S(d, opts)}" for w, d in READ_WORDS]
    return EX(id, letter, instr + ' <span style="font-weight:400">Выберите значение для каждого слова.</span>', OL(rows))


def story_gaps(id, letter="A", instr="Without looking back at the article on p. 11, see if you can complete Brian Willis’ story by putting the verbs in the correct tense."):
    """p. 12, Grammar A. Ключ pp. 12–13."""
    t = ("I remember one mistake I made when I <sup>1</sup>" + G("was teaching") + " (teach) in Argentina. "
         "I <sup>2</sup>" + G("had done") + " (do) a bit of Spanish before, but not much. In my first class, "
         "I <sup>3</sup>" + G("was explaining") + " (explain) to the students that I was a language learner too, so I knew how they felt. "
         "I <sup>4</sup>" + G("told") + " (tell) them – in Spanish – “Don’t get embarrassed!” The students <sup>5</sup>"
         + G("looked") + " (look) surprised and <sup>6</sup>" + G("said") + " (say) “Embarazada?” “Yes,” I said, "
         "“because if you’re embarrassed, you can’t talk” and <sup>7</sup>" + G("acted") + " (act) being embarrassed. "
         "Several students laughed and we <sup>8</sup>" + G("continued") + " (continue) the class. I later found out "
         "I <sup>9</sup>" + G("had used") + " (use) the wrong word and I <sup>10</sup>" + G("had actually said") +
         " (actually say) “Don’t get pregnant!” I felt stupid, but it <sup>11</sup>" + G("didn’t stop|did not stop") +
         " (not stop) me talking and learning. I just never made the same mistake again!")
    return EX(id, letter, instr, f'<div class="story">{t}</div>')


def tense_usage(id, letter="C", instr="Match the tense 1–3 with the usage a–c."):
    opts = ["1 The past continuous", "2 The past perfect", "3 The past simple"]
    rows = [
        S(opts[1], opts) + " emphasises an action that happened before another past action, time or event",
        S(opts[0], opts) + " shows an action was unfinished when another past action happened.",
        S(opts[2], opts) + " shows completed actions that follow one after the other.",
    ]
    return EX(id, letter, instr, OL(["The past continuous", "The past perfect", "The past simple"]) +
              OL(rows, "items alpha"))


def past_cont(id, letter="A", instr="Complete the sentences with the past continuous form of the verbs in the box."):
    """p. 12, Other uses of the past continuous. Ключ: 1 was crying 2 was he doing; were building ..."""
    box ='<div class="wordbox"><span>build</span><span>chat</span><span>cry</span><span>look for</span>' \
          '<span>drive</span><span>do</span><span>have</span><span>sort out</span></div>'
    items = [
        "I didn’t sleep very well last night. The baby " + G("was crying") + " all night.",
        DLG(("A", "My brother lived in Copenhagen for four years."),
            ("B", "What " + G("was") + " he " + G("doing") + " there?"),
            ("A", "He’s a civil engineer and they " + G("were building") + " a metro line there.")),
        "Sorry, I’m late. I " + G("was chatting") + " to a friend and I forgot the time.",
        "Sorry. I " + G("was having") + " a coffee over the road.",
        "Sorry I’m late. I " + G("was sorting out") + " a problem at work.",
        "Sorry I’m late. I " + G("was looking for") + " a parking space. I " + G("was driving") +
        " round in circles for about half an hour.",
    ]
    return EX(id, letter, instr, box + OL(items))


WR_ORDER = [
    ("do time usually free you do what your in?", "What do you usually do in your free time?"),
    ("of what are into music you kind?", "What kind of music are you into?"),
    ("favourite is your band who?", "Who is your favourite band?"),
    ("saw was last what the you film?", "What was the last film you saw?"),
    ("a favourite you do have writer?", "Do you have a favourite writer?"),
    ("read was last what the you book?", "What was the last book you read?"),
    ("you do sport like?", "Do you like sport?"),
    ("you got favourite have a team?", "Have you got a favourite team?"),
]


def writing_order(id, letter="A", instr="Put the words in the correct order to form questions people might ask when writing to pen friends for the first time."):
    """p. 121, Grammar: Common questions. Нажимайте на слова по порядку."""
    rows = [f'<i>{s}</i>' + ORDER(s, a) for s, a in WR_ORDER]
    return EX(id, letter, instr + ' <span style="font-weight:400">Нажимайте на слова по порядку; повторное нажатие возвращает слово.</span>', OL(rows))
