"""Упражнения модуля 8, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, EX, OL, DLG

AH = list("abcdefgh")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


COOK = ["grill", "slice", "mash", "steam", "deep-fry", "roast", "boil", "grate", "stir-fry", "marinate"]
SEEN = {"slice", "mash", "steam", "deep-fry", "roast", "boil", "grate", "stir-fry", "marinate"}


def cooking(id, letter="A", instr="Which of the ways of cooking in the box can you see in the picture?"):
    """p. 54, Vocabulary A. Ключ: stir-frying, slicing, mashing, steaming, grating, roasting, deep-frying, boiling,
    marinating (grilling в ключе нет)."""
    return EX(id, letter, instr, OL([f"<b>{w}</b> {C('Yes' if w in SEEN else 'No', 'Yes', 'No')}" for w in COOK]))


DISHES = ["Papa Rellena", "Anticuchos", "Ceviche", "Sopa De Carne", "Tallarín Con Mariscos", "Bistec Apanado",
          "Arroz Con Mariscos", "Arroz Con Pato", "Lomo Saltado", "Seco De Cabrito"]


def orders(id, letter="B", instr='<span class="audio-ic">♪</span> 8.1 Listen to the conversation. Which dishes does Claes '
           "decide to order?"):
    """p. 55, Listening B. Ключ: He orders Ceviche and Seco De Cabrito."""
    return EX(id, letter, instr, OL([f"{d} {C('Orders' if d in ('Ceviche', 'Seco De Cabrito') else 'No', 'Orders', 'No')}"
                                     for d in DISHES]))


def listen81(id, letter="D", instr="Complete the sentences from the conversation."):
    """p. 55, Listening D. Ключ: 1 afraid 2 through 3 stuffed 4 tender; juicy 5 for 6 thinly; served 7 like; spicier 8 kind
    9 tasty."""
    rows = [f"They don’t have an English menu, I’m {G('afraid')}.", f"You’ll just have to talk me {G('through')} it.",
            f"That’s balls of mashed potato, {G('stuffed')} with beef, raisins and olives.",
            f"It’s sliced cow’s heart, very {G('tender')} and {G('juicy')}.", f"I’ll go {G('for')} that.",
            f"That’s steak, sliced very {G('thinly')} and then fried and {G('served')} with rice.",
            f"It’s a bit {G('like')} a Spanish paella, but {G('spicier')}.", f"It’s a {G('kind')} of stew with goat’s meat in.",
            f"That sounds very {G('tasty')}."]
    return EX(id, letter, instr, OL(rows))


def words_c(id, letter="C", instr="Complete the sentences with words from the texts. The definitions in brackets will help you."):
    """p. 56, Reading C. Ключ: 1 off-putting 2 split 3 starving 4 unadventurous 5 mouldy 6 turn out to be 7 spreading 8 ready."""
    rows = [f"Ian said ‘stinky tofu’ smells like sweaty socks and rotting fish and it’s really {G('off-putting')}. "
            "(<i>making you not want to eat it</i>)",
            f"Ian said Americans usually just {G('split')} the bill. (<i>divide equally</i>)",
            f"Isabella didn’t like having dinner at 6 in the evening. She was always {G('starving')} by bedtime. (<i>really hungry</i>)",
            f"She said she was {G('unadventurous')} about eating new food before going to Scotland. (<i>not brave</i>)",
            f"Ya-Wen described blue cheese as {G('mouldy')} cow fat. (<i>rotten</i>)",
            f"She said she sometimes ordered things that didn’t {G('turn out to be')} very nice. (<i>end up being</i>)",
            f"Alan is now happy either pouring olive oil or {G('spreading')} butter on his bread. (<i>putting</i>)",
            f"He says people in Britain eat a lot of {G('ready')} meals instead of cooking fresh food. (<i>pre-cooked</i>)"]
    return EX(id, letter, instr, OL(rows))


def _neg(s):
    """Варианты ответа: «tend(s) not to» = «don’t / doesn’t tend to»."""
    out = [s]
    if "tends not to" in s:
        out.append(s.replace("tends not to", "doesn’t tend to"))
    elif "tend not to" in s:
        out.append(s.replace("tend not to", "don’t tend to"))
    return "|".join(out)


TEND = [("My family generally eats a lot of ready meals, as both my parents work full-time.",
         "My family tends to eat a lot of ready meals, as both my parents work full-time.|"
         "My family tends to eat a lot of ready meals, as both my parents work full time.", ""),
        ("We don’t normally keep food which is left over after dinner.",
         _neg("We tend not to keep food which is left over after dinner."), ""),
        ("Generally speaking, people here eat food with their hands.", "People here tend to eat food with their hands.", ""),
        ("I usually skip breakfast during the week unless I have a late start at work.",
         "I tend to skip breakfast during the week unless I have a late start at work.", ""),
        ("Generally speaking, our family doesn’t eat out unless it’s a special occasion.",
         _neg("Our family tends not to eat out unless it’s a special occasion."), ""),
        ("People don’t usually leave tips here unless it was an exceptionally good meal.",
         _neg("People tend not to leave tips here unless it was an exceptionally good meal."), ""),
        ("I hardly ever have a dessert when I go out for dinner.", _neg("I tend not to have a dessert when I go out for dinner."), ""),
        ("Most of the time people here avoid making any noises while they’re eating.",
         "People here tend to avoid making any noises while they’re eating.", " It’s seen as bad manners."),
        ("I don’t usually have time to have a big lunch, so I normally just have a sandwich.",
         "I tend not to have time to have a big lunch so I tend to just have a sandwich.|"
         "I don’t tend to have time to have a big lunch so I tend to just have a sandwich.|"
         "I tend not to have time to have a big lunch so I just tend to have a sandwich.|"
         "I don’t tend to have time to have a big lunch so I just tend to have a sandwich.", "")]


def tend(id, letter="A", instr="Rewrite these sentences replacing the adverbs and adverbial phrases with <i>tend to / tend not to</i>."):
    """p. 57, Grammar A. Ответы — ключ (tend not to = don’t tend to)."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}{tail}" for q, a, tail in TEND]))


def restaurants(id, letter="B", instr="Choose the words that were used in each conversation."):
    """p. 58, Listening B. Ключ: 1a looks out over 1b do 1c an appetite 2a limited 2b inviting 3a overpowers 3b tender
    4a deserve 4b generous."""
    def c(k, a, b):
        return C(k, a, b)
    rows = [f"a The terrace {c('looks out over', 'gives onto', 'looks out over')} the river.<br>"
            f"b They {c('do', 'do', 'make')} some really nice snacks.<br>"
            f"c The walk will give you {c('an appetite', 'hunger', 'an appetite')}.",
            f"a The menu’s a bit {c('limited', 'limited', 'short')}.<br>"
            f"b The restaurant doesn’t look very {c('inviting', 'interesting', 'inviting')}.",
            f"a The sauce is quite spicy so it really {c('overpowers', 'overcooks', 'overpowers')} the taste of everything else.<br>"
            f"b That steak is so {c('tender', 'tender', 'tough')}!",
            f"a The restaurant doesn’t {c('deserve', 'deserve', 'merit')} the money.<br>"
            f"b The portions weren’t very {c('generous', 'great', 'generous')}."]
    return EX(id, letter, instr, OL(rows))


OVER = ["overcharged", "overdid", "overcooked", "overheated", "overestimated", "overate", "overreacted", "overslept"]


def over(id, letter="A", instr="Complete the sentences with the words in the box."):
    """p. 58, Vocabulary over- A. Ключ: 1 overate 2 overcharged 3 overdid 4 overheated 5 overestimated 6 overcooked
    7 overreacted 8 overslept."""
    rows = [f"It was a great meal. In fact, my only complaint would be that the food was so good that I completely {G('overate')}!",
            f"When I checked the bill, I realised we’d been {G('overcharged')}.",
            f"He {G('overdid')} it at the gym. He should be more careful.",
            f"It was so hot, the car {G('overheated')} on our way there.",
            f"It was a mistake. I {G('overestimated')} how much food we needed.",
            f"It was a bit of a disaster, because I {G('overcooked')} the pasta.",
            f"I know the waiter was a bit rude, but I still think you {G('overreacted')}.",
            f"No wonder he {G('overslept')} this morning! He didn’t get to bed till three last night."]
    return EX(id, letter, instr, wordbox(OVER) + OL(rows))


def second_rule(id, letter="A", instr="Look at these examples from the conversations in <i>Listening</i> and then complete the "
                "explanation."):
    """p. 59, Grammar A. Ключ: past, present, would, might."""
    return EX(id, letter, instr,
              '<p class="ex-line">They might attract a few more people if they redecorated.<br>It would be better if it didn’t have '
              'so much sauce on it!<br>What would happen if they called the police?</p>'
              f'<div class="box"><p>These sentences are all examples of the second conditional. The <i>if</i> part of the sentence '
              f'is in the {G("past")} simple (or continuous). This shows the speaker thinks a situation in the {G("present")} or in '
              f'the future is impossible to change or is not actually going to take place. The other part of the sentence uses '
              f'either {G("would")} + base form – to show a definite result or {G("might")} + base form – to show a possible '
              f'result.</p></div>')


def second_c(id, letter="C", instr="Complete these sentences by putting the verbs in the correct form to make second conditionals."):
    """p. 59, Grammar C. Ключ: 1 would taste, were (was) 2 would be, had 3 would explode, ate 4 would help, did 5 would be, told
    6 would look, painted, changed."""
    w = lambda v: G(f"would {v}|’d {v}")
    rows = [DLG(("A", "How’s your steak?"), ("B", f"It’s OK, but it {w('taste')} (taste) better if it {G('were|was')} (be) a bit "
                                                  "more rare.")),
            DLG(("A", "How’s the soup?"), ("B", f"It’s a bit bland. It {w('be')} (be) better if it {G('had')} (have) some spices "
                                                "in it.")),
            DLG(("A", "Would you like any more?"), ("B", f"No thanks. No. I {w('explode')} (explode) if I {G('ate')} (eat) any "
                                                         "more.")),
            DLG(("A", "I keep putting on weight."), ("B", f"No wonder! You’re stuck in front of that computer all day. It "
                                                          f"{w('help')} (help) if you {G('did')} (do) more exercise.")),
            DLG(("A", "They told us we’d have a table in five minutes, but we had to wait for an hour."),
                ("B", f"That’s awful! I hate it when that kind of thing happens. It {w('be')} (be) better if they just "
                      f"{G('told')} (tell) the truth at times like that.")),
            DLG(("A", "They should do something about the décor. It looks so cold and bare in there."),
                ("B", f"I know. It {w('look')} (look) a lot more inviting if they {G('painted')} (paint) it a warmer colour and "
                      f"{G('changed')} (change) the lighting."))]
    return EX(id, letter, instr, OL(rows))


# ---- Writing 08 (pp. 134–135) ----
ADJ = ["moving", "gripping", "entertaining", "uplifting", "funny", "scary"]
ADJ_Q = [("I couldn’t stop laughing. It’s great.", "funny"), ("It’s so sad! I was in tears at the end of the film.", "moving"),
         ("Some scenes make you jump out of your seat and it could give you nightmares!", "scary"),
         ("It has lots of action and a great soundtrack.", "entertaining"),
         ("Although she has a difficult life, the film leaves you feeling really happy and positive. It’s an inspiring story.",
          "uplifting"),
         ("It’s really exciting – you just don’t know what’s going to happen next.", "gripping")]


def films_a(id, letter="A", instr="Match the words in the box to the descriptions 1–6."):
    """p. 134, Vocabulary A. Ключ: 1 funny 2 moving 3 scary 4 entertaining 5 uplifting 6 gripping."""
    return EX(id, letter, instr, wordbox(ADJ) + OL([f"{q} → {S(k, sorted(ADJ))}" for q, k in ADJ_Q]))


def films_b(id, letter="B", instr="Complete the sentences with the adjectives in the box."):
    """p. 134, Vocabulary B. Ключ: 1 chosen 2 acted 3 written 4 filmed 5 directed."""
    rows = [f"The soundtrack contains several well-{G('chosen')} songs, which really remind you of the time the film is set in.",
            f"The main character is superbly {G('acted')} by Daniel Day-Lewis.",
            f"It has a very well-{G('written')} script, full of jokes.",
            f"The mountains and countryside are beautifully {G('filmed')}.",
            f"The film is brilliantly {G('directed')} by Steven Spielberg."]
    return EX(id, letter, instr, wordbox(["acted", "chosen", "directed", "filmed", "written"]) + OL(rows))


def while_during(id, letter="", instr="Complete the sentences using <i>while</i> or <i>during</i>."):
    """p. 134, Key words for writing. Ключ: 1 during 2 while 3 While 4 During 5 during 6 While."""
    c = lambda k: C(k, "while", "during")
    rows = [f"The film takes place {c('during')} The Gulf War in 1990.", f"They fall in love {c('while')} she is planning his wedding!",
            f"{c('while')} he’s not looking, he puts a drug in her drink.", f"{c('during')} the night, the toys come alive.",
            f"Lots of things happen {c('during')} the journey that bring the family closer together.",
            f"{c('while')} the parents are away, he has to defend the house against robbers."]
    return EX(id, letter, instr, OL(rows))


NOUN = [("This is a moving love story. It’s about a disabled woman.", "This is a moving love story about a disabled woman."),
        ("This is a comedy action film. It stars Akshay Kumar.", "This is a comedy action film starring Akshay Kumar."),
        ("The film is directed by Lasse Hallstrom. He also directed <i>The Cider House Rules</i>.",
         "The film is directed by Lasse Hallstrom, who also directed The Cider House Rules."),
        ("The film is set in a small town. The story happens during the mayoral election.",
         "The film is set in a small town, during the mayoral election."),
        ("The main character is a brilliant but lonely doctor. The part is superbly played by Jennifer Jenkins.",
         "The main character is a brilliant but lonely doctor, superbly played by Jennifer Jenkins.|"
         "The main character is a brilliant but lonely doctor, a part superbly played by Jennifer Jenkins."),
        ("The documentary follows the lives of four couples. The couples have recently emigrated to Australia.",
         "The documentary follows the lives of four couples who have recently emigrated to Australia.|"
         "The documentary follows the lives of four couples that have recently emigrated to Australia.")]


def after_noun(id, letter="B", instr="Rewrite 1–6 as one sentence using an <i>-ed / -ing</i> participle, a prepositional "
               "phrase, or a relative clause."):
    """p. 135, Grammar B. Ответы — ключ."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in NOUN]))
