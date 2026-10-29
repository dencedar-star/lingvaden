"""Упражнения модуля 12, которые выводятся и в «Учебнике», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, EX, OL

AH = list("abcdefghij")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


CHAR1 = ["shy", "outgoing", "competitive", "naughty", "bright", "easy-going"]
CHAR2 = ["chatty", "spoilt", "generous", "intense", "lazy", "stubborn"]


def character(id, letter="A", instr="Complete the sentences with the adjectives in the boxes."):
    """p. 82, Vocabulary A. Ключ: 1 bright 2 outgoing 3 shy 4 easy-going 5 competitive 6 naughty 7 intense 8 lazy
    9 stubborn 10 generous 11 spoilt 12 chatty."""
    r1 = [f"He’s very clever – just really {G('bright')}.", f"She’s really friendly – really {G('outgoing')}. She’s really good "
          "at making new friends.", f"She’s quite quiet – quite {G('shy')}.", f"They’re very relaxed – just very {G('easy-going')}.",
          f"He’s very sporty, and very {G('competitive')}. He always wants to win!",
          f"He’s very sweet and affectionate, but he can be quite {G('naughty')} sometimes."]
    r2 = [f"He’s quite serious – quite {G('intense')}.", f"He’s a bit of a dropout – just very {G('lazy')}.",
          f"She’s very determined. In fact, she can be very {G('stubborn')}.",
          f"They’re strict, but they can also be very kind and {G('generous')}.",
          f"He’s very indulgent with his daughter. He gives her whatever she asks for, so she’s very {G('spoilt')}.",
          f"He can seem quite quiet when you first meet him, but he’s actually quite {G('chatty')} and funny once you get to "
          "know him."]
    return EX(id, letter, instr, wordbox(CHAR1) + wordbox(CHAR2) + OL(r1 + r2))


LIKE = ["He never does anything around the house.", "When he sees me, he always runs up and gives me a big hug. It’s so sweet.",
        "He’s so serious. He’s always talking about politics. You can never just have a good laugh with him.",
        "He lets her do whatever she wants – really spoils her.", "She really hates losing at whatever sport she does."]
LIKE_END = ["That’s like my cousin. He’s really competitive as well. He always plays to win. He can never just play for fun.",
            "That’s like my brother-in-law. He’s very intense.", "Ah! That’s like my niece. She’s really affectionate too.",
            "That’s like a friend of mine. He’s very indulgent too and his kid’s a nightmare – just really naughty.",
            "That’s like my sister. She’s really lazy too."]


def thats_like(id, letter="A", instr="Match sentences 1–5 with the comments a–e."):
    """p. 83, Developing conversations A. Ключ: 1 e 2 c 3 b 4 d 5 a."""
    key = "e c b d a".split()
    return EX(id, letter, instr, OL([f"{q} → {S(k, AH[:5])}" for q, k in zip(LIKE, key)]) + OL(LIKE_END, "items alpha"))


HEARD = [("Where did you {} to?", "disappear", "dissolve"), ("Maybe I am {} a bit.", "exaggerating", "excited"),
         ("Do you and your brother get {} well?", "on", "in"), ("He {} a scholarship to study Physics.", "won", "awarded"),
         ("We used to be quite {}.", "close", "closed"), ("He’s always going on {} and complaining about me using the car too "
                                                          "much.", "demonstrations", "manifestations"),
         ("Maybe it’s just a {} he’s going through.", "phase", "phrase"), ("He might grow {} it.", "out of", "up")]


def heard(id, letter="B", instr="Choose the words that you heard."):
    """p. 83, Listening B. Ключ: 1 disappear 2 exaggerating 3 on 4 won 5 close 6 demonstrations 7 phase 8 out of.
    Варианты — в порядке учебника."""
    order = [(1, 0)] * 6 + [(0, 1)] * 2
    rows = []
    for (t, ok, bad), (a, b) in zip(HEARD, order):
        opts = [bad, ok] if a == 1 else [ok, bad]
        rows.append(t.format(C(ok, *opts)))
    return EX(id, letter, instr, OL(rows))


def used_to_a(id, letter="A", instr="<span class=\"audio-ic\">♪</span> 12.2 Complete the sentences from <i>Listening</i> on p. 83. "
              "Then listen and check."):
    """p. 84, Grammar A. Ответ — аудиоскрипт 12.2 / ключ."""
    return EX(id, letter, instr,
              f"<p>We {G('used to be')} (be) quite close. We {G('were')} (be) both quite sporty – we {G('would go|’d go|used to go')} "
              f"(go) to the beach a lot, we {G('’d play|would play|used to play')} (play) tennis together and that kind of thing – "
              "but he’s not interested now.</p>")


def used_to_b(id, letter="B", instr="Complete the sentences with ONE word in each space."):
    """p. 84, Grammar B. Ключ: 1 be, was, would, would, got 2 to, was, stayed / camped, go, went, spent 3 used, go, would, got."""
    rows = [f"My brother used to <sup>1</sup>{G('be')} really naughty when he <sup>2</sup>{G('was')} younger. He "
            f"<sup>3</sup>{G('would')} write all over the walls and he <sup>4</sup>{G('would')} never do what my parents told him. "
            f"He sometimes <sup>5</sup>{G('got')} into fights at school too.",
            f"We used <sup>1</sup>{G('to')} go camping a lot when I <sup>2</sup>{G('was')} a kid. We usually "
            f"<sup>3</sup>{G('stayed|camped')} by the beach. We’d <sup>4</sup>{G('go')} swimming every day and do lots of "
            f"sunbathing. One year, we <sup>5</sup>{G('went')} to Slovakia and <sup>6</sup>{G('spent')} a week there, which was great.",
            f"I <sup>1</sup>{G('used')} to go to the gym all the time. I’d <sup>2</sup>{G('go')} every day after work and I "
            f"<sup>3</sup>{G('would')} usually spend two or three hours a day there. Eventually, though, I just "
            f"<sup>4</sup>{G('got')} fed up with it."]
    return EX(id, letter, instr, OL(rows))


NICOLAS = [("They met while travelling round a country.", "3"), ("He / She shared a bad experience with Nicolas.", "1"),
           ("They didn’t like each other to begin with.", "—"), ("He / She fell out with a friend of Nicolas’s.", "5"),
           ("She’s an ex-girlfriend of Nicolas’s.", "2"), ("She’s going out with Nicolas.", "4")]


def nicolas(id, letter="B", instr="<span class=\"audio-ic\">♪</span> 12.3 Now listen and write the number of the speaker against "
            "the correct statement a–f. There is one statement you do not need to use."):
    """p. 85, Listening B. Ключ: a 3 b 1 c – d 5 e 2 f 4."""
    opts = ["1", "2", "3", "4", "5", "—"]
    return EX(id, letter, instr, OL([f"{t} → {S(k, opts)}" for t, k in NICOLAS], "items alpha"))


SYN = [("~ calm, ~ in touch, try and ~ fit, ~ warm ~ friends, ~ in bed all morning, ~ quiet", "stay"),
       ("~ calm, ~ in touch, try and ~ fit, ~ warm, ~ it warm, ~ it cold, ~ trying, ~ getting into trouble, ~ forgetting", "keep"),
       ("~ calm, ~ in control, ~ a serious problem, the economy ~s strong, ~ a big challenge, ~ in power", "remain"),
       ("~ a conversation, ~ a friendship, ~ contact with, ~ good relations", "maintain")]


def synonyms(id, letter="B", instr="Decide which word in <i>italics</i> from exercise A completes each set of collocations 1–4."):
    """p. 85, Vocabulary B. Ключ: 1 stay 2 keep 3 remain 4 maintain."""
    opts = ["keep", "maintain", "remain", "stay"]
    return EX(id, letter, instr, OL([f"{t} → {S(k, opts)}" for t, k in SYN]))


REGRET = [("It’s a shame it took so long to get together.", "I wish it …",
           "I wish it hadn’t taken so long to get together.|I wish it hadn’t taken so long for us to get together.|"
           "I wish we’d got together sooner.|I wish we had got together sooner."),
          ("I didn’t want to be first to apologise. I regret that really.", "I wish I …",
           "I wish I hadn’t wanted to be the first to apologise.|I wish I hadn’t wanted to be first to apologise.|"
           "I wish I hadn’t been so stubborn.|I wish I had apologised first.|I wish I’d apologised first.")]


def regrets(id, letter="", instr="How could you rewrite the following sentences from <i>Listening</i> using <i>wish</i>?"):
    """p. 85, Grammar A 4. Ответы — ключ."""
    return EX(id, letter, instr, OL([f"{a}<br>{b}<br>{G(k, 'wide')}" for a, b, k in REGRET]))


TEXT_WORDS = ["come across", "drift apart", "endlessly", "struggle with", "distant friend", "ego trip", "paranoid", "track down"]
DEFS = [("If something continues for a long time in an unpleasant way, it happens {}.", "endlessly"),
        ("A {} is one you don’t see very often anymore and aren’t close to.", "distant friend"),
        ("If you believe people want to hurt you, even though you don’t have any proof of this, you’re {}.", "paranoid"),
        ("If you find something by accident, you {} it.", "come across"),
        ("If two friends slowly stop being close, they {}.", "drift apart"),
        ("If you manage to {} a person, you find them after a long search in lots of different places.", "track down"),
        ("If you do something just to make yourself feel important – and to show others how important you are – it’s an {}.", "ego trip"),
        ("If you find something very difficult and have to make a big effort to do it, you {} it.", "struggle with")]


def text_defs(id, letter="C", instr="Complete the definitions with these words from the text."):
    """p. 86, Reading C. Ключ: 1 endlessly 2 distant friend 3 paranoid 4 come across 5 drift apart 6 track down 7 ego trip
    8 struggle with."""
    return EX(id, letter, instr, wordbox(TEXT_WORDS) + OL([t.format(G(k)) for t, k in DEFS]))


STORY = [("Eventually, we lost touch completely.", "6"), ("when he suddenly got back in touch again after", "8"),
         ("After we left school,", "3"), ("tracking me down via the Internet.", "9"), ("but we slowly drifted apart.", "5"),
         ("I hadn’t heard from him for ages,", "7"), ("We used to be really close when we were at school.", "1"),
         ("We’d play together all the time and we’d go round to each other’s houses.", "2"), ("we stayed in touch for a while,", "4"),
         ("Since then, we’ve seen each other quite regularly.", "10")]


def friendship(id, letter="A", instr="Put the sentences in the correct order to make a short story about a friendship. The first one is done for you."):
    """p. 87, Speaking A. Ключ: 1 g 2 h 3 c 4 i 5 e 6 a 7 f 8 b 9 d 10 j."""
    nums = [str(i) for i in range(1, 11)]
    rows = [f"{t} → " + ("<b>1</b>" if k == "1" else S(k, nums)) for t, k in STORY]
    return EX(id, letter, instr, OL(rows, "items alpha"))
