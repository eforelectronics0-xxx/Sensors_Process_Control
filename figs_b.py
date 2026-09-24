# -*- coding: utf-8 -*-
"""figures for topics 5 - 11 (keys 5.1 .. 11.2)"""
import math

from figures_core import (CAPS, arrow, axes, chain, dev, figdef, panel, sheet)
from circuit import BLU, GRN, INK, ORG, PUR, RED


# --------------------------------------------------------------------- #
@figdef("5.1")
def f_5_1():
    s = sheet(780, 320)
    xs = chain(s, [["Sample", "(process fluid)"],
                   ["Receptor", "membrane"],
                   ["Receptor", "element"],
                   ["Transducer", "chem \u2192 elec"],
                   ["Display /", "controller"]],
               y=70, h=64, gap=40, size=13)
    labs = [None, "only the wanted ion", "chemical reaction",
            "electrical signal", None]
    for i in range(1, 5):
        x0, x1 = xs[i]
        arrow(s, x0 - 36, 102, x0 - 4, 102, label=labs[i], label_dy=-42,
              label_size=12)
    s.textbox(40, 175, 350, 235,
              ["receptor (recognition) +", "transducer (conversion)"],
              size=13, tag="note1")
    s.textbox(390, 175, 740, 235,
              ["selective membrane lets only", "the wanted species pass"],
              size=13, tag="note2")
    s.label(390, 285, "General structure of a chemical sensor", 17, PUR)
    return s


@figdef("5.2")
def f_5_2():
    s = sheet(780, 300)
    s.textbox(40, 70, 150, 170, ["test", "solution"], size=14, tag="soln")
    s.path("M95,70 L95,40 M95,40 L175,40", width=2.4)
    s.path("M60,55 L130,55", width=2.4, color=BLU, dash="6 4")
    s.label(95, 32, "beaker", 12, anchor="middle")
    # glass electrode
    s.path("M200,60 L200,150 L215,175 L245,175 L260,150 L260,60", width=2.8)
    s.path("M215,175 Q230,190 245,175", width=2.6, color=RED)
    s.textbox(168, 88, 292, 136, ["glass electrode", "(0.1 mm membrane)"],
              size=12, tag="ge")
    s.label(230, 205, "sensitive to H\u207a", 12, RED)
    # reference electrode
    s.path("M320,60 L320,175", width=2.8)
    s.path("M310,175 L330,175", width=2.8)
    s.textbox(302, 88, 422, 136, ["reference", "electrode (KCl)"],
              size=12, tag="ref")
    # buffer opamp block
    dev(s, 460, 85, 640, 165,
        ["high impedance buffer", "Zin > 10\u00b9\u00b2 \u03a9"],
        terminals=[("l", 460, 125), ("r", 640, 125)], size=14, tag="BUF")
    arrow(s, 414, 125, 456, 125)
    arrow(s, 640, 125, 700, 125, label="to ADC", label_dy=-16)
    # pH scale strip
    s.label(550, 205, "pH scale", 14, PUR)
    cols = [(RED, "0 acidic"), (ORG, "4"), (GRN, "7 neutral"), (BLU, "11"),
            (PUR, "14 alkaline")]
    x = 450.0
    for c, t in cols:
        w = len(t) * 12 * 0.52 + 14
        s.textbox(x, 220, x + w, 252, [t], size=12, color=c, tag="ph" + t)
        x += w + 4
    s.label(330, 285, "E = 59.16 mV per pH unit at 25 \u00b0C", 16, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("6.1")
def f_6_1():
    s = sheet(780, 300)
    panel(s, 20, 30, 380, 240, "construction")
    s.path("M100,70 L100,170 M260,70 L260,170", width=3)
    s.path("M100,70 L260,70 M100,170 L260,170", width=3)
    s.path("M108,85 L252,85 M108,100 L252,100", width=2, color=BLU)
    s.path("M130,70 L130,170 M170,70 L170,170 M210,70 L210,170 "
           "M250,70 L250,170", width=1.6, color=BLU)
    s.path("M140,120 L220,120 M140,120 L155,135 L185,105 L215,135 L220,120",
           width=2.4, color=RED)
    s.label(272, 84, "steel mesh cover", 12, BLU, anchor="start")
    s.label(180, 155, "heater coil inside", 12, RED)
    s.textbox(105, 175, 255, 210, ["SnO\u2082 on alumina tube"], size=13,
              tag="sno2")
    s.path("M140,210 L140,235 M220,210 L220,235", width=2.6)
    s.label(120, 232, "pins A, B, H", 12, anchor="end")
    panel(s, 410, 30, 760, 240, "working principle")
    s.textbox(430, 62, 740, 232,
              ["Clean air : oxygen ions on the",
               "surface trap electrons \u2192 R high",
               "Gas present : gas reacts with",
               "adsorbed oxygen \u2192 electrons free",
               "\u2192 R falls",
               "Rs (gas) / R\u2080 (air) \u2192 ppm"],
              size=13, tag="work")
    s.label(390, 275, "R\u209b decreases as gas ppm increases", 15, PUR)
    return s


@figdef("6.2")
def f_6_2():
    s = sheet(780, 390)
    s.rail(40, 60, 740, 60, color=RED, label="5 V")
    s.rail(40, 310, 740, 310, color=BLU, label="0 V")
    # MQ-2 between +5 V and the node; RL from the node down to 0 V
    dev(s, 150, 95, 250, 175, ["MQ-2", "Rs (gas)"],
        terminals=[("a", 200, 95), ("b", 200, 175)], size=14, tag="MQ2")
    s.wire_px([(200, 60), (200, 95)]); s.junction(200, 60)
    rl = s.place("resv", 10, 13, label="RL = 10 k\u03a9",
                 label_side="right", tag="RL")     # t=(200,210) b=(200,310)
    s.wire_px([(200, 175), rl.pin("t")])
    s.junction(200, 175)
    s.junction(200, 310)            # RL bottom pin sits exactly on the rail
    adc = s.place("adc", 22, 11, lines=["ADC"], tag="ADC")
    ai = adc.pin("i")               # (390,220)
    s.wire_px([rl.pin("t"), (ai[0], rl.pin("t")[1]), ai])
    s.junction(rl.pin("t")[0], rl.pin("t")[1])
    s.label(305, 198, "Vout", 13, GRN)
    s.label(420, 105, "Heater pins H1, H2 also need 5 V", 13, ORG)
    s.label(390, 366, "Vout = 5 \u00d7 RL / (Rs + RL)", 16, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("7.1")
def f_7_1():
    s = sheet(780, 300)
    panel(s, 20, 30, 400, 250, "construction")
    s.path("M70,70 L70,210 L300,210 L300,70", width=3)
    s.path("M70,70 Q185,40 300,70", width=3)
    s.label(185, 72, "base + steel case", 12, anchor="middle")
    s.textbox(140, 85, 260, 125, ["seismic mass (m)"], size=13, tag="mass")
    s.textbox(130, 140, 270, 180, ["piezo crystal (PZT)"], size=13,
              color=RED, tag="pz")
    s.path("M120,140 L120,180 M280,140 L280,180", width=2.4, color=BLU)
    s.path("M100,150 L120,150 M100,170 L120,170", width=2.4, color=BLU)
    s.label(95, 164, "C", 12, BLU, anchor="end")
    s.label(310, 160, "to charge amp", 12, anchor="start")
    panel(s, 430, 30, 760, 250, "working")
    s.textbox(450, 62, 740, 232,
              ["machine surface vibrates",
               "F = m \u00d7 a  acts on the crystal",
               "Q = d \u00d7 F   (d = piezo constant)",
               "V = Q / C",
               "charge \u2261 acceleration"],
              size=14, tag="work")
    s.label(390, 280, "piezoelectric accelerometer = vibration to voltage",
            15, PUR)
    return s


@figdef("7.2")
def f_7_2():
    s = sheet(780, 330)
    s.rail(40, 60, 740, 60, color=RED, label="5 V")
    s.rail(40, 270, 740, 270, color=BLU, label="0 V")
    r1 = s.place("resv", 6, 7, label="10 k\u03a9", label_side="right",
                 tag="R1")           # t=(120,90) b=(120,190)
    s.wire_px([(120, 60), r1.pin("t")]); s.junction(120, 60)
    # vibration switch = ball cavity, top terminal on the node row
    dev(s, 170, 190, 330, 255, ["metal ball", "inside cavity"],
        terminals=[("t", 240, 190), ("b", 240, 255)], size=13, tag="SW")
    s.path("M205,218 Q240,204 275,218 Q295,232 275,242 Q240,250 205,240 "
           "Q188,228 205,218", width=2.4, color=ORG)
    # node: R1 bottom -> switch top -> microcontroller input
    s.wire_px([r1.pin("b"), (360, 190)])
    s.junction(240, 190)
    s.junction(360, 190)            # corner where the MCU branch starts
    s.wire_px([(240, 255), (240, 270)]); s.junction(240, 270)
    dev(s, 400, 120, 620, 205, ["\u00b5C input", "(internal pull-up)"],
        terminals=[("i", 400, 162)], size=15, tag="MCU")
    s.wire_px([(360, 190), (360, 162), (400, 162)])
    s.label(330, 112, "pull-up holds the node HIGH", 13, ORG)
    s.label(300, 176, "vibration \u2192 contact \u2192 0", 13, GRN)
    s.label(390, 318, "ball touches \u2192 output LOW \u2192 \u00b5C alarm",
            15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("8.1")
def f_8_1():
    s = sheet(780, 300)
    panel(s, 20, 30, 420, 250, "LVDT construction")
    s.path("M60,100 L60,160 M360,100 L360,160", width=3)
    s.path("M60,100 L360,100 M60,160 L360,160", width=3)
    s.textbox(165, 108, 255, 152, ["primary P"], size=13, tag="pri")
    s.textbox(70, 108, 155, 152, ["S1"], size=13, tag="s1")
    s.textbox(265, 108, 350, 152, ["S2"], size=13, tag="s2")
    s.path("M120,185 L300,185", width=6, color=ORG)
    s.path("M300,185 L340,185", width=3, color=ORG)
    s.label(210, 215, "movable core (x)", 13, ORG)
    s.path("M140,235 L280,235", width=2, color=ORG, arrow=True)
    s.label(210, 72, "primary P with secondary S1 / S2", 12, anchor="middle")
    panel(s, 450, 30, 760, 250, "output characteristic")
    axes(s, 500, 70, 730, 190, "core position x", "Vout")
    s.path("M510,175 L615,90 L720,175", width=3, color=RED)
    s.label(615, 80, "null", 12, RED)
    s.label(560, 145, "slope = sensitivity", 12, GRN)
    s.label(390, 280, "Vout = |V(S1) \u2212 V(S2)| ; slope gives direction",
            15, PUR)
    return s


@figdef("8.2")
def f_8_2():
    s = sheet(780, 260)
    xs = chain(s, [["Force F"], ["Elastic", "element"],
                   ["Strain gauge", "(bridge)"], ["Amplifier"],
                   ["Display"]],
               y=75, h=60, gap=40, size=14)
    labs = [None, "\u0394L", "\u0394R", "voltage", None]
    for i in range(1, 5):
        x0, x1 = xs[i]
        arrow(s, x0 - 36, 105, x0 - 4, 105, label=labs[i], label_dy=-44,
              label_size=13)
    arrow(s, 8, 105, xs[0][0] - 4, 105, label="F", label_dy=-44,
          label_color=RED, label_size=14)
    s.label(390, 190, "F \u2192 strain \u2192 \u0394R \u2192 bridge \u2192 display",
            16, PUR)
    s.textbox(140, 215, 640, 248,
              ["dynamic / impact forces use a piezoelectric sensor"],
              size=13, tag="piezo")
    return s


# --------------------------------------------------------------------- #
@figdef("9.1")
def f_9_1():
    s = sheet(780, 340)
    panel(s, 20, 30, 470, 250, "on the rotating shaft")
    s.path("M60,120 L400,120 M60,170 L400,170", width=3)
    s.label(330, 100, "rotating shaft", 13, anchor="middle")
    s.textbox(125, 78, 255, 112, ["4 gauges at \u00b145\u00b0"], size=12,
              tag="g4")
    s.path("M150,170 L185,120 M200,170 L235,120 M255,170 L290,120 "
           "M305,170 L340,120", width=2.4, color=RED)
    s.label(230, 195, "torque T twists the shaft", 13, ORG)
    s.path("M80,60 L80,40", width=2.4, color=RED, arrow=True)
    s.label(80, 55, "T", 15, RED)
    s.path("M400,110 L430,110 M400,180 L430,180", width=2.4)
    s.label(428, 100, "slip rings", 12, anchor="start")
    dev(s, 500, 60, 700, 130, ["bridge + amplifier"],
        terminals=[("l", 500, 95), ("r", 700, 95)], size=15, tag="AMP")
    arrow(s, 432, 130, 496, 95, label="mV", label_dy=18)
    dev(s, 500, 170, 700, 240, ["ADC + \u00b5C"],
        terminals=[("l", 500, 205)], size=15, tag="ADC")
    arrow(s, 600, 132, 600, 166, label="digital", label_dy=0, label_size=12)
    s.label(390, 295, "T \u221d bridge output voltage", 16, PUR)
    return s


@figdef("9.2")
def f_9_2():
    s = sheet(780, 330)
    panel(s, 20, 30, 260, 250, "C-type Bourdon tube")
    s.path("M60,85 L60,105 Q60,180 150,180 Q210,180 210,130",
           width=4, color=BLU)
    s.path("M210,130 L210,105", width=2.6)
    s.label(95, 74, "pressure in", 12, BLU)
    s.label(150, 210, "tube straightens", 12, GRN)
    s.label(150, 232, "\u2192 tip moves", 12, GRN)
    panel(s, 285, 30, 515, 250, "bellows (low pressure)")
    s.path("M330,80 L330,175 M330,80 Q360,70 390,80 Q420,90 450,80 "
           "L450,175", width=3, color=BLU)
    s.path("M330,100 L450,100 M330,120 L450,120 M330,140 L450,140 "
           "M330,160 L450,160", width=2, color=BLU)
    s.path("M450,125 L490,125", width=2.4, arrow=True)
    s.label(390, 205, "\u0394x \u221d pressure", 13, GRN)
    s.label(390, 228, "for vacuum / low P", 12)
    panel(s, 540, 30, 760, 250, "diaphragm + gauges")
    s.path("M580,85 Q650,115 720,85", width=3.4, color=BLU)
    s.path("M580,175 Q650,145 720,175", width=3.4, color=BLU)
    s.label(650, 72, "P / \u0394P", 13, BLU)
    s.textbox(560, 190, 740, 240, ["strain gauges on diaphragm",
                                   "\u2192 bridge \u2192 mV out"], size=12,
              tag="dg")
    s.label(390, 285, "pressure transmitter : element + bridge + amplifier",
            15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("10.1")
def f_10_1():
    s = sheet(780, 330)
    s.rail(40, 60, 740, 60, color=RED, label="5 V")
    s.rail(40, 250, 740, 250, color=BLU, label="0 V")
    pot = s.place("pot", 11, 8, label="resistive track (L)",
                  label_side="right", tag="POT")
    # l -> +5 V rail, r -> 0 V rail, wiper -> ADC (routed below the body)
    s.wire_px([pot.pin("l"), (170, 60)]); s.junction(170, 60)
    s.wire_px([pot.pin("r"), (270, 250)]); s.junction(270, 250)
    adc = s.place("adc", 24, 9, lines=["ADC"], tag="ADC")
    w = pot.pin("w")                 # (220,210) bottom edge
    ai = adc.pin("i")                # (430,180)
    s.wire_px([w, (ai[0], w[1]), ai])
    s.label(305, 196, "wiper (x)", 13, GRN)
    s.label(390, 308, "Vout = 5 \u00d7 x / L   (joysticks, throttles)",
            16, PUR)
    return s


@figdef("10.2")
def f_10_2():
    s = sheet(780, 310)
    panel(s, 20, 30, 420, 250, "optical encoder")
    cx, cy, r = 165, 145, 62
    s.path("M%g,%g A%g,%g 0 1 1 %g,%g A%g,%g 0 1 1 %g,%g"
           % (cx - r, cy, r, r, cx + r, cy, r, r, cx - r, cy), width=3)
    for k in range(12):
        a0 = k * 30 * math.pi / 180.0
        s.path("M%g,%g L%g,%g" % (cx + 30 * math.cos(a0),
                                  cy + 30 * math.sin(a0),
                                  cx + r * math.cos(a0),
                                  cy + r * math.sin(a0)), width=2)
    s.label(cx, cy + 5, "disc", 14, anchor="middle")
    s.textbox(255, 75, 400, 120, ["LED"], size=14, tag="led")
    s.textbox(255, 165, 400, 210, ["photodiode"], size=14, tag="pd")
    s.path("M400,97 L430,97 L430,140 L400,140", width=2, color=RED)
    s.label(418, 130, "slots", 11, RED, anchor="end")
    s.label(165, 232, "encoder disc with slots", 12, anchor="middle")
    panel(s, 450, 30, 760, 250, "channels")
    axes(s, 490, 75, 740, 175, "time", "pulses")
    ya, yb = 110, 155
    s.path("M500,%g L530,%g L530,%g L570,%g L570,%g L610,%g L610,%g "
           "L650,%g L650,%g L690,%g" % (ya + 20, ya + 20, ya - 20, ya - 20,
                                          ya + 20, ya + 20, ya - 20,
                                          ya - 20, ya + 20, ya + 20),
           width=2.6, color=RED)
    s.path("M515,%g L545,%g L545,%g L585,%g L585,%g L625,%g L625,%g "
           "L665,%g L665,%g L705,%g" % (yb + 18, yb + 18, yb - 18,
                                          yb - 18, yb + 18, yb + 18,
                                          yb - 18, yb - 18, yb + 18,
                                          yb + 18),
           width=2.6, color=BLU)
    s.label(495, 105, "A", 14, RED, anchor="end")
    s.label(495, 150, "B", 14, BLU, anchor="end")
    s.label(615, 224, "pulses/s = speed", 13, GRN)
    s.label(615, 246, "phase of B vs A = direction", 13, GRN)
    return s


# --------------------------------------------------------------------- #
@figdef("11.1")
def f_11_1():
    s = sheet(780, 320)
    panel(s, 20, 30, 260, 250, "float type")
    s.path("M60,60 L60,210 L220,210 L220,60", width=2.6)
    s.path("M60,150 L220,150", width=2, color=BLU, dash="6 4")
    s.textbox(120, 100, 190, 140, ["float"], size=13, tag="fl")
    s.path("M155,100 L155,74", width=2.4)
    s.label(155, 68, "level \u2192 reading", 11, GRN)
    s.label(140, 232, "float moves \u2192 switch / pot", 11)
    panel(s, 285, 30, 515, 250, "capacitive probe")
    s.path("M325,60 L325,210 L475,210 L475,60", width=2.6)
    s.path("M325,160 L475,160", width=2, color=BLU, dash="6 4")
    s.path("M370,70 L370,190 M430,70 L430,190", width=3, color=RED)
    s.label(400, 68, "probe rods", 11, anchor="middle")
    s.label(400, 232, "C \u221d level \u2192 to \u00b5C", 12, GRN)
    panel(s, 540, 30, 760, 250, "ultrasonic (non-contact)")
    s.path("M575,60 L575,210 L725,210 L725,60", width=2.6)
    s.path("M575,165 L725,165", width=2, color=BLU, dash="6 4")
    s.textbox(605, 70, 695, 110, ["transducer"], size=12, tag="tr")
    s.path("M610,120 Q650,140 690,120", width=2, color=PUR, arrow=True)
    s.path("M610,135 Q650,155 690,135", width=2, color=PUR, arrow=True)
    s.label(650, 232, "h = (v \u00d7 t) / 2", 13, PUR)
    s.label(390, 285, "level sensing : contact and non-contact methods",
            15, PUR)
    return s


@figdef("11.2")
def f_11_2():
    s = sheet(780, 320)
    panel(s, 20, 30, 420, 250, "orifice plate in a pipe")
    s.path("M50,110 L390,110 M50,170 L390,170", width=3)
    s.path("M210,110 L210,140 M210,160 L210,170", width=4, color=RED)
    s.label(210, 98, "orifice plate", 12, RED)
    s.path("M170,170 L170,205 M260,170 L260,205", width=2.2)
    s.path("M170,205 L260,205", width=2.2)
    dev(s, 140, 210, 300, 250, ["DP transmitter"],
        terminals=[("t", 220, 210)], size=13, tag="DP")
    s.label(120, 140, "flow", 13, GRN)
    s.path("M70,140 L115,140", width=2.4, color=GRN, arrow=True)
    panel(s, 450, 30, 760, 250, "flow relation and other meters")
    s.label(605, 80, "Q = C \u00d7 A \u00d7 \u221a(2\u0394P/\u03c1)", 17, PUR)
    s.textbox(470, 105, 740, 245,
              ["Turbine : rotor speed \u221d flow",
               "Magnetic : V induced in liquid",
               "Vortex : shedding frequency",
               "Ultrasonic : Doppler / transit",
               "Rotameter : float in tapered tube",
               "Coriolis : true mass flow"],
              size=13, tag="meters")
    s.label(390, 290, "differential pressure family of flow meters",
            15, PUR)
    return s
