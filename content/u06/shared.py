"""Упражнения модуля 6, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, EX, OL, DLG

AH = list("abcdefghi")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


GROUPS = ["opinion", "how things are produced", "material"]
SOUV = [("hand-made", 1), ("silk", 2), ("gorgeous", 0), ("cute", 0), ("beautiful", 0), ("clay", 2), ("horrible", 0),
        ("carved", 1), ("hand-painted", 1), ("lovely", 0), ("plastic", 2), ("leather", 2), ("hand-printed", 1), ("wooden", 2),
        ("machine-woven", 1), ("tacky", 0)]


def souvenir_groups(id, letter="A", instr="Put the words in the box into three groups: 1 opinion, 2 how things are produced, "
                    "3 material."):
    """p. 42, Vocabulary A. Ключ: opinion — beautiful, lovely, gorgeous, horrible, cute, tacky; how things are produced —
    hand-made, hand-printed, hand-painted, machine-woven, carved; material — clay, leather, silk, wooden, plastic."""
    return EX(id, letter, instr, OL([f"<b>{w}</b> → {S(GROUPS[k], GROUPS)}" for w, k in SOUV]))


DESC = ["traditional hand-carved", "lovely silver", "little hand-woven", "really cute", "lovely hand-painted", "tacky plastic",
        "beautiful hand-printed silk", "nice clay"]


def souvenirs(id, letter="C", instr="Complete the sentences with the descriptions in the box."):
    """p. 42, Vocabulary C. Ключ: 1 beautiful hand-printed silk 2 tacky plastic 3 nice clay 4 really cute
    5 lovely hand-painted 6 lovely silver 7 traditional hand-carved 8 little hand-woven."""
    opts = sorted(DESC)
    s = lambda k: S(k, opts)
    rows = [f"My dad bought me what he thought was a {s('beautiful hand-printed silk')} scarf, but it was horrible! I’m never "
            "going to wear it!",
            f"He bought me this {s('tacky plastic')} model of the Eiffel Tower. I don’t know what to do with it. It’s horrible.",
            f"I bought this really {s('nice clay')} pot for cooking. It’s really heavy.",
            f"She bought me this {s('really cute')} teddy bear. I keep it on my bed.",
            f"They bought me this {s('lovely hand-painted')} plate. It looks like it was quite expensive.",
            f"He bought me this {s('lovely silver')} ring when we were in Paris. I’ve been wearing it ever since.",
            f"I bought this {s('traditional hand-carved')} African mask. I’m going to hang it on my wall. It’s great.",
            f"I bought this {s('little hand-woven')} rug. I’ve put it on the floor by my bed."]
    return EX(id, letter, instr, wordbox(DESC) + OL(rows))


YN = ["Yes", "No"]


def phones(id, letter="A", instr='<span class="audio-ic">♪</span> 6.2 Listen and complete the table.'):
    """p. 43, Listening A. Ключ: battery lithium / nickel cadmium; camera yes – 3 / yes – 1.7; memory card yes / no;
    MP3 yes / no; free calls 150 / 200; free texts 100 / 150."""
    rows = [("Kind of battery?", G("lithium"), G("nickel cadmium")),
            ("Camera (mega-pixels)?", G("3|yes 3|yes - 3|3 mega-pixel"), G("1.7|yes 1.7|yes - 1.7")),
            ("Comes with memory card?", S("Yes", YN), S("No", YN)), ("Comes with MP3?", S("Yes", YN), S("No", YN)),
            ("Minutes: free calls?", G("150"), G("200")), ("Number of free text messages?", G("100"), G("150"))]
    return EX(id, letter, instr, '<table class="voc"><tr><th>Features</th><th>N5703</th><th>S620</th></tr>' +
              "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows) + "</table>")


PH_FIX = [("The N5703 is", "slightly", "much", "better quality."),
          ("The lithium battery lasts", "a bit", "a lot|much|far", "longer than the other one."),
          ("The camera on the N5703 is", "more than", "almost", "twice as powerful."),
          ("With the memory card, the N5703 stores", "slightly fewer", "far more|a lot more|many more|much more",
           "photos than the S620."),
          ("The sound quality of the MP3 is", "much worse", "slightly worse|a bit worse", "than on a normal player.")]


def phone_fix(id, letter="C", instr="Correct the information in <i>italics</i>."):
    """p. 43, Listening C. Ключ: 1 much better 2 a lot longer 3 almost twice 4 far more 5 slightly worse."""
    return EX(id, letter, instr, OL([f"{a} <s><i>{w}</i></s> {G(k)} {b}" for a, w, k, b in PH_FIX]))


ONES = ["This phone has an MP3 player,", "This one only has 75 megabytes of memory,", "This one is only £43.99,",
        "These phones are on special offer,", "These ones all use a lithium battery,",
        "You can store up to 100 messages on this one,"]
ONES_END = ["whereas this one is 87.", "whereas this one has a hundred.", "whereas this one doesn’t.",
            "whereas that one only has room for 50.", "whereas those use a nickel cadmium one, which isn’t as good.",
            "whereas those ones aren’t."]


def ones(id, letter="A", instr="Match the sentence halves about two mobile phones."):
    """p. 43, Developing conversations A. Ключ: 1 c 2 b 3 a 4 f 5 e 6 d."""
    key = "c b a f e d".split()
    return EX(id, letter, instr, OL([f"{q} {S(k, AH[:6])}" for q, k in zip(ONES, key)]) + OL(ONES_END, "items alpha"))


ODD = [("necklace / bracelet / chain / belt / ring", "belt"), ("top / shirt / jacket / skirt / jumper", "skirt"),
       ("jeans / trousers / earrings / tracksuit bottoms / leggings", "earrings"),
       ("socks / trainers / sandals / boots / high heels", "socks"), ("scarf / gloves / T-shirt / woolly hat / thick jumper",
                                                                     "T-shirt"),
       ("scruffy / trendy / smart / cool / nice", "scruffy"), ("colourful / stripy / tight / bright / plain / checked", "tight")]


def odd_one(id, letter="A", instr="Decide which is the odd one out in each group and explain your decision."):
    """p. 44, Vocabulary A. Ключ: 1 belt 2 skirt 3 earrings 4 socks 5 T-shirt 6 scruffy 7 tight."""
    return EX(id, letter, instr, OL([C(k, *g.split(" / ")) for g, k in ODD]))


MUST_EX = ["I must try and book some tickets for a gig next week", "You must be able to get tickets somewhere",
           "If you like The Brain Police, you must go and see Spook Train."]
MUST_RULES = ["We often use <i>must</i> to make guesses about things, based on what we know. <i>Must</i> shows we believe "
              "something is very probably true.",
              "We can use <i>You must</i> to strongly recommend things like films, books, shops or tourist attractions.",
              "We use <i>I must</i> when we feel something is very important for us to do. We use <i>I mustn’t</i> when it is "
              "important for us not to do something."]


def must_rules(id, letter="A", instr="Look at the three examples of using <i>must</i> above. Match the examples with rules 1–3."):
    """p. 46, Grammar A. Ключ: 1 b 2 c 3 a."""
    key = ["b", "c", "a"]
    return EX(id, letter, instr, OL(["<i>" + e + "</i>" for e in MUST_EX], "items alpha") +
              OL([f"{r} {S(k, AH[:3])}" for r, k in zip(MUST_RULES, key)]))


MUST_USES = [("You must try the local food while you’re there. It’s great.", "2"),
             ("You must be able to find it cheaper somewhere else.", "1"),
             ("I must make sure I send them the money today.", "3"), ("That’s your third helping! You must be really hungry.", "1"),
             ("I mustn’t forget to thank her for all her help.", "3"), ("It must get really cold there in the winter.", "1"),
             ("You must go to Virgo. They’ve got a sale on.", "2"), ("It’s amazing. You must go and see it if you have time.", "2"),
             ("I really must try and buy a few souvenirs today.", "3")]


def must_uses(id, letter="B", instr="Match a–i to the uses of <i>must</i> 1–3 in exercise A."):
    """p. 46, Grammar B. Ключ: 1 b, d, f 2 a, g, h 3 c, e, i."""
    return EX(id, letter, instr, OL([f"{s} {S(k, ['1', '2', '3'])}" for s, k in MUST_USES], "items alpha"))


MUST_GAPS = [("Can you remind me later? I", "must", "remember to buy a present for my sister before I leave."),
             ("I", "must", "just go and say ‘hello’ to someone. I’ll be right back."),
             ("I have an appointment at half past two. I", "mustn’t", "be late."),
             ("Remind me – I", "mustn’t", "forget to phone my mum when we get to the hotel."),
             ("You really", "must", "try the grilled squid they do here."),
             ("Whatever else you do, you simply", "must", "take the ferry across to the islands. It’s amazing!"),
             ("I’d love some cake, but I really", "mustn’t", ". I’m on a diet!"),
             ("I", "mustn’t", "forget to pay my rent – or I’ll be in big trouble."),
             ("I", "must", "just let my boss know that the time of her flight has been changed."),
             ("I’m sure you’re very busy. I", "mustn’t", "keep you any longer.")]


def must_gaps(id, letter="D", instr="Complete these sentences with <i>must</i> or <i>mustn’t</i>."):
    """p. 47, Grammar D. Ключ: 1 must 2 must 3 mustn’t 4 mustn’t 5 must 6 must 7 mustn’t 8 mustn’t 9 must 10 mustn’t."""
    return EX(id, letter, instr, OL([f"{a} {S(k, ['must', 'mustn’t'])}{'' if b.startswith('.') else ' '}{b}"
                                     for a, k, b in MUST_GAPS]))


CONV1 = [("No, it’s too late for that. They won’t be able to deliver the tickets in time.", 4),
         ("I’m thinking of trying to get a ticket for the match tonight.", 1),
         ("You don’t want to do that. It’s illegal. You might get arrested. I’d try the Internet instead.", 3),
         ("It’s totally sold out. You’ve got no chance. I guess you could go and hang around outside the stadium and buy one "
          "from a ticket tout.", 2)]
CONV2 = [("There isn’t time! He doesn’t want to miss the plane!", 4),
         ("No, I wouldn’t do that! It’s more expensive. You’d be better getting something in town.", 3),
         ("I want to get a present for my girlfriend before I go back.", 1),
         ("Just get something at the airport in Duty Free.", 2),
         ("It’s OK. My flight’s not till three. I think I’ve got time. Where’s the best place to go?", 5)]


def rec_order(id, letter="A", instr="Put the two conversations in the correct order. In each conversation, there are three "
              "speakers."):
    """p. 47, Developing conversations A. Порядок — по ключу (Conversation 1, 2)."""
    def block(conv, n, given):
        nums = [str(i) for i in range(1, n + 1)]
        return '<div class="ord">' + "".join(
            f'<div class="ord-row">{"<b>1</b>" if given and k == 1 else S(str(k), nums)} <span>{t}</span></div>'
            for t, k in conv) + "</div>"
    return EX(id, letter, instr, "<p><b>Conversation 1</b></p>" + block(CONV1, 4, True) +
              "<p><b>Conversation 2</b></p>" + block(CONV2, 5, False))


# ---- Writing 06 (pp. 130–131) ----
def facilities(id, letter="A", instr="Complete the sentences with words from the report in the correct form."):
    """p. 131, Vocabulary A. Ключ: 1 small / limited 2 hang 3 courts 4 runs 5 rarely 6 wider 7 done 8 subsidise 9 consider."""
    rows = [f"There is only a {G('small|limited')} selection of classes you can go to.",
            f"The problem is that there’s nowhere safe for kids to {G('hang')} out with their friends.",
            f"There are several squash {G('courts')} and table tennis tables.",
            f"The school {G('runs')} a drama club in the evenings. Anyone can go.",
            f"There is a sauna at the sports centre, but for some reason it is {G('rarely')} used.",
            f"The cinema could put on a {G('wider')} range of films.",
            f"More could be {G('done')} with the existing facilities: why not open them in the evenings?",
            f"The government should {G('subsidise|subsidize')} swimming pools so everyone can afford to use them.",
            f"The council should {G('consider')} providing free sports equipment."]
    return EX(id, letter, instr, OL(rows))


REF = ["As far as public transport in the area was concerned,", "In terms of the canteen,",
       "As far as the hotel facilities are concerned,", "In terms of security,", "As far as the French classes are concerned,",
       "In terms of the park,"]
REF_END = ["the number of students should be reduced.", "the owners should consider building a swimming pool.",
           "more could be done to stop robberies.", "most people are satisfied with the quality of food.",
           "there’s a good range of play equipment for younger kids.", "many complained that the trains do not run late enough."]


def referring(id, letter="A", instr="Match 1–6 with the endings in a–f."):
    """p. 131, Key words for writing A. Ключ: 1 f 2 d 3 b 4 c 5 a 6 e."""
    key = "f d b c a e".split()
    return EX(id, letter, instr, OL([f"{q} {S(k, AH[:6])}" for q, k in zip(REF, key)]) + OL(REF_END, "items alpha"))
