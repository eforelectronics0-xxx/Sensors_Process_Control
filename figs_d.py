# -*- coding: utf-8 -*-
"""figures for topics 20 - 27 (keys 20.1 .. 27.2)"""
from figures_core import (CAPS, arrow, axes, chain, dev, figdef, panel, sheet)
from circuit import BLU, GRN, INK, ORG, PUR, RED


# --------------------------------------------------------------------- #
@figdef("20.1")
def f_20_1():
    s = sheet(780, 470)
    s.rail(40, 60, 230, 60, color=RED, label="+5 V")
    s.rail(40, 400, 740, 400, color=BLU, label="0 V")
    relay = s.place("relay", 8, 7, tag="K")     # c1(160,90) c2(160,190)
    q = s.place("nmos" if False else "npn", 8, 12, tag="Q1")
    # npn: b(110,240) c(180,190) e(180,290)
    fd = s.place("diode", 4, 7, rot=180, label="1N4007", label_side="below",
                 tag="D1")                      # cathode(top)(80,90)
    s.wire_px([(160, 60), relay.pin("c1")]); s.junction(160, 60)
    s.wire_px([fd.pin("b"), (80, 60)]); s.junction(80, 60)
    # coil bottom -> collector, flyback anode taps the same node
    s.wire_px([relay.pin("c2"), q.pin("c")])
    s.junction(180, 190)
    s.wire_px([fd.pin("t"), (180, 190)])
    s.junction(160, 190)
    # emitter -> 0 V rail (routed right of the microcontroller)
    s.wire_px([q.pin("e"), (380, 290), (380, 400)]); s.junction(380, 400)
    # base resistor from the MCU pin (vertical resv below the base lead)
    rb = s.place("resv", 4, 14, label="Rb 1 k\u03a9", label_at=(45, 250),
                 tag="RB")                       # t(80,230) b(80,330)
    s.wire_px([rb.pin("t"), (80, 200), (110, 200), q.pin("b")])
    mcu = dev(s, 140, 345, 340, 390, ["microcontroller", "digital pin"],
              terminals=[("t", 160, 345)], size=13, tag="MCU")
    s.wire_px([rb.pin("b"), (80, 345), (160, 345)])
    # contact side switches a mains lamp
    ac = dev(s, 430, 55, 560, 135, ["230 V AC", "mains"],
             terminals=[("r", 560, 95), ("b", 495, 135)], size=13, tag="AC")
    s.wire_px([ac.pin("r"), (600, 95), (600, 40), (250, 40),
               (250, 116), relay.pin("no")])
    lamp = s.place("lamp", 16, 7, tag="LP")     # t(320,70) b(320,170)
    s.wire_px([relay.pin("nc"), (260, 164), (260, 50), (320, 50),
               lamp.pin("t")])
    s.wire_px([lamp.pin("b"), (320, 230), (495, 230), ac.pin("b")])
    s.label(245, 140, "NO / NC contact", 11, ORG)
    s.label(390, 455,
            "low power coil circuit controls the high power mains circuit",
            14, PUR)
    return s


@figdef("20.2")
def f_20_2():
    s = sheet(780, 320)
    panel(s, 20, 35, 370, 255, "solenoid with plunger")
    s.path("M80,80 L80,170 M150,80 L150,170", width=3, color=BLU)
    for y in (95, 115, 135, 155):
        s.path("M80,%d L150,%d" % (y, y), width=2, color=BLU)
    s.path("M115,60 L115,200", width=5, color=ORG)
    s.path("M100,200 L130,200 L130,225 L100,225 Z", width=2.6, color=ORG)
    s.label(60, 70, "coil", 12, BLU, anchor="end")
    s.label(175, 78, "fixed core", 11, anchor="start")
    s.label(175, 215, "movable plunger", 11, ORG, anchor="start")
    s.label(195, 145, "leads", 11, anchor="start")
    s.path("M150,125 L190,125", width=2)
    panel(s, 395, 35, 760, 255, "solenoid operated valve (actuator)")
    s.path("M440,170 L500,140 L500,200 Z", width=2.6)
    s.path("M500,170 L560,140 L560,200 Z", width=2.6)
    s.path("M420,170 L440,170 M560,170 L620,170", width=3)
    s.path("M530,100 L530,155", width=2.6)
    s.path("M505,75 L555,75 L555,100 L505,100 Z", width=2.6, color=BLU)
    s.label(585, 90, "solenoid", 11, BLU, anchor="middle")
    s.path("M640,170 L700,170", width=3, color=GRN, arrow=True)
    s.label(670, 152, "flow", 12, GRN, anchor="middle")
    s.label(530, 232, "coil ON \u2192 plunger lifts \u2192 valve opens",
            11, PUR, anchor="middle")
    s.label(390, 285,
            "used in water inlet, irrigation, door locks, car starting motor",
            15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("21.1")
def f_21_1():
    s = sheet(780, 350)
    mcu = dev(s, 30, 70, 190, 160, ["microcontroller", "IN1 IN2 EN"],
              terminals=[("r", 190, 115)], size=13, tag="MCU")
    arrow(s, 190, 115, 246, 115, label="logic", label_dy=-16, label_size=12)
    drv = dev(s, 250, 60, 460, 175, ["L293D", "H-bridge driver"],
              terminals=[("l", 250, 115), ("r", 460, 115)], size=15,
              tag="L293")
    arrow(s, 460, 115, 516, 115, label="motor leads", label_dy=-16,
          label_size=12)
    mot = dev(s, 520, 70, 690, 160, ["DC motor", "+12 V supply"],
              terminals=[("l", 520, 115)], size=15, tag="MOT")
    s.textbox(40, 200, 440, 310,
              ["IN1   IN2   EN      motor",
               " 0      0    x       stop",
               " 1      0    1      forward",
               " 0      1    1      reverse",
               " x      x   PWM      speed"],
              size=13, tag="truth")
    s.textbox(470, 200, 740, 310,
              ["EN pin gives PWM", "\u2192 speed control",
               "IN1 / IN2 give direction",
               "12 V separate from 5 V logic"],
              size=13, tag="notes")
    s.label(390, 338, "H-bridge : four switches flip the motor polarity",
            15, PUR)
    return s


@figdef("21.2")
def f_21_2():
    s = sheet(780, 340)
    panel(s, 20, 35, 330, 255, "servo motor")
    sv = s.place("servo", 8, 9, tag="SV")      # v(136,230) s(160,230) g(184,230)
    s.register(136, 248, "v.end"); s.register(160, 248, "s.end")
    s.register(184, 248, "g.end")
    s.wire_px([sv.pin("v"), (136, 248)])
    s.wire_px([sv.pin("s"), (160, 248)])
    s.wire_px([sv.pin("g"), (184, 248)])
    s.label(136, 266, "V +5 V", 12, RED, anchor="middle")
    s.label(160, 288, "S PWM", 12, ORG, anchor="middle")
    s.label(184, 310, "GND", 12, BLU, anchor="middle")
    s.label(160, 95, "closed loop : pot feedback inside", 12, PUR,
            anchor="middle")
    panel(s, 360, 35, 760, 255, "PWM signal for angle control")
    # pulse train: 1 ms .. 2 ms within a 20 ms period
    s.path("M400,190 L400,110 L455,110 L455,190 L560,190 L560,110 "
           "L640,110 L640,190 L730,190", width=3, color=RED)
    s.path("M400,210 L730,210", width=2, arrow=True)
    s.label(427, 100, "1 ms", 12, RED, anchor="middle")
    s.label(597, 100, "2 ms", 12, RED, anchor="middle")
    s.label(500, 232, "period 20 ms (50 Hz)", 12, anchor="middle")
    s.label(385, 118, "0\u00b0", 12, anchor="end")
    s.label(385, 205, "180\u00b0", 12, anchor="end")
    s.label(390, 300,
            "1.5 ms \u2192 90\u00b0 ; pulse width sets the angle", 14, PUR)
    s.label(390, 328,
            "applications : robotic arm, RC aircraft, CNC", 13, ORG)
    return s


@figdef("21.3")
def f_21_3():
    s = sheet(780, 330)
    drv = dev(s, 40, 70, 230, 175, ["ULN2003", "darlington array"],
              terminals=[("r1", 230, 105), ("r2", 230, 145)], size=14,
              tag="ULN")
    mot = s.place("stepper", 17, 7, label="stepper (28BYJ-48)",
                  label_side="above", tag="STP")   # a(290,110) b(290,170)
    #   c(390,110) d(390,170)
    s.wire_px([drv.pin("r1"), (265, 105), (265, 110), mot.pin("a")])
    s.wire_px([drv.pin("r2"), (265, 145), (265, 170), mot.pin("b")])
    s.label(258, 128, "IN1\u2013IN4", 12, BLU, anchor="middle")
    s.textbox(460, 70, 740, 195,
              ["sequence :", "1000 / 0100 / 0010 / 0001",
               "half stepping doubles the",
               "resolution (4096 steps/rev)"],
              size=13, tag="seq")
    s.textbox(40, 215, 440, 300,
              ["step angle 5.625\u00b0 / 64 gear ratio",
               "\u2192 0.0879\u00b0 per step",
               "applications : 3D printer, robotic",
               "gripper, textile machines"],
              size=13, tag="app")
    s.textbox(470, 215, 740, 300,
              ["ULN2003 : 7 darlington channels",
               "handles 500 mA per coil",
               "common freewheel diodes inside"],
              size=13, tag="uln")
    s.label(390, 322, "IN1\u2013IN4 sequence rotates the stepper", 15, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("22.1")
def f_22_1():
    s = sheet(780, 360)
    sp = dev(s, 20, 95, 90, 145, ["SP"], terminals=[("r", 90, 120)],
             size=15, tag="SP")
    sm = s.place("sum", 8, 6, tag="SUM")         # l(110,120) r(210,120) b(160,170)
    ctl = dev(s, 250, 85, 400, 165, ["CONTROLLER", "(P, I, PI, PID)"],
              terminals=[("l", 250, 120), ("r", 400, 120)], size=13,
              tag="CTL")
    fce = dev(s, 440, 85, 600, 165, ["FINAL CONTROL", "ELEMENT (valve)"],
              terminals=[("l", 440, 120), ("r", 600, 120)], size=13,
              tag="FCE")
    prc = dev(s, 640, 85, 760, 165, ["PROCESS", "(plant)"],
              terminals=[("l", 640, 120), ("b", 700, 165)], size=13,
              tag="PRC")
    s.wire_px([sp.pin("r"), sm.pin("l")])
    s.wire_px([sm.pin("r"), ctl.pin("l")])
    s.wire_px([ctl.pin("r"), fce.pin("l")])
    s.wire_px([fce.pin("r"), prc.pin("l")])
    sn = dev(s, 540, 235, 760, 295, ["SENSOR / TRANSMITTER"],
             terminals=[("r", 760, 265), ("l", 540, 265)], size=14,
             tag="SN")
    s.wire_px([prc.pin("b"), (700, 205), (760, 205), (760, 265)])
    s.wire_px([sn.pin("l"), (480, 265), (480, 305), (160, 305),
               sm.pin("b")])
    s.label(230, 105, "error e", 12, ORG)
    s.label(420, 105, "m.v.", 12, GRN)
    s.label(650, 318, "controlled variable (measured)", 12, PUR)
    s.label(330, 340, "feedback closes the loop", 13, PUR, anchor="middle")
    return s


@figdef("22.2")
def f_22_2():
    s = sheet(780, 300)
    panel(s, 20, 35, 370, 245, "continuous control")
    axes(s, 70, 75, 345, 200, "time", "PV", xlab_dy=26)
    s.path("M78,170 C140,168 190,120 250,110 C290,104 320,102 340,102",
           width=3, color=RED)
    s.path("M78,102 L340,102", width=1.8, color=BLU, dash="6 4")
    s.label(300, 92, "SP", 12, BLU, anchor="start")
    s.label(210, 140, "PV follows SP smoothly", 11, GRN, anchor="middle")
    panel(s, 400, 35, 760, 245, "discrete (ON/OFF) control")
    axes(s, 450, 75, 730, 200, "time", "output", xlab_dy=26)
    s.path("M458,120 L540,120 L540,175 L630,175 L630,120 L720,120",
           width=3, color=RED)
    s.label(490, 110, "ON", 12, RED, anchor="middle")
    s.label(585, 165, "OFF", 12, BLU, anchor="middle")
    s.label(590, 252, "only two states, nothing in between", 11, PUR,
            anchor="middle")
    s.label(390, 278,
            "continuous : every value in range \u00b7 discrete : ON and OFF only",
            14, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("23.1")
def f_23_1():
    s = sheet(780, 310)
    x0, y0, x1, y1 = 130, 55, 710, 220
    axes(s, x0, y0, x1, y1, "time", "output")
    # input step
    s.path("M140,205 L260,205 L260,90 L700,90", width=2, color=BLU,
           dash="7 5")
    s.label(175, 195, "input step applied", 11, BLU, anchor="start")
    # first-order output with dead time
    s.path("M260,205 C330,203 360,175 400,140 C450,100 520,95 690,93",
           width=3, color=RED)
    s.path("M400,205 L400,140", width=1.6, color=ORG, dash="4 3")
    s.label(330, 218, "dead time (transport lag)", 11, ORG, anchor="middle")
    s.path("M400,140 L400,90", width=1.4, color=PUR, dash="3 3")
    s.label(470, 130, "63.2 % of final value \u2192 \u03c4", 11, PUR,
            anchor="start")
    s.label(640, 80, "final value", 11, BLU, anchor="start")
    s.label(415, 278,
            "large process lag \u2192 controller must go slow", 14, PUR)
    return s


@figdef("23.2")
def f_23_2():
    s = sheet(780, 330)
    panel(s, 20, 35, 370, 255, "self regulating")
    s.path("M60,70 L60,200 L200,200 L200,70", width=2.8)
    s.path("M60,140 L200,140", width=2, color=BLU, dash="6 4")
    s.path("M100,55 L100,90", width=2.4, color=GRN, arrow=True)
    s.label(100, 46, "Qin", 12, GRN, anchor="middle")
    s.path("M200,175 L250,175", width=2.4, color=RED, arrow=True)
    s.label(268, 180, "Qout \u221d h", 12, RED, anchor="start")
    s.textbox(40, 210, 350, 248,
              ["outlet slows as h falls \u2192 level settles"],
              size=12, tag="sr")
    panel(s, 400, 35, 760, 255, "non self regulating")
    s.path("M440,70 L440,200 L580,200 L580,70", width=2.8)
    s.path("M440,140 L580,140", width=2, color=BLU, dash="6 4")
    s.path("M480,55 L480,90", width=2.4, color=GRN, arrow=True)
    s.label(480, 46, "Qin", 12, GRN, anchor="middle")
    s.path("M580,175 L630,175", width=2.4, color=RED, arrow=True)
    s.label(648, 180, "Qout = constant", 12, RED, anchor="start")
    s.textbox(420, 210, 740, 248,
              ["constant outflow \u2192 level keeps falling / rising"],
              size=12, tag="nsr")
    s.textbox(40, 275, 370, 320,
              ["self regulating : open loop OK, P gives offset"],
              size=12, tag="sr2")
    s.textbox(400, 275, 760, 320,
              ["non self regulating : controller compulsory (I action)"],
              size=12, tag="nsr2")
    return s


# --------------------------------------------------------------------- #
@figdef("24.1")
def f_24_1():
    s = sheet(780, 330)
    x0, y0, x1, y1 = 120, 50, 720, 230
    axes(s, x0, y0, x1, y1, "time", "level (%)")
    # set point line
    s.path("M130,120 L710,120", width=2, color=BLU, dash="7 5")
    s.label(700, 110, "set point (SP) 50 %", 12, BLU, anchor="end")
    # control band
    s.path("M130,100 L710,100", width=1.4, color=ORG, dash="3 3")
    s.path("M130,140 L710,140", width=1.4, color=ORG, dash="3 3")
    s.label(140, 92, "control band (proportional band)", 11, ORG,
            anchor="start")
    # PV cycling into the band
    s.path("M130,185 C200,150 260,105 330,100 C400,96 450,135 520,140 "
           "C590,144 640,112 705,108", width=3, color=RED)
    s.label(330, 175, "initial error e = SP \u2212 PV", 11, RED,
            anchor="middle")
    s.label(560, 165, "cycling (oscillation)", 11, PUR, anchor="middle")
    s.path("M330,215 L520,215", width=1.6, color=GRN, arrow=True)
    s.label(425, 208, "settling / control time", 11, GRN, anchor="middle")
    s.label(415, 298,
            "error, control band, control time and cycling in one plot",
            14, PUR)
    return s


@figdef("25.1")
def f_25_1():
    s = sheet(780, 330)
    panel(s, 20, 35, 760, 155, "controller output")
    axes(s, 70, 65, 730, 135, "error", "output", xlab_dy=18, ylab_dx=-10)
    s.path("M150,80 L390,80 L390,125 L640,125", width=3, color=RED)
    s.label(210, 70, "100 % (ON)", 11, RED, anchor="middle")
    s.label(560, 115, "0 % (OFF)", 11, BLU, anchor="middle")
    s.path("M360,60 L360,145", width=1.4, color=ORG, dash="3 3")
    s.path("M420,60 L420,145", width=1.4, color=ORG, dash="3 3")
    s.label(390, 98, "differential gap", 11, ORG, anchor="middle")
    panel(s, 20, 175, 760, 295, "process variable response")
    axes(s, 70, 200, 730, 275, "time", "PV", xlab_dy=18, ylab_dx=-10)
    s.path("M80,230 L720,230", width=1.8, color=BLU, dash="6 4")
    s.label(715, 222, "SP", 11, BLU, anchor="end")
    s.path("M80,255 C150,250 200,215 280,212 C360,209 420,248 500,252 "
           "C580,255 650,222 715,218", width=3, color=RED)
    s.label(575, 268, "cycling between the two limits", 11, PUR,
            anchor="middle")
    s.label(415, 320, "two position control with differential gap",
            14, PUR)
    return s


@figdef("25.2")
def f_25_2():
    s = sheet(780, 310)
    x0, y0, x1, y1 = 130, 50, 710, 230
    axes(s, x0, y0, x1, y1, "error", "output %")
    # staircase : 5 position mode
    s.path("M150,215 L250,215 L250,180 L350,180 L350,145 L450,145 "
           "L450,110 L550,110 L550,75 L650,75", width=3, color=RED)
    # proportional straight line
    s.path("M150,220 L680,60", width=2.4, color=BLU, dash="7 5")
    s.label(215, 200, "25 %", 11, RED, anchor="middle")
    s.label(315, 165, "50 %", 11, RED, anchor="middle")
    s.label(415, 130, "75 %", 11, RED, anchor="middle")
    s.label(620, 68, "100 %", 11, RED, anchor="middle")
    s.label(155, 232, "0 %", 11, RED, anchor="middle")
    s.textbox(430, 175, 700, 235,
              ["solid : multi position mode", "dashed : proportional",
               "more positions \u2192 closer to P"],
              size=12, tag="leg")
    s.label(415, 278,
            "multi position control approaches proportional control",
            14, PUR)
    return s


# --------------------------------------------------------------------- #
@figdef("26.1")
def f_26_1():
    s = sheet(780, 310)
    x0, y0, x1, y1 = 130, 50, 710, 225
    axes(s, x0, y0, x1, y1, "time", "PV")
    s.path("M140,90 L700,90", width=2, color=BLU, dash="7 5")
    s.label(695, 80, "set point", 12, BLU, anchor="end")
    # PV settles below SP
    s.path("M140,205 C220,180 300,130 390,122 C480,114 560,120 690,120",
           width=3, color=RED)
    s.path("M560,90 L560,120", width=2, color=ORG, arrow=True)
    s.path("M560,90 L560,120", width=1.6, color=ORG, dash="3 3")
    s.label(575, 108, "offset (residual error)", 12, ORG, anchor="start")
    s.label(300, 155, "PV rises, then stops short of SP", 11, RED,
            anchor="middle")
    s.label(415, 278,
            "proportional control leaves a permanent offset", 14, PUR)
    return s


@figdef("26.2")
def f_26_2():
    s = sheet(780, 310)
    panel(s, 20, 35, 370, 245, "proportional action")
    axes(s, 70, 75, 345, 200, "t", "output", xlab_dy=26)
    s.path("M78,175 L160,175 L160,95 L340,95", width=3, color=RED)
    s.label(240, 82, "instant step \u221d error", 11, RED, anchor="middle")
    s.path("M78,140 L340,140", width=1.6, color=BLU, dash="5 4")
    s.label(95, 132, "error", 11, BLU, anchor="start")
    panel(s, 400, 35, 760, 245, "integral action")
    axes(s, 450, 75, 730, 200, "t", "output", xlab_dy=26)
    s.path("M458,185 L720,95", width=3, color=PUR)
    s.label(560, 128, "ramp while error persists", 11, PUR, anchor="middle")
    s.path("M458,185 L560,185", width=1.6, color=BLU, dash="5 4")
    s.label(500, 177, "constant error", 11, BLU, anchor="middle")
    s.textbox(40, 260, 740, 305,
              ["P : instant but leaves offset    "
               "I : slow but removes offset entirely"],
              size=13, tag="cmp")
    return s


# --------------------------------------------------------------------- #
@figdef("27.1")
def f_27_1():
    s = sheet(780, 360)
    sp = dev(s, 20, 95, 90, 145, ["SP"], terminals=[("r", 90, 120)],
             size=15, tag="SP")
    sm1 = s.place("sum", 8, 6, tag="SUM")  # l(110,120) r(210,120) b(160,170)
    pid = dev(s, 250, 70, 470, 180,
              ["PID CONTROLLER", "K\u209a e", "K\u209a/T\u1d62 \u222be dt",
               "K\u209aT\u1d40 de/dt"],
              terminals=[("l", 250, 120), ("r", 470, 120)], size=13,
              tag="PID")
    fce = dev(s, 510, 85, 670, 165, ["FINAL CONTROL", "ELEMENT"],
              terminals=[("l", 510, 120), ("r", 670, 120)], size=13,
              tag="FCE")
    s.wire_px([sp.pin("r"), sm1.pin("l")])
    s.wire_px([sm1.pin("r"), pid.pin("l")])
    s.wire_px([pid.pin("r"), fce.pin("l")])
    s.label(230, 105, "e", 13, ORG)
    s.label(490, 110, "m", 13, GRN)
    # element output drops into the process, sensor feeds sum back
    prc = dev(s, 560, 220, 760, 300, ["process (plant)"],
              terminals=[("t", 660, 220), ("l", 560, 260)], size=14,
              tag="PRC")
    s.wire_px([fce.pin("r"), (720, 120), (720, 190), (660, 190),
               (660, 220)])
    s.wire_px([prc.pin("l"), (500, 260), (500, 315), (160, 315),
               sm1.pin("b")])
    s.label(330, 300, "feedback from sensor (PV)", 12, PUR, anchor="middle")
    s.label(415, 348,
            "P speed + I accuracy + D stability in one controller",
            14, PUR)
    return s

@figdef("27.2")
def f_27_2():
    s = sheet(780, 320)
    x0, y0, x1, y1 = 130, 50, 700, 230
    axes(s, x0, y0, x1, y1, "time", "PV")
    s.path("M140,95 L690,95", width=2, color=BLU, dash="7 5")
    s.label(685, 85, "SP", 12, BLU, anchor="end")
    # P only : fast, overshoots a bit, offset
    s.path("M140,215 C200,170 260,110 330,105 C420,99 520,128 690,130",
           width=2.6, color=RED)
    # PI : slower, no offset
    s.path("M140,215 C220,185 320,120 430,100 C520,86 600,96 690,95",
           width=2.6, color=ORG)
    # PID : fast and settles on SP
    s.path("M140,215 C190,165 250,100 310,95 C400,88 480,96 690,95",
           width=3.4, color=PUR)
    s.label(355, 145, "P only \u2014 fast, leaves offset", 11, RED,
            anchor="start")
    s.label(470, 115, "PI \u2014 no offset", 11, ORG, anchor="start")
    s.label(300, 80, "PID \u2014 fast, no offset", 11, PUR, anchor="start")
    s.label(415, 285,
            "P speed \u00b7 I accuracy \u00b7 D stability \u2014 PID has all three",
            14, PUR)
    return s
