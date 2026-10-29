"""Страница «Письмо» модуля 10. Отдельного урока письма у юнита нет (к юнитам 9–12 относятся Writing 05–06, с. 128–131),
поэтому здесь — письменные задания из уроков юнита 10."""
from lib import EX, SEC, PAGE_BOX, IMG

IMG_DIR = "../assets/img/unit10/"


def writer(id, target, ph, rows=8):
    return (f'<div class="writer" data-target="{target}" data-id="{id}"><textarea rows="{rows}" placeholder="{ph}"></textarea>'
            '<div class="cnt"></div></div>')


def build():
    intro = ('<p class="note-s">В учебнике у юнита 10 нет отдельного урока письма: к блоку юнитов 9–12 относятся уроки '
             '<i>Writing 05 Suggesting changes</i> и <i>Writing 06 Reports</i> (с. 128–131). Здесь собраны письменные задания '
             'из уроков юнита 10.</p>')
    a = SEC("Describing what’s on", "p. 72",
            '<div class="box"><p><b>I haven’t seen</b> the new David Lynch movie, <b>but it’s supposed to be</b> quite weird.<br>'
            '<b>I haven’t been to</b> the Julie Freeman installation yet, <b>but it’s supposed to be</b> amazing.</p></div>' +
            EX("w10-a", "1", "Think of some films, plays, musicals, exhibitions, books, CDs or places that you do not personally "
               "know, but that you could describe using <i>spectacular, touristy, trendy, dull, weird, amazing, terrific …</i> "
               "Write five sentences about them using the patterns in the box.",
               writer("u10-w-supposed", "", "I haven’t seen …, but it’s supposed to be …", 6)))
    b = SEC("Describing an event", "p. 74",
            EX("w10-b", "2", "Write about a great / terrible time you had on holiday / at a cinema / theatre / restaurant / hotel "
               "/ party. Use a list with <i>everything</i> (<i>The music, the people, everything!</i>) and language from "
               "<i>Vocabulary: Describing an event</i>. Write 100–150 words.",
               writer("u10-w-event", "100–150", "It was one of the best things I’ve seen in ages. …")))
    c = SEC("The future in the past", "p. 75",
            EX("w10-c", "3", "Write about a last-minute change of plan, a prediction that failed to come true or a promise "
               "someone failed to keep. Use <i>was going to, would, was supposed to, was about to</i>. Write 80–120 words.",
               writer("u10-w-plan", "80–120", "I was going to …, but …")))
    d = SEC("Language patterns", "p. 74",
            EX("w10-d", "4", "Write the sentences in your language. Then translate them back into English and compare your "
               "English to the original.",
               '<p class="ex-line">It was one of the worst things I’ve seen in a long time.<br>It’s one of the worst clubs I’ve '
               'ever been to.<br>It’s the nicest thing anyone’s ever done for me.<br>It’s the best book I’ve read in ages.</p>' +
               writer("u10-w-patterns", "", "…", 6)))
    return intro + PAGE_BOX("70–75", IMG(IMG_DIR + "p71-friends.jpg", "", cls="md") + a + b + c + d)
