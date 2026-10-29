"""Упражнения модуля 11, которые выводятся и в «Учебнике», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, EX, OL, ORDER, TF, DLG

AH = list("abcdefghi")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


WHO = [("nearly killed one of the animals.", "2"), ("saved an animal’s life.", "1"),
       ("was too frightened to shout for help at one point.", "3"), ("sounded quite adventurous.", "3"),
       ("confused one of the animals for something else.", "2"), ("was distracted from some work.", "1"),
       ("had a lucky escape.", "3"), ("kept the animal and looked after it.", "1"), ("saw an animal eating.", "2")]


def which_conv(id, letter="B", instr="Listen again and decide in which conversation someone:"):
    """p. 76, Listening B. Ключ: a 2 b 1 c 3 d 3 e 2 f 1 g 3 h 1 i 2."""
    return EX(id, letter, instr, OL([f"{t} → {S(k, ['1', '2', '3'])}" for t, k in WHO], "items alpha"))


QBOX = ["What was that doing there?", "Seriously?", "What was that?", "What?", "So what happened in the end?"]


def story_qs(id, letter="A", instr="Complete the conversations below by adding the questions in the box."):
    """p. 77, Developing conversations A. Ключ: 1 What? 2 What was that?; Seriously? 3 What was that doing there?
    4 So what happened in the end?"""
    opts = sorted(QBOX)
    s = lambda k: S(k, opts)
    rows = [DLG(("A", "You’ll never guess what happened last night."), ("B", f"Go on. {s('What?')}"),
                ("A", "Well, I was walking home from the bus stop when I suddenly saw a horse standing there in the street.")),
            DLG(("C", "I saw something really strange while we were away."), ("D", f"Oh yeah? {s('What was that?')}"),
                ("C", "We saw this whale stuck on the beach."), ("D", f"{s('Seriously?')} Still alive?"),
                ("C", "Yeah! It was actually quite upsetting! We phoned the police to see if they could organise help.")),
            DLG(("E", "I was just about to put my shoes on when I found a scorpion hiding in one of the shoes!"),
                ("F", f"Really? God! {s('What was that doing there?')}"),
                ("E", "I don’t know. I guess it was just looking for somewhere to sleep.")),
            DLG(("G", "We spent hours trying to persuade the cat to come down from the tree, but it refused to come."),
                ("H", f"Oh no. That’s awful! {s('So what happened in the end?')}"),
                ("G", "Well, eventually, we gave up, but an hour later it walked into the kitchen, looking for its dinner!"))]
    return EX(id, letter, instr, wordbox(QBOX) + OL(rows))


ING = [("I saw a fox in the street. It was eating an old kebab.", "I saw a fox in the street eating an old kebab."),
       ("I could hear a large animal of some kind. It was moving around in the bushes.",
        "I could hear a large animal of some kind moving around in the bushes."),
       ("As we were walking along, I saw an eagle. It was circling right above us.",
        "As we were walking along I saw an eagle circling right above us."),
       ("I couldn’t sleep because of my grandmother’s parrot. It was making a dreadful noise all night.",
        "I couldn’t sleep because my grandmother’s parrot was making a dreadful noise all night.|"
        "I couldn’t sleep because of my grandmother’s parrot making a dreadful noise all night."),
       ("When we were camping, I saw a huge lizard. It was lying on a rock in the sun.",
        "When we were camping I saw a huge lizard lying on a rock in the sun."),
       ("The bear was lying beneath a tree. It was sleeping.", "The bear was lying beneath a tree sleeping."),
       ("I once saw a wolf. It was disappearing into a forest.", "I once saw a wolf disappearing into a forest."),
       ("I went into the bathroom and there was a snake in the corner. It was hissing at me.",
        "I went into the bathroom and there was a snake in the corner hissing at me.")]


def ing_clauses(id, letter="A", instr="Turn the pairs of sentences into single sentences by crossing out the words that are not needed."):
    """p. 77, Grammar A. Ответы — ключ."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in ING]))


HEADLINES = ["Mass extinctions predicted", "Illegal animal trade moves into cyberspace", "Man arrested for smuggling animal skulls",
             "Back from the point of extinction"]
WORDS = ["bred", "skeleton", "tiger skins", "reintroduced", "destroyed by global warming", "endangered species",
         "hunting and trading", "organised criminal gangs"]


# статьи pp. 78–79 из OCR: (буква, [(стр, область колонки)], [(фрагмент OCR, замена с {} для пропуска, ответ)])
ARTICLES = [
    ("A", [(78, (425, 135, 598, 350)), (78, (598, 135, 778, 350))],
     [("could be ........ if 2 action", "could be <sup>1</sup>{} if action", "destroyed by global warming"),
      ("because the 2 ....... of rare", "because the <sup>2</sup>{} of rare", "hunting and trading")], HEADLINES[0]),
    ("B", [(78, (425, 825, 598, 1050)), (78, (598, 825, 778, 1050))],
     [("world’s most are being", "world’s most <sup>3</sup>{} are being", "endangered species"),
      ("worried that – are using", "worried that <sup>4</sup>{} are using", "organised criminal gangs")], HEADLINES[1]),
    ("C", [(79, (28, 100, 370, 230))],
     [("included the of a dolphin", "included the <sup>5</sup>{} of a dolphin", "skeleton"),
      ("skull of an ape, and", "skull of an ape, <sup>6</sup>{}, and", "tiger skins")], HEADLINES[2]),
    ("D", [(79, (28, 470, 370, 670))],
     [("has been into the country", "has been <sup>7</sup>{} into the country", "reintroduced"),
      ("have been ?. and their", "have been <sup>8</sup>{} and their", "bred")], HEADLINES[3])]
ART_FIX = [("weck", "week"), ("IFA W- the International Fund for Animal Welfare -", "IFAW – the International Fund for Animal "
           "Welfare –"), ("relativcly", "relatively"), ("chimnanzees on US welriter.", "chimpanzees on US websites."),
           ("trade in live animale", "trade in live animals."), (" - ", " – ")]


def articles(id, letter="C", instr="Read the four articles quickly and match them with the correct headline from exercise A. "
             "Then complete the gaps with the words from exercise B.", img=""):
    """pp. 78–79, Reading C. Ключ: A Mass extinctions predicted, B Illegal animal trade moves into cyberspace,
    C Man arrested for smuggling animal skulls, D Back from the point of extinction; 1 destroyed by global warming
    2 hunting and trading 3 endangered species 4 organised criminal gangs 5 skeleton 6 tiger skins 7 reintroduced 8 bred."""
    from ocrtext import text
    out = []
    for let, cols, gaps, head in ARTICLES:
        t = " ".join(text(p, b) for p, b in cols)
        for a, b in ART_FIX:
            t = t.replace(a, b)
        for frag, rep, ans in gaps:
            assert frag in t, frag
            t = t.replace(frag, rep.format(S(ans, sorted(WORDS))))
        out.append(f'<div class="story"><h4>{let} {S(head, sorted(HEADLINES))}</h4><p>{t}</p></div>')
    return EX(id, letter, instr, wordbox(WORDS) + "".join(out) + img)


def passive_gaps(id, letter="A", instr="Complete these sentences from the articles in <i>Reading</i> by putting the verbs into a passive form."):
    """p. 79, Grammar A. Ключ: 1 are currently threatened 2 were being offered 3 has been arrested
    4 was searched / were found 5 is shown."""
    W = lambda a: G(a, "wide")
    rows = [f"More than 16,000 plant and animal species {W('are currently threatened')} (currently threaten) with extinction.",
            f"All of the items {W('were being offered')} for sale illegally. (offer)",
            f"A man from the west of England {W('has been arrested')} at Gatwick Airport. (arrest)",
            f"The man’s shop {G('was')} then {G('searched')} and various other illegal items {W('were found')}. (search, find)",
            f"The annual race for young riders {W('is shown')} on national TV. (show)"]
    return EX(id, letter, instr, OL(rows))


PART = ["arrested", "searched", "smuggled", "kept", "released", "taken"]
PART_ROWS = [("I was … at the airport / His house was … after the arrest / I was stopped and … on my way to work", "searched"),
             ("He was … out of the country / The guns were … across the border / Drugs are being … into prisons", "smuggled"),
             ("These photos were … in Spain / Action really must be … soon / He was … to hospital late last night", "taken"),
             ("The lions have been … back into the wild / He is due to be … from prison / The report was … last week", "released"),
             ("She was … for speeding / He has been … for murder / No one has been … yet", "arrested"),
             ("The dog’s … outside / The animals were being … in awful conditions / The boss makes sure we’re … busy", "kept")]


def participles(id, letter="B", instr="Which past participle in the box goes with each of the groups of words (1–6)?"):
    """p. 79, Grammar B. Ключ: 1 searched 2 smuggled 3 taken 4 released 5 arrested 6 kept."""
    return EX(id, letter, instr, wordbox(PART) + OL([f"{t} → {S(k, sorted(PART))}" for t, k in PART_ROWS]))


PETS_BOX = ["lick", "stroke", "mess", "the litter tray", "aggressive", "tank", "kittens", "size", "dry food", "looking after"]


def pets(id, letter="A", instr="Complete 1–10 with the words in the box."):
    """p. 80, Vocabulary A. Ключ: 1 tank 2 aggressive 3 kittens 4 stroke 5 looking after 6 dry food 7 the litter tray
    8 size 9 lick 10 mess."""
    rows = [f"I keep it <i>outside / in a cage / in a</i> {G('tank')}.",
            f"They’re quite <i>demanding / poisonous /</i> {G('aggressive')} <i>/ playful / smelly</i>.",
            f"She had six <i>babies /</i> {G('kittens')} <i>/ puppies / eggs</i>.",
            f"You can’t <i>hold /</i> {G('stroke')} <i>/ play with</i> them.",
            f"They need <i>a lot of</i> {G('looking after')} <i>/ exercise / food / attention</i>.",
            f"You can feed them <i>tinned food / leftovers /</i> {G('dry food')} <i>/ mice</i>.",
            f"You have to clean <i>them /</i> {G('the litter tray')} <i>/ the cage</i> regularly.",
            f"They grow <i>big / to about a metre / to an enormous</i> {G('size')}.",
            f"They often <i>scratch / jump on /</i> {G('lick')} you.",
            f"They can make an awful <i>noise /</i> {G('mess')}."]
    return EX(id, letter, instr, wordbox(PETS_BOX) + OL(rows))


PETS_TF = [("Al is going to keep the puppies.", "F"), ("Suzie prefers cats to dogs.", "T"), ("Suzie’s previous pet died.", "F"),
           ("The snake is not dangerous.", "T"), ("The snake eats tinned food.", "F"),
           ("Al wants to have his picture taken with the snake.", "F"), ("The snake once escaped into the kitchen.", "T")]


def pets_tf(id, letter="A", instr="<span class=\"audio-ic\">♪</span> 11.3 Listen. Decide if these sentences about the conversation are true or false."):
    """p. 80, Listening A. Ключ: 1 F 2 T 3 F 4 T 5 F 6 F 7 T."""
    return EX(id, letter, instr, OL([f"{t} {TF(k)}" for t, k in PETS_TF]))


NOUNS = [("The animals were set <u>free</u> after being bred in the zoo.", "Kids don’t have as much {} as they had in the past.", "freedom"),
         ("Thousand of hectares of forest are <u>destroyed</u> every hour.", "The bears are struggling to survive because of the {} of their habitats.", "destruction"),
         ("Mount Elgon, like Kilimanjaro, is an <u>extinct</u> volcano.", "Many of the animal species in this country are in danger of {}.", "extinction"),
         ("I <u>warned</u> them not to touch the plants, but they still did.", "Farmers ignored repeated {} that they were damaging the environment.", "warnings"),
         ("The gang <u>threatened</u> to kill anyone who got in their way.", "The construction of the road is a serious {} to wildlife.", "threat"),
         ("Scientists are <u>investigating</u> the cause of the disease which is killing the trees.", "The crime is currently under {}.", "investigation")]


def nouns(id, letter="A", instr="Complete 1–6 with noun forms of the underlined words."):
    """p. 81, Vocabulary A. Ключ: 1 freedom 2 destruction 3 extinction 4 warnings 5 threat 6 investigation."""
    return EX(id, letter, instr, OL([f"{a}<br>{b.format(G(k))}" for a, b, k in NOUNS]))


PET_QS = [("poisonous is it", "Is it poisonous?"), ("it breed what is", "What breed is it?"), ("it do where keep you", "Where do you keep it?"),
          ("I him stroke can", "Can I stroke him?"), ("it if is pick I up him OK", "Is it OK if I pick him up?"),
          ("it long you have had how", "How long have you had it?"), ("you do it what feed", "What do you feed it?"),
          ("long how for they do live", "How long do they live for?")]


def pet_questions(id, letter="A", instr="Put the words in the correct order to make questions about pets."):
    """p. 81, Speaking A. Ответы — ключ."""
    return EX(id, letter, instr, OL([ORDER(s, a) for s, a in PET_QS]))
