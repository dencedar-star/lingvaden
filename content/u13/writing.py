"""Страница «Письмо»: Writing 07 For and against, pp. 132–133."""
import re
from lib import S, EX, UL, OL, SEC, PAGE_BOX, IMG, REVEAL
from ocrtext import paras, fixed, FIX
from keys import rows
from . import shared as X

IMG_DIR = "../assets/img/unit13/"
FIX[132] = []
# пропуски эссе: регулярное выражение по OCR -> замена (номер, ответ по ключу)
GAPS = [(r"travel\.-\. I do", "travel. {1}, I do"), (r"popular\. “\., they", "popular. {2}, they"),
        (r"B\. \.+ people", "B. {3}, people"), (r"and “\.+ the car", "and {4}, the car"),
        (r"^\.+, in the long term, we”\.+ need", "{5}, in the long term, we {6} need"), (r"car\. ‘\.+ we will", "car. {7}, we will"),
        (r"^\.+, while", "{8}, while")]
KEY = ["Personally", "Firstly", "Secondly", "thirdly", "However", "obviously", "Otherwise", "In conclusion"]


def essay():
    opts = sorted(X.ESSAY_BOX, key=str.lower)
    html = ""
    for p in paras(132, (425, 330, 794, 780), indent=10**6, gap=1.2):
        for a, b in GAPS:
            p = re.sub(a, b, p)
        p = re.sub(r"\{(\d)\}", lambda m: f"<sup>{m.group(1)}</sup>" + S(KEY[int(m.group(1)) - 1], opts), p)
        html += f"<p>{p}</p>"
    assert html.count("<select") == 8, "пропуски эссе"
    return f'<div class="story typed">{html}</div>'


def build():
    spk = SEC("Speaking", "",
              EX("w13-s", "", "You are going to read a short essay about cars. First, work in pairs. Discuss these questions:",
                 UL(["What kind of car do you / the people in your family have?", "Do you have a favourite kind of car?",
                     "What is the traffic like where you live?", "Do you use the car much? To go where?"])))
    title = ('<div class="note"><p><b>‘Cars are no longer the most effective means of transport.’ How far do you agree with this '
             'statement?</b></p></div>')
    table = ('<table class="voc"><tr><th>Cars are good because…</th><th>Cars aren’t good because…</th></tr>' +
             "".join(f'<tr><td><div class="writer" data-target="" data-id="u13-good{i}"><textarea rows="2"></textarea></div></td>'
                     f'<td><div class="writer" data-target="" data-id="u13-bad{i}"><textarea rows="2"></textarea></div></td></tr>'
                     for i in (1, 2, 3)) + "</table>")
    dos = ('<div class="note"><h4>Dos and don’ts in academic writing</h4>' + OL([
        "Show you know why the question is being asked by giving examples of current trends or problems connected to it.",
        "Make your own opinion clear in your introduction.", "Allow space for points of view you disagree with.",
        "Explain why you disagree with them.", "Use paragraphs.",
        "Avoid using <i>you</i>. Use impersonal forms like <i>people</i> or <i>one</i>.",
        "Don’t use contractions like <i>it’ll</i> or <i>that’d</i>."]) + "</div>")
    wr = SEC("Writing", "",
             EX("w13-wa", "A", "Look at the essay title below. Write three reasons why people might agree with the statement in "
                "the title, and three reasons why people might disagree.", title + table) +
             EX("w13-wb", "B", "Work in pairs. Compare your ideas. Then discuss if you agree with the statements. Why? / Why not?",
                "") +
             EX("w13-wc", "C", "Read the essay. Does the writer think the same as you?", "") +
             EX("w13-wd", "D", "Complete the gaps with the words in the box.", X.wordbox(X.ESSAY_BOX) + essay()) +
             EX("w13-we", "E", "The list below contains seven pieces of advice. Find examples in the essay of where the writer "
                "follows each piece.", dos + REVEAL("<br>".join(rows(29, 0, 40, 52)), "Ответ (ключ)")))
    gbox = ('<div class="box"><p><b>We usually begin introductions to essays by describing current trends (or problems) connected '
            'to the title. To describe a change that happened before now, but which has present results, use the present '
            'perfect simple.</b></p><p class="ex-line">The number of cars on our roads has increased a lot over the last '
            'twenty years.</p><hr><p><b>To describe a trend that is not finished, we usually use the present continuous.</b></p>'
            '<p class="ex-line">Traffic is getting worse every year and we are slowly running out of oil.</p></div>')
    gr = SEC("Grammar", "Describing trends", gbox + X.trends("w13-ga") +
             REVEAL("<br>".join(rows(29, 1, 2, 12, split=57)), "Выражения времени (ключ)") +
             EX("w13-gb", "B", "Work in pairs. Discuss which trends are the same in your country – or how they are different.",
                "") +
             EX("w13-gc", "C", "Write similar introductions to those in exercise A for the two essay titles below.",
                '<div class="note"><p><b>‘We need the death penalty. It stops people from committing terrible crimes.’ '
                'Discuss.</b></p><p><b>‘Fast food is having a terrible effect on the health of the nation. As such, it should '
                'be banned.’ Do you agree?</b></p></div>'
                '<div class="writer" data-target="" data-id="u13-intro"><textarea rows="6"></textarea></div>'))
    kbox = ('<div class="box"><p><b>To introduce results or conclusions, we often use <i>as such</i>. It means ‘Because what has '
            'just been said is true.’ It usually begins a sentence and is followed by a comma.</b></p><hr>'
            '<p class="ex-line">Traffic is getting worse and we are slowly running out of oil. As such, it is worth asking if '
            'cars are still the most effective way to travel.</p></div>')
    kw = SEC("Keywords", "As such", kbox + X.as_such("w13-ka") +
             EX("w13-kb", "B", "Work in pairs. Think of one more possible sentence you could follow 1–5 with. Start each one "
                "with <i>As such</i>.", ""))
    pr = SEC("Practice", "",
             EX("w13-pa", "A", "You are going to write an essay of between 150 and 180 words based on the title below. Work "
                "in pairs. Discuss possible reasons why people might agree or disagree with the statement – and then discuss "
                "your own opinions.", '<div class="note"><p><b>‘Some sports and entertainment stars earn far too much money.’ '
                                      'How far do you agree with this statement?</b></p></div>') +
             EX("w13-pb", "B", "Plan the content of each of your paragraphs. Use the model text on the previous page to help you.",
                "") +
             EX("w13-pc", "C", "Write the essay. Use as much language from this unit as you can.",
                '<div class="writer" data-target="150–180" data-id="u13-essay"><textarea placeholder="Over the last few '
                'years, …"></textarea><div class="cnt"></div></div>'))
    p132 = PAGE_BOX(132, IMG(IMG_DIR + "p132-banner.jpg", "07 Writing — For and against") +
                    '<div class="cols"><div>' + spk + '</div><div>' + IMG(IMG_DIR + "p132-family.jpg", "") + "</div></div>" +
                    wr)
    p133 = PAGE_BOX(133, '<div class="cols"><div>' + gr + '</div><div>' + kw + pr + "</div></div>")
    return p132 + p133
