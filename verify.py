# -*- coding: utf-8 -*-
"""
verify.py -- real checks on the generated site.

For every .html file it:
  1. parses the whole document with html.parser  (catches unclosed tags / bad nesting)
  2. extracts every <svg>...</svg> and parses it with ElementTree (strict XML)
  3. checks that every href="#id" inside an SVG points at an id that exists
  4. checks that every internal link points at a file that exists
  5. checks that <use> never references an unknown symbol
  6. reports tag-balance problems
"""
import os
import re
import sys
import glob
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr",
        # svg / xml self-closing elements
        "path", "circle", "rect", "line", "polyline", "polygon", "ellipse",
        "use", "stop", "feturbulence", "fedisplacementmap"}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = set()
        self.links = []
        self.fragrefs = []
        self.svg_depth = 0
        self.figcount = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "use":
            ref = a.get("href", a.get("xlink:href", ""))
            if ref.startswith("#"):
                self.fragrefs.append(ref[1:])
        if tag == "svg":
            self.svg_depth += 1
        if tag == "figure":
            self.figcount += 1
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "use":
            ref = a.get("href", "")
            if ref.startswith("#"):
                self.fragrefs.append(ref[1:])

    def handle_endtag(self, tag):
        if tag == "svg":
            self.svg_depth -= 1
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("line %d: stray closing </%s>" % (self.getpos()[0], tag))
            return
        open_tag, pos = self.stack.pop()
        if open_tag != tag:
            self.errors.append("line %d: </%s> closes <%s> opened at line %d"
                               % (self.getpos()[0], tag, open_tag, pos[0]))


def svg_blocks(text):
    return re.findall(r"<svg\b.*?</svg>", text, re.S | re.I)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    files = sorted(glob.glob(os.path.join(here, "*.html")))
    total_svg = 0
    problems = 0
    print("checking %d html files\n" % len(files))
    for path in files:
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        c = Checker()
        try:
            c.feed(text)
            c.close()
        except Exception as e:                       # noqa: BLE001
            print("FAIL %-42s html.parser raised %s" % (name, e))
            problems += 1
            continue

        msgs = []

        # 1. tag balance
        for tag, pos in c.stack:
            msgs.append("unclosed <%s> opened at line %d" % (tag, pos[0]))
        msgs.extend(c.errors)

        # 2/3. every SVG must be strict XML and its symbols must resolve
        for n, block in enumerate(svg_blocks(text), start=1):
            total_svg += 1
            try:
                ET.fromstring(block)
            except ET.ParseError as e:
                msgs.append("figure %d: SVG is not valid XML -> %s" % (n, e))
        for ref in c.fragrefs:
            if ref not in c.ids:
                msgs.append("unknown reference #%s" % ref)

        # 4. internal links
        for link in c.links:
            if link.startswith(("http", "mailto:")) or link.startswith("#"):
                continue
            target = os.path.join(here, link.split("#")[0])
            if not os.path.exists(target):
                msgs.append("broken link -> %s" % link)

        # css / script presence
        if "css/notes.css" not in text:
            msgs.append("stylesheet link missing")
        if c.figcount and "figcaption" not in text:
            msgs.append("figure without caption")

        if msgs:
            problems += 1
            print("FAIL %s (%d figures, %d svg)" % (name, c.figcount, len(svg_blocks(text))))
            for m in msgs[:12]:
                print("       - %s" % m)
        else:
            print("ok   %-42s %2d figures, %3d symbol refs, %2d links"
                  % (name, c.figcount, len(c.fragrefs), len(c.links)))

    css = os.path.join(here, "css", "notes.css")
    print("\ncss/notes.css present: %s (%d bytes)" % (os.path.exists(css),
          os.path.getsize(css) if os.path.exists(css) else 0))
    print("total SVG diagrams parsed as XML: %d" % total_svg)
    print("files with problems: %d" % problems)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
