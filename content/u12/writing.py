"""Страница «Письмо» модуля 12. Отдельного урока письма у юнита нет (к юнитам 9–12 относятся Writing 05–06, с. 128–131),
поэтому здесь — письменные задания из уроков юнита 12, а после них Review 03, часть 2 — Check what you know, pp. 90–91
(проверочная по юнитам 9–12). Ключи — 03 Review (keys, с. 19); аудиоскрипт R 3.2 — с. 171."""
from lib import G, S, C, EX, OL, SEC, PAGE_BOX, IMG
from ocrtext import FIX
from review import gr, numbered_script, total
from .shared import wordbox

IMG_DIR = "../assets/img/unit12/"


def writer(id, target, ph, rows=8):
    return (f'<div class="writer" data-target="{target}" data-id="{id}"><textarea rows="{rows}" placeholder="{ph}"></textarea>'
            '<div class="cnt"></div></div>')


from writing_map import note as _wnote


def build():
    return _wnote(int("12")) + _build() + review()


def _build():
    intro = ('<p class="note-s">В учебнике у юнита 12 нет отдельного урока письма: к блоку юнитов 9–12 относятся уроки '
             '<i>Writing 05 Suggesting changes</i> и <i>Writing 06 Reports</i> (с. 128–131). Здесь собраны письменные задания '
             'из уроков юнита 12.</p>')
    a = SEC("Describing character", "pp. 82–83",
            EX("w12-a", "1", "Describe two people in your family or two friends. Use adjectives from <i>Describing character</i> "
               "(<i>bright, outgoing, easy-going, stubborn, chatty …</i>) and the pattern <i>He’s very …, but he can be quite … "
               "sometimes.</i> Write 80–120 words.", writer("u12-w-char", "80–120", "My cousin is very …")))
    b = SEC("Used to and would", "p. 84",
            EX("w12-b", "2", "Write about one of these: someone you know whose character has changed; your memories of a "
               "grandparent; your memories of summer holidays with family; a free-time activity you no longer do. Start with "
               "<i>used to</i> and give details with <i>would</i> or the past simple. Write 100–150 words.",
               writer("u12-w-usedto", "100–150", "When I was a kid, we used to …")))
    c = SEC("Expressing regrets", "p. 85",
            EX("w12-c", "3", "Write three sentences about things you wish you <i>had / had not done</i>. Explain what actually "
               "happened.", writer("u12-w-wish", "", "I wish I’d …", 6)))
    d = SEC("Opinion: friendships online", "pp. 86–87",
            EX("w12-d", "4", "Do you agree with the writer of <i>Give me my space</i>? Write your own opinion (120–180 words) "
               "about social networking sites and staying in touch with old friends. Use <i>If you ask me, …</i>",
               writer("u12-w-opinion", "120–180", "If you ask me, …")))
    return intro + PAGE_BOX("82–87", IMG(IMG_DIR + "p83-family.jpg", "", cls="md") + a + b + c + d)


# ---------------- Review 03, часть 2 (pp. 90–91) ----------------
FIX[171] = FIX.get(171, []) + [("5 R3.2", "R3.2"), ("In the end, | left", "In the end, I left"),
                               ("from the end", "from the end."),
                               ("all sorts - snakes", "all sorts – snakes")]
AE = list("abcde")
SP = ["1", "2", "3", "4", "—"]


def listening():
    topics = ["A night out at the theatre", "A trip to the zoo", "A family pet", "A film they went to see", "An adventure holiday"]
    sent = ["It has caused a few problems.", "It was better than the speaker was expecting.", "It was a very rewarding experience.",
            "There was a big argument.", "It wasn’t as good as the speaker was expecting."]
    a = EX("r90-la", "A", '<span class="audio-ic">♪</span> R 3.2 Listen to four people talking and decide what each person is '
           "talking about. There is one extra topic below that you do not need.",
           OL([f"{S(k, SP)} {t}" for t, k in zip(topics, ["2", "—", "3", "1", "4"])], "items alpha") +
           '<p class="note-s">Выберите номер говорящего; «—» — лишняя тема.</p>')
    b = EX("r90-lb", "B", "Listen again and decide which extract the sentences describe. There is one extra sentence that you "
           "do not need.", OL([f"{S(k, SP)} {t}" for t, k in zip(sent, ["3", "1", "4", "—", "2"])], "items alpha"))
    scr = numbered_script("R 3.2", [(171, (40, 890, 400, 1070)), (171, (400, 60, 794, 305))], "171")
    return SEC("Listening", "", a + b + scr + total(8))


def grammar():
    rows = [f"I watched <i>Star Wars</i> again the other day, for the first time in ages. It was great – just "
            f"{G('as good as')} it was the last time I saw it.",
            f"The town is still fairly quiet in the evenings, but it’s not {G('as dead as')} it used to be. At least there’s a "
            "bit of nightlife now.",
            f"The online market is growing at an incredibly fast rate. It’s getting {G('bigger')} and {G('bigger')} every day.",
            f"Property in the city is much {G('more expensive')} than it was a few years ago. Prices have gone up a lot.",
            f"Crime is much {G('worse')} than it used to be. I don’t feel safe on the streets anymore.",
            f"They’ve dealt with the problem really well, and so the rivers are much {G('less polluted')} than they used to be, "
            "which is great.",
            f"In the 1970s, Lombok wasn’t nearly {G('as touristy as')} it is now. I sometimes felt like I was the only foreigner "
            "on the island.",
            f"They built a road around the city last year and since then it’s nowhere near {G('as noisy')} as it used to be."]
    return SEC("Grammar", "Comparing the past with now",
               EX("r90-gr", "", "Complete each sentence by adding the adjectives in the box in the correct form.",
                  wordbox(["touristy", "expensive", "good", "bad", "big", "polluted", "dead", "noisy"]) + OL(rows)) +
               total(8) + gr(148))


def regrets():
    rows = [("My grandfather died before I was born, so I never had the chance to meet him.",
             f"I wish {G('I had known|I had met|I’d known|I’d met')} my grandfather."),
            ("She got really upset when I told her how I felt.", f"I wish I {G('hadn’t told|had not told')} her how I felt."),
            ("It’s my own fault I’m in this class. I didn’t study that much at school.",
             f"I sometimes wish {G('I had studied|I’d studied')} harder when I was at school."),
            ("I really regret not asking her out for a drink.", f"I wish {G('I had asked|I’d asked')} her out for a drink."),
            ("It’s a shame we didn’t have time to visit you when we were in Milan.",
             f"I wish we {G('had had|’d had')} time to visit you when we were in Milan.")]
    return SEC("Expressing regrets", "",
               EX("r90-er", "", "Complete the second sentences so that they mean the same as the first ones.",
                  OL([f"{a}<br>{b}" for a, b in rows])) + total(5) + gr(151))


def prepositions():
    rows = [("The crime rate has fallen quite a lot {} the past few years.", "over", "over", "from"),
            ("Banks are now offering more mortgages {} lower rates.", "at", "on", "at"),
            ("They’re building a new shopping mall {} the outskirts of town.", "on", "on", "in"),
            ("It’s the second turning {} the left.", "on", "from", "on"),
            ("I just saw a deer running {} the road.", "across", "across", "through"),
            ("We could hear wolves {} the distance.", "in", "in", "at"),
            ("They live {} the eighth floor, I think.", "on", "in", "on"),
            ("She was rushed {} hospital late last night.", "to", "in", "to"),
            ("The group is a serious threat {} the government.", "to", "for", "to"),
            ("What’s your sister like? Is she similar {} you?", "to", "to", "with")]
    return SEC("Prepositions", "",
               EX("r90-pr", "", "Choose the correct preposition.", OL([t.format(C(a, *o)) for t, a, *o in rows])) + total(10))


def patterns():
    rows = [("It still needs to discuss more at the next meeting.",
             "It still needs discussing more at the next meeting.|It still needs to be discussed more at the next meeting."),
            ("The whole place is need a good clean.", "The whole place needs a good clean."),
            ("It’s one of the bad films I’ve ever seen in my life.", "It’s one of the worst films I’ve ever seen in my life."),
            ("It’s the nicest thing nobody’s ever done for me.",
             "It’s the nicest thing anybody’s ever done for me.|It’s the nicest thing anybody has ever done for me.|"
             "It’s the nicest thing anyone’s ever done for me.|It’s the nicest thing anyone has ever done for me.|"
             "It’s the nicest thing somebody’s ever done for me.|It’s the nicest thing somebody has ever done for me.|"
             "It’s the nicest thing someone’s ever done for me.|It’s the nicest thing someone has ever done for me."),
            ("Suzhou is sometimes known the Venice of the East.", "Suzhou is sometimes known as the Venice of the East."),
            ("She’s nice, but she can quite intense sometimes.", "She’s nice, but she can be quite intense sometimes."),
            ("You can be so idiot sometimes!", "You can be such an idiot sometimes!|You can be so much of an idiot sometimes!")]
    return SEC("Language patterns", "",
               EX("r90-lp", "", "Correct the mistake in each of the sentences. Write the correct sentence.",
                  OL([f"{s}<br>{G(k, 'wide')}" for s, k in rows])) + total(7))


def passives():
    rows = [("Police fear that drugs and guns are still been smuggled across the border.",
             "Police fear that drugs and guns are still being smuggled across the border."),
            ("I’m afraid my flight has delay, so don’t wait for me. Go home and I’ll get a taxi to the hotel.",
             "I’m afraid my flight has been delayed, so don’t wait for me. Go home and I’ll get a taxi to the hotel.|"
             "I’m afraid my flight’s been delayed, so don’t wait for me. Go home and I’ll get a taxi to the hotel.|"
             "I’m afraid my flight is delayed, so don’t wait for me. Go home and I’ll get a taxi to the hotel.|"
             "I’m afraid my flight’s delayed, so don’t wait for me. Go home and I’ll get a taxi to the hotel."),
            ("I just worry that all sorts of private details could be post online.",
             "I just worry that all sorts of private details could be posted online."),
            ("The mosque build in the twelfth century.",
             "The mosque was built in the twelfth century.|The mosque was built in the 12th century."),
            ("I had a horrible feeling I was following, so I started to run.",
             "I had a horrible feeling I was being followed, so I started to run.|"
             "I had a horrible feeling that I was being followed, so I started to run."),
            ("Some of the most beautiful parts of the country are slowly being destroyed from global warming.",
             "Some of the most beautiful parts of the country are slowly being destroyed by global warming.")]
    return SEC("Passives", "",
               EX("r91-pa", "", "Correct the mistake in each of the sentences. Write the correct sentence.",
                  OL([f"{s}<br>{G(k, 'wide')}" for s, k in rows])) + total(6) + gr(150))


def conversations():
    rows = [f"Their garden’s huge. It’s about twice the {G('size')} of mine!",
            f"Would it be {G('possible')} to move the appointment to a later date?",
            f"Would you {G('mind')} if I invited friends over?",
            f"You can come back late if you want to – as {G('long')} as you don’t make too much noise.",
            f"Where are you? I’m waiting outside the college. I’m right in {G('front')} of the main entrance.",
            f"A: Do you fancy going rollerblading later?<br>B: No, thanks. I’m not really in the {G('mood')} for that sort of "
            "thing.",
            f"A: Are your grandparents still {G('alive')}?<br>B: Three of them are, yes, but one died last year."]
    return SEC("Developing conversations", "",
               EX("r91-dc", "", "Complete the dialogues with one word in each gap.", OL(rows)) + total(7))


def collocations():
    verbs = ["take out", "tighten", "protect", "kill", "go through", "remain", "keep", "put"]
    nouns = ["my appetite", "a phase", "in power", "trying", "my mind at rest", "a mortgage", "the law", "the environment"]
    key = "f g h a b c d e".split()
    return SEC("Collocations", "",
               EX("r91-co", "", "Match the verbs with the words they go with.",
                  OL([f"{v} … {S(k, list('abcdefgh'))}" for v, k in zip(verbs, key)]) + OL(nouns, "items alpha")) +
               total(8) + '<p class="help">▶ Find this difficult? Re-read units 9–12 in the Vocabulary Builder for more '
                          "information on collocation.</p>")


def forming():
    rows = [("We needed more space, so we decided to build an {}.", "EXTEND", "extension"),
            ("It used to be quite run-down, but there’s been a lot of {} in the area recently.", "INVEST", "investment"),
            ("There’s a {} of affordable housing.", "SHORT", "shortage"),
            ("Many species are currently threatened with {}.", "EXTINCT", "extinction"),
            ("The real problem is that much of the animal’s natural {} has been destroyed.", "INHABIT", "habitat"),
            ("The country gained {} in 1962.", "INDEPENDENT", "independence")]
    return SEC("Forming words", "",
               EX("r91-fw", "", "Complete the sentences with the noun forms of the words in CAPITALS.",
                  OL([t.format(G(a)) + f" <small>{w}</small>" for t, w, a in rows])) + total(6))


def vocabulary():
    g = lambda n, hint, a: f"<sup>{n}</sup><i>{hint}…</i> {G(a)}"
    t1 = (f"Affordable property in central location. Walking {g(1, 'd', 'distance')} from main park and shopping district. "
          f"Has three bedrooms, gas central heating and roof {g(2, 'te', 'terrace')}. Needs a bit of painting and "
          f"{g(3, 'de', 'decorating')}, but is generally in good condition and has real {g(4, 'po', 'potential')} for "
          "improvement.")
    t2 = (f"Nasrul Roesli has been called one of the greatest artists of our time. His work ranges from landscapes and "
          f"{g(5, 'po', 'portraits')} to video installations and {g(6, 'sc', 'sculptures')}. His new "
          f"{g(7, 'ex', 'exhibition')} opened last week at The Yahong {g(8, 'G', 'Gallery')} and is one of the best things I "
          f"have seen in ages. I have never been a great fan, but was very {g(9, 'pl', 'pleasantly')} surprised both by the "
          f"work on display and also by the {g(10, 've', 'venue')} itself.")
    t3 = (f"Let me tell you a bit about myself. I like to think of myself as a fairly easy-going, {g(11, 'r', 'rounded')} "
          f"kind of person. I’m quite sporty, but I don’t see myself as being {g(12, 'co', 'competitive')}. I just play for "
          f"fun. I like meeting new people, and my friends tell me I am quite {g(13, 'ch', 'chatty')} and easy to talk to. I "
          f"work hard and am {g(14, 'de', 'determined')} to do well in my job. However, I realise that sometimes I might come "
          f"across as being fairly {g(15, 'st', 'stubborn')} too because I like doing things my own way.")
    return SEC("Vocabulary", "",
               EX("r91-vo", "", "Complete the words in the three short texts. The first letter(s) are given.",
                  "".join(f'<div class="story hand"><p>{t}</p></div>' for t in (t1, t2, t3))) + total(15))


def review():
    p90 = PAGE_BOX(90, '<h2>Check what you know</h2><p class="lead">Проверочная работа по юнитам 9–12: в учебнике за неё '
                       'можно получить до 80 баллов.</p><div class="cols"><div>' + listening() + grammar() +
                   '</div><div>' + regrets() + prepositions() + patterns() + "</div></div>")
    p91 = PAGE_BOX(91, '<div class="cols"><div>' + passives() + conversations() + collocations() + '</div><div>' + forming() +
                   vocabulary() + "</div></div>")
    return p90 + p91
