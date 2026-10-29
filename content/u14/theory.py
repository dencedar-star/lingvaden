"""Страница «Теория»: Grammar reference p. 153 и правила из уроков юнита 14.
Справочник с. 153 состоит в основном из списков слов, поэтому собран вручную (правила + списки), а не из OCR."""
from grammar import gr_page
from . import shared as X


def wb(ws):
    return X.wordbox(ws)


def build():
    g153 = (
        '<h3><i>-ing</i> forms</h3>'
        '<p class="rule"><i>-ing</i> forms are also known as gerunds. They can be used as the subject or object of a clause.</p>'
        '<p class="egs"><i>Using energy-efficient bulbs saves a lot of electricity.<br>If you ask me, being short is a '
        'disadvantage in our society.</i></p>'
        '<p class="rule">Use <i>-ing</i> forms following prepositions.</p>'
        '<p class="egs"><i>I felt a bit sick after eating so much.<br>We were all involved in organising the event.<br>'
        'I just don’t agree with eating meat.</i></p>'
        '<p class="rule">These adjective + preposition combinations are followed by <i>-ing</i> forms:</p>' +
        wb(["pleased about / at", "upset about", "sorry about / for", "useless at", "involved in", "bored of", "capable of",
            "scared of", "wrong with"]) +
        '<p class="rule">The adjective <i>be / get used to</i> is followed by <i>-ing</i>.</p>'
        '<p class="rule">These verb + preposition combinations are often followed by <i>-ing</i> forms:</p>' +
        wb(["think of", "blame s.o. for", "complain about", "ask about", "succeed in", "push s.o. into", "apologise for",
            "cope with"]) +
        '<p class="rule">Several phrasal verbs are also followed by an <i>-ing</i> form. For example:</p>' +
        wb(["carry on", "take up", "look forward to", "end up", "give up"]) +
        '<h3><i>to</i>-infinitives</h3>'
        '<p class="rule">We use a <i>to</i>-infinitive to explain the reason or purpose of doing something.</p>'
        '<p class="egs"><i>I need to go to the bank to sort out a problem.<br>I burned a CD of my own music to give to my '
        'mum.</i></p>'
        '<p class="rule">They are also used after some adjectives without a preposition, and following <i>too</i> or '
        '<i>enough</i>.</p>'
        '<p class="egs"><i>It’s important to recycle as much as possible.<br>I’m too busy to think about that now.<br>'
        'We’re still not doing enough to stop global warming.</i></p>'
        '<h3><i>-ing</i> forms or <i>to</i>-infinitive?</h3>'
        '<p class="rule">Both <i>-ing</i> forms and <i>to</i>-infinitives can follow verbs with no preposition. There are no '
        'fixed rules.</p>'
        '<p class="egs"><i>He always avoids doing the washing up.<br>We’ve arranged to meet at nine outside the station.</i></p>'
        '<p class="rule">Other verbs that can be followed by <i>-ing</i>:</p>' +
        wb(["be caught", "can’t stand", "deny", "fancy", "feel like", "involve", "mind", "miss", "recommend", "risk", "spend",
            "suggest"]) +
        '<p class="rule">Other verbs that can be followed by <i>to</i>-infinitive:</p>' +
        wb(["agree", "arrange", "ask", "decide", "deserve", "fail", "hope", "intend", "learn", "manage", "persuade", "plan",
            "promise", "refuse", "threaten", "want"]))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 98–103</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3><i>-ing</i> forms and <i>to</i>-infinitives <small>(p. 103)</small></h3>'
        '<div class="box">' + "".join(f"<p>{l}) {r}</p>" for l, r in zip("abcde", X.RULES)) +
        '<hr><p class="ex-line">What’s wrong with just putting them in some water? (a)<br>You still need the cash to install the '
        'panels. (d)<br>I did consider getting one. (b)<br>If you want to have the perfect boiled egg, … (e)<br>Using this is more '
        'energy-efficient than boiling eggs. (c)</p></div>'
        '<h3>Abbreviations <small>(p. 99)</small></h3>'
        '<div class="box"><p><b>Abbreviations are formed using the first letters of each word in the name of something. When we '
        'say abbreviations, we usually stress each individual letter. However, occasionally we say them as one word.</b></p></div>'
        '<h3>Responding to advice <small>(p. 99)</small></h3>'
        '<div class="box"><p class="ex-line">A: Have you tried rebooting? / checked the connection?<br>B: Yeah, but it didn’t '
        'work / but it made no difference / but it didn’t do any good / but I didn’t have any success.<br>B: No, I haven’t / not '
        'yet.<br>A: Well, try that. Otherwise, I can’t really help / you’re best taking it to a shop / you’ll have to get a new '
        'one / I don’t know what else you can do.</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 100)</small></h4><p><b><i>hot</i></b> — when '
        'we describe something as <i>hot</i>, it means we think it is very exciting and interesting – because it is so new.</p>'
        '<p><i>Their new web phone is the hot new thing this winter.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 99)</small></h4><p><i>Have you tried re-booting it at all?<br>'
        'I didn’t learn anything at all on that course!<br>He hardly ate anything at all.<br>I hardly know her at all, to be '
        'honest.</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 98, 100, 102</span><h2>Vocabulary</h2>'
             '<h3>Computers <small>(p. 98)</small></h3>' + wb(X.PC) +
             '<p class="ex-line">scan something in · plug something into a socket · drop-down menu · move the cursor over the '
             'image · a three-pin plug · external hard drive · delete a file · the screen kept freezing · trip over a cable · '
             'the printer ran out of ink · spill something all over the keyboard · right-click on the mouse</p>'
             '<h3>Talking about markets <small>(p. 100)</small></h3><p class="ex-line">The market is almost saturated / '
             'completely saturated / growing steadily / booming / in decline / still growing / fairly steady / huge / tiny / '
             'big business / dead / bigger / smaller than it used to be.</p>'
             '<h3>Technology, programs and gadgets <small>(p. 102)</small></h3>' + wb(X.GADGET_BOX) + "</article>")
    writing = ('<article class="page" id="review"><span class="page-no">Учебник, с. 134–135</span><h2>Writing: a review</h2>'
               '<h3>Describing films</h3>' + wb(X.FILM_ADJ + ["well-chosen", "superbly acted", "well-written",
                                                              "beautifully filmed", "brilliantly directed"]) +
               '<h3>While and during</h3><div class="box"><p><b><i>during</i> + noun</b></p><p class="ex-line">… during the '
               'Second World War.</p><hr><p><b><i>while</i> + clause</b></p><p class="ex-line">While they are there, the father '
               'distracts the boy …</p></div>'
               '<h3>Adding information after the noun</h3><div class="box"><p><b>We often make a text shorter by adding '
               'information after a noun using an <i>-ed / -ing</i> participle, a prepositional phrase, or relative clause.</b>'
               '</p><p class="ex-line">This is a strangely uplifting film directed by and starring Roberto Benigni.</p></div>'
               "</article>")
    toc = ('<nav class="toc"><a href="#gr153">-ing forms and to-infinitives</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a><a href="#review">A review</a></nav>')
    return toc + gr_page(153, "gr153", g153) + unit_boxes + vocab + writing
