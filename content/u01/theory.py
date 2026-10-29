"""Страница «Теория»: Grammar reference pp. 136–137 (из OCR, правила/примеры — по цвету) и пояснения из юнита."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from lib import IMG
from keys import column

FIX[136] = [("questions ask about unfinished,", "questions ask about unfinished,")]
FIX[137] = [("(- I fell", "(= I fell"), ("remembered / hadn’t", "remembered I hadn’t"),
            ("cooker off.", "cooker off,"), ("When 1 unpacked", "When I unpacked")]


def build():
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 8–13</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>Question formation <small>(p. 8)</small></h3>'
        '<div class="box"><p><b>We generally make questions by using the auxiliary verb (<i>be / have / do</i>) + the subject '
        '(<i>you / your parents / he / they</i>) and then a noun, adjective or verb.</b></p><hr>'
        '<p class="ex-line">Are you a doctor? · Have your parents left already? · What did you do yesterday? · What are you doing now?</p></div>'
        '<h3>Narrative tenses <small>(p. 12)</small></h3>'
        '<div class="box"><p><b>The past simple:</b> <i>I stayed in and watched TV. / I went to bed as soon as I got home. / I didn’t hear you.</i></p><hr>'
        '<p><b>The past continuous:</b> <i>I was chatting to him and he suddenly walked off. / I’m sorry. I wasn’t listening.</i></p><hr>'
        '<p><b>The past perfect:</b> <i>He told me he’d asked you. / In the morning, I realised I’d left my bag in the restaurant.</i></p></div>'
        '<table class="voc"><tr><th>Tense</th><th>Usage (p. 12, ex. C — по ключу)</th></tr>'
        '<tr><td>The past continuous</td><td>shows an action was unfinished when another past action happened.</td></tr>'
        '<tr><td>The past perfect</td><td>emphasises an action that happened before another past action, time or event</td></tr>'
        '<tr><td>The past simple</td><td>shows completed actions that follow one after the other.</td></tr></table>'
        '<h3>Other uses of the past continuous <small>(p. 12)</small></h3>'
        '<div class="box"><p><b>Sometimes we use the past continuous to emphasise an activity and the fact that it went on for a period of time.</b></p><hr>'
        '<p class="ex-line">I was banging on the door and shouting, but nothing.<br>I’m looking for a flat to rent and I was phoning round a few places this morning before class.</p></div>'
        '<h3>Asking follow-up questions <small>(p. 9)</small></h3>'
        '<div class="box"><p><b>We often follow up a question and answer by asking a related question to find out more details. Some of these questions are quite fixed.</b></p></div>'
        '<h3>John was telling me … <small>(p. 13)</small></h3>'
        '<div class="box"><p><b>We often use <i>X was telling me (that)</i> to report what someone said, and then continue the conversation by adding a comment or a question.</b></p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 8)</small></h4><p><b><i>I’m really into</i></b> — In English, people often say <i>I’m really into</i> instead of <i>I really like</i>. It is generally used when talking about music, sport, films and free-time activities. This is particularly common among young people.</p><p><i>I’m really into cooking. I’m really into jazz.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 9)</small></h4><p><i>I’d rather not say.<br>I’d rather not.<br>I’d rather not talk about it, if you don’t mind.<br>I’d rather go somewhere else, if that’s OK with you.<br>I’d rather do something else.</i></p></div></div>'
        "</article>")
    vocab = (
        '<article class="page" id="vocab"><span class="page-no">Учебник, с. 10</span><h2>Vocabulary: Learning languages</h2>'
        '<table class="voc"><tr><th>Word / phrase</th><th>Meaning (ключ)</th></tr>'
        '<tr><td><b>fairly fluent</b>, <b>can maintain conversations on a range of topics</b></td><td>quite confident and able to speak without too much hesitation; can talk easily about different subjects</td></tr>'
        '<tr><td><b>get by</b></td><td>survive / manage</td></tr>'
        '<tr><td><b>very basic</b></td><td>simple / limited</td></tr>'
        '<tr><td><b>bilingual</b></td><td>speaking two languages equally well, as a native speaker</td></tr>'
        '<tr><td><b>speak slowly</b></td><td>don’t speak too fast</td></tr>'
        '<tr><td><b>teach yourself</b>, <b>pick it up</b></td><td>learn through self-study; learn informally</td></tr></table></article>')
    writing = (
        '<article class="page" id="too-also"><span class="page-no">Учебник, с. 121</span><h2>Key words for writing: too, also, as well, as well as</h2>'
        '<div class="box"><p><b>As well, too and also all mean the same thing. However, the way we use as well and too is different from the way we use also.</b></p><hr>'
        '<p class="ex-line">I’m really into electronic music and I quite like jazz and hip-hop as well.<br>I’m really into electronic music and I quite like jazz and hip-hop too.<br>I’m really into electronic music and I also quite like jazz and hip-hop.</p></div>'
        '<p class="rule">' + " ".join(column(27, 0, "A:", "B:", split=56)[0:2]) + ' <small>(ключ)</small></p>'
        '<div class="box"><p><b>As well as is sometimes used to join two ideas instead of using and or but. It is often used along with as well, too and also.</b></p><hr>'
        '<p class="ex-line">As well as being really into electronic music, I quite like jazz and hip-hop too.<br>As well as working long hours, I also like going out and having fun.</p></div></article>')
    toc = ('<nav class="toc"><a href="#gr136">Question formation</a><a href="#gr137">Narrative tenses</a>'
           '<a href="#boxes">Правила из уроков</a><a href="#vocab">Vocabulary</a><a href="#too-also">Too / also / as well</a></nav>')
    return (toc + gr_page(136, "gr136", grammar_ref(136, (0, 100, 397, 1050)))
            + gr_page(137, "gr137", grammar_ref(137, (0, 100, 420, 1050)))
            + unit_boxes + vocab + writing)
