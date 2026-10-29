"""Страница «Учебник»: Unit 08 Eating, pp. 54–59 (+ File 3, p. 156). Длинные тексты — из OCR и ключей."""
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import text, fixed, FIX
from keys import rows, numbered
from u07.ocrx import script2, col_paras
from . import shared as X

IMG_DIR = "../assets/img/unit08/"

FIX.setdefault(56, []).extend([(" - ", " – "), ("family. my", "family, my"), ("paying. which", "paying, which"),
                               ("father in-law", "father-in-law")])
FIX.setdefault(57, []).extend([(" - ", " – "), ("morcilla", "<i>morcilla</i>")])
FIX.setdefault(156, []).extend([(" - ", " – ")])
FIX.setdefault(166, []).extend([("Cevichel", "Ceviche!"), (" - ", " – ")])
FIX.setdefault(167, []).extend([(" - ", " – "), ("1 blame", "I blame")])


def person(name, p, boxes, img=""):
    return (f'<div class="story">{img}<h4>{name}</h4>' + "".join(f"<p>{t}</p>" for t in col_paras(p, boxes)) + "</div>")


def article():
    return ('<div class="article">' + IMG(IMG_DIR + "p56-title.jpg", "Food for thought", cls="md") +
            f'<p><i>{fixed(56, text(56, (300, 240, 590, 440)))}</i></p>' +
            '<div class="cols">' + person("Ian (American)", 56, [(545, 575, 794, 1085)], IMG(IMG_DIR + "p56-ducks.jpg", "", cls="sm")) +
            person("Isabella (Spanish)", 57, [(5, 95, 340, 520)], IMG(IMG_DIR + "p57-fishchips.jpg", "", cls="sm")) + "</div></div>")


def group_b():
    return REVEAL('<p class="note-s">File 3, p. 156 — Unit 8 p. 56 Reading, Group B</p><div class="cols">' +
                  person("Ya-Wen (Taiwanese)", 156, [(75, 650, 400, 1010)]) +
                  person("Alan (Scottish)", 156, [(418, 495, 794, 768), (598, 768, 794, 1010)]) + "</div>",
                  "Group B: Ya-Wen and Alan (File 3, p. 156)")


def S81():
    return SCRIPT("8.1", "A = Aurora, C = Claes", script2([(166, (397, 175, 794, 860))], "AC"), "166")


def S82():
    return SCRIPT("8.2", "", script2([(166, (397, 880, 794, 1060)), (167, (0, 70, 397, 805))], "ABCDEFGH"), "166–167")


def S83():
    return SCRIPT("8.3", "", [("Speaker", fixed(167, text(167, (40, 830, 397, 1060))))], "167")


def p54():
    spk = SEC("Speaking", "", EX("b54-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "Can you cook? What is your best dish?", "Who does the cooking in your house?", "What kind of thing do you usually eat?",
        "Are you a fussy eater, an unadventurous eater or an adventurous eater?",
        "Do you prefer to eat out at a restaurant or at home? When you eat at home, what do you like to cook?"])))
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(11, 1, 11, 18, split=62))]), "Ответы (ключ)")
    voc = SEC("Vocabulary", "Describing food", X.cooking("b54-va") +
              REVEAL(" ".join(rows(11, 1, 5, 10, split=62)), "Ключ: что делают повара") +
              EX("b54-vb", "B", "Which food in the picture do you think might be:", OL(["spicy?", "fattening?", "tasty?", "greasy?",
                                                                                      "bland?", "filling?"]) + bkey) +
              EX("b54-vc", "C", "Work in pairs. Look at the pictures in File 9 on p. 158. Do you know anyone who cannot – or does "
                 "not – eat any of these things? Explain why not.", ""))
    return PAGE_BOX(54, IMG(IMG_DIR + "p54-banner.jpg", "08 Eating") + '<div class="cols"><div>' + spk + '</div><div>' + voc +
                    "</div></div>" + IMG(IMG_DIR + "p54-kitchen.jpg", "A restaurant kitchen"))


def p55():
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a conversation between Aurora, a Peruvian businesswoman, and Claes who is '
              'visiting Peru. Aurora explains the things on the menu below.</p>' +
              EX("b55-la", "A", "Before you listen, discuss these questions:", UL([
                  "Do you eat much foreign food? What is your favourite?",
                  "Have you ever tried Peruvian food? Do you know anything about it?",
                  "Do you have any idea what any of the dishes on the menu below might be?"]) +
                 IMG(IMG_DIR + "p55-menu.jpg", "Menu", cls="md")) +
              X.orders("b55-lb") +
              EX("b55-lc", "C", "How much can you remember about each of the dishes that were mentioned?", "") +
              X.listen81("b55-ld", "D", "Work in pairs. Try to complete the sentences. Then listen again to check your answers.") +
              S81())
    box = ('<div class="box"><p><b>When we have to explain different foods or dishes, we often use the patterns below.</b></p><hr>'
           '<p class="ex-line"><i>It’s a kind of</i> vegetable / side dish / spice.<br><i>It’s a bit like</i> an oyster, <i>but</i> '
           'smaller.<br><i>It’s a bit like</i> vodka, <i>but not as</i> strong.<br><i>It’s made from</i> pig’s blood / a special '
           'kind of bean.</p></div>')
    dc = SEC("Developing conversations", "Describing dishes", box +
             EX("b55-da", "A", "Think of four different kinds of fruit, vegetables, drinks, dishes, etc. from your country. Decide "
                "how to explain them using the structures above.", "") +
             EX("b55-db", "B", "Work in pairs. Describe your choices and see if your partner can guess what you are describing.", ""))
    cp = SEC("Conversation practice", "",
             EX("b55-ca", "A", "Write a typical menu for a restaurant in your country. Write it in your own language.", "") +
             EX("b55-cb", "B", "Work in pairs. You’re trying to decide what to eat.",
                "<p><b>Student A:</b> you’re visiting the country on holiday or on business. You don’t speak the local language."
                "<br><b>Student B:</b> talk Student A through the menu.<br><b>Student A:</b> reject at least two things. Explain "
                "why. Then decide what you’d like to eat for starter, main course and dessert.</p>"))
    return PAGE_BOX(55, '<div class="cols"><div>' + IMG(IMG_DIR + "p55-market.jpg", "") + lis + '</div><div>' + dc + cp +
                    "</div></div>")


def p56():
    spk = SEC("Speaking", "",
              EX("b56-sa", "A", "Read the introduction to an article about people living abroad and getting used to foreign food. "
                 "Then work in pairs. Discuss these questions:", UL([
                     "Are there many specialist shops selling foreign food in your town / city? Are there any near where you live?",
                     "Do you ever shop in any of them? Why? / Why not?",
                     "What food from your country would you miss if you went to live abroad?"])))
    akey = REVEAL("<p>" + " ".join(rows(11, 1, 33, 46, split=62)) + "</p><p>" + " ".join(rows(11, 1, 46, 56, split=62)) + "</p>",
                  "Ответы (ключ)")
    read = SEC("Reading", "",
               EX("b56-ra", "A", "Work in two groups. Group A, read the texts about Ian and Isabella. Group B, read the texts "
                  "in File 3 on p. 156. As you read, answer these questions.", OL([
                      "Where are the two people in your texts from?", "Where are they living now? Why?",
                      "What do they like about the food and the way people eat there?", "Is there anything they miss about their home?",
                      "What do they still find strange or annoying?", "What do you think they’ll never get used to? Why?"]) +
                  article() + group_b() + akey) +
               EX("b56-rb", "B", "Work in pairs with a student from the other group. Ask each other the questions in exercise A.", "") +
               X.words_c("b56-rc", "C", "Continue working with a partner from the other group. Complete the sentences with words "
                         "from the texts. The definitions in brackets will help you.") +
               EX("b56-rd", "D", "Work in groups. Discuss these questions:", UL([
                   "Do you do or eat any of the things the four people found strange / annoying?",
                   "What was the strangest thing the four people mentioned?",
                   "What food and eating habits in your country do you think foreigners might find strange?"])))
    return PAGE_BOX(56, spk + read)


def p57():
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">Just because you’re foreign, it doesn’t '
                'mean (that) you can’t learn how to use chopsticks!<br>Just because I’m a man, it doesn’t mean (that) I can’t '
                'cook.<br>Just because I’m young, it doesn’t mean (that) I’m stupid, OK!<br>Just because you can it doesn’t mean '
                '(that) you should.</p></div>')
    box = ('<div class="box"><p><b>In <i>Reading</i>, the different people said:</b></p><p class="ex-line">The portions here '
           '<i>tend to be</i> enormous.<br>People <i>tend to buy</i> fresh food every day and cook.<br>They <i>tend not to eat</i> '
           'while they’re drinking.</p><hr><p><b>We use <i>tend to</i> before a verb to mean <i>usually, but not always</i>. The '
           'negative form is <i>tend not to</i> or <i>don’t tend to</i>.</b></p></div>')
    gr = SEC("Grammar", "tend to", box + X.tend("b57-ga") +
             EX("b57-gb", "B", "Work in pairs. Discuss which of the sentences in exercise A are true for you and your country. "
                "For example:", '<p class="ex-line">My wife and I <i>tend not to eat</i> ready meals, unless we’re both really busy. '
                                'We <i>tend to buy</i> fresh food and we cook most evenings.</p>') +
             EX("b57-gc", "C", "Work in pairs. Write five more sentences about your country using <i>tend (not) to</i>. The "
                "sentences could be about food, eating, shopping, work, education or character. Then tell your partner your "
                "sentences and see if they agree with you or are surprised by anything.",
                '<div class="writer" data-target="" data-id="u08-tend"><textarea rows="5"></textarea></div>') + HELP(147))
    return PAGE_BOX(57, patterns + gr + IMG(IMG_DIR + "p57-photos.jpg", ""))


def p58():
    voc = SEC("Vocabulary", "Restaurants",
              EX("b58-va", "A", "In pairs, discuss whether each of these sentences about restaurants is a good thing or a bad "
                 "thing. Why?", UL(["It’s always packed.", "It’s always deserted.", "It looks out over the sea.",
                                    "The portions are huge.", "The food’s very rich.", "It’s home-style cooking.",
                                    "It only does seafood.", "It’s got trendy décor.", "The food’s quite greasy.",
                                    "It’s all organic."])))
    spk = SEC("Speaking", "", EX("b58-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "Do you and your family eat out much? Where?",
        "Do you know any restaurants:" + UL(["with strange or unusual décor?", "where you get huge portions?",
                                             "that are always packed?", "which serve the local speciality?",
                                             "where you can eat really cheaply?", "which have a great view?",
                                             "which aren’t very good?"])])))
    akey = REVEAL(OL([r[2:] for r in numbered(rows(12, 0, 53, 61))]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear four conversations about restaurants and food.</p>' +
              EX("b58-la", "A", '<span class="audio-ic">♪</span> 8.2 Listen and answer the questions.', OL([
                  "In conversation 1, what reasons do they give for going to a restaurant further away?",
                  "In conversation 2, why do they think they need to do up the restaurant?",
                  "In conversation 3, why does the woman want to swap dishes?",
                  "In conversation 4, why is the man threatening to leave without paying?"]) + akey) +
              X.restaurants("b58-lb", "B", "Work in pairs. Choose the words that were used in each conversation. Listen again and "
                            "check.") +
              EX("b58-lc", "C", "Work in pairs. Role-play two conversations.", OL([
                  "Decide where to go for something to eat or drink. One of you should reject at least one suggestion.",
                  "You are having dinner together in a restaurant. Ask each other about the dishes you have ordered. Use the "
                  "menu on p. 55 for ideas, if you need to."])) + S82())
    box = ('<div class="box"><p><b>In <i>Listening</i>, you heard that the vegetables were <i>overcooked</i>. We add <i>over-</i> '
           'to some verbs to mean <i>too much</i>.</b></p><hr><p class="ex-line">The vegetables were <i>overcooked</i> because '
           'they had been cooked too long, so they tasted watery.</p></div>')
    over = SEC("Vocabulary", "over-", box + X.over("b58-oa") +
               EX("b58-ob", "B", "Work in pairs. Discuss these questions:", UL([
                   "What do you think happened in each of the situations described in exercise A?",
                   "Have any of these things ever happened to you?"])))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>No wonder</i></b></p><p>If you say <i>(It’s) no wonder</i> '
              'something happened, it means you are not surprised about it.</p><p><i>No wonder he overslept this morning! He '
              'didn’t get to bed till three last night.<br>A: I’m starving. I haven’t eaten all day.<br>B: No wonder you’re '
              'hungry!</i></p></div>')
    return PAGE_BOX(58, '<div class="cols"><div>' + voc + spk + lis + '</div><div>' + IMG(IMG_DIR + "p58-terrace.jpg", "") +
                    over + native + "</div></div>")


def p59():
    gr = SEC("Grammar", "Second conditionals", X.second_rule("b59-ga") + HELP(147) +
             EX("b59-gb", "B", "Complete these sentences so they are true for you.", OL([
                 "If I had to wait half an hour to pay the bill, I’d …", "If I spilt Coca-Cola all over someone’s clothes, I’d …",
                 "If a waiter was being very rude to me, I’d …", "If I forgot my wallet and couldn’t pay for my meal, I’d …",
                 "If I was undercharged, I’d …"]) +
                '<div class="writer" data-target="" data-id="u08-gb"><textarea rows="5"></textarea></div>') +
             X.second_c("b59-gc") +
             EX("b59-gd", "D", "Write some sentences explaining how the following could be improved – and why they need to be.",
                UL(["The canteen / food where you work or study.", "The way people eat and drink in your country.",
                    "Your job, university or school.", "Public transport."]) +
                '<div class="writer" data-target="" data-id="u08-gd"><textarea rows="5"></textarea></div>') +
             EX("b59-ge", "E", "Work in pairs. Tell a partner your ideas.", ""))
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(12, 1, 45, 52, split=58))]), "Ответы (ключ)")
    spk = SEC("Speaking", "",
              EX("b59-sa", "A", "Have you seen anything in the news about the following things connected to food and drinking? "
                 "What was the story?", X.wordbox(["the amount people drink", "famine", "diets", "school meals", "farming",
                                                   "obesity", "anorexia"])) +
              EX("b59-sb", "B", '<span class="audio-ic">♪</span> 8.3 Listen. Answer the questions. Then work in pairs to check '
                 "your answers.", OL(["What problem does the person talk about?", "What example from the media does she give?",
                                      "What does she think the solution is?"]) + bkey + S83()) +
              EX("b59-sc", "C", "Discuss these questions as a class:", UL([
                  "Do you think the situation in exercise B is a problem in your country?",
                  "Do you agree with the solution the speaker suggested?"])) +
              EX("b59-sd", "D", "Work in groups. Look at these suggestions about how to deal with some of the issues in exercise "
                 "A. Say if you agree or disagree with them, and why. Use these sentence starters, or other second conditionals.",
                 '<p class="ex-line">If they did that, …<br>It’d be better if …</p>' + UL([
                     "Fashion magazines shouldn’t be sold to anyone under 16.",
                     "They should ban the sale of chocolate and ice cream.",
                     "Students should be given two pieces of fruit a day at school.",
                     "The legal age for drinking should be raised to 21.", "Farmers shouldn’t get any money from the government.",
                     "All the extra food which is produced in Europe should be given to developing countries free.",
                     "Children should discuss issues connected to nutrition more in school."]) +
                 IMG(IMG_DIR + "p59-canteen.jpg", "", cls="md")))
    return PAGE_BOX(59, '<div class="cols"><div>' + gr + '</div><div>' + spk + "</div></div>")


def build():
    return p54() + p55() + p56() + p57() + p58() + p59()
