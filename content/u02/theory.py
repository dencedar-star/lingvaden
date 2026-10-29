"""Страница «Теория»: Grammar reference pp. 138–139 (из OCR) и правила из уроков юнита 02."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X
from .book import RESP

FIX[138] = [("She looks like a model!.", "She looks like a model!"), ("Ifeel a bit ill.", "I feel a bit ill."),
            ("1 was exhausted.", "I was exhausted."), ("02 EMOTIONS", "02 EMOTIONS")]
FIX[139] = [("1 live in Budapest.", "I live in Budapest."), ("(see - notice)", "(see = notice)"), ("(see -", "(see =")]

VERBS = ["agree", "believe", "belong", "depend", "disagree", "doubt", "forget", "like", "matter", "mean", "mind", "need",
         "own", "prefer", "realise", "seem", "suppose", "want"]
TABLE_OCR = ["agree believe belong depend disagree doubt", "forget like", "mind", "matter mean", "need",
             "prefer realise seem suppose want", "own"]


def build():
    g138 = (grammar_ref(138, (0, 100, 400, 505), heads=("be, look, seem, etc.",)) +
            grammar_ref(138, (400, 100, 794, 425), heads=("-ed / -ing adjectives",)))
    g139 = grammar_ref(139, (0, 100, 410, 1050), heads=("The present continuous", "Present simple and present continuous"),
                       skip=TABLE_OCR)
    table = '<div class="wordbox">' + "".join(f"<span>{v}</span>" for v in VERBS) + "</div>"
    # две синие строки подряд склеиваются в одно правило — разделяем и вставляем таблицу глаголов
    g139 = g139.replace('<p class="rule">Other verbs like this are: Some other verbs',
                        '<p class="rule">Other verbs like this are:</p>' + table + '<p class="rule">Some other verbs', 1)
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 14–19</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>be, look, seem etc <small>(p. 14)</small></h3>'
        '<div class="box"><p><b><i>Be, feel, look, seem,</i> and <i>sound</i> are all linking verbs that can be followed directly '
        'by an adjective.</b></p></div>'
        '<h3>-ing / -ed adjectives <small>(p. 17)</small></h3>'
        '<div class="box"><p><b>Some adjectives, including those ending in <i>-ing</i>, only describe things which cause a feeling:</b></p>'
        '<p class="ex-line">The film was so <i>boring</i> that I fell asleep.</p><hr>'
        '<p><b>The <i>-ed</i> and other adjectives in Vocabulary exercise A on p. 14 describe people’s feelings:</b></p>'
        '<p class="ex-line">I’m <i>exhausted</i>. I need to go to bed.</p></div>'
        '<h3>Present continuous / present simple questions <small>(p. 18)</small></h3>'
        '<div class="box"><p><b>Double questions are very common in English.</b></p><hr>'
        '<p class="ex-line">So what <i>are you doing</i> here? <i>Are you window shopping?</i><br>'
        'What <i>are you doing</i> on Friday? <i>Do you fancy</i> meeting?</p></div>'
        '<h3>Response expressions <small>(p. 15)</small></h3>'
        '<div class="box"><p><b>We use lots of short expressions to respond to news.</b></p><hr><p class="ex-line">' +
        " · ".join(b for _, b, _ in RESP) + '</p></div>'
        '<h3>Pronunciation: responding <small>(p. 15)</small></h3>'
        '<div class="box"><p><b>With positive responses our voice goes higher.</b></p><hr>'
        '<p><b>With negative responses our voice goes lower.</b></p></div>'
        '<h3>Making excuses <small>(p. 19)</small></h3>'
        '<div class="box"><p><b>We often use the present simple or continuous to explain why we can’t or don’t want to do '
        'something.</b></p><hr><p class="ex-line">I’m afraid I can’t. I play badminton on Fridays.<br>I’m going away for the weekend.</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 15)</small></h4><p><b><i>How come?</i></b> — '
        'People often use <i>How come?</i> instead of <i>Why?</i></p><p><i>A: I can’t come to your wedding, I’m afraid.<br>'
        'B: Oh what a shame. How come?<br>A: I’ve got an exam that day.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 14)</small></h4><p><i>She expected to get a better mark.<br>'
        'I expected London to be more modern.<br>I didn’t expect to have so much homework.<br>'
        'We didn’t expect it to take so long.<br>We didn’t expect you to be so early.</i></p></div></div>'
        "</article>")
    feel = ["exhausted", "worried", "fed up", "confused", "terrible", "relaxed", "stressed", "in a good / bad mood", "upset",
            "furious", "annoyed", "disappointed", "pleased", "down", "guilty"]
    coll = [("relaxing", "holiday / bath / atmosphere / place / time"), ("annoying", "habit / person / noise / problem / spam"),
            ("exciting", "city / new development / discovery / opportunity"),
            ("inspiring", "teacher / speech / story / book / film / video clip"),
            ("confusing", "instructions / message / grammar / explanation"),
            ("disappointing", "response / news / loss / result / game / sales")]
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 14, 16–17</span><h2>Vocabulary</h2>'
             '<h3>Feelings <small>(p. 14)</small></h3><div class="wordbox">' + "".join(f"<span>{w}</span>" for w in feel) + "</div>"
             '<h3>Adjective collocations <small>(p. 17, по ключу)</small></h3><table class="voc"><tr><th>Adjective</th><th>Nouns</th></tr>' +
             "".join(f"<tr><td><b>{a}</b></td><td>{n}</td></tr>" for a, n in coll) + "</table>"
             '<h3>Adjective + noun from the article <small>(p. 16, по ключу)</small></h3><div class="wordbox">' +
             "".join(f"<span>{a} {n}</span>" for a, n in zip(X.ADJ_KEY, X.ADJ_NOUNS)) + "</div></article>")
    writing = ('<article class="page" id="emails"><span class="page-no">Учебник, с. 122–123</span><h2>Writing: short emails</h2>'
               '<h3>Explaining why you are writing</h3>'
               '<div class="box"><p><b>We generally begin emails with a line explaining why we are writing. To people we already '
               'know, we often begin with sentence starters like this:</b></p><hr><p class="ex-line">Just a quick / short one / note / '
               'email ' + " / ".join(X.STARTERS) + '</p></div>'
               '<h3>Leaving out words</h3>'
               '<div class="box"><p><b>When we add information to a sentence using <i>and / or</i>, we often leave words out if they '
               'have already been used. We assume the missing words are understood by the reader.</b></p><hr>'
               '<p class="ex-line">I hope this is OK with you and (I hope this) won’t cause too many problems.</p></div>'
               '<h3>Ending emails</h3>'
               '<div class="box"><p><b>The way we end emails depends on who we are writing to. Some endings are more common for '
               'formal emails; some are more common for informal ones.</b></p></div>'
               '<table class="voc"><tr><th>Emails</th><th>Endings (ключ, suggested answers)</th></tr>'
               '<tr><td>business</td><td>Kind regards, Yours faithfully, Yours sincerely, Yours</td></tr>'
               '<tr><td>acquaintances</td><td>Many thanks, All the best</td></tr>'
               '<tr><td>close friends / family</td><td>Love, Lots of love, Cheers for now</td></tr></table></article>')
    toc = ('<nav class="toc"><a href="#gr138">be, look, seem · -ed / -ing</a><a href="#gr139">Present continuous</a>'
           '<a href="#boxes">Правила из уроков</a><a href="#vocab">Vocabulary</a><a href="#emails">Short emails</a></nav>')
    return toc + gr_page(138, "gr138", g138) + gr_page(139, "gr139", g139) + unit_boxes + vocab + writing
