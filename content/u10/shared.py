"""Упражнения модуля 10, которые выводятся и в «Учебнике», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, EX, OL, ORDER

AH = list("abcdefgh")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


ODD = [(["a horror film", "a thriller", "a romantic comedy", "an installation"], "an installation"),
       (["landscapes", "a trailer", "portraits", "a still life", "abstract"], "a trailer"),
       (["the painting", "the special effects", "the soundtrack", "the plot", "the photography"], "the painting"),
       (["a painter", "a video artist", "a director", "a sculptor", "an audience"], "an audience"),
       (["a drama", "a gig", "a tragedy", "a historical play", "a comedy"], "a gig"),
       (["the scenery", "the lighting", "the costumes", "sculpture", "the acting"], "sculpture")]


def odd_one(id, letter="A", instr="Decide which is the odd one out in each group and explain your decision."):
    """p. 70, Vocabulary A. Ключ: 1 an installation 2 a trailer 3 the painting 4 an audience 5 a gig 6 sculpture."""
    return EX(id, letter, instr, OL([" / ".join(g) + f" → {S(k, g)}" for g, k in ODD]))


WHATS_ON = ["What’s on in town at the moment?", "What kind of exhibition is it?", "What’s it about?", "Where’s it on?",
            "When’s it on?", "Who’s in it?"]
WHATS_ON_ANS = ["They’ve got showings at 6, 8.50 and 11.05. / It’s on till next week and the gallery’s open between 10 and 8.",
                "It’s some kind of romantic comedy. / It’s a drama about life in a rural community.",
                "Nobody I know. / Penelope Cruz and Charlize Theron.",
                "At the Hermitage gallery. / At the ABC Park cinema.",
                "It’s a collection of still-life paintings. / It’s an installation by the Mexican artist Gabriel Orozco.",
                "There’s the new film by Lee Myung-se. / Not much really. There’s a musical on at the theatre that might be OK."]


def whats_on(id, letter="C", instr="Match the questions 1–6 with the pairs of possible answers a–f."):
    """p. 70, Vocabulary C. Ключ: 1 f 2 e 3 b 4 d 5 a 6 c."""
    key = "f e b d a c".split()
    return EX(id, letter, instr, OL([f"{q} → {S(k, AH[:6])}" for q, k in zip(WHATS_ON, key)]) + OL(WHATS_ON_ANS, "items alpha"))


DIR_BOX1 = ["halfway", "front", "off", "next", "at"]
DIR_BOX2 = ["coming", "back", "towards", "out", "facing"]


def directions(id, letter="A", instr="Complete the sentences with the words in the boxes."):
    """p. 71, Developing conversations A. Ключ: 1 halfway 2 front 3 next 4 at 5 off 6 back 7 facing 8 coming 9 towards 10 out."""
    r1 = [f"You know Columbus Avenue? Well, it’s about {G('halfway')} down there.",
          f"You know the cathedral? Well, it’s right in {G('front')} of the main entrance.",
          f"You know the post office? Well, it’s the {G('next')} turning down from there, on the other side of the road.",
          f"You know the cinema? Well, there’s a car park {G('at')} the back.",
          f"You know the main square? Well, Hope Close is one of the streets {G('off')} there. I think it’s the little "
          "pedestrianised one."]
    r2 = [f"If you’ve got your {G('back')} to the station, you turn left.", f"If you’re {G('facing')} the station, it’s on your left.",
          f"If you’re {G('coming')} down the road away from the station, it’s the second turning on the left.",
          f"If you’re going up the road {G('towards')} the station and away from the river, it’s second on the right.",
          f"When you come {G('out')} of the building, you’ll see it right opposite."]
    return EX(id, letter, instr, wordbox(DIR_BOX1) + OL(r1) + wordbox(DIR_BOX2) + OL(r2, start=6))


ADJ = [("spectacular", "positive"), ("touristy", "both"), ("terrible", "negative"), ("dreadful", "negative"),
       ("trendy", "both"), ("dull", "negative"), ("weird", "both"), ("amazing", "positive"), ("marvellous", "positive"),
       ("incredible", "positive"), ("terrific", "positive"), ("brilliant", "positive")]


def adjectives(id, letter="A", instr="Decide if the words in the box are positive, negative or could be both, depending on the context."):
    """p. 72, Vocabulary A. Ответы — ключ."""
    opts = ["positive", "negative", "both"]
    return EX(id, letter, instr, OL([f"<b>{w}</b> → {S(k, opts)}" for w, k in ADJ]))


BOLD = [("authentic", "genuine, real"), ("birthplace", "where it began"), ("fusion", "mix of things"), ("catch", "see"),
        ("squad", "group of players from which team is chosen"), ("exclusive", "difficult to get in"),
        ("crowd", "group of people"), ("keen", "enthusiastic, dedicated"), ("stroll", "walk for pleasure"),
        ("cast", "group of actors")]


def bold_words(id, letter="D", instr="What do the words in <b>bold</b> in the text mean? Match them with the definitions."):
    """p. 72, Reading D. Ответы — ключ."""
    opts = sorted(d for _, d in BOLD)
    return EX(id, letter, instr, OL([f"<b>{w}</b> → {S(d, opts)}" for w, d in BOLD]))


def bold_gaps(id, letter="E", instr="Now use the words in <b>bold</b> to complete these sentences."):
    """p. 72, Reading E. Ключ: 1 exclusive 2 authentic 3 keen 4 birthplace 5 squad 6 stroll 7 catch 8 cast 9 fusion 10 crowd."""
    rows = [f"It’s a very {G('exclusive')} club. It’s members only.", f"They serve really {G('authentic')} Mexican food there.",
            f"My uncle is really fit. He’s a very {G('keen')} runner.",
            f"Mississippi is the {G('birthplace')} of the blues, country music, and rock &amp; roll.",
            f"I don’t think Real Madrid will win the league this year. Their {G('squad')} isn’t strong enough.",
            f"It’s a lovely evening. Let’s go out for a {G('stroll')} around town.",
            f"If you ever get the chance to {G('catch')} him playing live, don’t miss it! He’s just incredible.",
            f"It’s got an amazing {G('cast')}, but it’s an awful film.", f"His music is a clever {G('fusion')} of jazz and hip-hop.",
            f"It’s a nice club, but it does attract a very young {G('crowd')}."]
    return EX(id, letter, instr, OL(rows))


# p. 72, Developing conversations A: (слова вразброс, правильное выражение)
EXPR = [("it’s my thing really kind not of", "It’s not really my kind of thing."),
        ("don’t like really I feel it", "I don’t really feel like it."),
        ("that mood I’m kind not for really in of the thing", "I’m not really in the mood for that kind of thing."),
        ("me sounds trendy it for a bit too", "It sounds a bit too trendy for me."),
        ("touristy it looks me too for a bit", "It looks a bit too touristy for me."),
        ("too weird a bit me sounds for it", "It sounds a bit too weird for me.")]


def expressions(id, letter="A", instr="Put the words in the correct order to make six common expressions."):
    """p. 72, Developing conversations A (проверка — аудио 10.3; в ключах ответов нет, порядок слов однозначен)."""
    return EX(id, letter, instr, OL([ORDER(s, a) for s, a in EXPR]))


EVENT = ["It was really good, but they were quite weird paintings.", "It’s OK – a bit overrated, though.", "It was really moving.",
         "It was boiling hot.", "It was completely sold out.", "It’s very trendy – full of young, beautiful people.",
         "They were rubbish – just very dull.", "Amazing. There was such a great atmosphere."]
EVENT_END = ["It wasn’t as brilliant as everyone’s been saying.", "I can’t really describe them or say why I like them!",
             "I was sweating like crazy.", "It was absolutely packed.", "I was in tears by the end.",
             "The music, the people, everything.", "I felt a bit out of place.", "We actually left halfway through."]


def event(id, letter="A", instr="Match 1–8 with a–h."):
    """p. 74, Vocabulary A. Ключ: 1 b 2 a 3 e 4 c 5 d 6 g 7 h 8 f."""
    key = "b a e c d g h f".split()
    return EX(id, letter, instr, OL([f"{q} → {S(k, AH)}" for q, k in zip(EVENT, key)]) + OL(EVENT_END, "items alpha"))


def kinds(id, letter="A", instr="<span class=\"audio-ic\">♪</span> 10.5 Listen and decide what kind of event each person went to."):
    """p. 75, Listening A. Ключ: 1 film 2 club 3 play."""
    return EX(id, letter, instr, OL([f"Conversation 1: {G('film')}", f"Conversation 2: {G('club')}", f"Conversation 3: {G('play')}"]))


def fip_gaps(id, letter="B", instr="Complete the sentences with one word in each gap."):
    """p. 75, Grammar B. Ключ: 1 to; would; was 2 were; would 3 would; would."""
    rows = ['<div class="dlg"><b>A:</b><span>Did you go and see <i>The Bridge</i> last night?</span>'
            f'<b>B:</b><span>No, I was going {G("to")}, but I had an essay to hand in and it took longer than I thought it '
            f'{G("would")}, so by the time I’d finished, it {G("was")} too late.</span></div>',
            '<div class="dlg"><b>A:</b><span>What did you do at the weekend?</span>'
            f'<b>B:</b><span>Nothing much. We {G("were")} going to go to the beach, but the weather was so awful, we just stayed '
            'at home.</span>'
            f'<b>A:</b><span>I know. It was terrible – and on the forecast they said it {G("would")} be sunny!</span></div>',
            '<div class="dlg"><b>A:</b><span>Is Keira coming?</span>'
            f'<b>B:</b><span>She wasn’t sure. She said she {G("would")} meet us at the cinema if she finished work on time. Oh, '
            f'and she promised she {G("would")} ask James to come as well.</span></div>']
    return EX(id, letter, instr, OL(rows))


FIP = [("They / have a barbecue / start pouring with rain / have to cook indoors instead",
        "They were going to have a barbecue but it started pouring with rain so they had to cook indoors instead."),
       ("We / go to the beach for the day / miss the train / end up going to the park instead",
        "We were going to go to the beach for the day but we missed the train so we ended up going to the park instead."),
       ("She / give me a lift / car not start / get a taxi instead",
        "She was going to give me a lift but the car wouldn’t start so I got a taxi instead.|"
        "She was going to give me a lift but the car didn’t start so I got a taxi instead."),
       ("I / drive here / start pouring with rain / have to drive", "I was going to walk here but it started pouring with rain so I had to drive.|"
        "I was going to drive here but it started pouring with rain so I had to drive."),
       ("I / stay in and study / a friend call me / go out / meet him",
        "I was going to stay in and study but a friend called so I went out to meet him.")]


def fip_rewrite(id, letter="C", instr="Make sentences using the ideas in 1–6 and linking them with <i>but</i> and <i>so</i>."):
    """p. 75, Grammar C. Ответы — ключ (в п. 5 учебника опечатка: в ключе «walk here»)."""
    ex = ('<p class="ex-line">1 I / go out / feel exhausted / just stay in and go to bed early<br>'
          '<i>I was going to go out but I felt exhausted so I just stayed in and went to bed early.</i></p>')
    return EX(id, letter, instr, ex + OL([f"{q}<br>{G(a, 'wide')}" for q, a in FIP], start=2))
