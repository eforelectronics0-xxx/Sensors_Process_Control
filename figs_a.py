# -*- coding: utf-8 -*-
"""figures for topics 1 - 4 (keys 1.1 .. 4.3)"""
from figures_core import (CAPS, arrow, axes, chain, dev, figdef, panel, sheet)
from circuit import BLU, GRN, INK, ORG, PUR, RED


# --------------------------------------------------------------------- #
@figdef("1.1")
def f_1_1():
    s = sheet(780, 250)
    boxes = [["Sensing", "element"],
             ["Conversion", "element"],
             ["Signal", "conditioning"],
             ["Display /", "Controller"]]
    xs = chain(s, boxes, y=60, h=64, gap=52, size=15)
    # input arrow + signal names above the chain
    arrow(s, 8, 92, xs[0][0] - 4, 92)
    s.label(83, 34, "physical quantity", 14, RED)
    m1 = (xs[0][1] + xs[1][0]) / 2.0
    m2 = (xs[1][1] + xs[2][0]) / 2.0
    m3 = (xs[2][1] + xs[3][0]) / 2.0
    s.label(m1, 52, "raw signal", 12, GRN)
    s.label(m3, 52, "clean signal", 12, GRN)
    # captions under each box
    caps = ["(faces the process)", "mech \u2192 electrical",
            "amplify, filter, scale", "gives the reading"]
    for (x0, x1), c in zip(xs, caps):
        s.label((x0 + x1) / 2.0, 150, c, 13, INK)
    s.label(390, 205, "A complete measuring system (measuring chain)", 17, PUR)
    return s


@figdef("1.2")
def f_1_2():
    s = sheet(780, 300)
    s.textbox(330, 36, 450, 72, ["SENSORS"], size=17, tag="root")
    heads = [("By quantity", 140), ("By power", 390), ("By output", 640)]
    for t, cx in heads:
        s.textbox(cx - 70, 108, cx + 70, 144, [t], size=15, tag="h" + t)
    s.path("M390,72 L390,90 M140,90 L640,90 "
           "M140,90 L140,108 M390,90 L390,108 M640,90 L640,108", width=2.4)
    s.path("M140,144 L140,160 M390,144 L390,160 M640,144 L640,160", width=2.4)
    s.textbox(40, 160, 240, 280,
              ["Temperature, Pressure", "Level, Flow, Force, Torque",
               "Position, Displacement", "Humidity, pH, Gas"],
              size=13, tag="q")
    s.textbox(280, 160, 500, 280,
              ["Active : own output energy", "(thermocouple, piezo)",
               "Passive : needs ext. source", "(LDR, thermistor, gauge)"],
              size=13, tag="p")
    s.textbox(540, 160, 740, 280,
              ["Analog : continuous value", "(LM35, LVDT, LDR)",
               "Digital : pulses / bits", "(encoder, DHT11, flow)"],
              size=13, tag="o")
    return s


# --------------------------------------------------------------------- #
@figdef("2.1")
def f_2_1():
    s = sheet(780, 275)
    # panel 1 - symbol
    panel(s, 20, 30, 240, 230, "symbol")
    t = s.place("therm", 7, 8, tag="TH")
    s.label(130, 221, "NTC thermistor", 14)
    # panel 2 - construction
    panel(s, 260, 30, 520, 230, "construction")
    s.path("M320,75 L320,112 M440,75 L440,112", width=2.6)
    s.path("M320,158 L320,195 M440,158 L440,195", width=2.6)
    s.textbox(300, 112, 460, 158, ["metal oxide bead"], size=14, tag="bead")
    s.label(316, 68, "Pt lead", 12, anchor="end")
    s.label(444, 68, "Pt lead", 12, anchor="start")
    s.label(380, 212, "glass / epoxy seal", 12)
    # panel 3 - R-T curve
    panel(s, 540, 30, 760, 230, "R\u2013T characteristic")
    axes(s, 570, 70, 740, 190, "temperature T", "R")
    s.path("M578,82 C630,92 700,140 732,180", width=3, color=RED)
    s.label(655, 252, "NTC : R falls when T rises", 12, GRN)
    return s


@figdef("2.2")
def f_2_2():
    s = sheet(780, 380)
    s.rail(40, 60, 740, 60, color=RED, label="+5 V")
    s.rail(40, 290, 740, 290, color=BLU, label="GND (0 V)")
    r1 = s.place("resv", 10, 7, label="R\u2081 = 10 k\u03a9",
                 label_side="right", tag="R1")
    th = s.place("therm", 10, 12, label="NTC thermistor R\u2082",
                 label_side="left", tag="TH")
    cap = s.place("cap", 14, 12, label="0.1 \u00b5F", label_side="right",
                  tag="C1")
    adc = s.place("adc", 22, 10, lines=["ADC"], tag="ADC")
    # +5 V -> R1 top
    s.wire_px([(200, 60), r1.pin("t")])
    s.junction(200, 60)
    # node = R1 bottom = therm top; junction + wire to cap top + wire to ADC
    node = r1.pin("b")                       # == th.pin("t") == (200,190)
    s.junction(node[0], node[1])
    s.wire_px([node, cap.pin("t")])
    s.junction(cap.pin("t")[0], cap.pin("t")[1])
    ai = adc.pin("i")
    s.wire_px([cap.pin("t"), (ai[0], cap.pin("t")[1]), ai])
    # therm bottom + cap bottom sit on the GND rail
    s.junction(th.pin("b")[0], th.pin("b")[1])
    s.junction(cap.pin("b")[0], cap.pin("b")[1])
    s.label(240, 178, "Vout", 13, GRN)
    s.label(390, 356, "Vout = 5 \u00d7 R\u2082 / (R\u2081 + R\u2082)", 16, PUR)
    return s


@figdef("2.3")
def f_2_3():
    from circuit_test import lm35
    return lm35()          # the corrected reference circuit, pin-to-pin


# --------------------------------------------------------------------- #
@figdef("3.1")
def f_3_1():
    s = sheet(780, 260)
    panel(s, 20, 30, 430, 230, "mounted on the test surface")
    # bar with the gauge grid on top
    s.textbox(70, 150, 390, 195, ["metal bar / specimen"], size=14, tag="bar")
    s.path("M110,150 L110,125 L150,125 L150,140 L190,140 L190,125 "
           "L230,125 L230,140 L270,140 L270,125 L310,125 L310,150",
           width=2.6, color=RED)
    s.path("M110,140 L110,150 M310,140 L310,150", width=2.6, color=RED)
    s.textbox(120, 78, 300, 118, ["strain gauge (foil grid)"], size=13,
              tag="gauge")
    s.label(80, 132, "F", 16, RED)
    s.label(355, 132, "F", 16, RED)
    s.path("M60,100 L60,140", width=2.4, color=RED, arrow=True)
    s.path("M365,100 L365,140", width=2.4, color=RED, arrow=True)
    s.label(230, 215, "gauge bonded with epoxy adhesive", 13)
    panel(s, 450, 30, 760, 230, "working")
    s.textbox(470, 62, 740, 210,
              ["Tension : grid lengthens \u2192 wire",
               "area falls \u2192 R INCREASES",
               "Compression : R decreases",
               "\u0394R / R = G \u00d7 \u03b5   (G = gauge factor)",
               "output \u2192 bridge \u2192 amplifier"],
              size=14, tag="work")
    return s


@figdef("3.2")
def f_3_2():
    s = sheet(780, 480)
    s.rail(40, 60, 740, 60, color=RED, label="+V excitation (5 V)")
    s.rail(40, 360, 740, 360, color=BLU, label="0 V")
    r1 = s.place("resv", 10, 7, label="R\u2081", label_side="left", tag="R1")
    r2 = s.place("resv", 10, 12, label="R\u2082", label_side="left", tag="R2")
    r3 = s.place("resv", 18, 7, label="R\u2083", label_side="right", tag="R3")
    r4 = s.place("resv", 18, 12, label="R\u2084", label_side="right", tag="R4")
    amp = s.place("opamp", 28, 10, label="instrumentation amplifier",
                  label_side="above", tag="U1")
    adc = s.place("adc", 34, 10, lines=["ADC"], tag="ADC")
    # excitation
    s.wire_px([(200, 60), r1.pin("t")]); s.junction(200, 60)
    s.wire_px([(360, 60), r3.pin("t")]); s.junction(360, 60)
    s.junction(r1.pin("b")[0], r1.pin("b")[1])   # node A
    s.junction(r2.pin("t")[0], r2.pin("t")[1])
    s.junction(r3.pin("b")[0], r3.pin("b")[1])   # node B
    s.junction(r4.pin("t")[0], r4.pin("t")[1])
    A = r1.pin("b"); B = r3.pin("b")
    p = amp.pin("p"); n = amp.pin("n")
    # bottom rail is fed by short stubs from R2/R4 (pins sit at y=290)
    s.wire_px([r2.pin("b"), (r2.pin("b")[0], 360)]); s.junction(r2.pin("b")[0], 360)
    s.wire_px([r4.pin("b"), (r4.pin("b")[0], 360)]); s.junction(r4.pin("b")[0], 360)
    # B (right midpoint) -> non-inverting input, routed above the bridge
    s.wire_px([B, (460, B[1]), (460, 150), (500, 150), (500, p[1]), p])
    # A (left midpoint) -> inverting input, routed UNDER the bridge but
    # inside the bottom rail (y=330 < 360) so nothing is crossed
    s.wire_px([A, (140, A[1]), (140, 330), (470, 330),
               (470, n[1]), n])
    s.label(170, 178, "A", 13, ORG)
    s.label(390, 178, "B", 13, ORG)
    s.wire_px([amp.pin("o"), adc.pin("i")])
    s.label(390, 412, "Balanced bridge : R\u2081/R\u2082 = R\u2083/R\u2084  \u2192  Vout = 0",
            14, PUR)
    s.label(390, 444, "With strain : Vout \u2248 (V/4) \u00d7 (\u0394R/R) \u00d7 n",
            14, PUR)
    return s


@figdef("3.3")
def f_3_3():
    s = sheet(780, 320)
    panel(s, 20, 30, 470, 230, "cantilever load cell")
    s.textbox(60, 140, 300, 185, ["cantilever beam (alloy steel)"],
              size=13, tag="beam")
    s.path("M60,120 L60,200 L75,200 L75,120 Z", width=2.6)   # fixed end
    s.label(66, 112, "fixed end", 12, anchor="start")
    s.path("M360,70 L360,130", width=2.6, color=RED, arrow=True)
    s.label(372, 60, "Load W (kg)", 14, RED)
    # four gauges as tagged boxes on the beam top/bottom
    s.textbox(130, 96, 180, 130, ["R1 R3"], size=13, tag="g1")
    s.textbox(200, 190, 250, 224, ["R2 R4"], size=13, tag="g2")
    s.label(245, 252, "R1,R3 tension  \u00b7  R2,R4 compression", 12, GRN)
    s.label(360, 165, "beam bends", 13, ORG)
    s.label(360, 185, "by \u0394L", 13, ORG)
    # digital chain
    arrow(s, 470, 130, 530, 130, label="mV")
    d = dev(s, 530, 90, 700, 170, ["HX711 amplifier", "+ 24-bit ADC"],
            size=14, tag="HX")
    arrow(s, 700, 130, 740, 130, label="digital", label_dy=-16)
    s.textbox(530, 200, 700, 250, ["\u00b5C reads weight"], size=14, tag="mc")
    s.path("M615,170 L615,200", width=2.4, arrow=True)
    s.label(390, 285, "F \u2192 strain \u2192 \u0394R \u2192 bridge \u2192 digital weight",
            15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("4.1")
def f_4_1():
    s = sheet(780, 260)
    panel(s, 20, 30, 240, 230, "LDR symbol")
    s.place("ldr", 7, 8, tag="LDR")
    s.label(130, 215, "light dependent resistor", 13)
    panel(s, 260, 30, 520, 230, "construction")
    s.textbox(290, 70, 490, 130,
              ["CdS layer on ceramic", "zig-zag metal contacts"],
              size=13, tag="cons")
    s.path("M310,130 L310,175 M470,130 L470,175", width=2.6)
    s.path("M300,175 L330,175 M450,175 L480,175", width=2.6)
    s.path("M295,60 L335,95 M285,48 L345,88", width=2.2, color=RED)
    s.path("M335,95 L325,93 M335,95 L332,85 M345,88 L335,86 M345,88 L342,78",
           width=2, color=RED)
    s.label(380, 205, "photo-conductive effect", 13, PUR)
    panel(s, 540, 30, 760, 230, "working")
    s.textbox(552, 62, 748, 210,
              ["Dark : few free carriers",
               "\u2192 R very high (M\u03a9)",
               "Light : photons free",
               "electrons \u2192 R falls",
               "(hundreds of \u03a9)"],
              size=13, tag="work")
    return s


@figdef("4.2")
def f_4_2():
    s = sheet(780, 370)
    s.rail(40, 60, 740, 60, color=RED, label="+5 V")
    s.rail(40, 290, 740, 290, color=BLU, label="0 V rail")
    r1 = s.place("resv", 10, 7, label="R = 10 k\u03a9", label_side="right",
                 tag="R1")
    ld = s.place("ldr", 10, 12, label="LDR", label_side="left", tag="LDR")
    adc = s.place("adc", 22, 10, lines=["ADC"], tag="ADC")
    s.wire_px([(200, 60), r1.pin("t")]); s.junction(200, 60)
    node = r1.pin("b")                        # == ld.pin("t")
    s.junction(node[0], node[1])
    ai = adc.pin("i")
    s.wire_px([node, (ai[0], node[1]), ai])
    s.junction(ld.pin("b")[0], ld.pin("b")[1])
    s.label(250, 178, "Vout", 13, GRN)
    s.label(390, 346, "Bright light \u2192 R falls \u2192 Vout falls",
            15, PUR)
    return s


@figdef("4.3")
def f_4_3():
    s = sheet(780, 370)
    s.rail(40, 60, 740, 60, color=RED, label="+5 V")
    s.rail(40, 290, 740, 290, color=BLU, label="0 V")
    r1 = s.place("resv", 10, 7, label="R\u2092 10 k\u03a9", label_side="right",
                 tag="R1")
    # rotate 180: the bar (cathode) now sits on top -> REVERSE biased
    pd = s.place("photodiode", 10, 12, rot=180, label="photodiode",
                 label_side="left", tag="PD")
    adc = s.place("adc", 22, 10, lines=["ADC"], tag="ADC")
    s.wire_px([(200, 60), r1.pin("t")]); s.junction(200, 60)
    node = r1.pin("b")              # == cathode of the rotated photodiode
    s.junction(node[0], node[1])
    ai = adc.pin("i")
    s.wire_px([node, (ai[0], node[1]), ai])
    s.junction(pd.pin("t")[0], pd.pin("t")[1])   # anode taps the 0 V rail
    s.label(305, 213, "to comparator", 13, GRN)
    s.label(390, 346, "reverse biased : current \u2261 light intensity",
            15, PUR)
    return s
