"""Страница «Письмо» модуля 16: своего урока письма у юнита нет, поэтому здесь Review 04, часть 2 —
Check what you know, pp. 118–119 (проверочная по юнитам 13–16). Ключи — 04 Review; аудиоскрипт R 4.2 — с. 175."""
from lib import G, S, C, EX, OL, SEC, PAGE_BOX, REVEAL, SCRIPT, HELP
from ocrtext import lines, fixed, _fix, FIX
from . import shared as X

FIX[175] = FIX.get(175, []) + [("l’ve", "I’ve"), ("lused", "I used"), ("| try", "I try"), ("too confused", "too confused.")]
JOBS = ["computer programmer", "engineer", "flight attendant", "teacher", "businessman", "pilot", "writer", "doctor", "surgeon",
        "bus driver"]


def SR42():
    items = []
    for l in lines(175, (400, 80, 794, 600)):
        t = fixed(175, _fix(l["t"])).strip()
        if t.startswith("R 4.2") or t.startswith("OR 4.2") or t == "AUDIOSCRIPT":
            continue
        n, _, rest = t.partition(" ")
        if n.isdigit():
            items.append([f"Speaker {n}", rest])
        elif items:
            items[-1][1] += " " + t
    return SCRIPT("R 4.2", "", [tuple(i) for i in items], "175")


def listening():
    # ключ A: 1 pilot 2 doctor 3 engineer 4 computer programmer 5 businessman; по аудиоскрипту 3 — автор инструкций (writer),
    # 4 — преподаватель (teacher): эти варианты тоже засчитываются.
    keys = ["pilot", "doctor", "engineer|writer", "computer programmer|teacher", "businessman"]
    a = EX("r118-la", "A", '<span class="audio-ic">♪</span> R 4.2 Listen. Which of the things in the box does each person do?',
           X.wordbox(JOBS) + OL([f"Speaker {i}: {S(k, sorted(JOBS))}" for i, k in enumerate(keys, 1)], "items plain") +
           '<p class="note-s">В ключах: 1 pilot 2 doctor 3 engineer 4 computer programmer 5 businessman (по тексту записи '
           'для 3 и 4 подходят также writer и teacher).</p>')
    b = EX("r118-lb", "B", "Listen again and decide which speaker:", OL([
        f"has to deal with a lot of paperwork. {S('2', list('12345'))}", f"lost their job. {S('5', list('12345'))}",
        f"thinks technology has made things safer. {S('1', list('12345'))}", f"is setting up a website. {S('4', list('12345'))}",
        f"worries about being clear. {S('3', list('12345'))}"], "items alpha"))
    return SEC("Listening", "", '<p class="intro">You are going to hear five people talking about things connected with '
                                'technology.</p>' + a + b + SR42())


def conditionals():
    rows = [f"We wouldn’t have got lost if I’d {G('been')} driving.",
            f"If I’d known my ex-boyfriend was going to be here, I {G('wouldn’t')} have come to this party!",
            f"If you’d been more careful, it wouldn’t {G('have')} happened!",
            f"I don’t regret moving here. If I {G('hadn’t')}, who knows what might have happened to me?",
            f"If you {G('had')} told me earlier, I could have helped you.",
            f"Without her help, I would never have had enough money to buy a flat. I {G('would')} probably still be living at "
            "home!"]
    return SEC("Grammar", "Conditionals",
               EX("r118-gc", "", "Complete the sentences with one word in each gap. Contractions such as <i>didn’t, can’t</i>, "
                  "etc. count as one word.", OL(rows)) + HELP(152))


def regrets():
    rows = [f"It’s your birthday? You {G('should’ve told|should have told')} me.",
            f"She was really upset afterwards! I {G('shouldn’t have said|should not have said')} anything about her haircut!",
            f"My parents were furious when they saw the photos! I knew I {G('shouldn’t have posted|should not have posted')} "
            "them on the Web!",
            f"They’re completely full! We {G('should’ve booked|should have booked')} in advance.",
            f"I feel really sick. I {G('shouldn’t have eaten|should not have eaten')} so much earlier.",
            f"He’s so lazy! I saw him chatting on the phone earlier – when he "
            f"{G('should’ve been working|should have been working')}."]
    return SEC("Expressing regrets", "",
               EX("r118-er", "", "Complete the sentences using <i>should’ve / shouldn’t have</i> and the correct form of the "
                  "verbs in the box.", X.wordbox(["book", "eat", "post", "say", "tell", "work"]) + OL(rows)) + HELP(152))


def ing_to():
    rows = [("I’m really glad I gave up {}.", "smoking", ("smoking", "to smoke")),
            ("We’re hoping {} into a bigger place.", "to move", ("moving", "to move")),
            ("I tried to explain, but he refused {}.", "to listen", ("listening", "to listen")),
            ("I look forward to {} from you soon.", "hearing", ("hear", "hearing")),
            ("The government promised {} taxes if they were re-elected, but they haven’t done it yet!", "to cut",
             ("to cut", "cutting")),
            ("I seem to spend my whole life {}!", "working", ("to work", "working")),
            ("I was caught {} in an exam!", "cheating", ("cheating", "to cheat")),
            ("Research has failed {} any link between mobile phones and memory loss.", "to find", ("finding", "to find"))]
    return SEC("<i>-ing</i> forms and <i>to</i>-infinitives", "",
               EX("r118-it", "", "Choose the correct form.", OL([t.format(C(a, *o)) for t, a, o in rows])) + HELP(153))


def relatives():
    rows = [("He’s someone who music was ahead of its time.", "He’s someone whose music was ahead of its time."),
            ("Yalta is which they held a big meeting after the war.", "Yalta is where they held a big meeting after the war."),
            ("She was a nurse which set up her own hospital.", "She was a nurse who set up her own hospital.|"
                                                               "She was a nurse that set up her own hospital."),
            ("She was an activist campaigned for women’s rights.", "She was an activist campaigning for women’s rights.|"
                                                                  "She was an activist who campaigned for women’s rights."),
            ("The story was written around 500BC, during the time which Persia and Greece were at war.",
             "The story was written around 500BC, during the time when Persia and Greece were at war."),
            ("We started living together – and that’s I realised how different we were!",
             "We started living together – and that’s when I realised how different we were!|"
             "We started living together and that’s when I realised how different we were!|"
             "We started living together – and that’s when I realized how different we were!|"
             "We started living together and that’s when I realized how different we were!"),
            ("That’s the house where my mum used to live in.", "That’s the house where my mum used to live.|"
                                                               "That’s the house my mum used to live in.|"
                                                               "That’s the house that my mum used to live in.")]
    return SEC("Defining relative clauses", "",
               EX("r118-rc", "", "Correct the mistake in each of the sentences. Write the correct sentence.",
                  OL([f"{s}<br>{G(k, 'wide')}" for s, k in rows])) + HELP(155))


def reporting():
    rows = [f"I tried to {G('persuade')} him to go and see a doctor about it, but he didn’t listen!",
            f"I {G('warned')} you not to trust him, but you didn’t listen!",
            f"The doctor {G('recommended')} that I take a week off work.",
            f"After I complained, they {G('offered')} to refund me in full.",
            f"She’s so stubborn. She always {G('insists on')} doing things her own way!",
            f"Now we’ve split up, my ex-boyfriend {G('has threatened|threatened|’s threatened')} to post personal pictures of me "
            "on the web. It’s horrible.",
            f"I’m sure he’s having an affair, but whenever I ask him about it, he just {G('denies')} everything.",
            f"If she really wants to make up, she’ll have to {G('apologise|apologize')} first. She’s the one in the wrong – not me!"]
    return SEC("Reporting verbs", "",
               EX("r119-rv", "", "Complete the sentences with the correct form of the verbs in the box.",
                  X.wordbox(["apologise", "deny", "threaten", "insist on", "offer", "persuade", "recommend", "warn"]) + OL(rows))
               + HELP(154))


def forming():
    rows = [("He was {} president last year.", "ELECTION", "elected"), ("My son has developed an {} to eggs.", "ALLERGIC", "allergy"),
            ("He’s got a rare skin disease. It doesn’t hurt or itch, but it is {}.", "CURE", "incurable"),
            ("It’s an amazing gadget – and it made its {} a millionaire.", "CREATE", "creator"),
            ("Have you checked the {}? Maybe it’s not plugged in properly.", "CONNECT", "connection"),
            ("I got terrible food {} while I was backpacking.", "POISONOUS", "poisoning"),
            ("I chose this car because it’s more {} friendly than my old one.", "ENVIRONMENT", "environmentally"),
            ("He lost his first big boxing match, but he’s still only young and he showed real {}.", "BRAVE", "bravery"),
            ("Bird Flu is incredibly {} – but only for birds!", "INFECTION", "infectious"),
            ("Thank you so much for all your {}.", "GENEROUS", "generosity")]
    return SEC("Forming words", "",
               EX("r119-fw", "", "Complete the sentences with the correct forms of the words in CAPITALS.",
                  OL([t.format(G(a)) + f" <small>{w}</small>" for t, w, a in rows])))


def collocations():
    verbs = ["develop", "feel", "stamp", "bribe", "restart", "fall off", "save", "survive", "go on", "plant"]
    nouns = ["the computer", "a day trip", "a horse", "a vaccine", "your passport", "trees", "the crash", "the officials",
             "someone’s life", "sick"]
    key = "d j e h a c i g b f".split()
    return SEC("Collocations", "",
               EX("r119-co", "", "Match the verbs with the words they go with.",
                  OL([f"{v} … {S(k, list('abcdefghij'))}" for v, k in zip(verbs, key)]) + OL(nouns, "items alpha")))


def vocabulary():
    g = lambda n, hint, a: f"<sup>{n}</sup><i>{hint}…</i> {G(a)}"
    t1 = (f"We had an awful journey. We {g(1, 'm', 'missed')} the first train from the main station because we were waiting on "
          f"the wrong {g(2, 'p', 'platform')}. Then the next train was {g(3, 'de', 'delayed')} for ages! We heard it was "
          f"because of some kind of animal on the {g(4, 'l', 'line')}. Because of that, we ended up missing our flight. We then "
          f"had to spend ages {g(5, 'ha', 'hanging')} around at the airport. Oh, and Lawrence got stopped going through "
          f"{g(6, 'se', 'security')}, which was horrible as well.")
    t2 = (f"After growing {g(7, 'st', 'strong|strongly|steadily')} for several years, the market for hi-tech gadgets is now in "
          f"{g(8, 'de', 'decline')}. However, the latest mobile from Korea will surely change all that and will have people "
          f"rushing to {g(9, 'up', 'upgrade')} their phones. The G999 is greener and more {g(10, 'en', 'energy')}-efficient, "
          f"but still very {g(11, 'str', 'straightforward')} and easy to use. Plus, it has a very cool design.")
    t3 = (f"Patient complains that she has been feeling {g(12, 'di', 'dizzy')} lately and has also been getting terrible "
          f"{g(13, 'mig', 'migraines')}. Seems to be {g(14, 'u', 'under')} a lot of stress at work. Also suffers from high "
          f"blood {g(15, 'p', 'pressure')}.")
    return SEC("Vocabulary", "",
               EX("r119-vo", "", "Complete the texts by choosing the correct words.",
                  "".join(f'<div class="story hand"><p>{t}</p></div>' for t in (t1, t2, t3))))


from writing_map import note as _wnote


def build():
    return _wnote(int("16")) + _build()


def _build():
    p118 = PAGE_BOX(118, '<h2>Check what you know</h2><p class="lead">Проверочная работа по юнитам 13–16: в учебнике за неё '
                         'можно получить до 80 баллов.</p><div class="cols"><div>' + listening() + conditionals() +
                    '</div><div>' + regrets() + ing_to() + relatives() + "</div></div>")
    p119 = PAGE_BOX(119, '<div class="cols"><div>' + reporting() + forming() + '</div><div>' + collocations() + vocabulary() +
                    "</div></div>")
    return p118 + p119
