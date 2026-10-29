"""Упражнения модуля 5, которые выводятся и в «Учебнике» / «Письме», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, EX, OL, DLG, ORDER, IMG

AH = list("abcdefgh")
IMG_DIR = "../assets/img/unit05/"


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


JOBS_BOX = ["civil servant", "estate agent", "security guard", "plumber", "labourer", "electrician", "engineer", "lawyer",
            "graphic designer", "surgeon", "accountant", "programmer"]
JOB_PHOTOS = [("p36-job1.jpg", "estate agent"), ("p36-job2.jpg", "security guard"), ("p36-job3.jpg", "plumber"),
              ("p36-job4.jpg", "labourer"), ("p37-job5.jpg", "electrician"), ("p37-job6.jpg", "surgeon")]


def photo_grid(items, opts):
    return '<div class="pics">' + "".join(
        f'<figure><img src="{IMG_DIR}{f}" alt="" loading="lazy"><figcaption>{i} {S(k, opts)}</figcaption></figure>'
        for i, (f, k) in enumerate(items, 1)) + "</div>"


def jobs(id, letter="A", instr="Which of the jobs in the box can you see in the photos? Label the photos."):
    """pp. 36–37, Vocabulary A. Ключ: estate agent, security guard, plumber, labourer, electrician, surgeon."""
    return EX(id, letter, instr, wordbox(JOBS_BOX) + photo_grid(JOB_PHOTOS, sorted(JOBS_BOX)))


IVAN = [("I’m involved", ("in", "on"), "in", "designing what you see on the screen."),
        ("How did you", ("getting", "get into"), "get into", "that?"),
        ("Vodafone were recruiting people so I", ("applied", "replied"), "applied", "and I got a job."),
        ("It’s like any job. It has its boring", ("moments", "minutes"), "moments", "."),
        ("It depends if we have a deadline to", ("complete", "meet"), "meet", "."),
        ("I do", ("something", "anything"), "something", "like fifty or sixty hours a week."),
        ("That must be", ("stressed", "stressful"), "stressful", "."),
        ("I sometimes work better", ("under", "in"), "under", "pressure.")]


def ivan(id, letter="B", instr="Decide which words in <i>italics</i> you heard. Then listen again and check."):
    """p. 36, Listening B. Ключ: 1 in 2 get into 3 applied 4 moments 5 meet 6 something 7 stressful 8 under."""
    return EX(id, letter, instr, OL([f"{a} {C(k, *o)}{'' if b == '.' else ' '}{b}" for a, o, k, b in IVAN]))


WP = ["I work in the warehouse.", "I’m in the accounts department.", "I work in human resources.", "I’m in sales.",
      "I’m part of the marketing team."]
WP_END = ["I am mainly involved in planning the campaigns.", "I’m the rep for the whole of the south of Italy.",
          "I am responsible for packing all the orders and doing all the admin for the delivery.",
          "I am responsible for recruitment contracts and working conditions.", "I deal with all the pay and finances."]


def workplaces(id, letter="A", instr="Match 1–5 with the specific job descriptions a–e."):
    """p. 37, Vocabulary A. Ключ: 1 c 2 e 3 d 4 b 5 a."""
    key = "c e d b a".split()
    return EX(id, letter, instr, OL([f"{q} {S(k, AH[:5])}" for q, k in zip(WP, key)]) + OL(WP_END, "items alpha"))


HT = ["have to", "don’t have to", "can"]


def have_to(id, letter="A", instr="Complete the sentences with the correct form of <i>have to, don’t have to</i> or <i>can</i>."):
    """p. 38, Grammar A. Ключ: 1 have to 2 don’t have to 3 can 4 have to 5 can 6 don’t have to 7 have to 8 can 9 have to."""
    s = lambda k: S(k, HT)
    rows = [f"I {s('have to')} wear a stupid uniform. I really hate it!",
            f"It’s just round the corner, so I {s('don’t have to')} travel very far to work.",
            f"I work flexi-time, so I {s('can')} start and finish more or less whenever I want.",
            f"I {s('have to')} speak English over the phone, which can be difficult for me.",
            f"We {s('can')} wear whatever we want in the office.",
            f"I work hard, but at least I {s('don’t have to')} work weekends!",
            f"I sometimes {s('have to')} deal with some really awful people and my boss isn’t very supportive.",
            f"I {s('can')} usually take time off if I need to.",
            f"We always {s('have to')} show our ID cards to get into the building."]
    return EX(id, letter, instr, OL(rows))


PIC_JOBS = ["lifeguard", "optician", "vet", "farmer", "tour guide", "firefighter"]


def pic_jobs(id, letter="C", instr="Work in pairs. Discuss which jobs you can see in the pictures."):
    """p. 38, Grammar C. Ключ: 1 lifeguard 2 optician 3 vet 4 farmer 5 tour guide 6 firefighter."""
    opts = sorted(PIC_JOBS)
    return EX(id, letter, instr, IMG(IMG_DIR + "p38-jobs.jpg", "Jobs 1–6") +
              OL([S(k, opts) for k in PIC_JOBS]))


RULES = ["Women have to wear skirts or dresses at work.", "We have to go outside to smoke.",
         "We have to agree holidays with our boss. We can’t take time off when we want.",
         "We have to ask the admin assistant to make photocopies for us. We can’t just do them ourselves.",
         "We have to take our breaks at set times.", "We have to wear a hard hat at all times.",
         "We can’t surf the web on company computers.", "We can’t call mobile phones from the office.",
         "We can’t talk to each other while we’re working."]


def rules_conv(id, letter="B", instr='<span class="audio-ic">♪</span> 5.3 Listen and decide which of the rules in exercise A '
               "they talk about in each conversation."):
    """p. 39, Listening B. Ключ: 1 – 7, 2 – 1, 3 – 3."""
    nums = [str(i) for i in range(1, 10)]
    return EX(id, letter, instr, OL(RULES) + "<p>" + "<br>".join(f"Conversation {i}: rule {S(k, nums)}"
                                                                   for i, k in ((1, "7"), (2, "1"), (3, "3"))) + "</p>")


COLL = [("send", "personal", "emails"), ("get", "a computer", "virus"), ("infect", "the whole", "system"),
        ("work in", "a law", "firm"), ("have", "a strict", "dress code"), ("wear", "smart", "trousers"),
        ("have", "a quick", "word"), ("perform in", "a school", "concert"), ("ask", "at short", "notice")]


def collocations(id, letter="C", instr="Work in pairs. Match the words used in the conversations. Then listen to check your "
                 "answers."):
    """p. 39, Listening C. Ключ: send personal emails, get a computer virus, infect the whole system, work in a law firm,
    have a strict dress code, wear smart trousers, have a quick word, perform in a school concert, ask at short notice."""
    mid = ["smart", "a law", "a school", "a quick", "the whole", "personal", "at short", "a strict", "a computer"]
    end = ["emails", "virus", "notice", "firm", "dress code", "trousers", "word", "concert", "system"]
    return EX(id, letter, instr, OL([f"<b>{v}</b> {S(m, mid)} {S(e, end)}" for v, m, e in COLL]))


def rules_choose(id, letter="A", instr="Choose the correct form in <i>italics</i>."):
    """p. 39, Grammar A. Ключ: 1 You’re not allowed to 2 I’m supposed to 3 have to; I’m allowed to 4 supposed 5 We are allowed to
    6 shouldn’t really 7 I should really 8 You’re not really supposed to."""
    rows = [f"Sorry, {C('you’re not allowed to', 'you’re not allowed to', 'you don’t have to')} smoke in here. Can you go "
            "outside please?",
            f"{C('I’m supposed to', 'I’m supposed to', 'I don’t have to')} have my ID at all times, but nobody ever asks me for it!",
            f"I {C('have to', 'can’t', 'have to')} start really early some days, but at least "
            f"{C('I’m allowed to', 'I have to', 'I’m allowed to')} go home early.",
            f"You’re {C('supposed', 'supposed', 'allowed')} to dress smartly, but no one’s said anything when I’ve worn jeans.",
            f"{C('We are allowed to', 'We are supposed to', 'We are allowed to')} belong to a trade union, but our manager "
            "doesn’t really like it when we do.",
            f"We {C('shouldn’t really', 'shouldn’t really', 'don’t have to')} come out here on the roof of the building, but it’s "
            "a really nice place to have a break!",
            f"I know {C('I should really', 'I’m allowed to', 'I should really')} turn off my phone before I come in, but I’m "
            "expecting a really important call!",
            f"{C('You’re not really supposed to', 'You can’t', 'You’re not really supposed to')} eat or drink in the classroom, "
            "so please tidy everything up after you finish your coffee."]
    return EX(id, letter, instr, OL(rows))


ART_JOBS = ["Human guinea pigs", "Embalmers", "Call centre workers", "Recycling plant worker"]
PROBLEMS = [("are exposed to chemicals, dust or dirt.", "Recycling plant worker"), ("risk their lives.", "Human guinea pigs"),
            ("risk catching a disease.", "Human guinea pigs|Recycling plant worker"),
            ("work very long hours.", "Embalmers|Call centre workers"), ("do not have much space to work in.", "Call centre workers"),
            ("have to bend over a lot or lift heavy objects.", "Embalmers"), ("get a lot of abuse.", "Call centre workers"),
            ("are standing all day.", "Embalmers")]


def art_jobs(id, letter="C", instr="Read the rest of the article and decide which job in the article involves the problems in "
             "exercise B. Some jobs may match with more than one problem."):
    """p. 40, Reading C. Ключ: Human guinea pigs 2, 3; Embalmers 4, 6, 8; Call centre workers 5, 7 (and possibly 4);
    Recycling plant worker 1, 3. В пунктах 3 и 4 засчитываются оба варианта."""
    return EX(id, letter, instr, "<p><b>Workers who …</b></p>" + OL([f"{q} {S(k, ART_JOBS)}" for q, k in PROBLEMS]))


def art_words(id, letter="E", instr="Without looking at the text, complete the sentences."):
    """p. 41, Reading E. Ключ: 1 get 2 cramped 3 way 4 slammed 5 grateful 6 wage 7 effects 8 average."""
    rows = [f"I’m lucky, because I {G('get')} on really well with my colleagues.",
            f"There are six people living in a two-bedroom flat, so they have to put up with very {G('cramped')} conditions.",
            f"It’s a quick and easy {G('way')} of sending large video files.",
            f"Honestly, I was getting so angry I couldn’t continue talking to him, so I just {G('slammed')} down the phone.",
            f"Thank you so much. I’m very {G('grateful')} for all your help.",
            f"The boss is so mean! He basically just pays the minimum {G('wage')}. That’s it!",
            f"The drug was taken off the market after serious side {G('effects')} were reported.",
            f"Unemployment in the city is 25% – well above the national {G('average')}."]
    return EX(id, letter, instr, OL(rows))


USED = [(("It must be difficult getting up so early.", "Oh, {}. I had to get up at five in my last job."),
         "to I’m it used", "I’m used to it"),
        (("How are you finding the new job? It must be hard having to do everything in English.",
          "It is difficult, but {}. The people I work with are being very supportive."),
         "getting slowly to it I’m used", "I’m slowly getting used to it|I’m getting used to it slowly"),
        (("How are you finding your new job?",
          "Not that good, to be honest. I hate sitting at a desk all day, but I need the money, so I guess {}."),
         "to I’ll get used to just have it", "I’ll just have to get used to it"),
        (("How do you find working shifts?", "OK, although it {} working nights. I couldn’t sleep during the day to begin with, "
                                            "but it’s fine now."),
         "get to me a while used took to", "took me a while to get used to"),
        (("How do you find working nights? It must be quite difficult.", "It was to begin with, yeah, but {}."),
         "it totally now I’m to used", "I’m totally used to it now"),
        (("How are you finding your new job?", "The job’s OK, but I hate the journey to work. {} the crowded trains! I’m "
                                              "actually thinking of leaving."),
         "I’ll think don’t ever I used to get", "I don’t think I’ll ever get used to")]


def used_to(id, letter="B", instr="Complete the dialogues by putting the words in brackets in the correct order."):
    """p. 41, Vocabulary B. Ключ: 1 I’m used to it 2 I’m slowly getting used to it 3 I’ll just have to get used to it
    4 took me a while to get used to it 5 I’m totally used to it now 6 I don’t think I’ll ever get used to."""
    rows = []
    for (a, b), words, ans in USED:
        rows.append(DLG(("A", a), ("B", b.format("……"))) + f"<i>({' / '.join(words.split())})</i>" + ORDER(words, ans))
    return EX(id, letter, instr + ' <span style="font-weight:400">Нажимайте на слова по порядку; повторное нажатие возвращает '
              "слово.</span>", OL(rows))


# ---- Writing 05 (pp. 128–129) ----
PROG_BOX = ["include", "swap", "full", "exciting", "last-minute"]


def programme(id, letter="", instr="Complete the sentences with other collocations with <i>programme</i>."):
    """p. 129, Vocabulary. Ключ: 1 last-minute 2 swap 3 full 4 exciting 5 include."""
    rows = [f"There’s been a {G('last-minute')} change to the programme.",
            f"We could {G('swap')} some things round in the programme.",
            f"It is a very {G('full')} programme. Could we drop something and make room for some more free time?",
            f"It looks like a very {G('exciting')} programme of events.",
            f"In the end, we can’t {G('include')} everything in the programme."]
    return EX(id, letter, instr, wordbox(PROG_BOX) + OL(rows))


def hab_rules(id, letter="A", instr="Look in the letter and find examples of the words. Then complete the rules 1–2."):
    """p. 129, Keywords for writing A. Ключ: 1 Although, but; Although 2 However."""
    return EX(id, letter, instr, OL([
        f"{G('Although|although')} and {G('but')} connect two parts of the same sentence. {G('Although|although')} usually "
        "starts the sentence, but can come in the middle.",
        f"{G('However|however')} always connects to an idea in a previous sentence. It usually starts the second sentence, but "
        "it can come in the middle or at the end of the second sentence."]))


def hab_complete(id, letter="B", instr="Complete the sentences."):
    """p. 129, Keywords for writing B. Ключ: 1 Although 2 However 3 but / although 4 Although 5 however."""
    rows = [f"{G('Although')} it would be nice to visit the museum, we don’t have enough time.",
            f"It’s a very full programme. {G('However')}, there is space for one more visit on Monday afternoon.",
            f"We would really like to go to the exhibition, {G('but|although')} we were wondering if we could go on Tuesday "
            "instead of Sunday.",
            f"Thanks again for your help. {G('Although')} we realise these last minute changes are inconvenient, we are sure they "
            "will improve the programme.",
            f"On the whole, everything seems to be very clear. I do have couple of queries, {G('however')}."]
    return EX(id, letter, instr, OL(rows))
