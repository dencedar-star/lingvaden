"""Упражнения модуля 13, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, EX, OL, DLG

AH = list("abcdefghijkl")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


WAYS = ["by train", "by ferry", "by car", "by plane"]
TRAVEL = [("security", "by plane"), ("line", "by train"), ("crossing", "by ferry|by train|by car"), ("take-off", "by plane"),
          ("carriage", "by train"), ("deck", "by ferry"), ("platform", "by train"), ("traffic lights", "by car"),
          ("bend", "by car"), ("tyre", "by car"), ("harbour", "by ferry"), ("check-in desk", "by plane")]


def travel_sort(id, letter="A", instr="Match the words in the box with a way of travelling: by train, by ferry, by car or by plane."):
    """p. 92, Vocabulary A. Ключ: train – carriage, line, platform; ferry – crossing, deck, harbour; car – bend, tyre,
    traffic lights; plane – take-off, check-in desk, security (crossing — также поезд или машина)."""
    return EX(id, letter, instr, OL([f"<b>{w}</b> → {S(k, WAYS)}" for w, k in TRAVEL]) +
              '<p class="note-s">Ключ: <i>crossing</i> может относиться и к поезду (level crossing), и к машине '
              '(pedestrian crossing).</p>')


def travel_nouns(id, letter="C", instr="Complete the sentences below with nouns from exercise A."):
    """p. 92, Vocabulary C. Ключ: 1 platform 2 deck 3 tyre 4 take-off 5 crossing 6 line 7 security 8 bend."""
    rows = [f"I was waiting on the wrong {G('platform')} and so I ended up missing my train!",
            f"The sea was really rough. It was pouring with rain and very windy, so we couldn’t go out on {G('deck')}.",
            f"We got a flat {G('tyre')} on the motorway and had to stop and change it.",
            f"I hate flying. I get really anxious – especially during {G('take-off')} and landing.",
            f"Last time we came over it was quite rough, but this time we had a very smooth {G('crossing')}. It was lovely.",
            f"There’d been a terrible storm and there were trees on the {G('line')}, so the train was delayed for ages.",
            f"I got stopped going through {G('security')} and they confiscated a little penknife that I’d forgotten to take "
            "out of my bag.",
            f"It was terrifying. The taxi driver overtook another car on quite a tight {G('bend')}. You couldn’t see if "
            "anyone was coming in the opposite direction."]
    return EX(id, letter, instr, OL(rows))


def phrasal(id, letter="A", instr="Look at the extracts from <i>Listening</i>. Write the phrasal verbs that were used in "
            "place of the words in <i>italics</i>."):
    """p. 93, Vocabulary A. Ключ: 1 hanging around 2 go through 3 check-in 4 set off 5 pour down 6 work out 7 got back
    8 calm down."""
    rows = [("Andre didn’t want to spend too long <i>sitting, waiting and not doing much</i> at the airport.",
             "hanging around|hanging about"),
            ("I don’t want to <i>experience something unpleasant like</i> that again, I can tell you!", "go through"),
            ("Do you want to go to the office, or do you want to <i>sign and get your room</i> at the hotel first?",
             "check in|check-in"),
            ("Well, to begin with, it was still dark when we <i>started our journey</i>.", "set off"),
            ("And then it immediately started to <i>rain very heavily</i>, so the roads were really slippery.", "pour down"),
            ("I couldn’t <i>find an answer to the problem of</i> where I was or where I was going!", "work out"),
            ("When I finally <i>returned</i> onto the right road, I almost had an accident.", "got back"),
            ("I did have to stop and park the car for a few minutes to <i>stop feeling so angry and upset</i>.", "calm down")]
    return EX(id, letter, instr, OL([f"{t}<br>→ {G(a)}" for t, a in rows]))


def particles(id, letter="B", instr="Complete the sentences with the missing particle."):
    """p. 93, Vocabulary B. Ключ: 1 set off 2 checked in 3 hang around 4 get back / in 5 calm down 6 went through
    7 work out 8 pour down."""
    rows = [f"We set {G('off')} at 5 in the morning, so I’m exhausted.",
            f"We didn’t have to queue because we checked {G('in')} online.",
            f"We had to hang {G('around|about')} at the station for an hour because my mum couldn’t pick us up till 4.",
            f"I was exhausted. I left home at 6 in the morning and I didn’t get {G('back|in')} till ten at night.",
            f"My child got into a panic and she wouldn’t calm {G('down')}.",
            f"We went {G('through')} absolute hell to get here, I can tell you!",
            f"I was totally lost. I couldn’t work {G('out')} where I was.",
            f"It started to pour {G('down')} halfway there. We were absolutely soaked by the time we arrived."]
    return EX(id, letter, instr, OL(rows))


def third_box(id, letter="A", instr="Complete the explanation with one word in each space."):
    """p. 95, Grammar A. Ключ: been, never, have, had (past, would, participle)."""
    body = ('<div class="box"><p><b>At the end of the article in <i>Reading</i>, Martin O’Neill, the author, says:</b></p>'
            f'<p class="ex-line">If she hadn’t {G("been")} so determined, she would {G("never")} have made it to Australia.</p>'
            f'<p class="ex-line">I would probably {G("have")} ended up in trouble if I {G("had")} stayed there.</p><hr>'
            f'<p><b>These are examples of a third conditional. The <i>if</i> part of the sentence uses the {G("past")} perfect '
            f'to talk about imagined situations in the past. The second part of the sentence uses {G("would")} / <i>might</i> '
            f'+ <i>have</i> + the past {G("participle")} to talk about the results of the imagined situation.</b></p></div>')
    return EX(id, letter, instr, body)


THIRD = ["Our country would have been in a worse situation", "If it hadn’t been for the war,", "They wouldn’t have crashed",
         "If I hadn’t had that teacher,", "If we’d left a bit earlier,", "The team might have won"]
THIRD_END = ["I probably would never have gone to university.", "if they had been driving more slowly.",
             "if all the players had been fit.", "if we hadn’t had immigration.", "we would’ve stayed in our country.",
             "we might not have missed the beginning of the film."]


def third_match(id, letter="B", instr="Match 1–6 with a–f."):
    """p. 95, Grammar B. Ключ: 1 d 2 e 3 b 4 a 5 f 6 c."""
    key = "d e b a f c".split()
    return EX(id, letter, instr, OL([f"{q} … {S(k, AH[:6])}" for q, k in zip(THIRD, key)]) + OL(THIRD_END, "items alpha"))


STRONG_Q = ["What was the weather like in Greece? Was it hot?", "What was the weather like in Finland? Was it cold?",
            "What was Istanbul like? It’s quite a big city, isn’t it?", "What was the food like in Italy? Was it good?",
            "So what was your trip like? Was it good?", "How was the journey back? Did you get wet in that storm?",
            "You must be angry about them losing your luggage.", "You must be tired after such a long journey.",
            "You must be hungry after such a long journey.", "It’s supposed to be quite a dirty city, isn’t it?",
            "It’s supposed to be quite crowded, isn’t it?", "Tabriz is supposed to be quite an interesting city."]
STRONG_A = ["Great, really delicious. They really know how to eat.",
            "We got absolutely soaked! I didn’t have an umbrella or anything.", "Yeah, it was fantastic! We had a great time.",
            "Yeah, it was boiling – over 40 degrees most days.", "Yeah, it’s huge. The population’s around 12 million.",
            "Yeah, it was freezing – around minus 10 most days.", "Yes, it was really filthy! I couldn’t believe it.",
            "Yeah, I am. I’m exhausted. I’m ready for bed.", "Yeah, it was. It was absolutely packed when we went!",
            "Yeah, it’s fascinating. It dates back over a thousand years.", "I am. I’m absolutely furious!",
            "I am. I’m starving. Have you got anything to eat?"]


def strong_match(id, letter="A", instr="Match the questions 1–6 to the responses a–f. Then match the comments in 7–12 to the "
                 "responses g–l."):
    """p. 96, Vocabulary A. Ключ: 1d 2f 3e 4a 5c 6b 7k 8h 9l 10g 11i 12j."""
    key = "d f e a c b k h l g i j".split()
    return EX(id, letter, instr,
              OL([f"{q} … {S(k, AH[:6])}" for q, k in zip(STRONG_Q[:6], key[:6])]) + OL(STRONG_A[:6], "items alpha") +
              OL([f"{q} … {S(k, AH[6:])}" for q, k in zip(STRONG_Q[6:], key[6:])], start=7) +
              '<ol class="items alpha" start="7">' + "".join(f"<li>{a}</li>" for a in STRONG_A[6:]) + "</ol>")


def mistakes(id, letter="B", instr="Listen again. Complete the phrases about the mistakes each person made."):
    """p. 96, Listening B. Ключ: 1 thought more carefully 2 looked around more 3 stayed in the sun; put on some sun cream
    4 brought another suitcase."""
    rows = [f"It was stupid – I should’ve {G('thought more carefully|thought')} about what to pack.",
            f"We were silly. We should’ve {G('looked around more')}.",
            f"Oh, it was my own fault. I shouldn’t have {G('stayed in the sun')} for so long, especially with my skin! I "
            f"should’ve at least {G('put on some sun cream|put some sun cream on')}!",
            f"I told you we should’ve {G('brought another suitcase')}."]
    return EX(id, letter, instr, OL(rows))


def blame(id, letter="A", instr="Complete the sentences with one word in each gap."):
    """p. 97, Developing conversations A. Ключ: 1 blame, should 2 my, taken, have 3 yours, been 4 fault, should
    5 myself, had 6 have, fault."""
    rows = [f"Don’t {G('blame')} me. You {G('should')}’ve read the small print.",
            f"It’s not {G('my')} fault we’re late. If you hadn’t {G('taken')} so long to get ready, we would {G('have')} "
            "caught the train.",
            f"It’s not his fault – it’s {G('yours')}! You were the one who was driving. You should’ve {G('been')} more careful.",
            f"If you ask me, it’s the airline’s {G('fault')}. They {G('should')} have waited for us for one more minute.",
            f"I blame {G('myself')}. I should’ve listened to my dad. If I {G('had')} done what he said, none of this would’ve "
            "happened.",
            f"The problem could {G('have')} happened to anyone. It’s nobody’s {G('fault')}. It’s just one of those things that "
            "happen."]
    return EX(id, letter, instr, OL(rows))


# ---- Writing 07 (pp. 132–133) ----
ESSAY_BOX = ["obviously", "However", "Otherwise", "Secondly", "Firstly", "thirdly", "In conclusion", "Personally"]
TRENDS = [("Public transport {} (improve) dramatically over the last few years. Despite this, more and more people {} (drive) "
           "into the city centre to work every day.", ["has improved", "are driving"]),
          ("Crime {} (get) worse and worse at the moment. The government {} (recently / increase) the amount of money "
           "available to the police, but this has not made much difference.", ["is getting", "has recently increased"]),
          ("It is said that children’s behaviour these days {} (get) worse and worse. Many parents today seem unconcerned "
           "about these problems, whilst society as a whole {} (stop) caring about the young.", ["is getting", "has stopped"]),
          ("The number of women working {} (increase) a lot in recent years and more and more women {} (now / become) bosses.",
           ["has increased", "are now becoming"]),
          ("Over the last few years, there {} (be) several stories about people helping loved ones to die and euthanasia {} "
           "(become) a major issue. As such, several pressure groups {} (now / call) for a change in the law.",
           ["have been", "has become", "are now calling"])]


def trends(id, letter="A", instr="Complete these sentences by putting the verbs in brackets into the correct form."):
    """p. 133, Grammar A. Ключ: 1 has improved, are driving 2 is getting, has recently increased 3 is getting, has stopped
    4 has increased, are now becoming 5 have been, has become, are now calling."""
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
    key = "c d a e b".split()
    return EX(id, letter, instr, OL([f"{q} … {S(k, AH[:5])}" for q, k in zip(SUCH, key)]) + OL(SUCH_END, "items alpha"))
