"""Страница «Письмо»: Writing 01 Introducing yourself, pp. 120–121."""
from lib import S, EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL, INS
from ocrtext import paras, fixed, FIX
from keys import column
from . import shared as X

IMG_DIR = "../assets/img/unit01/"
ACTS = ["aerobics", "kick-boxing", "waterskiing", "trekking", "karaoke", "gardening"]
ACT_KEY = ["karaoke", "trekking", "waterskiing", "kick-boxing", "aerobics", "gardening"]  # ключ pp. 120–121
BOX = ["about", "also", "as well", "in", "on", "quite", "really", "to", "which", "who"]
EMAIL_KEY = ["on", "to", "which", "who", "really", "quite", "also", "as well", "about", "in"]

# Пунктир пропусков в скане «съедает» соседние буквы — правим по участкам, пропуски помечаем {n}
FIX[120] = [
    ("friend..... .... the", "friend {1} the"), ("writing ‘............. you", "writing {2} you"),
    ("Chile, m.... in case", "Chile, {3} in case"), ("Peru.I am", "Peru. I am"),
    ("sister,’..................... is", "sister, {4} is"),
    ("instructor.|........... ...... love surfing. swimming", "instructor. I {5} love surfing, swimming"),
    ("and... ike football •as well", "and I {6} like football as well"),
    ("movies. 1... eally like", "movies. I {7} really like"), ("into - electronic", "into electronic"),
    ("hip-hop “.........", "hip-hop {8}."), ("more yourself", "more {9} yourself"),
    ("have.’...................", "have a lot {10} common."),
]


def email():
    ps = [fixed(120, p) for p in paras(120, (410, 650, 760, 990), indent=10**6, gap=1.2)]
    body = ps[1]
    for i, k in enumerate(EMAIL_KEY, 1):
        body = body.replace("{%d}" % i, f"<sup>{i}</sup>" + S(k, BOX))
    return ('<div class="story"><p><b>To:</b> kaykoolkaye@hotmail.ml<br><b>Subject:</b> Re: Hello there</p>'
            f"<p>{ps[0]}</p><p>{body}</p><p>{ps[-1]}</p></div>")


def kay():
    t = fixed(120, " ".join(paras(120, (400, 300, 780, 412), indent=10**6, gap=10**6)))
    return ('<div class="story" style="display:flex;gap:14px;align-items:flex-start">'
            f'<img src="{IMG_DIR}p120-kay.jpg" alt="Kay" style="width:84px;border-radius:8px">'
            f"<div><p><b>Kay</b></p><p>{t}</p></div></div>")


def build():
    spk = SEC("Speaking", "", EX("w-s", "", "Work in pairs. Discuss these questions:", UL([
        "Have you ever had a pen friend or have you ever written to anybody in a different country?",
        "How did you get in touch?", "What can you remember about them?"])))
    pics = '<div class="pics">' + "".join(
        f'<figure><img src="{IMG_DIR}p120-act{i}.jpg" alt="" loading="lazy"><figcaption>{i} {S(k, ACTS)}</figcaption></figure>'
        for i, k in enumerate(ACT_KEY, 1)) + "</div>"
    voc = SEC("Vocabulary", "Free-time activities",
              EX("w-va", "A", "Match the words in the box to the pictures.",
                 '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ACTS) + "</div>" + pics) +
              EX("w-vb", "B", "Work in groups of three. Discuss these questions:", UL([
                  "Which of these activities have you done? When? Did you enjoy them?",
                  "Are there any you would like to try sometime in the future?",
                  "Are there any you really do not want to try? Why not?"])))
    wr = SEC("Writing", "Introducing yourself",
             EX("w-wa", "A", "Read this Internet advert from a person looking for pen friends. Would you write to Kay? Why? / Why not?", kay()) +
             EX("w-wb", "B", "Below is a reply to Kay. Complete the message with the words in the box.",
                '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in BOX) + "</div>" + email()) +
             EX("w-wc", "C", "Work in pairs. How much do you have in common with Fernanda?", ""))
    box1 = ('<div class="box"><p><b>As well, too and also all mean the same thing. However, the way we use as well and too is '
            'different from the way we use also.</b></p><hr><p class="ex-line">I’m really into electronic music and I quite like '
            'jazz and hip-hop as well.<br>I’m really into electronic music and I quite like jazz and hip-hop too.<br>'
            'I’m really into electronic music and I also quite like jazz and hip-hop.</p></div>')
    box2 = ('<div class="box"><p><b>As well as is sometimes used to join two ideas instead of using and or but. It is often used '
            'along with as well, too and also.</b></p><hr><p class="ex-line">As well as being really into electronic music, I quite '
            'like jazz and hip-hop too.<br>As well as working long hours, I also like going out and having fun.</p></div>')
    ins = [
        ("I’m really into computers, but I like going out and having fun too.", "too"),
        ("I like reading and writing and I also do photography.", "also"),
        ("I go to the theatre quite a lot, but I like staying in and reading as well.", "as well"),
        ("I really love gardening and I’m also into yoga.", "also"),
        ("I do a lot of kick-boxing and I go running a lot as well.", "as well"),
        ("I’m studying Art History and I’m also doing a French course at the moment.", "also"),
    ]
    ckey = [r for r in column(27, 0, "C:", "Grammar:", split=56)]
    cks, cur = [], ""
    for r in ckey:
        if r[:1].isdigit() and cur:
            cks.append(cur); cur = r
        else:
            cur = (cur + " " + r).strip()
    cks.append(cur)
    akey = " ".join(column(27, 0, "A:", "B:", split=56)[0:2])
    kw = SEC("Key words for writing", "Too, also, as well, as well as", box1 +
             EX("w-ka", "A", "Which patterns can you see in the sentences above?", REVEAL(akey, "Ответ (ключ)")) +
             EX("w-kb", "B", "Complete these sentences by putting the words in brackets into the correct place. "
                '<span style="font-weight:400">Нажмите на место между словами, куда нужно вставить слово.</span>',
                OL([INS(s, w) for s, w in ins])) + box2 +
             EX("w-kc", "C", "Rewrite 1–6 in exercise B so that each sentence starts with <i>As well as</i>.",
                REVEAL(OL([c[2:] for c in cks]), "Ответы (ключ)")))
    gr = SEC("Grammar", "Common questions", X.writing_order("w-ga") +
             EX("w-gb", "B", "Work in pairs. Ask and answer the questions in exercise A.", ""))
    pr = SEC("Practice", "",
             EX("w-pa", "A", "You are going to write a message to someone you would like to be pen friends with. The message "
                "should be around 150 words long. Before you start, underline any language from these pages you want to use. "
                "Try to remember it.", "") +
             EX("w-pb", "B", "Close your book and write the message. When you have finished, check that you remembered the "
                "underlined language correctly.",
                '<div class="writer" data-id="u01-message"><textarea placeholder="Dear …"></textarea><div class="cnt"></div></div>'))
    p120 = PAGE_BOX(120, IMG(IMG_DIR + "p120-banner.jpg", "01 Writing — Introducing yourself") +
                    '<div class="cols"><div>' + spk + voc + '</div><div>' + wr + "</div></div>")
    p121 = PAGE_BOX(121, '<div class="cols"><div>' + kw + '</div><div>' + gr + pr +
                    IMG(IMG_DIR + "p121-kickboxing.jpg", "") + "</div></div>")
    return p120 + p121
