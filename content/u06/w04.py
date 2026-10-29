"""Страница «Письмо»: Writing 04 Making requests, pp. 126–127."""
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from keys import rows, numbered
from u04 import shared as X

IMG_DIR = "../assets/img/unit04/"


def build():
    spk = SEC("Speaking", "",
              EX("w4-s", "", "Check you understand the words in <b>bold</b>. Then discuss the questions in pairs:", UL([
                  "When was the last time you <b>did a friend a favour</b>? What was it?",
                  "When was the last time you <b>asked a friend to do you a favour</b>? What was it? How did you ask? What did "
                  "they say?", "Do you <b>owe</b> anyone <b>a favour</b> at the moment?"])))
    gbox = ('<div class="box"><p><b>When we ask people to do things for us, we use modal verbs like <i>can</i> and <i>could</i>. '
            'We also sometimes use past tenses to sound polite. However, we also make questions longer using typical sentence '
            'starters.</b></p><hr><p>For example: <i>I was wondering if you could help me</i> is more polite than <i>I wonder if '
            'you can help me</i>. Less polite than either is <i>Can you help me?</i></p></div>')
    bkey = REVEAL("<p>" + "<br>".join(rows(28, 0, 56, 61, split=56)) + "</p>", "Ответ (ключ)")
    gr = SEC("Grammar", "Requests", gbox + X.requests("w4-ga") +
             EX("w4-gb", "B", "Work in pairs. Look at the four requests in exercise A and underline the parts of each that can be "
                "re-used in other questions. Then discuss these questions:", UL([
                    "Which of the four question starters is the most formal?",
                    "What form of the verb follows each of the question starters?"]) + bkey) +
             EX("w4-gc", "C", "Write a different ending for each of the four question starters in exercise A.",
                '<div class="writer" data-target="" data-id="u04-req"><textarea rows="4" placeholder="I was wondering …">'
                "</textarea></div>"))
    wr = SEC("Writing", "",
             EX("w4-wa", "A", "Read the four short emails. Then work in pairs. Discuss these questions. Do not fill in the gaps "
                "yet.", UL(["Do you think all the requests are reasonable?", "Are there any you would not ask? Why?"])) +
             X.emails("w4-wb"))
    kbox = ('<div class="box"><p><b>We saw in <i>Writing 02</i> on pp. 122–123 that <i>as</i> is sometimes used to mean '
            '<i>while</i>. <i>As</i> is also commonly used to mean <i>because</i>:</b></p><hr>'
            '<p class="ex-line">As your English is so good, could you do me a big favour and look through it carefully to check '
            'it’s OK?<br>I’d be really grateful as I’ll have loads of luggage.</p></div>')
    ideas = ["send me another copy of the invoice / Many", "give me a lift? / really grateful",
             "stay at your place for a few days? / really grateful", "extend the deadline for my essay? / incredibly grateful",
             "complete the work by Thursday / thanks"]
    kkey = REVEAL(OL([r[2:] for r in numbered(rows(28, 1, 9, 22, split=56))]), "Возможные ответы (ключ)")
    kw = SEC("Keywords for writing", "<i>as</i>", kbox +
             EX("w4-ka", "", "Use the ideas below to write five requests and say thanks. Add reasons using <i>as</i> and then add "
                "your own ideas. For example:",
                '<p class="ex-line"><i>look after the kids? / really grateful</i><br>Is there any way you could look after the '
                'kids tonight as we really need a night out together on our own? We’d be really grateful.</p>' + OL(ideas) +
                '<div class="writer" data-target="" data-id="u04-as"><textarea rows="6"></textarea></div>' + kkey))
    vbox = ('<div class="box"><p><b><i>As</i> is also used in certain common expressions</b></p><hr>'
            '<p class="ex-line">Do you think you could inform me as soon as possible?</p></div>')
    voc = SEC("Vocabulary", "<i>as … as</i> expressions", vbox + X.as_order("w4-va") + X.as_gaps("w4-vb"))
    pr = SEC("Practice", "",
             EX("w4-pa", "A", "Work in pairs. Write two short emails making requests. One should be to a hotel or company and "
                "the other should be to your partner. Use as much language from this writing unit as you can.",
                '<div class="writer" data-target="" data-id="u04-mail1"><textarea placeholder="Dear Sir/Madam, …"></textarea>'
                '<div class="cnt"></div></div><div class="writer" data-target="" data-id="u04-mail2">'
                '<textarea placeholder="Hi …"></textarea><div class="cnt"></div></div>') +
             EX("w4-pb", "B", "Swap your emails with your partner. Write a reply to each one.", ""))
    p126 = PAGE_BOX(126, IMG(IMG_DIR + "p126-banner.jpg", "04 Writing — Making requests") +
                    '<div class="cols"><div>' + spk + gr + '</div><div>' + wr + "</div></div>")
    p127 = PAGE_BOX(127, '<div class="cols"><div>' + IMG(IMG_DIR + "p127-airport.jpg", "Milan airport", cls="md") + kw +
                    '</div><div>' + voc + pr + "</div></div>")
    return p126 + p127
