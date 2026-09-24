# -*- coding: utf-8 -*-
"""Builds index.html : the master table of contents for the notes site."""
import os
from build_a import TOPICS, OUT
import helpers as H

# short note about the content of every topic (2nd column of the table)
WHAT = {
 1:  "Introduction &bull; Need of sensors &bull; Definition of sensor, transducer, transmitter &bull; Measuring chain &bull; Classification tree of sensors",
 2:  "Thermistor (NTC/PTC, construction, R&ndash;T curve, divider circuit) &bull; LM35 (pin-out, 10 mV/&deg;C, ADC interface) &bull; Comparison table",
 3:  "Stress &amp; strain, Hooke's law &bull; Strain gauge construction &bull; Gauge factor &bull; Wheatstone bridge &bull; Cantilever load cell with HX711",
 4:  "LDR construction (CdS) &bull; Photo-conductive effect &bull; Voltage divider circuit &bull; Photodiode &bull; Phototransistor &bull; Applications",
 5:  "Definition &bull; Receptor + transducer structure &bull; Electrochemical, optical, semiconductor, catalytic, piezoelectric, biosensors &bull; pH &amp; Clark electrode",
 6:  "MQ series &bull; MQ-2 construction (SnO&#8322; + heater) &bull; Semiconductor gas sensing principle &bull; Load resistor circuit &bull; ppm calculation &bull; Pre-heat",
 7:  "Need of vibration monitoring &bull; Piezoelectric accelerometer &bull; Vibration switch &bull; MEMS accelerometer &bull; Comparison &bull; Predictive maintenance",
 8:  "LVDT &bull; Capacitive &bull; Optical encoder &bull; Potentiometer &bull; Force sensors &bull; Proof body &bull; Measuring chain of a force sensor",
 9:  "Strain gauge torque sensor (&plusmn;45&deg;) &bull; Slip rings &bull; Magneto-elastic &bull; Bourdon tube &bull; Bellows &bull; Diaphragm &bull; Piezoresistive pressure",
 10: "Potentiometric &bull; LVDT &bull; Hall effect &bull; Rotary encoder (A/B/Z) &bull; Proximity &bull; Tachogenerator &bull; Variable reluctance &bull; IMU",
 11: "Float, displacer, hydrostatic, capacitive, ultrasonic, radar level &bull; Orifice, turbine, magnetic, vortex, rotameter flow meters",
 12: "DHT11 construction &bull; 40 bit single bus protocol &bull; Pull-up circuit &bull; pH glass electrode &bull; 59.16 mV/pH &bull; Buffer amplifier &bull; Calibration",
 13: "Soil probe + LM393 comparator &bull; Electrolysis problem &bull; Photoelectric smoke chamber &bull; Ionisation smoke chamber &bull; Fire alarm",
 14: "Electret condenser microphone &bull; Sound module AO/DO &bull; LM393 &bull; Dynamic, MEMS, piezo microphones &bull; Ultrasonic transducer &bull; Noise meter",
 15: "Definition &bull; Architecture block diagram &bull; Self calibration &amp; diagnosis &bull; Linearisation &bull; HART / Fieldbus / I&sup2;C &bull; Smart vs conventional",
 16: "Accuracy &bull; Resolution &bull; Threshold &bull; Impedance &bull; Sensitivity &bull; Hysteresis &bull; Linearity &bull; Range &bull; Reliability &bull; Selectivity &bull; Bandwidth &bull; Drift, MTBF",
 17: "Definition &bull; Principle (energy conversion + power amplification) &bull; Sensor vs Transducer vs Actuator &bull; Classification &bull; Selection criteria",
 18: "Globe, gate, ball, butterfly, needle, diaphragm valves &bull; I/P converter &bull; Positioner &bull; Cv &bull; PCV, PRV, safety valve &bull; Air to open / close",
 19: "SCR (P-N-P-N, latching, holding current) &bull; TRIAC (AC control, DIAC dimmer) &bull; MOSFET (voltage controlled, PWM drive) &bull; Comparison",
 20: "Relay construction (coil, armature, NO/NC) &bull; Driver circuit with flyback diode &bull; SSR, reed, contactor &bull; Solenoid plunger &bull; Solenoid valve",
 21: "DC motor + H-bridge &bull; Servo motor (PWM 1/1.5/2 ms) &bull; Stepper motor (ULN2003, step angle) &bull; AC induction motor (RMF, slip, VFD)",
 22: "Process &amp; control definitions &bull; Elements of a loop &bull; Continuous control &bull; Discrete / sequential control &bull; Composite control &bull; Open vs closed loop",
 23: "Process equation (tank example) &bull; Transfer function &bull; Process load &bull; Transfer, capacity and measurement lag &bull; Self vs non self regulation",
 24: "Error &amp; offset &bull; Variable range &amp; span &bull; Control parameter range (proportional band) &bull; Rise / settling / dead time &bull; Cycling &amp; hunting",
 25: "Two position (ON-OFF) mode &bull; Differential gap &bull; Cycling &bull; Multi position mode &bull; Stepped characteristic &bull; Comparison &bull; Thermostat examples",
 26: "Proportional mode &amp; offset &bull; Proportional band &bull; Integral (reset) action &amp; wind-up &bull; Derivative (rate) action &bull; Noise problem",
 27: "PI control &bull; PD control &bull; PID control &bull; Block diagram &bull; Response comparison &bull; Ziegler-Nichols tuning table &bull; Applications",
}

UNITS = [
 ("Unit I &mdash; Fundamentals of Sensors", 1, 16,
  "Definition, need and types of sensors; detailed study of temperature, stress/strain, light, chemical, gas, "
  "vibration, displacement, force, torque, pressure, position, motion, level, flow, humidity, pH, soil, smoke, "
  "sound and smart sensors with diagrams, construction, working and applications; and the eleven performance "
  "parameters of a sensor."),
 ("Unit II &mdash; Actuators", 17, 21,
  "Definition and principle of actuators, difference between sensor, transducer and actuator; pressure and flow "
  "control actuators (valves); power control devices SCR, TRIAC and MOSFET; magnetic control devices relay and "
  "solenoid; electromechanical motors &mdash; servo, DC, AC and stepper."),
 ("Unit III &mdash; Fundamentals of Process Automation", 22, 24,
  "Process control system and its elements; continuous, discrete state and composite control; process "
  "characteristics &mdash; process equation, load, lag and self regulation; control system parameters &mdash; "
  "error, variable range, control parameter range, control time and cycling."),
 ("Unit IV &mdash; Controller Modes", 25, 27,
  "Discontinuous modes &mdash; two position and multi position; continuous modes &mdash; proportional, integral "
  "and derivative; composite modes &mdash; PI, PD and PID with tuning and response comparison."),
]

FORMULAS = [
 ("Stress", "&sigma; = F / A"),
 ("Strain", "&epsilon; = &Delta;L / L &nbsp;&nbsp;and&nbsp;&nbsp; &sigma; = E &epsilon;"),
 ("Gauge factor", "G = (&Delta;R / R) / &epsilon;"),
 ("Bridge output", "V&#8339;&#8341;&#8348; &asymp; (V / 4) &times; G &times; &epsilon;"),
 ("Thermistor", "R<sub>T</sub> = R&#8320; e<sup>&beta;(1/T &minus; 1/T&#8320;)</sup>"),
 ("LM35", "V&#8339;&#8341;&#8348; = 10 mV &times; T (&deg;C)"),
 ("pH electrode", "E = 59.16 mV &times; pH at 25 &deg;C"),
 ("Voltage divider", "V&#8339;&#8341;&#8348; = V&#8345; &times; R&#8322; / (R&#8321; + R&#8322;)"),
 ("Torque &amp; power", "T = F &times; r &nbsp;&nbsp; P = 2&pi;NT / 60"),
 ("Pressure", "P = F / A &nbsp;&nbsp; and &nbsp;&nbsp; P = &rho; g h"),
 ("Orifice flow", "Q = C &times; A &times; &radic;(2&Delta;P / &rho;)"),
 ("Hall voltage", "V<sub>H</sub> = B I / (n e t)"),
 ("Encoder speed", "N (rpm) = (pulses/s &times; 60) / number of slots"),
 ("Induction motor", "N<sub>s</sub> = 120 f / P &nbsp;&nbsp; s = (N<sub>s</sub> &minus; N)/N<sub>s</sub>"),
 ("Servo PWM", "1 ms &rarr; 0&deg;, &nbsp; 1.5 ms &rarr; 90&deg;, &nbsp; 2 ms &rarr; 180&deg; (50 Hz)"),
 ("Valve flow", "Q = C<sub>v</sub> &radic;(&Delta;P / SG)"),
 ("Tank process", "A (dh/dt) + h/R = Q<sub>i</sub> &nbsp;&rarr;&nbsp; &tau; = AR"),
 ("First order response", "y(t) = K &Delta;u (1 &minus; e<sup>&minus;t/&tau;</sup>)"),
 ("Error", "e = SP &minus; PV"),
 ("Proportional band", "PB (%) = 100 / K<sub>p</sub>"),
 ("Proportional mode", "m = K<sub>p</sub> e + m&#8320;"),
 ("Integral mode", "m = K<sub>i</sub> &int; e dt + m&#8320;"),
 ("Derivative mode", "m = K<sub>d</sub> (de/dt) + m&#8320;"),
 ("PID mode", "m = K<sub>p</sub>[ e + (1/T<sub>i</sub>)&int;e dt + T<sub>d</sub>(de/dt) ] + m&#8320;"),
]

rows = []
for idx, (fname, unit, title, sub) in enumerate(TOPICS, start=1):
    short = title.split(" &middot; ", 1)[-1]
    rows.append(
        '<tr><td>%d</td><td>%s</td><td><a href="%s">%s</a></td><td>%s</td>'
        '<td><a class="btn" href="%s" style="text-decoration:none">Open</a></td></tr>'
        % (idx, unit.split(" &middot; ")[0], fname, short, WHAT[idx], fname))

table = ('<div class="tw"><table class="index">\n'
         '<tr><th>No.</th><th>Unit</th><th>Topic</th><th>What is covered in the note</th><th>Note</th></tr>\n'
         + "\n".join(rows) + '\n</table></div>\n')

unitblocks = []
for name, a, b, desc in UNITS:
    items = "".join('<li><a href="%s">%s</a></li>' % (TOPICS[i][0], TOPICS[i][2].split(" &middot; ", 1)[-1])
                    for i in range(a - 1, b))
    unitblocks.append(
        '<div class="unitblock"><span class="uh">%s</span>'
        '<p style="margin:8px 0 4px">%s</p>'
        '<ul class="arr" style="columns:2;column-gap:40px">%s</ul></div>' % (name, desc, items))

formrows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (k, v) for k, v in FORMULAS)

body = """
<div class="cover">
  <span class="unit-tag">Handwritten Notes &middot; Complete Syllabus</span>
  <div class="big">Sensors and<br>Process Control Systems</div>
  <div class="mid">All 27 topics &middot; one separate page for each</div>
  <div class="small">paragraph form notes &bull; hand drawn circuit diagrams &bull; comparison tables &bull;
  important formulae &bull; exam tips</div>
</div>
<div class="rule"></div>

<h2><span class="no">&#9998;</span>Index of all topics</h2>
<p>Every topic of the syllabus is kept in its <span class="b">own .html file</span>. Click any row to open
that note. Each note contains the <span class="g">diagram</span>, <span class="o">construction</span>,
<span class="p">working</span> and <span class="m">applications</span> written in simple paragraph form, with
hand drawn circuit and block diagrams made in SVG.</p>
""" + table + """

<h2><span class="no">&#9998;</span>Unit wise summary</h2>
""" + "\n".join(unitblocks) + """

<h2><span class="no">&#9998;</span>All important formulae on one page</h2>
<div class="tw"><table>
<tr><th>Quantity</th><th>Formula</th></tr>
""" + formrows + """
</table></div>

<h2><span class="no">&#9998;</span>How to use these notes</h2>
<ul class="tick">
  <li>Open any topic from the table above &mdash; each topic is a separate <code>.html</code> file, so you can
      send only the page you need on WhatsApp or by e-mail.</li>
  <li>Use the <span class="b">Blue / Red / Green</span> buttons at the top of every page to change the pen
      colour of the text, exactly like changing a pen while revising.</li>
  <li>Use the <span class="b">Print</span> button to get a clean black-on-white copy for the file. Diagrams
      are printed without the notebook background.</li>
  <li>Every page has <span class="b">Previous / Next</span> buttons at the bottom, so the whole syllabus can
      be read in sequence.</li>
  <li>Diagrams are drawn with <span class="b">SVG</span>, so they stay sharp at any zoom level and never get
      blurred like a scanned photo.</li>
</ul>
<div class="tip"><span class="cap">Study plan (14 days)</span>
Day 1&ndash;4 : Unit I sensors (3 topics per day) &nbsp;&bull;&nbsp; Day 5 : performance parameters &nbsp;&bull;&nbsp;
Day 6&ndash;8 : Unit II actuators &nbsp;&bull;&nbsp; Day 9&ndash;10 : Unit III process automation &nbsp;&bull;&nbsp;
Day 11&ndash;12 : Unit IV controller modes &nbsp;&bull;&nbsp; Day 13 : formula sheet + diagrams &nbsp;&bull;&nbsp;
Day 14 : full revision with the comparison tables.</div>
"""

html = H.page("index.html", "Sensors &amp; Process Control Systems",
              "Handwritten Notes", "Sensors and Process Control Systems &middot; Complete Index",
              body, None, (TOPICS[0][0], "Start Topic 1"))

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as fh:
    fh.write(html)
print("wrote index.html %d bytes, %d topic rows" % (len(html), len(rows)))
