# -*- coding: utf-8 -*-
"""
circuit.py -- a small schematic renderer with collision avoidance.

Design goal: it must be *impossible* to produce an overlapping or clipped
diagram.  So the renderer keeps a map of every occupied pixel rectangle:

  * every component reserves its footprint + a margin
  * every label reserves its estimated text box
  * every wire reserves the thin strip it runs through

`place()` and `label()` raise `Collision` instead of drawing over something,
and `check()` verifies at the end that nothing sits outside the canvas.

Grid: 20 units per cell.  Component pins are exactly on cell corners, so
wires are always straight horizontal / vertical lines and junctions land
exactly on pins.
"""

import math
import re
import html as _html

CELL = 20
INK = "#16324f"
RED = "#c62828"
GRN = "#1b7a3d"
BLU = "#123c8c"
PUR = "#6d28d9"
ORG = "#b45309"
FILL = "#fffdf3"

W_FACTOR = 0.52          # conservative glyph width / font size

# the same hand-drawn displacement filter the site's figures have always used
SK_FILTER = ('<filter id="sk" x="-12%" y="-12%" width="124%" height="124%">'
             '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" '
             'seed="9" result="n"/>'
             '<feDisplacementMap in="SourceGraphic" in2="n" scale="1.7" '
             'xChannelSelector="R" yChannelSelector="G"/></filter>')


class Collision(Exception):
    pass


# --------------------------------------------------------------------- #
#  symbols: every symbol is drawn inside a 100 x 100 box.
#  pins are on the box border so they land exactly on grid cells.
#  returns (svg_markup, [ (pin_name, x, y), ... ])
# --------------------------------------------------------------------- #
def _p(d, w=3, color=INK, cap="round"):
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linecap="%s" stroke-linejoin="round"/>' % (d, color, w, cap))


def _box(x, y, w, h, rx=6, fill=FILL, color=INK, sw=3, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" stroke-width="%g"%s/>' \
           % (x, y, w, h, rx, fill, color, sw, d)


def _txt(x, y, s, size=17, color=INK, anchor="middle", weight="normal"):
    # escape bare &, <, > but keep existing numeric/named entity refs intact
    s = re.sub(r"&(?![a-zA-Z][a-zA-Z0-9]*;|#\d+;|#x[0-9a-fA-F]+;)",
               "&amp;", str(s))
    s = s.replace("<", "&lt;").replace(">", "&gt;") if "<" in s or ">" in s else s
    return ('<text x="%g" y="%g" font-size="%g" fill="%s" text-anchor="%s" '
            'font-family="Caveat,cursive" font-weight="%s">%s</text>'
            % (x, y, size, color, anchor, weight, s))


SYM = {}


def symbol(name):
    """returns (markup, pins) for a symbol drawn in a 100x100 box"""
    return SYM[name]()


# --- passive ---------------------------------------------------------- #
def s_res():
    m = _p("M0,50 L20,50 L26,32 L36,68 L46,32 L56,68 L66,32 L74,50 L100,50")
    return m, [("l", 0, 50), ("r", 100, 50)]


def s_resv():
    m = _p("M50,0 L50,20 L32,26 L68,36 L32,46 L68,56 L32,66 L68,74 L50,80 L50,100")
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_cap():
    m = _p("M50,0 L50,38 M22,38 L78,38 M22,62 L78,62 M50,62 L50,100", 3.4)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_capv():
    m = _p("M50,0 L50,38 M22,38 L78,38 M22,62 L78,62 M50,62 L50,100", 3.4)
    m += _p("M84,20 L84,32 M78,26 L90,26", 2.6, RED)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_ind():
    m = _p("M0,50 L14,50 M14,50 A9,9 0 0 1 32,50 A9,9 0 0 1 50,50 "
           "A9,9 0 0 1 68,50 A9,9 0 0 1 86,50 M86,50 L100,50")
    return m, [("l", 0, 50), ("r", 100, 50)]


def s_pot():
    m = _p("M0,50 L20,50 L26,32 L36,68 L46,32 L56,68 L66,32 L74,50 L100,50")
    m += _p("M50,100 L50,74")
    m += '<path d="M42,80 L50,70 L58,80 Z" fill="%s"/>' % INK
    return m, [("l", 0, 50), ("r", 100, 50), ("w", 50, 100)]


def s_bat():
    m = _p("M50,0 L50,30 M22,30 L78,30 M36,46 L64,46 M22,62 L78,62 M50,62 L50,100", 3.2)
    m += _txt(84, 26, "+", 18, RED) + _txt(84, 78, "&#8211;", 20, BLU)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_gnd():
    """compact: pin at the top, symbol only 60 units tall so grounds can be
    stacked directly under a component without wasting grid rows"""
    m = _p("M50,0 L50,30 M18,32 L82,32 M30,46 L70,46 M42,60 L58,60", 3.2)
    return m, [("t", 50, 0)]


def s_vcc():
    m = _p("M50,100 L50,52 M30,50 L70,50", 3.2)
    return m, [("b", 50, 100)]


# --- semiconductor ---------------------------------------------------- #
def s_diode():
    m = '<path d="M32,30 L68,30 L50,64 Z" fill="%s" stroke="%s" stroke-width="2"/>' % (INK, INK)
    m += _p("M50,0 L50,30 M30,66 L70,66 M50,66 L50,100", 3.2)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_led():
    m = '<path d="M32,30 L68,30 L50,64 Z" fill="%s" stroke="%s" stroke-width="2"/>' % (RED, RED)
    m += _p("M50,0 L50,30 M30,66 L70,66 M50,66 L50,100", 3.2)
    m += _p("M70,26 L86,12 M76,38 L92,24", 2.4, RED)
    m += '<path d="M86,12 L78,13 L85,20 Z" fill="%s"/>' % RED
    m += '<path d="M92,24 L84,25 L91,32 Z" fill="%s"/>' % RED
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_npn():
    m = '<circle cx="50" cy="50" r="34" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _p("M0,50 L36,50", 3.2)
    m += _p("M40,28 L40,72", 4)
    m += _p("M40,38 L70,16 L70,0", 3)
    m += _p("M40,62 L70,84 L70,100", 3)
    m += '<path d="M56,74 L70,84 L58,88 Z" fill="%s"/>' % INK
    m += _txt(80, 20, "C", 16, BLU) + _txt(80, 92, "E", 16, BLU) + _txt(14, 42, "B", 16, RED)
    return m, [("b", 0, 50), ("c", 70, 0), ("e", 70, 100)]


def s_pnp():
    m = '<circle cx="50" cy="50" r="34" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _p("M0,50 L36,50", 3.2)
    m += _p("M40,28 L40,72", 4)
    m += _p("M40,38 L70,16 L70,0", 3)
    m += _p("M40,62 L70,84 L70,100", 3)
    m += '<path d="M52,32 L40,38 L54,46 Z" fill="%s"/>' % INK
    m += _txt(80, 20, "E", 16, BLU) + _txt(80, 92, "C", 16, BLU) + _txt(14, 42, "B", 16, RED)
    return m, [("b", 0, 50), ("e", 70, 0), ("c", 70, 100)]


def s_nmos():
    m = _p("M0,50 L36,50", 3.2)
    m += _p("M42,22 L42,78", 4)
    m += _p("M52,22 L52,42 M52,58 L52,78", 3.2)
    m += _p("M52,32 L78,32 L78,0", 3)
    m += _p("M52,68 L78,68 L78,100", 3)
    m += _p("M52,50 L78,50", 3)
    m += '<path d="M60,50 L72,44 L72,56 Z" fill="%s"/>' % INK
    m += _txt(88, 20, "D", 16, BLU) + _txt(88, 92, "S", 16, BLU) + _txt(12, 40, "G", 16, RED)
    return m, [("g", 0, 50), ("d", 78, 0), ("s", 78, 100)]


def s_scr():
    m = _p("M50,0 L50,26 M50,74 L50,100", 3.4)
    m += _p("M26,26 L74,26 M26,74 L74,74", 3.4)
    m += '<path d="M32,26 L32,74 L68,50 Z" fill="none" stroke="%s" stroke-width="3" ' \
         'stroke-linejoin="round"/>' % INK
    m += _p("M68,62 L92,62 L92,86", 2.8, RED)
    m += _txt(16, 20, "A", 17, BLU) + _txt(16, 92, "K", 17, BLU) + _txt(88, 98, "G", 17, RED)
    return m, [("a", 50, 0), ("k", 50, 100), ("g", 92, 86)]


def s_triac():
    m = _p("M50,0 L50,24 M50,76 L50,100", 3.4)
    m += _p("M24,24 L76,24 M24,76 L76,76", 3.4)
    m += '<path d="M32,24 L32,58 L68,24 Z" fill="none" stroke="%s" stroke-width="3" ' \
         'stroke-linejoin="round"/>' % INK
    m += '<path d="M32,76 L32,42 L68,76 Z" fill="none" stroke="%s" stroke-width="3" ' \
         'stroke-linejoin="round"/>' % INK
    m += _p("M62,66 L92,66 L92,88", 2.8, RED)
    m += _txt(10, 16, "MT2", 15, BLU, anchor="start") + _txt(10, 96, "MT1", 15, BLU, anchor="start")
    m += _txt(88, 100, "G", 17, RED)
    return m, [("t2", 50, 0), ("t1", 50, 100), ("g", 92, 88)]


def s_diac():
    m = '<path d="M34,26 L34,60 L66,26 Z" fill="none" stroke="%s" stroke-width="3"/>' % INK
    m += '<path d="M34,74 L34,40 L66,74 Z" fill="none" stroke="%s" stroke-width="3"/>' % INK
    m += _p("M50,0 L50,26 M50,74 L50,100", 3.2)
    return m, [("t", 50, 0), ("b", 50, 100)]


# --- sensors ---------------------------------------------------------- #
def s_therm():
    m = _p("M50,0 L50,20 L32,26 L68,36 L32,46 L68,56 L32,66 L68,74 L50,80 L50,100")
    m += _p("M16,88 L84,14", 2.8, RED)
    m += _p("M16,88 L30,84 M16,88 L20,74", 2.8, RED)
    m += _txt(24, 22, "&#8211;t&#176;", 16, RED)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_ldr():
    m = '<circle cx="50" cy="50" r="30" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _p("M50,0 L50,20 M50,80 L50,100", 3.2)
    m += _p("M32,60 L40,60 L44,46 L50,70 L56,42 L62,64 L66,54 L72,54", 2.4)
    m += _p("M6,20 L28,40 M18,6 L42,28", 2.6, RED)
    m += _p("M28,40 L18,38 M28,40 L25,29 M42,28 L32,26 M42,28 L39,17", 2.6, RED)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_photodiode():
    m = '<path d="M32,30 L68,30 L50,64 Z" fill="%s" stroke="%s" stroke-width="2"/>' % (INK, INK)
    m += _p("M50,0 L50,30 M30,66 L70,66 M50,66 L50,100", 3.2)
    m += _p("M6,20 L26,40 M18,8 L40,28", 2.6, RED)
    m += _p("M26,40 L17,38 M26,40 L23,30 M40,28 L31,26 M40,28 L37,18", 2.6, RED)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_mic():
    m = '<circle cx="50" cy="50" r="28" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _txt(50, 60, "M", 22)
    m += _p("M0,50 L22,50", 3.2)
    return m, [("l", 0, 50)]


def s_spk():
    m = '<path d="M14,36 L34,36 L56,18 L56,82 L34,64 L14,64 Z" fill="%s" stroke="%s" ' \
        'stroke-width="3"/>' % (FILL, INK)
    m += _p("M0,50 L14,50", 3.2)
    m += _p("M68,34 Q78,50 68,66 M80,24 Q96,50 80,76", 2.6, RED)
    return m, [("l", 0, 50)]


def s_mod3():
    m = _box(6, 20, 88, 60, 8)
    m += _p("M26,20 L26,4 M50,20 L50,4 M74,20 L74,4", 3.2)
    m += _txt(26, 16, "VCC", 13, RED) + _txt(50, 16, "OUT", 13, GRN) + _txt(74, 16, "GND", 13, BLU)
    m += _txt(50, 58, "SENSOR", 19)
    return m, [("vcc", 26, 0), ("out", 50, 0), ("gnd", 74, 0)]


def s_probe():
    m = _p("M30,10 L30,80 M70,10 L70,80", 4)
    m += _p("M20,82 L40,82 M60,82 L80,82", 4)
    m += _p("M14,92 Q50,80 86,92", 3, "#8a5a2b")
    m += _txt(50, 34, "soil", 15, "#8a5a2b")
    return m, [("l", 30, 0), ("r", 70, 0)]


def s_strain():
    m = _box(14, 14, 72, 72, 6)
    m += _p("M26,74 L26,30 L40,30 L40,70 L54,70 L54,30 L68,30 L68,70 L74,70", 2.6, RED)
    m += _p("M26,74 L14,86 M74,70 L86,86", 2.6)
    return m, [("l", 0, 86), ("r", 100, 86)]


# --- blocks ----------------------------------------------------------- #
def _blocklabel(lines, w=88, h=60, color=INK, size=17):
    m = _box((100 - w) / 2, (100 - h) / 2, w, h, 8)
    n = len(lines)
    y0 = 50 - (n - 1) * (size * 0.62)
    for i, ln in enumerate(lines):
        m += _txt(50, y0 + i * size * 1.24 + size * 0.35, ln, size, color)
    return m


def s_opamp():
    m = '<path d="M14,12 L86,50 L14,88 Z" fill="%s" stroke="%s" stroke-width="3.2" ' \
        'stroke-linejoin="round"/>' % (FILL, INK)
    m += _p("M86,50 L100,50 M0,32 L14,32 M0,68 L14,68", 3.2)
    m += _txt(26, 38, "+", 20, BLU) + _txt(26, 76, "&#8211;", 22, RED)
    return m, [("p", 0, 32), ("n", 0, 68), ("o", 100, 50)]


def s_ic():
    m = _blocklabel(["IC"], 70, 66)
    m += _p("M20,17 L20,0 M50,17 L50,0 M80,17 L80,0", 3)
    m += _p("M85,50 L100,50", 3)
    return m, [("i1", 20, 0), ("i2", 50, 0), ("i3", 80, 0), ("o", 100, 50)]


def s_ic3():
    """3-pin IC drawn the way a textbook draws it: two pins on the left, one on
    the right, each lead labelled.  Pin names are set with place(lines=[...])
    as [left-top, left-bottom, right]."""
    m = _box(15, 17, 70, 66, 8)
    m += _p("M0,30 L15,30 M0,70 L15,70 M85,50 L100,50", 3)
    return m, [("lt", 0, 30), ("lb", 0, 70), ("r", 100, 50)]


def s_adc():
    m = _blocklabel(["ADC"], 80, 56)
    m += _p("M0,50 L10,50 M90,50 L100,50", 3.2)
    return m, [("i", 0, 50), ("o", 100, 50)]


def s_dac():
    m = _blocklabel(["DAC"], 80, 56)
    m += _p("M0,50 L10,50 M90,50 L100,50", 3.2)
    return m, [("i", 0, 50), ("o", 100, 50)]


def s_amp():
    m = _blocklabel(["AMP"], 80, 56)
    m += _p("M0,50 L10,50 M90,50 L100,50", 3.2)
    return m, [("i", 0, 50), ("o", 100, 50)]


def s_mcu():
    m = _box(8, 8, 84, 84, 10, dash="11 7")
    m += _txt(50, 46, "&#181;C /", 19)
    m += _txt(50, 68, "Arduino", 16)
    m += _p("M0,30 L8,30 M0,70 L8,70 M92,30 L100,30 M92,70 L100,70", 3)
    return m, [("l1", 0, 30), ("l2", 0, 70), ("r1", 100, 30), ("r2", 100, 70)]


def s_mcu2():
    """microcontroller block with pins on left and bottom"""
    m = _box(8, 8, 84, 84, 10, dash="11 7")
    m += _txt(50, 46, "&#181;C /", 19)
    m += _txt(50, 68, "Arduino", 16)
    m += _p("M0,50 L8,50 M50,92 L50,100", 3)
    return m, [("l", 0, 50), ("b", 50, 100)]


def s_display():
    m = _blocklabel(["DISPLAY"], 84, 50, BLU, 16)
    m += _p("M0,50 L8,50", 3.2)
    return m, [("i", 0, 50)]


def s_block2():
    m = _blocklabel(["BLOCK"], 84, 56)
    m += _p("M0,50 L8,50 M92,50 L100,50", 3.2)
    return m, [("i", 0, 50), ("o", 100, 50)]


def s_lamp():
    m = '<circle cx="50" cy="50" r="28" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _p("M30,30 L70,70 M70,30 L30,70", 2.6)
    m += _p("M50,0 L50,22 M50,78 L50,100", 3.2)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_heater():
    m = _box(14, 28, 72, 44, 8)
    m += _p("M24,58 Q31,38 38,58 Q45,78 52,58 Q59,38 66,58 Q70,68 76,58", 2.8, RED)
    m += _p("M0,50 L14,50 M86,50 L100,50", 3.2)
    return m, [("l", 0, 50), ("r", 100, 50)]


def s_motor():
    m = '<circle cx="50" cy="50" r="30" fill="%s" stroke="%s" stroke-width="3.2"/>' % (FILL, INK)
    m += _txt(50, 62, "M", 28)
    m += _p("M50,0 L50,20 M50,80 L50,100", 3.2)
    return m, [("t", 50, 0), ("b", 50, 100)]


def s_servo():
    m = _box(12, 26, 76, 52, 8)
    m += '<circle cx="50" cy="26" r="11" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _p("M26,78 L26,100 M50,78 L50,100 M74,78 L74,100", 3)
    m += _txt(26, 62, "V", 14, RED) + _txt(50, 62, "S", 14, ORG) + _txt(74, 62, "G", 14, BLU)
    return m, [("v", 26, 100), ("s", 50, 100), ("g", 74, 100)]


def s_stepper():
    m = '<circle cx="50" cy="50" r="30" fill="%s" stroke="%s" stroke-width="3.2"/>' % (FILL, INK)
    m += _txt(50, 58, "STP", 16)
    m += _p("M8,22 L28,36 M8,78 L28,64 M92,22 L72,36 M92,78 L72,64", 3)
    return m, [("a", 0, 20), ("b", 0, 80), ("c", 100, 20), ("d", 100, 80)]


def s_relay():
    m = _box(18, 16, 64, 68, 8)
    m += _p("M32,66 A9,9 0 0 1 50,66 A9,9 0 0 1 68,66", 3)
    m += _txt(50, 44, "K", 20, RED)
    m += _p("M50,0 L50,16 M50,84 L50,100", 3.2)
    m += _p("M100,26 L85,26 M85,74 L100,74", 3)
    m += '<circle cx="80" cy="26" r="5" fill="%s" stroke="%s" stroke-width="2.4"/>' % (FILL, INK)
    m += '<circle cx="80" cy="74" r="5" fill="%s" stroke="%s" stroke-width="2.4"/>' % (FILL, INK)
    m += _p("M80,30 L60,70", 3)
    return m, [("c1", 50, 0), ("c2", 50, 100), ("no", 100, 26), ("nc", 100, 74)]


def s_solenoid():
    m = _p("M0,34 L14,34 M14,34 A9,9 0 0 1 32,34 A9,9 0 0 1 50,34 A9,9 0 0 1 68,34 "
           "A9,9 0 0 1 86,34 M86,34 L100,34")
    m += _box(22, 58, 46, 18, 6)
    m += _p("M68,67 L96,67 M0,67 L22,67", 3)
    m += '<path d="M78,54 L96,67 L78,80" fill="none" stroke="%s" stroke-width="2.6"/>' % RED
    return m, [("l1", 0, 34), ("l2", 0, 67)]


def s_switch():
    m = _p("M0,50 L28,50 M72,50 L100,50", 3.2)
    m += '<circle cx="30" cy="50" r="5" fill="%s" stroke="%s" stroke-width="2.4"/>' % (FILL, INK)
    m += '<circle cx="70" cy="50" r="5" fill="%s" stroke="%s" stroke-width="2.4"/>' % (FILL, INK)
    m += _p("M33,47 L68,28", 3)
    return m, [("l", 0, 50), ("r", 100, 50)]


def s_push():
    m = _p("M0,50 L30,50 M70,50 L100,50", 3.2)
    m += '<circle cx="32" cy="50" r="5" fill="%s" stroke="%s" stroke-width="2.4"/>' % (FILL, INK)
    m += '<circle cx="68" cy="50" r="5" fill="%s" stroke="%s" stroke-width="2.4"/>' % (FILL, INK)
    m += _p("M28,38 L72,32", 3)
    m += _p("M50,22 L50,34", 2.8, RED)
    m += '<circle cx="50" cy="18" r="6" fill="none" stroke="%s" stroke-width="2.6"/>' % RED
    return m, [("l", 0, 50), ("r", 100, 50)]


def s_buzzer():
    m = '<path d="M20,32 L58,20 L58,80 L20,68 Z" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _p("M0,50 L20,50", 3.2)
    m += _p("M68,36 Q78,50 68,64", 2.6, RED)
    return m, [("l", 0, 50)]


def s_sum():
    """summing junction: circle with Sigma; inputs left, out right, feedback bottom"""
    m = '<circle cx="50" cy="50" r="32" fill="%s" stroke="%s" stroke-width="3"/>' % (FILL, INK)
    m += _txt(50, 61, "&#931;", 28, INK)
    m += _p("M0,50 L18,50 M82,50 L100,50 M50,82 L50,100", 3.2)
    return m, [("l", 0, 50), ("r", 100, 50), ("b", 50, 100)]


def s_pkg4():
    """4-pin bottom package (DHT11 style): leads at x = 10/30/50/70"""
    m = _box(6, 10, 88, 62, 8)
    m += _p("M10,72 L10,100 M30,72 L30,100 M50,72 L50,100 M70,72 L70,100", 3)
    return m, [("v", 10, 100), ("d", 30, 100), ("n", 50, 100), ("g", 70, 100)]


SYM.update({k[2:]: v for k, v in list(globals().items()) if k.startswith("s_") and callable(v)})
SYM = {k: v for k, v in SYM.items()}

# Real content bounds inside the 100x100 symbol box (x0,y0,x1,y1).  Only the
# drawn part of the symbol is reserved, otherwise short symbols such as the
# ground would waste whole grid rows.
BOUNDS = {
    "gnd":     (18, 0, 82, 60),
    "vcc":     (30, 50, 70, 100),
    "mic":     (0, 22, 78, 78),
    "spk":     (0, 18, 96, 82),
    "buzzer":  (0, 20, 78, 80),
    "diode":   (30, 0, 70, 100),
    "led":     (6, 0, 92, 100),
    "photodiode": (6, 0, 70, 100),
    "scr":     (10, 0, 92, 100),
    "triac":   (10, 0, 92, 100),
    "npn":     (0, 0, 92, 100),
    "pnp":     (0, 0, 92, 100),
    "nmos":    (0, 0, 96, 100),
    "bat":     (22, 0, 88, 100),
    "therm":   (14, 0, 86, 100),
    "ldr":     (6, 0, 94, 100),
    "probe":   (14, 0, 86, 96),
    "solenoid": (0, 20, 100, 82),
    "relay":   (14, 0, 100, 100),
    "servo":   (12, 14, 88, 100),
    "stepper": (8, 8, 92, 92),
    "motor":   (20, 0, 80, 100),
    "lamp":    (22, 0, 78, 100),
    "opamp":   (0, 12, 100, 88),
    "ic":      (15, 0, 100, 83),
    "ic3":     (0, 17, 100, 109),
    "mcu":     (0, 8, 100, 92),
    "mcu2":    (8, 8, 92, 100),
    "adc":     (0, 22, 100, 78),
    "dac":     (0, 22, 100, 78),
    "amp":     (0, 22, 100, 78),
    "display": (0, 25, 100, 75),
    "block2":  (0, 22, 100, 78),
    "res":     (0, 30, 100, 70),
    "ind":     (0, 38, 100, 62),
    "pot":     (0, 30, 100, 100),
    "heater":  (0, 28, 100, 72),
    "cap":     (22, 0, 78, 100),
    "capv":    (22, 0, 90, 100),
    "resv":    (30, 0, 70, 100),
    "strain":  (0, 14, 100, 86),
    "diac":    (32, 0, 68, 100),
    "push":    (0, 10, 100, 62),
    "switch":  (0, 26, 100, 62),
    "mod3":    (6, 0, 94, 80),
    "sum":     (0, 18, 100, 100),
    "pkg4":    (6, 10, 94, 100),
}


def bounds(name):
    return BOUNDS.get(name, (0, 0, 100, 100))


# --------------------------------------------------------------------- #
#  the sheet
# --------------------------------------------------------------------- #
class Schematic:
    def __init__(self, w=760, h=430, margin=14):
        self.w = float(w)
        self.h = float(h)
        self.margin = margin
        self.items = []          # svg markup, in draw order
        self.occupied = []       # (x0,y0,x1,y1,what,solid)
        self.wire_segs = []      # (x0,y0,x1,y1)
        self.wire_polys = []     # the full point list of every wire
        self.pin_pts = []        # every pin coordinate, for connectivity checks
        self.rails = []          # power rail segments a wire may start on
        self.errors = []
        self.drawn = []       # painted bounds (x0,y0,x1,y1,what) for wire checks

    # -- low level ---------------------------------------------------- #
    def _snap(self, v):
        return int(round(v / CELL)) * CELL

    def _reserve(self, x0, y0, x1, y1, what, solid=True):
        """Record a rectangle.

        Solid rectangles (component footprints) may never overlap anything
        solid - that is a hard error.  Advisory rectangles (wires, labels)
        are allowed to touch a component, because a wire has to reach its
        pin; real crossings are reported later by check().
        """
        if solid:
            for a, b, c, d, w2, s2 in self.occupied:
                if s2 and x0 < c and a < x1 and y0 < d and b < y1:
                    raise Collision("%s overlaps %s  [%.0f,%.0f - %.0f,%.0f]"
                                    % (what, w2, x0, y0, x1, y1))
        self.occupied.append((x0, y0, x1, y1, what, solid))
        return True

    # -- placement ---------------------------------------------------- #
    def place(self, name, col, row, rot=0, scale=1.0, label=None, label_at=None,
              label_color=RED, label_size=16, tag=None, margin=6, lines=None,
              label_side="above", pin_names=None, lines_size=17):
        """place a symbol so its centre sits on grid cell (col,row).

        rot is 0/90/180/270 clockwise.  Returns the placed object so the
        caller can read its pin coordinates.
        """
        pnames = list(pin_names) if pin_names else None   # keep: `pins` below is the symbol's
        markup, pins = SYM[name]()
        if name == "pkg4":
            nm = (list(lines) + ["SENSOR"])[0] if lines else "SENSOR"
            m = _box(6, 10, 88, 62, 8)
            m += _txt(50, 30, nm, 16, INK)
            if lines and len(lines) > 1:
                m += _txt(50, 48, lines[1], 10, BLU)
            if lines and len(lines) > 2:
                m += _txt(50, 62, lines[2], 10, BLU)
            m += _p("M10,72 L10,100 M30,72 L30,100 M50,72 L50,100 M70,72 L70,100", 3)
            markup = m
        elif name == "ic3":
            # lines = [chip name]; pins = [left-top, left-bottom, right] pin NAMES.
            # Number + name together, each on its own line INSIDE the block, so
            # neither a wire nor the chip name can run over them.
            nm = (list(lines) + ["IC"])[0] if lines else "IC"
            pn = (list(pnames) + ["", "", ""])[:3] if pnames else ["", "", ""]
            # box x10..90 y17..109.  Every text gets its own band, measured at
            # width factor 0.52 (worst case): 1@y34 (23.9-36.5), 2@y54
            # (43.9-56.5), 3@y74 (63.9-76.5), name@y96 (83.1-99.3) -- the
            # smallest gap between any two bands is 6.6 px.
            m = _box(10, 17, 80, 92, 8)
            m += _txt(14, 34, "1 " + pn[0], 14, RED, anchor="start", weight="bold")
            m += _txt(86, 54, "2 " + pn[2], 14, GRN, anchor="end", weight="bold")
            m += _txt(14, 74, "3 " + pn[1], 14, BLU, anchor="start", weight="bold")
            m += _txt(50, 96, nm, 18, INK)
            m += _p("M0,30 L10,30 M0,70 L10,70 M90,50 L100,50", 3)
            markup = m
        elif lines is not None and name in ("ic", "adc", "dac", "amp", "block2", "display"):
            gen = SYM[name]
            if name == "ic":
                markup, pins = _blocklabel(lines, 70, 66, size=lines_size), pins
                markup += _p("M20,17 L20,0 M50,17 L50,0 M80,17 L80,0", 3)
                markup += _p("M85,50 L100,50", 3)
            else:
                w, h = (84, 50) if name == "display" else (80, 56)
                markup, pins = _blocklabel(lines, w, h, size=lines_size), pins
                markup += _p("M0,50 L10,50 M90,50 L100,50", 3.2)
        cx = self._snap(col * CELL)
        cy = self._snap(row * CELL)
        size = 100 * scale
        half = size / 2.0

        def rotpt(x, y):
            for _ in range(int(rot / 90) % 4):
                x, y = y, 100 - x
            return x, y

        rpins = {}
        for pn, px, py in pins:
            rx, ry = rotpt(px, py)
            rpins[pn] = (cx - half + rx * scale, cy - half + ry * scale)

        # footprint = the real drawn bounds of the symbol (rotated with it),
        # not the whole 100x100 box.  Reserve exactly those bounds as solid:
        # the margin is only the offset used when placing side labels, so two
        # parts stacked pin-to-pin may touch at the shared pin without a
        # false "overlaps" error.
        bx0, by0, bx1, by1 = bounds(name)
        if int(rot / 90) % 4:
            pts = [(bx0, by0), (bx1, by0), (bx0, by1), (bx1, by1)]
            for _ in range(int(rot / 90) % 4):
                pts = [(py, 100 - px) for px, py in pts]
            bx0 = min(p[0] for p in pts); bx1 = max(p[0] for p in pts)
            by0 = min(p[1] for p in pts); by1 = max(p[1] for p in pts)
        x0 = cx - half + bx0 * scale
        y0 = cy - half + by0 * scale
        x1 = cx - half + bx1 * scale
        y1 = cy - half + by1 * scale
        self._reserve(x0, y0, x1, y1, tag or name, solid=True)
        self.drawn.append((x0, y0, x1, y1, tag or name))

        tf = "translate(%g,%g) rotate(%g,50,50) translate(%g,%g) scale(%g)" % (
            cx - half, cy - half, rot, 0, 0, scale)
        self.items.append('<g transform="%s">%s</g>' % (tf, markup))

        for pn, (px, py) in rpins.items():
            self.pin_pts.append((px, py, (tag or name) + "." + pn))
        obj = _Comp(self, name, cx, cy, rpins, rot, scale)
        if label:
            if label_at:
                lx, ly, anch = label_at[0], label_at[1], "middle"
            elif label_side == "right":
                lx, ly, anch = x1 + margin + 8, cy + label_size * 0.35, "start"
            elif label_side == "left":
                lx, ly, anch = x0 - margin - 8, cy + label_size * 0.35, "end"
            elif label_side == "below":
                lx, ly, anch = cx, y1 + margin + label_size + 2, "middle"
            else:
                lx, ly, anch = cx, y0 - margin - 4, "middle"
            self.label(lx, ly, label, size=label_size, color=label_color,
                       anchor=anch, tag=(tag or name) + " label")
        return obj

    def label(self, x, y, text, size=16, color=INK, anchor="middle", tag="label",
              weight="normal"):
        w = len(_html.unescape(re.sub(r"<[^>]+>", "", text))) * size * W_FACTOR
        if anchor == "middle":
            x0 = x - w / 2.0
        elif anchor == "end":
            x0 = x - w
        else:
            x0 = x
        y0 = y - size
        if tag == "label":
            tag = "label[%s]" % _html.unescape(
                re.sub(r"<[^>]+>", "", text))[:16]
        if x0 < 0 or x0 + w > self.w or y0 < 0 or y > self.h:
            raise Collision("label %r runs off the canvas (x %.0f..%.0f, y %.0f)"
                            % (text, x0, x0 + w, y))
        self._reserve(x0 - 1, y0 - 1, x0 + w + 1, y + 3, tag, solid=False)
        self.items.append(_txt(x, y, text, size, color, anchor, weight))

    def wire(self, pts, color=INK, width=3, dash=None, arrow=False, tag="wire"):
        """pts are GRID CELLS (col,row); they are snapped to the grid.
        Use wire_px() when you already have absolute pixel coordinates
        (for example the pin positions returned by place())."""
        abs_pts = [(self._snap(c * CELL), self._snap(r * CELL)) for c, r in pts]
        return self._draw_wire(abs_pts, color, width, dash, arrow, tag)

    def wire_px(self, pts, color=INK, width=3, dash=None, arrow=False, tag="wire"):
        """pts are ABSOLUTE coordinates - used for pin to pin wiring"""
        abs_pts = [(float(x), float(y)) for x, y in pts]
        return self._draw_wire(abs_pts, color, width, dash, arrow, tag)

    def _draw_wire(self, abs_pts, color, width, dash, arrow, tag):
        for i in range(len(abs_pts) - 1):
            ax, ay = abs_pts[i]
            bx, by = abs_pts[i + 1]
            if ax != bx and ay != by:
                raise Collision("wire segment (%g,%g)-(%g,%g) is not orthogonal"
                                % (ax, ay, bx, by))
        for i in range(len(abs_pts) - 1):
            ax, ay = abs_pts[i]
            bx, by = abs_pts[i + 1]
            x0, x1 = min(ax, bx), max(ax, bx)
            y0, y1 = min(ay, by), max(ay, by)
            self.wire_segs.append((x0, y0, x1, y1))
            self._reserve(x0 - 3, y0 - 3, x1 + 3, y1 + 3, tag, solid=False)
        self.wire_polys.append(abs_pts)
        style = "fill:none;stroke:%s;stroke-width:%s;stroke-linecap:round;stroke-linejoin:round" \
                % (color, width)
        if dash:
            style += ";stroke-dasharray:%s" % dash
        mark = ""
        if arrow:
            style += ";marker-end:url(#arw)"
        self.items.append('<polyline points="%s" style="%s"%s/>'
                          % (" ".join("%g,%g" % p for p in abs_pts), style, mark))
        return abs_pts

    def rail(self, x0, y0, x1, y1, color=RED, label=None, tag="rail"):
        """a power rail in ABSOLUTE coordinates: a wire other wires may tap"""
        pts = self.wire_px([(x0, y0), (x1, y1)], color=color, tag=tag)
        self.rails.append((pts[0][0], pts[0][1], pts[-1][0], pts[-1][1]))
        if label:
            if abs(y0 - y1) < 0.5:          # horizontal rail: label below it
                self.label((x0 + x1) / 2.0, y0 + 26, label, size=15, color=color,
                           anchor="middle", tag=tag + " label")
            else:                            # vertical rail: label beside it
                self.label(x0 + 10, (y0 + y1) / 2.0, label, size=15, color=color,
                           anchor="start", tag=tag + " label")
        return pts

    def register(self, x, y, name="node"):
        """declare a point that wires may legally start or end on"""
        self.pin_pts.append((float(x), float(y), name))

    def junction(self, x, y):
        if isinstance(x, tuple):
            x, y = self._snap(x[0] * CELL), self._snap(x[1] * CELL)
        self.items.append('<circle cx="%g" cy="%g" r="5.5" fill="%s"/>' % (x, y, INK))
        self.pin_pts.append((float(x), float(y), "junction"))

    def textbox(self, x0, y0, x1, y1, lines, size=15, color=INK, fill=FILL,
                weight="normal", tag=None, radius=8):
        """checked rectangle with centred text lines (trees, legends, tables)"""
        x0, y0, x1, y1 = float(x0), float(y0), float(x1), float(y1)
        self._reserve(x0 - 2, y0 - 2, x1 + 2, y1 + 2,
                      tag or ("box:" + str(lines[0])[:14]), solid=True)
        self.drawn.append((x0, y0, x1, y1, tag or ("box:" + str(lines[0])[:12])))
        m = '<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" ' \
            'stroke="%s" stroke-width="2.6"/>' % (x0, y0, x1 - x0, y1 - y0,
                                                  radius, fill, color)
        n = len(lines)
        widest = max(len(str(l)) for l in lines) * size * W_FACTOR
        if widest > (x1 - x0) - 8:
            raise Collision("textbox too narrow for %r (needs %.0f, has %.0f)"
                            % (str(lines[0])[:24], widest, x1 - x0 - 8))
        if n * size * 1.35 > (y1 - y0) - 4:
            raise Collision("textbox too short for %d lines of size %g"
                            % (n, size))
        span = y1 - y0
        step = min(size * 1.35, (span - size * 0.6) / max(n - 1, 1)) if n > 1 else 0
        y_first = (y0 + y1) / 2.0 - step * (n - 1) / 2.0 + size * 0.34
        for i, ln in enumerate(lines):
            w = len(str(ln)) * size * W_FACTOR
            lx = (x0 + x1) / 2.0
            # reserve the line itself so a stray label cannot land on it
            tag_l = (tag or "box") + "#line%d" % i
            self._reserve(lx - w / 2.0 - 1, y_first + i * step - size * 0.72 - 1,
                          lx + w / 2.0 + 1, y_first + i * step + size * 0.18 + 1,
                          tag_l, solid=False)
            m += _txt(lx, y_first + i * step, ln, size, color,
                      "middle", weight)
        self.items.append(m)
        return (x0, y0, x1, y1)

    def path(self, d, color=INK, width=3, dash=None, arrow=False):
        style = "fill:none;stroke:%s;stroke-width:%s;stroke-linecap:round" % (color, width)
        if dash:
            style += ";stroke-dasharray:%s" % dash
        if arrow:
            style += ";marker-end:url(#arw)"
        self.items.append('<path d="%s" style="%s"/>' % (d, style))

    def frame(self, x0, y0, x1, y1, color="#7d8ea3", dash="9 6"):
        self.items.insert(0, _box(x0, y0, x1 - x0, y1 - y0, 12, "none", color, 2.4, dash))

    # -- verification ------------------------------------------------- #
    @staticmethod
    def _on_rail(x, y, rails, tol=2.0):
        for rx0, ry0, rx1, ry1 in rails:
            if abs(ry0 - ry1) < 0.5:                      # horizontal rail
                if abs(y - ry0) <= tol and min(rx0, rx1) - tol <= x <= max(rx0, rx1) + tol:
                    return True
            else:                                         # vertical rail
                if abs(x - rx0) <= tol and min(ry0, ry1) - tol <= y <= max(ry0, ry1) + tol:
                    return True
        return False

    def check_pins(self, tol=1.5):
        """every wire end must sit exactly on a pin, a junction or a rail.
        This is what stops a wire from starting inside a component body."""
        bad = []
        ends = []
        for pts in self.wire_polys:
            ends.append(pts[0])       # only the two true ends of a wire,
            ends.append(pts[-1])      # never its corners
        for (x, y) in sorted(ends):
            ok = any(abs(x - px) <= tol and abs(y - py) <= tol
                     for px, py, _n in self.pin_pts)
            if not ok:
                ok = self._on_rail(x, y, self.rails)
            if not ok:
                bad.append("wire end (%g,%g) is not on any pin, junction or rail"
                           % (x, y))
        return bad

    def check(self):
        """returns a list of problems: off-canvas items and wires that run
        through the inside of a component"""
        bad = []
        for x0, y0, x1, y1, what, solid in self.occupied:
            if x0 < -1 or y0 < -1 or x1 > self.w + 1 or y1 > self.h + 1:
                bad.append("off canvas: %s (%.0f,%.0f)-(%.0f,%.0f)" % (what, x0, y0, x1, y1))
        for (wx0, wy0, wx1, wy1) in self.wire_segs:
            # trim 9px at both ends ALONG the wire (pin entry is legal),
            # give the wire 6px of thickness ACROSS, and test painted bounds -
            # never the margin-inflated footprint, or every pin approach dies.
            if wy0 == wy1:                       # horizontal
                x0, x1 = ((wx0 + 9, wx1 - 9) if wx1 - wx0 > 22 else (wx0, wx1))
                y0, y1 = wy0 - 3, wy1 + 3
            else:                                # vertical
                y0, y1 = ((wy0 + 9, wy1 - 9) if wy1 - wy0 > 22 else (wy0, wy1))
                x0, x1 = wx0 - 3, wx1 + 3
            for (bx0, by0, bx1, by1, what) in self.drawn:
                ix0, ix1 = max(x0, bx0), min(x1, bx1)
                iy0, iy1 = max(y0, by0), min(y1, by1)
                if ix1 - ix0 > 4 and iy1 - iy0 > 4:
                    bad.append("wire runs through %s (overlap %.0fx%.0f)"
                               % (what, ix1 - ix0, iy1 - iy0))
        # two labels may never overlap (they reserve exact estimated boxes)
        labs = [(x0, y0, x1, y1, what) for x0, y0, x1, y1, what, solid
                in self.occupied if not solid and
                ("label" in str(what) or "#line" in str(what))]
        for i in range(len(labs)):
            for j in range(i + 1, len(labs)):
                a, b = labs[i], labs[j]
                if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                    bad.append("label %s overlaps label %s" % (a[4], b[4]))
        # a label centred on a component footprint is printed over the part
        solids = [(x0, y0, x1, y1, what) for x0, y0, x1, y1, what, solid
                  in self.occupied if solid and not str(what).startswith("rail")]
        for lx0, ly0, lx1, ly1, tag in labs:
            if "#line" in str(tag):
                continue          # textbox lines live inside their own box by design
            ccx, ccy = (lx0 + lx1) / 2.0, (ly0 + ly1) / 2.0
            for x0, y0, x1, y1, what in solids:
                if x0 + 2 < ccx < x1 - 2 and y0 + 2 < ccy < y1 - 2:
                    bad.append("label %s sits on %s" % (tag, what))
                    break
        bad.extend(self.errors)
        return bad

    def svg(self, caption, defs="", sketch=True):
        body = "\n".join(self.items)
        if sketch:
            body = '<g filter="url(#sk)">\n%s\n</g>' % body
            defs = (SK_FILTER + defs)
        return (
            '\n<figure class="fig">\n'
            '<svg viewBox="0 0 %g %g" role="img" aria-label="%s" '
            'style="background:#fffef7;border-radius:12px">\n'
            '<defs>\n'
            '<marker id="arw" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" '
            'markerHeight="9" orient="auto"><path d="M1,1.5 L10,6 L1,10.5 Z" fill="%s"/></marker>\n'
            '%s</defs>\n%s\n</svg>\n<figcaption>%s</figcaption>\n</figure>\n'
            % (self.w, self.h, caption.replace('"', "'"), INK, defs, body, caption)
        )


class _Comp:
    def __init__(self, sheet, name, cx, cy, pins, rot, scale):
        self.sheet, self.name, self.cx, self.cy = sheet, name, cx, cy
        self.pins, self.rot, self.scale = pins, rot, scale

    def pin(self, name):
        return self.pins[name]

    def xy(self, name):
        x, y = self.pins[name]
        return x, y


def demo():
    s = Schematic(760, 340)
    s.label(380, 26, "LM35 temperature sensor circuit", 20, PUR)
    ic = s.place("ic", 12, 7, label="LM35")
    return s


if __name__ == "__main__":
    s = demo()
    print("problems:", s.check())
