"""Страница «Письмо»: Writing 03 Stories, pp. 124–125."""
from lib import G, EX, UL, SEC, PAGE_BOX, IMG, REVEAL
from ocrtext import paras, fixed, FIX
from keys import rows
from u03 import shared as X

IMG_DIR = "../assets/img/unit03/"
# пропуски рассказа: OCR-фрагмент -> (номер, ответ по ключу, подсказка)
GAPS = [("when I: .. (say)", "when I", 1, "said|had said", "say"),
        ("Everyone else (seem)", "Everyone else", 2, "seemed", "seem"),
        ("my heart! (beat)", "my heart", 3, "was beating", "beat"),
        ("Just as I* (think)", "Just as I", 4, "was thinking", "think"),
        ("behind me s (scream)", "behind me", 5, "screamed", "scream"),
        ("just .. (really / disappeared. I’ fly)", "just disappeared. I", 6, "was really flying", "really / fly"),
        ("and it? (open)", "and it", 7, "opened", "open"),
        ("views. I (land)", "views. I", 8, "landed", "land")]
FIX[124] = [("suddenly, the panic", "Suddenly, the panic"), ("I foated", "I floated"), (" - ", " – ")]


def story():
    html = ""
    for p in paras(124, (440, 230, 712, 745), indent=10**6, gap=1.2):
        p = fixed(124, p)
        for ocr, lead, n, ans, hint in GAPS:
            p = p.replace(ocr, f"{lead} <sup>{n}</sup>{G(ans)} ({hint})")
        html += f"<p>{p}</p>"
    return f'<div class="story hand">{html}</div>'


def build():
    spk = SEC("Speaking", "",
              '<p class="intro">You are going to read a short story written for an exam. It starts with the line: <i><b>It was '
              'dangerous, but I knew I had to do it.</b></i></p>' +
              EX("w3-s", "", "Work in pairs. Discuss these questions:", UL([
                  "Based on this first line, think of four possible things that the writer was about to do.",
                  "How do you think each of these four stories might then develop?"])))
    ckey = REVEAL(" ".join(rows(28, 0, 5, 7, split=56)), "Ответ (ключ)")
    wr = SEC("Writing", "A story",
             EX("w3-wa", "", "The four sentences a–d below all come from the story. Check you understand the words in <b>bold</b>. "
                "Then answer the questions.",
                "<p>1 What do you think is the connection between the sentences?</p>" + ckey) +
             X.story_order("w3-wb", "", "2 What order would you expect them to happen in?"))
    gr = SEC("Grammar", "Narrative tenses",
             EX("w3-ga", "A", "Do you remember how to use the past simple, the past continuous and the past perfect? Look back "
                'at the <a href="../unit01/theory.html">grammar reference on pp. 136–137</a> to check.', "") +
             EX("w3-gb", "B", "Now read the story and put the words in brackets into the correct form.", story()))
    spk2 = SEC("Speaking", "", EX("w3-s2", "", "Work in pairs. Discuss these questions:", UL([
        "Do you know anyone who has done a parachute jump?", "Would you like to do one? Why? / Why not?",
        "Would you like to any of these other dangerous things? Are there any you have done already?" + UL([
            "go white-water rafting", "go mountaineering", "do a bungee-jump", "go hang-gliding", "hitch-hike round the world",
            "explore caves"])])))
    kbox = ('<div class="box"><p><b><i>Was / Were (just) about to</i> + verb is used to talk about something you were planning to '
            'do before something else happened. <i>When suddenly</i> often follows <i>just about to</i>.</b></p>'
            '<p class="ex-line">I was just about to jump when it suddenly hit me!</p><hr>'
            '<p><b><i>Just as</i> is used to emphasise that two verbs happened at exactly the same time. It is more common to use '
            'the past continuous after <i>just as</i>, but the past simple is also possible.</b></p>'
            '<p class="ex-line">Just as I was thinking about maybe changing my mind, the voice behind me screamed, ‘Go! Go! Go!’<br>'
            'Just as I turned on the computer, the lights went out.</p></div>')
    kw = SEC("Key words for writing", "Just about to, just as", kbox + X.just_match("w3-ka") +
             EX("w3-kb", "B", "Work in pairs. Think of one more possible ending for each sentence half in 1–6 in exercise A.", "") +
             X.just_rewrite("w3-kc"))
    vbox = ('<div class="box"><p><b>Using descriptive verbs makes stories more exciting.</b></p><hr>'
            '<p class="ex-line">The voice behind me screamed, ‘Go! Go! Go!’</p></div>')
    voc = SEC("Vocabulary", "Ways of doing things", vbox + X.verbs_match("w3-va") +
              EX("w3-vb", "B", "Take turns acting the words in exercise A. Can your partner guess what you are doing?", "") +
              X.verbs_gaps("w3-vc"))
    pr = SEC("Practice", "",
             EX("w3-pa", "A", "Look at the exam questions below and choose one. Write a story that starts with one of the "
                "following lines:", UL(["It was three in the morning when the phone rang.",
                                        "It was dangerous, but I knew I had to do it."]) +
                "<p><b>Or write a story that ends with one of the following lines:</b></p>" +
                UL(["… and that was the best day of my life.", "… and that the worst day of my life."])) +
             EX("w3-pb", "B", "Spend five minutes planning your story. Then work in pairs to discuss your ideas. Can you think "
                "of any ways to make the story more exciting?", "") +
             EX("w3-pc", "C", "Write a story of between 150 and 180 words.",
                '<div class="writer" data-target="150–180" data-id="u03-story"><textarea placeholder="It was …"></textarea>'
                '<div class="cnt"></div></div>'))
    p124 = PAGE_BOX(124, IMG(IMG_DIR + "p124-banner.jpg", "03 Writing — Stories") +
                    '<div class="cols"><div>' + spk + wr + gr + IMG(IMG_DIR + "p124-parachute.jpg", "", cls="md") +
                    '</div><div>' + spk2 + "</div></div>")
    p125 = PAGE_BOX(125, IMG(IMG_DIR + "p125-banner.jpg", "") +
                    '<div class="cols"><div>' + kw + '</div><div>' + voc + pr + "</div></div>")
    return p124 + p125
