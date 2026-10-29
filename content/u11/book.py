"""Страница «Учебник»: Unit 11 The natural world, pp. 76–81 (+ File 10, p. 159). Длинные тексты — из OCR и ключей."""
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import text, script, fixed, FIX
from . import shared as X

IMG_DIR = "../assets/img/unit11/"

FIX.setdefault(81, []).extend([("but 1 really", "but I really"), ("beautifull", "beautiful!"), (" - ", " – ")])
FIX.setdefault(169, []).extend([("911.1", ""), ("so 1 went", "so I went"), ("B. Yeah?", "B: Yeah?"), ("Wowl", "Wow!"),
                                ("Yeahl", "Yeah!"), ("shocked, 1 almost", "shocked, I almost"), ("Godl", "God!"),
                                ("A- Well", "A: Well"), ("when._", "when …"), ("in...", "in …"), ("indonesia", "Indonesia")])
FIX.setdefault(170, []).extend([("Er ._ no!", "Er … no!"), ("Nol I buy", "No! I buy"), ("but | really", "but I really"),
                                (" - ", " – ")])


def S111():
    return SCRIPT("11.1", "", script(169, (40, 895, 397, 1050)) + script(169, (400, 80, 794, 800)), "169")


def S112():
    return SCRIPT("11.2", "", script(169, (400, 830, 794, 1050)) + script(170, (0, 70, 397, 170)), "169–170")


def S113():
    return SCRIPT("11.3", "S = Suzie, A = Al", script(170, (0, 215, 392, 1050)) + script(170, (400, 70, 794, 150)), "170")


def p76():
    voc = SEC("Vocabulary", "Animals",
              EX("b76-va", "A", "Work in pairs. Look at the pictures in File 10 on p. 159 and discuss these questions:",
                 UL(["Which of these animals do you like? Why?", "Are you scared of any of these animals? Why?"]) +
                 REVEAL(IMG(IMG_DIR + "p159-animals.jpg", "File 10: squirrel, lizard, bear, eagle, dolphin, cockroach, deer, "
                            "whale, wolf, crow, crocodile, parrot, snake, scorpion, rat",
                            "Information files, p. 159: 1 squirrel 2 lizard 3 bear 4 eagle 5 dolphin 6 cockroach 7 deer "
                            "8 whale 9 wolf 10 crow 11 crocodile 12 parrot 13 snake 14 scorpion 15 rat"), "File 10 (p. 159)")) +
              EX("b76-vb", "B", "Close your books. How many of the animals can you remember?", "") +
              EX("b76-vc", "C", "Which animals might you:", UL([
                  "see lying on a rock?", "see circling in the sky?", "see running across a road?",
                  "see swimming and jumping around off the coast?", "see disappearing into long grass?",
                  "hear making a dreadful noise?", "hear in the bushes?", "hear in the distance?",
                  "find crawling around a dirty kitchen?", "find hiding in your shoe?", "find sitting in a tree?"])))
    akey = REVEAL(OL(["1 crows, parrot; 2 snake, rat; 3 lizards",
                      "1 The crows were chasing a parrot. 2 The snake was lying across the road and the rat was eating it. "
                      "3 The lizards were running out of the bushes.",
                      "1 sorry, sympathetic, concerned; 2 disgusted, shocked"]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear three conversations about animals that people have seen.</p>' +
              EX("b76-la", "A", '<span class="audio-ic">♪</span> 11.1 Listen. Answer the questions.',
                 OL(["Which animals did each person see?", "What were they doing?", "How did each speaker feel?"]) + akey) +
              X.which_conv("b76-lb") + S111())
    spk = SEC("Speaking", "", EX("b76-sa", "A", "Work in pairs. Discuss these questions.", UL([
        "Have you heard any stories about animals escaping from anywhere?",
        "Would you ever save or kill an animal? In what situation?",
        "Do you like the idea of going trekking through the jungle? Why? / Why not?"])))
    return PAGE_BOX(76, IMG(IMG_DIR + "p76-banner.jpg", "11 The natural world") +
                    '<div class="cols"><div>' + voc + '</div><div>' + lis + spk + "</div></div>" +
                    IMG(IMG_DIR + "p76-lizard.jpg", ""))


def p77():
    box = ('<div class="box"><p><b>Good listeners ask questions when people tell stories.</b></p><hr>'
           '<p class="ex-line">A: I really thought they were going to eat me.<br>B: God! That sounds terrifying! <i>So what '
           'happened?</i><br>A: Well, luckily, the guides managed to stop the lizards.</p></div>')
    dc = SEC("Developing conversations", "Helping to tell stories", box + X.story_qs("b77-da") +
             EX("b77-db", "B", '<span class="audio-ic">♪</span> 11.2 Listen and check your answers.', "") + S112())
    gbox = ('<div class="box"><p><b>We can add clauses that begin with a verb in the <i>-ing</i> form to a sentence. It explains '
            'what someone / something is, or was, doing at a particular time.</b></p><hr>'
            '<p class="ex-line"><i>I suddenly noticed a group of crows looking quite excited.</i><br>(= I suddenly noticed a group '
            'of crows. They were looking quite excited.)<br><i>I suddenly saw this huge snake lying across the road.</i><br>'
            '(= I suddenly saw this huge snake. It was lying across the road.)</p></div>')
    gr = SEC("Grammar", "<i>-ing</i> clauses", gbox + X.ing_clauses("b77-ga") +
             EX("b77-gb", "B", "Work in pairs. Complete these sentences by adding <i>-ing</i> clauses.", OL([
                 "This deer was standing about three metres away from us …", "When we were on the ferry to Greece, we saw some "
                 "dolphins …", "Outside my window this morning, there was this squirrel …",
                 "I didn’t sleep very well last night. I could hear a dog somewhere …"]) +
                '<div class="writer" data-target="" data-id="u11-ing"><textarea rows="4"></textarea></div>') + HELP(150))
    cp = SEC("Conversation practice", "",
             EX("b77-ca", "A", "Think of any strange or unusual animals you have seen – or any animals you have seen doing "
                "something strange. Think about where they were and what they were doing when you saw them. Think about how "
                "you felt and what happened. Then work in groups. Tell some other students about your experiences. When one "
                "person finishes their story, another should try to tell a similar story. Use these expressions to connect "
                "the stories:", '<p class="ex-line"><i>It reminds me of something I once saw …<br>It actually reminds me of '
                                'something that happened to me …</i></p>'))
    return PAGE_BOX(77, '<div class="cols"><div>' + IMG(IMG_DIR + "p77-flamingos.jpg", "") + dc + '</div><div>' + gr + cp +
                    "</div></div>")


def p78():
    dkey = REVEAL(OL(["a global warming, destruction of habitats, hunting and trading; b global warming",
                      "a to check online trading sites for illegal animal trading; b because it’s relatively safe and makes it "
                      "possible to reach large numbers of potential buyers easily",
                      "a they were part of his hobby; b the police thought he was smuggling them into the country to sell them",
                      "a because horses have always been very important in the country; b because some were kept in zoos for "
                      "breeding and their numbers increased"]), "Ответы (ключ)")
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">Mongolia is known as ‘the land of '
                'the horse’.<br>Shanghai is known as ‘the Paris of the East’.<br>Aubergines are also known as eggplants.<br>'
                'The area is known for its oysters.<br>This rare species of shark is known to inhabit fresh water.<br>'
                'Very few details are known about this rare species.</p></div>')
    read = SEC("Reading", "",
               '<p class="intro">You are going to read four newspaper articles about animals and the environment.</p>' +
               EX("b78-ra", "A", "Look at the headlines below. Work in pairs. Discuss what you think each article might be "
                  "about.", UL([X.HEADLINES[i] for i in (1, 3, 0, 2)])) +
               EX("b78-rb", "B", "All of the words in the box appear in the four articles. Work in pairs. Discuss which words "
                  "you think might appear in which article, and why.", X.wordbox(X.WORDS)) +
               X.articles("b78-rc", img='<div class="cols">' + IMG(IMG_DIR + "p78-chimp.jpg", "") +
                          IMG(IMG_DIR + "p79-rider.jpg", "") + "</div>") +
               EX("b78-rd", "D", "Answer the questions about the four articles.", OL([
                   "a In article A, what four threats to animals are mentioned?<br>b Which sounds like the most serious?",
                   "a In article B, what do you think was the purpose of the IFAW investigation?<br>b Why do you think "
                   "organised gangs use the Internet?",
                   "a In article C, what did the man claim his smuggled goods were for?<br>b What do you think the police "
                   "thought he was doing?",
                   "a In article D, why do you think Mongolia is called ‘the land of the horse’?<br>b What saved the "
                   "<i>takhi</i> from extinction?"]) + dkey))
    return PAGE_BOX("78", read + patterns)


def p79():
    gbox = ('<div class="box"><p><b>We use passives when it is not clear who does an action (or it is unimportant). Passives '
            'are formed using the correct form of the verb <i>to be</i> + the past participle.</b></p><hr>'
            '<p class="ex-line">Scientists have warned that up to 50% of all animal species <i>could be destroyed</i> by '
            'global warming if action <i>is not taken</i> soon.</p></div>')
    gr = SEC("Grammar", "Passives", gbox + X.passive_gaps("b79-ga") + X.participles("b79-gb") + HELP(150))
    spk = SEC("Speaking", "", EX("b79-sa", "A", "Work in groups. Discuss these questions:", UL([
        "Are there any endangered species in your country? Is anything being done about it?",
        "Has global warming affected your country? How?",
        "Have you ever heard any other stories about animals being smuggled, traded, or cruelly treated (think about hunting, "
        "over fishing, fur, exotic pets and animal fighting for ‘sport’)?",
        "What else are organised criminal gangs involved in?", "Have you heard of anyone being arrested recently?",
        "Do you know any environmental groups? What do they do? Would you consider joining them?"])))
    return PAGE_BOX(79, '<div class="cols"><div>' + IMG(IMG_DIR + "p79-horses.jpg", "", cls="md") + '</div><div>' + gr + spk +
                    "</div></div>")


def p80():
    voc = SEC("Vocabulary", "Keeping pets", X.pets("b80-va") +
              EX("b80-vb", "B", "Work in pairs.", "<p><b>Student A:</b> compare and contrast photos 1 and 2 and say which "
                 "animal you think makes the best pet.<br><b>Student B:</b> do the same with photos 3 and 4. Use as much of the "
                 "language from exercise A as you can.</p>" +
                 '<div class="cols">' + IMG(IMG_DIR + "p80-dog.jpg", "1 dog", "1 dog") + IMG(IMG_DIR + "p80-cat.jpg", "2 cat", "2 cat") +
                 IMG(IMG_DIR + "p80-snake.jpg", "3 snake", "3 snake") + IMG(IMG_DIR + "p80-ferret.jpg", "4 ferret", "4 ferret") +
                 "</div>"))
    bkey = REVEAL(OL(["dogs – they grow too big, demanding; cats – only interested in food; snakes – terrifying, disgusting",
                      "answers will vary", "it hid behind the cooker – she had to offer it a mouse to persuade it to come out",
                      "answers will vary"]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two friends, Suzie and Al, talking about pets.</p>' + X.pets_tf("b80-la") +
              EX("b80-lb", "B", "Work in pairs. Discuss these questions. Listen again if you need to.", OL([
                  "What reasons do they give for not having these pets? – dogs – cats – snakes",
                  "Do you agree with the reasons they give?", "What happened when the snake escaped?",
                  "Do you know anyone whose pet escaped / was lost?"]) + bkey) + S113())
    native = ('<div class="note"><h4>Native speaker English</h4><p>We often describe ourselves in terms of things we like – or do '
              'not like – by saying we are <i>a dog / morning / film person</i>.</p><p><i>I’m actually more of a cat person.<br>'
              'I’m not really a people person. I don’t like to socialise much.<br>I’m a night person. I often don’t go to bed '
              'till three or later.<br>He’s not a music person. He’d much rather sit and watch TV.</i></p></div>')
    return PAGE_BOX(80, '<div class="cols"><div>' + voc + '</div><div>' + lis + native + "</div></div>")


def p81():
    pron = SEC("Pronunciation", "Stress and intonation for emphasis",
               '<div class="box"><p><b>In <i>Listening</i>, Suzie says <i>They’re so cute</i>. We often put an extra stress on '
               'adverbs like <i>so</i> to emphasise how we feel. Notice how the vowel sound is also lengthened.</b></p></div>' +
               EX("b81-pa", "A", '<span class="audio-ic">♪</span> 11.4 Listen and repeat the sentences.', OL([
                   "Oh, they’re <u>so</u> cute!", "He’s <u>so</u> lovely.", "He’s <u>so</u> annoying!",
                   "Their dog is just <u>really</u> out of control!", "It <u>really</u> stinks!", "It’s just <u>incredibly</u> noisy!",
                   "He <u>even</u> lets the cat walk on the kitchen surfaces!", "He <u>even</u> lets the dog <u>actually</u> lick his face!"])) +
               EX("b81-pb", "B", '<span class="audio-ic">♪</span> 11.5 Work in pairs. Underline the adverbs below that you think '
                  "carry an extra stress. Then listen and see if you were right.",
                  IMG(IMG_DIR + "p81-dog-owner.jpg", "", cls="md") +
                  f'<div class="story"><p>{fixed(81, text(81, (85, 620, 380, 770)))}</p></div>' +
                  '<p class="note-s">Аудиоскрипт 11.5 (с. 170) совпадает с текстом упражнения.</p>') +
               EX("b81-pc", "C", "Work in small groups. Take turns reading the text in exercise B. Who does it the best?", "") +
               EX("b81-pd", "D", "Think about things you really like or find really annoying about animals, pet owners or other "
                  "aspects of modern life. Use some of the sentence starters below.",
                  '<p class="ex-line"><i>I really love …<br>They’re so cute, the way they … / when they …<br>It’s so annoying '
                  'how …<br>What really annoys me is the way that / the fact that …</i></p>') +
               EX("b81-pe", "E", "Work in pairs. Tell your partner your ideas. Use extra stress to emphasise how you feel. Does "
                  "your partner agree with you?", ""))
    voc = SEC("Vocabulary", "Forming words",
              '<p class="intro">In <i>Listening</i>, Suzie said she liked cats’ independence. The noun <i>independence</i> comes '
              'from the adjective <i>independent</i>.</p>' + X.nouns("b81-va") +
              EX("b81-vb", "B", "Underline any collocations which go with the nouns in exercise A. Can you think of any other "
                 "collocations?", REVEAL(UL(["to have / enjoy / give someone their freedom",
                                             "destruction of their habitats / the rainforest / the planet",
                                             "in danger of extinction / at risk of extinction / threatened with extinction",
                                             "repeated warnings / a health warning / a final warning",
                                             "a serious threat / an enormous threat / a real threat",
                                             "under investigation / a police investigation / a thorough investigation"]),
                                         "Ответ (ключ)")))
    spk = SEC("Speaking", "", X.pet_questions("b81-sa") +
              EX("b81-sb", "B", "Work in pairs. Describe a pet that you or someone you know has. Show a picture if you have one. "
                 "Then talk about your pet, answering the questions from exercise A.", ""))
    return PAGE_BOX(81, '<div class="cols"><div>' + pron + '</div><div>' + IMG(IMG_DIR + "p81-kitten.jpg", "", cls="md") + voc +
                    spk + "</div></div>")


def build():
    return p76() + p77() + p78() + p79() + p80() + p81()
