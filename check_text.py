# -*- coding: utf-8 -*-
"""
check_text.py -- text-overlap and off-canvas audit for every SVG on the site.

For every <svg> in every *.html (and for any standalone *.svg) it resolves
transforms, estimates each <text> box (width factor 0.52 = the conservative
factor circuit.py also uses) and reports:

  OVERLAP   two text boxes intersect   (checked at 0.52 / 0.50 / 0.42 / 0.36)
  OFFPAGE   a text box leaves the viewBox (would be clipped)

Because every edge of a text box moves inward as the width factor shrinks,
a clean result at 0.52 implies a clean result at all smaller factors; the
smaller factors are still printed so a suspicious hit can be confirmed.

Exit code 1 if anything overlaps or leaves the page at wf = 0.52.
"""
import glob
import itertools
import os
import re
import sys
import xml.etree.ElementTree as ET

FACTORS = (0.52, 0.50, 0.42, 0.36)
SVG_RE = re.compile(r"<svg\b.*?</svg>", re.S | re.I)
TF_RE = re.compile(r"translate\(\s*([-\d.]+)[ ,]+([-\d.]+)\s*\)")


def texts_with_transforms(block):
    """[(x, y, size, anchor, body)] in root coordinates."""
    root = ET.fromstring(block)
    vb = (root.get("viewBox") or "0 0 760 440").split()
    vw, vh = float(vb[2]), float(vb[3])
    out = []

    def walk(el, ox, oy):
        for ch in el:
            tr = ch.get("transform") or ""
            dx = dy = 0.0
            m = TF_RE.search(tr)
            if m:
                dx, dy = float(m.group(1)), float(m.group(2))
            tag = ch.tag.split("}")[-1]
            if tag == "text":
                body = "".join(ch.itertext())
                if body.strip():
                    out.append((ox + dx + float(ch.get("x", 0)),
                                oy + dy + float(ch.get("y", 0)),
                                float(ch.get("font-size", 16)),
                                ch.get("text-anchor", "start"), body))
            elif tag != "defs":
                walk(ch, ox + dx, oy + dy)

    walk(root, 0, 0)
    return out, vw, vh


def boxes(texts, wf):
    bx = []
    for x, y, sz, anc, body in texts:
        w = len(body) * sz * wf
        if anc == "middle":
            x0 = x - w / 2.0
        elif anc == "end":
            x0 = x - w
        else:
            x0 = x
        bx.append((x0, y - sz * 0.72, x0 + w, y + sz * 0.18, body))
    return bx


def audit_block(block, label):
    """returns list of problem strings for one <svg> block"""
    try:
        texts, vw, vh = texts_with_transforms(block)
    except ET.ParseError as e:
        return (["UNPARSEABLE SVG -> %s" % e], {})
    probs = []
    per_factor = {}
    for wf in FACTORS:
        bx = boxes(texts, wf)
        hits = []
        for a, b in itertools.combinations(bx, 2):
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                hits.append('"%s" x "%s"' % (a[4].strip()[:28], b[4].strip()[:28]))
        per_factor[wf] = hits
    bx = boxes(texts, 0.52)
    for x0, y0, x1, y1, body in bx:
        if x0 < -0.5 or y0 < -0.5 or x1 > vw + 0.5 or y1 > vh + 0.5:
            probs.append('OFFPAGE "%s" x %.0f..%.0f y %.0f..%.0f (canvas %.0fx%.0f)'
                         % (body.strip()[:28], x0, x1, y0, y1, vw, vh))
    for h in per_factor[0.52]:
        probs.append("OVERLAP@0.52 " + h)
    return probs, per_factor


def main():
    files = sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "*.html")))
    files += sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           "*.svg")))
    bad_files = 0
    total_probs = 0
    soft = {}          # hits that only appear at thinner factors (informational)
    for path in files:
        name = os.path.basename(path)
        src = open(path, encoding="utf-8").read()
        probs_here = []
        for n, block in enumerate(SVG_RE.findall(src), start=1):
            probs, per_factor = audit_block(block, name)
            for wf in FACTORS[1:]:
                for h in per_factor[wf]:
                    soft.setdefault(name, []).append("fig %d wf=%.2f %s" % (n, wf, h))
            for p in probs:
                probs_here.append("fig %d %s" % (n, p))
        if probs_here:
            bad_files += 1
            total_probs += len(probs_here)
            print("FAIL " + name)
            for p in probs_here[:14]:
                print("     " + p)
            if len(probs_here) > 14:
                print("     ... %d more" % (len(probs_here) - 14))
    if soft:
        print("\nthinner-factor observations (not failures):")
        for name, hits in soft.items():
            for h in hits[:6]:
                print("     %s  %s" % (name, h))
    print("\nfiles checked: %d   files with overlaps/offpage: %d   problems: %d"
          % (len(files), bad_files, total_probs))
    return 1 if total_probs else 0


if __name__ == "__main__":
    sys.exit(main())
