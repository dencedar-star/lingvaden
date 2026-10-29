"""Упражнения модуля 16, которые выводятся и в «Учебнике», и в «Тестах» (с разными id). Ответы — ключи."""
from itertools import combinations
from lib import G, S, EX, OL

AH = list("abcdef")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


PAIRS = [("close down", "made redundant"), ("get divorced", "have an affair"), ("stab", "victim"), ("pass away", "funeral"),
         ("sign", "midfielder")]


def news_pairs(id, letter="A", instr="The words below come from the conversations: two from each. Which pairs of words go "
               "together?"):
    """p. 110, Listening A. Ключ (16.1): get divorced – have an affair; close down – made redundant; stab – victim;
    pass away – funeral; sign – midfielder."""
    opts = sorted(b for _, b in PAIRS)
    return EX(id, letter, instr, OL([f"<b>{a}</b> → {S(b, opts)}" for a, b in PAIRS]))


PEOPLE = [("Marie Curie was a Polish {} who <i>studied radiation</i> and <i>discovered</i> the radioactive substance polonium.",
           "scientist"),
          ("Martin Luther King was a human rights {} who <i>campaigned for the rights of</i> black people in the United States.",
           "activist"),
          ("Pol Pot was a {} in Cambodia who <i>was responsible for the deaths of</i> over a million people.", "dictator"),
          ("Kemal Atatürk <i>led the liberation struggle</i> in Turkey and was the {} of the republic.", "founder"),
          ("Sergey Bubka is a Ukrainian pole-vaulter. He’s perhaps the greatest {} of all time. He <i>set the world record</i> "
           "in 1994 and he still holds it. No one’s come close to beating it.", "athlete"),
          ("Euclid was a Greek {} who <i>is considered the father of</i> geometry.", "mathematician"),
          ("Pedro Alonso is a Spanish {}. He led a team which has <i>developed a vaccine against</i> malaria.", "doctor"),
          ("Gustav Klimt is an Austrian {} whose <i>most famous work is</i> probably ‘The Kiss’.", "artist")]
WHO = ["artist", "activist", "scientist", "athlete", "dictator", "founder", "doctor", "mathematician"]


def who_people(id, letter="A", instr="The descriptions 1–8 describe some of the people in the pictures. Complete the sentences "
               "with the words in the box."):
    """p. 112, Vocabulary A. Ключ: 1 scientist 2 activist 3 dictator 4 founder 5 athlete 6 mathematician 7 doctor 8 artist."""
    return EX(id, letter, instr, wordbox(WHO) + OL([t.format(G(a)) for t, a in PEOPLE]))


REL = [("He was a military leader in the nineteenth century {} helped unify Italy.", ["who", "that", "which"], "which"),
       ("It’s a European Union scheme {} provides grants to teachers.", ["that", "who", "which"], "who"),
       ("It’s {} they have Rembrandt’s most famous paintings.", ["who", "when", "where"], "who, when"),
       ("He set up a charity {} has helped thousands of poor children.", ["that", "which", "where"], "where"),
       ("He’s a composer {} most famous work is probably the Rites of Spring.", ["who", "that", "whose"], "who, that"),
       ("At the time {} he was writing, his ideas were very radical.", ["that", "who", "when"], "who"),
       ("It’s supposed to be the house {} Shakespeare was born.", ["when", "where", "that"], "when, that"),
       ("She was a writer {} ideas were very influential.", ["whose", "who", "which"], "who, which")]


def rel_cross(id, letter="A", instr="Cross out the word or words that are not correct in sentences 1–8. Choose what to cross "
              "out."):
    """p. 113, Grammar A. Ключ (что вычеркнуть): 1 which 2 who 3 who, when 4 where 5 who, that 6 who 7 when, that
    8 who, which."""
    out = []
    for t, ws, k in REL:
        opts = ws + [", ".join(c) for c in combinations(ws, 2)]
        out.append(t.format("<i>" + " / ".join(ws) + "</i>") + f"<br>✗ {S(k, opts)}")
    return EX(id, letter, instr, OL(out))


SECTIONS = [("a popular talent show", "2"), ("retired people", "6"), ("an act of great generosity", "3"),
            ("an act of great bravery", "5"), ("viral emails", "4"), ("physical attraction", "1")]


def sections(id, letter="B", instr="In which of the six sections of the article were the following mentioned?"):
    """p. 114, Reading B. Ключ: a 2 b 6 c 3 d 5 e 4 f 1."""
    return EX(id, letter, instr, OL([f"{t} → {S(k, list('123456'))}" for t, k in SECTIONS], "items alpha"))


def fame_words(id, letter="D", instr="Complete the sentences with the correct form of the words from the article."):
    """p. 114, Reading D. Ключ: 1 option 2 footsteps 3 barrier 4 control 5 will 6 saved 7 forward 8 caught 9 repay
    10 came into."""
    rows = [f"We would love to buy a house and move in together, but on our wages that {G('option')} isn’t available to us.",
            f"My dad wants me to follow in his {G('footsteps')} and join the army, but it’s just not what I want to do with "
            "my life.", f"Physical disability is no {G('barrier')} to a successful career.",
            f"My spending just got out of {G('control')}. If you ask me, it’s the bank’s fault for lending me so much money.",
            f"My aunt left me a house in her {G('will')}.",
            f"You {G('saved')} my life! How can I ever thank you enough? I would’ve died if you hadn’t rescued me.",
            f"Could you {G('forward')} the email from Head Office to me?",
            f"There were some really good-looking guys at the party, but one in particular {G('caught')} my eye.",
            f"Thanks again for everything you did for us. I hope that one day we can {G('repay')} your kindness. All the best, "
            "Omar.", f"She {G('came into')} a lot of money when her father died."]
    return EX(id, letter, instr, wordbox(["barrier", "control", "footsteps", "option", "will"]) + OL(rows[:5]) +
              wordbox(["catch", "come into", "forward", "repay", "save"]) + OL(rows[5:], start=6))
