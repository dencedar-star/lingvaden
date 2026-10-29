"""Упражнения модуля 3, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, EX, OL

AH = list("abcdefgh")
BOX1 = ["galleries", "lake", "market", "palace", "square"]
BOX2 = ["old town", "castle", "mosque", "ruins", "theme park"]


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


def places(id, letter="A", instr="Complete the sentences with the words in the boxes."):
    """p. 20, Vocabulary A. Ключ: 1 lake 2 market 3 square 4 palace 5 galleries 6 castle 7 theme park 8 old town 9 ruins 10 mosque."""
    r1 = [f"There’s a huge {G('lake')} about ten miles outside of town, which is a great place to go fishing.",
          f"There’s a great street {G('market')} out in the east of the city.",
          f"There are lots of nice cafés and restaurants in the main {G('square')}.",
          f"There’s an old royal {G('palace')} down by the river. They were restoring it for years and they’ve just reopened it.",
          f"It’s a very cultural city. There are lots of great museums and {G('galleries')} there."]
    r2 = [f"There’s an incredible {G('castle')} there, where the Royal Family spend their holidays.",
          f"There’s a really fun {G('theme park')} down by the beach. They’ve got some great rides there.",
          f"There are some historic buildings in the {G('old town')}.",
          f"There are lots of ancient {G('ruins')} to go and see all along the coast.",
          f"There’s a beautiful {G('mosque')} near here. You’ll hear the call to prayer in the morning."]
    return EX(id, letter, instr, wordbox(BOX1) + OL(r1) + wordbox(BOX2) + OL(r2, start=6))


def preps(id, letter="B", instr="Complete the expressions with prepositions from exercise A."):
    """p. 20, Vocabulary B. Ключ: a outside of town b out in the west c down by the river d all along the coast."""
    rows = [f"<b>about</b> ten miles / sixty kilometres / an hour {G('outside')} <b>of town</b>",
            f"{G('out')} <b>in the</b> west of the city / desert / country",
            f"{G('down')} <b>by the</b> river / beach / lake",
            f"<b>all</b> {G('along')} <b>the</b> coast / river / canal"]
    return EX(id, letter, instr, OL(rows, "items alpha"))


def recommend(id, letter="C", instr="Complete the sentences. Then listen again to check your answers."):
    """p. 21, Listening C. Ключ: 1 wonder 2 thinking 3 recommend 4 on what 5 fan 6 could 7 How about 8 book / place."""
    rows = [f"I {G('wonder')} if you can help me.", f"I’m {G('thinking')} of going sightseeing today.",
            f"Can you {G('recommend')} anywhere good to go?", f"It depends {G('on what')} you like.",
            f"I’m not really a big {G('fan')} of churches, to be honest.", f"Well, in that case, you {G('could')} try Kazimierz.",
            f"{G('How about')} a guided tour of Nowa Huta?", f"I can call and {G('book')} a {G('place')} for you, if you want."]
    return EX(id, letter, instr, OL(rows))


# p. 21, Developing conversations A: (реплика в порядке учебника, номер по ключу)
CONV1 = [("Well, <b>you could try</b> Oxford Street. There are lots of big department stores there.", 2),
         ("Oh, OK. Well, <b>in that case, how about</b> Portobello Road? It’s a big street market. You can find lots of bargains there.", 4),
         ("<b>To be honest, I’m not really a big fan of</b> department stores.", 3),
         ("Oh, that sounds great. I love that kind of thing. Is it easy to get to?", 5),
         ("<b>I’m thinking of doing</b> some shopping today. Can you recommend anywhere?", 1),
         ("Yes, very. Here. I’ll show you on the map.", 6)]
CONV2 = [("Right. I’m not really into museums, to be honest.", 3),
         ("Well, you could try the local museum. That’s quite close to here. They’ve got lots of interesting things in there.", 2),
         ("No, it’s quite cheap. It should only be about $10.", 6),
         ("I’m thinking of doing some sightseeing today. Can you recommend anywhere?", 1),
         ("Oh, that sounds better. Is it expensive to get into?", 5),
         ("That’s OK. In that case, how about going to the Roman ruins down by the lake? There are also some nice cafés and you "
          "can swim there.", 4)]


def conv_order(id, letter="A", instr="Put the two conversations into the correct order.", given=True):
    """p. 21. Порядок — по ключу (pp. 20–21, Developing Conversations A)."""
    nums = [str(i) for i in range(1, 7)]

    def block(conv, first_given):
        out = []
        for t, k in conv:
            sel = "<b>1</b>" if first_given and k == 1 else S(str(k), nums)
            out.append(f'<div class="ord-row">{sel} <span>{t}</span></div>')
        return '<div class="ord">' + "".join(out) + "</div>"
    return EX(id, letter, instr, block(CONV1, given) + "<hr>" + block(CONV2, False))


PROBLEMS_BOX = ["arguing + angry", "stole + spoilt", "stuck + hours", "crowded + space", "upset + threw up", "poured + windy",
                "ripped off + charged", "missed + lost"]


def problems(id, letter="B", instr="Complete the sentences with the pairs of words from the box."):
    """p. 22, Vocabulary B. Ключ: 1 missed, lost 2 stole, spoilt 3 crowded, space 4 poured, windy 5 upset, threw up
    6 ripped off, charged 7 arguing, angry 8 stuck, hours."""
    rows = [f"Our flight was delayed so we {G('missed')} our connecting flight. Then they {G('lost')} our luggage.",
            f"Two days before we left, we got robbed. Someone {G('stole')} my bag with my camera, purse and passport. We’d actually "
            f"had a lovely time up till then, but that rather {G('spoilt')} the holiday.",
            f"The beach was always really {G('crowded')}. You could hardly find a {G('space')} to put your towel.",
            f"The weather was awful. It {G('poured')} with rain most of the time and it was really {G('windy')} as well.",
            f"I don’t know if it was the food or the water, but I had a really bad {G('upset')} stomach. I was in and out of the "
            f"toilet for three days and I {G('threw up')} twice.",
            f"We got {G('ripped off')} a couple of times. In one restaurant, they {G('charged')} €20 for a salad.",
            f"My sisters didn’t stop {G('arguing')} with each other the whole time we were away, and then my parents got "
            f"{G('angry')} with them. It was a nightmare!",
            f"There was an accident on the motorway. We were {G('stuck')} in a traffic jam for {G('hours')}."]
    return EX(id, letter, instr, wordbox(PROBLEMS_BOX) + OL(rows))


NUMS = [("millions", "people stuck in traffic"), ("20", "days of holiday entitlement"), ("16", "public holidays in Slovenia"),
        ("hundreds", "people getting sunburnt"), ("eight", "bank holidays"), ("one", "holiday cancelled in France"),
        ("three", "amount of new public holidays union wants"), ("twenty-one", "government workers holidays in Puerto Rico")]


def numbers(id, letter="D", instr="What do these numbers in the article refer to?"):
    """p. 22, Reading D. Ответы — формулировки ключа."""
    opts = sorted(d for _, d in NUMS)
    return EX(id, letter, instr, OL([f"<b>{n}</b> → {S(d, opts)}" for n, d in NUMS]))


WEATHER = ["It said it’ll be hot and humid during the day, and so", "They said it’s going to be really windy, so",
           "Apparently, it’s going to be really sunny, so", "They said it’s going to be freezing and",
           "They said it’s going to be boiling hot all week and", "Apparently, it’s going to pour down tomorrow, so",
           "They said it’s going to be generally quite warm, but", "The same as today: grey, cloudy, cold, but"]
WEATHER_END = ["it might drop to minus 10°.", "on Tuesday it might reach 36°. I hate the heat!",
               "there might possibly be a storm this evening.", "we should take down the parasol or it’ll blow away.",
               "I’ll probably stay at home and keep out of the rain!", "hopefully I might get a bit of a suntan!",
               "they said it might clear up next week!", "it might be a bit chilly, especially at night."]


def weather(id, letter="A", instr="Match the sentence halves."):
    """p. 24, Vocabulary A. Ключ: 1c 2d 3f 4a 5b 6e 7h 8g."""
    key = "c d f a b e h g".split()
    return EX(id, letter, instr, OL([f"{q} … {S(k, AH)}" for q, k in zip(WEATHER, key)]) + OL(WEATHER_END, "items alpha"))


FUT = ["I’m <b>not going to</b> be here.", "I’<b>ve got</b> a week off work.", "It’<b>ll probably</b> clear up later.",
       "We’<b>re thinking of</b> going to Palermo.", "I’<b>ve got to</b> work.", "I’<b>m having</b> lunch with my parents.",
       "I <b>might</b> go for a picnic in the park."]
FUT_DEF = ["Something which is definite / planned / organised.", "Something which is uncertain / unplanned.", "An obligation.",
           "Only a 50% certainty."]
FUT_OPTS = ["a", "b", "c", "d", "a, b", "a, c", "a, d", "b, c", "b, d", "c, d"]


def future_match(id, letter="B", instr="Match the structures 1–7 from <i>Listening</i> with a–d below. Some structures match more than once."):
    """p. 25, Grammar B. Ключ: 1 a 2 a 3 b 4 d 5 a, c 6 a 7 b, d."""
    key = ["a", "a", "b", "d", "a, c", "a", "b, d"]
    return EX(id, letter, instr, OL([f"{s} → {S(k, FUT_OPTS)}" for s, k in zip(FUT, key)]) + OL(FUT_DEF, "items alpha"))


FUT_BOX = ["going to", "’ll", "thinking", "might", "meeting", "’s got", "’ve got to", "might"]


def future_gaps(id, letter="C", instr="Complete the conversations with the words in the box."):
    """p. 25, Grammar C. Ключ: 1 thinking 2 ’ll 3 might 4 meeting 5 ’s got 6 might 7 going to 8 ’ve got to."""
    opts = sorted(set(FUT_BOX))
    s = lambda k: S(k, opts)
    d1 = ('<div class="dlg"><b>A:</b><span>Are you going away in the summer?</span>'
          f'<b>B:</b><span>Probably, but we’re <sup>1</sup>{s("thinking")} of leaving it to the last minute to book, and trying to '
          'get some cheap package deal to Greece or somewhere like that. What about you?</span>'
          f'<b>A:</b><span>Not abroad. We<sup>2</sup>{s("’ll")} probably just go to my parents’ in Scotland at some point. I suppose '
          f'we <sup>3</sup>{s("might")} go camping if the weather’s OK, but it really depends on my wife. She’s not a big fan of '
          'camping.</span></div>')
    d2 = ('<div class="dlg"><b>A:</b><span>Have you got any plans for the weekend?</span>'
          f'<b>B:</b><span>Yeah, I’m probably <sup>4</sup>{s("meeting")} a friend on Sunday, but I’m waiting for him to confirm. '
          f'He<sup>5</sup>{s("’s got")} an exam next week, so he <sup>6</sup>{s("might")} have to study on Sunday – it depends how '
          f'much he gets done on Saturday. Anyway, he is <sup>7</sup>{s("going to")} ring me at some point on Saturday evening to '
          'confirm. Why? What about you?</span>'
          f'<b>A:</b><span>Well, unfortunately, I<sup>8</sup>{s("’ve got to")} do some shopping at some point, as I’ve got nothing '
          'in the fridge. Apart from that, no plans at all.</span>'
          '<b>B:</b><span>Well, we could meet up on Saturday, if you like.</span></div>')
    return EX(id, letter, instr, wordbox(FUT_BOX) + d1 + d2)


# ---- Writing 03 (pp. 124–125) ----
STORY_ORDER = [("I could feel the wind <b>rushing</b> past me as I fell.", "2"), ("I <b>floated</b> slowly down.", "4"),
               ("I moved my feet closer to the <b>edge</b> and looked down!", "1"), ("Eventually, I pulled the <b>cord</b>.", "3")]


def story_order(id, letter="", instr="What order would you expect them to happen in?"):
    """p. 124, Writing. Ключ: Order: c, a, d, b."""
    return EX(id, letter, instr, OL([f"{t} → {S(k, ['1', '2', '3', '4'])}" for t, k in STORY_ORDER], "items alpha"))


HALVES = ["I was just about to give up and stop looking", "She was just about to go back to bed", "We were just about to kiss",
          "Just as we were all sitting down to eat dinner,", "Just as the band appeared on the stage,",
          "Just as I was walking out of the store,"]
HALVES_END = ["when she suddenly heard a strange noise downstairs.", "three men ran in, holding guns and pushed past me.",
              "when suddenly I saw something shiny in the dirt.", "there was a loud knock at the door.",
              "when my ex-boyfriend suddenly walked in.", "the woman next to me started screaming like crazy!"]


def just_match(id, letter="A", instr="Match the sentence halves."):
    """p. 125, Key words for writing A. Ключ: 1 c 2 a 3 e 4 d 5 f 6 b."""
    key = "c a e d f b".split()
    return EX(id, letter, instr, OL([f"{q} … {S(k, AH[:6])}" for q, k in zip(HALVES, key)]) + OL(HALVES_END, "items alpha"))


JUST = [("We were planning to leave. Then they gave us a table. (just about to)",
         "We were just about to leave when they gave us a table."),
        ("I was planning to give up and go home. Then I saw him walking towards me. (just about to)",
         "I was just about to give up and go home when I saw him walking towards me."),
        ("I was planning to go to bed. Then the doorbell rang. (just about to)",
         "I was just about to go to bed when the doorbell rang."),
        ("We were walking towards our car. A police car drove up and stopped right in front of us. (just as)",
         "Just as we were walking towards our car, a police car drove up and stopped right in front of us."),
        ("We were starting to think the holiday would be a disaster. At that moment, the sun came out. (just as)",
         "Just as we were starting to think the holiday would be a disaster, the sun came out.")]


def just_rewrite(id, letter="C", instr="Rewrite 1–5 as one sentence. Link your ideas using the words in brackets."):
    """p. 125, Key words for writing C. Ответы — ключ."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in JUST]))


VERBS = ["slam", "grab", "shout", "stare", "rush", "creep", "whisper"]
DEFS = [("say very quietly", "whisper"), ("move very quietly / slowly", "creep"), ("look at something a long time", "stare"),
        ("close / put something angrily / loudly", "slam"), ("say very loudly", "shout"), ("run / go in a hurry", "rush"),
        ("take hold with your hand suddenly", "grab")]


def verbs_match(id, letter="A", instr="Match the descriptive verbs and definitions."):
    """p. 125, Vocabulary A. Ключ: 1 whisper 2 creep 3 stare 4 slam 5 shout 6 rush 7 grab."""
    return EX(id, letter, instr, wordbox(VERBS) + OL([f"{d} → {S(k, VERBS)}" for d, k in DEFS]))


def verbs_gaps(id, letter="C", instr="Complete the sentences with a word from exercise A."):
    """p. 125, Vocabulary C. Ключ: 1 rushed 2 slammed 3 stared 4 grabbed 5 shouting 6 crept 7 whisper."""
    rows = [f"The train was leaving in ten minutes, so we {G('rushed')} to the station.",
            f"He ran out and {G('slammed')} the door shut behind him.", f"I {G('stared')} at the paper. I couldn’t believe it!",
            f"Just as I was leaving, someone {G('grabbed')} my bag and ran off.",
            f"It was chaos. Everyone was screaming and {G('shouting')}.",
            f"I {G('crept')} down the stairs trying not to make a noise.",
            f"I tried to {G('whisper')} the answer to my friend, but the teacher heard me."]
    return EX(id, letter, instr, OL(rows))
