"""Страница «Письмо»: Writing 05 Suggesting changes, pp. 128–129. Письмо — из OCR."""
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from ocrtext import paras, fixed, FIX
from keys import rows
from u05 import shared as X

IMG_DIR = "../assets/img/unit05/"
FIX[128] = [("the goo that", "the zoo that"), ("after lunch:", "after lunch."), ("afternoon;", "afternoon,"), (" - ", " – "),
            ("on behalf of", "<b>on behalf of</b>"), ("On the whole", "<b>On the whole</b>"), ("are scheduled", "<b>are scheduled</b>"),
            ("Alternatively", "<b>Alternatively</b>"), ("sorry if this causes any inconvenience", "<b>sorry if this causes any "
                                                                                              "inconvenience</b>"),
            (" Yours sincerely,", "")]


def letter():
    ps = [fixed(128, p) for p in paras(128, (425, 240, 760, 960), indent=10**6, gap=1.2)]
    return ('<div class="story hand">' + "".join(f"<p>{p}</p>" for p in ps) +
            "<p>Yours sincerely,</p><p>Simon Holden</p></div>")


def build():
    spk = SEC("Speaking", "", EX("w5-s", "", "Work in groups. Discuss these questions:", UL([
        "What things need doing when you organise the following?" + UL(["a meeting", "a surprise party", "a wedding",
                                                                       "a group excursion", "a conference"]),
        "Which is the most difficult thing to organise? Why?",
        "Have you ever been involved in organising any of these things? How easy was it?",
        "Did you have to make any changes or compromises?"])))
    wr = SEC("Writing", "",
             '<p class="intro">Fourteen 15-year-old schoolchildren are going on an exchange visit to Valencia, Spain. One of '
             'them, Simon Holden, has written to the leader of the organisation that is arranging the trip (Ms Roberts) to ask '
             'for a change to the programme.</p>' + letter() +
             EX("w5-wa", "A", "Read the letter. If you were Ms Roberts, would you agree to the change? Why? / Why not?", "") +
             EX("w5-wb", "B", "What ways does Simon Holden use to try and persuade Ms Roberts?", "") +
             EX("w5-wc", "C", "Translate the words in <b>bold</b> into your language. Then write new example sentences using the "
                "words.", '<div class="writer" data-target="" data-id="u05-bold"><textarea rows="5"></textarea></div>'))
    voc = SEC("Vocabulary", "<i>Programme</i>",
              '<p class="intro">In the letter the writer says thanks for <i>putting together the programme</i>.</p>' +
              X.programme("w5-va"))
    kbox = ('<div class="box"><p><b><i>However, although</i> and <i>but</i> can all have a similar meaning, but they use '
            'different grammar.</b></p></div>')
    ckey = REVEAL(OL(["Giving all the participants a souvenir is a nice idea, but it might be a bit too expensive.",
                      "Although I personally like rock music, some of the older people coming might prefer something different.",
                      "The menu for the dinner looks great. However, I think we should have a better option for vegetarians."]),
                  "Ответ (ключ)")
    kw = SEC("Keywords for writing", "<i>However, although</i> and <i>but</i>", kbox +
             X.hab_rules("w5-ka", "A", "Look in the letter and find examples of the words. Then complete the rules 1–2. Did you "
                         "notice how commas were used in the sentences?") + X.hab_complete("w5-kb") +
             EX("w5-kc", "C", "Punctuate these sentences correctly.", OL([
                 "Giving all the participants a souvenir is a nice idea but it might be a bit too expensive.",
                 "Although I personally like rock music some of the older people coming might prefer something different.",
                 "The menu for the dinner looks great however I think we should have a better option for vegetarians."]) +
                '<div class="writer" data-target="" data-id="u05-punct"><textarea rows="4"></textarea></div>' + ckey))
    pr = SEC("Practice", "",
             EX("w5-pa", "A", "Work in pairs. Plan either a day trip round a city you know or a surprise party / event for a "
                "friend. Write out the programme of events and times.",
                '<div class="writer" data-target="" data-id="u05-prog"><textarea rows="5"></textarea></div>') +
             EX("w5-pb", "B", "Swap your programme with another pair. Write a letter suggesting a change to their programme. "
                "Explain why you want to make the change and how it could be done. Use as much of the language from these pages "
                "as you can.", '<div class="writer" data-target="" data-id="u05-letter"><textarea placeholder="Dear …">'
                               '</textarea><div class="cnt"></div></div>'))
    p128 = PAGE_BOX(128, IMG(IMG_DIR + "p128-banner.jpg", "05 Writing — Suggesting changes") +
                    '<div class="cols"><div>' + spk + IMG(IMG_DIR + "p128-valencia.jpg", "Valencia", cls="md") +
                    '</div><div>' + wr + "</div></div>")
    p129 = PAGE_BOX(129, '<div class="cols"><div>' + voc + IMG(IMG_DIR + "p129-fan.jpg", "", cls="md") +
                    IMG(IMG_DIR + "p129-race.jpg", "Motorcycle Grand Prix", cls="md") + '</div><div>' + kw + pr + "</div></div>")
    return p128 + p129
