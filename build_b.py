# -*- coding: utf-8 -*-
"""Builds topic pages 12 - 27 and the index page of the handwritten notes site."""
import os
from build_a import TOPICS, save, OUT
import helpers as H
import figures_core
import figs_a, figs_b, figs_c, figs_d  # register the 55 builders

B = {}   # index in TOPICS -> body

# ====================================================================== #
# 12 : Humidity (DHT11) and pH sensors
# ====================================================================== #
B[11] = """
<h2><span class="no">1</span>Humidity Sensors &mdash; Introduction</h2>
<p class="q"><span class="b">Humidity</span> is the amount of water vapour present in the air.
<span class="b">Absolute humidity</span> is the mass of vapour per unit volume (g/m&sup3;) and
<span class="b">relative humidity (RH)</span> is the ratio of the actual vapour content to the maximum
possible content at that temperature, expressed in percent. Most sensors measure RH.
Humidity measurement is important in air conditioning, textile mills, food storage, green houses,
pharmaceutical and paper industries.</p>
<h2><span class="no">2</span>DHT11 Humidity and Temperature Sensor</h2>
<h3>2.1 Construction</h3>
<p class="q">The DHT11 is a small blue plastic package which contains three parts on a tiny PCB:
a <span class="b">resistive type humidity sensing element</span>, an <span class="b">NTC thermistor</span>
for temperature, and an <span class="b">8 bit microcontroller</span> which converts the analog signals into
a digital serial data stream. Because the conversion happens inside the sensor, the DHT11 is called a
<span class="hl">smart / digital sensor</span>. It has 4 pins out of which only 3 are used.</p>
<div class="tw"><table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Humidity range / accuracy</td><td>20 to 90 % RH, &plusmn;5 % RH</td></tr>
<tr><td>Temperature range / accuracy</td><td>0 to 50 &deg;C, &plusmn;2 &deg;C</td></tr>
<tr><td>Supply</td><td>3 to 5.5 V DC (5 V typical)</td></tr>
<tr><td>Sampling rate</td><td>Once every 1 second (1 Hz)</td></tr>
<tr><td>Output</td><td>40 bit serial single-bus digital data</td></tr>
</table></div>
""" + figures_core.render("12.1") + """
<h3>2.2 Working</h3>
<p class="q">The humidity sensing element is a resistive material whose resistance changes with the moisture
absorbed from the air; the NTC thermistor gives the temperature. The internal microcontroller reads both,
calculates RH and temperature and sends them as <span class="b">40 bits</span> on a single wire:
8 bit humidity integer + 8 bit humidity decimal + 8 bit temperature integer + 8 bit temperature decimal
+ 8 bit checksum. The communication is started by the microcontroller, which pulls the line LOW for at
least 18 ms and then releases it; the DHT11 answers with a response pulse and then the data. Each bit is a
26&ndash;28 &micro;s LOW followed by a HIGH whose length decides 0 (26 &micro;s) or 1 (70 &micro;s).</p>
<h3>2.3 Applications</h3>
<ul class="arr">
  <li>Automatic air conditioners, de-humidifiers and coolers.</li>
  <li>Weather stations and green house climate control.</li>
  <li>Textile, paper and pharmaceutical humidity control.</li>
  <li>Food and cold storage monitoring, incubators.</li>
</ul>
<div class="note"><span class="cap">DHT11 vs DHT22</span>
DHT22 (AM2302) has the same interface but a better range (&minus;40 to 80 &deg;C, 0 to 100 % RH) and better
accuracy (&plusmn;0.5 &deg;C). If the project needs accurate readings, always prefer DHT22.</div>

<h2><span class="no">3</span>pH Sensor</h2>
<h3>3.1 Introduction</h3>
<p class="q"><span class="b">pH</span> tells how acidic or alkaline a solution is. The scale runs from
0 (strongly acidic) to 14 (strongly alkaline); 7 is neutral (pure water). Mathematically
pH = &minus;log&#8321;&#8320;[H&#8314;]. pH control is very important in water treatment, chemical dosing,
food and dairy industries, swimming pools, hydroponics and electroplating.</p>
<h3>3.2 Construction</h3>
<p class="q">A pH sensor consists of a <span class="b">measuring (glass) electrode</span> and a
<span class="b">reference electrode</span>, both dipped in the test solution. The glass electrode has a very
thin (0.1 mm) special glass bulb filled with a buffer solution of known pH and a silver-silver chloride
wire inside it. The reference electrode contains a stable electrolyte (KCl) and gives a constant potential.
A combination probe has both electrodes in one body. The signal produced is a very small DC voltage, so a
<span class="b">high input impedance buffer amplifier</span> (input impedance greater than 10&sup1;&sup2; &#937;)
is compulsory.</p>
""" + figures_core.render("12.2") + """
<h3>3.3 Working</h3>
<p class="q">Hydrogen ions from the test solution interact with the outer surface of the glass bulb. This
creates a potential difference across the thin glass membrane. The reference electrode provides a fixed
reference potential. The measured voltage is therefore directly proportional to the pH of the solution and
changes by 59.16 mV for each pH unit at 25 &deg;C. Because the voltage changes with temperature, good pH
meters have <span class="b">automatic temperature compensation (ATC)</span>.</p>
<div class="formula">E = E&#8320; &minus; (2.303 R T / F) &times; pH &nbsp;&nbsp;&rarr;&nbsp;
59.16 mV per pH at 25 &deg;C</div>
<h3>3.4 Calibration and Applications</h3>
<p class="q">The probe is calibrated with <span class="b">standard buffer solutions of pH 4, 7 and 9.2</span>
(two point calibration). Without calibration the reading drifts within a few weeks. Applications: water
treatment plants, swimming pool control, dairy and beverage industry, soil testing, hydroponics,
electroplating bath control and effluent (ETP) monitoring.</p>
<div class="warn"><span class="cap">Care</span>
The glass bulb is <b>very fragile</b>. Keep the probe wet (in KCl solution) when not in use, never let it
dry out, and never touch the bulb with fingers or a cloth.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">4</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A DHT11 returns raw humidity count 980 on its internal scale where 0&ndash;1023 maps to 20&ndash;80 %RH (factory-scaled). Find the humidity.</div>
<p class="q"><span class="b">Solution.</span> Fraction = 980/1023 = 0.958. RH = 20 + 0.958 &times; (80 &minus; 20) = 20 + 57.5 RH &asymp; 77.5 % &mdash; realistically the module itself prints %RH directly. <span class="hl">RH &asymp; 77 % (module output is usually already in %RH).</span></p>
<h2><span class="no">5</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What does %RH mean?</span><br><span class="o">A.</span> Relative humidity: the water vapour present compared with the maximum the air could hold at that temperature, expressed in percent.</p>
<p class="q"><span class="b">Q2. Why are polymer humidity sensors temperature sensitive?</span><br><span class="o">A.</span> Adsorption equilibrium shifts with temperature, so RH elements need temperature compensation to give correct %RH.</p>
<p class="q"><span class="b">Q3. What is the Nernst slope for pH?</span><br><span class="o">A.</span> 2.303 RT/F &asymp; 59.16 mV per pH unit at 25 &deg;C; it is the electrode's millivolts-per-pH sensitivity.</p>
<p class="q"><span class="b">Q4. How should a pH electrode be stored?</span><br><span class="o">A.</span> Always in pH 4 or pH 7 storage solution, never in distilled water, which leaches ions from the glass and shortens life.</p>
<h2><span class="no">6</span>Summary</h2>

<p class="q">Humidity sensing relies on the water affinity of a polymer or oxide layer, and pH sensing on the potential developed across a selective glass membrane. Both outputs are chemistry-dependent, temperature-dependent and ageing, so calibration intervals and correct storage matter as much as the initial selection.</p>
<h2><span class="no">7</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>DHT11</th><th>Industrial humidity element</th><th>pH electrode</th></tr>
<tr><td>Range</td><td>20&ndash;80 %RH, 0&ndash;50 &deg;C</td><td>0&ndash;100 %RH</td><td>0&ndash;14 pH</td></tr>
<tr><td>Accuracy</td><td>&plusmn;5 %RH, &plusmn;2 &deg;C</td><td>&plusmn;1&ndash;3 %RH</td><td>&plusmn;0.01&ndash;0.1 pH</td></tr>
<tr><td>Output</td><td>Digital single wire</td><td>Capacitance / voltage</td><td>&plusmn;59 mV/pH</td></tr>
</table></div>
"""


# ====================================================================== #
# 13 : Soil and Smoke sensors
# ====================================================================== #
B[12] = """
<h2><span class="no">1</span>Soil Moisture Sensor</h2>
<h3>1.1 Introduction and need</h3>
<p class="q">A soil moisture sensor measures the <span class="b">water content of the soil</span>. It is the
heart of every <span class="b">automatic irrigation system</span> because watering must be done only when the
soil is actually dry. Watering on a fixed time schedule either wastes water or drowns the plant.</p>
<h3>1.2 Construction</h3>
<p class="q">The sensor has two parts. The first is the <span class="b">probe</span> &mdash; two nickel
plated or carbon tracks printed on a fibre glass board, kept parallel and a few millimetres apart. This
probe is pushed into the soil. The second part is the <span class="b">comparator module</span> which carries
an <span class="b">LM393 comparator IC</span>, a preset (potentiometer) for adjusting the threshold, one
green power LED, one output LED and a 3 pin header. The probe has two terminals which connect to the module.</p>
""" + figures_core.render("13.1") + """
<h3>1.3 Working</h3>
<p class="q">The soil between the two probe tracks behaves as a <span class="b">resistor</span>. Dry soil has
very few free ions, so its resistance is very high (mega ohms). Wet soil has plenty of dissolved ions, so its
resistance becomes low (a few kilo ohms). The probe is connected in a voltage divider; the resulting voltage
is compared with the reference voltage set by the preset. If the soil moisture is below the set value the
output is HIGH (dry), otherwise LOW (wet). The analog output AO can also be read by the ADC to get the
percentage of moisture.</p>
<h3>1.4 Applications</h3>
<ul class="arr">
  <li>Automatic drip and sprinkler irrigation in farms and gardens.</li>
  <li>Green house and nursery climate control.</li>
  <li>Golf course and lawn watering automation.</li>
  <li>Soil research, moisture mapping, drought monitoring.</li>
</ul>
<div class="warn"><span class="cap">Big practical problem</span>
Passing DC current through wet soil causes <b>electrolysis and corrosion</b>, so the cheap probe gets
damaged in a few weeks. Solutions: power the probe only for a few milliseconds before reading, use a
<b>capacitive (contactless)</b> soil sensor, or use stainless steel probes.</div>

<h2><span class="no">2</span>Smoke Sensor (Smoke Detector)</h2>
<h3>2.1 Introduction</h3>
<p class="q">A smoke sensor detects the smoke particles produced in the beginning of a fire, long before the
fire becomes visible or hot. It is a life saving device and is compulsory in offices, hotels, hospitals,
server rooms and industries. There are three main types:
<span class="b">ionisation</span>, <span class="b">photoelectric (optical)</span> and
<span class="b">semiconductor (MQ-2 type)</span>.</p>
<h3>2.2 Construction and working &mdash; Photoelectric type</h3>
<p class="q">Inside a dark chamber an <span class="b">infra-red LED</span> and a
<span class="b">photodiode</span> are placed at an angle so that the light beam does not fall on the
photodiode directly. When smoke enters the chamber, the smoke particles
<span class="b">scatter the light</span> and some of it falls on the photodiode. The photodiode current
increases, the amplifier output rises and the alarm is triggered. This type is best for
<span class="b">smouldering fires</span>.</p>
""" + figures_core.render("13.2") + """
<h3>2.3 Ionisation type</h3>
<p class="q">A very small amount of radioactive material (Americium-241) ionises the air inside a chamber,
allowing a small steady current to flow between two electrodes. When smoke enters, the ions attach to the
smoke particles and the <span class="b">current falls</span>. This fall is detected and the alarm sounds.
It responds very fast to <span class="b">fast flaming fires</span> but is less sensitive to smouldering
smoke.</p>
<h3>2.4 Applications</h3>
<ul class="arr">
  <li>Fire alarm systems in buildings, hotels, hospitals, schools and industries.</li>
  <li>Server rooms, control rooms, warehouses and museums.</li>
  <li>Kitchen exhaust and LPG leak cum smoke alarms (MQ-2).</li>
  <li>Chimney and duct smoke detection.</li>
</ul>
<div class="tw"><table>
<tr><th>Type</th><th>Detects</th><th>Advantage</th><th>Disadvantage</th></tr>
<tr><td>Ionisation</td><td>Fast flaming fire</td><td>Very fast, cheap</td><td>Radioactive source, nuisance alarms from cooking</td></tr>
<tr><td>Photoelectric</td><td>Smouldering smoke</td><td>Fewer false alarms, no radiation</td><td>Slightly slower for flaming fire</td></tr>
<tr><td>Semiconductor (MQ-2)</td><td>Smoke, LPG, CO</td><td>Very cheap, easy with microcontroller</td><td>Needs pre-heat, not for certified fire alarm</td></tr>
</table></div>
""" + """
<!--EXTRAS-->
<h2><span class="no">3</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A capacitive soil sensor is calibrated dry at 310 pF and waterlogged at 780 pF. It reads 540 pF in the field. Find the volumetric water content if 0 % &rarr; 310 pF and 40 % &rarr; 780 pF.</div>
<p class="q"><span class="b">Solution.</span> Fraction = (540 &minus; 310)/(780 &minus; 310) = 230/470 = 0.489 &theta; = 0 + 0.489 &times; 40 = 19.6 % by volume Irrigation thresholds are then set, e.g. irrigate at 15 %, stop at 28 %. <span class="hl">Water content &asymp; 19.6 % by volume.</span></p>
<h2><span class="no">4</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Compare resistive and capacitive soil moisture sensors.</span><br><span class="o">A.</span> Resistive probes pass current through the soil (electrode corrosion, salinity sensitive); capacitive probes measure dielectric constant with no exposed current and last longer.</p>
<p class="q"><span class="b">Q2. Why must soil sensors be recalibrated per soil type?</span><br><span class="o">A.</span> Bulk density, salinity and organic matter change the capacitance-to-moisture curve, so a single factory curve misreads across soils.</p>
<p class="q"><span class="b">Q3. What particle size does a photoelectric smoke sensor see?</span><br><span class="o">A.</span> Smoke particles around 0.4&ndash;10 &micro;m that Mie-scatter the chamber LED or lamp light onto the detector.</p>
<p class="q"><span class="b">Q4. How does an ionisation chamber detect smoke?</span><br><span class="o">A.</span> Smoke particles reduce ion current from a trace radioactive source; the fall in current is compared with a reference chamber.</p>
<p class="q"><span class="b">Q5. Why do steam and dust cause false alarms?</span><br><span class="o">A.</span> They scatter light or displace ions similarly to smoke; multi-sensor logic and time patterns distinguish them.</p>
<p class="q"><span class="b">Q6. Where are soil moisture sensors actually installed?</span><br><span class="o">A.</span> At root depth near representative plants, away from walls and wetting lines, at more than one point per irrigation zone.</p>
<h2><span class="no">5</span>Summary</h2>

<p class="q">Soil moisture sensors track slow water content changes for irrigation control using resistive or capacitive principles, while smoke sensors protect life safety with fast optical or ionisation detection. Calibration against known moisture levels, correct probe placement, and understanding each smoke principle's blind spot are what make these sensors reliable in the field rather than merely functional on the bench.</p>
<h2><span class="no">6</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Capacitive soil probe</th><th>Photoelectric smoke</th><th>Ionisation smoke</th></tr>
<tr><td>Principle</td><td>Dielectric constant vs moisture</td><td>Light scattering</td><td>Ion current reduction</td></tr>
<tr><td>Range</td><td>0&ndash;50 % VWC typical</td><td>0.05&ndash;10 %/m obscuration</td><td>0.5&ndash;10 %/m</td></tr>
<tr><td>Output</td><td>Analog voltage / I&#178;C</td><td>Comparator / MCU alarm</td><td>Comparator alarm</td></tr>
<tr><td>Response</td><td>seconds to minutes</td><td>under 30 s (smouldering)</td><td>under 10 s (flaming)</td></tr>
<tr><td>Power</td><td>3.3&ndash;5 V, low duty</td><td>Alarm loop 9 V standby</td><td>Alarm loop standby</td></tr>
</table></div>
"""


# ====================================================================== #
# 14 : Sound sensors
# ====================================================================== #
B[13] = """
<h2><span class="no">1</span>Introduction</h2>
<div class="def"><span class="cap">Definition</span>
A <b>sound sensor</b> is a device that detects <b>sound waves</b> (pressure variations in air) and converts
them into an equivalent <b>electrical signal</b>. The device which does this conversion is called a
<b>microphone</b> or acoustic transducer.</div>
<p class="q">Sound is a mechanical longitudinal wave. Its important parameters are
<span class="b">frequency</span> (20 Hz to 20 kHz for human hearing), <span class="b">amplitude</span>
(loudness, measured in decibel dB) and <span class="b">waveform</span>. A sound sensor gives a voltage whose
amplitude follows the loudness and whose waveform follows the sound pattern.</p>
<h2><span class="no">2</span>Construction (electret condenser microphone)</h2>
<p class="q">The most common sound sensor element is the <span class="b">electret condenser microphone</span>
(ECM). It has a thin <span class="b">diaphragm</span> made of an electret material (permanently charged
plastic film) placed very close to a fixed metal <span class="b">back plate</span>. Together they form a
small capacitor. A <span class="b">JFET</span> is built inside the same capsule as an impedance converter.
When sound waves strike the diaphragm it vibrates, the gap changes, the capacitance changes and a small
alternating voltage appears. Because the output is only a few millivolts, an
<span class="b">amplifier</span> is always required.</p>
""" + figures_core.render("14.1") + """
<h2><span class="no">3</span>Working</h2>
<p class="q">Sound waves make the diaphragm vibrate at the same frequency. Since the capacitance of the
microphone is C = &epsilon;A/d, a change of the gap d produces a change of capacitance and hence a small
AC voltage. This signal is amplified by a transistor or op-amp. In the popular sound sensor module
(LM393 based), the amplified signal goes to the comparator which compares it with a reference set by the
preset. So the module gives two outputs:</p>
<ul class="dot">
  <li><span class="b">AO (analog output)</span> &mdash; voltage proportional to the loudness, read by the ADC.</li>
  <li><span class="b">DO (digital output)</span> &mdash; HIGH when sound is below the set level and LOW when
      the sound crosses it (or the reverse, depending on the module).</li>
</ul>
<h2><span class="no">4</span>Other sound sensors</h2>
<div class="tw"><table>
<tr><th>Sensor</th><th>Principle</th><th>Use</th></tr>
<tr><td>Dynamic (moving coil) microphone</td><td>Coil moves in a magnetic field</td><td>Stage, studio</td></tr>
<tr><td>Condenser / electret microphone</td><td>Capacitance change</td><td>Mobile, laptops, sensor modules</td></tr>
<tr><td>Piezoelectric microphone</td><td>Charge on a crystal</td><td>Contact mics, knock sensors</td></tr>
<tr><td>MEMS microphone</td><td>Micro-machined diaphragm + IC</td><td>Smartphones, voice assistants</td></tr>
<tr><td>Ultrasonic transducer (40 kHz)</td><td>Piezoelectric, beyond hearing</td><td>Distance measurement, pest repeller</td></tr>
</table></div>
<h2><span class="no">5</span>Applications</h2>
<ul class="arr">
  <li><span class="b">Voice controlled systems</span> &mdash; clapping switch, voice assistant, speech
      recognition.</li>
  <li><span class="b">Noise level monitoring</span> in industries and near highways (sound level meter).</li>
  <li>Machine fault detection by listening to abnormal noise.</li>
  <li>Baby monitor, burglar alarm, ultrasonic distance measurement.</li>
  <li>Hearing aids and public address systems.</li>
</ul>
<div class="tip"><span class="cap">Note for the exam</span>
Sound sensor = <b>acoustic transducer</b>. Its important specifications are <b>sensitivity</b>
(mV/Pa), <b>frequency response</b> (Hz), <b>signal to noise ratio</b> (dB) and <b>directivity</b>.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A microphone with sensitivity &minus;44 dBV/Pa (re 1 V/Pa) hears 94 dB SPL. Find its output voltage, given 94 dB SPL &asymp; 1 Pa.</div>
<p class="q"><span class="b">Solution.</span> &minus;44 dB means V = 10<sup>&minus;44/20</sup> = 6.31&times;10<sup>&minus;3</sup> V per Pa. At 1 Pa: V = 6.31 mV. Doubling pressure adds 6 dB, so 100 dB &rArr; 2 Pa &rArr; 12.6 mV. <span class="hl">V<sub>out</sub> &asymp; 6.3 mV at 94 dB SPL.</span></p>
<div class="formula"><span class="b">Problem 2.</span> Two machines produce 85 dB and 88 dB at a workstation. Find the combined level and check it against a 90 dB exposure limit.</div>
<p class="q"><span class="b">Solution.</span> Add intensities: ratio = 10<sup>(88&minus;85)/10</sup> = 10<sup>0.3</sup> = 2.0. Combined = 10 lg(10<sup>8.5</sup> + 10<sup>8.8</sup>) = 88 + 10 lg(1 + 0.5) = 89.76 dB 89.76 dB &lt; 90 dB limit &mdash; margin is only 0.24 dB, so any addition breaches it. <span class="hl">Combined &asymp; 89.8 dB (just under the 90 dB limit).</span></p>
<div class="formula"><span class="b">Problem 3.</span> A sound level meter on A-weighting shows 78 dB(A) and the dose timer runs 8 h. The permissible 8-h level is 85 dB(A). Is the dose within limit? By how much can level rise for the same dose?</div>
<p class="q"><span class="b">Solution.</span> Dose ratio = 10<sup>(78&minus;85)/5</sup> = 10<sup>&minus;1.4</sup> = 0.040 of allowable &mdash; very safe. Exchange rate 3 dB: level could rise 7 dB above 78 &rArr; 85 dB(A) at same time. NIOSH allows exactly 85 dB(A) for 8 h; OSHA uses 90 dB(A) with 5 dB rule. <span class="hl">Dose is about 4 % of limit; safe to 85 dB(A) for 8 h.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What is the working principle of an electret condenser microphone?</span><br><span class="o">A.</span> A permanently charged electret diaphragm forms a capacitor with a back plate; sound moves the diaphragm, changing capacitance and current in the JFET buffer.</p>
<p class="q"><span class="b">Q2. Why are measurement microphones calibrated with a pistonphone?</span><br><span class="o">A.</span> A pistonphone injects a known 114 or 94 dB reference tone so the whole chain is verified before and after a survey.</p>
<p class="q"><span class="b">Q3. What is the difference between dB SPL and dB sound level?</span><br><span class="o">A.</span> dB SPL is the physical pressure level referenced to 20 &micro;Pa; sound level meters apply frequency weightings (A, C) and time weightings before display.</p>
<p class="q"><span class="b">Q4. Why is A-weighting used for hearing-risk surveys?</span><br><span class="o">A.</span> The ear is less sensitive at low frequencies; A-weighting mirrors that response and correlates better with noise-induced hearing loss.</p>
<p class="q"><span class="b">Q5. What causes microphone self-noise?</span><br><span class="o">A.</span> Thermal and electronic noise in the diaphragm and preamplifier sets the floor for quiet measurements, quoted as dB(A) or &micro;V rms.</p>
<p class="q"><span class="b">Q6. Where are MEMS microphones replacing electrets?</span><br><span class="o">A.</span> In phones, headsets and compact IoT audio &mdash; they reflow-solder like any SMD part and tolerate automated assembly.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">Sound sensors convert pressure fluctuations at a diaphragm into electrical signals: electret and MEMS microphones for communication, polarised measurement microphones for instrumentation. Sensitivity in dBV/Pa, self-noise, weighting filters and time response define meter quality, and correct calibration with a pistonphone plus proper windshielding define field accuracy. Combining levels logarithmically, not arithmetically, is the calculation every noise survey depends on.</p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Electret mic (ECM)</th><th>MEMS mic</th><th>Class 2 sound level meter</th></tr>
<tr><td>Sensitivity</td><td>&minus;35 to &minus;44 dBV/Pa</td><td>&minus;26 to &minus;38 dBV/Pa</td><td>Defined by IEC 61672</td></tr>
<tr><td>Frequency range</td><td>50 Hz &ndash; 16 kHz</td><td>100 Hz &ndash; 10 kHz</td><td>20 Hz &ndash; 20 kHz (&plusmn;1 dB)</td></tr>
<tr><td>Supply</td><td>1.5&ndash;10 V with JFET</td><td>1.8&ndash;3.6 V</td><td>Internal battery</td></tr>
<tr><td>Self-noise</td><td>30&ndash;40 dB(A)</td><td>25&ndash;35 dB(A)</td><td>Depends on class</td></tr>
<tr><td>Weighting</td><td>None (raw audio)</td><td>None</td><td>A / C / Z selectable</td></tr>
<tr><td>Typical use</td><td>Voice recorders, intercoms</td><td>Phones, wearables</td><td>Occupational noise surveys</td></tr>
</table></div>
"""


# ====================================================================== #
# 15 : Smart sensors
# ====================================================================== #
B[14] = """
<h2><span class="no">1</span>Definition</h2>
<div class="def"><span class="cap">Definition</span>
A <b>smart sensor (intelligent sensor)</b> is a sensor in which the <b>sensing element, signal conditioning
circuit, microprocessor, memory and a communication interface</b> are combined in a single package, so that
the sensor can <b>process, store, self-check and communicate</b> its own data.</div>
<p class="q">A conventional sensor only gives a raw analog signal which must be amplified, filtered and
converted outside the sensor. A smart sensor does all this inside itself and talks to the controller over a
<span class="b">digital network</span> such as I&sup2;C, SPI, 1-Wire, HART, Profibus, Foundation Fieldbus or
wireless. Examples: DHT11, BME280, MPU-6050, MAX31855, smart pressure transmitters.</p>
<h2><span class="no">2</span>Architecture (block diagram)</h2>
""" + figures_core.render("15.1") + """
<h2><span class="no">3</span>Working</h2>
<p class="q">The physical quantity is first converted into an electrical signal by the sensing element. This
signal is amplified and filtered by the conditioning circuit and then digitised by the ADC. The
microprocessor performs the following jobs on the digital data:</p>
<ol>
  <li><span class="b">Linearisation</span> &mdash; the non-linear sensor curve is converted into a straight
      line by using a look-up table or a polynomial stored in memory.</li>
  <li><span class="b">Temperature compensation</span> &mdash; an inbuilt temperature sensor gives the
      correction so that the reading does not change with ambient temperature.</li>
  <li><span class="b">Auto-zero and span adjustment</span> &mdash; the sensor can be told to take the
      present reading as zero or full scale.</li>
  <li><span class="b">Self diagnosis</span> &mdash; the sensor checks its own wires, supply and signal and
      sends a "sensor fault" message instead of a wrong reading.</li>
  <li><span class="b">Alarm and scaling</span> &mdash; high and low limits are compared inside the sensor and
      a flag is sent.</li>
  <li><span class="b">Digital communication</span> &mdash; the result is sent as digital data with the sensor
      ID, unit, tag name and time stamp.</li>
</ol>
<h2><span class="no">4</span>Advantages and disadvantages</h2>
<div class="tw"><table>
<tr><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>High accuracy because of internal compensation and linearisation</td><td>Costlier than a conventional sensor</td></tr>
<tr><td>Long wiring not a problem &mdash; digital data does not pick up noise</td><td>Needs programming and configuration</td></tr>
<tr><td>Self diagnosis increases reliability and reduces maintenance</td><td>Internal electronics can fail in very hot places</td></tr>
<tr><td>Easy replacement &mdash; calibration data is inside the sensor</td><td>Response can be slower due to internal averaging</td></tr>
<tr><td>Many sensors can share one communication bus (multi-drop)</td><td>Needs a compatible controller / protocol</td></tr>
</table></div>
<h2><span class="no">5</span>Applications</h2>
<ul class="arr">
  <li>Smart pressure and temperature transmitters in DCS based chemical plants.</li>
  <li>Automobile &mdash; tyre pressure, air bag, engine management (all smart MEMS sensors).</li>
  <li>Mobile phones, smart watches, drones (accelerometer, gyro, compass, barometer).</li>
  <li>Industrial Internet of Things (IIoT) and wireless sensor networks.</li>
  <li>Smart home and smart agriculture nodes.</li>
</ul>
<div class="note"><span class="cap">Exam line</span>
<b>Sensor</b> measures, <b>transducer</b> converts, <b>transmitter</b> standardises the signal
(4&ndash;20 mA), and a <b>smart sensor</b> measures + processes + communicates.</div>
""" + """
<!--EXTRAS-->
<p class="q">A smart sensor is best understood as a measuring device plus a small engineering office on the same chip. The raw element still does the physics, but conversion, linearisation, temperature compensation, alarm limits and digital comms all happen inside the package. For the system designer this shortens the signal path &mdash; fewer analogue metres of cable for noise to enter &mdash; and moves complexity from hardware debugging into configuration registers that can be changed over software.</p>
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A smart RTD sensor returns 16-bit count 0x13C0. The datasheet formula is T = count &times; 0.0625 &minus; 256. Find the temperature.</div>
<p class="q"><span class="b">Solution.</span> 0x13C0 = 1&times;4096 + 3&times;256 + 12&times;16 = 5056 decimal. Scaled value = 5056 &times; 0.0625 = 316.0. T = 316.0 &minus; 256 = 60.0 &deg;C. <span class="hl">T = 60.0 &deg;C.</span></p>
<div class="formula"><span class="b">Problem 2.</span> An accelerometer smart sensor reports peak 16384 counts at &plusmn;4 g full scale on a signed 16-bit output (&minus;32768 to +32767). Find g at count 4096.</div>
<p class="q"><span class="b">Solution.</span> Full scale counts = 32767 for +4 g. Scale = 4 / 32767 = 1.2206&times;10<sup>&minus;4</sup> g/count. At 4096: a = 4096 &times; 1.2206&times;10<sup>&minus;4</sup> = 0.50 g. <span class="hl">a = 0.50 g.</span></p>
<div class="formula"><span class="b">Problem 3.</span> A smart flow sensor on Modbus RTU returns 0x0A2C = 2604 counts on a scaled register where 4000 counts = 100.0 m&sup3;/h. Find the flow.</div>
<p class="q"><span class="b">Solution.</span> Scale = 100.0 / 4000 = 0.025 m&sup3;/h per count. Flow = 2604 &times; 0.025 = 65.1 m&sup3;/h. Hex is used on the wire; engineers usually work in decimal. <span class="hl">Q = 65.1 m&sup3;/h.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What makes a sensor 'smart'?</span><br><span class="o">A.</span> On-board signal processing plus a digital communication interface &mdash; self-calibration, diagnostics and configuration are possible, not just raw measurement.</p>
<p class="q"><span class="b">Q2. Name typical digital buses used by smart sensors.</span><br><span class="o">A.</span> I&#178;C, SPI, 1-Wire, HART superimposed on 4&ndash;20 mA, Profibus PA, Foundation Fieldbus, IO-Link.</p>
<p class="q"><span class="b">Q3. What is a blob or pre-calibrated module?</span><br><span class="o">A.</span> A factory-calibrated sensor-plus-ASIC sealed as one unit; the OEM drops it in without individual calibration.</p>
<p class="q"><span class="b">Q4. Why is scaling information as important as the raw count?</span><br><span class="o">A.</span> The controller multiplies the count by scale and offset; a wrong register scaling silently corrupts every engineering unit downstream.</p>
<p class="q"><span class="b">Q5. What diagnostics do smart transmitters offer?</span><br><span class="o">A.</span> Open sensor, shorted input, out-of-range, calibration due, power supply low and stuck-at-fault detection on the loop.</p>
<p class="q"><span class="b">Q6. How does self-diagnostics improve plant reliability?</span><br><span class="o">A.</span> Failures are announced with an error code instead of passing as a plausible wrong value, so maintenance is triggered before the loop miscontrols.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">Smart sensors integrate element, converter, compensation and digital communication into one package, shifting work from analogue conditioning to register configuration. Correct interpretation of scaled counts, use of the documented formula, and reliance on built-in diagnostics are the skills needed to exploit them. In return the system gains noise immunity, remote reconfiguration and early fault announcement.</p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Typical smart sensor feature</th><th>Benefit</th></tr>
<tr><td>Interface</td><td>I&#178;C / SPI / HART / IO-Link</td><td>Direct digital connection to MCU or PLC</td></tr>
<tr><td>Resolution</td><td>12&ndash;24 bit internal ADC</td><td>Finer steps than 4&ndash;20 mA loop</td></tr>
<tr><td>Compensation</td><td>Temperature, linearisation, drift</td><td>Better accuracy over ambient</td></tr>
<tr><td>Diagnostics</td><td>Open, short, over-range, due-cal</td><td>Failures announce themselves</td></tr>
<tr><td>Configuration</td><td>Address, range, filter, alarms</td><td>Change without rewiring</td></tr>
<tr><td>Power</td><td>1.8&ndash;3.6 V core, bus powered</td><td>Suitable for battery and IoT nodes</td></tr>
<tr><td>Example devices</td><td>BME280, TMP117, XENSIVDLM</td><td>Humidity, precision temperature, presence</td></tr>
</table></div>
"""


# ====================================================================== #
# 16 : Specifications and performance parameters
# ====================================================================== #
B[15] = """
<h2><span class="no">1</span>Why specifications are needed</h2>
<p class="q">Two sensors may look the same and measure the same quantity, yet one may cost ten times the
other. The reason lies in their <span class="b">performance parameters</span>. Before selecting a sensor we
must know what these words mean, because the question paper always asks for definitions of any four or five
of them. They are divided into <span class="b">static characteristics</span> (when the input is steady) and
<span class="b">dynamic characteristics</span> (when the input is changing with time).</p>

<h2><span class="no">2</span>The input &ndash; output characteristic</h2>
""" + figures_core.render("16.1") + """
<h2><span class="no">3</span>Definitions of each parameter</h2>
<div class="def"><span class="cap">1. Accuracy</span>
<b>Accuracy</b> is the closeness of the measured value to the <b>true value</b> of the quantity. It is
expressed as a percentage of full scale or as a plus-minus band. Example: a thermometer of range 0 to
100 &deg;C with &plusmn;1 % accuracy can be wrong by 1 &deg;C anywhere in the range.
<i>Note: a sensor can be precise but not accurate.</i></div>
<div class="def"><span class="cap">2. Resolution</span>
<b>Resolution</b> is the <b>smallest change of input</b> that the sensor can detect and show in its output.
If a digital thermometer displays up to 0.1 &deg;C, its resolution is 0.1 &deg;C. For a digital sensor,
resolution = full scale range / 2<sup>n</sup>, where n is the number of ADC bits
(10 bit &rarr; 1024 steps).</div>
<div class="def"><span class="cap">3. Threshold</span>
<b>Threshold</b> is the <b>minimum value of input</b> below which no output change is observed at all, when
the input is increased from zero. Example: a flow meter may not show anything below 0.5 litre per minute.
The related term <b>dead zone (dead band)</b> is the range of input over which the output does not change in
either direction.</div>
<div class="def"><span class="cap">4. Impedance</span>
<b>Impedance</b> is the total opposition offered by the sensor to the flow of alternating current
(Z = R + jX). The <b>input impedance</b> of a sensor should be <b>high</b> and the <b>output impedance</b>
should be <b>low</b>, otherwise the measuring instrument will load the sensor and give a wrong reading
(loading error). Example: a pH electrode has a very high output impedance, so a buffer amplifier is needed.</div>
<div class="def"><span class="cap">5. Sensitivity</span>
<b>Sensitivity</b> is the <b>ratio of the change in output to the change in input</b> that caused it &mdash;
it is the slope of the input-output curve. Sensitivity S = &Delta;output / &Delta;input. Example: LM35 has a
sensitivity of 10 mV/&deg;C. A high sensitivity sensor gives a large signal for a small change.</div>
<div class="def"><span class="cap">6. Hysteresis</span>
<b>Hysteresis</b> is the difference in the output when the same input is reached by
<b>increasing</b> the input and by <b>decreasing</b> the input. It is caused by friction, backlash, magnetic
retentivity or elastic lag in the sensing element. It is expressed as a percentage of full scale.</div>
""" + figures_core.render("16.2") + """
<div class="def"><span class="cap">7. Linearity</span>
<b>Linearity</b> tells how close the actual input-output curve is to a <b>straight line</b>. It is expressed
as the maximum deviation from the best fit straight line, as a percentage of full scale.
<b>Non-linearity</b> makes calculation difficult, so most sensors are linearised in hardware or software.</div>
<div class="def"><span class="cap">8. Range (Span)</span>
<b>Range</b> is the region between the <b>minimum and maximum</b> values of the input that can be measured.
<b>Span</b> = maximum value &minus; minimum value. Example: a pressure sensor of range 0 to 10 bar has a
span of 10 bar. A sensor of range &minus;10 to +60 &deg;C has a span of 70 &deg;C.</div>
<div class="def"><span class="cap">9. Reliability</span>
<b>Reliability</b> is the ability of the sensor to give the <b>same performance consistently over a long
period</b> without failure. It is expressed by <b>MTBF</b> (Mean Time Between Failures) and by
<b>drift</b> (slow change of reading with time). High reliability means less maintenance and less
downtime.</div>
<div class="def"><span class="cap">10. Selectivity (Specificity)</span>
<b>Selectivity</b> is the ability of the sensor to respond <b>only to the wanted quantity</b> and to ignore
all other quantities. Example: a CO sensor should not respond to alcohol vapour; a pH electrode should not
be affected by the colour of the solution. Poor selectivity gives a false reading.</div>
<div class="def"><span class="cap">11. Bandwidth</span>
<b>Bandwidth</b> is the range of frequencies over which the sensor can follow the input signal without a
significant loss of output (usually within &minus;3 dB of the mid-band gain). It tells how
<b>fast</b> the sensor can respond to a changing input. A sensor with a 1 kHz bandwidth cannot correctly
measure a vibration of 5 kHz.</div>
""" + figures_core.render("16.3") + """
<h2><span class="no">4</span>Other important terms</h2>
<div class="tw"><table>
<tr><th>Term</th><th>Meaning</th></tr>
<tr><td><b>Precision (repeatability)</b></td><td>Closeness of repeated readings of the same input. A precise
sensor gives the same reading every time, even if it is wrong.</td></tr>
<tr><td><b>Reproducibility</b></td><td>Closeness of readings when measured by different persons or
instruments.</td></tr>
<tr><td><b>Drift</b></td><td>Slow unwanted change of output with time at constant input (zero drift,
sensitivity drift).</td></tr>
<tr><td><b>Response time</b></td><td>Time taken to reach the final value (usually 90 % or 63.2 %) after a
step change of input.</td></tr>
<tr><td><b>Time constant (&tau;)</b></td><td>Time to reach 63.2 % of the final value in a first order
sensor.</td></tr>
<tr><td><b>Turndown ratio</b></td><td>Maximum range &divide; minimum range over which accuracy is
maintained.</td></tr>
<tr><td><b>Stability</b></td><td>Ability to keep the same calibration over a period.</td></tr>
<tr><td><b>Input / output impedance</b></td><td>Opposition offered at the input / output terminals.</td></tr>
</table></div>
<div class="tip"><span class="cap">Accuracy vs Precision (very common question)</span>
<b>Accuracy</b> = how near the reading is to the true value.
<b>Precision</b> = how near the readings are to each other.
If a scale reads 50.2, 50.3, 50.2 kg for a true weight of 60 kg, it is <b>precise but not accurate</b>.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">5</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A 0&ndash;20 bar transmitter with accuracy &plusmn;0.5 % of span reads 14.0 bar. Find the possible true value.</div>
<p class="q"><span class="b">Solution.</span> Span = 20 bar; error = 0.5 &times; 20 / 100 = 0.1 bar. True value lies in 14.0 &minus; 0.1 to 14.0 + 0.1 = 13.9 to 14.1 bar. <span class="hl">13.9&ndash;14.1 bar (&plusmn;0.1 bar).</span></p>
<h2><span class="no">6</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Distinguish accuracy, precision and resolution.</span><br><span class="o">A.</span> Accuracy is closeness to true value; precision is repeatability; resolution is the smallest displayable change.</p>
<p class="q"><span class="b">Q2. What is hysteresis error?</span><br><span class="o">A.</span> The maximum difference between ascending and descending outputs at the same input, caused by mechanical or magnetic lag.</p>
<h2><span class="no">7</span>Summary</h2>

<p class="q">Range, span, accuracy, uncertainty, linearity, hysteresis, repeatability, resolution and response time together describe what an instrument can honestly deliver. </p>
<h2><span class="no">8</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Typical good value (process)</th><th>Notes</th></tr>
<tr><td>Range</td><td>Match process min&ndash;max with margin</td><td>Never operate above URV</td></tr>
<tr><td>Accuracy</td><td>&plusmn;0.075&ndash;0.5 % of span</td><td>Classified by standard like 0.5</td></tr>
</table></div>
"""


# ====================================================================== #
# 17 : Actuators - introduction
# ====================================================================== #
B[16] = """
<h2><span class="no">1</span>Introduction</h2>
<p class="q">In Unit I we studied devices which <span class="b">take information from</span> the process.
Now we study the devices which <span class="b">give action to</span> the process. These are the
<span class="r">actuators</span> &mdash; the hands and legs of the control system. The controller decides
what to do, but the actuator is the one which actually does it.</p>
<div class="def"><span class="cap">Definition &mdash; Actuator</span>
An <b>actuator</b> is a device that converts a <b>control signal</b> (usually electrical, pneumatic or
hydraulic) into <b>mechanical motion or physical action</b> such as rotation, linear movement, opening of a
valve, heating, or generation of light and sound.</div>
<div class="def"><span class="cap">Principle of an actuator</span>
An actuator works on the principle of <b>energy conversion</b>: it takes energy from a source (electric
supply, compressed air, hydraulic oil) and, under the command of a small control signal, releases that
energy in a controlled manner to produce the required mechanical action. The control signal is
<b>low power</b> (a few mA or a few volts) while the output action is <b>high power</b>, so the actuator
also acts as a <b>power amplifier</b>.</div>
""" + figures_core.render("17.1") + """
<h2><span class="no">2</span>Difference between Sensor, Transducer and Actuator</h2>
<div class="tw"><table>
<tr><th>Basis</th><th>Sensor</th><th>Transducer</th><th>Actuator</th></tr>
<tr><td>Definition</td><td>Detects a physical quantity and gives a signal</td><td>Converts one form of energy
into another</td><td>Converts a control signal into mechanical action</td></tr>
<tr><td>Direction of energy</td><td>Process &rarr; signal (input device)</td><td>Either direction</td>
<td>Signal &rarr; process (output device)</td></tr>
<tr><td>Position in loop</td><td>Feedback path (measuring element)</td><td>Both paths</td>
<td>Final control element</td></tr>
<tr><td>Power</td><td>Very low (signal level)</td><td>Low</td><td>High (drives the load)</td></tr>
<tr><td>Example</td><td>Thermocouple, LDR, DHT11, load cell</td><td>Microphone, loudspeaker, LVDT</td>
<td>Relay, solenoid valve, servo motor, heater</td></tr>
<tr><td>Human body analogy</td><td>Sense organs (eye, skin)</td><td>Nerves</td><td>Muscles and hands</td></tr>
</table></div>
<div class="note"><span class="cap">Important relation</span>
A sensor is always a transducer, and an actuator is also a transducer (electrical &rarr; mechanical).
So <b>transducer</b> is the widest word. A loudspeaker is an actuator and a transducer, but not a sensor.
A thermocouple is a sensor and a transducer, but not an actuator.</div>
<h2><span class="no">3</span>Classification of actuators</h2>
<div class="tw"><table>
<tr><th>Basis</th><th>Types</th><th>Examples</th></tr>
<tr><td>Energy source</td><td>Electrical, pneumatic, hydraulic, thermal, magnetic</td>
<td>Motor, diaphragm valve, hydraulic cylinder, heater, relay</td></tr>
<tr><td>Motion produced</td><td>Rotary or linear</td><td>DC motor (rotary), solenoid (linear)</td></tr>
<tr><td>Control action</td><td>Two position (ON/OFF) or proportional</td><td>Relay (ON/OFF), control valve
(proportional)</td></tr>
<tr><td>Function</td><td>Pressure control, flow control, power control, motion control</td>
<td>Pressure controller, valve, SCR / TRIAC, servo motor</td></tr>
</table></div>
<h2><span class="no">4</span>Selection of an actuator</h2>
<ul class="arr">
  <li><span class="b">Force or torque</span> required and the speed of movement.</li>
  <li><span class="b">Type of motion</span> &mdash; rotary or linear, and the stroke length.</li>
  <li><span class="b">Available energy</span> &mdash; is compressed air available in the plant?</li>
  <li><span class="b">Fail-safe action</span> &mdash; on failure should it open or close?
      (air to open / air to close)</li>
  <li><span class="b">Accuracy, response time, cost, size and environment</span> (explosive, wet, hot).</li>
</ul>
<div class="tip"><span class="cap">Examples around us</span>
The <b>vibrator of a mobile phone</b> is an actuator. The <b>printer head</b> is moved by a stepper motor
(actuator) while the <b>paper sensor</b> is a sensor. In a <b>washing machine</b>, the water inlet valve is
an actuator and the water level switch is a sensor.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">5</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A pneumatic actuator has an effective piston area of 40 cm&sup2; and supply pressure of 6 bar. Find the force available at full stroke.</div>
<p class="q"><span class="b">Solution.</span> P = 6 bar = 6&times;10<sup>5</sup> Pa; A = 40 cm&sup2; = 4&times;10<sup>&minus;3</sup> m&sup2;. F = P &times; A = 6&times;10<sup>5</sup> &times; 4&times;10<sup>&minus;3</sup> = 2400 N. Derate about 15 % for friction and spring opposition &rArr; about 2040 N useful. <span class="hl">F &asymp; 2400 N (about 2 kN before derating).</span></p>
<div class="formula"><span class="b">Problem 2.</span> A 24 V DC motor draws 0.5 A at no load (R<sub>a</sub> = 1.2 &Omega;) and 4 A at rated load. Torque constant k<sub>t</sub> = 0.075 Nm/A. Find no-load back-emf, armature voltage drop at rated load, and developed torque.</div>
<p class="q"><span class="b">Solution.</span> E<sub>no-load</sub> = V &minus; I<sub>0</sub> R<sub>a</sub> = 24 &minus; 0.5 &times; 1.2 = 23.4 V. Rated drop = I R<sub>a</sub> = 4 &times; 1.2 = 4.8 V, so E = 19.2 V and speed falls about 18 % below no load. T = k<sub>t</sub> I = 0.075 &times; 4 = 0.30 Nm developed at rated load. <span class="hl">E<sub>0</sub> = 23.4 V, drop = 4.8 V, T = 0.30 Nm.</span></p>
<h2><span class="no">6</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What is meant by fail-safe action of an actuator?</span><br><span class="o">A.</span> The position the valve or damper takes when power, signal or instrument air is lost &mdash; typically fail-close or fail-open.</p>
<p class="q"><span class="b">Q2. Why is a spring-and-yoke actuator common on control valves?</span><br><span class="o">A.</span> The spring returns the stem to the fail position without air, and the yoke gives a stiff, aligned mounting for the stem and positioner.</p>
<p class="q"><span class="b">Q3. Differentiate on-off and modulating actuators.</span><br><span class="o">A.</span> On-off actuators only energise fully one way or the other; modulating actuators hold any intermediate position proportional to the controller signal.</p>
<p class="q"><span class="b">Q4. What is stroke time and why is it specified?</span><br><span class="o">A.</span> Time for full travel open-to-close; it must be much less than the process time constant for stable control and less than safety time for protection.</p>
<p class="q"><span class="b">Q5. How are electric actuators protected outdoors?</span><br><span class="o">A.</span> Through enclosure ratings (IP65/67), corrosion-resistant coatings and heaters to stop condensation in the gearbox.</p>
<p class="q"><span class="b">Q6. Give two reasons to prefer pneumatic over electric actuation.</span><br><span class="o">A.</span> Intrinsic safety in hazardous areas, and very high force-to-weight with simple, reliable fail-safe springs.</p>
<h2><span class="no">7</span>Summary</h2>

<p class="q">Actuators convert controller output into motion: pneumatic, hydraulic, electric and manual drives each covering a different corner of force, speed and environment. Selection proceeds from process force or torque through stroke time, duty cycle and fail-safe position to the final rating plate. Control valves add flow characteristics and trim options; every installation must document where the actuator goes when everything fails.</p>
<h2><span class="no">8</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Pneumatic linear</th><th>Electric rotary</th><th>Hydraulic</th></tr>
<tr><td>Typical force</td><td>0.5&ndash;50 kN</td><td>Torque 5&ndash;500 Nm</td><td>10&ndash;500 kN</td></tr>
<tr><td>Supply</td><td>3&ndash;7 bar air</td><td>24 V DC / 230 V AC</td><td>70&ndash;350 bar oil</td></tr>
<tr><td>Fail-safe</td><td>Spring return (choose FC/FO)</td><td>Motor / spring brake</td><td>Accumulator or lock</td></tr>
<tr><td>Stroke time</td><td>1&ndash;60 s</td><td>5&ndash;60 s</td><td>0.5&ndash;10 s</td></tr>
<tr><td>Hazardous area</td><td>Inherently safe option</td><td>Certified enclosure needed</td><td>Special enclosures</td></tr>
<tr><td>Typical use</td><td>Control valves, dampers</td><td>Quarter-turn valves, louvres</td><td>Heavy presses, rams</td></tr>
</table></div>
"""


# ====================================================================== #
# 18 : Pressure and flow control actuators (valves)
# ====================================================================== #
B[17] = """
<h2><span class="no">1</span>What is a control valve?</h2>
<div class="def"><span class="cap">Definition</span>
A <b>control valve</b> is the <b>final control element</b> of a process control loop. It receives the
control signal from the controller and changes the <b>flow area</b> in a pipe, thereby controlling the
<b>flow rate, pressure, level or temperature</b> of the process fluid.</div>
<p class="q">A control valve has two main parts: the <span class="b">valve body</span> (which contains the
plug, seat and the fluid passage) and the <span class="b">actuator</span> (which provides the force to move
the plug). Common actuators are the <span class="b">pneumatic diaphragm</span> (most popular),
<span class="b">pneumatic piston</span>, <span class="b">electric motor operated</span> and
<span class="b">hydraulic</span> actuators.</p>
""" + figures_core.render("18.1") + """
<h2><span class="no">2</span>Flow control actuators (types of valves)</h2>
<div class="tw"><table>
<tr><th>Valve</th><th>Construction</th><th>Use</th></tr>
<tr><td><b>Globe valve</b></td><td>Plug moves perpendicular to the seat, S-shaped body</td>
<td>Throttling (flow control), good control over wide range</td></tr>
<tr><td><b>Gate valve</b></td><td>Flat gate slides up and down</td><td>ON / OFF service only, full flow, low
pressure drop</td></tr>
<tr><td><b>Ball valve</b></td><td>Ball with a hole, quarter turn</td><td>Quick ON / OFF, some throttling</td></tr>
<tr><td><b>Butterfly valve</b></td><td>Disc rotates in the middle of the pipe</td><td>Large pipes, low cost,
low pressure</td></tr>
<tr><td><b>Needle valve</b></td><td>Long tapered needle plug</td><td>Very fine flow control, instrumentation
lines</td></tr>
<tr><td><b>Diaphragm valve</b></td><td>Flexible diaphragm pinches the flow</td><td>Slurry, corrosive and
sterile fluids</td></tr>
<tr><td><b>Pinch valve</b></td><td>Rubber sleeve is pinched</td><td>Slurry and abrasive fluids</td></tr>
<tr><td><b>Three way valve</b></td><td>Three ports, mixing or diverting</td><td>Temperature control by mixing
hot and cold streams</td></tr>
</table></div>
<h2><span class="no">3</span>Working</h2>
<p class="q">The controller compares the measured variable with the set point and sends an output signal of
<span class="b">4&ndash;20 mA</span>. The <span class="b">I/P converter</span> changes this current into a
<span class="b">3&ndash;15 psi</span> air pressure. This air pressure is applied on the diaphragm of the
actuator. The diaphragm pushes the spring and moves the valve stem and the plug. When the plug moves away
from the seat, the flow area increases and the flow increases. A <span class="b">positioner</span> compares
the actual stem position with the demanded position and corrects any error caused by friction or fluid
force.</p>
<div class="formula">Flow through a valve : &nbsp; Q = C<sub>v</sub> &times; &radic;(&Delta;P / SG)</div>
<p class="q">Here C<sub>v</sub> is the valve coefficient (flow in US gallons per minute at 1 psi drop) and SG
is the specific gravity of the fluid. C<sub>v</sub> tells the size of the valve.</p>
<h2><span class="no">4</span>Pressure control actuators</h2>
<ul class="dot">
  <li><span class="b">Pressure control valve (PCV)</span> &mdash; keeps the downstream pressure constant by
      throttling; used on steam headers and gas lines.</li>
  <li><span class="b">Pressure reducing valve (PRV)</span> &mdash; self operated, reduces a high inlet
      pressure to a fixed lower outlet pressure.</li>
  <li><span class="b">Safety / relief valve</span> &mdash; opens automatically when the pressure exceeds the
      set limit; a mechanical actuator for safety.</li>
  <li><span class="b">Back pressure regulator</span> &mdash; maintains the upstream pressure.</li>
  <li><span class="b">Air filter regulator</span> &mdash; supplies clean air at a set pressure to pneumatic
      instruments (1.4 bar typical).</li>
</ul>
<h2><span class="no">5</span>Fail-safe action (very important)</h2>
<div class="tw"><table>
<tr><th>Action</th><th>Meaning</th><th>Chosen when</th></tr>
<tr><td><b>Air to Open (ATO) / Fail Close (FC)</b></td><td>Valve opens when air is applied; on air failure it
closes</td><td>It is safe to stop the flow (fuel line to a burner)</td></tr>
<tr><td><b>Air to Close (ATC) / Fail Open (FO)</b></td><td>Valve closes when air is applied; on air failure
it opens</td><td>It is safe to keep the flow (cooling water to a reactor)</td></tr>
</table></div>
<h2><span class="no">6</span>Applications</h2>
<ul class="arr">
  <li>Flow, level, pressure and temperature control in every chemical, sugar, cement and power plant.</li>
  <li>Steam pressure control in boilers and process headers.</li>
  <li>Water distribution networks and pumping stations.</li>
  <li>Oil and gas pipelines, refineries and LPG bottling plants.</li>
  <li>HVAC control of chilled water and air handling units.</li>
</ul>
""" + """
<!--EXTRAS-->
<h2><span class="no">7</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A valve has C<sub>v</sub> = 25 and passes water (&rho; = 1000 kg/m&sup3;, SG = 1) with &Delta;P = 1 bar (100 kPa). Find flow in m&sup3;/h.</div>
<p class="q"><span class="b">Solution.</span> Q (US gpm) = C<sub>v</sub> &times; &radic;(&Delta;P / SG) = 25 &times; &radic;100 Q = 25 &times; 10 = 250 gpm Convert: 1 gpm = 0.2271 m&sup3;/h &rArr; Q = 250 &times; 0.2271 = 56.8 m&sup3;/h <span class="hl">Q &asymp; 56.8 m&sup3;/h (250 gpm).</span></p>
<div class="formula"><span class="b">Problem 2.</span> An air-to-open valve fails ______ on loss of air; state the position and one application where fail-open is chosen instead.</div>
<p class="q"><span class="b">Solution.</span> Air pressure pushes against the spring to open; loss of air lets the spring close the valve. Fail-closed suits fuel, feed or product lines that must stop. Fail-open suits cooling water, quench or relief-assist duties where losing flow is dangerous. <span class="hl">Fails closed; use fail-open for cooling or utility lines that must keep flowing.</span></p>
<h2><span class="no">8</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What is the valve coefficient C<sub>v</sub>?</span><br><span class="o">A.</span> US gallons per minute of water at 60 &deg;F passing with 1 psi pressure drop &mdash; the sizing number for a valve.</p>
<p class="q"><span class="b">Q2. Compare quick-opening, linear and equal percentage trims.</span><br><span class="o">A.</span> Quick-opening gives most flow early (on-off duty); linear is proportional to travel; equal percentage gives equal flow change per equal percent travel, suitable when process gain varies strongly.</p>
<p class="q"><span class="b">Q3. What is a positioner and why is it needed?</span><br><span class="o">A.</span> A local controller that forces valve position to match the signal despite friction and unbalance &mdash; it fixes stiction and improves stroking speed.</p>
<p class="q"><span class="b">Q4. Why is valve sizing in terms of &Delta;P important?</span><br><span class="o">A.</span> If available &Delta;P across the valve is small at high demand, the valve cavitates or simply cannot pass required flow even at full open.</p>
<p class="q"><span class="b">Q5. What is cavitation and how is it avoided?</span><br><span class="o">A.</span> Liquid flashes to vapour then collapses, pitting trim; avoided with pressure recovery trim, lower &Delta;P per stage, or operating above vapour pressure.</p>
<p class="q"><span class="b">Q6. What tests are done during valve commissioning?</span><br><span class="o">A.</span> Stroke travel, verify fail position, check travel vs mA linearity, tightness test, and travel time measurement.</p>
<h2><span class="no">9</span>Summary</h2>

<p class="q">Control valves act as the final control element: actuator, positioner and internals working together to place flow exactly where the controller demands. Correct C<sub>v</sub> sizing, matched flow characteristic, explicit fail-safe action and healthy stroking mechanics are the four pillars. Without them the best tuning in the world cannot hold the process steady.</p>
<h2><span class="no">10</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Typical specification</th><th>Remark</th></tr>
<tr><td>Body size</td><td>1/2" to 12" DN15&ndash;DN300</td><td>Match line velocity and C<sub>v</sub></td></tr>
<tr><td>C<sub>v</sub> range</td><td>0.1 &ndash; 1000+</td><td>From sizing equation and &Delta;P</td></tr>
<tr><td>Characteristic</td><td>Linear / equal % / quick</td><td>Equal % most common in liquid service</td></tr>
<tr><td>Actuation</td><td>Spring-and-yoke pneumatic</td><td>Air-to-open / air-to-close</td></tr>
</table></div>
"""


# ====================================================================== #
# 19 : Power control devices - SCR, TRIAC, MOSFET
# ====================================================================== #
B[18] = """
<h2><span class="no">1</span>Introduction</h2>
<p class="q">A <span class="b">power control device</span> (also called a power semiconductor switch)
controls a <span class="b">large amount of power</span> in the load by using a <span class="b">very small
control signal</span>. It works as a switch &mdash; fully ON or fully OFF &mdash; and not as a linear
amplifier, so the power loss inside the device is small and the efficiency is high. The three most important
devices are the <span class="r">SCR</span>, the <span class="r">TRIAC</span> and the
<span class="r">MOSFET</span>.</p>

<h2><span class="no">2</span>SCR &mdash; Silicon Controlled Rectifier</h2>
<h3>2.1 Construction</h3>
<p class="q">An SCR is a <span class="b">four layer (P-N-P-N), three junction, three terminal</span>
semiconductor device. The three terminals are the <span class="b">Anode (A)</span>, the
<span class="b">Cathode (K)</span> and the <span class="b">Gate (G)</span>. The gate terminal is taken from
the P layer near the cathode. The silicon chip is mounted on a stud or a disc package with a heat sink
because it handles large currents (from 1 A to more than 1000 A).</p>
<h3>2.2 Working</h3>
<p class="q">An SCR is a <span class="b">latching device</span>. In the forward blocking state (anode
positive) only a tiny leakage current flows. When a small positive current pulse is applied to the gate, the
SCR turns ON and behaves like a closed switch. Once it is ON, <span class="hl">the gate loses control</span>
&mdash; even if the gate signal is removed, the SCR stays ON as long as the anode current is greater than
the <span class="b">holding current</span>. To turn it OFF the anode current must be reduced below the
holding current (commutation). Therefore an SCR can be turned ON by the gate but
<span class="b">cannot be turned OFF by the gate</span>.</p>
""" + figures_core.render("19.1") + """
<div class="tw"><table>
<tr><th>State</th><th>Condition</th></tr>
<tr><td>Forward blocking</td><td>Anode positive, no gate current &rarr; OFF</td></tr>
<tr><td>Forward conduction</td><td>Gate pulse applied &rarr; ON, V<sub>AK</sub> &asymp; 1 to 2 V</td></tr>
<tr><td>Reverse blocking</td><td>Anode negative &rarr; OFF (like a reverse biased diode)</td></tr>
</table></div>

<h2><span class="no">3</span>TRIAC</h2>
<p class="q">A TRIAC is equivalent to <span class="b">two SCRs connected in anti-parallel with a common
gate</span>. It has three terminals: <span class="b">MT1, MT2 and Gate</span>. Because it conducts in
<span class="hl">both directions</span>, it can control AC power with a single device. It is used in
<span class="b">light dimmers, fan speed regulators and AC motor speed control</span>.</p>
""" + figures_core.render("19.2") + """

<h2><span class="no">4</span>MOSFET (Power MOSFET)</h2>
<p class="q">A MOSFET (Metal Oxide Semiconductor Field Effect Transistor) is a
<span class="b">voltage controlled</span> device with three terminals: <span class="b">Gate (G), Drain (D)
and Source (S)</span>. The gate is insulated from the channel by a very thin layer of silicon dioxide, so the
<span class="b">input impedance is extremely high</span> (mega ohms) and the gate draws almost no current.
When the gate-source voltage V<sub>GS</sub> exceeds the threshold voltage (about 2 to 4 V), a channel is
formed and the drain current flows, turning the device ON.</p>
""" + figures_core.render("19.3") + """
<h2><span class="no">5</span>Comparison</h2>
<div class="tw"><table>
<tr><th>Parameter</th><th>SCR</th><th>TRIAC</th><th>MOSFET</th></tr>
<tr><td>Terminals</td><td>Anode, Cathode, Gate</td><td>MT1, MT2, Gate</td><td>Drain, Source, Gate</td></tr>
<tr><td>Conduction</td><td>One direction only</td><td>Both directions</td><td>One direction (body diode)</td></tr>
<tr><td>Control</td><td>Current triggered, latching</td><td>Current triggered, latching</td>
<td>Voltage controlled, not latching</td></tr>
<tr><td>Turn OFF</td><td>Commutation needed</td><td>Natural at AC zero crossing</td><td>Simply make V<sub>GS</sub> = 0</td></tr>
<tr><td>Frequency</td><td>Low (up to a few kHz)</td><td>Low (mains frequency)</td><td>Very high (100 kHz to MHz)</td></tr>
<tr><td>Typical use</td><td>DC motor control, battery charger, HVDC</td><td>Light dimmer, fan regulator, AC heater</td>
<td>SMPS, motor drive, DC-DC converter, relay drive</td></tr>
</table></div>
<div class="tip"><span class="cap">Remember</span>
SCR and TRIAC are <b>latching (semi-controlled)</b> switches used mainly on <b>AC mains</b>.
MOSFET is a <b>fully controlled</b> high speed switch used in <b>low voltage DC</b> circuits and PWM
applications. A MOSFET has a very high input impedance, so a microcontroller pin can drive it directly
through a small resistor.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A 230 V, 50 Hz supply feeds a resistive heater through a TRIAC at firing angle &alpha; = 90&deg;. Find the RMS load voltage and power if R = 48.4 &Omega;.</div>
<p class="q"><span class="b">Solution.</span> V<sub>rms</sub> = (V<sub>m</sub>/&radic;2) &times; &radic;(1 &minus; &alpha;/&pi; + sin2&alpha;/(2&pi;)) with &alpha; in radians, &alpha; = &pi;/2. &radic;(1 &minus; 0.5 + 0) = &radic;0.5 = 0.707; V<sub>rms</sub> = 230 &times; 0.707 = 162.6 V. P = V&sup2;/R = 162.6&sup2; / 48.4 = 545 W (full-on would be 1100 W). <span class="hl">V<sub>rms</sub> = 162.6 V, P &asymp; 545 W.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. How does an SCR differ from a diode?</span><br><span class="o">A.</span> An SCR is a latching four-layer device: it only conducts after a gate pulse once anode is positive, and then stays on until current falls below holding level.</p>
<p class="q"><span class="b">Q2. What is latching current versus holding current?</span><br><span class="o">A.</span> Latching current is the minimum anode current to keep the SCR on right after gate removal; holding current is the minimum to stay on once already latched.</p>
<p class="q"><span class="b">Q3. Why can a TRIAC control AC but an SCR needs two for full control?</span><br><span class="o">A.</span> A TRIAC conducts both half-cycles with either gate polarity; a single SCR blocks one half-cycle, so back-to-back SCRs or a BRCS pair are used for full-wave control.</p>
<p class="q"><span class="b">Q4. What does 'firing angle' mean?</span><br><span class="o">A.</span> The delay from the zero crossing of the AC waveform to the moment the device is triggered; it directly sets RMS power delivered.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">SCRs, TRIACs and power MOSFETs form the core of electric power control: phase-controlled conduction for AC mains duty, high-frequency chopper switching for DC and inverter duty. Firing angle sets RMS output, duty cycle sets average output, and in both cases losses, heatsinking and protection snubbers must be sized with the same care as the switching device itself.</p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>SCR (e.g. C106)</th><th>TRIAC (e.g. BTA16)</th><th>MOSFET (e.g. IRF540)</th></tr>
<tr><td>Voltage rating</td><td>400&ndash;1600 V</td><td>400&ndash;800 V</td><td>55&ndash;600 V (low R<sub>DS</sub>)</td></tr>
<tr><td>Current rating</td><td>10&ndash;100 A (heatsunk)</td><td>16&ndash;40 A</td><td>20&ndash;100 A pulsed</td></tr>
<tr><td>Gate / drive</td><td>Pulse, few mA</td><td>Pulse, few mA</td><td>Voltage driven, 10 V gate, low charge</td></tr>
<tr><td>Switching speed</td><td>Line frequency, &mu;s turn-off</td><td>Line frequency</td><td>ns &mdash; 100 kHz+ PWM</td></tr>
</table></div>
"""


# ====================================================================== #
# 20 : Magnetic control devices - Relay and Solenoid
# ====================================================================== #
B[19] = """
<h2><span class="no">1</span>Introduction</h2>
<p class="q"><span class="b">Magnetic control devices</span> use the magnetic field produced by an
electromagnet (a coil carrying current) to produce mechanical movement. The two most common devices are the
<span class="r">relay</span> and the <span class="r">solenoid</span>. Both work on the same principle:
<span class="b">when current flows through a coil, a magnetic field is produced which attracts a movable iron
part</span>.</p>

<h2><span class="no">2</span>Relay</h2>
<h3>2.1 Definition and Construction</h3>
<div class="def"><span class="cap">Definition</span>
A <b>relay</b> is an <b>electromagnetically operated switch</b>. A small current in its coil produces a
magnetic field which moves an armature and opens or closes one or more sets of contacts, thereby controlling
a separate, usually high power, circuit.</div>
<p class="q">A relay has four main parts: (1) the <span class="b">coil (electromagnet)</span> wound on a soft
iron core, (2) the <span class="b">armature</span> &mdash; a movable soft iron lever, (3) a
<span class="b">return spring</span> which brings the armature back when the coil is de-energised, and
(4) the <span class="b">contacts</span> &mdash; normally open (NO), normally closed (NC) and common (C).
Relays are available for 5 V, 6 V, 12 V and 24 V DC coils with contact ratings of 5 A to 30 A.</p>
""" + figures_core.render("20.1") + """
<h3>2.2 Working</h3>
<p class="q">When the coil is energised, the magnetic field attracts the armature against the spring force.
The armature carries the moving contact, so the NO contact closes and the NC contact opens. The load
connected to the contacts is therefore switched ON. When the coil current is removed, the spring returns the
armature and the contacts come back to their normal position. Because the coil circuit and the contact
circuit are <span class="hl">electrically isolated</span>, a 5 V microcontroller can safely switch 230 V
mains. The diode connected across the coil is compulsory &mdash; it absorbs the high voltage spike produced
by the collapsing magnetic field and protects the transistor or the microcontroller.</p>
<h3>2.3 Types and applications</h3>
<div class="tw"><table>
<tr><th>Type</th><th>Feature</th><th>Use</th></tr>
<tr><td>Electromechanical relay (EMR)</td><td>Moving contacts, 5&ndash;30 A</td><td>General switching</td></tr>
<tr><td>Solid state relay (SSR)</td><td>Opto-coupler + TRIAC, no moving part</td><td>Heater control, fast
switching, long life</td></tr>
<tr><td>Reed relay</td><td>Contacts sealed in a glass tube</td><td>Test equipment, fast, low power</td></tr>
<tr><td>Latching relay</td><td>Stays in position after a pulse</td><td>Energy saving, meters</td></tr>
<tr><td>Protective relay</td><td>Operates on over current / earth fault</td><td>Power system protection</td></tr>
<tr><td>Contactor</td><td>Large relay for motors, 10 A to 1000 A</td><td>Motor starters</td></tr>
</table></div>
<ul class="arr">
  <li>Switching of motors, heaters, pumps and lights by low voltage control signals.</li>
  <li>Isolation between the control circuit and the power circuit.</li>
  <li>Automatic transfer switch, star-delta starter, protection schemes.</li>
  <li>Home automation and relay modules with Arduino.</li>
</ul>

<h2><span class="no">3</span>Solenoid</h2>
<div class="def"><span class="cap">Definition</span>
A <b>solenoid</b> is a coil of wire which, when energised, produces a magnetic field that pulls a movable
iron <b>plunger</b> and converts <b>electrical energy into short linear mechanical motion</b>.</div>
<p class="q"><span class="g">Construction:</span> It has a hollow coil wound on a former, a
<span class="b">fixed iron core (stop)</span> at one end and a movable <span class="b">soft iron
plunger</span> inside. A spring pushes the plunger out when the coil is de-energised. The plunger is connected
to the mechanism to be operated.</p>
<p class="q"><span class="g">Working:</span> When the coil is energised the magnetic flux tries to travel
through the shortest path, so the plunger is pulled into the centre of the coil against the spring force.
The force is proportional to the square of the current and inversely proportional to the square of the air
gap, so the force is maximum at the end of the stroke. When the supply is removed the spring returns the
plunger. The stroke is short (2 to 50 mm) but the force is high and the speed is very fast (a few
milliseconds).</p>
""" + figures_core.render("20.2") + """
<div class="tw"><table>
<tr><th>Basis</th><th>Relay</th><th>Solenoid</th></tr>
<tr><td>Main purpose</td><td>To switch an electrical circuit</td><td>To produce linear mechanical motion</td></tr>
<tr><td>Moving part</td><td>Armature carrying contacts</td><td>Iron plunger connected to a mechanism</td></tr>
<tr><td>Stroke</td><td>Very small (1&ndash;2 mm)</td><td>Larger (5&ndash;50 mm)</td></tr>
<tr><td>Output</td><td>Electrical (closing of contacts)</td><td>Mechanical force and displacement</td></tr>
<tr><td>Example</td><td>12 V relay module</td><td>Solenoid valve, car starter, door lock, pinball kicker</td></tr>
</table></div>
""" + """
<!--EXTRAS-->
<h2><span class="no">4</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A 24 V DC relay coil draws 60 mA. Find coil resistance, power consumption, and the flyback energy stored in a 100 mH coil at steady current.</div>
<p class="q"><span class="b">Solution.</span> R = V/I = 24/0.06 = 400 &Omega;. P = V &times; I = 24 &times; 0.06 = 1.44 W. E = ½ L I&sup2; = 0.5 &times; 0.1 &times; 0.06&sup2; = 180 &micro;J &mdash; small but enough to damage an unclamped transistor. <span class="hl">R = 400 &Omega;, P = 1.44 W, stored energy = 180 &micro;J.</span></p>
<h2><span class="no">5</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Why is a diode connected across a DC relay coil?</span><br><span class="o">A.</span> It clips the high-voltage inductive spike when the coil is switched off, protecting the transistor driver.</p>
<p class="q"><span class="b">Q2. What does '10 A resistive, 1 A inductive' contact rating mean?</span><br><span class="o">A.</span> Inductive loads arc far more at break, so the same contacts must be derated heavily for solenoid, motor or transformer loads.</p>
<p class="q"><span class="b">Q3. Difference between latching and non-latching relays?</span><br><span class="o">A.</span> Non-latching returns to original state when coil de-energises; latching holds position with permanent or mechanical lock until a pulse of opposite polarity.</p>
<p class="q"><span class="b">Q4. How does a solenoid produce linear motion?</span><br><span class="o">A.</span> Current in the coil magnetises the core; the gap field pulls the plunger to reduce reluctance, converting electrical power into stroke force.</p>
<p class="q"><span class="b">Q5. What is drop-out voltage of a relay?</span><br><span class="o">A.</span> Coil voltage below which the armature releases &mdash; typically 70&ndash;80 % of nominal; a sagging supply can cause chatter.</p>
<h2><span class="no">6</span>Summary</h2>

<p class="q">Relays provide galvanically isolated contact switching and solenoids provide direct linear or rotary actuation, both from magnetic circuits. Coil resistance, pull-in and drop-out voltages, contact ratings for the actual load type, and spike suppression are the numbers that decide reliability. Mounted clean, driven with proper flyback protection and derated for inrush, these simple devices run for millions of operations.</p>
<h2><span class="no">7</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>General purpose relay</th><th>DC solenoid valve</th></tr>
<tr><td>Coil</td><td>5&ndash;240 V AC/DC, 0.1&ndash;2 W</td><td>12/24 V DC, 5&ndash;30 W typical</td></tr>
<tr><td>Pull-in / drop-out</td><td>70&ndash;100 % / 10&ndash;40 % of V<sub>nom</sub></td><td>Pull-in rated, drop-out &lt; 70 %</td></tr>
<tr><td>Contacts</td><td>SPDT/DPDT, 8&ndash;10 A resistive</td><td>&mdash; (valve is the load)</td></tr>
</table></div>
"""


# ====================================================================== #
# 21 : Electromechanical motors
# ====================================================================== #
B[20] = """
<h2><span class="no">1</span>Introduction</h2>
<p class="q">An <span class="b">electromechanical motor</span> is an actuator which converts
<span class="b">electrical energy into mechanical rotational energy</span>. It works on the principle that a
current carrying conductor placed in a magnetic field experiences a force
(F = B I L). Motors are the most widely used actuators in industry &mdash; pumps, fans, compressors,
conveyors, robots and machine tools are all driven by motors.</p>
<div class="tw"><table>
<tr><th>Motor</th><th>Supply</th><th>Speed control</th><th>Position control</th><th>Typical use</th></tr>
<tr><td>DC motor</td><td>DC</td><td>Very easy (armature voltage / PWM)</td><td>Needs encoder feedback</td>
<td>Toys, robots, conveyors, fans</td></tr>
<tr><td>Servo motor</td><td>DC + control pulse</td><td>Built in</td><td>Built in (closed loop)</td>
<td>Robotic arm, RC models, CNC</td></tr>
<tr><td>Stepper motor</td><td>DC pulses</td><td>By pulse rate</td><td>Open loop, step by step</td>
<td>3D printer, CNC, printer head</td></tr>
<tr><td>AC induction motor</td><td>AC single / three phase</td><td>VFD needed</td><td>Difficult</td>
<td>Pumps, compressors, machine tools</td></tr>
</table></div>

<h2><span class="no">2</span>DC Motor</h2>
<p class="q"><span class="g">Construction:</span> It has a <span class="b">stator</span> (field magnets or
field winding) and a <span class="b">rotor (armature)</span> carrying the winding. The
<span class="b">commutator</span> and <span class="b">brushes</span> reverse the direction of the armature
current every half revolution so that the torque remains in the same direction.</p>
<p class="q"><span class="g">Working:</span> The speed of a DC motor is proportional to the applied armature
voltage and the torque is proportional to the armature current (N &prop; V, T &prop; I<sub>a</sub>). So speed
is controlled easily by varying the armature voltage, which in modern circuits is done by
<span class="b">PWM using a MOSFET or an H-bridge driver (L293D, L298N)</span>. Reversing the polarity
reverses the direction.</p>
""" + figures_core.render("21.1") + """

<h2><span class="no">3</span>Servo Motor</h2>
<p class="q"><span class="g">Construction:</span> A servo motor is a small package containing a
<span class="b">DC motor</span>, a <span class="b">gear train</span> (to increase the torque), a
<span class="b">potentiometer</span> connected to the output shaft (position feedback), a
<span class="b">control board</span> and three wires &mdash; red (V<sub>CC</sub> +5 V), black or brown
(GND) and yellow or orange (control signal). Standard servos rotate from 0&deg; to 180&deg;; continuous
rotation servos rotate fully.</p>
<p class="q"><span class="g">Working:</span> The control signal is a <span class="b">PWM pulse of 50 Hz
(20 ms period)</span>. The width of the pulse decides the angle: <span class="b">1 ms &rarr; 0&deg;,
1.5 ms &rarr; 90&deg;, 2 ms &rarr; 180&deg;</span>. Inside the servo the potentiometer tells the actual
shaft angle; the control board compares it with the demanded angle and drives the motor until the error
becomes zero. This is a <span class="hl">closed loop position control system built inside the
servo</span>.</p>
""" + figures_core.render("21.2") + """

<h2><span class="no">4</span>Stepper Motor</h2>
<p class="q"><span class="g">Construction:</span> A stepper motor has a <span class="b">stator with several
poles</span> carrying concentrated windings and a <span class="b">rotor with a toothed iron wheel</span>
(variable reluctance type) or a <span class="b">permanent magnet</span>. It has 4, 6 or 8 leads &mdash; a
unipolar motor has 5 or 6 wires and a bipolar motor has 4 wires. The common step angles are
<span class="b">1.8&deg; (200 steps per revolution)</span> and 7.5&deg; (48 steps).</p>
<p class="q"><span class="g">Working:</span> The stator coils are energised in a fixed sequence. Each
energising pattern pulls the rotor teeth into alignment, so the shaft moves by one
<span class="b">step</span>. By counting the number of steps we know the exact angular position
<span class="hl">without any feedback (open loop)</span>, and by changing the step rate we control the speed.
The energising sequence is given by a driver such as the <span class="b">ULN2003</span> or
<span class="b">A4988 / DRV8825</span>.</p>
""" + figures_core.render("21.3") + """

<h2><span class="no">5</span>AC Motor (Induction Motor)</h2>
<p class="q"><span class="g">Construction:</span> It has a <span class="b">stator</span> with a three phase
(or single phase) distributed winding and a <span class="b">rotor</span> which is either a
<span class="b">squirrel cage</span> (aluminium or copper bars short circuited by end rings &mdash; 90 % of
industrial motors) or a <span class="b">wound rotor</span> (slip ring type).</p>
<p class="q"><span class="g">Working:</span> When a three phase supply is given to the stator, a
<span class="b">rotating magnetic field (RMF)</span> is produced which rotates at the synchronous speed
N<sub>s</sub> = 120 f / P. This RMF cuts the rotor bars, an EMF and hence a current is induced in them
(transformer action), and the current carrying rotor conductors in the magnetic field experience a force.
The rotor therefore starts rotating in the same direction as the RMF but always at a slightly lower speed.
The difference is called <span class="b">slip</span>.</p>
<div class="formula">N<sub>s</sub> = 120 f / P &nbsp;&nbsp;&nbsp; s = (N<sub>s</sub> &minus; N) / N<sub>s</sub>
&nbsp;&nbsp;&nbsp; N = N<sub>s</sub>(1 &minus; s)</div>
<p class="q">Speed control of an induction motor is done by a <span class="b">VFD (variable frequency
drive)</span> which changes the supply frequency while keeping V/f constant.</p>
<div class="tw"><table>
<tr><th>Point</th><th>Servo motor</th><th>Stepper motor</th></tr>
<tr><td>Control</td><td>Closed loop (feedback)</td><td>Open loop (counting steps)</td></tr>
<tr><td>Motion</td><td>Smooth continuous rotation</td><td>Discrete steps</td></tr>
<tr><td>Speed</td><td>High (3000 to 6000 rpm)</td><td>Low to medium</td></tr>
<tr><td>Torque at high speed</td><td>High</td><td>Falls sharply</td></tr>
<tr><td>Cost</td><td>High</td><td>Low</td></tr>
<tr><td>Use</td><td>Robots, CNC axis, high precision</td><td>3D printer, printer, simple positioning</td></tr>
</table></div>
""" + """
<!--EXTRAS-->
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A 4-pole induction motor runs at 1440 rpm on 50 Hz supply. Find synchronous speed and slip.</div>
<p class="q"><span class="b">Solution.</span> N<sub>s</sub> = 120 f / P = 120 &times; 50 / 4 = 1500 rpm. Slip s = (1500 &minus; 1440)/1500 = 0.04 = 4 %. <span class="hl">N<sub>s</sub> = 1500 rpm, slip = 4 %.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Why does an induction motor always run below synchronous speed?</span><br><span class="o">A.</span> Torque needs relative motion (slip); at synchronous speed no current is induced and torque is zero.</p>
<p class="q"><span class="b">Q2. What is pull-out torque?</span><br><span class="o">A.</span> Maximum torque before the motor stalls; steppers lose steps beyond it.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">Actuator motors span induction machines for general speed control, DC and brushless DC for wide range torque, steppers for open-loop positioning and servos for closed-loop precision.</p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>3-ph induction</th><th>Stepper (NEMA 17)</th><th>Servo (with encoder)</th></tr>
<tr><td>Speed control</td><td>VFD, pole change</td><td>Pulse rate (open loop)</td><td>Closed-loop drive</td></tr>
<tr><td>Position info</td><td>None (open loop)</td><td>Counted steps</td><td>Encoder absolute/incremental</td></tr>
</table></div>
"""


# ====================================================================== #
# 22 : Process control systems
# ====================================================================== #
B[21] = """
<h2><span class="no">1</span>What is a process and what is process control?</h2>
<div class="def"><span class="cap">Definitions</span>
A <b>process</b> is any operation or series of operations in which <b>energy or material is transformed</b>
&mdash; for example heating water, distilling alcohol, grinding cement or filling bottles.<br>
<b>Process control</b> is the technique of <b>maintaining the output of a process at the desired value</b>
by continuously measuring it, comparing it with the desired value and correcting the difference
automatically.</div>
<h2><span class="no">2</span>Elements of a process control system</h2>
""" + figures_core.render("22.1") + """
<div class="tw"><table>
<tr><th>Element</th><th>Function</th><th>Example (boiler water level control)</th></tr>
<tr><td><b>Process</b></td><td>The plant where the transformation takes place</td><td>The boiler</td></tr>
<tr><td><b>Controlled variable (PV)</b></td><td>The quantity to be controlled</td><td>Water level</td></tr>
<tr><td><b>Set point (SP)</b></td><td>The desired value of the controlled variable</td><td>70 % level</td></tr>
<tr><td><b>Manipulated variable (MV)</b></td><td>The quantity adjusted by the controller</td><td>Feed water flow</td></tr>
<tr><td><b>Measuring element</b></td><td>Measures the PV and sends the signal</td><td>DP level transmitter</td></tr>
<tr><td><b>Error detector</b></td><td>Finds e = SP &minus; PV</td><td>Comparator in the controller</td></tr>
<tr><td><b>Controller</b></td><td>Decides the corrective action</td><td>PID controller</td></tr>
<tr><td><b>Final control element</b></td><td>Actually changes the process</td><td>Control valve</td></tr>
<tr><td><b>Disturbance</b></td><td>Any unwanted input that upsets the process</td><td>Sudden change of steam demand</td></tr>
</table></div>
<h2><span class="no">3</span>Types of process control</h2>
<h3>3.1 Continuous (analog) process control</h3>
<p class="q">Here the controlled variable changes <span class="b">continuously over a range</span> of values
and the controller output is also continuous. The objective is to hold the variable at the set point in
spite of disturbances. Examples: temperature of a furnace, level of a tank, pressure of a boiler, flow rate,
pH of an effluent, speed of a motor. Instruments used: transmitters, PID controllers, control valves,
recorders. This is the classical field of <span class="b">process control / instrumentation</span>.</p>
""" + figures_core.render("22.2") + """
<h3>3.2 Discrete state (sequential / logic) control</h3>
<p class="q">Here the process variables and the controller outputs can take only a
<span class="b">finite number of distinct states</span> &mdash; normally ON or OFF, open or closed, high or
low. The control action follows a <span class="b">sequence of steps</span> which depends on logic conditions
(AND, OR, NOT) and on timers and counters. Examples: bottle filling machine, washing machine cycle, traffic
light, elevator, conveyor sequence, machine tool cycle. The device used is the
<span class="b">PLC (Programmable Logic Controller)</span>.</p>
<h3>3.3 Composite discrete / continuous control</h3>
<p class="q">Most real plants need <span class="b">both</span>. In a bottling plant the
<span class="b">level of the liquid in the tank is controlled continuously</span> by a PID controller and a
control valve, while the <span class="b">bottle handling, capping and labelling is controlled
discretely</span> by a PLC using proximity switches and timers. The modern solution is a single
<span class="b">hybrid PLC / DCS</span> which has both analog (PID) and digital (ladder logic) capability.
Examples: batch reactors, boiler control, water treatment plant, packaging lines, automobile assembly.</p>
<div class="tw"><table>
<tr><th>Feature</th><th>Continuous control</th><th>Discrete control</th></tr>
<tr><td>Variable</td><td>Analog, varies over a range</td><td>Digital, two or few states</td></tr>
<tr><td>Controller</td><td>PID controller, DCS</td><td>PLC, relay logic, timers, counters</td></tr>
<tr><td>Final element</td><td>Control valve (throttling)</td><td>Solenoid valve, contactor, relay (ON/OFF)</td></tr>
<tr><td>Goal</td><td>Regulation &mdash; hold the value at set point</td><td>Sequence &mdash; do the steps in order</td></tr>
<tr><td>Programming</td><td>Tuning of P, I, D</td><td>Ladder logic / function block</td></tr>
<tr><td>Example</td><td>Boiler drum level</td><td>Washing machine cycle</td></tr>
</table></div>
<h2><span class="no">4</span>Open loop versus closed loop</h2>
<p class="q">In an <span class="b">open loop</span> system the output is not measured and no correction is
made &mdash; for example an immersion heater switched ON for 10 minutes by a timer. It is simple and cheap
but cannot correct for disturbances. In a <span class="b">closed loop</span> (feedback) system the output is
measured, compared with the set point and the error is used to correct the input &mdash; for example a
thermostat controlled water heater. Closed loop control is more accurate and can reject disturbances, but it
can become unstable if not tuned properly.</p>
<div class="tip"><span class="cap">Supervisory levels of automation</span>
<b>Field level</b> (sensors and actuators) &rarr; <b>Control level</b> (PLC / DCS / PID controllers) &rarr;
<b>Supervisory level</b> (SCADA, HMI) &rarr; <b>Management level</b> (MES / ERP).</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">5</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A level loop has set point 50 %, process variable 47 % and a proportional-only controller with gain K<sub>c</sub> = 2.5 %/% and bias of 40 %. Find controller output.</div>
<p class="q"><span class="b">Solution.</span> Error e = SP &minus; PV = 50 &minus; 47 = +3 %. u = bias + K<sub>c</sub> e = 40 + 2.5 &times; 3 = 47.5 %. Output drives valve to 47.5 % open (4&ndash;20 mA equivalent). <span class="hl">u = 47.5 %.</span></p>
<h2><span class="no">6</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What are the four elements of a process control loop?</span><br><span class="o">A.</span> Measurement (sensor/transmitter), comparison (controller), final control element (valve, drive), and the process itself.</p>
<p class="q"><span class="b">Q2. Difference between continuous and discrete state control?</span><br><span class="o">A.</span> Continuous manipulates a variable proportionally over a range; discrete changes between fixed states (on/off, step sequences).</p>
<p class="q"><span class="b">Q3. What is open-loop control?</span><br><span class="o">A.</span> Output is set without reference to the measured result &mdash; no correction of disturbances, used where the process is very predictable.</p>
<p class="q"><span class="b">Q4. Why is feedback control preferred in plants?</span><br><span class="o">A.</span> It automatically corrects unmeasured disturbances and model errors by acting on the measured error.</p>
<p class="q"><span class="b">Q5. Name the signals carried on a typical analog loop.</span><br><span class="o">A.</span> 4&ndash;20 mA or 1&ndash;5 V measurement in, 4&ndash;20 mA output out, plus Hart or fieldbus digital overlay where used.</p>
<p class="q"><span class="b">Q6. What is an interlock?</span><br><span class="o">A.</span> A logic condition that prevents an unsafe action until safety criteria are satisfied &mdash; the discrete twin of feedback control.</p>
<h2><span class="no">7</span>Summary</h2>

<p class="q">Process control systems close the loop between measurement, decision and action using sensors, controllers and final control elements. Continuous control handles smoothly varying quantities with feedback, discrete control handles states and sequences with logic, and composite systems combine both. Open loop is simpler but blind to disturbances; closed loop is the default wherever the process wanders.</p>
<h2><span class="no">8</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Typical loop element</th><th>Standard value</th></tr>
<tr><td>Measurement</td><td>Transmitter to controller</td><td>4&ndash;20 mA / HART, fieldbus</td></tr>
<tr><td>Controller</td><td>PLC / DCS analog task</td><td>Scan 0.1&ndash;1 s per loop</td></tr>
<tr><td>Output</td><td>To final control element</td><td>4&ndash;20 mA, 0&ndash;10 V, discrete</td></tr>
<tr><td>Final element</td><td>Control valve, drive, heater</td><td>Sized for max demand + margin</td></tr>
<tr><td>Feedback</td><td>PV compared with SP each scan</td><td>Error drives corrective action</td></tr>
<tr><td>Alarm layer</td><td>High/low deviation alerts</td><td>Independent of continuous action</td></tr>
</table></div>
"""


# ====================================================================== #
# 23 : Process characteristics
# ====================================================================== #
B[22] = """
<h2><span class="no">1</span>Introduction</h2>
<p class="q">Before designing or tuning a controller we must understand the
<span class="b">character of the process</span> itself &mdash; how it responds when we change the input.
Every process is described by four important characteristics: the
<span class="r">process equation</span>, the <span class="r">process load</span>, the
<span class="r">process lag</span> and <span class="r">self regulation</span>.</p>
<h2><span class="no">2</span>Process equation</h2>
<p class="q">The process equation is the <span class="b">mathematical relation between the input and the
output of the process</span>. It is obtained by writing the mass or energy balance of the process. It tells
how the process will behave and what type of controller is suitable.</p>
<div class="def"><span class="cap">Example &mdash; liquid tank</span>
Let Q<sub>i</sub> be the inflow, Q<sub>o</sub> the outflow, A the cross sectional area and h the level.
Mass balance gives:<br>
<b>A (dh/dt) = Q<sub>i</sub> &minus; Q<sub>o</sub></b><br>
If the outflow is through a valve with resistance R, then Q<sub>o</sub> = h/R, so<br>
<b>A (dh/dt) + h/R = Q<sub>i</sub></b> &nbsp;&rarr;&nbsp; <b>AR (dh/dt) + h = R Q<sub>i</sub></b><br>
This is a <b>first order</b> process with time constant &tau; = A R and gain K = R.</div>
<p class="q">In general the process equation is written as a <span class="b">transfer function</span>:
G(s) = Output(s) / Input(s). A first order process gives G(s) = K / (1 + &tau;s). Most industrial processes
(temperature, level, pressure) are first or second order with some dead time.</p>
<h2><span class="no">3</span>Process load</h2>
<div class="def"><span class="cap">Definition</span>
<b>Process load</b> is the <b>rate at which the process consumes or demands the controlled quantity</b>.
It is also called the <b>demand</b>. A change in load is the most common <b>disturbance</b> to a control
system.</div>
<p class="q">Examples: in a water tank the load is the outflow drawn by the consumers; in a boiler the load
is the steam drawn by the plant; in a temperature controlled oven the load is the heat lost to the
surroundings plus the cold material put inside; in a generator the load is the electrical power drawn.</p>
<ul class="dot">
  <li><span class="b">Constant load</span> &mdash; the demand does not change with time (easy to control).</li>
  <li><span class="b">Variable load</span> &mdash; the demand changes continuously (needs good controller
      tuning).</li>
  <li><span class="b">Shock load</span> &mdash; a sudden large change of demand (needs fast response and
      derivative action).</li>
</ul>
<h2><span class="no">4</span>Process lag</h2>
<p class="q">No process responds instantly. The delay between the application of the input and the
appearance of the response is called <span class="b">process lag</span> (dead time or transport lag). There
are three kinds:</p>
<div class="tw"><table>
<tr><th>Type</th><th>Meaning</th><th>Example</th></tr>
<tr><td><b>Transfer lag (transport lag)</b></td><td>Time taken by the material or signal to travel from one
point to another</td><td>Long pipe between the valve and the temperature sensor</td></tr>
<tr><td><b>Capacity lag</b></td><td>Delay due to the storage capacity of the process</td><td>Large tank
takes long time to change level</td></tr>
<tr><td><b>Measurement lag</b></td><td>Delay in the sensor or transmitter</td><td>Thermowell protects the
sensor but slows it down</td></tr>
</table></div>
""" + figures_core.render("23.1") + """
<div class="formula">First order process : &nbsp; y(t) = K &Delta;u (1 &minus; e<sup>&minus;t/&tau;</sup>)
&nbsp;&nbsp;&nbsp; &tau; = RC (time constant)</div>
<p class="q">A large lag is bad for control because the controller takes action on the basis of old
information. Lag is reduced by placing the sensor close to the point of control, using a fast sensor and
reducing the distance between the valve and the sensor.</p>
<h2><span class="no">5</span>Self regulation</h2>
<div class="def"><span class="cap">Definition</span>
<b>Self regulation</b> is the inherent ability of a process to <b>balance itself at a new steady state
without any external control action</b>, after a change in input or load.</div>
<p class="q"><span class="g">Self regulating process:</span> Consider a tank with an inlet and an outlet
valve. If the inflow is increased, the level rises. As the level rises, the head and therefore the outflow
also increases. Finally the outflow becomes equal to the new inflow and the level settles at a new higher
value. The process has <span class="hl">balanced itself</span>. Examples: liquid level tank, heat exchanger,
RC circuit, gas pressure vessel.</p>
<p class="q"><span class="g">Non self regulating process:</span> Here the process does not settle by itself;
the output keeps changing until it reaches a limit. Example: a tank whose outlet is pumped at a
<span class="b">constant rate</span> independent of the level. If the inflow exceeds the pumped outflow the
level will keep rising and the tank will overflow. Another example is a
<span class="b">temperature process with no heat loss</span>. Such processes are called
<span class="b">integrating processes</span> and always need a controller.</p>
""" + figures_core.render("23.2") + """
<div class="tip"><span class="cap">Summary of process characteristics</span>
<b>Process equation</b> tells the mathematical behaviour, <b>process load</b> is the demand (disturbance),
<b>process lag</b> is the delay, and <b>self regulation</b> tells whether the process can balance itself.
A good controller is always selected after studying these four characteristics.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A well-stirred tank of time constant &tau; = 4 min receives a step disturbance. Find how long until the temperature reaches 63.2 % of its final change, and the % at 2 min.</div>
<p class="q"><span class="b">Solution.</span> First-order: y(t) = &Delta;y (1 &minus; e<sup>&minus;t/&tau;</sup>). At t = &tau; = 4 min: y = 63.2 % of &Delta;y by definition. At t = 2 min: 1 &minus; e<sup>&minus;0.5</sup> = 1 &minus; 0.607 = 39.3 %. <span class="hl">63.2 % at 4 min; 39.3 % at 2 min.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Define process lag.</span><br><span class="o">A.</span> The exponential delay while the process variable moves toward its new steady value after a disturbance, characterised by time constant &tau; (63.2 % point).</p>
<p class="q"><span class="b">Q2. What is dead time and why is it the enemy of control?</span><br><span class="o">A.</span> Pure transport or measurement delay with no output movement until it expires; it adds phase lag that forces lower controller gains to stay stable.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">Every process presents its own mix of capacity, dead time, lag and self-regulation. First-order responses reach 63.2 % of the change in one time constant, dead time adds pure delay measured in seconds or minutes, and the ratio &theta;/&tau; indicates how hard the loop will be to tune.</p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Characteristic</th><th>Symbol / unit</th><th>Effect on control</th></tr>
<tr><td>Process gain</td><td>K (&Delta;PV/&Delta;manipulated)</td><td>Sets required controller gain</td></tr>
<tr><td>Dead time</td><td>&theta; (s, min)</td><td>Limits gain; causes oscillation if large</td></tr>
<tr><td>Time constant</td><td>&tau; (s, min)</td><td>Response speed; 63.2 % at 1&tau;</td></tr>
</table></div>
"""


# ====================================================================== #
# 24 : Control system parameters
# ====================================================================== #
B[23] = """
<h2><span class="no">1</span>Introduction</h2>
<p class="q">To specify, design or tune a controller we must be able to describe its working in numbers. The
important control system parameters are: <span class="b">error, variable range (span), control parameter
range, control time and cycling</span>. Let us understand each one with a common example &mdash; a water
tank whose level is to be controlled between 40 % and 60 % by a transmitter of range 0 to 100 %.</p>
""" + figures_core.render("24.1") + """
<h2><span class="no">2</span>Error</h2>
<div class="def"><span class="cap">Definition</span>
<b>Error</b> is the <b>difference between the set point and the measured value</b> of the controlled
variable.<br>
<b>e = SP &minus; PV</b> (for direct acting) &nbsp; or &nbsp; <b>e = PV &minus; SP</b> (for reverse acting).</div>
<ul class="dot">
  <li><span class="b">Positive error</span> &mdash; the PV is below the SP, so the controller must increase
      the output.</li>
  <li><span class="b">Negative error</span> &mdash; the PV is above the SP, so the output must be
      decreased.</li>
  <li><span class="b">Offset (steady state error)</span> &mdash; the small permanent error that remains
      even after the process has settled. It is produced by proportional control and is removed by integral
      action.</li>
  <li><span class="b">Dynamic error</span> &mdash; the error during the transient period while the process is
      still changing.</li>
</ul>
<div class="formula">Error in % = [(SP &minus; PV) / span of the variable] &times; 100</div>
<h2><span class="no">3</span>Variable range and span</h2>
<div class="def"><span class="cap">Definition</span>
<b>Variable range</b> (measurement range) is the <b>minimum and maximum values of the controlled variable
that the transmitter can measure</b>. <b>Span</b> is the difference between the maximum and minimum
values.</div>
<p class="q">Example: a level transmitter is calibrated for 0 to 200 cm. Then the variable range is
0&ndash;200 cm and the span is 200 cm. If the range is changed to 50&ndash;200 cm the span becomes 150 cm.
The <span class="b">control range</span> (or operating range) is the smaller portion of the variable range
within which we actually want to control, for example 80 to 120 cm.</p>
<h2><span class="no">4</span>Control parameter range (proportional band)</h2>
<div class="def"><span class="cap">Definition</span>
<b>Control parameter range</b>, more commonly called the <b>proportional band (PB)</b>, is the <b>range of
change in the controlled variable that is needed to drive the controller output through its full range
(0 to 100 %)</b>. It is the reciprocal of the proportional gain.</div>
<div class="formula">PB (%) = (1 / K<sub>p</sub>) &times; 100 &nbsp;&nbsp;&nbsp; K<sub>p</sub> = 100 / PB</div>
<p class="q">If a tank level of span 0 to 100 % has a proportional band of 50 %, then a level change of
50 % is needed to move the valve from fully closed to fully open. A <span class="b">narrow PB (high
gain)</span> gives a fast and sensitive response but may cause oscillation. A <span class="b">wide PB (low
gain)</span> gives a slow and stable response but a large offset.</p>
<h2><span class="no">5</span>Control time</h2>
<p class="q">Control time is the time related quantity of a control loop. The following terms are used:</p>
<div class="tw"><table>
<tr><th>Term</th><th>Definition</th></tr>
<tr><td><b>Response time</b></td><td>Time taken by the PV to reach the new steady state after a change in
set point or load.</td></tr>
<tr><td><b>Rise time</b></td><td>Time taken to go from 10 % to 90 % of the final value.</td></tr>
<tr><td><b>Settling time</b></td><td>Time taken for the PV to enter and stay within a specified band
(usually &plusmn;2 % or &plusmn;5 %) of the final value.</td></tr>
<tr><td><b>Dead time (t&#8320;)</b></td><td>Time before any response is seen after the input is changed.</td></tr>
<tr><td><b>Time constant (&tau;)</b></td><td>Time to reach 63.2 % of the final change.</td></tr>
<tr><td><b>Integral time (T<sub>i</sub>)</b></td><td>Time in which the integral action repeats the
proportional action (reset time, minutes per repeat).</td></tr>
<tr><td><b>Derivative time (T<sub>d</sub>)</b></td><td>Time by which the derivative action anticipates the
proportional action (rate time).</td></tr>
</table></div>
<h2><span class="no">6</span>Cycling</h2>
<div class="def"><span class="cap">Definition</span>
<b>Cycling</b> is the <b>repeated oscillation of the controlled variable about the set point</b>. The
variable goes up and down continuously instead of settling. The number of oscillations per unit time is the
<b>cycling frequency</b> and the peak difference is the <b>amplitude of cycling</b>.</div>
<p class="q">Cycling is caused by: (i) too narrow a proportional band (too much gain), (ii) too much
integral action, (iii) large dead time or lag in the process, (iv) hunting of the final control element
(sticky valve), and (v) a wrong controller action (direct instead of reverse). Small cycling around the set
point is normal in two position (ON/OFF) control and is called <span class="b">hunting</span>; large and
growing cycling means the loop is <span class="b">unstable</span> and must be detuned.</p>
<div class="tw"><table>
<tr><th>Parameter</th><th>Unit</th><th>Good design value</th></tr>
<tr><td>Error (offset)</td><td>% of span</td><td>Zero (use I action)</td></tr>
<tr><td>Overshoot</td><td>% of final value</td><td>10 to 30 %</td></tr>
<tr><td>Settling time</td><td>seconds / minutes</td><td>As short as stability allows</td></tr>
<tr><td>Cycling amplitude</td><td>% of span</td><td>Less than &plusmn;1 % for good control</td></tr>
<tr><td>Dead time to time constant ratio</td><td>&mdash;</td><td>t&#8320;/&tau; &lt; 0.3 for easy control</td></tr>
</table></div>
<div class="tip"><span class="cap">Quick revision</span>
<b>Error</b> = SP &minus; PV &nbsp;|&nbsp; <b>Span</b> = max &minus; min of the variable &nbsp;|&nbsp;
<b>PB</b> = 100/K<sub>p</sub> &nbsp;|&nbsp; <b>Control time</b> = rise / settling / dead time &nbsp;|&nbsp;
<b>Cycling</b> = oscillation about the set point.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">7</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A temperature transmitter spans 0&ndash;200 &deg;C with 4&ndash;20 mA output. Find the mA at 75 &deg;C and the temperature represented by 13.6 mA.</div>
<p class="q"><span class="b">Solution.</span> % span = (75 &minus; 0)/(200 &minus; 0) &times; 100 = 37.5 %. I = 4 + 0.16 &times; 75 = 4 + 12 = 16? No: 16 mA per 200 &deg;C &rArr; 16 &times; 0.375 = 6; I = 4 + 6 = 10 mA. Reverse: &theta; = (13.6 &minus; 4)/16 &times; 200 = 120 &deg;C. <span class="hl">75 &deg;C &rArr; 10 mA; 13.6 mA &rArr; 120 &deg;C.</span></p>
<h2><span class="no">8</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Define error in a feedback loop.</span><br><span class="o">A.</span> The algebraic difference between set point and process variable; conventionally e = SP &minus; PV so positive error calls for more output in heating/flow loops.</p>
<p class="q"><span class="b">Q2. Differentiate range and span.</span><br><span class="o">A.</span> Range is the complete set of values the instrument measures; span is URV minus LRV &mdash; e.g. range 0&ndash;200 &deg;C has span 200 &deg;C, but a range &minus;50 to +150 also has span 200.</p>
<h2><span class="no">9</span>Summary</h2>

<p class="q">Error, range, span, proportional band, cycling and control time are the quantities used to describe loop performance in words and numbers. Percentage definitions must always name their denominator (span or reading), 4&ndash;20 mA scaling converts engineering values linearly, and cycling amplitude plus period provides the first diagnostic fingerprint when a loop misbehaves.</p>
<h2><span class="no">10</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Definition</th><th>Typical note</th></tr>
<tr><td>Error e</td><td>SP &minus; PV (or opposite &mdash; fix convention)</td><td>Sign sets action direction</td></tr>
<tr><td>Range</td><td>Min to max measurable</td><td>0&ndash;200 &deg;C, &minus;1 to 1 bar...</td></tr>
<tr><td>Span</td><td>URV &minus; LRV</td><td>Denominator of % span error</td></tr>
</table></div>
"""


# ====================================================================== #
# 25 : Discontinuous controller modes
# ====================================================================== #
B[24] = """
<h2><span class="no">1</span>What are controller modes?</h2>
<p class="q">The <span class="b">mode of a controller</span> is the way in which the controller output changes
in response to the error. The modes are of two broad classes:</p>
<ul class="dot">
  <li><span class="b">Discontinuous (discrete) modes</span> &mdash; the output can take only a few discrete
      values, normally ON or OFF. Two position and multi position modes belong to this class.</li>
  <li><span class="b">Continuous (analog) modes</span> &mdash; the output can take any value within its
      range and varies continuously with the error. P, I, D, PI, PD and PID belong to this class.</li>
</ul>

<h2><span class="no">2</span>Two position (ON-OFF / bang-bang) mode</h2>
<div class="def"><span class="cap">Definition</span>
In the <b>two position mode</b> the controller output has only <b>two states</b> &mdash; fully ON (100 %) or
fully OFF (0 %). The output switches from one state to the other when the error changes sign.</div>
<div class="formula">If e &gt; 0 &rarr; output = 100 % (ON) &nbsp;&nbsp;&nbsp; If e &lt; 0 &rarr; output = 0 %
(OFF)</div>
<p class="q">If the switching happens exactly at the set point, the output will chatter rapidly because of
the noise and small variations. To avoid this, a <span class="b">differential gap (dead band or
hysteresis)</span> is introduced: the output switches ON at a lower limit and OFF at an upper limit. The
process variable therefore <span class="b">oscillates continuously</span> between the two limits &mdash; this
oscillation is called <span class="b">cycling</span> and cannot be eliminated in two position control.</p>
""" + figures_core.render("25.1") + """
<div class="tw"><table>
<tr><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>Very simple and cheap (relay, thermostat)</td><td>Continuous cycling around the set point</td></tr>
<tr><td>Easy to understand and maintain</td><td>Wear and tear of the contacts and the final element</td></tr>
<tr><td>No tuning required</td><td>Not suitable for processes with large lag</td></tr>
<tr><td>Sufficient where wide tolerance is acceptable</td><td>Cannot give accurate control</td></tr>
</table></div>
<p class="q"><span class="g">Applications:</span> Domestic refrigerator and air conditioner thermostat, room
heater, geyser, water tank pump ON/OFF by float switch, oven thermostat, iron box, soldering station.</p>

<h2><span class="no">3</span>Multi position mode</h2>
<div class="def"><span class="cap">Definition</span>
In the <b>multi position mode</b> the controller output can take <b>more than two (but a finite number of)
discrete values</b>, for example 0 %, 25 %, 50 %, 75 % and 100 %. The output changes in steps as the error
increases.</div>
<p class="q">It is an improvement over the two position mode. Because the output is not always fully ON, the
process is not driven so hard and the <span class="b">amplitude of cycling is much reduced</span>. As the
number of positions increases, the response comes closer to proportional control; in the limit, when the
number of positions becomes infinite, the multi position mode becomes a proportional mode.</p>
""" + figures_core.render("25.2") + """
<ul class="arr">
  <li>Used where a single valve has several fixed positions or where several valves or heaters are switched
      in steps (for example 4 heaters of 25 % each).</li>
  <li>Multi stage air conditioners and multi speed fan controllers.</li>
  <li>Stepper motor based valve positioning.</li>
  <li>Batch heating where different power levels are needed at different stages.</li>
</ul>
<div class="tw"><table>
<tr><th>Basis</th><th>Two position mode</th><th>Multi position mode</th></tr>
<tr><td>Output states</td><td>Two (ON / OFF)</td><td>More than two, finite</td></tr>
<tr><td>Cycling amplitude</td><td>Large</td><td>Smaller</td></tr>
<tr><td>Accuracy</td><td>Poor</td><td>Better</td></tr>
<tr><td>Cost and complexity</td><td>Lowest</td><td>Moderate</td></tr>
<tr><td>Example</td><td>Thermostat, float switch</td><td>Stepped heater controller, multi speed fan</td></tr>
</table></div>
<div class="tip"><span class="cap">When to use discontinuous modes?</span>
When the process is <b>slow</b>, the tolerance is <b>wide</b>, the cost must be <b>low</b> and the final
control element can work only in ON/OFF fashion (relay, solenoid valve, contactor).</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">4</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A heater thermostat switches ON at 48 &deg;C and OFF at 52 &deg;C. Find the differential gap, average temperature bias if the process ramps linearly between extremes, and the cycle energy implication for a 3 kW heater with 5 min on / 15 min off.</div>
<p class="q"><span class="b">Solution.</span> Differential gap = 52 &minus; 48 = 4 &deg;C (&plusmn;2 &deg;C around 50 &deg;C). Set point usually marked at midpoint 50 &deg;C; mean follows mid-gap. Duty = 5/(5+15) = 25 %; average heating power = 3 &times; 0.25 = 750 W. <span class="hl">Gap = 4 &deg;C; average power = 750 W at 25 % duty.</span></p>
<h2><span class="no">5</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. What is differential gap?</span><br><span class="o">A.</span> The difference between the switch-on and switch-off values of a two-position controller; it prevents excessively rapid cycling.</p>
<p class="q"><span class="b">Q2. Why is a two-position loop always oscillatory?</span><br><span class="o">A.</span> The output can only be fully on or off, so the process variable must swing between the two trip points; true steady state is impossible.</p>
<p class="q"><span class="b">Q3. How is set point related to the switch points?</span><br><span class="o">A.</span> It is normally the mid-gap value; switching occurs symmetrically above and below it unless the scheme is offset for load reasons.</p>
<p class="q"><span class="b">Q4. Where is two-position control still preferred today?</span><br><span class="o">A.</span> Domestic heating and refrigeration, small ovens, air compressors and any place where a proportional loop would be uneconomic.</p>
<p class="q"><span class="b">Q5. What is the risk of too small a differential gap?</span><br><span class="o">A.</span> Rapid cycling that burns out contactors, contactors and motors, and wears mechanical elements &mdash; the classic short-cycle failure.</p>
<p class="q"><span class="b">Q6. How does three-position control differ?</span><br><span class="o">A.</span> It adds a neutral middle state with drive in either direction, approximating proportional action with two thresholds.</p>
<h2><span class="no">6</span>Summary</h2>

<p class="q">Discontinuous control switches output between fixed states: two-position with a differential gap for simple regulation, multi-position for graduated response. The differential gap sets the amplitude of the unavoidable oscillation and protects equipment from short cycling, while the midpoint defines the apparent set point. These loops are cheap, robust and perfectly adequate wherever a few degrees or a few percent of swing is acceptable.</p>
<h2><span class="no">7</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Parameter</th><th>Typical ON-OFF setting</th><th>Remark</th></tr>
<tr><td>Set point</td><td>Mid-gap value</td><td>Marked on dial or HMI</td></tr>
<tr><td>Differential gap</td><td>1&ndash;10 &deg;C or 2&ndash;10 % span</td><td>Equipment protection + stability</td></tr>
<tr><td>Output</td><td>Discrete: energised / de-energised</td><td>Relay, contactor, SSR</td></tr>
<tr><td>Cycle period</td><td>Minutes (process dependent)</td><td>Too short = wear</td></tr>
<tr><td>Oscillation amplitude</td><td>&asymp; differential gap</td><td>Inherent, cannot be tuned away</td></tr>
<tr><td>Minimum off time</td><td>Compressor/driver protection</td><td>3&ndash;5 min typical for refrigeration</td></tr>
<tr><td>Multi-position band</td><td>&plusmn; dead zone + 2 drive states</td><td>Damper and heater banks</td></tr>
</table></div>
"""


# ====================================================================== #
# 26 : Continuous controller modes (P, I, D)
# ====================================================================== #
B[25] = """
<h2><span class="no">1</span>Introduction</h2>
<p class="q">In <span class="b">continuous controller modes</span> the output of the controller can take
<span class="hl">any value</span> within its range (0 to 100 %) and it changes continuously in proportion to
the error. These modes are used where accurate and smooth control is needed. There are three basic modes
&mdash; <span class="r">proportional (P)</span>, <span class="r">integral (I)</span> and
<span class="r">derivative (D)</span> &mdash; which are combined to give PI, PD and PID modes.</p>
<div class="formula">General controller equation : &nbsp; m(t) = K<sub>p</sub> e(t) +
(K<sub>p</sub>/T<sub>i</sub>) &int; e dt + K<sub>p</sub> T<sub>d</sub> (de/dt) + m<sub>0</sub></div>

<h2><span class="no">2</span>Proportional control mode (P)</h2>
<div class="def"><span class="cap">Definition</span>
In proportional mode the <b>controller output is directly proportional to the error</b> at every instant.<br>
<b>m = K<sub>p</sub> e + m<sub>0</sub></b> where K<sub>p</sub> is the proportional gain and m<sub>0</sub> is
the output when the error is zero (bias).</div>
<p class="q">The proportional band (PB) is the change of error needed to drive the output through its full
range: PB = 100 / K<sub>p</sub>. A large K<sub>p</sub> (narrow PB) gives a fast response but a large risk of
oscillation; a small K<sub>p</sub> (wide PB) gives a slow but stable response.</p>
<p class="q"><span class="b">The main drawback is OFFSET.</span> Suppose the load on the process increases.
The PV falls, an error is produced and the controller increases the output. But for the output to stay
increased, the error must remain &mdash; so the PV settles at a value <span class="hl">slightly below the set
point</span>. This permanent difference between the SP and the PV is called
<span class="b">offset or residual error</span>. Proportional control can never remove the offset; it only
reduces it when K<sub>p</sub> is increased.</p>
""" + figures_core.render("26.1") + """
<div class="tw"><table>
<tr><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>Simple, fast response to error</td><td>Offset (steady state error) always remains</td></tr>
<tr><td>Stable and easy to tune</td><td>Large K<sub>p</sub> causes oscillation</td></tr>
<tr><td>Good for load changes that are not frequent</td><td>Cannot track a changing set point without error</td></tr>
</table></div>
<p class="q"><span class="g">Application:</span> Level control of a tank (a small offset is acceptable),
pressure control, flow control where fast response is more important than zero error.</p>

<h2><span class="no">3</span>Integral control mode (I)</h2>
<div class="def"><span class="cap">Definition</span>
In integral mode the <b>controller output is proportional to the integral (sum) of the error with respect to
time</b>.<br>
<b>m = K<sub>i</sub> &int; e dt + m<sub>0</sub></b></div>
<p class="q">This means the output keeps changing as long as any error exists. Even a very small error, if
it persists, will slowly build up the output until the error becomes zero. Therefore
<span class="hl">integral action eliminates the offset completely</span>. Integral action is also called
<span class="b">reset action</span> and is expressed as <span class="b">repeats per minute</span> or as the
integral time T<sub>i</sub>.</p>
<p class="q"><span class="g">Drawbacks:</span> (1) It is <span class="b">slow</span> &mdash; it cannot give
an immediate response to a sudden error. (2) It produces <span class="b">overshoot and oscillation</span>
because the accumulated action takes time to come down. (3) If the actuator saturates, the integral term
keeps increasing &mdash; this is the well known <span class="b">integral wind-up</span>, which is prevented
by anti-windup circuits. Integral action is therefore <span class="b">never used alone</span>.</p>

<h2><span class="no">4</span>Derivative control mode (D)</h2>
<div class="def"><span class="cap">Definition</span>
In derivative mode the <b>controller output is proportional to the rate of change of the error</b>.<br>
<b>m = K<sub>d</sub> (de/dt) + m<sub>0</sub></b></div>
<p class="q">Derivative action looks at <span class="b">how fast</span> the error is changing and
<span class="hl">anticipates</span> the future error. If the PV is approaching the set point very fast, the
derivative action reduces the output in advance and thereby <span class="b">reduces the overshoot</span> and
improves the stability. Derivative action is also called <span class="b">rate action</span>.</p>
<p class="q"><span class="g">Drawbacks:</span> (1) For a <span class="b">constant error</span> the rate of
change is zero, so the derivative output is zero &mdash; it cannot remove the offset. (2) It
<span class="b">amplifies noise</span>, so it is not used in fast and noisy loops such as flow control.
(3) A sudden step change of set point gives a very large derivative kick. Therefore derivative action is
always used together with proportional action.</p>
""" + figures_core.render("26.2") + """
<div class="tw"><table>
<tr><th>Mode</th><th>Output depends on</th><th>Main advantage</th><th>Main drawback</th><th>Used for</th></tr>
<tr><td><b>P</b></td><td>Size of the error</td><td>Fast response</td><td>Offset remains</td><td>Level, pressure,
flow</td></tr>
<tr><td><b>I</b></td><td>Sum (duration) of the error</td><td>Removes offset</td><td>Slow, overshoot,
wind-up</td><td>Combined with P</td></tr>
<tr><td><b>D</b></td><td>Rate of change of the error</td><td>Reduces overshoot, adds stability</td>
<td>No action for constant error, amplifies noise</td><td>Temperature, slow processes</td></tr>
</table></div>
<div class="tip"><span class="cap">Remember in one line</span>
<b>P</b> looks at the <b>present</b> error, <b>I</b> looks at the <b>past</b> (accumulated) error, and
<b>D</b> looks at the <b>future</b> (predicted) error.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">5</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A PID controller has K<sub>c</sub> = 2.0 %/%, T<sub>i</sub> = 0.5 min, T<sub>d</sub> = 0.1 min. At one instant e = 3 %, de/dt = 5 %/min and &int;e dt = 6 %&middot;min. Find controller output.</div>
<p class="q"><span class="b">Solution.</span> P term = K<sub>c</sub> e = 2.0 &times; 3 = 6 %. I term = K<sub>c</sub> (&int;e dt)/T<sub>i</sub> = 2.0 &times; 6/0.5 = 24 %. D term = K<sub>c</sub> T<sub>d</sub> de/dt = 2.0 &times; 0.1 &times; 5 = 1 %. u = 6 + 24 + 1 = 31 % (plus bias if used). <span class="hl">u = 31 %.</span></p>
<h2><span class="no">6</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Why does proportional-only control leave an offset?</span><br><span class="o">A.</span> Output must change to correct error, but a changed output requires some persistent error to sustain it &mdash; so error never reaches zero.</p>
<p class="q"><span class="b">Q2. What does integral action do to stability?</span><br><span class="o">A.</span> It adds phase lag and can cause slow hunting if too fast; its benefit is eliminating offset and rejecting steady load changes.</p>
<h2><span class="no">7</span>Summary</h2>

<p class="q">Continuous controller modes provide proportional action for immediate response, integral action for offset-free accuracy, and derivative action for damping. Gain and proportional band are reciprocal views of P strength; reset rate and T<sub>i</sub> set how fast offset vanishes; rate and T<sub>d</sub> set how much the controller anticipates.</p>
<h2><span class="no">8</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Mode</th><th>Tuning parameter</th><th>Main effect</th><th>Main risk</th></tr>
<tr><td>Proportional</td><td>K<sub>c</sub> or PB</td><td>Speed of immediate correction</td><td>Offset if too small, oscillation if too big</td></tr>
<tr><td>Integral</td><td>T<sub>i</sub> or repeats/min</td><td>Removes offset, rejects load change</td><td>Windup, slow oscillation</td></tr>
<tr><td>Derivative</td><td>T<sub>d</sub> or rate</td><td>Damps, reduces overshoot</td><td>Amplifies noise</td></tr>
</table></div>
"""


# ====================================================================== #
# 27 : Composite modes - PI, PD, PID
# ====================================================================== #
B[26] = """
<h2><span class="no">1</span>Why composite modes?</h2>
<p class="q">Each basic mode has one strong point and one weakness. P is fast but leaves an offset, I removes
the offset but is slow and overshoots, D improves the stability but does nothing for a constant error.
By <span class="b">combining</span> them we get a controller which has the good points of all three. These
combinations are called <span class="b">composite modes</span>.</p>

<h2><span class="no">2</span>Proportional-Integral (PI) control</h2>
<div class="formula">m = K<sub>p</sub> [ e + (1/T<sub>i</sub>) &int; e dt ] + m<sub>0</sub></div>
<p class="q"><span class="g">Working:</span> The proportional part gives an <span class="b">immediate</span>
response to the error and the integral part slowly builds up additional output until the error becomes zero.
So PI control gives a <span class="b">fast response and zero offset</span>. It is the
<span class="hl">most widely used controller mode</span> in industry (about 75 % of the loops).</p>
<p class="q"><span class="g">Effect of tuning:</span> Increasing K<sub>p</sub> makes the response faster but
increases the overshoot. Decreasing T<sub>i</sub> (stronger integral action) removes the offset faster but
can cause oscillation and wind-up. PI control is used where the process lag is small and offset is not
acceptable &mdash; <span class="b">flow control and level control</span> are the classic examples.</p>

<h2><span class="no">3</span>Proportional-Derivative (PD) control</h2>
<div class="formula">m = K<sub>p</sub> [ e + T<sub>d</sub> (de/dt) ] + m<sub>0</sub></div>
<p class="q"><span class="g">Working:</span> The proportional part responds to the present error and the
derivative part adds an output proportional to the rate at which the error is changing. This
<span class="b">anticipatory action</span> applies the brake in advance, so the
<span class="b">overshoot is reduced, the response is faster and the stability margin increases</span>.
It is very useful in processes with a <span class="b">large lag or a large time constant</span>.</p>
<p class="q"><span class="g">Limitation:</span> PD control still <span class="b">cannot remove the
offset</span> because there is no integral term. It also amplifies noise, so the measured signal must be
filtered. PD control is used in <span class="b">position control of servos, robotics and temperature
control</span> where a small offset is acceptable.</p>

<h2><span class="no">4</span>Proportional-Integral-Derivative (PID) control</h2>
<div class="def"><span class="cap">Definition</span>
A <b>PID controller</b> is a continuous controller whose output is the sum of three terms &mdash;
<b>proportional to the error, proportional to the integral of the error and proportional to the derivative of
the error</b>. It is the most complete and most used controller in process industry.</div>
<div class="formula">m(t) = K<sub>p</sub> [ e(t) + (1/T<sub>i</sub>) &int;<sub>0</sub><sup>t</sup> e dt +
T<sub>d</sub> (de/dt) ] + m<sub>0</sub></div>
""" + figures_core.render("27.1") + """
<h3>4.1 Working of PID control</h3>
<p class="q">When a disturbance occurs, the error appears. The <span class="b">P term</span> immediately
changes the output in proportion to the size of the error. If the error persists, the
<span class="b">I term</span> keeps adding to the output until the error is driven to zero, thus removing the
offset. If the PV starts moving towards the set point too fast, the <span class="b">D term</span> opposes the
output and prevents the overshoot. The three actions together give a response which is
<span class="hl">fast, accurate and stable</span>.</p>
""" + figures_core.render("27.2") + """
<h3>4.2 Comparison of all composite modes</h3>
<div class="tw"><table>
<tr><th>Mode</th><th>Equation</th><th>Offset</th><th>Overshoot</th><th>Response</th><th>Typical use</th></tr>
<tr><td><b>P</b></td><td>K<sub>p</sub> e</td><td>Yes</td><td>Small</td><td>Fast</td><td>Level, pressure, flow
(offset acceptable)</td></tr>
<tr><td><b>PI</b></td><td>K<sub>p</sub> e + K<sub>i</sub>&int;e</td><td>No</td><td>Moderate</td><td>Moderate</td>
<td>Flow, level, pressure (75 % of loops)</td></tr>
<tr><td><b>PD</b></td><td>K<sub>p</sub> e + K<sub>d</sub> de/dt</td><td>Yes</td><td>Very small</td><td>Fast</td>
<td>Servo position, robotics, temperature</td></tr>
<tr><td><b>PID</b></td><td>K<sub>p</sub> e + K<sub>i</sub>&int;e + K<sub>d</sub> de/dt</td><td>No</td>
<td>Small</td><td>Fastest</td><td>Temperature, composition, pH &mdash; where accuracy is critical</td></tr>
</table></div>
<h3>4.3 Tuning of a PID controller</h3>
<p class="q">Tuning means selecting the three constants K<sub>p</sub>, T<sub>i</sub> and T<sub>d</sub> so that
the loop is fast, stable and accurate. Common methods are:</p>
<ul class="dot">
  <li><span class="b">Trial and error</span> &mdash; start with I and D off, increase K<sub>p</sub> till
      slight oscillation, then add integral to remove the offset, and finally add a little derivative to
      reduce the overshoot.</li>
  <li><span class="b">Ziegler-Nichols (ultimate gain) method</span> &mdash; with only P action, increase
      K<sub>p</sub> until sustained oscillation occurs. Note the ultimate gain K<sub>u</sub> and the ultimate
      period T<sub>u</sub>. Then use the table below.</li>
  <li><span class="b">Process reaction curve (step test) method</span> &mdash; find the dead time L and the
      time constant &tau; from the open loop response and calculate the settings.</li>
  <li><span class="b">Auto-tuning</span> &mdash; modern digital controllers and PLCs do this automatically.</li>
</ul>
<div class="tw"><table>
<tr><th>Controller</th><th>K<sub>p</sub></th><th>T<sub>i</sub> (integral time)</th><th>T<sub>d</sub> (derivative
time)</th></tr>
<tr><td>P</td><td>0.50 K<sub>u</sub></td><td>&mdash;</td><td>&mdash;</td></tr>
<tr><td>PI</td><td>0.45 K<sub>u</sub></td><td>T<sub>u</sub> / 1.2</td><td>&mdash;</td></tr>
<tr><td>PID</td><td>0.60 K<sub>u</sub></td><td>T<sub>u</sub> / 2</td><td>T<sub>u</sub> / 8</td></tr>
</table></div>
<h2><span class="no">5</span>Applications</h2>
<ul class="arr">
  <li><span class="b">PI</span> &mdash; flow and level control loops in every plant.</li>
  <li><span class="b">PD</span> &mdash; position control of servo and stepper drives, drone stabilisation.</li>
  <li><span class="b">PID</span> &mdash; temperature of a furnace or reactor, pH control, pressure of a
      boiler, speed of a DC drive, altitude hold of a drone, 3D printer hot end.</li>
  <li>Digital PID is available in every <b>PLC, DCS, SCADA and even in Arduino libraries</b>
      (PID_v1 library).</li>
</ul>
<div class="tip"><span class="cap">Final exam line</span>
<b>P</b> gives speed, <b>I</b> gives accuracy and <b>D</b> gives stability. A
<b>PID controller</b> therefore gives all three together and is the standard controller of the process
industry.</div>
""" + """
<!--EXTRAS-->
<h2><span class="no">6</span>Worked numericals</h2>

<div class="formula"><span class="b">Problem 1.</span> A loop oscillates with period P<sub>u</sub> = 40 s at K<sub>u</sub> = 6 (ultimate gain). Find P, PI and PID settings.</div>
<p class="q"><span class="b">Solution.</span> P-only: K<sub>c</sub> = K<sub>u</sub>/2 = 3. PI: K<sub>c</sub> = 0.45 K<sub>u</sub> = 2.7, T<sub>i</sub> = P<sub>u</sub>/1.2 = 33.3 s. PID: K<sub>c</sub> = 0.6 K<sub>u</sub> = 3.6, T<sub>i</sub> = P<sub>u</sub>/2 = 20 s, T<sub>d</sub> = P<sub>u</sub>/8 = 5 s. <span class="hl">P: 3; PI: 2.7, 33 s; PID: 3.6, T<sub>i</sub> 20 s, T<sub>d</sub> 5 s.</span></p>
<h2><span class="no">7</span>Viva questions and answers</h2>

<p class="q"><span class="b">Q1. Why prefer PI over P for most process loops?</span><br><span class="o">A.</span> Integral eliminates the offset of P-only action so the process lands on set point after load changes.</p>
<p class="q"><span class="b">Q2. When would you choose PD instead of PID?</span><br><span class="o">A.</span> When integral is unnecessary or risky (windup) but damping is needed &mdash; fast position and pressure loops.</p>
<h2><span class="no">8</span>Summary</h2>

<p class="q">PI, PD and PID combine the three continuous actions to give offset-free, well-damped control of real processes. </p>
<h2><span class="no">9</span>Specifications at a glance</h2>

<div class="tw"><table>
<tr><th>Mode</th><th>Best suited to</th><th>Typical T<sub>i</sub></th><th>Typical T<sub>d</sub></th></tr>
<tr><td>PI</td><td>Most process loops: flow, level, pressure, temperature</td><td>0.2&ndash;5 min</td><td>&mdash;</td></tr>
<tr><td>PID</td><td>Large lag, moderate dead time (temp, batch)</td><td>0.5&ndash;3 &times; &theta; or P<sub>u</sub>/2</td><td>P<sub>u</sub>/8 or &theta;/4</td></tr>
</table></div>
"""


for i, body in B.items():
    save(i, body)
print("done part B")
