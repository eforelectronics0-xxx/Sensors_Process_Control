# -*- coding: utf-8 -*-
"""figures for topics 12 - 19 (keys 12.1 .. 19.3)"""
from figures_core import (CAPS, arrow, axes, chain, dev, figdef, panel, sheet)
from circuit import BLU, GRN, INK, ORG, PUR, RED


# --------------------------------------------------------------------- #
@figdef("12.1")
def f_12_1():
    s = sheet(780, 380)
    s.rail(40, 60, 740, 60, color=RED, label="+5 V")
    s.rail(40, 310, 740, 310, color=BLU, label="0 V rail")
    d = s.place("pkg4", 10, 5, lines=["DHT11", "1 VCC   2 DATA",
                                       "3 NC    4 GND"], tag="DHT")
    # v(160,150) d(180,150) n(200,150) g(220,150)
    cap = s.place("cap", 7, 13, label="100 nF", label_side="left", tag="C1")
    rl = s.place("resv", 17, 6, label="10 k\u03a9 pull-up",
                 label_side="right", tag="R1")
    # +5 V feeds DHT11 VCC via the cap node
    s.wire_px([cap.pin("t"), (140, 60)]); s.junction(140, 60)
    s.wire_px([(160, 150), (160, 180), (140, 180)])
    s.junction(140, 180)
    s.wire_px([(140, 210), (140, 180)]); s.junction(140, 180)
    # pull-up from +5 V to DATA node
    s.wire_px([(340, 60), rl.pin("t")]); s.junction(340, 60)
    # DATA wire to the microcontroller
    mcu = dev(s, 500, 80, 720, 160, ["\u00b5C / Arduino"],
              terminals=[("l", 500, 120)], size=15, tag="MCU")
    s.wire_px([(180, 150), (180, 200), (480, 200), (480, 120), (500, 120)])
    s.wire_px([rl.pin("b"), (340, 200)]); s.junction(340, 200)
    s.junction(180, 200)
    # GND + cap bottom on the rail
    s.wire_px([(220, 150), (220, 310)]); s.junction(220, 310)
    s.junction(140, 310)
    s.label(300, 188, "single-wire DATA", 12, GRN)
    s.label(390, 276,
            "4.7 k\u03a9 to 10 k\u03a9 pull-up on DATA is compulsory", 14, PUR)
    return s


@figdef("12.2")
def f_12_2():
    s = sheet(780, 340)
    # electrode pair feeding the buffer
    s.textbox(40, 70, 170, 160, ["glass +", "reference", "electrodes"],
              size=14, tag="el")
    arrow(s, 170, 115, 216, 115)
    dev(s, 220, 70, 440, 160, ["buffer amp", "Zin > 10\u00b9\u00b2 \u03a9"],
        terminals=[("l", 220, 115), ("r", 440, 115)], size=14, tag="BUF")
    arrow(s, 440, 115, 510, 115, label="to ADC", label_dy=-16)
    s.label(140, 55, "low pH \u2192 +mV", 12, RED)
    s.label(430, 55, "pH 7 \u2192 0 mV", 12, GRN)
    # pH scale
    s.label(390, 205, "pH scale", 15, PUR)
    cols = [(RED, "0  acidic"), (ORG, "4"), (GRN, "7  neutral"),
            (BLU, "11"), (PUR, "14  alkaline")]
    x = 155.0
    for c, t in cols:
        w = len(t) * 13 * 0.52 + 20
        s.textbox(x, 225, x + w, 263, [t], size=13, color=c, tag="ph" + t)
        x += w + 6
    s.label(390, 305, "slope = 59.16 mV per pH unit (25 \u00b0C)", 16, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("13.1")
def f_13_1():
    s = sheet(780, 380)
    s.rail(40, 60, 740, 60, color=RED, label="5 V")
    s.rail(40, 310, 740, 310, color=BLU, label="0 V")
    r1 = s.place("resv", 5, 6, label="10 k\u03a9", label_at=(210, 110),
                 tag="R1")                       # t(100,70) b(100,170)
    pr = s.place("probe", 9, 11, tag="PR")       # l(160,170) r(200,170)
    adc = s.place("adc", 22, 7, lines=["ADC"], tag="ADC")
    s.wire_px([(100, 60), r1.pin("t")]); s.junction(100, 60)
    # node = R1 bottom -> probe left rod
    s.wire_px([r1.pin("b"), pr.pin("l")])
    s.junction(130, 170)
    s.wire_px([(130, 170), (130, 140), (390, 140), adc.pin("i")])
    # probe right rod -> 0 V rail, routed clear of the probe body
    s.wire_px([pr.pin("r"), (240, 170), (240, 310)])
    s.junction(240, 310)
    s.label(300, 128, "analog out", 12, GRN)
    s.label(390, 272, "wet soil \u2192 R falls \u2192 Vout rises", 14, PUR)
    s.label(390, 360,
            "LM393 module : AO to ADC, DO to \u00b5C digital pin", 13, ORG)
    return s


@figdef("13.2")
def f_13_2():
    s = sheet(780, 310)
    panel(s, 20, 30, 380, 250, "photoelectric (optical) chamber")
    s.path("M70,90 L70,200 L330,200 L330,90 Z", width=2.8)
    s.textbox(85, 105, 175, 145, ["IR LED"], size=13, tag="led")
    s.textbox(225, 105, 315, 145, ["photodiode"], size=13, tag="pd")
    s.path("M175,125 L225,125", width=2, color=GRN)
    s.label(200, 115, "beam", 11, GRN, anchor="middle")
    s.path("M150,165 L210,185 M165,175 L225,195", width=2, color=ORG)
    s.label(195, 160, "smoke scatters light", 11, ORG, anchor="start")
    s.label(200, 228, "current drops \u2192 alarm", 12, PUR, anchor="middle")
    panel(s, 405, 30, 760, 250, "ionisation chamber")
    s.path("M450,90 L450,200 L710,200 L710,90 Z", width=2.8)
    s.textbox(465, 105, 575, 150, ["Am-241 source"], size=13, tag="am")
    s.textbox(595, 105, 695, 150, ["air gap"], size=13, tag="gap")
    s.path("M575,128 L595,128", width=2, color=RED, arrow=True)
    s.label(515, 175, "ions on smoke", 11, ORG, anchor="middle")
    s.path("M470,175 L690,175", width=1.8, color=BLU, dash="5 4")
    s.label(580, 228, "small current FALLS \u2192 alarm", 12, PUR,
            anchor="middle")
    s.label(390, 285,
            "both chambers give an electrical signal when smoke enters",
            15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("14.1")
def f_14_1():
    s = sheet(780, 300)
    xs = chain(s, [["microphone", "(capsule)"], ["amplifier"],
                   ["LM393", "comparator"], ["\u00b5C"]],
               y=75, h=64, gap=52, size=14)
    labs = [None, "mV signal", "DO", None]
    for i in range(1, 4):
        x0, x1 = xs[i]
        arrow(s, x0 - 48, 107, x0 - 4, 107, label=labs[i], label_dy=-44,
              label_size=13)
    arrow(s, 8, 107, xs[0][0] - 4, 107)
    s.label(95, 63, "sound waves", 12, RED, anchor="middle")
    # analogue branch from the amplifier down to the ADC path
    s.textbox(80, 175, 360, 235,
              ["AO : continuous analogue level", "DO : 0 / 1 above threshold"],
              size=13, tag="ao")
    s.textbox(400, 175, 700, 235,
              ["blue preset sets the DO threshold", "on the sensor module"],
              size=13, tag="pre")
    s.label(390, 272, "microphone \u2192 amplifier \u2192 threshold \u2192 \u00b5C",
            16, PUR)
    return s


@figdef("15.1")
def f_15_1():
    s = sheet(780, 320)
    panel(s, 30, 40, 750, 250, "SMART SENSOR PACKAGE")
    xs = chain(s, [["Sensing", "element"], ["Signal", "conditioning"],
                   ["ADC"], ["\u00b5Processor", "+ memory"],
                   ["Communication", "I\u00b2C / HART"]],
               y=95, h=70, gap=44, size=13)
    for i in range(1, 5):
        x0, x1 = xs[i]
        arrow(s, x0 - 40, 130, x0 - 4, 130)
    s.textbox(90, 190, 360, 240,
              ["calibration data, ID, alarm limits"], size=12, tag="mem")
    s.textbox(400, 190, 690, 240,
              ["self calibration, compensation, diagnostics"],
              size=12, tag="fn")
    arrow(s, 225, 165, 225, 190)
    arrow(s, 545, 165, 545, 190)
    s.label(390, 285,
            "smart sensor = sensor + conditioner + ADC + CPU + bus",
            15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("16.1")
def f_16_1():
    s = sheet(780, 310)
    x0, y0, x1, y1 = 130, 55, 700, 230
    axes(s, x0, y0, x1, y1, "input", "output")
    # ideal straight line and actual curve with dead zone
    s.path("M%g,%g L%g,%g" % (x0, y1, x1, y0 + 20), width=2, color=BLU,
           dash="7 5")
    s.path("M%g,%g L190,%g L640,%g L%g,%g"
           % (x0, y1, y1 - 6, y0 + 45, x1, y0 + 12), width=3, color=RED)
    s.label(175, y1 - 22, "dead zone", 12, ORG, anchor="start")
    s.label(455, y0 + 32, "ideal line", 12, BLU, anchor="start")
    s.label(500, y0 + 75, "actual curve", 12, RED, anchor="start")
    s.label(415, 176, "max deviation = non-linearity", 12, PUR,
            anchor="middle")
    s.label(415, 286, "range (span) \u00b7 sensitivity = slope",
            14, PUR, anchor="middle")
    return s


@figdef("16.2")
def f_16_2():
    s = sheet(780, 300)
    x0, y0, x1, y1 = 130, 55, 700, 225
    axes(s, x0, y0, x1, y1, "input", "output")
    # hysteresis loop: two arcs
    s.path("M200,%g C330,%g 470,%g 630,%g" % (y1 - 30, y0 + 20, y0 + 25,
                                                y1 - 25), width=3, color=RED)
    s.path("M200,%g C330,%g 470,%g 630,%g" % (y1 - 55, y0 + 45, y0 + 50,
                                                y1 - 50), width=3, color=BLU)
    s.label(255, y0 + 30, "increasing", 12, RED, anchor="start")
    s.label(470, y1 - 36, "decreasing", 12, BLU, anchor="start")
    s.path("M415,%d L415,%d" % (y0 + 42, y1 - 42), width=2, color=PUR,
           dash="5 4")
    s.label(415, y0 + 34, "hysteresis", 12, PUR, anchor="middle")
    s.label(415, y1 - 48, "error", 12, PUR, anchor="middle")
    s.label(415, 286, "output differs for the same input \u2014 max error",
            14, PUR, anchor="middle")
    return s


@figdef("16.3")
def f_16_3():
    s = sheet(780, 300)
    panel(s, 20, 35, 380, 245, "step response")
    axes(s, 70, 75, 350, 200, "t", "output", xlab_dy=26)
    s.path("M78,192 C130,190 170,150 210,115 L340,105", width=3, color=RED)
    s.path("M70,105 L345,105", width=1.8, color=BLU, dash="6 4")
    s.label(250, 95, "final value", 11, BLU, anchor="start")
    s.path("M150,192 L150,115", width=1.6, color=ORG, dash="4 3")
    s.label(160, 168, "rise time / \u03c4", 11, ORG, anchor="start")
    panel(s, 405, 35, 760, 245, "frequency response")
    axes(s, 455, 75, 730, 200, "f (Hz)", "gain", xlab_dy=26)
    s.path("M463,105 L600,105 C640,105 655,130 668,165 L720,195",
           width=3, color=RED)
    s.path("M463,140 L720,140", width=1.6, color=BLU, dash="6 4")
    s.label(675, 132, "\u22123 dB", 11, BLU, anchor="start")
    s.path("M668,75 L668,200", width=1.6, color=PUR, dash="4 3")
    s.label(660, 85, "bandwidth", 11, PUR, anchor="end")
    s.label(390, 278, "dynamic response : how fast and up to what frequency",
            15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("17.1")
def f_17_1():
    s = sheet(780, 320)
    # command in
    dev(s, 20, 95, 110, 155, ["command"], terminals=[("r", 110, 125)],
        size=14, tag="CMD")
    arrow(s, 110, 125, 156, 125, label="set point", label_dy=-16,
          label_size=12)
    c = dev(s, 160, 85, 300, 165, ["Controller", "(decision)"],
            terminals=[("l", 160, 125), ("r", 300, 125)], size=14, tag="CTL")
    arrow(s, 300, 125, 346, 125, label="control signal", label_dy=-16,
          label_size=12)
    a = dev(s, 350, 85, 500, 165, ["ACTUATOR", "signal \u2192 action"],
            terminals=[("l", 350, 125), ("r", 500, 125)], size=14, tag="ACT")
    arrow(s, 500, 125, 546, 125, label="power / motion", label_dy=-16,
          label_size=12)
    p = dev(s, 550, 85, 740, 165, ["PROCESS", "(plant, tank, motor)"],
            terminals=[("l", 550, 125), ("b", 645, 165)], size=14, tag="PRC")
    # feedback loop: process -> sensor -> controller
    sn = dev(s, 400, 225, 620, 285, ["Sensor (measures)"],
            terminals=[("r", 620, 255), ("l", 400, 255)], size=14, tag="SNS")
    arrow(s, 645, 165, 645, 225)
    arrow(s, 400, 255, 230, 255, label="feedback (measurement)",
          label_dy=-16, label_size=12, color=PUR)
    arrow(s, 230, 255, 230, 165, color=PUR)
    s.label(668, 200, "measured", 11, GRN, anchor="start")
    s.label(390, 308,
            "actuator completes the closed loop: signal \u2192 action",
            15, PUR)
    return s


@figdef("18.1")
def f_18_1():
    s = sheet(780, 340)
    panel(s, 20, 35, 330, 265, "globe control valve")
    # valve body: two triangles meeting at the seat
    s.path("M55,195 L105,170 L105,220 Z", width=2.6)
    s.path("M105,195 L155,170 L155,220 Z", width=2.6)
    s.path("M40,195 L55,195 M155,195 L200,195", width=3)
    s.path("M130,145 L130,195", width=2.6)
    s.path("M100,120 L160,120 L160,145 L100,145 Z", width=2.6)
    s.label(130, 110, "diaphragm actuator", 11, anchor="middle")
    s.label(130, 245, "plug moves \u2192 flow changes", 11, GRN,
            anchor="middle")
    s.label(50, 185, "air", 11, BLU, anchor="end")
    # I/P + positioner
    dev(s, 370, 60, 540, 130, ["I / P converter", "4\u201320 mA \u2192 3\u201315 psi"],
        terminals=[("r", 540, 95)], size=13, tag="IP")
    dev(s, 580, 60, 750, 130, ["Positioner", "(feedback)"],
        terminals=[("l", 580, 95), ("b", 665, 130)], size=13, tag="POS")
    arrow(s, 540, 95, 576, 95)
    arrow(s, 665, 130, 665, 178, color=BLU)
    s.label(690, 160, "air", 11, BLU, anchor="start")
    # stem position feedback
    s.path("M455,175 L455,245 L300,245 L300,215", width=2, color=PUR,
           dash="6 4", arrow=True)
    s.label(375, 262, "stem position feedback", 11, PUR, anchor="middle")
    dev(s, 370, 285, 750, 330,
        ["Controller \u2192 I/P \u2192 positioner \u2192 actuator \u2192 plug \u2192 flow"],
        size=13, tag="SEQ")
    return s


# --------------------------------------------------------------------- #
@figdef("19.1")
def f_19_1():
    s = sheet(780, 400)
    s.rail(40, 60, 740, 60, color=RED, label="+ V (AC or DC)")
    s.rail(40, 340, 740, 340, color=BLU, label="0 V")
    lamp = s.place("lamp", 6, 7, label="lamp", label_side="left",
                   tag="LP")                        # t(120,90) b(120,190)
    scr = s.place("scr", 6, 12, tag="SCR")          # a(120,190) k(120,290)
    s.wire_px([(120, 60), lamp.pin("t")]); s.junction(120, 60)
    s.junction(120, 190)          # lamp bottom pin == SCR anode pin
    s.wire_px([scr.pin("k"), (120, 340)]); s.junction(120, 340)
    # gate trigger: +V -> R -> push -> gate
    rg = s.place("resv", 14, 6, label="R\u2098 gate", label_side="right",
                 tag="RG")                            # t(280,70) b(280,170)
    pb = s.place("push", 14, 11, rot=90, tag="PB")
    # push rot90: top pin (280,170) bottom (280,270)
    s.wire_px([(280, 60), rg.pin("t")]); s.junction(280, 60)
    s.junction(280, 170)          # R bottom == push top
    g = scr.pin("g")              # (162,276)
    s.wire_px([(280, 270), (280, 276), (162, 276)])
    s.junction(280, 276)
    s.label(390, 392,
            "gate pulse \u2192 lamp ON and stays ON until current < holding",
            14, PUR)
    return s


@figdef("19.2")
def f_19_2():
    s = sheet(780, 430)
    s.rail(40, 60, 740, 60, color=RED, label="230 V AC (L)")
    s.rail(40, 370, 740, 370, color=BLU, label="neutral")
    lamp = s.place("lamp", 6, 7, label="lamp", label_side="left",
                   tag="LP")                  # t(120,90) b(120,190)
    tri = s.place("triac", 6, 12, tag="TR")   # t2(120,190) t1(120,290) g(162,278)
    s.wire_px([(120, 60), lamp.pin("t")]); s.junction(120, 60)
    s.junction(120, 190)                      # lamp b == MT2
    s.wire_px([tri.pin("t1"), (120, 370)]); s.junction(120, 370)
    # timing chain from MT2: R + pot (rheostat) to node J
    r = s.place("res", 11, 9, label="R 220 \u03a9", label_side="above",
                tag="RD")                     # l(170,180) r(270,180)
    pot = s.place("pot", 16, 9, label="pot 500 k", label_side="above",
                  tag="PT")                   # l(270,180) r(370,180) w(320,230)
    s.wire_px([(120, 190), (155, 190), (155, 180), r.pin("l")])
    s.junction(270, 180)                      # R right == pot left (rheostat in)
    # node J: pot wiper -> diac top and timing cap top
    diac = s.place("diac", 16, 14, label="DIAC", label_side="left", tag="DC")
    # diac t should sit on pot.w (320,230): cy=280 -> t=(320,230) yes
    cap = s.place("cap", 19, 14, label="0.1 \u00b5F", label_side="right",
                  tag="C1")                   # t(380,230) b(380,330)
    s.junction(320, 230)                      # pot.w == diac.t
    s.wire_px([(320, 230), cap.pin("t")])
    s.junction(380, 230)
    s.wire_px([cap.pin("b"), (380, 370)]); s.junction(380, 370)
    # diac bottom -> gate
    s.wire_px([diac.pin("b"), (320, 352), (162, 352), (162, 278)])
    s.junction(320, 352)
    s.label(390, 424, "Pot sets the firing angle \u2192 power in the load",
            14, PUR)
    return s


@figdef("19.3")
def f_19_3():
    s = sheet(780, 390)
    s.rail(40, 60, 740, 60, color=RED, label="+12 V")
    s.rail(40, 330, 740, 330, color=BLU, label="0 V")
    mot = s.place("motor", 14, 7, label="DC motor", label_side="right",
                  tag="M")                     # t(280,90) b(280,190)
    s.wire_px([(280, 60), mot.pin("t")]); s.junction(280, 60)
    # freewheel diode across the motor (cathode up -> rotate 180)
    fd = s.place("diode", 10, 7, rot=180, label="freewheel 1N4007",
                 label_side="left", tag="D1")  # b(top)(200,90) t(bot)(200,190)
    s.wire_px([fd.pin("b"), (200, 60)]); s.junction(200, 60)
    s.junction(280, 190)                       # motor b == diode a == drain node
    s.wire_px([fd.pin("t"), (280, 190)])
    # low-side NMOS switch
    q = s.place("nmos", 14, 12, tag="Q1")      # g(230,240) d(308,190) s(308,290)
    s.wire_px([(280, 190), q.pin("d")])        # along the shared top edge
    s.junction(280, 190)
    s.wire_px([q.pin("s"), (308, 330)]); s.junction(308, 330)
    # gate resistor from the microcontroller
    rg = s.place("res", 9, 12, label="gate R", label_side="above", tag="RG")
    # rg l(130,240) r(230,240) == gate pin
    mcu = dev(s, 20, 200, 110, 280, ["\u00b5C", "PWM"],
              terminals=[("r", 110, 240)], size=13, tag="MCU")
    s.wire_px([(110, 240), rg.pin("l")])
    s.junction(230, 240)                       # gate R right == gate pin
    s.label(118, 300, "PWM", 12, ORG, anchor="start")
    s.label(390, 386,
            "Vgs > threshold \u2192 channel forms \u2192 motor runs (PWM speed)",
            14, PUR)
    return s
