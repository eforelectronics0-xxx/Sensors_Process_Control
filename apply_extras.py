# -*- coding: utf-8 -*-
"""Splice extras_content.EXTRAS into build_a.py / build_b.py bodies.

Budget: aim final full-page words ~1160 (range 1000-1200).
Every topic gets all four sections; counts scale with remaining budget.
Idempotent: skips bodies already containing <!--EXTRAS-->.
"""
import io, re
import extras_content as EX

TARGET = 1160
MARK = "<!--EXTRAS-->"

# current full-page word counts measured after figure splice
CURRENT = {
    1: 818, 2: 947, 3: 785, 4: 615, 5: 640, 6: 657, 7: 616, 8: 681,
    9: 741, 10: 594, 11: 737, 12: 871, 13: 738, 14: 532, 15: 523,
    16: 1037, 17: 593, 18: 675, 19: 759, 20: 781, 21: 1025, 22: 770,
    23: 898, 24: 911, 25: 680, 26: 865, 27: 973,
}


def words(html):
    return len(re.sub(r"<[^>]+>", " ", html).split())


def sentences(text, n):
    parts = re.split(r"(?<=[.!?]) ", text.strip())
    return " ".join(parts[:n])


def num_html(d, idx):
    steps = " ".join(d["steps"])
    return ('<div class="formula"><span class="b">Problem %d.</span> %s</div>\n'
            '<p class="q"><span class="b">Solution.</span> %s '
            '<span class="hl">%s</span></p>' % (idx, d["given"], steps, d["ans"]))


def viva_html(pairs, start=1):
    out = []
    for i, (q, a) in enumerate(pairs, start):
        out.append('<p class="q"><span class="b">Q%d. %s</span><br>'
                   '<span class="o">A.</span> %s</p>' % (i, q, a))
    return "\n".join(out)


def spec_html(rows):
    lines = ['<div class="tw"><table>']
    for j, row in enumerate(rows):
        cell = "th" if j == 0 else "td"
        cells = "".join("<%s>%s</%s>" % (cell, c, cell) for c in row)
        lines.append("<tr>%s</tr>" % cells)
    lines.append("</table></div>")
    return "\n".join(lines)


def compose(current, x):
    B = TARGET - current
    nums = x.get("num", [])
    vivas = list(x.get("viva", []))
    summ_full = x.get("summ", "")
    spec_full = list(x.get("spec", []))
    prose_list = list(x.get("prose", []))
    heads = ["Worked numericals", "Viva questions and answers",
             "Summary", "Specifications at a glance"]

    def cost(n_num, n_viv, summ_html, n_spec, n_prose):
        h = 16  # four h2 blocks incl. number spans
        if n_num:
            h += sum(words(num_html(d, i + 1)) for i, d in enumerate(nums[:n_num]))
        if n_viv:
            h += words(viva_html(vivas[:n_viv]))
        h += words(summ_html)
        if n_spec:
            h += words(spec_html(spec_full[:n_spec]))
        h += sum(words(p) for p in prose_list[:n_prose])
        return h

    def summ_at(n_sent):
        if n_sent >= 99:
            return summ_full
        return '<p class="q">%s</p>' % sentences(summ_full, n_sent)

    n_num = 1 if nums else 0
    n_viv = min(3, len(vivas))
    n_spec = min(4, len(spec_full))
    n_prose = 0
    summ_sent = 2
    summ_use = summ_at(summ_sent)

    # floors: if even floor exceeds budget, drop to 2 viva once
    if cost(n_num, n_viv, summ_use, n_spec, 0) + 16 > B and n_viv > 2:
        n_viv = 2

    while True:
        grew = False
        if n_viv < len(vivas) and cost(n_num, n_viv + 1, summ_use, n_spec, n_prose) + 16 <= B:
            n_viv += 1; continue
        if summ_sent < 99:
            nxt = summ_full if (sentences(summ_full, summ_sent + 1) == summ_full or
                                words(summ_full) - words(sentences(summ_full, summ_sent)) < 15) \
                else None
            cand = summ_full if nxt is not None and summ_sent + 1 >= count_sents(summ_full) \
                else sentences(summ_full, summ_sent + 1)
            if cand != summ_use and cost(n_num, n_viv, '<p class="q">%s</p>' % cand, n_spec, n_prose) + 16 <= B:
                summ_use = '<p class="q">%s</p>' % cand
                summ_sent = summ_sent + 1 if cand != summ_full else 99
                continue
            elif summ_full != sentences(summ_full, summ_sent) and \
                    cost(n_num, n_viv, '<p class="q">%s</p>' % summ_full, n_spec, n_prose) + 16 <= B:
                summ_use = '<p class="q">%s</p>' % summ_full
                summ_sent = 99
                continue
        if n_num < len(nums) and cost(n_num + 1, n_viv, summ_use, n_spec, n_prose) + 16 <= B:
            n_num += 1; continue
        if n_spec < len(spec_full) and cost(n_num, n_viv, summ_use, n_spec + 1, n_prose) + 16 <= B:
            n_spec += 1; continue
        if n_prose < len(prose_list) and cost(n_num, n_viv, summ_use, n_spec, n_prose + 1) + 16 <= B:
            n_prose += 1; continue
        break

    prose_html = "\n".join('<p class="q">%s</p>' % p for p in prose_list[:n_prose])
    return dict(prose=prose_html, nums=nums[:n_num], vivas=vivas[:n_viv],
                summ=summ_use, spec=spec_full[:n_spec], heads=heads,
                total=cost(n_num, n_viv, summ_use, n_spec, n_prose))


def count_sents(t):
    return len(re.split(r"(?<=[.!?]) ", t.strip()))


def render_block(next_no, sel):
    h2 = '<h2><span class="no">%d</span>%s</h2>\n'
    out = []
    n = next_no
    if sel["prose"]:
        out.append(sel["prose"])
    out.append(h2 % (n, sel["heads"][0])); n += 1
    for i, d in enumerate(sel["nums"], 1):
        out.append(num_html(d, i))
    out.append(h2 % (n, sel["heads"][1])); n += 1
    out.append(viva_html(sel["vivas"]))
    out.append(h2 % (n, sel["heads"][2])); n += 1
    out.append(sel["summ"])
    out.append(h2 % (n, sel["heads"][3])); n += 1
    out.append(spec_html(sel["spec"]))
    return "\n".join(out) + "\n"


def max_h2_no(text):
    nums = [int(m) for m in re.findall(r'<h2><span class="no">(\d+)</span>', text)]
    return max(nums) if nums else 0


def scan_append_end(s, open_paren):
    """open_paren points at '(' of B.append(. Returns (inner_slice, insert_pos)."""
    d = 0; j = open_paren
    while True:
        c = s[j]
        if c == "(":
            d += 1
        elif c == ")":
            d -= 1
            if d == 0:
                return (open_paren + 1, j), j  # inner, insert before ')'
        elif c in "\"'":
            q = c; j += 1
            while s[j] != q:
                j += 2 if s[j] == "\\" else 1
        j += 1


def scan_assign_end(s, start):
    """start = index just after '=' of B[k] = . Returns (inner_start, insert_pos)."""
    k = start
    last = None
    while True:
        save = k
        while k < len(s) and s[k] in " \t\n":
            k += 1
        if k < len(s) and s[k] == "+":
            k += 1
            continue
        if s.startswith('"""', k):
            k2 = s.find('"""', k + 3)
            assert k2 > 0, "unterminated string"
            k = k2 + 3
            last = k
            continue
        if s.startswith('figures_core.render', k):
            d = s.index("(", k)
            dd = 0; j = d
            while True:
                c = s[j]
                if c == "(":
                    dd += 1
                elif c == ")":
                    dd -= 1
                    if dd == 0:
                        break
                j += 1
            k = j + 1
            last = k
            continue
        pos = last if last is not None else save
        return start, pos


def patch(fname, start_topic, mode):
    s = io.open(fname, encoding="utf-8").read()
    spans = []
    if mode == "append":
        for m in re.finditer(r"B\.append\(", s):
            i = s.index("(", m.start())
            (a, b), pos = scan_append_end(s, i)
            spans.append((a, b, pos))
    else:
        for m in re.finditer(r"B\[(\d+)\]\s*=\s*", s):
            a, pos = scan_assign_end(s, m.end())
            b = pos
            spans.append((a, b, pos))

    edits = []
    idx = 0
    for a, b, pos in spans:
        topic = start_topic + idx
        idx += 1
        inner = s[a:b]
        if MARK in inner:
            print("  topic %d already done" % topic)
            continue
        if topic not in EX.EXTRAS:
            print("  topic %d MISSING extras" % topic)
            continue
        sel = compose(CURRENT[topic], EX.EXTRAS[topic])
        nxt = max_h2_no(inner) + 1
        blk = render_block(nxt, sel)
        add = words(blk)
        final = CURRENT[topic] + add
        flag = ""
        if final > 1200:
            flag = "  ** OVER"
        elif final < 1000:
            flag = "  ** UNDER"
        print("  topic %2d: C=%4d + %3d -> %4d%s" % (topic, CURRENT[topic], add, final, flag))
        frag = ' + """\n' + MARK + '\n' + blk + '"""\n'
        if mode == "append":
            edits.append((pos, pos, frag))  # before ')': handled below
        else:
            edits.append((pos, pos, frag))

    # apply reverse (append inserts BEFORE the closing paren, i.e. at pos)
    for pos0, _, frag in reversed(edits):
        if mode == "append":
            s = s[:pos0] + frag.rstrip("\n") + s[pos0:]
        else:
            s = s[:pos0] + frag + s[pos0:]
    io.open(fname, "w", encoding="utf-8").write(s)
    print("patched", fname, "-", len(edits), "topics")


if __name__ == "__main__":
    print("build_a (topics 1-11):")
    patch("build_a.py", 1, "append")
    print("build_b (topics 12-27):")
    patch("build_b.py", 12, "assign")
