"""Страница «Письмо» модуля 04: своего урока письма у юнита нет, поэтому здесь Review 01, часть 2 — Check what you know,
pp. 34–35 (проверочная по юнитам 1–4). Ключи — 01 Review (keys, с. 6–7); аудиоскрипт R 1.3 — с. 163."""
from lib import G, S, C, EX, OL, SEC, PAGE_BOX, IMG
from ocrtext import FIX
from writing_map import note
from review import gr, numbered_script, total
from .shared import wordbox

IMG_DIR = "../assets/img/unit04/"
AE = list("abcde")
SP = ["1", "2", "3", "4", "—"]

FIX[163] = FIX.get(163, []) + [(" - ", " – "), ("smile -", "smile –"), ("1 play for", "I play for"), ("l’ve", "I’ve")]


def listening():
    topics = ["People’s habits in different countries", "A free-time activity", "A language they speak", "Future plans",
              "A holiday"]
    feel = ["a bit confused and sometimes embarrassed", "fed up and disappointed", "relaxed", "shocked at something",
            "pleased with themselves"]
    a = EX("r34-la", "A", '<span class="audio-ic">♪</span> R 1.3 Listen to four people describing how they feel about '
           "different things. Decide what each speaker is talking about. There is one extra topic below that you do not need.",
           OL([f"{S(k, SP)} {t}" for t, k in zip(topics, ["2", "3", "4", "—", "1"])], "items alpha") +
           '<p class="note-s">Выберите номер говорящего; «—» — лишняя тема.</p>')
    b = EX("r34-lb", "B", "Listen again and decide how they feel – or felt. There is one extra feeling below that you do not "
           "need.", OL([f"{S(k, SP)} {t}" for t, k in zip(feel, ["2", "3", "1", "—", "4"])], "items alpha"))
    scr = numbered_script("R 1.3", [(163, (40, 860, 400, 1060)), (163, (400, 60, 794, 290))], "163")
    return SEC("Listening", "", a + b + scr + total(8))


def grammar():
    g = lambda n, a: f"<sup>{n}</sup>{G(a)}"
    d = [("A", "I need to lose some weight."),
         ("B", f"Really? You don’t {g(1, 'look')} very fat."),
         ("A", f"I’ve put on 6 kilos {g(2, 'since')} March."),
         ("B", f"Really? {g(3, 'Do')} you do much exercise?"),
         ("A", f"Not as much as I {g(4, 'used')} to. I {g(5, 'started')} running every day when I was at university, but "
               f"since I started work, I’ve {g(6, 'been')} going less and less and then in March I {g(7, 'had')} an accident, "
               "so I more or less stopped completely."),
         ("B", f"Oh dear. What {g(8, 'happened')}?"),
         ("A", f"Well, I went running near my house and it was already dark as I’d {g(9, 'got|arrived')} back from work late. "
               f"Anyway, I was {g(10, 'running')} along a narrow street and suddenly I slipped and {g(11, 'fell')} backwards. "
               f"I looked back and someone {g(12, 'had')} dropped a banana skin on the floor."),
         ("B", "You’re joking!"),
         ("A", "No, honestly. Anyway. It was really painful and I can’t run at the moment."),
         ("B", f"Why don’t you go swimming? I {g(13, 'go')} once or twice a week."),
         ("A", f"Maybe. I’m not very good {g(14, 'at')} swimming."),
         ("B", f"Well, I don’t go very fast. What {g(15, 'are')} you doing tomorrow? I’m {g(16, 'going')} to my local pool in "
               "the evening. You could come with me."),
         ("A", f"I’ve got {g(17, 'to')} work late tomorrow, but maybe some other time."),
         ("B", f"Well, I {g(18, 'will|’ll')} probably go on Saturday as well."),
         ("A", f"I need to check my diary, but that {g(19, 'might|could|may')} be better. I’ll "
               f"{g(20, 'call|ring|text|email|phone|contact')} you later to confirm. It’d be nice to go with someone.")]
    body = '<div class="dlg">' + "".join(f"<b>{s}:</b><span>{t}</span>" for s, t in d) + "</div>"
    return SEC("Grammar", "", EX("r34-gr", "", "Complete the conversation with one word in each gap.", body) + total(20))


def present_perfect():
    rows = [("A: Have you been to the old town yet?", f"B: Yeah, we {G('walked round')} there last night. It’s lovely.",
             "walk round"),
            ("A: Have you seen Ricardo today?", f"B: No, but I {G('’m meeting|am meeting')} him for lunch later.", "meet"),
            ("A: Have you decided what you’re doing this weekend?",
             f"B: Not really. I {G('’ll probably stay|will probably stay')} at home. I’m exhausted.", "probably stay"),
            ("A: Have you been to Mexico before?", f"B: Yeah, I {G('’ve been|have been')} a few times on business.", "be"),
            ("A: Have you heard that new song by <i>The Love Machine</i>?",
             f"B: No, but it {G('’s supposed to be|is supposed to be')} quite catchy.", "be")]
    return SEC("Present perfect questions and answers", "",
               EX("r34-pp", "", "Complete the answers to the present perfect questions with the correct form of the verbs in "
                  "brackets.", OL([f"{q}<br>{a} <small>({v})</small>" for q, a, v in rows])) + total(5) + gr(140))


def adjectives():
    rows = [f"I was a bit {C('disappointed', 'disappointed', 'disappointing')} when I saw the castle in real life. I expected "
            "it to be bigger.",
            f"We went on this really {C('scary', 'scary', 'scared')} ride at a theme park. My dad was "
            f"{C('terrified', 'terrifying', 'terrified')}.",
            f"There’s a really {C('fascinating', 'fascinating', 'fascinated')} museum there about the history of farming.",
            f"I saw this new Russian film at the weekend. It was great – really {C('moving', 'moved', 'moving')}.",
            f"My friend said the play was really {C('depressing', 'depressing', 'depressed')}, but I thought the ending was "
            f"quite {C('uplifting', 'uplifting', 'uplifted')}."]
    return SEC("<i>-ing / -ed</i> adjectives", "",
               EX("r34-ad", "", "Choose the correct form.", OL(rows)) + total(7) + gr(138) +
               IMG(IMG_DIR + "p34-ride.jpg", "Theme park ride", cls="md"))


def conversations():
    q = ["I’ve locked myself out of the house.", "To be honest, I’m not a big sports fan.", "He’s really into windsurfing.",
         "I’m thinking of eating out. Can you recommend anywhere?", "Are you any good at tennis?",
         "What kind of music are you into?", "My husband used to teach English.", "I’ve just heard I got a place at university."]
    r = ["Oh well, in that case, how about going to a museum instead?", "All sorts.", "Really? How long did he do that for?",
         "No, I’m useless, but I still enjoy playing.", "Congratulations! Are you doing anything to celebrate?",
         "Oh no, what a pain! How are you going to get in?", "How long has he been doing that?",
         "Well, you could try that place round the corner."]
    key = "f a g h d b c e".split()
    return SEC("Developing conversations", "",
               EX("r35-dc", "", "Match 1–8 to the responses a–h.",
                  OL([f"{t} … {S(k, list('abcdefgh'))}" for t, k in zip(q, key)]) + OL(r, "items alpha")) + total(8))


def collocations():
    verbs = ["restore", "reach", "go", "borrow", "pour", "spoil", "hit", "miss", "wonder", "get into"]
    nouns = ["my connecting flight", "some trainers to play tennis", "the holiday", "if you want to go out", "an old church",
             "in a straight line", "45 degrees in the shade", "the museum free", "the ball into the net", "with rain"]
    key = "e g f b j c i a d h".split()
    return SEC("Collocations", "",
               EX("r35-co", "", "Match the verbs with the words they go with.",
                  OL([f"{v} … {S(k, list('abcdefghij'))}" for v, k in zip(verbs, key)]) + OL(nouns, "items alpha")) +
               total(10))


def forming():
    rows = [("There’s plenty of cheap {} available in the town, if you want to stay.", "ACCOMMODATE", "accommodation"),
            ("We got a very good {} from the advert.", "RESPOND", "response"),
            ("It looks like the company is going to make a big {} this year.", "LOSE", "loss"),
            ("I just can’t deal with the {} at all.", "HOT", "heat"),
            ("I didn’t use my full holiday {}.", "ENTITLE", "entitlement")]
    return SEC("Forming words", "",
               EX("r35-fw", "", "Complete the sentences with the noun forms of the words in CAPITALS.",
                  OL([t.format(G(a)) + f" <small>{w}</small>" for t, w, a in rows])) + total(5) +
               '<p class="help">▶ Find this difficult? Look for other words in the same word family when you learn a new '
               "word.</p>")


def patterns():
    rows = [("How much did that cost, if you don’t mind me to ask?", "How much did that cost, if you don’t mind me asking?"),
            ("I’d rather not to sit in the front row, if you don’t mind.", "I’d rather not sit in the front row, if you don’t mind."),
            ("We didn’t expect to have so difficulty finding a place.",
             "We didn’t expect to have such difficulty finding a place.|We didn’t expect to have so much difficulty finding a "
             "place.|We didn’t expect to have such difficulty finding the place.|We didn’t expect to have so much difficulty "
             "finding the place."),
            ("I only brought a T-shirt as I expected that it be warmer.",
             "I only brought a T-shirt as I expected that it would be warmer.|I only brought a T-shirt as I expected it would "
             "be warmer.|I only brought a T-shirt as I expected it to be warmer."),
            ("It depends of my dad whether I can go or not.", "It depends on my dad whether I can go or not.|It depends on my "
                                                              "dad whether I can go out or not."),
            ("It depends how much does it cost.", "It depends how much it costs.|It depends on how much it costs."),
            ("She goes swimming every day – if she’s busy.", "She goes swimming every day – if she isn’t busy.|She goes "
             "swimming every day – unless she’s busy.|She goes swimming every day – if she’s not busy.|She goes swimming "
             "every day if she isn’t busy.|She goes swimming every day unless she’s busy.|She goes swimming every day – "
             "unless she is busy.|She goes swimming every day – if she is not busy."),
            ("I never managed that I won – not even once!", "I never managed to win – not even once!|I never managed to win "
                                                             "not even once!")]
    return SEC("Language patterns", "",
               EX("r35-lp", "", "Correct the mistake in each of the sentences. Write the correct sentence.",
                  OL([f"{s}<br>{G(k, 'wide')}" for s, k in rows])) + total(8))


def vocabulary():
    def g(n, opts, a):
        return f"<sup>{n}</sup>{S(a, opts)}"
    t1 = (f"Joey Chestnut has {g(1, ['won', 'lost', 'beaten'], 'beaten')} Japanese speed eating legend Takeru Kobayashi to "
          f"win Nathan’s Hot dog Eating Contest in Coney Island. Kobayashi had never "
          f"{g(2, ['lost', 'defended', 'missed'], 'lost')} in America and was "
          f"{g(3, ['attempting', 'pretending', 'wishing'], 'attempting')} to win the competition for the seventh year "
          f"running. Chestnut also {g(4, ['won', 'set', 'gave'], 'set')} a new world record by eating 66 hot dogs in just "
          "12 minutes.")
    t2 = (f"A conference is being held this weekend to {g(5, ['draw attention', 'tell', 'highlight'], 'highlight')} the "
          f"health problems caused by global warming. There’s {g(6, ['evidence', 'fact', 'show'], 'evidence')} that climate "
          f"change has led to {g(7, ['improvements', 'increases', 'more'], 'increases')} in skin cancer and it is also being "
          f"{g(8, ['proved', 'caused', 'linked'], 'linked')} to greater risks of food poisoning and infectious diseases as "
          f"the planet gets hotter. A spokesman for the conference said, ‘We are "
          f"{g(9, ['finding out', 'doing', 'making'], 'making')} progress in understanding these problems, but we need to "
          "do more’.")
    return SEC("Vocabulary", "",
               EX("r35-vo", "", "Complete the short news stories by choosing the correct word.",
                  "".join(f'<div class="story hand"><p>{t}</p></div>' for t in (t1, t2))) + total(9))


def build():
    return note(4) + _build()


def _build():
    p34 = PAGE_BOX(34, '<h2>Check what you know</h2><p class="lead">Проверочная работа по юнитам 1–4: в учебнике за неё '
                       'можно получить до 80 баллов.</p><div class="cols"><div>' + listening() + grammar() +
                   '</div><div>' + present_perfect() + adjectives() + "</div></div>")
    p35 = PAGE_BOX(35, '<div class="cols"><div>' + conversations() + collocations() + forming() + '</div><div>' + patterns() +
                   vocabulary() + "</div></div>")
    return p34 + p35
