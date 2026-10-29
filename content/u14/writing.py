"""Страница «Письмо»: Writing 08 A review, pp. 134–135."""
from lib import EX, UL, OL, SEC, PAGE_BOX, IMG, REVEAL
from ocrtext import paras, fixed
from keys import rows
from . import shared as X

IMG_DIR = "../assets/img/unit14/"
FILMS = [("Life is Beautiful <span>(La vita è bella)</span>", "p135-life.jpg", (50, 410, 375, 535)),
         ("Spellbound", "p135-spellbound.jpg", (50, 665, 375, 805)),
         ("Batman Begins", "p135-batman.jpg", (50, 940, 375, 1080))]


def films():
    out = ""
    for t, img, box in FILMS:
        txt = " ".join(fixed(135, p) for p in paras(135, box, indent=12)).replace("try Batman Begins", "try <i>Batman Begins</i>")
        out += f'<div class="note"><h4><i>{t}</i> ★★★★★</h4>' + IMG(IMG_DIR + img, "", cls="md") + f"<p>{txt}</p></div>"
    return '<div class="article"><h3 class="art-title">Something for everyone!</h3>' + out + "</div>"


def build():
    spk = SEC("Speaking", "", EX("w14-s", "", "Work in groups. Discuss these questions:", UL([
        "Which do you prefer: watching films at the cinema, on DVD, on TV or downloaded from the internet? What is good / bad "
        "about each one?", "How do you decide what film you want to watch? Do you ever read reviews?",
        "Have you ever been given a recommendation which turned out to be a bad one?"])))
    voc = SEC("Vocabulary", "Describing films", X.film_adj("w14-va") + X.film_part("w14-vb") +
              EX("w14-vc", "C", "Choose four adjectives from exercises A and B. Use them to tell a partner about films you know.",
                 ""))
    wr = SEC("Writing", "",
             '<p class="intro">You are going to read a short article recommending three films.</p>' +
             EX("w14-wa", "A", "Read the text and answer the questions.", OL([
                 "Have you seen the films? Do you agree with the descriptions?", "Would you like to see the films? Why? / Why not?",
                 "Does the choice of films offer ‘something for everyone’?"])) + films() +
             EX("w14-wb", "B", "Work in pairs. Answer the questions.", OL([
                 "What tense is used to describe the plot?", "Are you told the whole plot? Why not?",
                 "When does the writer give opinions about the film?"]) +
                REVEAL("<br>".join(rows(29, 1, 30, 36, split=57)), "Ответ (ключ)")))
    kbox = ('<div class="box"><p><b><i>While</i> and <i>during</i> both introduce a period of time when something else happened. '
            'They have different grammar:</b></p><hr><p><b><i>during</i> + noun</b></p><p class="ex-line">It tells the story of '
            'an Italian man and his son who are sent to a concentration camp during the Second World War.</p><hr>'
            '<p><b><i>while</i> + clause</b></p><p class="ex-line">While they are there, the father distracts the boy from all '
            'the bad things that are happening.</p></div>')
    kw = SEC("Key words for writing", "<i>While</i> and <i>during</i>", kbox + X.while_during("w14-ka"))
    gbox = ('<div class="box"><p><b>We often make a text shorter by adding information after a noun using an <i>-ed / -ing</i> '
            'participle, a prepositional phrase, or relative clause.</b></p></div>')
    gr = SEC("Grammar", "Adding information after the noun",
             EX("w14-ga", "A", "Can you remember how 1–3 were written as one sentence in the articles?", OL([
                 "This is a strangely uplifting film. It is directed by and stars Roberto Benigni.",
                 "This is a marvellous documentary. It is about the national spelling competition.",
                 "It also stars Cillian Murphy. He is particularly brilliant as the scary villain, the Scarecrow."]) +
                REVEAL("1 This is a strangely uplifting film directed by and starring Roberto Benigni.<br>2 This is a marvellous "
                       "documentary about the national spelling competition …<br>3 It also stars Cillian Murphy, who is "
                       "particularly brilliant as the scary villain, the Scarecrow.", "Ответ (текст статьи)")) + gbox +
             EX("w14-gb", "B", "Rewrite 1–6 as one sentence using each method twice.", OL([
                 "This a moving love story. It’s about a disabled woman.", "This is a comedy action film. It stars Akshay Kumar.",
                 "The film is directed by Lasse Hallstrom. He also directed <i>The Cider House Rules</i>.",
                 "The film is set in a small town. The story happens during the mayoral election.",
                 "The main character is a brilliant but lonely doctor. The part is superbly played by Jennifer Jenkins.",
                 "The documentary follows the lives of four couples. The couples have recently emigrated to Australia."]) +
                '<div class="writer" data-target="" data-id="u14-noun"><textarea rows="6"></textarea></div>' +
                REVEAL("<br>".join(rows(29, 1, 44, 55, split=57)), "Ответ (ключ)")))
    pr = SEC("Practice", "",
             EX("w14-pa", "", "A film magazine has a competition inviting readers to send in reviews of three films. Each week "
                "they publish one winner. Write your entry for one of the choices below. It should be between 150 and 180 "
                "words.", UL(["Three best films of last year", "Three films for a Sunday afternoon with the family",
                              "Three classics", "Three films for three different moods"]) +
                '<div class="writer" data-target="150–180" data-id="u14-review"><textarea placeholder="This is a …">'
                '</textarea><div class="cnt"></div></div>'))
    p134 = PAGE_BOX(134, IMG(IMG_DIR + "p134-banner.jpg", "08 Writing — A review") +
                    '<div class="cols"><div>' + spk + voc + '</div><div>' + kw + "</div></div>")
    p135 = PAGE_BOX(135, '<div class="cols"><div>' + wr + '</div><div>' + gr + pr + "</div></div>")
    return p134 + p135
