# -*- coding: utf-8 -*-
"""Builds topic pages 1 - 11 of the handwritten notes site."""
import os
import helpers as H
import figures_core
import figs_a, figs_b, figs_c, figs_d  # register the 55 builders

OUT = os.path.dirname(os.path.abspath(__file__))

TOPICS = [
    ("01-fundamentals-of-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 1 &middot; Introduction to Sensors", "Need, Definition, Types of Sensors"),
    ("02-temperature-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 2 &middot; Temperature Sensors", "Thermistor and LM35"),
    ("03-stress-strain-load-cells.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 3 &middot; Stress, Strain and Load Cells", "Strain Gauge, Wheatstone Bridge, Load Cell"),
    ("04-light-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 4 &middot; Light Sensors", "LDR and Photodiode"),
    ("05-chemical-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 5 &middot; Chemical Sensors", "Principle, Types, Working and Applications"),
    ("06-gas-sensors-mq2.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 6 &middot; Gas Sensors", "MQ-2 Gas / Smoke Sensor"),
    ("07-vibration-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 7 &middot; Vibration Sensors", "Accelerometer, Piezo and Vibration Switch"),
    ("08-displacement-force-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 8 &middot; Displacement and Force Sensors", "LVDT, Capacitive, Optical and Load based"),
    ("09-torque-pressure-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 9 &middot; Torque and Pressure Sensors", "Shaft Torque, Bourdon, Strain Gauge, Piezoresistive"),
    ("10-position-motion-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 10 &middot; Position and Motion Sensors", "Potentiometric, Inductive, Hall Effect, Encoder"),
    ("11-level-flow-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 11 &middot; Level and Flow Sensors", "Float, Capacitive, Ultrasonic, Orifice, Turbine"),
    ("12-humidity-ph-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 12 &middart; Humidity and pH Sensors", "DHT11 and Glass Electrode pH Sensor"),
    ("13-soil-smoke-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 13 &middot; Soil and Smoke Sensors", "Moisture Sensor and Smoke Detector"),
    ("14-sound-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 14 &middot; Sound Sensors", "Microphone Module, Sound Detector"),
    ("15-smart-sensors.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 15 &middot; Smart Sensors", "Architecture, Functions and Networks"),
    ("16-performance-parameters.html", "Unit I &middot; Fundamentals of Sensors",
     "Topic 16 &middot; Specifications &amp; Performance Parameters",
     "Accuracy, Resolution, Hysteresis, Linearity, Bandwidth ..."),
    ("17-actuators-introduction.html", "Unit II &middot; Actuators",
     "Topic 17 &middot; Introduction to Actuators",
     "Definition, Principle, Sensor vs Transducer vs Actuator"),
    ("18-control-valves.html", "Unit II &middot; Actuators",
     "Topic 18 &middot; Pressure &amp; Flow Control Actuators", "Control Valves and Positioners"),
    ("19-power-control-devices.html", "Unit II &middot; Actuators",
     "Topic 19 &middot; Power Control Devices", "SCR, TRIAC and MOSFET"),
    ("20-magnetic-control-devices.html", "Unit II &middot; Actuators",
     "Topic 20 &middot; Magnetic Control Devices", "Relay and Solenoid"),
    ("21-electromechanical-motors.html", "Unit II &middot; Actuators",
     "Topic 21 &middot; Electromechanical Motors", "Servo, DC, AC and Stepper Motors"),
    ("22-process-control-systems.html", "Unit III &middot; Fundamentals of Process Automation",
     "Topic 22 &middot; Process Control Systems",
     "Continuous, Discrete and Composite Control"),
    ("23-process-characteristics.html", "Unit III &middot; Fundamentals of Process Automation",
     "Topic 23 &middot; Process Characteristics",
     "Process Equation, Load, Lag and Self Regulation"),
    ("24-control-system-parameters.html", "Unit III &middot; Fundamentals of Process Automation",
     "Topic 24 &middot; Control System Parameters",
     "Error, Variable Range, Control Time and Cycling"),
    ("25-discontinuous-controller-modes.html", "Unit IV &middot; Controller Modes",
     "Topic 25 &middot; Discontinuous Controller Modes", "Two Position and Multi Position Modes"),
    ("26-continuous-controller-modes.html", "Unit IV &middot; Controller Modes",
     "Topic 26 &middot; Continuous Controller Modes", "P, I and D Control"),
    ("27-composite-controller-modes.html", "Unit IV &middot; Controller Modes",
     "Topic 27 &middot; Composite Controller Modes", "PI, PD and PID Control"),
]

# fix the accidental entity typo above
TOPICS = [(f, u, ti.replace("&middart;", "&middot;"), s) for f, u, ti, s in TOPICS]

SLUGS = [x[0] for x in TOPICS]


def nav(i):
    prev = (TOPICS[i - 1][0], "Prev") if i > 0 else None
    nxt = (TOPICS[i + 1][0], "Next") if i < len(TOPICS) - 1 else None
    return prev, nxt


def save(i, body):
    fname, unit, title, sub = TOPICS[i]
    prev, nxt = nav(i)
    html = H.page(fname, unit, title, sub, body, prev, nxt)
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote %-42s %6d bytes" % (fname, len(html)))


B = []  # collectors, one per topic

# ====================================================================== #
# TOPIC 1 : Fundamentals of Sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Introduction &mdash; Why do we need sensors?</h2>
<p class="q">Every automatic system in the world, from a small water level controller in our house to a
huge chemical plant, works on one simple idea: <span class="hl">first measure, then decide, then act</span>.
The part which does the "measuring" job is the <span class="b">sensor</span>. Without a sensor the
controller is like a person with closed eyes &mdash; it cannot know what is happening in the process, so it
cannot take a correct decision.</p>
<p class="q">The <span class="o">need of sensors</span> can be written in the following simple points:</p>
<ul class="tick">
  <li>To <span class="b">measure a physical quantity</span> (temperature, pressure, level, flow, position,
      force etc.) which the human eye cannot read continuously.</li>
  <li>To convert that quantity into an <span class="b">electrical signal</span> which wires, controllers and
      computers can understand.</li>
  <li>To give <span class="b">safety</span> &mdash; for example a gas sensor alarms before a leakage becomes
      dangerous, an over-temperature sensor cuts off a heater before the vessel bursts.</li>
  <li>To give <span class="b">quality control</span> &mdash; a process runs correctly only when its
      temperature, pH, pressure and flow stay inside limits.</li>
  <li>To give <span class="b">feedback</span> to the controller, so that automatic (closed loop) control
      becomes possible.</li>
  <li>To <span class="b">record data</span> for study, billing and troubleshooting.</li>
</ul>

<h2><span class="no">2</span>Definition of Sensor, Transducer and Transmitter</h2>
<div class="def"><span class="cap">Definition &mdash; Sensor</span>
A <b>sensor</b> is a device that <b>senses or detects</b> a physical quantity or a chemical condition of the
environment and gives an <b>output signal</b> (mostly electrical) which is a function of that quantity.
In simple words, a sensor is the <b>sense organ</b> of a machine.</div>
<div class="def"><span class="cap">Definition &mdash; Transducer</span>
A <b>transducer</b> is a device which <b>converts one form of energy into another form of energy</b>.
Example: a microphone converts sound energy into electrical energy.</div>
<div class="note"><span class="cap">Note (very often asked in exam)</span>
Every sensor is a transducer, but <b>every transducer is not a sensor</b>. A loudspeaker is a transducer
(electrical &rarr; sound) but it is not a sensor. A sensor always takes information <b>from</b> the process.
A <b>transmitter</b> is a transducer plus signal conditioning circuit which gives a <b>standard output</b>
such as 4&ndash;20 mA or 0&ndash;10 V so that the signal can travel far without noise.</div>

<h3>Basic building blocks of a sensor system</h3>
<p class="q">Any measuring system can be drawn as three blocks in a line: the <span class="b">sensing
element</span> which faces the process, the <span class="b">conversion element</span> which makes the
electrical signal, and the <span class="b">manipulation / signal conditioning element</span> which cleans and
scales the signal before it goes to the display or controller.</p>
""" + figures_core.render("1.1") + """

<h2><span class="no">3</span>Types of Sensors (Classification)</h2>
<p class="q">Sensors are classified in many ways. The most common classification is on the basis of
<span class="b">what they measure</span>. A second useful classification is <span class="b">active versus
passive</span> and <span class="b">analog versus digital</span>.</p>
""" + figures_core.render("1.2") + """
<div class="tw"><table>
<tr><th>Basis</th><th>Type</th><th>Example</th></tr>
<tr><td>Quantity measured</td><td>Temperature, pressure, level, flow, displacement, force, torque, humidity,
pH, gas, light, sound, vibration</td><td>LM35, Bourdon gauge, DHT11, MQ-2, LDR</td></tr>
<tr><td>Power requirement</td><td><b>Active</b> (self generating, no external supply needed)</td>
<td>Thermocouple, piezoelectric, photovoltaic cell</td></tr>
<tr><td>Power requirement</td><td><b>Passive</b> (needs external supply / excitation)</td>
<td>Thermistor, LDR, strain gauge, LVDT</td></tr>
<tr><td>Output signal</td><td><b>Analog</b> (continuous voltage/current/resistance)</td><td>LM35, LVDT, LDR</td></tr>
<tr><td>Output signal</td><td><b>Digital</b> (pulses, serial data)</td><td>DHT11, rotary encoder, smart sensor</td></tr>
<tr><td>Contact with process</td><td>Contact / Non-contact</td><td>Thermocouple (contact), IR pyrometer (non-contact)</td></tr>
<tr><td>Intelligence</td><td>Conventional / <b>Smart</b> sensor</td><td>Simple LDR / DHT11 with inbuilt &micro;C</td></tr>
</table></div>

<h2><span class="no">4</span>How a sensor is studied (method for every topic)</h2>
<p class="q">For every sensor in this unit we shall follow the same four headings, which is also the pattern
followed in the university question paper:</p>
<ol>
  <li><span class="g">Diagram</span> &mdash; the physical construction and the electrical circuit.</li>
  <li><span class="g">Construction</span> &mdash; which materials and parts are used.</li>
  <li><span class="g">Working</span> &mdash; the principle on which it converts the quantity into a signal.</li>
  <li><span class="g">Applications</span> &mdash; where it is actually used in industry and daily life.</li>
</ol>
<div class="tip"><span class="cap">Remember</span>
A sensor must be (i) <b>sensitive</b> only to the quantity to be measured, (ii) <b>fast</b> enough,
(iii) <b>rugged</b> enough to survive the plant atmosphere, and (iv) <b>cheap</b> enough to be used in
large numbers. No sensor is perfect; selecting a sensor is always a <b>compromise</b> between accuracy,
speed, cost and life.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">5</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> An ammeter has a range of 0&ndash;10 A and is marked accuracy class 0.5. Find the limiting error when it reads 6 A.</div>
<p class="q"><span class="b">Solution.</span> Maximum permissible error = 0.5 % of full scale = 0.5 &times; 10 / 100 = 0.05 A. So the true value lies between 6.00 &minus; 0.05 = 5.95 A and 6.00 + 0.05 = 6.05 A. Percentage error at this reading = 0.05 / 6.00 &times; 100 = 0.83 %. <span class="hl">Error = &plusmn;0.05 A (0.83 % at the 6 A reading).</span></p>
<h2><span class="no">6</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What is the difference between a sensor and a transducer?</span><br><span class="o">A.</span> A sensor directly senses the physical quantity; a transducer converts one form of energy into another. Many books use the two words loosely, but every transducer that also senses is treated as a sensor.</p>
<p class="q"><span class="b">Q2. Why is a transmitter used ahead of a controller?</span><br><span class="o">A.</span> To convert the weak sensor signal into a standard, noise-resistant signal such as 4&ndash;20 mA or 1&ndash;5 V so it can travel long cable lengths without loss.</p>
<h2><span class="no">7</span>Summary</h2>

<p class="q">In this topic we built the foundation for the whole subject: a sensor is the measuring eye of an automatic system, the measurement chain adds error block by block, and instruments are specified by range, span, accuracy class and uncertainty. Choosing a sensor is a four-question exercise &mdash; quantity, range, tolerance and output form &mdash; and every later topic on temperature, pressure, flow or control simply applies this same framework to one physical quantity at a time.</p>
<h2><span class="no">8</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Typical specification</th><th>Meaning</th></tr>
<tr><td>Input range</td><td>0&ndash;100 of the measured quantity</td><td>Safe measurable span</td></tr>
<tr><td>Span</td><td>URV &minus; LRV</td><td>Denominator of all % errors</td></tr>
<tr><td>Accuracy class</td><td>0.1, 0.2, 0.5, 1.0, 1.5, 2.5</td><td>Max error as % of full scale</td></tr>
<tr><td>Uncertainty</td><td>&plusmn;0.5 % of span</td><td>Guaranteed error band</td></tr>
<tr><td>Output signal</td><td>4&ndash;20 mA, 0&ndash;5 V, digital</td><td>What the controller receives</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 2 : Temperature sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Introduction to temperature measurement</h2>
<p class="q">Temperature is the most commonly measured quantity in any process industry &mdash; boilers,
distillation columns, plastic moulding, food processing, incubators and even our mobile phone battery.
The sensors used are broadly of two families: <span class="b">contact type</span> (thermocouple, RTD,
thermistor, IC sensor) which touch the body, and <span class="b">non-contact type</span> (infrared pyrometer)
which measures the radiated heat. In this topic we study the two most important ones for our syllabus:
the <span class="r">Thermistor</span> and the <span class="r">LM35</span>.</p>

<h2><span class="no">2</span>Thermistor (Thermally Sensitive Resistor)</h2>
<h3>2.1 Construction</h3>
<p class="q">A thermistor is made by sintering (baking at high temperature) a mixture of
<span class="b">semiconducting metal oxides</span> such as manganese, nickel, cobalt, copper and iron oxides
with a binder. The baked ceramic pellet is only a few millimetres in size. Two platinum or silver leads are
attached to it and the whole assembly is sealed inside a <span class="b">glass or epoxy coating</span> to
protect it from moisture and chemicals. Because the sensing bead is very small, the thermistor responds
<span class="hl">very fast</span> to a temperature change.</p>
""" + figures_core.render("2.1") + """
<h3>2.2 Types</h3>
<ul class="dot">
  <li><span class="b">NTC thermistor</span> (Negative Temperature Coefficient) &mdash; resistance
      <span class="r">decreases</span> when temperature increases. Most common type.</li>
  <li><span class="b">PTC thermistor</span> (Positive Temperature Coefficient) &mdash; resistance
      <span class="r">increases</span> when temperature increases. Used for over-current protection and
      motor starting.</li>
</ul>
<h3>2.3 Working</h3>
<p class="q">In a semiconductor the number of free charge carriers increases when it is heated. Therefore in
an NTC thermistor, more heat &rarr; more free electrons &rarr; <span class="b">lower resistance</span>.
The relation between resistance and temperature is exponential, not linear:</p>
<div class="formula">R<sub>T</sub> = R<sub>0</sub> &middot; e<sup>&beta;(1/T &minus; 1/T<sub>0</sub>)</sup>
&nbsp;&nbsp; where T is in kelvin and &beta; is the material constant (3000 &ndash; 5000 K)</div>
<p class="q">A thermistor is a <span class="b">passive device</span>, so it must be connected in a
<span class="b">voltage divider</span> with a fixed resistor and excited from a stable DC supply. The output
voltage at the junction changes with temperature and is read by the ADC of a microcontroller.</p>
""" + figures_core.render("2.2") + """
<h3>2.4 Applications of thermistor</h3>
<ul class="arr">
  <li>Temperature measurement in <span class="b">battery chargers, inverters and SMPS</span>.</li>
  <li><span class="b">Inrush current limiting</span> &mdash; PTC thermistor in series with the supply.</li>
  <li>Thermal protection of motors, transformers and power amplifiers.</li>
  <li>Digital thermometers, incubators, green-house controllers, air-conditioners.</li>
  <li>Cold-junction compensation of thermocouples and hot-wire anemometers (flow of air).</li>
</ul>
<div class="tw"><table>
<tr><th>Point</th><th>Thermistor</th></tr>
<tr><td>Sensitivity</td><td>Very high (about &minus;4 %/&deg;C, much more than RTD)</td></tr>
<tr><td>Range</td><td>&minus;50 &deg;C to +150 &deg;C (glass type up to 300 &deg;C)</td></tr>
<tr><td>Output</td><td>Resistance (non-linear)</td></tr>
<tr><td>Advantages</td><td>Cheap, small, very fast response, large output signal</td></tr>
<tr><td>Disadvantages</td><td>Non-linear, needs linearising circuit, limited range, self heating error</td></tr>
</table></div>

<h2><span class="no">3</span>LM35 Temperature Sensor IC</h2>
<h3>3.1 Introduction and Construction</h3>
<p class="q">The LM35 is a <span class="b">precision integrated-circuit temperature sensor</span> made in
silicon. Its output voltage is <span class="hl">directly proportional to the Celsius temperature</span>, so
no external calibration and no mathematics of subtraction is needed. It is available in three packages:
TO-92 (plastic, 3 pins &mdash; most common), TO-46 (metal can) and SOIC (surface mount). Inside the chip
there is a temperature sensing junction, a buffer amplifier and a reference circuit, all on one silicon die.</p>
<div class="tw"><table>
<tr><th>Pin (TO-92, flat side towards us)</th><th>Name</th><th>Function</th></tr>
<tr><td>Pin 1 (left)</td><td>V<sub>CC</sub></td><td>Supply +4 V to +30 V (normally +5 V)</td></tr>
<tr><td>Pin 2 (middle)</td><td>V<sub>OUT</sub></td><td>Analog output, 10 mV per &deg;C</td></tr>
<tr><td>Pin 3 (right)</td><td>GND</td><td>Ground / 0 V</td></tr>
</table></div>
<h3>3.2 Working</h3>
<p class="q">The forward voltage of a silicon junction falls by about 2 mV for every 1 &deg;C rise. The LM35
uses two matched junctions and an internal amplifier to produce a very clean output of exactly
<span class="b">10 mV/&deg;C</span>. That is, at 25 &deg;C the output is 250 mV and at 100 &deg;C it is 1 V.
The device draws only about 60 &micro;A, so self heating is less than 0.1 &deg;C in still air.</p>
<div class="formula">V<sub>OUT</sub> = 10 mV &times; T (&deg;C) &nbsp;&rarr;&nbsp; T = V<sub>OUT</sub> / 0.010 &deg;C</div>
""" + figures_core.render("2.3") + """
<h3>3.3 Applications of LM35</h3>
<ul class="arr">
  <li>Digital thermometers and temperature display panels.</li>
  <li>Temperature control of incubators, green houses, water heaters, CPU cooling fans.</li>
  <li>Cold junction compensation and battery management systems.</li>
  <li>Any student project with Arduino / 8051 because the interfacing is very simple.</li>
</ul>
<div class="tw"><table>
<tr><th>Parameter</th><th>Thermistor</th><th>LM35</th></tr>
<tr><td>Output</td><td>Resistance (non-linear)</td><td>Voltage, 10 mV/&deg;C (linear)</td></tr>
<tr><td>Range</td><td>&minus;50 to +150 &deg;C</td><td>&minus;55 to +150 &deg;C (0 to 100 &deg;C normally)</td></tr>
<tr><td>Accuracy</td><td>&plusmn;1 &deg;C to &plusmn;2 &deg;C</td><td>&plusmn;0.5 &deg;C at 25 &deg;C</td></tr>
<tr><td>Calibration</td><td>Needed (2 point)</td><td>Not needed (factory calibrated)</td></tr>
<tr><td>Supply</td><td>Needs divider supply</td><td>+4 V to +30 V</td></tr>
<tr><td>Cost / use</td><td>Very cheap, rugged</td><td>Cheap, easy to interface</td></tr>
</table></div>
<div class="warn"><span class="cap">Practical mistake to avoid</span>
Do not connect the LM35 pins wrongly. If V<sub>CC</sub> and GND are interchanged the chip becomes
<b>very hot within seconds</b> and gets damaged. Always keep the flat face towards you while soldering.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">4</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> An NTC thermistor has &beta; = 4000 K and R = 10 k&Omega; at T<sub>0</sub> = 298 K (25 &deg;C). Find its resistance at T = 308 K (35 &deg;C).</div>
<p class="q"><span class="b">Solution.</span> R<sub>T</sub> = R<sub>0</sub> &middot; e<sup>&beta;(1/T &minus; 1/T<sub>0</sub>)</sup> 1/T &minus; 1/T<sub>0</sub> = 1/308 &minus; 1/298 = 3.247&times;10<sup>&minus;3</sup> &minus; 3.356&times;10<sup>&minus;3</sup> = &minus;1.088&times;10<sup>&minus;4</sup> K<sup>&minus;1</sup> Exponent = 4000 &times; (&minus;1.088&times;10<sup>&minus;4</sup>) = &minus;0.435 R<sub>T</sub> = 10 &times; e<sup>&minus;0.435</sup> = 10 &times; 0.647 = 6.47 k&Omega; <span class="hl">R<sub>35&deg;C</sub> &asymp; 6.47 k&Omega; (resistance falls as temperature rises).</span></p>
<h2><span class="no">5</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Why is an NTC called negative temperature coefficient?</span><br><span class="o">A.</span> Its resistance decreases when temperature increases, unlike a metal RTD which shows a small positive coefficient.</p>
<p class="q"><span class="b">Q2. Give the LM35 sensitivity and supply range.</span><br><span class="o">A.</span> Sensitivity is 10 mV/&deg;C (0 V at 0 &deg;C); supply is +4 V to +30 V, typically +5 V.</p>
<h2><span class="no">6</span>Summary</h2>

<p class="q">Temperature measurement offers three workhorse devices: the thermistor for a large, cheap, non-linear resistance change over a short range; the RTD for stable, nearly linear precision; and integrated sensors like the LM35 that deliver a ready-made 10 mV/&deg;C voltage.</p>
<h2><span class="no">7</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>NTC thermistor</th><th>LM35</th></tr>
<tr><td>Range</td><td>&minus;40 to +125 &deg;C (device dependent)</td><td>+4 to +30 V supply</td></tr>
<tr><td>Output</td><td>Resistance (needs bridge)</td><td>10 mV/&deg;C, voltage</td></tr>
<tr><td>Typical accuracy</td><td>&plusmn;0.2 to &plusmn;1 &deg;C</td><td>&plusmn;0.5 &deg;C at 25 &deg;C</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 3 : Stress, Strain and Load Cells
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Stress, strain and the basic idea</h2>
<p class="q">When a force is applied on a body, the internal resisting force per unit area is called
<span class="b">stress</span> and the deformation produced (change in length per original length) is called
<span class="b">strain</span>. Strain is a ratio of two lengths, so it has <span class="hl">no unit</span>
and is expressed in microstrain (&micro;&epsilon;).</p>
<div class="formula">&sigma; = F / A &nbsp;&nbsp;(N/m&sup2; = Pa) &nbsp;&nbsp;&nbsp;&nbsp;
&epsilon; = &Delta;L / L &nbsp;&nbsp;&nbsp;&nbsp; &sigma; = E &times; &epsilon; &nbsp;(Hooke's law)</div>
<p class="q">Here <span class="b">E</span> is the modulus of elasticity (Young's modulus) of the material.
The sensor which measures strain is the <span class="r">strain gauge</span>, and a strain gauge mounted on a
properly shaped metal element becomes a <span class="r">load cell</span>.</p>

<h2><span class="no">2</span>Strain Gauge &mdash; Construction</h2>
<p class="q">A strain gauge consists of a very thin <span class="b">metallic foil or fine wire</span>
(constantan, nichrome or karma alloy) arranged in a zig-zag grid pattern and bonded between two thin insulating
backing sheets. The grid is bonded to the test surface with a special adhesive (epoxy or cyanoacrylate).
Two copper lead wires are soldered to the ends of the grid. The whole gauge is only a few millimetres square
and its nominal resistance is 120 &#937;, 350 &#937; or 1000 &#937;.</p>
""" + figures_core.render("3.1") + """
<h2><span class="no">3</span>Working of the strain gauge</h2>
<p class="q">When the surface stretches, the grid also stretches. Its length increases and its cross-section
decreases, so the <span class="b">resistance increases</span>. When the surface is compressed, the
resistance decreases. The sensitivity is expressed by the <span class="b">gauge factor</span>:</p>
<div class="formula">G = (&Delta;R / R) / &epsilon; &nbsp;&nbsp; (about 2 for metal foil gauges)</div>
<p class="q">The problem is that the change is <span class="hl">very small</span>. For example a 120 &#937;
gauge at 1000 &micro;&epsilon; changes only by 0.24 &#937;. Such a tiny change can never be measured with an
ordinary multimeter, so the gauge is always connected in a <span class="b">Wheatstone bridge</span>.</p>
""" + figures_core.render("3.2") + """

<h2><span class="no">4</span>Load Cell &mdash; Construction and Working</h2>
<p class="q">A <span class="b">load cell</span> is a complete transducer assembly in which
<span class="b">four strain gauges</span> are bonded on a properly designed elastic metal element
(alloy steel or aluminium) called the <span class="b">flexure / proof body</span>. Common shapes are
<span class="b">cantilever beam</span> (bending type, used in platform weighing),
<span class="b">S-type / tension-compression</span>, <span class="b">shear beam</span> and
<span class="b">column / pancake type</span> (used for very large loads).</p>
<p class="q">The four gauges are connected in a full Wheatstone bridge. When load is applied, two gauges are
in tension (R increases) and two are in compression (R decreases). This gives
<span class="hl">four times more output</span> than a single gauge and also cancels temperature error.
The output is a few millivolts per volt of excitation (for example 2 mV/V) which is amplified by an
<span class="b">HX711 / instrumentation amplifier</span> and then converted to digital by the ADC.</p>
""" + figures_core.render("3.3") + """
<h3>Applications of load cells</h3>
<ul class="arr">
  <li><span class="b">Electronic weighing machines</span> &mdash; kitchen scale, platform scale, weigh bridge
      for trucks.</li>
  <li>Hopper and silo weighing in cement, sugar and food industries.</li>
  <li>Force measurement in <span class="b">universal testing machines</span> (tensile / compression testing).</li>
  <li>Crane overload protection, torque wrenches, dynamometers.</li>
  <li>Medical bed weighing, baggage weighing at airports.</li>
</ul>
<div class="tip"><span class="cap">Important points for viva</span>
(i) Strain gauge is a <b>passive</b> transducer. (ii) Gauge factor G &asymp; 2. (iii) Bridge output is
<b>millivolts</b>, so amplification is compulsory. (iv) Four-gauge (full bridge) arrangement gives maximum
output and <b>automatic temperature compensation</b>. (v) Load cell is a <b>secondary</b> transducer because
it converts force &rarr; strain &rarr; resistance &rarr; voltage.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">5</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A strain gauge of 120 &Omega; with gauge factor GF = 2.0 is bonded to a beam. The strain is 500 &micro;&epsilon; (500&times;10<sup>&minus;6</sup>). Find the change in resistance and the bridge output if the supply is 5 V.</div>
<p class="q"><span class="b">Solution.</span> &Delta;R/R = GF &times; &epsilon; = 2.0 &times; 500&times;10<sup>&minus;6</sup> = 1.0&times;10<sup>&minus;3</sup> &Delta;R = 120 &times; 10<sup>&minus;3</sup> = 0.12 &Omega; For a quarter bridge, V<sub>out</sub> &asymp; (V<sub>s</sub>/4) &times; &Delta;R/R = 5/4 &times; 0.001 = 1.25 mV <span class="hl">&Delta;R = 0.12 &Omega;; bridge output &asymp; 1.25 mV.</span></p>
<h2><span class="no">6</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Define gauge factor.</span><br><span class="o">A.</span> GF = (&Delta;R/R) / &epsilon;, the fractional resistance change per unit strain; metal gauges are near 2, semiconductor gauges can exceed 100.</p>
<p class="q"><span class="b">Q2. Why is a Wheatstone bridge used with strain gauges?</span><br><span class="o">A.</span> The resistance change is tiny; the bridge converts it into a differential voltage and cancels common effects such as temperature drift.</p>
<p class="q"><span class="b">Q3. What does a quarter, half and full bridge mean?</span><br><span class="o">A.</span> One, two or four active gauges in the bridge arms; more active arms give more sensitivity and better temperature compensation.</p>
<p class="q"><span class="b">Q4. How does a load cell actually work?</span><br><span class="o">A.</span> Applied force strains a calibrated elastic body; bonded gauges read that strain, which is proportional to force within the elastic limit.</p>
<p class="q"><span class="b">Q5. Why do we need four load cells on a tank?</span><br><span class="o">A.</span> To support each leg, sum the weights, and remain accurate when the centre of gravity shifts off centre.</p>
<h2><span class="no">7</span>Summary</h2>

<p class="q">Stress and strain describe how a material deforms under load, a strain gauge turns that deformation into a fractional resistance change through the gauge factor, and a bridge plus amplifier lifts the millivolt signal to a usable level. Load cells package the same principle into calibrated force bodies used in weighing systems.</p>
<h2><span class="no">8</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Foil strain gauge</th><th>Load cell (0&ndash;500 kg)</th></tr>
<tr><td>Nominal resistance</td><td>120 &Omega; or 350 &Omega;</td><td>Bridge inside the package</td></tr>
<tr><td>Gauge factor</td><td>about 2 (metal)</td><td>Fixed by factory calibration</td></tr>
<tr><td>Sensitivity</td><td>1.25 mV/V (quarter bridge)</td><td>2 mV/V typical</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 4 : Light sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Introduction</h2>
<p class="q">A light sensor converts the <span class="b">intensity of light</span> falling on it into an
electrical quantity (resistance, current or voltage). The three most used devices are the
<span class="r">LDR</span> (photoresistor), the <span class="r">photodiode</span> and the
<span class="r">phototransistor</span>. Solar cells and opto-couplers also belong to this family.</p>

<h2><span class="no">2</span>LDR &mdash; Light Dependent Resistor</h2>
<h3>2.1 Construction</h3>
<p class="q">An LDR is made of a thin layer of <span class="b">high resistance semiconductor</span> such as
<span class="b">cadmium sulphide (CdS)</span> or cadmium selenide deposited on a ceramic insulating substrate.
On this layer a <span class="b">metallic contact</span> is deposited in a zig-zag (comb like) pattern so that
a long conducting path is obtained in a small area. The whole assembly is sealed inside a transparent glass
or plastic envelope. Two leads come out of it, so the LDR is a <span class="b">two terminal, non-polar</span>
device &mdash; it can be connected in any direction.</p>
""" + figures_core.render("4.1") + """
<h3>2.2 Working</h3>
<p class="q">The working of an LDR is based on the <span class="b">photo-conductive effect</span>. When
photons of light having energy greater than the band gap of the semiconductor strike the layer,
electron-hole pairs are created. These extra charge carriers increase the conductivity, so the
<span class="b">resistance falls</span> as the light intensity increases. In complete darkness the resistance
is called the <span class="b">dark resistance</span> (about 1 M&#937; to 10 M&#937;) and in bright light it
falls to a few hundred ohms.</p>
<p class="q">Because the LDR is a passive device, it is used in a <span class="b">potential divider</span>
circuit to obtain a varying voltage.</p>
""" + figures_core.render("4.2") + """
<h3>2.3 Applications</h3>
<ul class="arr">
  <li><span class="b">Automatic street lights</span> &mdash; lamp ON at night, OFF in day.</li>
  <li>Camera exposure (light meter) control.</li>
  <li>Burglar alarm using a light beam which is interrupted.</li>
  <li>Smoke detectors (light scattering type), flame detectors.</li>
  <li>Contrast and brightness control in photocopiers.</li>
</ul>
<div class="tw"><table>
<tr><th>Property</th><th>Value / Remark</th></tr>
<tr><td>Dark resistance</td><td>1 M&#937; &ndash; 10 M&#937;</td></tr>
<tr><td>Bright light resistance</td><td>100 &#937; &ndash; 1 k&#937;</td></tr>
<tr><td>Response time</td><td>Slow (10 ms to 100 ms)</td></tr>
<tr><td>Peak sensitivity</td><td>CdS ~ 550 nm (green), CdSe ~ 720 nm (infra red)</td></tr>
<tr><td>Advantages</td><td>Cheap, high sensitivity, easy to use, no polarity</td></tr>
<tr><td>Disadvantages</td><td>Slow, temperature sensitive, contains cadmium (hazardous), non-linear</td></tr>
</table></div>

<h2><span class="no">3</span>Photodiode and Phototransistor (brief)</h2>
<p class="q">A <span class="b">photodiode</span> is a PN junction diode operated in
<span class="b">reverse bias</span>. Light creates electron-hole pairs which are swept across the junction
and produce a small reverse current proportional to light intensity. It is <span class="hl">very fast</span>
(nano-seconds) and is used in optical communication, barcode readers and encoders. A
<span class="b">phototransistor</span> is the same idea but with transistor amplification built in, so it
gives a much larger current (100 times) but is slightly slower.</p>
""" + figures_core.render("4.3") + """
<div class="note"><span class="cap">Exam tip</span>
If the question is only "LDR", draw Fig. 4.1 and Fig. 4.2, write the construction, the photo-conductive
principle, the dark/bright resistance values and 4 applications. If the question is "light sensors" in
general, add photodiode, phototransistor and solar cell in one line each.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">4</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> An LDR has 1 k&Omega; in bright light and 200 k&Omega; in darkness. It is used with a 10 k&Omega; series resistor across a 5 V supply. Find V<sub>out</sub> in both cases (voltage across the LDR).</div>
<p class="q"><span class="b">Solution.</span> Bright: V<sub>out</sub> = 5 &times; 1 / (1 + 10) = 0.45 V. Dark: V<sub>out</sub> = 5 &times; 200 / (200 + 10) = 4.76 V. A comparator with threshold near 2.5 V therefore gives a clean light/dark digital output. <span class="hl">V<sub>bright</sub> = 0.45 V, V<sub>dark</sub> = 4.76 V.</span></p>
<div class="formula"><span class="b">Problem 2.</span> A photodiode with responsivity R = 0.55 A/W at 850 nm is illuminated with 200 &micro;W of laser power. Find the photocurrent and the voltage across a 10 k&Omega; load resistor.</div>
<p class="q"><span class="b">Solution.</span> I<sub>ph</sub> = R &times; P = 0.55 &times; 200&times;10<sup>&minus;6</sup> = 110 &micro;A. V<sub>out</sub> = I<sub>ph</sub> &times; R<sub>L</sub> = 110&times;10<sup>&minus;6</sup> &times; 10&times;10<sup>3</sup> = 1.1 V Response time of a reverse-biased diode is in nanoseconds, much faster than an LDR. <span class="hl">I<sub>ph</sub> = 110 &micro;A, V<sub>out</sub> = 1.1 V.</span></p>
<h2><span class="no">5</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Why is a photodiode operated in reverse bias?</span><br><span class="o">A.</span> Reverse bias widens the depletion layer, reduces junction capacitance and makes the response much faster; photocurrent is then almost linear with light power.</p>
<p class="q"><span class="b">Q2. What is the dark current?</span><br><span class="o">A.</span> The small current that flows with no light, caused by thermal generation; it sets the lowest detectable light level.</p>
<p class="q"><span class="b">Q3. Why does an LDR response depend on light history?</span><br><span class="o">A.</span> CdS has a memory effect &mdash; resistance rises and falls slowly, so it is slow to recover after bright light, which makes it unsuitable for fast signals.</p>
<p class="q"><span class="b">Q4. How does a phototransistor differ from a photodiode?</span><br><span class="o">A.</span> Base light current is amplified by the transistor action, giving 100&times; more sensitivity but slower speed and less linearity.</p>
<p class="q"><span class="b">Q5. Name an application where a photodiode array is used.</span><br><span class="o">A.</span> Position-sensing, barcode readers, optical encoders and short-range fibre-optic links.</p>
<p class="q"><span class="b">Q6. What is the photovoltaic mode?</span><br><span class="o">A.</span> The diode is left unbiased and generates a voltage like a small solar cell; it is very linear but slower than reverse-biased operation.</p>
<h2><span class="no">6</span>Summary</h2>

<p class="q">Light measurement uses either a photoconductor whose resistance falls with illumination (LDR) or junction devices that generate a photocurrent (photodiode, phototransistor). Linearity, speed and spectral response decide which family fits the job: LDRs for simple switching, photodiodes for fast and proportional measurement. Dark current, load resistance and bias conditions together set the smallest light level the circuit can reliably see.</p>
<h2><span class="no">7</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>LDR (CdS)</th><th>Silicon photodiode</th></tr>
<tr><td>Dark resistance</td><td>0.2&ndash;2 M&Omega;</td><td>Dark current 1&ndash;20 nA</td></tr>
<tr><td>Light resistance</td><td>few k&Omega; at 10 lux</td><td>&mdash; photocurrent instead</td></tr>
<tr><td>Response time</td><td>20&ndash;100 ms (slow)</td><td>ns to &micro;s</td></tr>
<tr><td>Spectral peak</td><td>about 540 nm</td><td>about 900 nm (near IR)</td></tr>
<tr><td>Sensitivity</td><td>resistance vs lux</td><td>0.4&ndash;0.65 A/W</td></tr>
<tr><td>Typical use</td><td>Street-light switch, camera exposure</td><td>Encoders, comms, detectors</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 5 : Chemical sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Definition and Need</h2>
<div class="def"><span class="cap">Definition</span>
A <b>chemical sensor</b> is a device that converts <b>chemical information</b> (concentration of a specific
chemical component or species in a sample) into an <b>analytical signal</b> which is usually electrical.
The chemical information may be composition, concentration, presence of a particular ion or gas.</div>
<p class="q">Chemical sensors are needed wherever we have to know <span class="b">what is inside a
substance</span> and not merely its physical condition &mdash; for example the pH of water, the oxygen
content of blood, the sugar in juice, the alcohol in breath, or the carbon monoxide in a room. Physical
sensors cannot answer these questions.</p>
<h2><span class="no">2</span>Construction (general structure)</h2>
<p class="q">Almost every chemical sensor has two main parts. The first is the
<span class="b">receptor (recognition) element</span>, which selectively reacts with the chemical species to
be measured. The second is the <span class="b">transducer element</span>, which converts that chemical
reaction into an electrical signal. Between them we often need a <span class="b">selective membrane</span>
which allows only the wanted species to pass, so that other substances do not disturb the reading.</p>
""" + figures_core.render("5.1") + """
<h2><span class="no">3</span>Types of Chemical Sensors</h2>
<div class="tw"><table>
<tr><th>Type</th><th>Principle / Output</th><th>Example</th></tr>
<tr><td><b>Electrochemical</b></td><td>Chemical reaction produces voltage, current or change of conductivity</td>
<td>pH (potentiometric), dissolved oxygen (amperometric), glucose sensor</td></tr>
<tr><td><b>Optical</b></td><td>Change in light absorption, emission or colour intensity</td>
<td>Colorimeter, infra-red CO&#8322; sensor, spectrophotometer</td></tr>
<tr><td><b>Semiconductor / MOS</b></td><td>Gas adsorption changes the resistance of a metal oxide layer</td>
<td>MQ-2, MQ-3, MQ-135 gas sensors, SnO&#8322; sensors</td></tr>
<tr><td><b>Catalytic (pellistor)</b></td><td>Combustible gas burns on a catalyst and raises its temperature</td>
<td>Combustible gas detector in mines</td></tr>
<tr><td><b>Thermal / calorimetric</b></td><td>Heat of reaction is measured</td><td>Thermistor based gas sensor</td></tr>
<tr><td><b>Piezoelectric / QCM</b></td><td>Mass deposited on a crystal changes its resonant frequency</td>
<td>Quartz crystal microbalance, humidity sensor</td></tr>
<tr><td><b>Biosensor</b></td><td>Biological element (enzyme, antibody) plus transducer</td>
<td>Glucometer, DNA sensor</td></tr>
</table></div>

<h2><span class="no">4</span>Working of two important examples</h2>
<h3>4.1 Potentiometric sensor (pH electrode)</h3>
<p class="q">A thin glass membrane separates two solutions of different hydrogen ion concentration. A
potential difference develops across this membrane which depends on the pH of the test solution. This
voltage is measured against a stable <span class="b">reference electrode</span> and is about
<span class="b">59.16 mV per pH unit</span> at 25 &deg;C.</p>
""" + figures_core.render("5.2") + """
<h3>4.2 Amperometric sensor (Clark dissolved oxygen electrode)</h3>
<p class="q">Oxygen diffuses through a membrane and is reduced at a platinum cathode. The resulting
<span class="b">current is directly proportional to the oxygen concentration</span>. Used in water treatment
and blood gas analysis.</p>
<h2><span class="no">5</span>Applications</h2>
<ul class="arr">
  <li><span class="b">Water quality monitoring</span> &mdash; pH, chlorine, dissolved oxygen, turbidity.</li>
  <li><span class="b">Medical</span> &mdash; blood glucose meter, blood gas analyser, breath analyser.</li>
  <li><span class="b">Environmental safety</span> &mdash; CO, CO&#8322;, H&#8322;S, NH&#8323;, toxic gas
      alarms in mines and chemical plants.</li>
  <li><span class="b">Food industry</span> &mdash; freshness, ripeness, alcohol and sugar content.</li>
  <li><span class="b">Automobile</span> &mdash; oxygen (lambda) sensor in the exhaust for fuel control.</li>
</ul>
<div class="tip"><span class="cap">Two words to remember</span>
<b>Selectivity</b> &mdash; the sensor must respond only to the wanted species.
<b>Drift</b> &mdash; the slow change of reading with time, which makes frequent calibration necessary.
Both these problems are the biggest drawbacks of chemical sensors.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A pH electrode follows E = E<sub>0</sub> + 0.05916 &times; pH at 25 &deg;C. A process sample reads pH 7.00 on the reference and pH 10.00 on the process side. Find the electrode voltage difference.</div>
<p class="q"><span class="b">Solution.</span> &Delta;pH = 10.00 &minus; 7.00 = 3.00 pH units. &Delta;E = 0.05916 &times; 3.00 = 0.1775 V = 177.5 mV. The sign is negative for rising pH on a standard glass electrode (about &minus;59.16 mV per pH unit). <span class="hl">|&Delta;E| = 177.5 mV (&minus;59.16 mV per pH at 25 &deg;C).</span></p>
<div class="formula"><span class="b">Problem 2.</span> A dissolved-oxygen probe gives 8.2 &micro;A at saturation (9.2 mg/L) and 3.1 &micro;A in the sample. Find the oxygen concentration.</div>
<p class="q"><span class="b">Solution.</span> Assume current is linear with concentration: C = C<sub>sat</sub> &times; I / I<sub>sat</sub> C = 9.2 &times; 3.1 / 8.2 = 3.49 mg/L Temperature compensation corrects saturation value if the sample is not at the calibration temperature. <span class="hl">Dissolved oxygen &asymp; 3.5 mg/L.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What is a reference electrode?</span><br><span class="o">A.</span> A stable electrode of known potential (e.g. Ag/AgCl) that provides a fixed baseline so the sensing electrode voltage can be interpreted absolutely.</p>
<p class="q"><span class="b">Q2. Why does a pH electrode need a high-impedance amplifier?</span><br><span class="o">A.</span> Glass electrodes can source almost no current; any load would collapse the millivolt signal, so input impedance must be 10<sup>12</sup> &Omega; or higher.</p>
<p class="q"><span class="b">Q3. Distinguish potentiometric and amperometric sensors.</span><br><span class="o">A.</span> Potentiometric measures an open-circuit voltage (no current, logarithmic in concentration); amperometric measures a current at fixed bias (linear in concentration).</p>
<p class="q"><span class="b">Q4. What is the Clark electrode used for?</span><br><span class="o">A.</span> Measuring dissolved oxygen in water and blood through a membrane-covered cathode that reduces oxygen and produces a proportional current.</p>
<p class="q"><span class="b">Q5. How do you calibrate a pH sensor?</span><br><span class="o">A.</span> Two-point buffer calibration, usually pH 4.0 and 7.0 (or 7.0 and 10.0), setting slope and offset.</p>
<p class="q"><span class="b">Q6. Name one hazard when chemical sensors foul.</span><br><span class="o">A.</span> Drift and false readings; membranes coated by oil, scale or biological film stop responding and must be cleaned or replaced.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">Chemical sensors convert concentration or activity into an electrical quantity by one of two routes: a selective membrane that develops a voltage (potentiometric, e.g. pH electrode) or a controlled reaction that draws a current (amperometric, e.g. Clark cell). Both need stable references, careful calibration and clean sensing surfaces. Choosing the right interface circuit &mdash; high-impedance amplifier for voltage-type sensors, transimpedance amplifier for current-type sensors &mdash; is half the design job.</p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>pH (glass electrode)</th><th>Dissolved O&#8322; (Clark)</th></tr>
<tr><td>Principle</td><td>Potentiometric</td><td>Amperometric</td></tr>
<tr><td>Output</td><td>&plusmn;59 mV per pH at 25 &deg;C</td><td>0&ndash;100 nA / ppm class currents</td></tr>
<tr><td>Range</td><td>0&ndash;14 pH</td><td>0&ndash;20 mg/L</td></tr>
<tr><td>Accuracy</td><td>&plusmn;0.01&ndash;0.1 pH</td><td>&plusmn;0.1&ndash;0.5 mg/L</td></tr>
<tr><td>Response time</td><td>seconds to a minute</td><td>60&ndash;90 s (T<sub>90</sub>)</td></tr>
<tr><td>Calibration</td><td>Two buffer points</td><td>Water-saturated air / zero solution</td></tr>
<tr><td>Typical use</td><td>Effluent, fermentation, pools</td><td>Aquaculture, boilers, blood gas</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 6 : Gas sensors (MQ-2)
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Introduction</h2>
<p class="q">A gas sensor detects the presence or concentration of a gas in the air. The most popular and
cheapest family for student projects and domestic alarms is the <span class="b">MQ series of semiconductor
(MOS) gas sensors</span> &mdash; MQ-2 (smoke, LPG, propane), MQ-3 (alcohol), MQ-4 (methane, CNG),
MQ-6 (LPG), MQ-7 (carbon monoxide), MQ-135 (air quality, NH&#8323;, CO&#8322;). In this topic we study the
<span class="r">MQ-2</span> in detail.</p>
<div class="tw"><table>
<tr><th>Part</th><th>Material / Detail</th></tr>
<tr><td>Sensing layer</td><td>Tin dioxide (SnO&#8322;) &mdash; semiconductor ceramic</td></tr>
<tr><td>Heater</td><td>Ni-Cr alloy coil, about 0.8 W, keeps layer at 200&ndash;300 &deg;C</td></tr>
<tr><td>Electrodes</td><td>Platinum, 6 pins (4 for signal, 2 for heater)</td></tr>
<tr><td>Body</td><td>Stainless steel mesh (protects and lets gas diffuse)</td></tr>
<tr><td>Supply</td><td>5 V DC (heater needs 5 V), signal 0.1&ndash;4.5 V</td></tr>
</table></div>

<h2><span class="no">2</span>Construction of MQ-2</h2>
<p class="q">Inside the steel mesh there is a small <span class="b">alumina (Al&#8322;O&#8323;) ceramic
tube</span>. On the outer surface of this tube a layer of <span class="b">tin dioxide</span> is deposited;
this is the sensing layer. A <span class="b">heating coil</span> is placed inside the tube to keep the
sensing layer at a high temperature, because the chemical reaction takes place only when it is hot. Two
platinum electrodes collect the current from the sensing layer. The heater and the sensor are electrically
separate, so the MQ-2 has <span class="b">six pins</span> &mdash; two heater pins (H) and four sensing pins
(A and B, internally connected in pairs).</p>
""" + figures_core.render("6.1") + """
<h2><span class="no">3</span>Working</h2>
<p class="q">When the sensor is heated in clean air, oxygen molecules from the air get adsorbed on the
surface of SnO&#8322; and capture free electrons to form O&#8315; and O&#8322;&#8315; ions. Because the
electrons are trapped, the <span class="b">resistance of the sensing layer is high</span> (about 10 k&#937;
or more, this is called R&#8320;).</p>
<p class="q">When a <span class="b">reducing gas</span> such as LPG, smoke or propane comes in contact with
the hot surface, it reacts with the adsorbed oxygen ions. The trapped electrons are released back into the
tin dioxide, so the number of free electrons increases and the <span class="b">resistance falls</span>.
The higher the gas concentration, the lower the resistance. In a potential divider circuit this fall of
resistance gives a <span class="b">rise in output voltage</span>, which the microcontroller reads through the
ADC. If the voltage crosses the set limit, the controller switches ON the buzzer, the exhaust fan or the
relay.</p>
""" + figures_core.render("6.2") + """
<div class="formula">ppm is found from the curve : &nbsp; Rs/R&#8320; &nbsp;versus&nbsp; ppm (log-log graph)
&nbsp;&nbsp; Rs = (5 V &minus; Vout)/Vout &times; RL</div>
<h2><span class="no">4</span>Applications</h2>
<ul class="arr">
  <li><span class="b">LPG leakage alarm</span> in domestic kitchens and cylinder stores.</li>
  <li>Smoke detector combined with fire alarm systems.</li>
  <li>Air quality monitoring in offices, laboratories and smart homes.</li>
  <li>Portable gas leak detector for pipeline checking.</li>
  <li>Automated exhaust fan / gas valve shut-off systems.</li>
</ul>
<div class="warn"><span class="cap">Care while using MQ-2</span>
The sensor needs a <b>pre-heat (burn-in) time of 24 to 48 hours for the first use</b> and 2 to 3 minutes for
normal use, otherwise the reading drifts. The heater makes the sensor hot, so do not touch it and do not use
it in a very dusty or silicon-vapour atmosphere.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">5</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> An MQ-2 is wired with R<sub>L</sub> = 10 k&Omega; across 5 V and reads V<sub>out</sub> = 2.0 V in clean air where R<sub>0</sub> gives V<sub>out0</sub> = 1.0 V. Find R<sub>s</sub> / R<sub>0</sub>.</div>
<p class="q"><span class="b">Solution.</span> Divider: V<sub>out</sub> = V<sub>cc</sub> &times; R<sub>L</sub> / (R<sub>s</sub> + R<sub>L</sub>) Clean air: 1.0 = 5 &times; 10 / (R<sub>0</sub> + 10) &rArr; R<sub>0</sub> = 40 k&Omega; Gas present: 2.0 = 5 &times; 10 / (R<sub>s</sub> + 10) &rArr; R<sub>s</sub> = 15 k&Omega; Ratio R<sub>s</sub>/R<sub>0</sub> = 15/40 = 0.375 &mdash; read it off the log-log curve for the gas in question. <span class="hl">R<sub>s</sub>/R<sub>0</sub> = 0.375 (concentration comes from the datasheet curve).</span></p>
<h2><span class="no">6</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What material is the sensing element of MQ-2?</span><br><span class="o">A.</span> Tin dioxide (SnO&#8322;), an n-type semiconductor whose surface resistance changes when combustible gases adsorb on it.</p>
<p class="q"><span class="b">Q2. Why is a heater coil inside the can?</span><br><span class="o">A.</span> The sensing reaction needs a controlled high surface temperature, roughly 200 to 400 &deg;C, supplied by the internal nichrome heater.</p>
<p class="q"><span class="b">Q3. Does MQ-2 consume oxygen?</span><br><span class="o">A.</span> Yes &mdash; it needs fresh air reference oxygen at the surface, so it should not be sealed in a tiny volume without ventilation.</p>
<p class="q"><span class="b">Q4. Is the sensor output linear in gas concentration?</span><br><span class="o">A.</span> No. The relationship is log-log; the datasheet curve of R<sub>s</sub>/R<sub>0</sub> against ppm is used, or a microcontroller fits that curve.</p>
<p class="q"><span class="b">Q5. How is selectivity improved in a gas sensor array?</span><br><span class="o">A.</span> Several sensors with different dopants (Sn, Pd, Al) are combined and their pattern is classified by a small algorithm.</p>
<p class="q"><span class="b">Q6. What safety rating do LPG sensors often carry?</span><br><span class="o">A.</span> Many MQ-2 modules are advertised as explosion-proof and flameproof for domestic LPG leak alarm use, but the module still needs certified installation.</p>
<h2><span class="no">7</span>Summary</h2>

<p class="q">The MQ-2 is a resistive SnO&#8322; gas sensor: combustible gas on the heated surface changes the semiconductor resistance, and a simple load resistor converts that change into a voltage the ADC can read. Accurate work depends on knowing R&#8320; at baseline, following the log-log response curve rather than assuming linearity, respecting heater temperature and burn-in, and never trapping the sensor away from fresh air.</p>
<h2><span class="no">8</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>MQ-2 specification</th><th>Remark</th></tr>
<tr><td>Detectable gases</td><td>LPG, propane, hydrogen, smoke, alcohol</td><td>Combustible range</td></tr>
<tr><td>Supply (heater)</td><td>5 V AC/DC, about 450 mW</td><td>Keep temperature stable</td></tr>
<tr><td>Sensor supply</td><td>5 V</td><td>Divider powered from same rail</td></tr>
<tr><td>R&#8320; in clean air</td><td>10&ndash;60 k&Omega; (device spread)</td><td>Store this as baseline</td></tr>
<tr><td>Sensitivity</td><td>R<sub>s</sub>/R&#8320; &lt; 0.6 at 200 ppm LPG</td><td>From datasheet curve</td></tr>
<tr><td>Response / recovery</td><td>about 10 s / 30 s</td><td>T<sub>90</sub> values</td></tr>
<tr><td>Pre-heat (burn-in)</td><td>24&ndash;48 h first use</td><td>Then periodic calibration</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 7 : Vibration sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Introduction and need</h2>
<p class="q">Vibration is the to-and-fro oscillatory motion of a machine part about its mean position.
Every rotating machine vibrates, but when the vibration crosses a limit it means that something is wrong
&mdash; imbalance, misalignment, loose bearing, bent shaft or cavitation. A <span class="b">vibration
sensor</span> measures this oscillation so that the fault can be detected
<span class="hl">before the machine fails</span>. This is called <span class="b">condition monitoring</span>
or predictive maintenance.</p>
<p class="q">Vibration is described by three quantities: <span class="b">displacement</span> (micron),
<span class="b">velocity</span> (mm/s) and <span class="b">acceleration</span> (g or m/s&sup2;), together
with its <span class="b">frequency</span> in Hz.</p>

<h2><span class="no">2</span>Piezoelectric Accelerometer &mdash; Construction</h2>
<p class="q">It is the most common industrial vibration sensor. A <span class="b">seismic mass</span> is
placed on a <span class="b">piezoelectric crystal</span> (quartz or PZT ceramic). The crystal is sandwiched
between two electrodes and the whole assembly is sealed in a steel case. When the case vibrates, the mass
presses the crystal with a varying force and the crystal generates a <span class="b">charge</span>.</p>
""" + figures_core.render("7.1") + """
<h2><span class="no">3</span>Working</h2>
<p class="q">The piezoelectric effect states that when a mechanical force is applied on certain crystals,
electric charges appear on their faces. The generated charge Q = d &times; F, where d is the piezoelectric
constant and F is the applied force. Since the force on the mass is F = m &times; a, the
<span class="b">charge produced is directly proportional to the acceleration</span> of the vibration. This
very small charge must be converted by a <span class="b">charge amplifier</span> or the built-in IEPE
amplifier into a usable voltage (typically 100 mV/g).</p>
<h2><span class="no">4</span>Other vibration sensors</h2>
<h3>4.1 Vibration switch (SW-18020P / ball type)</h3>
<p class="q">It is a simple digital sensor. A small metal ball is kept inside a cylindrical spring or cavity.
When vibration occurs the ball touches the walls and the contacts close, giving a LOW or HIGH signal. It is
used where only "vibration present / absent" information is needed.</p>
""" + figures_core.render("7.2") + """
<h3>4.2 MEMS accelerometer (ADXL335 / MPU-6050)</h3>
<p class="q">A tiny silicon cantilever with a proof mass is made by micro-machining. Its capacitance changes
with movement and the on-chip circuit converts it to an analog voltage (ADXL335) or to I&sup2;C digital data
(MPU-6050). Used in mobile phones, drones, car airbags and step counting watches.</p>
<div class="tw"><table>
<tr><th>Sensor</th><th>Type</th><th>Output</th><th>Typical use</th></tr>
<tr><td>Piezoelectric accelerometer</td><td>Active</td><td>Charge / mV per g</td><td>Machine condition monitoring</td></tr>
<tr><td>MEMS accelerometer</td><td>Passive, IC type</td><td>Analog V or I&sup2;C digital</td><td>Mobile, drone, airbag</td></tr>
<tr><td>Velocity transducer</td><td>Moving coil</td><td>mm/s</td><td>Large machines, ISO 10816 limits</td></tr>
<tr><td>Proximity (eddy current) probe</td><td>Non-contact</td><td>micron displacement</td><td>Shaft vibration of turbines</td></tr>
<tr><td>Vibration switch</td><td>Digital contact</td><td>ON / OFF</td><td>Simple alarm, theft alarm</td></tr>
</table></div>
<h2><span class="no">5</span>Applications</h2>
<ul class="arr">
  <li><span class="b">Predictive maintenance</span> of motors, pumps, fans, gear boxes, compressors.</li>
  <li>Bearing fault detection and shaft imbalance analysis.</li>
  <li>Earthquake and structural health monitoring of bridges and buildings.</li>
  <li>Vehicle crash detection (airbag), anti-theft alarms, mobile screen rotation.</li>
  <li>Washing machine unbalance detection and drone stabilisation.</li>
</ul>
""" + """
<!--EXTRAS-->
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A piezoelectric accelerometer has sensitivity 100 pC/g and is connected to a charge amplifier with C<sub>f</sub> = 1000 pF. Find the amplifier output at 10 g.</div>
<p class="q"><span class="b">Solution.</span> Charge Q = 100 pC/g &times; 10 g = 1000 pC. V<sub>out</sub> = Q / C<sub>f</sub> = 1000 pC / 1000 pF = 1.0 V. Charge amplifiers are preferred because cable capacitance does not change the gain. <span class="hl">V<sub>out</sub> = 1.0 V.</span></p>
<div class="formula"><span class="b">Problem 2.</span> An accelerometer with 500 mV/g output is sampled while the machine vibrates at 0.4 g. The controller alarms above 1.0 g. Find the ADC counts at 0.4 g with a 3.3 V, 12-bit ADC.</div>
<p class="q"><span class="b">Solution.</span> V = 0.5 V/g &times; 0.4 g = 0.2 V. Counts = 0.2 / 3.3 &times; 4095 = 248. Alarm level 1.0 g = 0.5 V &rArr; 620 counts &mdash; threshold can be set directly in counts. <span class="hl">ADC code &asymp; 248 at 0.4 g.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What does an accelerometer actually measure?</span><br><span class="o">A.</span> It measures the force needed to accelerate its own proof mass; by Newton's law that force divided by mass equals the vibration acceleration.</p>
<p class="q"><span class="b">Q2. Why do piezo accelerometers need a charge or IEPE amplifier?</span><br><span class="o">A.</span> The crystal generates charge but almost no current; a charge amplifier or built-in IEPE conditioning converts it to a usable voltage before the cable.</p>
<p class="q"><span class="b">Q3. What is the resonant frequency of a vibration sensor?</span><br><span class="o">A.</span> The mounting-structure natural frequency; measurements are only trusted well below it, usually below one third.</p>
<p class="q"><span class="b">Q4. Why are MEMS accelerometers popular in modern machines?</span><br><span class="o">A.</span> They are tiny, cheap, low power and put X, Y, Z plus temperature on one digital interface straight into a microcontroller.</p>
<p class="q"><span class="b">Q5. What is a vibration switch used for?</span><br><span class="o">A.</span> It gives a simple trip output when vibration crosses a set level &mdash; cheap protection for pumps, fans and washers without full spectrum analysis.</p>
<p class="q"><span class="b">Q6. How does sampling rate relate to vibration analysis?</span><br><span class="o">A.</span> The sample rate must be at least twice the highest frequency of interest (Nyquist); bearing faults often need several kilohertz sampling.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">Vibration sensors convert mechanical oscillation into an electrical signal: piezoelectric accelerometers for wide bandwidth and harsh duty, MEMS devices for compact three-axis digital sensing, and simple vibration switches for alarm duty. The sensor output is a charge or voltage proportional to acceleration, the mounting must be mechanically stiff, and the electronics must resolve the tiny signals before cable noise takes over.</p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Piezo accelerometer</th><th>MEMS (e.g. ADXL335)</th></tr>
<tr><td>Principle</td><td>Piezoelectric charge</td><td>Capacitive silicon proof mass</td></tr>
<tr><td>Sensitivity</td><td>10&ndash;1000 pC/g</td><td>100&ndash;1000 mV/g (scaled to range)</td></tr>
<tr><td>Frequency range</td><td>1 Hz &ndash; 10 kHz+</td><td>DC &ndash; a few hundred Hz</td></tr>
<tr><td>Axes</td><td>Single axis</td><td>1, 2 or 3 axes</td></tr>
<tr><td>Output</td><td>Charge / IEPE voltage</td><td>Analog or I&#178;C / SPI digital</td></tr>
<tr><td>Supply</td><td>2&ndash;20 mA IEPE constant current</td><td>1.7&ndash;3.6 V low voltage</td></tr>
<tr><td>Typical use</td><td>Bearing analysis, balancing</td><td>Tilt, impact, appliance monitoring</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 8 : Displacement and Force sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Displacement Sensors</h2>
<div class="def"><span class="cap">Definition</span>
A <b>displacement sensor</b> measures the <b>change of position</b> (linear or angular movement) of an object
from a reference point and converts it into an electrical signal.</div>
<p class="q">Displacement sensors are classified as <span class="b">resistive</span> (potentiometer),
<span class="b">inductive</span> (LVDT, eddy current), <span class="b">capacitive</span>,
<span class="b">optical</span> (encoder, laser) and <span class="b">ultrasonic</span>.</p>
<h3>1.1 LVDT &mdash; Linear Variable Differential Transformer</h3>
<p class="q"><span class="g">Construction:</span> It consists of one <span class="b">primary winding</span>
in the centre and two identical <span class="b">secondary windings</span> (S1 and S2) wound on a hollow
cylindrical former. A <span class="b">soft iron core</span> is placed inside the former and is free to move
along the axis; the core is attached to the object whose displacement is to be measured. The two secondaries
are connected in <span class="b">series opposition</span> (differential).</p>
<p class="q"><span class="g">Working:</span> An AC supply (1 to 10 kHz, 3 to 15 V) is given to the primary.
When the core is exactly in the middle (null position) the voltages induced in S1 and S2 are equal and
opposite, so the net output is <span class="b">zero</span>. When the core moves to one side, the coupling
with that secondary increases, so the differential output voltage rises and its
<span class="b">phase</span> tells the direction of movement. The output is linear over a range of
&plusmn;10 mm to &plusmn;250 mm.</p>
""" + figures_core.render("8.1") + """
<h3>1.2 Capacitive displacement sensor</h3>
<p class="q">Two parallel plates form a capacitor. If the distance between them (or the overlapping area)
changes due to the movement of one plate, the capacitance changes as <span class="b">C = &epsilon;A/d</span>.
This change is converted to voltage by an oscillator or a bridge circuit. Very high resolution (nanometre)
but very sensitive to dust and humidity.</p>
<h3>1.3 Optical encoder</h3>
<p class="q">A disc with alternate transparent and opaque slots rotates with the shaft. An LED and a
photodiode on either side produce pulses as the slots pass. Counting the pulses gives the angular
displacement and the pulse rate gives the speed. Two channels 90&deg; apart give the direction.</p>
<div class="tw"><table>
<tr><th>Sensor</th><th>Range</th><th>Advantage</th><th>Disadvantage</th></tr>
<tr><td>Potentiometer</td><td>few cm</td><td>Cheap, simple, large output</td><td>Wear, noise, limited life</td></tr>
<tr><td>LVDT</td><td>&plusmn;10 mm to 250 mm</td><td>Frictionless, infinite resolution, rugged</td><td>Needs AC supply, sensitive to stray magnetic field</td></tr>
<tr><td>Capacitive</td><td>micron</td><td>Very high resolution, non-contact</td><td>Needs clean environment, complex electronics</td></tr>
<tr><td>Optical encoder</td><td>360&deg;</td><td>Digital, accurate, fast</td><td>Dust affects, costlier</td></tr>
</table></div>

<h2><span class="no">2</span>Force Sensors</h2>
<div class="def"><span class="cap">Definition</span>
A <b>force sensor</b> measures a push or pull force and gives an output proportional to it. In practice the
force is first converted into a <b>deflection</b> of an elastic element and the deflection is then measured
by a strain gauge, LVDT or piezoelectric crystal.</div>
<p class="q">The elastic element is called the <span class="b">force summing device</span> or proof body.
Common shapes are the <span class="b">proving ring</span>, the <span class="b">cantilever beam</span>, the
<span class="b">column</span> and the <span class="b">diaphragm</span>. The complete assembly of proof body
plus strain gauges plus bridge circuit is the <span class="b">load cell</span> studied in Topic 3.</p>
""" + figures_core.render("8.2") + """
<h3>Applications</h3>
<ul class="arr">
  <li>Weighing scales, weigh bridges, hopper and tank weighing.</li>
  <li>Universal testing machines, press force monitoring, torque wrenches.</li>
  <li>Robot gripper force control, tactile sensors.</li>
  <li>Touch screens and force feedback joysticks (piezoelectric).</li>
</ul>
<div class="tip"><span class="cap">Difference to remember</span>
<b>Displacement</b> sensor tells "how much it moved", <b>force</b> sensor tells "how hard it was pushed".
Both often use the same elastic element &mdash; a load cell measures the <i>displacement</i> of a beam
caused by the <i>force</i>.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">3</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> An LVDT with sensitivity 40 mV/mm/V has an excitation of 5 V. The core moves 3 mm from null. Find the output voltage.</div>
<p class="q"><span class="b">Solution.</span> Sensitivity referred to 5 V = 40 &times; 5 = 200 mV/mm. V<sub>out</sub> = 200 mV/mm &times; 3 mm = 600 mV (phase indicates direction). <span class="hl">V<sub>out</sub> = 600 mV (0.6 V, sign/phase gives direction).</span></p>
<div class="formula"><span class="b">Problem 2.</span> A capacitive gap sensor has C = 100 pF at nominal gap d = 1 mm with area A fixed. Find C when the gap changes to 1.05 mm, and the fractional change.</div>
<p class="q"><span class="b">Solution.</span> C &prop; 1/d, so C' = C &times; d/d' = 100 &times; 1/1.05 = 95.2 pF. &Delta;C/C = &minus;&Delta;d/d = &minus;0.05/1 = &minus;0.05 = &minus;5 %. Half the fractional gap change appears as output in a simple differential arrangement. <span class="hl">C' = 95.2 pF, &Delta;C/C = &minus;5 %.</span></p>
<h2><span class="no">4</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. How does an LVDT work?</span><br><span class="o">A.</span> A movable core changes the mutual inductance of two secondary coils; the difference of the two secondary voltages is a signed measure of core position.</p>
<p class="q"><span class="b">Q2. Why is there no wear in an LVDT?</span><br><span class="o">A.</span> The core never touches the coils &mdash; coupling is purely magnetic, so life is practically unlimited.</p>
<p class="q"><span class="b">Q3. What is the principle of a capacitive displacement sensor?</span><br><span class="o">A.</span> Capacitance varies inversely with electrode gap; a bridge or C-to-V converter detects sub-nanometre changes.</p>
<p class="q"><span class="b">Q4. How does an incremental encoder differ from an absolute encoder?</span><br><span class="o">A.</span> Incremental counts steps from power-on and loses position at power-off; absolute gives a unique code for every shaft angle at any time.</p>
<p class="q"><span class="b">Q5. Where is torque measured on a rotating shaft?</span><br><span class="o">A.</span> With strain-gauge torque flanges that transmit data wirelessly, avoiding slip rings and their maintenance.</p>
<p class="q"><span class="b">Q6. Give two industrial uses of force sensors.</span><br><span class="o">A.</span> Weighing platforms and material-testing machines (tensile/compression rigs).</p>
<h2><span class="no">5</span>Summary</h2>

<p class="q">This topic covered the measurement of how far something moves, how hard it is pushed and how strongly it is twisted. LVDTs, capacitive probes and encoders cover position and displacement with different resolutions and contact arrangements, while force and torque almost always rest on strain-gauge bridges in elastic bodies. All of them must be mounted stiffly enough that the sensor actually sees the motion or load it is supposed to measure.</p>
<h2><span class="no">6</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>LVDT</th><th>Capacitive probe</th><th>Incremental encoder</th></tr>
<tr><td>Measuring principle</td><td>Mutual inductance</td><td>Gap capacitance</td><td>Optical / magnetic slots</td></tr>
<tr><td>Resolution</td><td>0.1 &micro;m typical</td><td>0.01 &micro;m possible</td><td>1 pulse (e.g. 1024/rev)</td></tr>
<tr><td>Range</td><td>&plusmn;0.5 to &plusmn;500 mm</td><td>0.1&ndash;10 mm gap</td><td>Continuous counting</td></tr>
<tr><td>Contact</td><td>Non-contact core</td><td>Non-contact field</td><td>Non-contact light path</td></tr>
<tr><td>Output</td><td>Analog AC-bridge or 4&ndash;20 mA</td><td>Capacitance / voltage</td><td>A & B phase pulses</td></tr>
<tr><td>Typical use</td><td>Valve position, gauging</td><td>Run-out, film thickness</td><td>Motor speed, CNC axes</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 9 : Torque and Pressure sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Torque Sensors</h2>
<div class="def"><span class="cap">Definition</span>
<b>Torque</b> is the turning (twisting) effect of a force applied at some distance from the axis of rotation.
Torque T = F &times; r (N-m). A <b>torque sensor</b> measures this twisting action on a rotating shaft.</div>
<h3>1.1 Construction and working (strain gauge torque sensor)</h3>
<p class="q">When a shaft transmits power it twists slightly. This twist produces
<span class="b">shear stress</span> on the surface of the shaft. The maximum shear stress occurs on planes
inclined at <span class="b">45&deg;</span> to the shaft axis. Therefore <span class="b">four strain
gauges</span> are bonded on the shaft at &plusmn;45&deg; and connected as a full Wheatstone bridge &mdash; two
in tension and two in compression. When the shaft twists, the bridge unbalances and gives an output voltage
proportional to the applied torque.</p>
<p class="q">Because the shaft is rotating, the small bridge signal must be transferred to the stationary
side. This is done by <span class="b">slip rings and brushes</span>, by <span class="b">rotary transformers</span>
or, in modern sensors, by <span class="b">telemetry (wireless) or magneto-elastic</span> coupling.</p>
""" + figures_core.render("9.1") + """
<div class="formula">T = (&pi; &times; d&sup3; &times; &tau;) / 16 &nbsp;&nbsp; and &nbsp;&nbsp;
Power P = 2&pi;NT / 60 &nbsp; watt</div>
<h3>Other torque sensors</h3>
<ul class="dot">
  <li><span class="b">Magneto-elastic / magnetostrictive</span> &mdash; twist changes the magnetic
      permeability of the shaft; contactless.</li>
  <li><span class="b">Optical torque sensor</span> &mdash; two encoder discs on the shaft, twist changes the
      phase between the two pulse trains.</li>
  <li><span class="b">Reaction torque sensor</span> &mdash; measures the torque on the stationary housing of
      a motor (used in dynamometers).</li>
</ul>
<h3>Applications of torque sensors</h3>
<ul class="arr">
  <li>Engine and motor dynamometers, brake testing.</li>
  <li>Power measurement of pumps, compressors, gear boxes, turbines.</li>
  <li>Electric power steering and tightening tools (torque wrench).</li>
  <li>Conveyor and crane drive monitoring.</li>
</ul>

<h2><span class="no">2</span>Pressure Sensors</h2>
<div class="def"><span class="cap">Definition</span>
<b>Pressure</b> is the force acting per unit area, P = F/A, measured in Pa, bar, psi or mm of Hg.
A <b>pressure sensor</b> converts this pressure into an electrical signal, usually by first converting it
into a <b>deflection</b> of an elastic element.</div>
<h3>2.1 Bourdon tube pressure gauge</h3>
<p class="q">A C-shaped (or spiral) hollow tube of elliptical cross-section is used. When pressure is applied
inside the tube it tends to become circular, so the free end of the C <span class="b">straightens out</span>.
This movement is amplified by a link and pinion and moves a pointer over a calibrated dial. It is a purely
mechanical device, very rugged and cheap.</p>
""" + figures_core.render("9.2") + """
<h3>2.2 Strain gauge / diaphragm pressure sensor</h3>
<p class="q">Pressure is applied on one side of a thin stainless steel diaphragm. Four strain gauges bonded
on the diaphragm form a Wheatstone bridge. The deflection is proportional to pressure, so the bridge output
(in mV) is proportional to pressure. Such sensors are used inside
<span class="b">pressure transmitters</span> which give a 4&ndash;20 mA output.</p>
<h3>2.3 Piezoresistive pressure sensor</h3>
<p class="q">Here a silicon diaphragm is micro-machined and piezoresistors are diffused into it. The
resistance of silicon changes directly with stress, so no bonding is needed. Very small, cheap and used in
mobile phones, medical devices and car MAP sensors.</p>
<div class="tw"><table>
<tr><th>Type</th><th>Element</th><th>Range</th><th>Use</th></tr>
<tr><td>Bourdon tube</td><td>C tube, spiral</td><td>1 bar to 1000 bar</td><td>Local gauge indication</td></tr>
<tr><td>Bellows</td><td>Convolution tube</td><td>vacuum to 5 bar</td><td>Low pressure, actuators</td></tr>
<tr><td>Diaphragm</td><td>Metal capsule</td><td>vacuum to 25 bar</td><td>Differential pressure, transmitters</td></tr>
<tr><td>Strain gauge</td><td>Diaphragm + gauges</td><td>wide</td><td>4&ndash;20 mA transmitters</td></tr>
<tr><td>Piezoresistive</td><td>Silicon diaphragm</td><td>wide</td><td>Compact electronic sensors</td></tr>
<tr><td>Capacitive</td><td>Diaphragm as plate</td><td>very low</td><td>High accuracy, DP flow</td></tr>
</table></div>
<h3>Applications of pressure sensors</h3>
<ul class="arr">
  <li>Boiler, steam line, hydraulic and pneumatic system pressure monitoring.</li>
  <li>Blood pressure measurement (medical), tyre pressure monitoring (TPMS).</li>
  <li>Level measurement by hydrostatic head (P = &rho;gh).</li>
  <li>Flow measurement using differential pressure across an orifice.</li>
  <li>Altitude measurement in aircraft (barometric pressure).</li>
</ul>
""" + """
<!--EXTRAS-->
<h2><span class="no">3</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A diaphragm pressure sensor of area 2 cm&sup2; sees 15 bar gauge. Find the force on the diaphragm (1 bar = 10<sup>5</sup> Pa).</div>
<p class="q"><span class="b">Solution.</span> A = 2 cm&sup2; = 2 &times; 10<sup>&minus;4</sup> m&sup2;. P = 15 bar = 1.5 &times; 10<sup>6</sup> Pa. F = P &times; A = 1.5&times;10<sup>6</sup> &times; 2&times;10<sup>&minus;4</sup> = 300 N. <span class="hl">F = 300 N on the diaphragm.</span></p>
<h2><span class="no">4</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Distinguish gauge, absolute and differential pressure.</span><br><span class="o">A.</span> Gauge is referenced to atmosphere, absolute to vacuum, differential is the difference between two process points (e.g. across an orifice).</p>
<p class="q"><span class="b">Q2. How does a Bourdon tube work?</span><br><span class="o">A.</span> A curved hollow tube tends to straighten as internal pressure rises; the tip motion drives a gear and pointer.</p>
<p class="q"><span class="b">Q3. What is overpressure rating?</span><br><span class="o">A.</span> The maximum pressure a sensor survives without calibration shift, often 2&ndash;3 times full scale.</p>
<p class="q"><span class="b">Q4. Why do pressure transmitters show a small static zero error?</span><br><span class="o">A.</span> Sealed systems, temperature effects on fill fluid, or installing a gauge reference where absolute was specified.</p>
<p class="q"><span class="b">Q5. What is impulse piping?</span><br><span class="o">A.</span> The tube that connects the process tap to the transmitter; it must be lagged, valved and free of trapped gas or liquid that would distort the reading.</p>
<p class="q"><span class="b">Q6. Where are piezoresistive sensors commonly used?</span><br><span class="o">A.</span> Manifold absolute-pressure (MAP) sensors in engines, tyre-pressure monitors and medical devices &mdash; where size and cost dominate.</p>
<h2><span class="no">5</span>Summary</h2>

<p class="q">Pressure sensors all measure the force of a fluid on a defined area, but they differ in the elastic element used &mdash; Bourdon tube, corrugated diaphragm or silicon bridge &mdash; and in the electrical readout. Range, reference (gauge/absolute/differential), overpressure margin and 4&ndash;20 mA scaling are the four decisions that determine whether a pressure installation measures correctly on day one and keeps measuring after water hammer and blockage events.</p>
<h2><span class="no">6</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Bourdon gauge</th><th>Strain-gauge transmitter</th><th>Piezoresistive (MEMS)</th></tr>
<tr><td>Range</td><td>0&ndash;1000 bar possible</td><td>0&ndash;0.4 to 0&ndash;400 bar</td><td>0&ndash;1 to 0&ndash;35 bar</td></tr>
<tr><td>Output</td><td>Pointer angle</td><td>4&ndash;20 mA / 1&ndash;5 V</td><td>mV-level bridge / digital</td></tr>
<tr><td>Accuracy</td><td>&plusmn;1 % of span</td><td>&plusmn;0.075&ndash;0.25 % of span</td><td>&plusmn;0.25&ndash;1 % FS</td></tr>
<tr><td>Overpressure</td><td>Mechanical stop</td><td>2&times; to 5&times; FS</td><td>1&times; to 3&times; FS</td></tr>
<tr><td>Reference</td><td>Gauge</td><td>Gauge / abs / diff</td><td>Gauge or absolute</td></tr>
<tr><td>Typical use</td><td>Local indication, steam lines</td><td>Process control loops</td><td>Automotive, tyres, medical</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 10 : Position and Motion sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Position Sensors</h2>
<div class="def"><span class="cap">Definition</span>
A <b>position sensor</b> detects the <b>location</b> of an object with respect to a reference point and
converts it into an electrical signal. Position may be <b>linear</b> (along a straight line) or
<b>rotary / angular</b> (about an axis).</div>
<p class="q">A position sensor is basically a displacement sensor used inside a <span class="b">feedback
loop</span> of a control system. The most common ones are:</p>
<div class="tw"><table>
<tr><th>Sensor</th><th>Type</th><th>Principle</th><th>Output</th></tr>
<tr><td>Potentiometric</td><td>Resistive, contact</td><td>Wiper divides the resistance track</td><td>Analog voltage</td></tr>
<tr><td>LVDT</td><td>Inductive</td><td>Differential transformer</td><td>AC voltage (amplitude + phase)</td></tr>
<tr><td>Hall effect</td><td>Magnetic</td><td>Voltage across a current carrying conductor in a magnetic field</td><td>Digital or analog</td></tr>
<tr><td>Rotary encoder</td><td>Optical / magnetic</td><td>Slotted disc with LED-photodiode</td><td>Digital pulses (A, B, Z)</td></tr>
<tr><td>Proximity (inductive / capacitive)</td><td>Non-contact</td><td>Eddy current or capacitance change</td><td>Digital ON / OFF</td></tr>
<tr><td>Ultrasonic / IR</td><td>Non-contact</td><td>Time of flight of the wave</td><td>Distance in cm</td></tr>
</table></div>
<h3>1.1 Potentiometric position sensor</h3>
<p class="q">A resistive track with a sliding wiper is used. The wiper is coupled to the moving object.
The output voltage is V<sub>out</sub> = V<sub>in</sub> &times; (x / L), so the voltage is directly
proportional to position. It is cheap and gives a large output, but the wiper wears out and the track gets
noisy.</p>
""" + figures_core.render("10.1") + """
<h3>1.2 Hall effect position sensor</h3>
<p class="q">When a current carrying conductor is placed in a magnetic field, a voltage appears across it at
right angles to both the current and the field: <span class="b">V<sub>H</sub> = (B I) / (n e t)</span>.
A small Hall IC (A3144, SS49E) is kept near a rotating magnet. Whenever the magnet passes, the IC gives a
pulse. Counting the pulses gives the position and speed &mdash; this is how the
<span class="b">BLDC motor and the bicycle speedometer</span> work.</p>

<h2><span class="no">2</span>Motion (Speed) Sensors</h2>
<p class="q">Motion means the change of position with time, so a motion sensor measures
<span class="b">speed</span> (rpm or m/s) and sometimes <span class="b">direction</span>. Important types:</p>
<ul class="dot">
  <li><span class="b">Tachogenerator (DC tachometer)</span> &mdash; a small DC generator coupled to the
      shaft; the generated EMF is proportional to speed. Simple and rugged.</li>
  <li><span class="b">Optical / magnetic encoder</span> &mdash; pulses counted per second give speed; two
      channels 90&deg; apart give direction.</li>
  <li><span class="b">Variable reluctance (VR) sensor</span> &mdash; a coil with a magnet placed near a
      toothed wheel; each passing tooth induces a voltage pulse. Used as the crankshaft position sensor in
      cars.</li>
  <li><span class="b">Hall effect sensor</span> &mdash; digital, very reliable, used in BLDC motors.</li>
  <li><span class="b">Accelerometer / gyro (IMU)</span> &mdash; measures linear acceleration and angular
      velocity, used in drones and mobile phones.</li>
</ul>
""" + figures_core.render("10.2") + """
<div class="formula">Speed (rpm) = (pulses per second &times; 60) / (number of slots)</div>
<h3>Applications</h3>
<ul class="arr">
  <li>CNC machines, robots, 3D printers &mdash; position feedback of axes.</li>
  <li>Motor speed control in washing machines, fans, electric vehicles.</li>
  <li>Crankshaft and camshaft position sensing in petrol and diesel engines.</li>
  <li>Proximity switches on conveyor lines to count bottles or packets.</li>
  <li>Parking sensors and drone altitude hold (ultrasonic).</li>
</ul>
""" + """
<!--EXTRAS-->
<h2><span class="no">3</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A 10 k&Omega; linear potentiometer of travel 100 mm is fed with 5 V. The wiper is at 35 mm from the zero end. Find V<sub>out</sub>.</div>
<p class="q"><span class="b">Solution.</span> V<sub>out</sub> = V<sub>in</sub> &times; x/L = 5 &times; 35/100 V<sub>out</sub> = 1.75 V Sensitivity = 5 V / 100 mm = 50 mV per mm. <span class="hl">V<sub>out</sub> = 1.75 V.</span></p>
<div class="formula"><span class="b">Problem 2.</span> A 1024-pulse-per-revolution incremental encoder is read for 0.2 s and counts 1200 pulses. Find shaft speed in rpm.</div>
<p class="q"><span class="b">Solution.</span> Revolutions = 1200 / 1024 = 1.1719 rev in 0.2 s. Speed = 1.1719 / 0.2 = 5.859 rev/s. rpm = 5.859 &times; 60 = 351.6 rpm. <span class="hl">N &asymp; 352 rpm.</span></p>
<div class="formula"><span class="b">Problem 3.</span> A Hall sensor closes at B<sub>op</sub> = 35 mT with a magnet that decays 1.5 % per year. Estimate how many years before a 2 mm gap increase causes a miss, given field &prop; 1/r&sup3; from an initial gap of 4 mm.</div>
<p class="q"><span class="b">Solution.</span> Field at 4 mm &rarr; 6 mm: ratio = (4/6)&sup3; = 0.296 &mdash; far below any margin. In practice a 25 % field margin is designed in, tolerating roughly 8 % gap growth. Gap grows mainly from vibration loosening, not from magnet ageing; check torque on brackets during PM. <span class="hl">Mechanical gap control matters more than magnet ageing &mdash; verify 4 mm gap in PM.</span></p>
<h2><span class="no">4</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Difference between absolute and incremental encoding?</span><br><span class="o">A.</span> Absolute encoders report the true angle at every instant, even after power loss; incremental encoders only count changes and need a reference at start-up.</p>
<p class="q"><span class="b">Q2. What are quadrature signals?</span><br><span class="o">A.</span> Two pulse channels 90&deg; apart; their phase order reveals direction and combining edges gives 2&times; or 4&times; resolution.</p>
<p class="q"><span class="b">Q3. How does a tachogenerator measure speed?</span><br><span class="o">A.</span> It is a small generator whose output voltage is proportional to shaft speed, giving an immediate analog rpm signal.</p>
<p class="q"><span class="b">Q4. Why use a Hall sensor for speed pickup?</span><br><span class="o">A.</span> Non-contact, no wear, works through dust and oil where optical slotted wheels would clog.</p>
<p class="q"><span class="b">Q5. What is homing in motion control?</span><br><span class="o">A.</span> Moving an axis to a fixed reference switch at start-up to establish the coordinate origin before absolute work begins.</p>
<p class="q"><span class="b">Q6. Where are resolvers preferred over encoders?</span><br><span class="o">A.</span> In hot, vibrating environments such as traction motors &mdash; they are rugged rotating transformers with no optical parts.</p>
<h2><span class="no">5</span>Summary</h2>

<p class="q">Position sensing answers where and speed sensing answers how fast. Potentiometers give simple absolute voltage, Hall devices give contactless digital edges, and encoders give high-resolution quadrature counts for servo loops. Correct gaps, screened cables and a reliable homing procedure are what keep the numbers the controller sees equal to the real shaft or table position.</p>
<h2><span class="no">6</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Linear pot</th><th>Incremental encoder</th><th>Hall speed sensor</th></tr>
<tr><td>Type</td><td>Absolute analog</td><td>Incremental digital</td><td>Digital pulses</td></tr>
<tr><td>Resolution</td><td>Continuous (noise limited)</td><td>e.g. 1024 ppr, 4&times; decode</td><td>1 per tooth</td></tr>
<tr><td>Output</td><td>0&ndash;5 V</td><td>A/B/Z TTL or line driver</td><td>Open-collector square wave</td></tr>
<tr><td>Speed limit</td><td>Wiper wear limits speed</td><td>Up to MHz class counting</td><td>Depends on gear tooth size</td></tr>
<tr><td>Life</td><td>10<sup>6</sup> operations (wear)</td><td>Bearing life (no contact wear)</td><td>Effectively unlimited</td></tr>
<tr><td>Typical use</td><td>Valve position, joysticks</td><td>CNC and robot axes</td><td>Wheel speed, crank position</td></tr>
</table></div>
""")

# ====================================================================== #
# TOPIC 11 : Level and Flow sensors
# ====================================================================== #
B.append("""
<h2><span class="no">1</span>Level Sensors</h2>
<div class="def"><span class="cap">Definition</span>
A <b>level sensor</b> measures the <b>height of a liquid (or solid) surface</b> inside a tank, silo or vessel
and converts it into an electrical signal. Measurement may be <b>point level</b> (liquid present / absent at
one point) or <b>continuous level</b> (exact height).</div>
<div class="tw"><table>
<tr><th>Method</th><th>Principle</th><th>Contact?</th><th>Typical use</th></tr>
<tr><td><b>Float type</b></td><td>Buoyancy &mdash; float rises with level, moves a magnet / reed switch or a
potentiometer</td><td>Yes</td><td>Water tanks, sump pumps</td></tr>
<tr><td><b>Displacer type</b></td><td>Apparent weight of a submerged rod changes with level</td><td>Yes</td>
<td>Boiler drum level</td></tr>
<tr><td><b>Hydrostatic (DP)</b></td><td>P = &rho; g h, pressure at the bottom is proportional to height</td>
<td>Yes</td><td>Tanks, wells, dam monitoring</td></tr>
<tr><td><b>Capacitive</b></td><td>Liquid acts as dielectric, capacitance changes with level</td><td>Yes / probe</td>
<td>Conductive and non-conductive liquids</td></tr>
<tr><td><b>Ultrasonic</b></td><td>Time taken by a sound pulse to return from the surface</td><td>No</td>
<td>Corrosive liquids, sewage, grains</td></tr>
<tr><td><b>Radar (guided wave)</b></td><td>Time of flight of microwave</td><td>No</td><td>Oil tanks, high accuracy</td></tr>
<tr><td><b>Conductivity probe</b></td><td>Two electrodes conduct only when dipped</td><td>Yes</td>
<td>Pump ON/OFF control of water</td></tr>
</table></div>
""" + figures_core.render("11.1") + """

<h2><span class="no">2</span>Flow Sensors</h2>
<div class="def"><span class="cap">Definition</span>
A <b>flow sensor (flow meter)</b> measures the <b>rate of flow</b> of a liquid or gas through a pipe. It is
expressed as <b>volumetric flow</b> (litre per minute, m&sup3;/hr) or <b>mass flow</b> (kg/hr).</div>
<h3>2.1 Orifice plate (differential pressure flow meter)</h3>
<p class="q">A thin plate with a small concentric hole is inserted in the pipe. The flow velocity increases
at the constriction, so the pressure there falls (Bernoulli's theorem). The pressure difference
P&#8321; &minus; P&#8322; across the plate is measured with a differential pressure transmitter and the flow
is calculated. This is the cheapest and most widely used industrial flow meter.</p>
""" + figures_core.render("11.2") + """
<h3>2.2 Turbine flow meter</h3>
<p class="q">A small multi-blade rotor is placed in the flow. The flowing fluid rotates the rotor and its
speed is proportional to the flow velocity. A magnetic pickup coil counts the pulses generated by each
passing blade. Very accurate for clean liquids and gases.</p>
<h3>2.3 Electromagnetic flow meter</h3>
<p class="q">The pipe is non-magnetic and lined with an insulator. When a <span class="b">conductive
liquid</span> flows through a magnetic field, an EMF is induced across two electrodes:
<span class="b">E = B L v</span>. It has no moving part and no obstruction, so it is used for sewage,
slurry and chemicals.</p>
<h3>2.4 Rotameter (variable area meter)</h3>
<p class="q">A float is kept inside a vertical tapered glass tube. The flow lifts the float until the upward
drag equals the weight of the float. The height of the float gives the flow directly. It is a simple local
indicator, no power required.</p>
<div class="tw"><table>
<tr><th>Meter</th><th>Output</th><th>Advantage</th><th>Disadvantage</th></tr>
<tr><td>Orifice + DP</td><td>&Delta;P</td><td>Cheap, no moving part, standard</td><td>Pressure loss, limited turndown</td></tr>
<tr><td>Turbine</td><td>Pulses</td><td>Very accurate, wide range</td><td>Bearing wear, needs clean fluid</td></tr>
<tr><td>Magnetic</td><td>mV</td><td>No obstruction, bidirectional</td><td>Only conductive liquids, needs power</td></tr>
<tr><td>Vortex</td><td>Frequency</td><td>Good for steam, no moving part</td><td>Needs minimum velocity</td></tr>
<tr><td>Rotameter</td><td>Visual height</td><td>Simple, cheap, no power</td><td>Local indication only, glass breaks</td></tr>
</table></div>
<h3>Applications</h3>
<ul class="arr">
  <li>Water supply metering, irrigation and sewage flow measurement.</li>
  <li>Steam, fuel gas and air flow in boilers and furnaces.</li>
  <li>Chemical dosing, batching and custody transfer of petroleum.</li>
  <li>Medical &mdash; oxygen flow meter in anaesthesia machines.</li>
</ul>
<div class="tip"><span class="cap">One line summary</span>
<b>Level</b> tells "how much height of material is inside the tank"; <b>flow</b> tells "how much quantity is
passing through the pipe every second". Both are needed to control a tank &mdash; inflow, outflow and level
must always be balanced.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">3</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> An orifice plate meter is calibrated so that Q = 0.05 &times; &radic;&Delta;P with &Delta;P in Pa and Q in m&sup3;/h. Find Q at &Delta;P = 400 Pa, and the new &Delta;P if Q doubles.</div>
<p class="q"><span class="b">Solution.</span> Q = 0.05 &times; &radic;400 = 0.05 &times; 20 = 1.0 m&sup3;/h. Q &prop; &radic;&Delta;P, so doubling Q needs 4&times; &Delta;P. New &Delta;P = 400 &times; 4 = 1600 Pa. <span class="hl">Q = 1.0 m&sup3;/h at 400 Pa; doubled flow needs 1600 Pa.</span></p>
<h2><span class="no">4</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Why is Q proportional to the square root of &Delta;P in an orifice meter?</span><br><span class="o">A.</span> Bernoulli's equation gives velocity &prop; &radic;&Delta;P and volumetric flow is velocity times area, so the differential pressure must be square-rooted in the transmitter.</p>
<p class="q"><span class="b">Q2. What fluids can an electromagnetic flow meter handle?</span><br><span class="o">A.</span> Any liquid that conducts at least about 5 &micro;S/cm &mdash; water, acids, slurries &mdash; but not pure solvents or oil.</p>
<p class="q"><span class="b">Q3. How does a guided radar (TDR) level probe work?</span><br><span class="o">A.</span> A pulse travels down the probe, reflects at the liquid surface, and the time difference gives level regardless of foam or density changes.</p>
<p class="q"><span class="b">Q4. Why is a bypass rotameter not suitable for billing?</span><br><span class="o">A.</span> It is a variable-area local indicator with modest accuracy; fiscal transfer needs certified meters with traceable calibration.</p>
<p class="q"><span class="b">Q5. What is totaliser functionality in a flow transmitter?</span><br><span class="o">A.</span> It integrates pulse or flow-rate input over time to display total volume or mass, like an odometer for fluid.</p>
<p class="q"><span class="b">Q6. What causes a float switch to stick?</span><br><span class="o">A.</span> Scale, wax, sticky residues or mechanical wear; materials must be chosen compatible with the process fluid.</p>
<h2><span class="no">5</span>Summary</h2>

<p class="q">Level instrumentation determines how much is in the tank, flow instrumentation determines how fast it moves, and both feed inventory control and billing. Ultrasonic, radar, float and differential-pressure methods cover level; orifice, turbine, electromagnetic and variable-area methods cover flow. Every selection must match fluid properties and required accuracy, and every meter needs periodic verification against a known volume.</p>
<h2><span class="no">6</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Ultrasonic level</th><th>Orifice + dP</th><th>Electromagnetic flow</th></tr>
<tr><td>Principle</td><td>Echo time of sound</td><td>Bernoulli differential</td><td>Faraday's law</td></tr>
<tr><td>Range</td><td>0.5&ndash;15 m typical</td><td>Depends on transmitter span</td><td>10 mm &ndash; 3 m bore</td></tr>
<tr><td>Accuracy</td><td>&plusmn;0.25&ndash;0.5 %</td><td>&plusmn;1&ndash;2 % of reading</td><td>&plusmn;0.2&ndash;0.5 %</td></tr>
<tr><td>Output</td><td>4&ndash;20 mA, HART</td><td>4&ndash;20 mA (&radic; extracted)</td><td>Pulse / 4&ndash;20 mA</td></tr>
<tr><td>Fluid limits</td><td>Clean liquids, some foam ok</td><td>Cleanish liquids, single phase</td><td>Needs conductivity</td></tr>
</table></div>
""")

for i, body in enumerate(B):
    save(i, body)
print("done part A")
