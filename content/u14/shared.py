"""Упражнения модуля 14, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, TF, EX, OL, REVEAL

AH = list("abcdefghijkl")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


PC = ["cable", "hard drive", "mouse", "scanner", "cursor", "keyboard", "plug", "screen", "file", "menu", "printer", "socket"]


def pc_nouns(id, letter="B", instr="Complete the sentences with the nouns from exercise A."):
    """p. 98, Vocabulary B. Ключ: 1 scanner 2 socket 3 menu 4 cursor 5 plug 6 hard drive 7 file 8 screen 9 cable
    10 printer 11 keyboard 12 mouse."""
    rows = [f"Have you got a {G('scanner')}? OK. Good. Then just scan the images in, save them as JPEGs, and email them to me.",
            f"Can you just make sure you’ve plugged the microphone into the right {G('socket')}?",
            f"If you click on the icon at the top left-hand side, that should display the drop-down {G('menu')}.",
            f"Move the {G('cursor')} over the image and wait for the instructions to come up.",
            f"You won’t be able to use that laptop in Spain. It’s got a three-pin {G('plug')} on it and they don’t work over "
            "there.",
            f"In future, you really should make back-up copies of all your work on the external {G('hard drive')} – just to "
            "be safe.",
            f"I deleted a really important {G('file')} by accident.",
            f"Every time I tried to play a DVD, the {G('screen')} kept freezing and I kept having to restart the computer.",
            f"I tripped over a {G('cable')} on the floor and knocked the whole computer over.",
            f"I had to hand in an important essay at university ASAP, but the {G('printer')} ran out of ink after the first "
            "three pages!",
            f"I spilled coffee all over the {G('keyboard')}. Half the keys stopped working after that.",
            f"Right-click on the {G('mouse')} and select ‘hyperlink’."]
    return EX(id, letter, instr, wordbox(PC) + OL(rows))


ARTICLE_TF = [("The floppy discs the writer found were extremely old.", "F"),
              ("Canals played an important role in the development of some countries.", "T"),
              ("Canals have started becoming more popular again.", "T"),
              ("VHS videotapes became more popular than Betamax videos because they were better quality.", "F"),
              ("VHS videotapes dominated the market for a long time.", "F"),
              ("The Sinclair C5 was designed to be environmentally friendly.", "T"),
              ("You needed a driving licence to drive the C5.", "F"),
              ("The writer mentions the C5 in order to suggest that it is not worth buying the latest gadgets and inventions.",
               "T")]


def article_tf(id, letter="C", instr="Decide if these sentences about the article are true or false, according to the author."):
    """p. 100, Reading C. Ключ: 1 F 2 T 3 T 4 F 5 F 6 T 7 F 8 T."""
    return EX(id, letter, instr, OL([f"{s} {TF(k)}" for s, k in ARTICLE_TF]))


GADGETS = [("I wanted to {} to something which was more {}.", ["upgrade", "powerful"]),
           ("It’s {} so I can {} a lot of games and videos on it.", ["100GB|100 GB", "store"]),
           ("It has a bigger {} and so the {} is a lot clearer.", ["screen", "picture"]),
           ("They {} on electricity bills because they’re more energy-{}.", ["save", "efficient"]),
           ("It {} a lot of time because it does it all {}.", ["saves", "automatically"]),
           ("It’s just a very nice {}. It looks really {}.", ["design", "cool"]),
           ("You can just {} the timer and it {} itself on.", ["set", "switches"]),
           ("It {} you when you’re about to visit a {} website.", ["warns", "dangerous"]),
           ("It {} you to change videos into different {}.", ["allows", "formats"]),
           ("It’s {} and easier to {} around.", ["lighter", "carry"]),
           ("Even my mum finds it easy to {}. It’s so {}.", ["use", "straightforward"]),
           ("It {} off solar power, so it’s a lot {}.", ["runs", "greener"])]
GADGET_BOX = ["design + cool", "saves + automatically", "runs + greener", "warns + dangerous", "set + switches",
              "save + efficient", "100GB + store", "allows + formats", "lighter + carry", "upgrade + powerful",
              "screen + picture", "use + straightforward"]


def gadgets(id, letter="A", instr="Complete the sentences with the pairs of words."):
    """p. 102, Vocabulary A. Ключ: 1 upgrade + powerful 2 100 GB + store 3 screen + picture 4 save + efficient
    5 saves + automatically 6 design + cool 7 set + switches 8 warns + dangerous 9 allows + formats 10 lighter + carry
    11 use + straightforward 12 runs + greener."""
    return EX(id, letter, instr, wordbox(GADGET_BOX) + OL([t.format(*[G(a) for a in ans]) for t, ans in GADGETS]))


RULES = ["<i>-ing</i> forms are often used after a preposition such as <i>in, on</i> and <i>from</i>",
         "<i>-ing</i> forms follow certain verbs such as <i>avoid, miss,</i> and <i>mind</i>",
         "<i>-ing</i> forms are used when they’re the subject of a clause",
         "<i>to</i>-infinitives are used to explain the reason or purpose for something",
         "<i>to</i>-infinitives are used after certain verbs such as <i>learn, ask</i> and <i>plan</i>"]
RULE_EX = ["What’s wrong with just putting them in some water?", "You still need the cash to install the panels.",
           "I did consider getting one.", "If you want to have the perfect boiled egg, …",
           "Using this is more energy-efficient than boiling eggs."]


def ing_rules(id, letter="A", instr="Match the examples 1–5 from <i>Listening</i> to the rules a–e."):
    """p. 103, Grammar A. Ключ: 1 a 2 d 3 b 4 e 5 c."""
    key = "a d b e c".split()
    return EX(id, letter, instr, OL([f"{q} … {S(k, AH[:5])}" for q, k in zip(RULE_EX, key)]) + OL(RULES, "items alpha"))


ING_C = [("My computer keeps to crash.", "keeps crashing"), ("You should take it somewhere to get it looked at.", ""),
         ("To make your own films is much easier with MDirector.", "Making your own films …"),
         ("I became much greener after to see <i>An Inconvenient Truth</i>.", "after seeing"),
         ("I use them for saving energy.", ""), ("We’re all guilty of to damage the planet in some way.", "guilty of damaging"),
         ("People need to get used to not drive everywhere. They should walk more.", "get used to not driving"),
         ("I took the laptop back to the shop and luckily they agreed to exchange it.", "")]


def ing_correct(id, letter="C", instr="Decide if the following sentences are correct or incorrect."):
    """p. 103, Grammar C. Ключ: 1 keeps crashing 2 OK 3 Making 4 seeing 5 OK 6 damaging 7 not driving 8 OK."""
    return EX(id, letter, instr, OL([f"{s}<br>{C('Incorrect' if k else 'Correct', 'Correct', 'Incorrect')}" +
                                     (REVEAL(k, "Исправление (ключ)") if k else "") for s, k in ING_C]))


# ---- Writing 08 (pp. 134–135) ----
FILM_ADJ = ["moving", "gripping", "entertaining", "uplifting", "funny", "scary"]


def film_adj(id, letter="A", instr="Match the words in the box to the descriptions 1–6."):
    """p. 134, Vocabulary A. Ключ: 1 funny 2 moving 3 scary 4 entertaining 5 uplifting 6 gripping."""
    rows = [("I couldn’t stop laughing. It’s great.", "funny"), ("It’s so sad! I was in tears at the end of the film.", "moving"),
            ("Some scenes make you jump out of your seat and it could give you nightmares!", "scary"),
            ("It has lots of action and a great soundtrack.", "entertaining"),
            ("Although she has a difficult life, the film leaves you feeling really happy and positive. It’s an inspiring "
             "story.", "uplifting"),
            ("It’s really exciting – you just don’t know what’s going to happen next.", "gripping")]
    return EX(id, letter, instr, wordbox(FILM_ADJ) + OL([f"{t} → {S(k, sorted(FILM_ADJ))}" for t, k in rows]))


def film_part(id, letter="B", instr="Complete the sentences with the adjectives in the box."):
    """p. 134, Vocabulary B. Ключ: 1 chosen 2 acted 3 written 4 filmed 5 directed."""
    rows = [f"The soundtrack contains several well-{G('chosen')} songs, which really remind you of the time the film is set in.",
            f"The main character is superbly {G('acted')} by Daniel Day-Lewis.",
            f"It has a very well-{G('written')} script, full of jokes.",
            f"The mountains and countryside are beautifully {G('filmed')}.",
            f"The film is brilliantly {G('directed')} by Steven Spielberg."]
    return EX(id, letter, instr, wordbox(["acted", "chosen", "directed", "filmed", "written"]) + OL(rows))


def while_during(id, letter="", instr="Complete the sentences using <i>while</i> or <i>during</i>."):
    """p. 134, Key words for writing. Ключ: 1 during 2 while 3 While 4 During 5 during 6 While."""
    wd = lambda k: S(k, ["while", "during"]) if k.islower() else S(k, ["While", "During"])
    rows = [f"The film takes place {wd('during')} the Gulf War in 1990.",
            f"They fall in love {wd('while')} she is planning his wedding!",
            f"{wd('While')} he’s not looking, he puts a drug in her drink.", f"{wd('During')} the night, the toys come alive.",
            f"Lots of things happen {wd('during')} the journey that bring the family closer together.",
            f"{wd('While')} the parents are away, he has to defend the house against robbers."]
    return EX(id, letter, instr, OL(rows))
