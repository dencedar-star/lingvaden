"""Страница «Теория»: Grammar reference pp. 142–143 (из OCR) и правила из уроков юнита 04."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX[142] = [("Whenever | get", "Whenever I get"), ("but / hardly", "but I hardly"), (" - ", " – ")]
FIX[143] = [("drive during for", "drive <s>during</s> for"), ("walking since from", "walking <s>since</s> from"), (" - ", " – ")]

REPLIES = [("(Yes / Yeah)", "<i>All the time.</i> Maybe three or four times a week."),
           ("(Yes / Yeah)", "<i>A lot.</i> Maybe two or three times a month."),
           ("(Yes / Yeah)", "<i>Quite often / Quite a lot.</i> I probably go once or twice a week."),
           ("(Yes / Yeah)", "<i>Sometimes</i> – it depends how I feel."),
           ("(No)", "<i>Not that often.</i> I don’t have much spare time."),
           ("(No)", "<i>Hardly ever.</i> The last time I went was about three years ago."),
           ("(No)", "<i>Never.</i> I’m just not interested.")]


def _fixes(html, pairs):
    for a, b in pairs:
        html = html.replace(a, b)
    return html


def build():
    g142 = (grammar_ref(142, (25, 95, 335, 312)) +
            '<table class="voc">' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in REPLIES) + "</table>" +
            '<p class="rule">Do not use <i>Yes / No</i> when you answer <i>How often</i> questions.</p>'
            '<p class="egs"><b>Say:</b> <i>Once a month / three times a week</i><br><b>Say:</b> <i>Once every two months / Once '
            'every three weeks</i><br><b>Say small numbers first:</b> <i>once or twice / two or three times</i></p>' +
            grammar_ref(142, (25, 628, 335, 840)) + grammar_ref(142, (395, 95, 706, 445)))
    g143 = _fixes(grammar_ref(143, (85, 110, 405, 1045)) + grammar_ref(143, (445, 110, 745, 180)), [
        ('<p class="egs"><i>Other tenses</i></p><h3>Use the present tense to talk about the typical duration</h3>'
         '<p class="rule">of regular activities.</p>',
         '<h3>Other tenses</h3><p class="rule">Use the present tense to talk about the typical duration of regular activities.</p>'),
        ('<p class="egs"><i>We also use during + noun to mean throughout a time period.</i></p>',
         '<p class="rule">We also use <i>during</i> + noun to mean throughout a time period.</p>'),
        ('<h3>Until or till shows the point at which a period</h3><p class="rule">finished.</p>',
         '<p class="rule"><i>Until</i> or <i>till</i> shows the point at which a period finished.</p>')])
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 26–31</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>Frequency <small>(p. 27)</small></h3>'
        '<div class="box"><p><b>We can ask about frequency in the present with these patterns:</b></p><hr>'
        '<p class="ex-line"><i>Do you</i> + verb + <i>much / a lot?</i><br><i>How often do you</i> + verb?<br>'
        '<i>Do you ever</i> + verb?</p></div>'
        '<h3>Duration <small>(p. 29)</small></h3>'
        '<div class="box"><p><b>Rules</b></p><p>Use <b>for</b> (not <i>during</i>) with periods of time in the past and present.</p>'
        '<p>Use <b>since</b> to show the <i>start</i> of a period of time from the past to now.</p>'
        '<p>Use the <b>present perfect (continuous)</b> tense to talk about periods including now.</p>'
        '<p>Use the <b>past</b> tense to talk about periods of time which are finished.</p></div>'
        '<h3>Connected speech <small>(p. 26)</small></h3>'
        '<div class="box"><p><b>Hearing words in groups can be confusing. Fluent speakers join words together – especially when '
        'final consonants are followed by vowels.</b></p><p class="ex-line">Not as‿much as‿I used to</p><hr><p><b>They also '
        'don’t pronounce certain letters – such as when final consonants are followed by a word beginning with another '
        'consonant.</b></p><p class="ex-line">No<s>t</s> as much as I use<s>d</s> to</p></div>'
        '<h3>Auxiliaries <small>(p. 29)</small></h3>'
        '<div class="box"><p><b><i>How long</i> is used with other tenses as well as the past simple and the present perfect '
        'continuous. It is easy to mishear these questions because the auxiliary verb is pronounced very softly.</b></p>'
        '<p class="ex-line">' + "<br>".join(X.HOW_LONG) + '</p></div>'
        '<h3>Are you any good? <small>(p. 27)</small></h3>'
        '<div class="box"><p class="ex-line">A: So are you any good?<br>B: I’m OK. I’m quite good in defence, but I’m useless at '
        'shooting. I think the last time I scored a goal was about three years ago.</p><hr><p><b>No, I’m useless · No, not '
        'really · I’m OK · Yeah, quite good</b> — and then explain the short answer.</p></div>'
        '<h3>Music, films and books <small>(p. 30)</small></h3>'
        '<div class="box"><p><b>We often move from more general questions to more specific.</b></p><p class="ex-line">' +
        "<br>".join(t for t, k in sorted(X.MUSIC_CONV, key=lambda c: c[1])) + '</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 28)</small></h4><p><b><i>kind of</i></b> — '
        'People often use <i>kind of</i> to modify an adjective or a verb. It means <i>more or less, but not exactly</i>.</p>'
        '<p><i>He’s been on TV a few times, so he’s kind of famous now!<br>I didn’t really plan to do it. It just kind of '
        'happened!</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 27)</small></h4><p><i>Nearly every day, unless I’m really busy.<br>'
        'Most weekends, unless it’s raining.<br>I usually play on Saturdays, unless I’m away on business.<br>I never missed a '
        'lesson, unless I was really ill.<br>He used to see us every day, unless we were away.</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 26, 28, 30</span><h2>Vocabulary</h2>'
             '<h3>Evening and weekend activities <small>(p. 26)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{s}</td><td>{' / '.join(o for o in opts if o != k)}</td></tr>" for s, opts, k in X.ENDINGS) +
             "</table><h3>Problems and sports <small>(p. 28)</small></h3>" + X.wordbox(X.PROB_BOX) +
             '<h3>Music <small>(p. 30)</small></h3><p class="ex-line">catchy · repetitive · heavy · soft · sentimental · '
             'commercial · moving · bland · uplifting · depressing</p></article>')
    writing = ('<article class="page" id="requests"><span class="page-no">Учебник, с. 126–127</span><h2>Writing: making requests</h2>'
               '<div class="box"><p><b>When we ask people to do things for us, we use modal verbs like <i>can</i> and '
               '<i>could</i>. We also sometimes use past tenses to sound polite. However, we also make questions longer using '
               'typical sentence starters.</b></p><hr><p><i>I was wondering if you could help me</i> is more polite than <i>I '
               'wonder if you can help me</i>. Less polite than either is <i>Can you help me?</i></p></div>'
               '<p class="ex-line">I was wondering if you could …?<br>Do you think you could …?<br>Is there any way you could …?<br>'
               'Could you do me a favour and …?</p>'
               '<h3><i>as</i> = because</h3><div class="box"><p class="ex-line">As your English is so good, could you do me a big '
               'favour and look through it carefully to check it’s OK?<br>I’d be really grateful as I’ll have loads of luggage.'
               '</p></div><h3><i>as … as</i> expressions</h3><p class="ex-line">' +
               " · ".join(a for _, a in X.AS_ORDER) + "</p></article>")
    toc = ('<nav class="toc"><a href="#gr142">Frequency</a><a href="#gr143">Duration</a>'
           '<a href="#boxes">Правила из уроков</a><a href="#vocab">Vocabulary</a><a href="#requests">Requests</a></nav>')
    return toc + gr_page(142, "gr142", g142, "04 Interests") + gr_page(143, "gr143", g143) + unit_boxes + vocab + writing
