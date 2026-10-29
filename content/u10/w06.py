"""Страница «Письмо»: Writing 06 Reports, pp. 130–131. Отчёт — из OCR."""
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from ocrtext import lines, fixed, _fix, FIX
from u06 import shared as X

IMG_DIR = "../assets/img/unit06/"
FIX[130] = [("sporte centre", "sports centre")]
HEADS = ("Current provision", "Sports", "Other activities", "Recommendations")


def report():
    out, cur = [], None
    for l in lines(130, (405, 540, 780, 1060)):
        t = fixed(130, _fix(l["t"])).strip()
        if t in HEADS:
            out.append(f"<h4>{t}</h4>")
            cur = None
        elif cur is None or (t.startswith("In terms of") and out[-1].startswith("<p>")):
            out.append("<p>" + t)
            cur = len(out) - 1
        else:
            out[cur] += " " + t
    return '<div class="story">' + "".join(x if x.startswith("<h4>") else x + "</p>" for x in out) + "</div>"


def build():
    spk = SEC("Speaking", "", EX("w6-s", "", "Work in pairs. Discuss these questions:", UL([
        "Look at the pictures below. What kind of age group do you think the activities / places are good for? 3–6 · 7–11 · "
        "12–15 · 16–18", "What other facilities are there for young people where you live? Do you think there are enough "
                         "facilities? Why? / Why not?"])) + IMG(IMG_DIR + "p130-activities.jpg", "", cls="md"))
    bkey = REVEAL("<p>… this is rarely used … / … more could be done … / … so it could be used … The passive is used because it "
                  "is more formal and impersonal and the person / people doing the action is / are unclear or unimportant.</p>",
                  "Ответ (ключ)")
    ckey = REVEAL("<p>… the council could provide … / … more could be done … / why not show …? / … the council should "
                  "consider …</p>", "Ответ (ключ)")
    wr = SEC("Writing", "",
             EX("w6-wa", "A", "Read the report on the facilities for young people in a residential area called Rocafort. Work in "
                "pairs. Discuss the questions.", UL([
                    "Do you think the area is better or worse for young people than where you live? Why?",
                    "Can you think of any other services or facilities that could be provided for the young people of Rocafort?"])) +
             EX("w6-wb", "B", "Look at the report. Underline all the examples of the Passive that you can find. Then work in "
                "pairs. Discuss these questions.", UL(["Why is the passive used in writing reports?",
                                                       "Do you use the passive in this way in your language?"]) + bkey) +
             EX("w6-wc", "C", "Which three ways of giving advice / recommendations were used in the report?", ckey) + report())
    voc = SEC("Vocabulary", "Describing facilities", X.facilities("w6-va") +
              EX("w6-vb", "B", "Work in pairs. Discuss these questions.", UL([
                  "Where do kids hang out in your town / area? Is it a problem?",
                  "Does the government subsidise anything in your area?",
                  "Are there any places / facilities you know which are under used? How could more be done with them?",
                  "Is there anything your local council should consider doing?"])))
    kbox = ('<div class="box"><p><b>We often refer to particular things in a report using <i>as far as X is / are concerned</i> '
            'or <i>in terms of X</i>.</b></p><hr><p class="ex-line">As far as classes are concerned, the council could provide a '
            'wider range for all age groups.<br>In terms of the sports facilities, the council could provide more organised '
            'teams.</p></div>')
    kw = SEC("Key words for writing", "Referring to things", kbox + X.referring("w6-ka") +
             EX("w6-kb", "B", "Think of the area where you live. Write endings for these sentence starters explaining how people "
                "feel or how things could be different.", OL([
                    "As far as public transport is concerned, …", "As far as schools are concerned, …",
                    "In terms of sports facilities, …", "In terms of things for young people, …"]) +
                '<div class="writer" data-target="" data-id="u06-ref"><textarea rows="5"></textarea></div>') +
             EX("w6-kc", "C", "Work in pairs. Discuss your sentences from exercise B. Does your partner agree?", ""))
    pr = SEC("Practice", "",
             EX("w6-pa", "", "Write a short report on one of the following.", UL([
                 "Facilities for young people where you live", "Public transport where you live",
                 "Your school / university / workplace"]) +
                "<p><b>Talk about the current situation and make some recommendations about how things could be improved.</b></p>"
                '<div class="writer" data-target="" data-id="u06-report"><textarea placeholder="Current provision …"></textarea>'
                '<div class="cnt"></div></div>'))
    p130 = PAGE_BOX(130, IMG(IMG_DIR + "p130-banner.jpg", "06 Writing — Reports") +
                    '<div class="cols"><div>' + spk + '</div><div>' + wr + "</div></div>")
    p131 = PAGE_BOX(131, '<div class="cols"><div>' + voc + kw + '</div><div>' + pr + "</div></div>")
    return p130 + p131
