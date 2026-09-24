# -*- coding: utf-8 -*-
"""
figures_core.py -- framework for redrawing every site diagram on the checked grid.

Each figure builder returns a circuit.Schematic.  render(key) runs the full
battery on it:

  * s.check()        off-canvas items, wire through a part, text-vs-text,
                     text printed on a component
  * s.check_pins()   every wire end lands on a pin, junction or rail
  * strict XML parse of the <svg>
  * check_text.audit_block()  text overlap at width factor 0.52 + off-page

and raises circuit.Collision listing every problem, so a broken figure can
never reach the site.  Output goes through helpers.safe_svg so named entities
(&mdash;) become numeric and ElementTree can parse them.
"""
import re
import xml.etree.ElementTree as ET

import helpers as H
from check_text import audit_block
from circuit import Collision, Schematic, INK, PUR, RED, BLU, GRN, ORG, FILL

# captions exactly as the site has always shown them
CAPS = {
    "1.1": "Fig. 1.1 &mdash; Block diagram of a measuring system (sensor chain)",
    "1.2": "Fig. 1.2 &mdash; Classification tree of sensors",
    "2.1": "Fig. 2.1 &mdash; Thermistor symbol, construction and its R&ndash;T characteristic",
    "2.2": "Fig. 2.2 &mdash; Thermistor in a voltage divider: the practical measuring circuit",
    "2.3": "Fig. 2.3 &mdash; LM35 connection diagram with ADC interface",
    "3.1": "Fig. 3.1 &mdash; Strain gauge, its mounting and the resistance change mechanism",
    "3.2": "Fig. 3.2 &mdash; Wheatstone bridge with strain gauges and instrumentation amplifier",
    "3.3": "Fig. 3.3 &mdash; Cantilever beam load cell with four strain gauges and HX711",
    "4.1": "Fig. 4.1 &mdash; LDR symbol, construction and principle",
    "4.2": "Fig. 4.2 &mdash; LDR voltage divider (light to voltage converter)",
    "4.3": "Fig. 4.3 &mdash; Photodiode in reverse bias (photoconductive mode)",
    "5.1": "Fig. 5.1 &mdash; Block diagram of a chemical sensor",
    "5.2": "Fig. 5.2 &mdash; Potentiometric (glass electrode) chemical sensor",
    "6.1": "Fig. 6.1 &mdash; MQ-2 construction and semiconductor sensing principle",
    "6.2": "Fig. 6.2 &mdash; MQ-2 interfacing circuit with load resistor and ADC",
    "7.1": "Fig. 7.1 &mdash; Piezoelectric accelerometer: construction and working",
    "7.2": "Fig. 7.2 &mdash; Simple vibration switch circuit with pull-up resistor",
    "8.1": "Fig. 8.1 &mdash; LVDT construction and its linear output characteristic",
    "8.2": "Fig. 8.2 &mdash; How a force sensor works (measuring chain)",
    "9.1": "Fig. 9.1 &mdash; Strain gauge torque sensor on a rotating shaft",
    "9.2": "Fig. 9.2 &mdash; Pressure sensing elements: Bourdon tube, bellows and diaphragm",
    "10.1": "Fig. 10.1 &mdash; Potentiometric position sensor circuit",
    "10.2": "Fig. 10.2 &mdash; Optical encoder for position and motion (speed / direction) sensing",
    "11.1": "Fig. 11.1 &mdash; Float, capacitive and ultrasonic level measuring methods",
    "11.2": "Fig. 11.2 &mdash; Orifice plate flow meter and other common types",
    "12.1": "Fig. 12.1 &mdash; DHT11 connection with pull-up resistor and decoupling capacitor",
    "12.2": "Fig. 12.2 &mdash; pH glass electrode with buffer amplifier and the pH scale",
    "13.1": "Fig. 13.1 &mdash; Soil moisture sensor probe with LM393 comparator module",
    "13.2": "Fig. 13.2 &mdash; Photoelectric and ionisation smoke sensing chambers",
    "14.1": "Fig. 14.1 &mdash; Sound sensor signal chain: microphone to microcontroller",
    "15.1": "Fig. 15.1 &mdash; Block diagram (architecture) of a smart sensor",
    "16.1": "Fig. 16.1 &mdash; Input-output characteristic showing linearity, dead zone, range and sensitivity",
    "16.2": "Fig. 16.2 &mdash; Hysteresis loop of a sensor",
    "16.3": "Fig. 16.3 &mdash; Dynamic response and bandwidth of a sensor",
    "17.1": "Fig. 17.1 &mdash; Position of the actuator in a closed loop control system",
    "18.1": "Fig. 18.1 &mdash; Control valve with positioner and I/P converter",
    "19.1": "Fig. 19.1 &mdash; SCR symbol and a latching lamp control circuit",
    "19.2": "Fig. 19.2 &mdash; TRIAC symbol and the classic TRIAC-DIAC dimmer circuit",
    "19.3": "Fig. 19.3 &mdash; MOSFET used as a switch to drive a DC motor with PWM",
    "20.1": "Fig. 20.1 &mdash; Relay driver circuit with base resistor and flyback diode",
    "20.2": "Fig. 20.2 &mdash; Solenoid and the solenoid operated valve",
    "21.1": "Fig. 21.1 &mdash; DC motor driven through an H-bridge with PWM speed control",
    "21.2": "Fig. 21.2 &mdash; Servo motor and its PWM angle control signal",
    "21.3": "Fig. 21.3 &mdash; Stepper motor with ULN2003 driver and energising sequence",
    "22.1": "Fig. 22.1 &mdash; Block diagram of a closed loop process control system",
    "22.2": "Fig. 22.2 &mdash; Continuous control versus discrete control output",
    "23.1": "Fig. 23.1 &mdash; Process lag: dead time and time constant of a first order process",
    "23.2": "Fig. 23.2 &mdash; Self regulating and non self regulating processes",
    "24.1": "Fig. 24.1 &mdash; Error, control band, control time and cycling in one response curve",
    "25.1": "Fig. 25.1 &mdash; Two position (ON-OFF) control with differential gap and the resulting cycling",
    "25.2": "Fig. 25.2 &mdash; Multi position control characteristic approaching proportional control",
    "26.1": "Fig. 26.1 &mdash; Proportional control leaves a permanent offset",
    "26.2": "Fig. 26.2 &mdash; Proportional action gives an instant step, integral action gives a ramp",
    "27.1": "Fig. 27.1 &mdash; Block diagram of a PID controller",
    "27.2": "Fig. 27.2 &mdash; Step response comparison of P, PI and PID control",
}

FIGS = {}


def figdef(key):
    """register a figure builder under its caption key"""
    def deco(fn):
        FIGS[key] = fn
        return fn
    return deco


def sheet(w=780, h=340):
    return Schematic(w, h)


# --------------------------------------------------------------------- #
#  drawing helpers built on the checked primitives
# --------------------------------------------------------------------- #
def panel(s, x0, y0, x1, y1, title=None, title_color=PUR):
    """dashed panel frame with an optional title on its top edge"""
    s.frame(x0, y0, x1, y1)
    if title:
        s.label((x0 + x1) / 2.0, y0 + 22, title, 15, title_color)


def arrow(s, x0, y0, x1, y1, color=None, dash=None, label=None,
          label_dy=-9, label_size=13, label_color=None):
    """signal-flow arrow (path, so it may be diagonal) with optional label"""
    s.path("M%g,%g L%g,%g" % (x0, y0, x1, y1),
           color=color or INK, width=2.6, dash=dash, arrow=True)
    if label:
        s.label((x0 + x1) / 2.0, (y0 + y1) / 2.0 + label_dy, label,
                label_size, label_color or (color or INK))


def chain(s, boxes, y, h=64, gap=46, size=15, arrow_labels=None):
    """horizontal block chain; boxes = list of line-lists.
    Returns the list of (x0, x1) of each box for wiring arrows."""
    x = 40.0
    out = []
    for i, lines in enumerate(boxes):
        widest = max(len(str(l)) for l in lines) * size * 0.52
        w = max(widest + 24, 110)
        s.textbox(x, y, x + w, y + h, lines, size=size, tag="chain%d" % i)
        out.append((x, x + w))
        if i:
            lab = (arrow_labels or [None] * len(boxes))[i]
            arrow(s, x - gap + 4, y + h / 2.0, x - 4, y + h / 2.0,
                  label=lab, label_dy=-8)
        x += w + gap
    return out


class _Dev:
    """a labelled box: .pin(name) gives the registered terminal point"""
    def __init__(self, box, terminals):
        self.box = box
        self._t = {nm: (float(x), float(y)) for nm, x, y in terminals}

    def pin(self, name):
        return self._t[name]


def dev(s, x0, y0, x1, y1, lines, terminals=None, size=14, tag="dev"):
    """labelled box with registered terminal points (wires may end there).
    terminals = [(name, x, y), ...] in ABSOLUTE coordinates."""
    s.textbox(x0, y0, x1, y1, lines, size=size, tag=tag)
    terms = list(terminals or [])
    for nm, x, y in terms:
        s.register(x, y, tag + "." + nm)
    return _Dev((x0, y0, x1, y1), terms)


def axes(s, x0, y0, x1, y1, xlabel, ylabel, xlab_dy=24, ylab_dx=-12):
    """L-shaped axes with arrow heads; returns origin (x0, y1)"""
    s.path("M%g,%g L%g,%g" % (x0, y1, x0, y0), width=2.6, arrow=True)
    s.path("M%g,%g L%g,%g" % (x0, y1, x1, y1), width=2.6, arrow=True)
    s.label((x0 + x1) / 2.0, y1 + xlab_dy, xlabel, 14)
    s.label(x0 + ylab_dx, y0 - 6, ylabel, 14, anchor="end")
    return (x0, y1)


def grid3(s, y=52):
    """standard page title inside a figure"""
    pass  # figures rely on <figcaption> for the title


# --------------------------------------------------------------------- #
#  verification / rendering
# --------------------------------------------------------------------- #
def render(key):
    """build one figure and return its <figure> html, or raise Collision"""
    if key not in FIGS:
        raise Collision("no builder registered for figure %s" % key)
    s = FIGS[key]()
    geo = s.check()
    con = s.check_pins()
    # named entities must become numeric before ElementTree sees the markup
    svg = H.safe_svg(s.svg(CAPS[key]))
    block_m = re.search(r"<svg.*?</svg>", svg, re.S)
    if not block_m:
        raise Collision("fig %s: no svg element produced" % key)
    block = block_m.group(0)
    probs = []
    try:
        ET.fromstring(block)
    except ET.ParseError as e:
        probs.append("XML not well formed: %s" % e)
    tprobs, _t = audit_block(block, key)
    probs += tprobs
    allp = geo + con + probs
    if allp:
        raise Collision("fig %s: %s" % (key, "  |  ".join(allp)))
    return svg


def render_all(verbose=True):
    """build every registered figure; returns (ok_keys, {key: error})"""
    ok, bad = [], {}
    for key in sorted(FIGS, key=lambda k: tuple(int(x) for x in k.split("."))):
        try:
            render(key)
            ok.append(key)
            if verbose:
                print("ok   fig %s" % key)
        except Collision as e:
            bad[key] = str(e)
            if verbose:
                print("FAIL fig %s\n     %s" % (key, e))
        except Exception as e:  # noqa: BLE001 - report, never crash the sweep
            bad[key] = "%s: %s" % (type(e).__name__, e)
            if verbose:
                print("FAIL fig %s\n     %s: %s" % (key, type(e).__name__, e))
    if verbose:
        print("\nfigures ok: %d   failed: %d   registered: %d"
              % (len(ok), len(bad), len(FIGS)))
    return ok, bad
