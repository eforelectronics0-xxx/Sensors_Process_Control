# -*- coding: utf-8 -*-
"""
layout.py -- static geometry audit of every hand drawn diagram.

For each <figure> it estimates the drawn width of every <text> (0.5 x
font-size per character, which is a fair average for the handwritten fonts
used) and reports:

  CLIP   the text runs outside the svg viewBox (it would be cut off)
  IN-BOX the centre of the text is inside a <rect> / <use> box that was drawn
         before it (possible overlap between a label and a component)

Because the estimate is approximate, IN-BOX hits are warnings to look at,
while CLIP hits are always real defects.
"""
import glob
import os
import re
import sys
import html as html_mod
import xml.etree.ElementTree as ET

W_FACTOR = 0.50          # average glyph width / font size
BOX_TOL = 2.0            # px tolerance when testing containment


def est_width(text, size):
    t = html_mod.unescape(re.sub(r"<[^>]+>", "", text))
    return len(t) * size * W_FACTOR


def visible(root):
    """elements that are actually drawn - everything outside <defs>"""
    skip = set()
    for d in root.iter():
        if d.tag.split('}')[-1] == 'defs':
            for sub in d.iter():
                skip.add(sub)
    return [e for e in root.iter() if e not in skip]


def texts_of(root):
    out = []
    for el in visible(root):
        tag = el.tag.split('}')[-1]
        if tag != 'text':
            continue
        body = "".join(el.itertext()).strip()
        if not body:
            continue
        size = float(el.get("font-size", 16))
        x = float(el.get("x", 0))
        y = float(el.get("y", 0))
        anchor = el.get("text-anchor", "start")
        w = est_width(body, size)
        if anchor == "middle":
            x0 = x - w / 2.0
        elif anchor == "end":
            x0 = x - w
        else:
            x0 = x
        out.append((body, x0, x0 + w, y - size, y, size))
    return out


def boxes_of(root):
    out = []
    for el in visible(root):
        tag = el.tag.split('}')[-1]
        if tag == 'rect':
            x = float(el.get('x', 0)); y = float(el.get('y', 0))
            w = float(el.get('width', 0)); h = float(el.get('height', 0))
            # ignore the faint full-canvas background rects
            if w * h > 120000:
                continue
            out.append((x, y, x + w, y + h, 'rect'))
        elif tag == 'use':
            x = float(el.get('x', 0)); y = float(el.get('y', 0))
            w = float(el.get('width', 100)); h = float(el.get('height', 100))
            out.append((x, y, x + w, y + h, 'use#' + (el.get('href') or '?')[1:]))
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    total_clip = total_box = 0
    for path in sorted(glob.glob(os.path.join(here, "*.html"))):
        name = os.path.basename(path)
        src = open(path, encoding="utf-8").read()
        issues = []
        for fig, block in enumerate(re.findall(r"<svg\b.*?</svg>", src, re.S), start=1):
            root = ET.fromstring(block)
            vb = (root.get("viewBox") or "0 0 760 400").split()
            vw, vh = float(vb[2]), float(vb[3])
            ts = texts_of(root)
            bs = boxes_of(root)
            for body, x0, x1, y0, y1, size in ts:
                if x1 > vw + 1 or x0 < -1 or y1 > vh + 1:
                    issues.append("fig %d CLIP   %-38s x %.0f..%.0f y %.0f (canvas %.0fx%.0f)"
                                  % (fig, '"' + body[:36] + '"', x0, x1, y1, vw, vh))
                    total_clip += 1
                    continue
                cx = (x0 + x1) / 2.0
                cy = (y0 + y1) / 2.0
                for bx0, by0, bx1, by1, kind in bs:
                    if bx0 + BOX_TOL < cx < bx1 - BOX_TOL and by0 + BOX_TOL < cy < by1 - BOX_TOL:
                        issues.append("fig %d IN-BOX %-38s centre (%.0f,%.0f) inside %s (%.0f,%.0f)-(%.0f,%.0f)"
                                      % (fig, '"' + body[:36] + '"', cx, cy, kind, bx0, by0, bx1, by1))
                        total_box += 1
                        break
        if issues:
            print(name)
            for i in issues:
                print("    " + i)
    print("\nclipped labels: %d    labels centred inside a component box: %d"
          % (total_clip, total_box))
    return 0


if __name__ == "__main__":
    sys.exit(main())
