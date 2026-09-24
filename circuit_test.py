# circuit_test.py -- reference circuits drawn with circuit.py
#
# Every wire below is written PIN TO PIN: it starts and ends at a coordinate
# returned by place().pin() or junction(), never at a hand-typed number.
# s.check() catches overlaps; s.check_pins() catches wires that do not
# actually reach a pin, junction or power rail.
#
# Run:  cd /home/user/sensors-notes && python3 circuit_test.py

import io
import re
import sys
import xml.etree.ElementTree as ET

from circuit import BLU, PUR, RED, Schematic


def lm35():
    """LM35 in a TO-92 package, front view, pins left to right:
       pin 1 = Vcc   pin 2 (middle) = Vout   pin 3 = GND
       (flat side facing you, leads pointing down)"""
    s = Schematic(760, 380)
    s.label(380, 22, "LM35 temperature sensor \u2014 pin 1 Vcc, pin 2 Vout, pin 3 GND", 19, PUR)

    s.rail(40, 60, 640, 60, color=RED, label="+5 V")
    s.rail(40, 300, 640, 300, color=BLU, label="0 V (GND)")

    u = s.place("ic3", 12, 7, lines=["LM35"],
                pin_names=["Vcc", "GND", "Vout"], tag="LM35")
    adc = s.place("adc", 27, 7, lines=["ADC"], tag="ADC")

    # pin 1 (Vcc) to the +5 V rail
    vcc = u.pin("lt")
    s.wire_px([vcc, (vcc[0], 60)])
    s.junction(vcc[0], 60)

    # pin 3 (GND) to the 0 V rail
    gnd = u.pin("lb")
    s.wire_px([gnd, (gnd[0], 300)])
    s.junction(gnd[0], 300)

    # pin 2 (Vout) to the ADC, with a 10 k pull-down from the same node
    vo = u.pin("r")
    ai = adc.pin("i")
    s.wire_px([vo, ai])
    s.junction(380, vo[1])

    r1 = s.place("resv", 19, 11, label="10 k\u03a9", label_side="right", tag="R1")
    s.wire_px([(380, vo[1]), r1.pin("t")])
    s.wire_px([r1.pin("b"), (380, 300)])
    s.junction(380, 300)

    s.label(380, 358, "Vout = 10 mV per \u00b0C   \u2192   25 \u00b0C gives 250 mV", 16, PUR)
    return s


def verify(s, name):
    geo, con = s.check(), s.check_pins()
    svg = s.svg("Fig. 2.3 &#8212; " + name + ": pin 1 = Vcc, pin 2 = Vout, pin 3 = GND")
    ET.fromstring(re.search(r"<svg.*</svg>", svg, re.S).group(0))   # must be strict XML
    print("%-10s geometry: %-38s connectivity: %s"
          % (name, geo or "NONE", con or "NONE"))
    return svg, geo, con


def make_preview(template="preview-template.html", out="preview-diagrams.html"):
    """Inline the figure into the preview page.

    The in-app viewer renders HTML in a sandboxed iframe with NO network access,
    so <img src="....svg"> would show a broken image: the SVG must be embedded.
    The template is a separate file so re-running never eats the <!--SVG--> marker."""
    svg, geo, con = verify(lm35(), "LM35")
    page = io.open(template, encoding="utf-8").read()
    body = svg[svg.index("<figure"):svg.index("</figure>") + 9]   # figure + caption
    assert "<!--SVG-->" in page, "template has no <!--SVG--> marker"
    page = page.replace("    <!--SVG-->", "    " + body, 1)
    assert "<img" not in page, "page still references an external image"
    assert page.count("<figure") == 1, "figure markup missing from the page"
    assert "<figcaption>" in page, "figure has no caption"
    io.open(out, "w", encoding="utf-8").write(page)
    print("wrote", out, len(page), "bytes (figure + caption inlined)")
    return svg


if __name__ == "__main__":
    svg = make_preview()
    if len(sys.argv) > 1:                      # keep a standalone .svg copy too
        with open(sys.argv[1], "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", sys.argv[1], len(svg), "bytes")
