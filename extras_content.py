# -*- coding: utf-8 -*-
"""Per-topic study extras: worked numericals, viva Q&A, summary, specs table.
Indexed by global topic number (1-27). HTML fragments only — no <h2> numbers;
apply_extras.py numbers and splices them into build_a/build_b."""

EXTRAS = {}

# ------------------------------------------------------------------ 1
EXTRAS[1] = dict(
    prose=[
        "A student often asks which sensor to choose for a job. The answer lies in "
        "asking four questions in order: what quantity must be measured, what is the "
        "smallest and largest value it will take, how much error the application can "
        "tolerate, and in what form the reading must reach the controller. Writing "
        "these four answers on paper first saves a lot of later trouble, because many "
        "sensor problems in industry are actually selection mistakes rather than "
        "failures of the device itself.",
        "It is equally important to remember that a sensor never works alone. It sits "
        "inside a chain of signal-conditioning hardware &mdash; amplifiers, filters, "
        "converters &mdash; and every link in that chain adds a little error of its own. "
        "When a reading looks wrong, a good engineer checks the whole chain from the "
        "sensing tip to the display, one block at a time, instead of blaming the sensor "
        "immediately. This habit of walking the signal path is the practical side of "
        "the block diagram studied in this topic.",
    ],
    num=[
        dict(given="An ammeter has a range of 0&ndash;10 A and is marked accuracy class 0.5. "
                   "Find the limiting error when it reads 6 A.",
             steps=["Maximum permissible error = 0.5 % of full scale = 0.5 &times; 10 / 100 = 0.05 A.",
                    "So the true value lies between 6.00 &minus; 0.05 = 5.95 A and 6.00 + 0.05 = 6.05 A.",
                    "Percentage error at this reading = 0.05 / 6.00 &times; 100 = 0.83 %."],
             ans="Error = &plusmn;0.05 A (0.83 % at the 6 A reading)."),
        dict(given="A pressure sensor has a range of 0&ndash;10 bar and a guaranteed "
                   "uncertainty of &plusmn;0.1 bar. Express this as a percentage of span, "
                   "and find the reading if the output is 6.2 bar.",
             steps=["% of span = 0.1 / (10 &minus; 0) &times; 100 = 1 % of span.",
                    "Reported value = 6.2 bar with uncertainty &plusmn;0.1 bar.",
                    "As a fraction of reading the error is 0.1 / 6.2 = 1.61 %."],
             ans="Uncertainty = &plusmn;1 % of span (&plusmn;0.1 bar)."),
    ],
    viva=[
        ("What is the difference between a sensor and a transducer?",
         "A sensor directly senses the physical quantity; a transducer converts one "
         "form of energy into another. Many books use the two words loosely, but every "
         "transducer that also senses is treated as a sensor."),
        ("Why is a transmitter used ahead of a controller?",
         "To convert the weak sensor signal into a standard, noise-resistant signal such "
         "as 4&ndash;20 mA or 1&ndash;5 V so it can travel long cable lengths without loss."),
        ("Define span of an instrument.",
         "Span is the difference between the maximum and minimum values it can measure: "
         "span = upper range value &minus; lower range value."),
        ("What is static error?",
         "The difference between the measured value and the true value when both are "
         "steady, usually expressed in percent of full scale or percent of reading."),
        ("Name the two main groups of sensors on the basis of energy.",
         "Active (self-generating, e.g. thermocouple, piezoelectric) and passive "
         "(needs an external supply, e.g. RTD, strain gauge, LDR)."),
        ("What is the purpose of calibration?",
         "To compare the instrument against a known standard and adjust or record the "
         "correction so that future readings are traceable and accurate."),
    ],
    summ="In this topic we built the foundation for the whole subject: a sensor is the "
         "measuring eye of an automatic system, the measurement chain adds error block "
         "by block, and instruments are specified by range, span, accuracy class and "
         "uncertainty. Choosing a sensor is a four-question exercise &mdash; quantity, "
         "range, tolerance and output form &mdash; and every later topic on temperature, "
         "pressure, flow or control simply applies this same framework to one physical "
         "quantity at a time.",
    spec=[
        ("Parameter", "Typical specification", "Meaning"),
        ("Input range", "0&ndash;100 of the measured quantity", "Safe measurable span"),
        ("Span", "URV &minus; LRV", "Denominator of all % errors"),
        ("Accuracy class", "0.1, 0.2, 0.5, 1.0, 1.5, 2.5", "Max error as % of full scale"),
        ("Uncertainty", "&plusmn;0.5 % of span", "Guaranteed error band"),
        ("Output signal", "4&ndash;20 mA, 0&ndash;5 V, digital", "What the controller receives"),
        ("Response time", "ms to s (sensor dependent)", "How fast the output follows a change"),
        ("Operating temperature", "&minus;20 to +80 &deg;C (typ.)", "Environment limits"),
    ],
)

# ------------------------------------------------------------------ 2
EXTRAS[2] = dict(
    prose=[
        "While choosing between a thermistor and an RTD or thermocouple, remember the "
        "trade-off. A thermistor gives a very large change of resistance for a small "
        "change of temperature, so the measuring circuit is cheap and sensitive, but its "
        "range is short and its curve is not straight. An RTD is almost linear and very "
        "stable, yet needs more elaborate circuitry. The LM35 solves a different problem "
        "altogether: it already contains the conditioning inside the chip, so a beginner "
        "can read temperature in volts directly on a meter.",
        "Self-heating is a practical pitfall worth understanding. Current flowing "
        "through any resistance raises its temperature slightly above the true process "
        "temperature. In a thermistor bridge the measuring current is therefore kept "
        "small, and in continuous monitoring the duty cycle of the supply is reduced. "
        "A reading that drifts upward a few degrees after power-on, with no real "
        "temperature change, is often self-heating rather than a faulty sensor.",
    ],
    num=[
        dict(given="An NTC thermistor has &beta; = 4000 K and R = 10 k&Omega; at "
                   "T<sub>0</sub> = 298 K (25 &deg;C). Find its resistance at "
                   "T = 308 K (35 &deg;C).",
             steps=["R<sub>T</sub> = R<sub>0</sub> &middot; e<sup>&beta;(1/T &minus; 1/T<sub>0</sub>)</sup>",
                    "1/T &minus; 1/T<sub>0</sub> = 1/308 &minus; 1/298 = 3.247&times;10<sup>&minus;3</sup> "
                    "&minus; 3.356&times;10<sup>&minus;3</sup> = &minus;1.088&times;10<sup>&minus;4</sup> K<sup>&minus;1</sup>",
                    "Exponent = 4000 &times; (&minus;1.088&times;10<sup>&minus;4</sup>) = &minus;0.435",
                    "R<sub>T</sub> = 10 &times; e<sup>&minus;0.435</sup> = 10 &times; 0.647 = 6.47 k&Omega;"],
             ans="R<sub>35&deg;C</sub> &asymp; 6.47 k&Omega; (resistance falls as temperature rises)."),
        dict(given="An LM35 is connected to a 10-bit ADC (0&ndash;5 V reference). The "
                   "temperature is 35.6 &deg;C. Find the output voltage and the ADC code.",
             steps=["V<sub>out</sub> = 10 mV/&deg;C &times; 35.6 = 0.356 V.",
                    "ADC code = V<sub>out</sub> / V<sub>ref</sub> &times; 1023 = 0.356 / 5 &times; 1023 = 72.8",
                    "The processor therefore reads a count of about 73 and converts it back "
                    "with &deg;C = count &times; 5000 / 1023 / 10."],
             ans="V<sub>out</sub> = 0.356 V, ADC code &asymp; 73."),
    ],
    viva=[
        ("Why is an NTC called negative temperature coefficient?",
         "Its resistance decreases when temperature increases, unlike a metal RTD which "
         "shows a small positive coefficient."),
        ("Give the LM35 sensitivity and supply range.",
         "Sensitivity is 10 mV/&deg;C (0 V at 0 &deg;C); supply is +4 V to +30 V, "
         "typically +5 V."),
        ("What is the &beta; of a thermistor?",
         "A material constant in kelvin, typically 3000&ndash;5000 K, that sets how steeply "
         "the resistance changes with temperature."),
        ("Why is a thermistor bridge circuit used?",
         "The bridge converts the resistance change into a small voltage change that can "
         "be amplified and filtered before it reaches the ADC."),
        ("What is self-heating error?",
         "The measuring current warms the sensor above the true process temperature; it "
         "is minimised by keeping the current small."),
        ("Why does an RTD need lead compensation?",
         "Lead resistance adds directly to the small RTD resistance and would be read as "
         "temperature; three-wire or four-wire connections cancel it."),
    ],
    summ="Temperature measurement offers three workhorse devices: the thermistor for a "
         "large, cheap, non-linear resistance change over a short range; the RTD for "
         "stable, nearly linear precision; and integrated sensors like the LM35 that "
         "deliver a ready-made 10 mV/&deg;C voltage. Understanding the exponential "
         "&beta; relation, the ADC conversion chain and the self-heating pitfall allows "
         "you to size any temperature channel from sensor tip to controller input.",
    spec=[
        ("Parameter", "NTC thermistor", "LM35"),
        ("Range", "&minus;40 to +125 &deg;C (device dependent)", "+4 to +30 V supply"),
        ("Output", "Resistance (needs bridge)", "10 mV/&deg;C, voltage"),
        ("Typical accuracy", "&plusmn;0.2 to &plusmn;1 &deg;C", "&plusmn;0.5 &deg;C at 25 &deg;C"),
        ("Linearity", "Exponential (&beta; curve)", "Linear by design"),
        ("Response time", "0.5&ndash;5 s in still air", "about 10 s in still air"),
        ("Application", "Inrush limiting, cheap thermometers", "Microcontroller temperature logging"),
    ],
)

# ------------------------------------------------------------------ 3
EXTRAS[3] = dict(
    prose=[
        "The strain gauge is the classic example of a passive sensor whose entire "
        "value lies in a tiny change of resistance &mdash; often less than one ohm out "
        "of a hundred and twenty. Because the signal is so small, every detail of the "
        "installation matters: the gauge must be bonded flat with no air bubbles, the "
        "lead wires must be short or twisted together, and the amplifier must reject "
        "hum that is hundreds of times larger than the signal. This is why strain-gauge "
        "instrumentation spends as much effort on the bridge and amplifier as on the "
        "sensor itself.",
        "Load cells take the same idea and package it into a machined steel or "
        "aluminium body that concentrates the applied force into known points. In "
        "tanks and hoppers, four load cells under the legs are wired in parallel so "
        "that any tilt still gives the same total weight. When a weighing scale reads "
        "the wrong value, technicians first check zero balance, then span calibration "
        "with a known weight, and only then suspect the electronics.",
    ],
    num=[
        dict(given="A strain gauge of 120 &Omega; with gauge factor GF = 2.0 is bonded "
                   "to a beam. The strain is 500 &micro;&epsilon; (500&times;10<sup>&minus;6</sup>). "
                   "Find the change in resistance and the bridge output if the supply is 5 V.",
             steps=["&Delta;R/R = GF &times; &epsilon; = 2.0 &times; 500&times;10<sup>&minus;6</sup> = 1.0&times;10<sup>&minus;3</sup>",
                    "&Delta;R = 120 &times; 10<sup>&minus;3</sup> = 0.12 &Omega;",
                    "For a quarter bridge, V<sub>out</sub> &asymp; (V<sub>s</sub>/4) &times; &Delta;R/R "
                    "= 5/4 &times; 0.001 = 1.25 mV"],
             ans="&Delta;R = 0.12 &Omega;; bridge output &asymp; 1.25 mV."),
        dict(given="A load cell rated 0&ndash;500 kg gives 2 mV/V at full scale with a "
                   "10 V excitation. What output corresponds to 200 kg, and what amplifier "
                   "gain is needed for a 0&ndash;5 V ADC input?",
             steps=["Full-scale output = 2 mV/V &times; 10 V = 20 mV at 500 kg.",
                    "At 200 kg: 20 &times; 200/500 = 8 mV.",
                    "Gain needed = 5 V / 20 mV = 250 to make full scale use the whole ADC."],
             ans="Output = 8 mV; required gain = 250."),
    ],
    viva=[
        ("Define gauge factor.",
         "GF = (&Delta;R/R) / &epsilon;, the fractional resistance change per unit strain; "
         "metal gauges are near 2, semiconductor gauges can exceed 100."),
        ("Why is a Wheatstone bridge used with strain gauges?",
         "The resistance change is tiny; the bridge converts it into a differential "
         "voltage and cancels common effects such as temperature drift."),
        ("What does a quarter, half and full bridge mean?",
         "One, two or four active gauges in the bridge arms; more active arms give more "
         "sensitivity and better temperature compensation."),
        ("How does a load cell actually work?",
         "Applied force strains a calibrated elastic body; bonded gauges read that "
         "strain, which is proportional to force within the elastic limit."),
        ("Why do we need four load cells on a tank?",
         "To support each leg, sum the weights, and remain accurate when the centre of "
         "gravity shifts off centre."),
        ("What is creep in a load cell?",
         "Slow output drift after the load is applied or removed, caused by elastic "
         "after-effects in the body and adhesive."),
    ],
    summ="Stress and strain describe how a material deforms under load, a strain gauge "
         "turns that deformation into a fractional resistance change through the gauge "
         "factor, and a bridge plus amplifier lifts the millivolt signal to a usable "
         "level. Load cells package the same principle into calibrated force bodies used "
         "in weighing systems. The whole chain &mdash; bonded gauge, bridge, amplifier, "
         "calibration weights &mdash; must be treated as one instrument to get trustworthy "
         "force readings.",
    spec=[
        ("Parameter", "Foil strain gauge", "Load cell (0&ndash;500 kg)"),
        ("Nominal resistance", "120 &Omega; or 350 &Omega;", "Bridge inside the package"),
        ("Gauge factor", "about 2 (metal)", "Fixed by factory calibration"),
        ("Sensitivity", "1.25 mV/V (quarter bridge)", "2 mV/V typical"),
        ("Full-scale output", "&mdash; 1.25 to 5 mV at 5 V", "10 mV at 5 V excitation"),
        ("Accuracy", "&plusmn;0.1&ndash;1 % of reading", "&plusmn;0.02&ndash;0.25 % of span"),
        ("Excitation", "1&ndash;10 V DC", "5&ndash;15 V DC"),
        ("Typical use", "Beam deflection, pressure cells", "Scales, hoppers, batching"),
    ],
)

# ------------------------------------------------------------------ 4
EXTRAS[4] = dict(
    prose=[
        "Light sensors split naturally into two families with different strengths. "
        "Photoconductive devices such as the LDR are simple and cheap: light falls on "
        "cadmium sulphide and the resistance drops, which is perfect for dark-detecting "
        "and daylight switching. Photosensitive junction devices such as photodiodes and "
        "phototransistors are faster and more linear, so they suit communication links, "
        "encoder discs and precise lux measurement. Choosing between them is mostly a "
        "question of how fast and how linear the response must be.",
        "A common installation mistake is to ignore the spectrum. A laser pointer, a "
        "fluorescent tube and noon sunlight may carry similar visible brightness, yet "
        "they put energy into very different parts of the spectrum. A silicon photodiode "
        "responds strongly to infrared, while the human eye peaks near green. Sensor "
        "datasheets therefore state spectral response curves, and outdoor measurements "
        "need a filter if the reading must match what a person sees.",
    ],
    num=[
        dict(given="An LDR has 1 k&Omega; in bright light and 200 k&Omega; in darkness. "
                   "It is used with a 10 k&Omega; series resistor across a 5 V supply. Find "
                   "V<sub>out</sub> in both cases (voltage across the LDR).",
             steps=["Bright: V<sub>out</sub> = 5 &times; 1 / (1 + 10) = 0.45 V.",
                    "Dark: V<sub>out</sub> = 5 &times; 200 / (200 + 10) = 4.76 V.",
                    "A comparator with threshold near 2.5 V therefore gives a clean "
                    "light/dark digital output."],
             ans="V<sub>bright</sub> = 0.45 V, V<sub>dark</sub> = 4.76 V."),
        dict(given="A photodiode with responsivity R = 0.55 A/W at 850 nm is illuminated "
                   "with 200 &micro;W of laser power. Find the photocurrent and the voltage "
                   "across a 10 k&Omega; load resistor.",
             steps=["I<sub>ph</sub> = R &times; P = 0.55 &times; 200&times;10<sup>&minus;6</sup> = 110 &micro;A.",
                    "V<sub>out</sub> = I<sub>ph</sub> &times; R<sub>L</sub> = 110&times;10<sup>&minus;6</sup> &times; 10&times;10<sup>3</sup> = 1.1 V",
                    "Response time of a reverse-biased diode is in nanoseconds, much faster "
                    "than an LDR."],
             ans="I<sub>ph</sub> = 110 &micro;A, V<sub>out</sub> = 1.1 V."),
    ],
    viva=[
        ("Why is a photodiode operated in reverse bias?",
         "Reverse bias widens the depletion layer, reduces junction capacitance and makes "
         "the response much faster; photocurrent is then almost linear with light power."),
        ("What is the dark current?",
         "The small current that flows with no light, caused by thermal generation; it "
         "sets the lowest detectable light level."),
        ("Why does an LDR response depend on light history?",
         "CdS has a memory effect &mdash; resistance rises and falls slowly, so it is slow "
         "to recover after bright light, which makes it unsuitable for fast signals."),
        ("How does a phototransistor differ from a photodiode?",
         "Base light current is amplified by the transistor action, giving 100&times; more "
         "sensitivity but slower speed and less linearity."),
        ("Name an application where a photodiode array is used.",
         "Position-sensing, barcode readers, optical encoders and short-range fibre-optic "
         "links."),
        ("What is the photovoltaic mode?",
         "The diode is left unbiased and generates a voltage like a small solar cell; it "
         "is very linear but slower than reverse-biased operation."),
    ],
    summ="Light measurement uses either a photoconductor whose resistance falls with "
         "illumination (LDR) or junction devices that generate a photocurrent "
         "(photodiode, phototransistor). Linearity, speed and spectral response decide "
         "which family fits the job: LDRs for simple switching, photodiodes for fast and "
         "proportional measurement. Dark current, load resistance and bias conditions "
         "together set the smallest light level the circuit can reliably see.",
    spec=[
        ("Parameter", "LDR (CdS)", "Silicon photodiode"),
        ("Dark resistance", "0.2&ndash;2 M&Omega;", "Dark current 1&ndash;20 nA"),
        ("Light resistance", "few k&Omega; at 10 lux", "&mdash; photocurrent instead"),
        ("Response time", "20&ndash;100 ms (slow)", "ns to &micro;s"),
        ("Spectral peak", "about 540 nm", "about 900 nm (near IR)"),
        ("Sensitivity", "resistance vs lux", "0.4&ndash;0.65 A/W"),
        ("Typical use", "Street-light switch, camera exposure", "Encoders, comms, detectors"),
    ],
)

# ------------------------------------------------------------------ 5
EXTRAS[5] = dict(
    prose=[
        "Chemical sensors are unique because their working surface actually takes part "
        "in a chemical interaction. The sensing electrode must be clean, the reference "
        "electrode must remain stable, and the sample must not coat or poison the "
        "membrane. In process lines this practical care is as important as the "
        "electrical design: a pH probe kept dry in its storage solution will last for "
        "years, while the same probe left in air for weeks will drift and fail.",
        "Two conversion principles cover most chemical sensors. Potentiometric sensors "
        "measure a voltage that already exists across a selective membrane, so almost no "
        "current flows and the sensor does not disturb the sample. Amperometric sensors "
        "apply a fixed polarising voltage and read the current that results from the "
        "target species reacting at the electrode; the current is directly proportional "
        "to concentration. Knowing which principle a sensor uses tells you what interface "
        "circuit it needs.",
    ],
    num=[
        dict(given="A pH electrode follows E = E<sub>0</sub> + 0.05916 &times; pH at "
                   "25 &deg;C. A process sample reads pH 7.00 on the reference and pH 10.00 "
                   "on the process side. Find the electrode voltage difference.",
             steps=["&Delta;pH = 10.00 &minus; 7.00 = 3.00 pH units.",
                    "&Delta;E = 0.05916 &times; 3.00 = 0.1775 V = 177.5 mV.",
                    "The sign is negative for rising pH on a standard glass electrode "
                    "(about &minus;59.16 mV per pH unit)."],
             ans="|&Delta;E| = 177.5 mV (&minus;59.16 mV per pH at 25 &deg;C)."),
        dict(given="A dissolved-oxygen probe gives 8.2 &micro;A at saturation (9.2 mg/L) "
                   "and 3.1 &micro;A in the sample. Find the oxygen concentration.",
             steps=["Assume current is linear with concentration: C = C<sub>sat</sub> "
                    "&times; I / I<sub>sat</sub>",
                    "C = 9.2 &times; 3.1 / 8.2 = 3.49 mg/L",
                    "Temperature compensation corrects saturation value if the sample is "
                    "not at the calibration temperature."],
             ans="Dissolved oxygen &asymp; 3.5 mg/L."),
    ],
    viva=[
        ("What is a reference electrode?",
         "A stable electrode of known potential (e.g. Ag/AgCl) that provides a fixed "
         "baseline so the sensing electrode voltage can be interpreted absolutely."),
        ("Why does a pH electrode need a high-impedance amplifier?",
         "Glass electrodes can source almost no current; any load would collapse the "
         "millivolt signal, so input impedance must be 10<sup>12</sup> &Omega; or higher."),
        ("Distinguish potentiometric and amperometric sensors.",
         "Potentiometric measures an open-circuit voltage (no current, logarithmic in "
         "concentration); amperometric measures a current at fixed bias (linear in "
         "concentration)."),
        ("What is the Clark electrode used for?",
         "Measuring dissolved oxygen in water and blood through a membrane-covered "
         "cathode that reduces oxygen and produces a proportional current."),
        ("How do you calibrate a pH sensor?",
         "Two-point buffer calibration, usually pH 4.0 and 7.0 (or 7.0 and 10.0), "
         "setting slope and offset."),
        ("Name one hazard when chemical sensors foul.",
         "Drift and false readings; membranes coated by oil, scale or biological film "
         "stop responding and must be cleaned or replaced."),
    ],
    summ="Chemical sensors convert concentration or activity into an electrical quantity "
         "by one of two routes: a selective membrane that develops a voltage "
         "(potentiometric, e.g. pH electrode) or a controlled reaction that draws a "
         "current (amperometric, e.g. Clark cell). Both need stable references, careful "
         "calibration and clean sensing surfaces. Choosing the right interface circuit "
         "&mdash; high-impedance amplifier for voltage-type sensors, transimpedance "
         "amplifier for current-type sensors &mdash; is half the design job.",
    spec=[
        ("Parameter", "pH (glass electrode)", "Dissolved O&#8322; (Clark)"),
        ("Principle", "Potentiometric", "Amperometric"),
        ("Output", "&plusmn;59 mV per pH at 25 &deg;C", "0&ndash;100 nA / ppm class currents"),
        ("Range", "0&ndash;14 pH", "0&ndash;20 mg/L"),
        ("Accuracy", "&plusmn;0.01&ndash;0.1 pH", "&plusmn;0.1&ndash;0.5 mg/L"),
        ("Response time", "seconds to a minute", "60&ndash;90 s (T<sub>90</sub>)"),
        ("Calibration", "Two buffer points", "Water-saturated air / zero solution"),
        ("Typical use", "Effluent, fermentation, pools", "Aquaculture, boilers, blood gas"),
    ],
)

# ------------------------------------------------------------------ 6
EXTRAS[6] = dict(
    prose=[
        "The MQ-2 is representative of a whole family of tin-dioxide gas sensors that "
        "share the same working idea. Fresh from the factory the sensor needs a burn-in "
        "period of a day or two, during which its baseline settles. Even afterwards the "
        "zero point drifts with humidity and age, so designs that matter re-calibrate "
        "periodically or compare the present resistance with a stored baseline taken "
        "when the air was known to be clean.",
        "Heater management is the key practical point. The sensing layer only works at "
        "its designated temperature; too cold and the reaction is sluggish, too hot and "
        "the sensor ages in hours instead of years. Many boards therefore duty-cycle the "
        "5 V heater to hold temperature while saving power, and the reading is taken only "
        "after the layer has stabilised. Because the device also consumes oxygen from a "
        "sealed space, sensors are rated for open, ventilated locations rather than "
        "inside closed enclosures.",
    ],
    num=[
        dict(given="An MQ-2 is wired with R<sub>L</sub> = 10 k&Omega; across 5 V and "
                   "reads V<sub>out</sub> = 2.0 V in clean air where R<sub>0</sub> gives "
                   "V<sub>out0</sub> = 1.0 V. Find R<sub>s</sub> / R<sub>0</sub>.",
             steps=["Divider: V<sub>out</sub> = V<sub>cc</sub> &times; R<sub>L</sub> / (R<sub>s</sub> + R<sub>L</sub>)",
                    "Clean air: 1.0 = 5 &times; 10 / (R<sub>0</sub> + 10) &rArr; R<sub>0</sub> = 40 k&Omega;",
                    "Gas present: 2.0 = 5 &times; 10 / (R<sub>s</sub> + 10) &rArr; R<sub>s</sub> = 15 k&Omega;",
                    "Ratio R<sub>s</sub>/R<sub>0</sub> = 15/40 = 0.375 &mdash; read it off the "
                    "log-log curve for the gas in question."],
             ans="R<sub>s</sub>/R<sub>0</sub> = 0.375 (concentration comes from the datasheet curve)."),
        dict(given="For the same divider, what R<sub>L</sub> keeps V<sub>out</sub> within "
                   "the 0&ndash;4.9 V ADC range when R<sub>s</sub> varies from 10 k&Omega; to "
                   "500 k&Omega;?",
             steps=["At R<sub>s</sub> = 10 k&Omega;: V = 5 &times; R<sub>L</sub>/(10 + R<sub>L</sub>) &le; 4.9 &rArr; R<sub>L</sub> &ge; 98 k&Omega; approx.",
                    "At R<sub>s</sub> = 500 k&Omega;: V = 5 &times; R<sub>L</sub>/(500 + R<sub>L</sub>) &mdash; larger R<sub>L</sub> keeps it measurable.",
                    "A 100 k&Omega; load is a common compromise between sensitivity and range."],
             ans="R<sub>L</sub> &asymp; 100 k&Omega; suits the full sensor span."),
    ],
    viva=[
        ("What material is the sensing element of MQ-2?",
         "Tin dioxide (SnO&#8322;), an n-type semiconductor whose surface resistance changes "
         "when combustible gases adsorb on it."),
        ("Why is a heater coil inside the can?",
         "The sensing reaction needs a controlled high surface temperature, roughly 200 "
         "to 400 &deg;C, supplied by the internal nichrome heater."),
        ("Does MQ-2 consume oxygen?",
         "Yes &mdash; it needs fresh air reference oxygen at the surface, so it should not "
         "be sealed in a tiny volume without ventilation."),
        ("Is the sensor output linear in gas concentration?",
         "No. The relationship is log-log; the datasheet curve of R<sub>s</sub>/R<sub>0</sub> "
         "against ppm is used, or a microcontroller fits that curve."),
        ("How is selectivity improved in a gas sensor array?",
         "Several sensors with different dopants (Sn, Pd, Al) are combined and their "
         "pattern is classified by a small algorithm."),
        ("What safety rating do LPG sensors often carry?",
         "Many MQ-2 modules are advertised as explosion-proof and flameproof for domestic "
         "LPG leak alarm use, but the module still needs certified installation."),
    ],
    summ="The MQ-2 is a resistive SnO&#8322; gas sensor: combustible gas on the heated "
         "surface changes the semiconductor resistance, and a simple load resistor "
         "converts that change into a voltage the ADC can read. Accurate work depends on "
         "knowing R&#8320; at baseline, following the log-log response curve rather than "
         "assuming linearity, respecting heater temperature and burn-in, and never "
         "trapping the sensor away from fresh air.",
    spec=[
        ("Parameter", "MQ-2 specification", "Remark"),
        ("Detectable gases", "LPG, propane, hydrogen, smoke, alcohol", "Combustible range"),
        ("Supply (heater)", "5 V AC/DC, about 450 mW", "Keep temperature stable"),
        ("Sensor supply", "5 V", "Divider powered from same rail"),
        ("R&#8320; in clean air", "10&ndash;60 k&Omega; (device spread)", "Store this as baseline"),
        ("Sensitivity", "R<sub>s</sub>/R&#8320; &lt; 0.6 at 200 ppm LPG", "From datasheet curve"),
        ("Response / recovery", "about 10 s / 30 s", "T<sub>90</sub> values"),
        ("Pre-heat (burn-in)", "24&ndash;48 h first use", "Then periodic calibration"),
    ],
)

# ------------------------------------------------------------------ 7
EXTRAS[7] = dict(
    prose=[
        "Vibration measurement sits at the boundary between mechanics and electronics, "
        "and the mechanical mounting is where most measurements go wrong. A sensor "
        "bolted through a thin sheet of panel metal reads the panel, not the machine; a "
        "sensor held only by magnet picks up electrical hum; a long cable swinging with "
        "the sensor adds its own motion. For faithful readings the accelerometer must be "
        "rigidly part of the structure it measures, with stiffness far above the "
        "frequencies of interest.",
        "Choosing between a piezoelectric accelerometer and a MEMS device is a question "
        "of frequency and price. Piezo sensors have no electronics inside, survive high "
        "temperatures, and measure engine or bearing frequencies up to several kilohertz. "
        "MEMS devices integrate the amplifier and give you X, Y and Z channels plus "
        "temperature on a digital bus for a fraction of the cost &mdash; ideal for buildings, "
        "appliances and consumer products, but bandwidth-limited compared with piezo "
        "probes.",
    ],
    num=[
        dict(given="A piezoelectric accelerometer has sensitivity 100 pC/g and is "
                   "connected to a charge amplifier with C<sub>f</sub> = 1000 pF. Find the "
                   "amplifier output at 10 g.",
             steps=["Charge Q = 100 pC/g &times; 10 g = 1000 pC.",
                    "V<sub>out</sub> = Q / C<sub>f</sub> = 1000 pC / 1000 pF = 1.0 V.",
                    "Charge amplifiers are preferred because cable capacitance does not "
                    "change the gain."],
             ans="V<sub>out</sub> = 1.0 V."),
        dict(given="An accelerometer with 500 mV/g output is sampled while the machine "
                   "vibrates at 0.4 g. The controller alarms above 1.0 g. Find the ADC "
                   "counts at 0.4 g with a 3.3 V, 12-bit ADC.",
             steps=["V = 0.5 V/g &times; 0.4 g = 0.2 V.",
                    "Counts = 0.2 / 3.3 &times; 4095 = 248.",
                    "Alarm level 1.0 g = 0.5 V &rArr; 620 counts &mdash; threshold can be set "
                    "directly in counts."],
             ans="ADC code &asymp; 248 at 0.4 g."),
    ],
    viva=[
        ("What does an accelerometer actually measure?",
         "It measures the force needed to accelerate its own proof mass; by Newton's law "
         "that force divided by mass equals the vibration acceleration."),
        ("Why do piezo accelerometers need a charge or IEPE amplifier?",
         "The crystal generates charge but almost no current; a charge amplifier or "
         "built-in IEPE conditioning converts it to a usable voltage before the cable."),
        ("What is the resonant frequency of a vibration sensor?",
         "The mounting-structure natural frequency; measurements are only trusted well "
         "below it, usually below one third."),
        ("Why are MEMS accelerometers popular in modern machines?",
         "They are tiny, cheap, low power and put X, Y, Z plus temperature on one digital "
         "interface straight into a microcontroller."),
        ("What is a vibration switch used for?",
         "It gives a simple trip output when vibration crosses a set level &mdash; cheap "
         "protection for pumps, fans and washers without full spectrum analysis."),
        ("How does sampling rate relate to vibration analysis?",
         "The sample rate must be at least twice the highest frequency of interest "
         "(Nyquist); bearing faults often need several kilohertz sampling."),
    ],
    summ="Vibration sensors convert mechanical oscillation into an electrical signal: "
         "piezoelectric accelerometers for wide bandwidth and harsh duty, MEMS devices "
         "for compact three-axis digital sensing, and simple vibration switches for "
         "alarm duty. The sensor output is a charge or voltage proportional to "
         "acceleration, the mounting must be mechanically stiff, and the electronics must "
         "resolve the tiny signals before cable noise takes over.",
    spec=[
        ("Parameter", "Piezo accelerometer", "MEMS (e.g. ADXL335)"),
        ("Principle", "Piezoelectric charge", "Capacitive silicon proof mass"),
        ("Sensitivity", "10&ndash;1000 pC/g", "100&ndash;1000 mV/g (scaled to range)"),
        ("Frequency range", "1 Hz &ndash; 10 kHz+", "DC &ndash; a few hundred Hz"),
        ("Axes", "Single axis", "1, 2 or 3 axes"),
        ("Output", "Charge / IEPE voltage", "Analog or I&#178;C / SPI digital"),
        ("Supply", "2&ndash;20 mA IEPE constant current", "1.7&ndash;3.6 V low voltage"),
        ("Typical use", "Bearing analysis, balancing", "Tilt, impact, appliance monitoring"),
    ],
)

# ------------------------------------------------------------------ 8
EXTRAS[8] = dict(
    prose=[
        "Displacement, force and torque form a closely related family because each can "
        "be traced back to strain in an elastic element. The LVDT measures position "
        "directly with a sliding magnetic coupling and no mechanical wear, the capacitive "
        "sensor measures minute gaps with extreme resolution, and the optical encoder "
        "counts digital steps for shaft position. Underneath force and torque sensors "
        "you will usually find strain gauges again, so the bridge techniques of the "
        "earlier topic reappear here in heavier packaging.",
        "Selection guidelines are worth fixing in memory. Where contact wear must be "
        "zero, choose LVDT or optical. Where sub-micron resolution is required and the "
        "gap can be tightly controlled, choose capacitive. For rotating shaft power "
        "measurements, torque flanges with telemetry beat strain-gauge slip rings for "
        "maintenance. And always match the mechanical stiffness of the sensor to the "
        "structure: a very soft spring-mounted sensor will not follow fast changes, no "
        "matter how good its electronics are.",
    ],
    num=[
        dict(given="An LVDT with sensitivity 40 mV/mm/V has an excitation of 5 V. The "
                   "core moves 3 mm from null. Find the output voltage.",
             steps=["Sensitivity referred to 5 V = 40 &times; 5 = 200 mV/mm.",
                    "V<sub>out</sub> = 200 mV/mm &times; 3 mm = 600 mV (phase indicates direction)."],
             ans="V<sub>out</sub> = 600 mV (0.6 V, sign/phase gives direction)."),
        dict(given="A capacitive gap sensor has C = 100 pF at nominal gap d = 1 mm with "
                   "area A fixed. Find C when the gap changes to 1.05 mm, and the "
                   "fractional change.",
             steps=["C &prop; 1/d, so C' = C &times; d/d' = 100 &times; 1/1.05 = 95.2 pF.",
                    "&Delta;C/C = &minus;&Delta;d/d = &minus;0.05/1 = &minus;0.05 = &minus;5 %.",
                    "Half the fractional gap change appears as output in a simple "
                    "differential arrangement."],
             ans="C' = 95.2 pF, &Delta;C/C = &minus;5 %."),
        dict(given="A torque sensor on a shaft reads 2.5 mV/V output at 10 V excitation "
                   "when 500 Nm is applied, and is rated 0&ndash;1000 Nm. Find output at "
                   "500 Nm and the torque for 20 mV output.",
             steps=["Full scale = 2.5 &times; 10 = 25 mV at 1000 Nm.",
                    "At 500 Nm: 25 &times; 0.5 = 12.5 mV.",
                    "For 20 mV: T = 1000 &times; 20/25 = 800 Nm."],
             ans="12.5 mV at 500 Nm; 20 mV &rArr; 800 Nm."),
    ],
    viva=[
        ("How does an LVDT work?",
         "A movable core changes the mutual inductance of two secondary coils; the "
         "difference of the two secondary voltages is a signed measure of core position."),
        ("Why is there no wear in an LVDT?",
         "The core never touches the coils &mdash; coupling is purely magnetic, so life is "
         "practically unlimited."),
        ("What is the principle of a capacitive displacement sensor?",
         "Capacitance varies inversely with electrode gap; a bridge or C-to-V converter "
         "detects sub-nanometre changes."),
        ("How does an incremental encoder differ from an absolute encoder?",
         "Incremental counts steps from power-on and loses position at power-off; absolute "
         "gives a unique code for every shaft angle at any time."),
        ("Where is torque measured on a rotating shaft?",
         "With strain-gauge torque flanges that transmit data wirelessly, avoiding slip "
         "rings and their maintenance."),
        ("Give two industrial uses of force sensors.",
         "Weighing platforms and material-testing machines (tensile/compression rigs)."),
    ],
    summ="This topic covered the measurement of how far something moves, how hard it is "
         "pushed and how strongly it is twisted. LVDTs, capacitive probes and encoders "
         "cover position and displacement with different resolutions and contact "
         "arrangements, while force and torque almost always rest on strain-gauge bridges "
         "in elastic bodies. All of them must be mounted stiffly enough that the sensor "
         "actually sees the motion or load it is supposed to measure.",
    spec=[
        ("Parameter", "LVDT", "Capacitive probe", "Incremental encoder"),
        ("Measuring principle", "Mutual inductance", "Gap capacitance", "Optical / magnetic slots"),
        ("Resolution", "0.1 &micro;m typical", "0.01 &micro;m possible", "1 pulse (e.g. 1024/rev)"),
        ("Range", "&plusmn;0.5 to &plusmn;500 mm", "0.1&ndash;10 mm gap", "Continuous counting"),
        ("Contact", "Non-contact core", "Non-contact field", "Non-contact light path"),
        ("Output", "Analog AC-bridge or 4&ndash;20 mA", "Capacitance / voltage", "A & B phase pulses"),
        ("Typical use", "Valve position, gauging", "Run-out, film thickness", "Motor speed, CNC axes"),
    ],
)

# ------------------------------------------------------------------ 9
EXTRAS[9] = dict(
    prose=[
        "Pressure is measured in more different ways than almost any other quantity, "
        "which is a hint about the engineering trade-offs involved. The humble Bourdon "
        "tube needs no electricity at all and is still found on every steam line; the "
        "strain-gauge diaphragm gives an electrical signal straight from the process "
        "flange; the piezoresistive silicon chip miniaturises the same idea onto a "
        "MEMS die for automotive and medical work. Choosing among them means weighing "
        "range, media compatibility, overpressure survival and the required output.",
        "Gauge, absolute and differential pressure are three different zero references "
        "and mixing them up is a classic installation error. A gauge-pressure transmitter "
        "vents to atmosphere, so it reads zero when the pipe is at ambient even though "
        "molecules remain inside. An absolute-pressure sensor has a sealed vacuum behind "
        "the diaphragm and never reads zero. Always check which reference the drawing "
        "calls for before commissioning, because a wrong reference shows up as a "
        "constant offset that looks exactly like a calibration fault.",
    ],
    num=[
        dict(given="A diaphragm pressure sensor of area 2 cm&sup2; sees 15 bar gauge. Find "
                   "the force on the diaphragm (1 bar = 10<sup>5</sup> Pa).",
             steps=["A = 2 cm&sup2; = 2 &times; 10<sup>&minus;4</sup> m&sup2;.",
                    "P = 15 bar = 1.5 &times; 10<sup>6</sup> Pa.",
                    "F = P &times; A = 1.5&times;10<sup>6</sup> &times; 2&times;10<sup>&minus;4</sup> = 300 N."],
             ans="F = 300 N on the diaphragm."),
        dict(given="A strain-gauge pressure transmitter is rated 0&ndash;25 bar and gives "
                   "4&ndash;20 mA. Find the current at 10 bar, and the bar reading when the "
                   "current is 13.6 mA.",
             steps=["I = 4 + (20 &minus; 4) &times; (x &minus; 0)/(25 &minus; 0) = 4 + 0.64 x",
                    "At x = 10 bar: I = 4 + 6.4 = 10.4 mA.",
                    "At I = 13.6 mA: x = (13.6 &minus; 4)/0.64 = 15 bar."],
             ans="10 bar &rArr; 10.4 mA; 13.6 mA &rArr; 15 bar."),
        dict(given="A Bourdon tube gauge with an effective length of 80 mm and tip lever "
                   "of 30 mm moves its pointer 270&deg; through a 1:6 gear. Find the tip "
                   "travel.",
             steps=["Pointer 270&deg; on pinion &rArr; pinion = 270/6 = 45&deg; travel need not be used directly.",
                    "Arc at tip lever radius: s = r &theta; = 30 mm &times; 45&deg; &times; &pi;/180 = 23.6 mm.",
                    "This is the small deflection the tube tip must deliver."],
             ans="Tip travel &asymp; 23.6 mm."),
    ],
    viva=[
        ("Distinguish gauge, absolute and differential pressure.",
         "Gauge is referenced to atmosphere, absolute to vacuum, differential is the "
         "difference between two process points (e.g. across an orifice)."),
        ("How does a Bourdon tube work?",
         "A curved hollow tube tends to straighten as internal pressure rises; the tip "
         "motion drives a gear and pointer."),
        ("What is overpressure rating?",
         "The maximum pressure a sensor survives without calibration shift, often 2&ndash;3 "
         "times full scale."),
        ("Why do pressure transmitters show a small static zero error?",
         "Sealed systems, temperature effects on fill fluid, or installing a gauge "
         "reference where absolute was specified."),
        ("What is impulse piping?",
         "The tube that connects the process tap to the transmitter; it must be lagged, "
         "valved and free of trapped gas or liquid that would distort the reading."),
        ("Where are piezoresistive sensors commonly used?",
         "Manifold absolute-pressure (MAP) sensors in engines, tyre-pressure monitors "
         "and medical devices &mdash; where size and cost dominate."),
    ],
    summ="Pressure sensors all measure the force of a fluid on a defined area, but they "
         "differ in the elastic element used &mdash; Bourdon tube, corrugated diaphragm or "
         "silicon bridge &mdash; and in the electrical readout. Range, reference "
         "(gauge/absolute/differential), overpressure margin and 4&ndash;20 mA scaling are "
         "the four decisions that determine whether a pressure installation measures "
         "correctly on day one and keeps measuring after water hammer and blockage events.",
    spec=[
        ("Parameter", "Bourdon gauge", "Strain-gauge transmitter", "Piezoresistive (MEMS)"),
        ("Range", "0&ndash;1000 bar possible", "0&ndash;0.4 to 0&ndash;400 bar", "0&ndash;1 to 0&ndash;35 bar"),
        ("Output", "Pointer angle", "4&ndash;20 mA / 1&ndash;5 V", "mV-level bridge / digital"),
        ("Accuracy", "&plusmn;1 % of span", "&plusmn;0.075&ndash;0.25 % of span", "&plusmn;0.25&ndash;1 % FS"),
        ("Overpressure", "Mechanical stop", "2&times; to 5&times; FS", "1&times; to 3&times; FS"),
        ("Reference", "Gauge", "Gauge / abs / diff", "Gauge or absolute"),
        ("Typical use", "Local indication, steam lines", "Process control loops", "Automotive, tyres, medical"),
    ],
)

# ------------------------------------------------------------------ 10
EXTRAS[10] = dict(
    prose=[
        "Position and motion sensing answer two different factory questions: where is "
        "the part right now, and how fast is it going. Absolute position must survive a "
        "power failure, so absolute encoders, resolvers and potentiometers dominate "
        "that job. Speed can always be recomputed from pulses arriving per second, so "
        "incremental encoders, tachogenerators and Hall sensors cover it cheaply. A "
        "servo axis typically needs both: an incremental channel for velocity inside the "
        "loop and a home switch or multiturn absolute channel for start-up.",
        "Installation details decide whether a position channel stays trustworthy. "
        "Potentiometers wear at the wiper, Hall sensors lose calibration if the magnet "
        "gap changes, and encoder cables running beside motor leads pick up pulses that "
        "the drive counts as phantom motion. Keeping magnets glued with the specified "
        "air gap, wiring encoder cables in screened pairs, and confirming the home "
        "sensor position after every maintenance stop are the small habits that keep "
        "position loops healthy.",
    ],
    num=[
        dict(given="A 10 k&Omega; linear potentiometer of travel 100 mm is fed with 5 V. "
                   "The wiper is at 35 mm from the zero end. Find V<sub>out</sub>.",
             steps=["V<sub>out</sub> = V<sub>in</sub> &times; x/L = 5 &times; 35/100",
                    "V<sub>out</sub> = 1.75 V",
                    "Sensitivity = 5 V / 100 mm = 50 mV per mm."],
             ans="V<sub>out</sub> = 1.75 V."),
        dict(given="A 1024-pulse-per-revolution incremental encoder is read for 0.2 s and "
                   "counts 1200 pulses. Find shaft speed in rpm.",
             steps=["Revolutions = 1200 / 1024 = 1.1719 rev in 0.2 s.",
                    "Speed = 1.1719 / 0.2 = 5.859 rev/s.",
                    "rpm = 5.859 &times; 60 = 351.6 rpm."],
             ans="N &asymp; 352 rpm."),
        dict(given="A Hall sensor closes at B<sub>op</sub> = 35 mT with a magnet that decays "
                   "1.5 % per year. Estimate how many years before a 2 mm gap increase "
                   "causes a miss, given field &prop; 1/r&sup3; from an initial gap of 4 mm.",
             steps=["Field at 4 mm &rarr; 6 mm: ratio = (4/6)&sup3; = 0.296 &mdash; far below any margin.",
                    "In practice a 25 % field margin is designed in, tolerating roughly "
                    "8 % gap growth.",
                    "Gap grows mainly from vibration loosening, not from magnet ageing; "
                    "check torque on brackets during PM."],
             ans="Mechanical gap control matters more than magnet ageing &mdash; verify 4 mm gap in PM."),
    ],
    viva=[
        ("Difference between absolute and incremental encoding?",
         "Absolute encoders report the true angle at every instant, even after power "
         "loss; incremental encoders only count changes and need a reference at start-up."),
        ("What are quadrature signals?",
         "Two pulse channels 90&deg; apart; their phase order reveals direction and "
         "combining edges gives 2&times; or 4&times; resolution."),
        ("How does a tachogenerator measure speed?",
         "It is a small generator whose output voltage is proportional to shaft speed, "
         "giving an immediate analog rpm signal."),
        ("Why use a Hall sensor for speed pickup?",
         "Non-contact, no wear, works through dust and oil where optical slotted wheels "
         "would clog."),
        ("What is homing in motion control?",
         "Moving an axis to a fixed reference switch at start-up to establish the "
         "coordinate origin before absolute work begins."),
        ("Where are resolvers preferred over encoders?",
         "In hot, vibrating environments such as traction motors &mdash; they are rugged "
         "rotating transformers with no optical parts."),
    ],
    summ="Position sensing answers where and speed sensing answers how fast. Potentiometers "
         "give simple absolute voltage, Hall devices give contactless digital edges, and "
         "encoders give high-resolution quadrature counts for servo loops. Correct gaps, "
         "screened cables and a reliable homing procedure are what keep the numbers the "
         "controller sees equal to the real shaft or table position.",
    spec=[
        ("Parameter", "Linear pot", "Incremental encoder", "Hall speed sensor"),
        ("Type", "Absolute analog", "Incremental digital", "Digital pulses"),
        ("Resolution", "Continuous (noise limited)", "e.g. 1024 ppr, 4&times; decode", "1 per tooth"),
        ("Output", "0&ndash;5 V", "A/B/Z TTL or line driver", "Open-collector square wave"),
        ("Speed limit", "Wiper wear limits speed", "Up to MHz class counting", "Depends on gear tooth size"),
        ("Life", "10<sup>6</sup> operations (wear)", "Bearing life (no contact wear)", "Effectively unlimited"),
        ("Typical use", "Valve position, joysticks", "CNC and robot axes", "Wheel speed, crank position"),
    ],
)

# ------------------------------------------------------------------ 11
EXTRAS[11] = dict(
    prose=[
        "Level and flow measurements close the loop between what is stored in a vessel "
        "and what is moving through a pipe, and they are the two quantities most often "
        "billed or accounted for. That commercial importance explains why flow meters "
        "come in so many grades: a bypass rotameter for local indication, a turbine meter "
        "with pulse output for batching, an electromagnetic meter with custody-transfer "
        "accuracy for fiscal accounting. The measurement principle chosen must suit the "
        "fluid &mdash; dirty, corrosive, conducting or not &mdash; not just the pipe size.",
        "Level sensing has its own practical traps. Float switches can hang up on scale, "
        "ultrasonic sensors are confused by heavy foam, and guided-radar probes must be "
        "installed clear of the agitator. A simple rule helps during selection: if the "
        "fluid is clean and the vessel quiet, use float, capacitance or ultrasonic; if it "
        "is viscous or coated, prefer guided radar or a differential-pressure tap; if the "
        "measurement drives custody transfer, calibrate against a strapping table.",
    ],
    num=[
        dict(given="An orifice plate meter is calibrated so that Q = 0.05 &times; "
                   "&radic;&Delta;P with &Delta;P in Pa and Q in m&sup3;/h. Find Q at "
                   "&Delta;P = 400 Pa, and the new &Delta;P if Q doubles.",
             steps=["Q = 0.05 &times; &radic;400 = 0.05 &times; 20 = 1.0 m&sup3;/h.",
                    "Q &prop; &radic;&Delta;P, so doubling Q needs 4&times; &Delta;P.",
                    "New &Delta;P = 400 &times; 4 = 1600 Pa."],
             ans="Q = 1.0 m&sup3;/h at 400 Pa; doubled flow needs 1600 Pa."),
        dict(given="A turbine meter gives 7.5 pulses per litre. The controller counts "
                   "30 000 pulses in a batch. What volume has been delivered, and what "
                   "pulse rate corresponds to 60 L/min?",
             steps=["Volume = 30 000 / 7.5 = 4000 L.",
                    "60 L/min = 1 L/s &rArr; 7.5 pulses/s = 7.5 Hz.",
                    "Batch time at that rate = 4000 / 60 = 66.7 min."],
             ans="Volume = 4000 L; 60 L/min &rArr; 7.5 Hz."),
        dict(given="A cylindrical tank of diameter 2 m holds liquid at 1.5 m depth. Find "
                   "the volume, and the height that corresponds to a 4&ndash;20 mA level "
                   "transmitter reading 12 mA on a 0&ndash;3 m range.",
             steps=["Area = &pi; d&sup2;/4 = &pi; &times; 4 / 4 = 3.1416 m&sup2;.",
                    "V = 3.1416 &times; 1.5 = 4.71 m&sup3;.",
                    "12 mA is half span &rArr; h = 1.5 m."],
             ans="V = 4.71 m&sup3;; 12 mA &rArr; 1.5 m level."),
    ],
    viva=[
        ("Why is Q proportional to the square root of &Delta;P in an orifice meter?",
         "Bernoulli's equation gives velocity &prop; &radic;&Delta;P and volumetric flow is "
         "velocity times area, so the differential pressure must be square-rooted in the "
         "transmitter."),
        ("What fluids can an electromagnetic flow meter handle?",
         "Any liquid that conducts at least about 5 &micro;S/cm &mdash; water, acids, slurries "
         "&mdash; but not pure solvents or oil."),
        ("How does a guided radar (TDR) level probe work?",
         "A pulse travels down the probe, reflects at the liquid surface, and the time "
         "difference gives level regardless of foam or density changes."),
        ("Why is a bypass rotameter not suitable for billing?",
         "It is a variable-area local indicator with modest accuracy; fiscal transfer "
         "needs certified meters with traceable calibration."),
        ("What is totaliser functionality in a flow transmitter?",
         "It integrates pulse or flow-rate input over time to display total volume or "
         "mass, like an odometer for fluid."),
        ("What causes a float switch to stick?",
         "Scale, wax, sticky residues or mechanical wear; materials must be chosen "
         "compatible with the process fluid."),
    ],
    summ="Level instrumentation determines how much is in the tank, flow instrumentation "
         "determines how fast it moves, and both feed inventory control and billing. "
         "Ultrasonic, radar, float and differential-pressure methods cover level; "
         "orifice, turbine, electromagnetic and variable-area methods cover flow. Every "
         "selection must match fluid properties and required accuracy, and every meter "
         "needs periodic verification against a known volume.",
    spec=[
        ("Parameter", "Ultrasonic level", "Orifice + dP", "Electromagnetic flow"),
        ("Principle", "Echo time of sound", "Bernoulli differential", "Faraday's law"),
        ("Range", "0.5&ndash;15 m typical", "Depends on transmitter span", "10 mm &ndash; 3 m bore"),
        ("Accuracy", "&plusmn;0.25&ndash;0.5 %", "&plusmn;1&ndash;2 % of reading", "&plusmn;0.2&ndash;0.5 %"),
        ("Output", "4&ndash;20 mA, HART", "4&ndash;20 mA (&radic; extracted)", "Pulse / 4&ndash;20 mA"),
        ("Fluid limits", "Clean liquids, some foam ok", "Cleanish liquids, single phase", "Needs conductivity"),
        ("Typical use", "Tank inventory", "Steam, water, gas lines", "Water, slurry, chemical dosing"),
    ],
)

# ------------------------------------------------------------------ 12
EXTRAS[12] = dict(
    prose=[
        "Humidity and pH look like unrelated subjects, yet both are dominated by "
        "surface chemistry rather than bulk mechanics. A humidity sensor measures water "
        "molecules adsorbed on a polymer or oxide layer; a pH electrode measures the "
        "activity of hydrogen ions exchanging across a glass gel layer. Because the "
        "mechanism is chemical, both sensors age, both need periodic calibration, and "
        "both drift if stored in the wrong environment. Treating them as consumables "
        "with a replacement schedule is normal industrial practice.",
        "The DHT11 shows how low-cost consumer sensors work: a resistive humidity "
        "element and an NTC thermistor share one package with a small 8-bit MCU that "
        "calibrates itself in the factory and streams digits over a single wire. Its "
        "accuracy is modest, but for room monitoring it removes all analog design work. "
        "Industrial pH, by contrast, still needs a true high-impedance amplifier and "
        "careful cabling &mdash; there is no shortcut around the physics of a glass "
        "electrode.",
    ],
    num=[
        dict(given="A DHT11 returns raw humidity count 980 on its internal scale where "
                   "0&ndash;1023 maps to 20&ndash;80 %RH (factory-scaled). Find the humidity.",
             steps=["Fraction = 980/1023 = 0.958.",
                    "RH = 20 + 0.958 &times; (80 &minus; 20) = 20 + 57.5",
                    "RH &asymp; 77.5 % &mdash; realistically the module itself prints %RH directly."],
             ans="RH &asymp; 77 % (module output is usually already in %RH)."),
        dict(given="A freshly calibrated pH electrode reads a 177.5 mV difference between "
                   "pH 4.00 and pH 7.00 buffers at 25 &deg;C. Find the slope and compare "
                   "with the Nernst value.",
             steps=["&Delta;pH = 7.00 &minus; 4.00 = 3.00 units; slope = 177.5 / 3.00 = 59.17 mV/pH.",
                    "Nernst slope at 25 &deg;C = 2.303 RT/F = 59.16 mV/pH.",
                    "Percent of ideal = 59.17 / 59.16 &times; 100 &asymp; 100 % &mdash; healthy electrode."],
             ans="Slope = 59.17 mV/pH &asymp; 100 % of Nernst (excellent)."),
        dict(given="At 25 &deg;C a pH electrode measures &minus;41.4 mV relative to its "
                   "isopotential point. Find the pH if the offset is 0 mV.",
             steps=["pH = &minus;E / 59.16 = 41.4 / 59.16",
                    "pH = 0.70 &mdash; very acidic sample.",
                    "Temperature compensation uses 59.16 mV/pH only at 25 &deg;C; slope "
                    "changes about 0.2 mV/pH per &deg;C."],
             ans="pH &asymp; 0.70."),
    ],
    viva=[
        ("What does %RH mean?",
         "Relative humidity: the water vapour present compared with the maximum the air "
         "could hold at that temperature, expressed in percent."),
        ("Why are polymer humidity sensors temperature sensitive?",
         "Adsorption equilibrium shifts with temperature, so RH elements need temperature "
         "compensation to give correct %RH."),
        ("What is the Nernst slope for pH?",
         "2.303 RT/F &asymp; 59.16 mV per pH unit at 25 &deg;C; it is the electrode's "
         "millivolts-per-pH sensitivity."),
        ("How should a pH electrode be stored?",
         "Always in pH 4 or pH 7 storage solution, never in distilled water, which "
         "leaches ions from the glass and shortens life."),
        ("What is double junction electrode construction?",
         "Two reference systems in series so hostile process chemicals never contact the "
         "primary reference &mdash; used in silver-sensitive or protein-rich media."),
        ("Give one industrial use of humidity sensors.",
         "HVAC comfort control, grain and pharmaceutical drying, and paint booth climate "
         "control."),
    ],
    summ="Humidity sensing relies on the water affinity of a polymer or oxide layer, and "
         "pH sensing on the potential developed across a selective glass membrane. Both "
         "outputs are chemistry-dependent, temperature-dependent and ageing, so "
         "calibration intervals and correct storage matter as much as the initial "
         "selection. Low-cost modules like the DHT11 digitalise the consumer end, while "
         "process pH still demands high-impedance analogue design.",
    spec=[
        ("Parameter", "DHT11", "Industrial humidity element", "pH electrode"),
        ("Range", "20&ndash;80 %RH, 0&ndash;50 &deg;C", "0&ndash;100 %RH", "0&ndash;14 pH"),
        ("Accuracy", "&plusmn;5 %RH, &plusmn;2 &deg;C", "&plusmn;1&ndash;3 %RH", "&plusmn;0.01&ndash;0.1 pH"),
        ("Output", "Digital single wire", "Capacitance / voltage", "&plusmn;59 mV/pH"),
        ("Response", "1&ndash;10 s", "5&ndash;30 s", "seconds (stirred solution)"),
        ("Calibration", "Factory only", "Salt solutions / chill mirror", "Two-point buffers"),
        ("Storage", "Dry ambient", "Moderate RH", "Storage solution, capped"),
    ],
)

# ------------------------------------------------------------------ 13
EXTRAS[13] = dict(
    prose=[
        "Soil moisture and smoke detection illustrate how differently nature presents "
        "its measurements. Soil moisture is a slow, spatially uneven quantity &mdash; a "
        "probe reads only a small bulb of soil around it, so placement near roots and "
        "away from the wall matters as much as sensor accuracy. Smoke, on the other hand, "
        "is fast and transient: the sensor must respond within seconds while ignoring "
        "cooking vapour and dust. The same word 'sensor' covers devices whose time "
        "constants differ by six orders of magnitude.",
        "The two smoke-detection principles each have a blind spot, which is why "
        "buildings often install both. Optical (photoelectric) chambers are excellent at "
        "slow, smouldering fires that make big particles, but can be fooled by steam. "
        "Ionisation chambers react quickly to fast flaming fires, yet their weak "
        "radioactive source makes disposal regulated. Modern multi-sensor detectors run "
        "both algorithms and combine them to cut false alarms while keeping response "
        "time low.",
    ],
    num=[
        dict(given="A capacitive soil sensor is calibrated dry at 310 pF and waterlogged "
                   "at 780 pF. It reads 540 pF in the field. Find the volumetric water "
                   "content if 0 % &rarr; 310 pF and 40 % &rarr; 780 pF.",
             steps=["Fraction = (540 &minus; 310)/(780 &minus; 310) = 230/470 = 0.489",
                    "&theta; = 0 + 0.489 &times; 40 = 19.6 % by volume",
                    "Irrigation thresholds are then set, e.g. irrigate at 15 %, stop at 28 %."],
             ans="Water content &asymp; 19.6 % by volume."),
        dict(given="A photoelectric smoke chamber scatters 0.9 &micro;A into the photodiode "
                   "in clear air (dark current 5 nA) and 12 &micro;A in dense smoke. If the "
                   "alarm threshold is set at 3 &micro;A, what fraction of the dense-smoke "
                   "signal triggers the alarm?",
             steps=["Threshold above baseline: 3 &micro;A &minus; negligible dark current.",
                    "Ratio = 3 / 12 = 0.25 &rArr; 25 % of dense-smoke signal.",
                    "Housing gain and chamber geometry set how much real smoke reaches "
                    "this level."],
             ans="Alarm at 25 % of the dense-smoke photocurrent."),
        dict(given="An ionisation chamber draws 30 nA normally and rises to 55 nA in "
                   "smoke. The alarm band is set 8 nA above baseline. Find the alarm point "
                   "and margin to saturation.",
             steps=["Alarm current = 30 + 8 = 38 nA.",
                    "Margin to the 55 nA smoke value = 17 nA (about 62 % of the rise).",
                    "Alpha source strength and chamber geometry define these currents."],
             ans="Alarm at 38 nA; margin 17 nA before dense-smoke level."),
    ],
    viva=[
        ("Compare resistive and capacitive soil moisture sensors.",
         "Resistive probes pass current through the soil (electrode corrosion, salinity "
         "sensitive); capacitive probes measure dielectric constant with no exposed "
         "current and last longer."),
        ("Why must soil sensors be recalibrated per soil type?",
         "Bulk density, salinity and organic matter change the capacitance-to-moisture "
         "curve, so a single factory curve misreads across soils."),
        ("What particle size does a photoelectric smoke sensor see?",
         "Smoke particles around 0.4&ndash;10 &micro;m that Mie-scatter the chamber LED or "
         "lamp light onto the detector."),
        ("How does an ionisation chamber detect smoke?",
         "Smoke particles reduce ion current from a trace radioactive source; the fall in "
         "current is compared with a reference chamber."),
        ("Why do steam and dust cause false alarms?",
         "They scatter light or displace ions similarly to smoke; multi-sensor logic and "
         "time patterns distinguish them."),
        ("Where are soil moisture sensors actually installed?",
         "At root depth near representative plants, away from walls and wetting lines, "
         "at more than one point per irrigation zone."),
    ],
    summ="Soil moisture sensors track slow water content changes for irrigation control "
         "using resistive or capacitive principles, while smoke sensors protect life "
         "safety with fast optical or ionisation detection. Calibration against known "
         "moisture levels, correct probe placement, and understanding each smoke "
         "principle's blind spot are what make these sensors reliable in the field rather "
         "than merely functional on the bench.",
    spec=[
        ("Parameter", "Capacitive soil probe", "Photoelectric smoke", "Ionisation smoke"),
        ("Principle", "Dielectric constant vs moisture", "Light scattering", "Ion current reduction"),
        ("Range", "0&ndash;50 % VWC typical", "0.05&ndash;10 %/m obscuration", "0.5&ndash;10 %/m"),
        ("Output", "Analog voltage / I&#178;C", "Comparator / MCU alarm", "Comparator alarm"),
        ("Response", "seconds to minutes", "under 30 s (smouldering)", "under 10 s (flaming)"),
        ("Power", "3.3&ndash;5 V, low duty", "Alarm loop 9 V standby", "Alarm loop standby"),
        ("Best for", "Irrigation scheduling", "Homes, offices, hotels", "Fast flaming fire detection"),
    ],
)

# ------------------------------------------------------------------ 14
EXTRAS[14] = dict(
    prose=[
        "Sound measurement has two quite different faces. Consumer devices capture "
        "speech and music with an electret or MEMS microphone for communication, while "
        "instrumentation-grade sound level meters measure pressure fluctuations for "
        "safety and regulatory compliance. The physics at the diaphragm is identical; "
        "everything downstream &mdash; calibration, weighting filters, time averaging &mdash; "
        "differs according to whether the goal is intelligible speech or a legally "
        "defensible decibel reading.",
        "Microphone choice depends on environment as much as specification. Electret "
        "condenser microphones dominate portables because the charge is baked in and the "
        "external circuit is tiny. Measurement microphones use a separate polarising "
        "supply and a calibration socket so a 94 dB pistonphone can be injected before "
        "each survey. In windy outdoor sites a foam or fur windshield is not an "
        "accessory but part of the instrument, because wind rumble otherwise swamps the "
        "measurement in the low frequencies.",
    ],
    num=[
        dict(given="A microphone with sensitivity &minus;44 dBV/Pa (re 1 V/Pa) hears "
                   "94 dB SPL. Find its output voltage, given 94 dB SPL &asymp; 1 Pa.",
             steps=["&minus;44 dB means V = 10<sup>&minus;44/20</sup> = 6.31&times;10<sup>&minus;3</sup> V per Pa.",
                    "At 1 Pa: V = 6.31 mV.",
                    "Doubling pressure adds 6 dB, so 100 dB &rArr; 2 Pa &rArr; 12.6 mV."],
             ans="V<sub>out</sub> &asymp; 6.3 mV at 94 dB SPL."),
        dict(given="Two machines produce 85 dB and 88 dB at a workstation. Find the "
                   "combined level and check it against a 90 dB exposure limit.",
             steps=["Add intensities: ratio = 10<sup>(88&minus;85)/10</sup> = 10<sup>0.3</sup> = 2.0.",
                    "Combined = 10 lg(10<sup>8.5</sup> + 10<sup>8.8</sup>) = 88 + 10 lg(1 + 0.5) = 89.76 dB",
                    "89.76 dB &lt; 90 dB limit &mdash; margin is only 0.24 dB, so any addition "
                    "breaches it."],
             ans="Combined &asymp; 89.8 dB (just under the 90 dB limit)."),
        dict(given="A sound level meter on A-weighting shows 78 dB(A) and the dose timer "
                   "runs 8 h. The permissible 8-h level is 85 dB(A). Is the dose within "
                   "limit? By how much can level rise for the same dose?",
             steps=["Dose ratio = 10<sup>(78&minus;85)/5</sup> = 10<sup>&minus;1.4</sup> = 0.040 of allowable &mdash; very safe.",
                    "Exchange rate 3 dB: level could rise 7 dB above 78 &rArr; 85 dB(A) at same time.",
                    "NIOSH allows exactly 85 dB(A) for 8 h; OSHA uses 90 dB(A) with 5 dB rule."],
             ans="Dose is about 4 % of limit; safe to 85 dB(A) for 8 h."),
    ],
    viva=[
        ("What is the working principle of an electret condenser microphone?",
         "A permanently charged electret diaphragm forms a capacitor with a back plate; "
         "sound moves the diaphragm, changing capacitance and current in the JFET buffer."),
        ("Why are measurement microphones calibrated with a pistonphone?",
         "A pistonphone injects a known 114 or 94 dB reference tone so the whole chain "
         "is verified before and after a survey."),
        ("What is the difference between dB SPL and dB sound level?",
         "dB SPL is the physical pressure level referenced to 20 &micro;Pa; sound level "
         "meters apply frequency weightings (A, C) and time weightings before display."),
        ("Why is A-weighting used for hearing-risk surveys?",
         "The ear is less sensitive at low frequencies; A-weighting mirrors that response "
         "and correlates better with noise-induced hearing loss."),
        ("What causes microphone self-noise?",
         "Thermal and electronic noise in the diaphragm and preamplifier sets the floor "
         "for quiet measurements, quoted as dB(A) or &micro;V rms."),
        ("Where are MEMS microphones replacing electrets?",
         "In phones, headsets and compact IoT audio &mdash; they reflow-solder like any SMD "
         "part and tolerate automated assembly."),
    ],
    summ="Sound sensors convert pressure fluctuations at a diaphragm into electrical "
         "signals: electret and MEMS microphones for communication, polarised "
         "measurement microphones for instrumentation. Sensitivity in dBV/Pa, self-noise, "
         "weighting filters and time response define meter quality, and correct "
         "calibration with a pistonphone plus proper windshielding define field accuracy. "
         "Combining levels logarithmically, not arithmetically, is the calculation every "
         "noise survey depends on.",
    spec=[
        ("Parameter", "Electret mic (ECM)", "MEMS mic", "Class 2 sound level meter"),
        ("Sensitivity", "&minus;35 to &minus;44 dBV/Pa", "&minus;26 to &minus;38 dBV/Pa", "Defined by IEC 61672"),
        ("Frequency range", "50 Hz &ndash; 16 kHz", "100 Hz &ndash; 10 kHz", "20 Hz &ndash; 20 kHz (&plusmn;1 dB)"),
        ("Supply", "1.5&ndash;10 V with JFET", "1.8&ndash;3.6 V", "Internal battery"),
        ("Self-noise", "30&ndash;40 dB(A)", "25&ndash;35 dB(A)", "Depends on class"),
        ("Weighting", "None (raw audio)", "None", "A / C / Z selectable"),
        ("Typical use", "Voice recorders, intercoms", "Phones, wearables", "Occupational noise surveys"),
    ],
)

# ------------------------------------------------------------------ 15
EXTRAS[15] = dict(
    prose=[
        "A smart sensor is best understood as a measuring device plus a small "
        "engineering office on the same chip. The raw element still does the physics, "
        "but conversion, linearisation, temperature compensation, alarm limits and "
        "digital comms all happen inside the package. For the system designer this "
        "shortens the signal path &mdash; fewer analogue metres of cable for noise to "
        "enter &mdash; and moves complexity from hardware debugging into configuration "
        "registers that can be changed over software.",
        "The trade-off is that smart sensors are less transparent. When a 4&ndash;20 mA "
        "transmitter shows 12.6 mA you can put a multimeter anywhere and reason about "
        "the loop; when a sensor answers an I&#178;C register with a compensated value "
        "you must trust the factory compensation and the bus integrity. Good practice "
        "therefore keeps a check point: periodic comparison against a reference "
        "instrument, loop diagnostics on the digital bus, and documented register maps "
        "so firmware and device never drift apart.",
    ],
    num=[
        dict(given="A smart RTD sensor returns 16-bit count 0x13C0. The datasheet formula is "
                   "T = count &times; 0.0625 &minus; 256. Find the temperature.",
             steps=["0x13C0 = 1&times;4096 + 3&times;256 + 12&times;16 = 5056 decimal.",
                    "Scaled value = 5056 &times; 0.0625 = 316.0.",
                    "T = 316.0 &minus; 256 = 60.0 &deg;C."],
             ans="T = 60.0 &deg;C."),
        dict(given="An accelerometer smart sensor reports peak 16384 counts at &plusmn;4 g "
                   "full scale on a signed 16-bit output (&minus;32768 to +32767). Find g at "
                   "count 4096.",
             steps=["Full scale counts = 32767 for +4 g.",
                    "Scale = 4 / 32767 = 1.2206&times;10<sup>&minus;4</sup> g/count.",
                    "At 4096: a = 4096 &times; 1.2206&times;10<sup>&minus;4</sup> = 0.50 g."],
             ans="a = 0.50 g."),
        dict(given="A smart flow sensor on Modbus RTU returns 0x0A2C = 2604 counts on a "
                   "scaled register where 4000 counts = 100.0 m&sup3;/h. Find the flow.",
             steps=["Scale = 100.0 / 4000 = 0.025 m&sup3;/h per count.",
                    "Flow = 2604 &times; 0.025 = 65.1 m&sup3;/h.",
                    "Hex is used on the wire; engineers usually work in decimal."],
             ans="Q = 65.1 m&sup3;/h."),
    ],
    viva=[
        ("What makes a sensor 'smart'?",
         "On-board signal processing plus a digital communication interface &mdash; "
         "self-calibration, diagnostics and configuration are possible, not just raw "
         "measurement."),
        ("Name typical digital buses used by smart sensors.",
         "I&#178;C, SPI, 1-Wire, HART superimposed on 4&ndash;20 mA, Profibus PA, Foundation "
         "Fieldbus, IO-Link."),
        ("What is a blob or pre-calibrated module?",
         "A factory-calibrated sensor-plus-ASIC sealed as one unit; the OEM drops it in "
         "without individual calibration."),
        ("Why is scaling information as important as the raw count?",
         "The controller multiplies the count by scale and offset; a wrong register "
         "scaling silently corrupts every engineering unit downstream."),
        ("What diagnostics do smart transmitters offer?",
         "Open sensor, shorted input, out-of-range, calibration due, power supply low and "
         "stuck-at-fault detection on the loop."),
        ("How does self-diagnostics improve plant reliability?",
         "Failures are announced with an error code instead of passing as a plausible "
         "wrong value, so maintenance is triggered before the loop miscontrols."),
    ],
    summ="Smart sensors integrate element, converter, compensation and digital "
         "communication into one package, shifting work from analogue conditioning to "
         "register configuration. Correct interpretation of scaled counts, use of the "
         "documented formula, and reliance on built-in diagnostics are the skills needed "
         "to exploit them. In return the system gains noise immunity, remote "
         "reconfiguration and early fault announcement.",
    spec=[
        ("Parameter", "Typical smart sensor feature", "Benefit"),
        ("Interface", "I&#178;C / SPI / HART / IO-Link", "Direct digital connection to MCU or PLC"),
        ("Resolution", "12&ndash;24 bit internal ADC", "Finer steps than 4&ndash;20 mA loop"),
        ("Compensation", "Temperature, linearisation, drift", "Better accuracy over ambient"),
        ("Diagnostics", "Open, short, over-range, due-cal", "Failures announce themselves"),
        ("Configuration", "Address, range, filter, alarms", "Change without rewiring"),
        ("Power", "1.8&ndash;3.6 V core, bus powered", "Suitable for battery and IoT nodes"),
        ("Example devices", "BME280, TMP117, XENSIVDLM", "Humidity, precision temperature, presence"),
    ],
)

# ------------------------------------------------------------------ 16
EXTRAS[16] = dict(
    prose=[
        "These performance parameters are the language of every datasheet and every "
        "purchase enquiry, and they are also the language of contract disputes. When a "
        "vendor promises 0.5 % of span and the plant measures 1 % of reading, the "
        "argument is really about which definition was agreed. Reading this topic "
        "carefully therefore pays twice: once when you select an instrument, and again "
        "when you defend or negotiate its specification.",
        "A useful mental habit is to convert every percentage into engineering units "
        "before comparing instruments. An error of &plusmn;1 % of a 100 bar span is "
        "&plusmn;1 bar, which may be excellent for a vessel survey and hopeless for a "
        "laboratory regulator working at 2 bar. The same number means different things "
        "in different parts of the range, which is why modern specifications quote both "
        "% of reading and % of span, and why averaging repeated readings can reduce "
        "random error but never cancel a systematic bias.",
    ],
    num=[
        dict(given="A 0&ndash;20 bar transmitter with accuracy &plusmn;0.5 % of span reads "
                   "14.0 bar. Find the possible true value.",
             steps=["Span = 20 bar; error = 0.5 &times; 20 / 100 = 0.1 bar.",
                    "True value lies in 14.0 &minus; 0.1 to 14.0 + 0.1 = 13.9 to 14.1 bar.",
                    "As % of the reading this is 0.1/14 = 0.71 %."],
             ans="13.9&ndash;14.1 bar (&plusmn;0.1 bar)."),
        dict(given="A level transmitter spans 0&ndash;5 m and outputs 4&ndash;20 mA. The "
                   "current is 7.2 mA. Find level and % of span error if the meter is "
                   "&plusmn;0.2 mA.",
             steps=["% of span = (7.2 &minus; 4)/16 &times; 100 = 20 % &rArr; level = 1.0 m.",
                    "0.2 mA in level = 0.2/16 &times; 5 = 0.0625 m.",
                    "Level = 1.000 &plusmn; 0.063 m."],
             ans="Level = 1.0 m &plusmn; 0.063 m."),
        dict(given="Successive readings of a steady 50.00 V standard are 49.8, 50.1, 49.9, "
                   "50.0 and 50.2 V. Find mean, random error and any bias if true value "
                   "is 50.10 V.",
             steps=["Mean = (49.8+50.1+49.9+50.0+50.2)/5 = 50.00 V.",
                    "Random spread &asymp; &plusmn;0.2 V around the mean.",
                    "Bias = mean &minus; true = 50.00 &minus; 50.10 = &minus;0.10 V (systematic)."],
             ans="Mean 50.00 V, random &plusmn;0.2 V, bias &minus;0.10 V."),
    ],
    viva=[
        ("Distinguish accuracy, precision and resolution.",
         "Accuracy is closeness to the true value; precision is repeatability of "
         "readings; resolution is the smallest change the display or output can show."),
        ("What is hysteresis error?",
         "The maximum difference between ascending and descending outputs at the same "
         "input, caused by mechanical or magnetic lag."),
        ("Why is % of span different from % of reading?",
         "% of span keeps a fixed error band across the range; % of reading shrinks with "
         "the value, so the two diverge at low readings."),
        ("What does trimmer-free calibration mean?",
         "Digital calibration stored in EEPROM replaces mechanical potentiometers, "
         "improving stability and allowing remote recalibration."),
        ("How does dead band differ from resolution?",
         "Resolution is the smallest detectable input step; dead band is an input region "
         "where the output does not respond at all until the change exceeds a threshold."),
        ("Define repeatability.",
         "The ability of the same instrument under the same conditions to give the same "
         "output for repeated applications of one input, without regard to true value."),
    ],
    summ="Range, span, accuracy, uncertainty, linearity, hysteresis, repeatability, "
         "resolution and response time together describe what an instrument can honestly "
         "deliver. Percentages must be converted into engineering units before they are "
         "compared, random error can be reduced by averaging, and systematic bias can "
         "only be removed by calibration. These definitions form the acceptance criteria "
         "for every sensor procurement.",
    spec=[
        ("Parameter", "Typical good value (process)", "Notes"),
        ("Range", "Match process min&ndash;max with margin", "Never operate above URV"),
        ("Span", "URV &minus; LRV", "Base of all % span errors"),
        ("Accuracy", "&plusmn;0.075&ndash;0.5 % of span", "Classified by standard like 0.5"),
        ("Repeatability", "&plusmn;0.05 % of span", "Often better than accuracy"),
        ("Hysteresis", "0.05&ndash;0.5 % of span", "Worse in mechanical elements"),
        ("Resolution", "1 part in 4096 (12 bit) or better", "Display or digital output step"),
        ("Response (T<sub>63</sub>)", "ms (pressure) to min (temperature well)", "Must suit process time constant"),
    ],
)

# ------------------------------------------------------------------ 17
EXTRAS[17] = dict(
    prose=[
        "Actuators are where the controller finally touches the process, so their "
        "selection determines whether a good control strategy actually works. A valve "
        "that strok es slowly, a motor that overheats under continuous duty, or a relay "
        "whose contacts weld shut will defeat perfect sensor readings and perfect PID "
        "tuning. Sizing therefore starts with the process &mdash; force, torque, travel, "
        "duty cycle, environment &mdash; and only then looks at electrical ratings.",
        "Fail-safe philosophy deserves special attention because it protects people and "
        "plant when power or air fails. The usual convention is air-to-open, fail-close "
        "for feed lines that must not overrun, and the reverse for cooling or relief "
        "duties that must keep flowing. Every actuator decision should state the failure "
        "position explicitly on the datasheet and drawing, and the stroke time must be "
        "compatible with the process safety time; an actuator slower than the process "
        "hazard offers no protection at all.",
    ],
    num=[
        dict(given="A pneumatic actuator has an effective piston area of 40 cm&sup2; and "
                   "supply pressure of 6 bar. Find the force available at full stroke.",
             steps=["P = 6 bar = 6&times;10<sup>5</sup> Pa; A = 40 cm&sup2; = 4&times;10<sup>&minus;3</sup> m&sup2;.",
                    "F = P &times; A = 6&times;10<sup>5</sup> &times; 4&times;10<sup>&minus;3</sup> = 2400 N.",
                    "Derate about 15 % for friction and spring opposition &rArr; about 2040 N useful."],
             ans="F &asymp; 2400 N (about 2 kN before derating)."),
        dict(given="A 24 V DC motor draws 0.5 A at no load (R<sub>a</sub> = 1.2 &Omega;) and 4 A "
                   "at rated load. Torque constant k<sub>t</sub> = 0.075 Nm/A. Find no-load "
                   "back-emf, armature voltage drop at rated load, and developed torque.",
             steps=["E<sub>no-load</sub> = V &minus; I<sub>0</sub> R<sub>a</sub> = 24 &minus; 0.5 &times; 1.2 = 23.4 V.",
                    "Rated drop = I R<sub>a</sub> = 4 &times; 1.2 = 4.8 V, so E = 19.2 V and speed "
                    "falls about 18 % below no load.",
                    "T = k<sub>t</sub> I = 0.075 &times; 4 = 0.30 Nm developed at rated load."],
             ans="E<sub>0</sub> = 23.4 V, drop = 4.8 V, T = 0.30 Nm."),
        dict(given="A valve must close in 8 s for a process safety time of 25 s. The "
                   "positioner receives 4&ndash;20 mA and the actuator stroks in 12 s at "
                   "full signal. Is it acceptable?",
             steps=["Actuator full stroke 12 s vs required safe close 8 s from trip.",
                    "Trip can be issued at t = 0; valve fully closed at 12 s &lt; 25 s safety time.",
                    "Even partial travel early in the stroke may suffice &mdash; check required "
                    "tightness point."],
             ans="12 s stroke &lt; 25 s safety time &mdash; acceptable if trip starts immediately."),
    ],
    viva=[
        ("What is meant by fail-safe action of an actuator?",
         "The position the valve or damper takes when power, signal or instrument air is "
         "lost &mdash; typically fail-close or fail-open."),
        ("Why is a spring-and-yoke actuator common on control valves?",
         "The spring returns the stem to the fail position without air, and the yoke "
         "gives a stiff, aligned mounting for the stem and positioner."),
        ("Differentiate on-off and modulating actuators.",
         "On-off actuators only energise fully one way or the other; modulating "
         "actuators hold any intermediate position proportional to the controller signal."),
        ("What is stroke time and why is it specified?",
         "Time for full travel open-to-close; it must be much less than the process "
         "time constant for stable control and less than safety time for protection."),
        ("How are electric actuators protected outdoors?",
         "Through enclosure ratings (IP65/67), corrosion-resistant coatings and heaters "
         "to stop condensation in the gearbox."),
        ("Give two reasons to prefer pneumatic over electric actuation.",
         "Intrinsic safety in hazardous areas, and very high force-to-weight with "
         "simple, reliable fail-safe springs."),
    ],
    summ="Actuators convert controller output into motion: pneumatic, hydraulic, "
         "electric and manual drives each covering a different corner of force, speed and "
         "environment. Selection proceeds from process force or torque through stroke "
         "time, duty cycle and fail-safe position to the final rating plate. Control "
         "valves add flow characteristics and trim options; every installation must "
         "document where the actuator goes when everything fails.",
    spec=[
        ("Parameter", "Pneumatic linear", "Electric rotary", "Hydraulic"),
        ("Typical force", "0.5&ndash;50 kN", "Torque 5&ndash;500 Nm", "10&ndash;500 kN"),
        ("Supply", "3&ndash;7 bar air", "24 V DC / 230 V AC", "70&ndash;350 bar oil"),
        ("Fail-safe", "Spring return (choose FC/FO)", "Motor / spring brake", "Accumulator or lock"),
        ("Stroke time", "1&ndash;60 s", "5&ndash;60 s", "0.5&ndash;10 s"),
        ("Hazardous area", "Inherently safe option", "Certified enclosure needed", "Special enclosures"),
        ("Typical use", "Control valves, dampers", "Quarter-turn valves, louvres", "Heavy presses, rams"),
    ],
)

# ------------------------------------------------------------------ 18
EXTRAS[18] = dict(
    prose=[
        "Control valves are the most slowly changing part of any control loop and "
        "frequently the most neglected. A perfectly tuned controller cannot overcome a "
        "valve with a loose stem gland, a saturated actuator, or stiction that makes it "
        "jump in steps. During loop audits, watching the positioner feedback while the "
        "signal ramps slowly will reveal dead band, hysteresis and stick-slip long before "
        "they show up as mysterious oscillations in the process variable.",
        "Choosing flow characteristics is really choosing where in the installed "
        "system you want the gain to live. A linear trim gives equal percentage gain from "
        "the valve itself; combined with a process whose gain falls as opening increases "
        "&mdash; typical of many liquid loops &mdash; the product stays nearly constant and "
        "the loop behaves similarly at low and high flow. Quick-opening trims are for "
        "on-off duty, and linear trims suit pressure or gas duty where the process gain "
        "does not vary much with position.",
    ],
    num=[
        dict(given="A valve has C<sub>v</sub> = 25 and passes water (&rho; = 1000 kg/m&sup3;, "
                   "SG = 1) with &Delta;P = 1 bar (100 kPa). Find flow in m&sup3;/h.",
             steps=["Q (US gpm) = C<sub>v</sub> &times; &radic;(&Delta;P / SG) = 25 &times; &radic;100",
                    "Q = 25 &times; 10 = 250 gpm",
                    "Convert: 1 gpm = 0.2271 m&sup3;/h &rArr; Q = 250 &times; 0.2271 = 56.8 m&sup3;/h"],
             ans="Q &asymp; 56.8 m&sup3;/h (250 gpm)."),
        dict(given="An air-to-open valve fails ______ on loss of air; state the position "
                   "and one application where fail-open is chosen instead.",
             steps=["Air pressure pushes against the spring to open; loss of air lets the "
                    "spring close the valve.",
                    "Fail-closed suits fuel, feed or product lines that must stop.",
                    "Fail-open suits cooling water, quench or relief-assist duties where "
                    "losing flow is dangerous."],
             ans="Fails closed; use fail-open for cooling or utility lines that must keep flowing."),
        dict(given="An equal percentage valve has rangeability R = 50 (q<sub>min</sub>/q<sub>max</sub> "
                   "= 1/50). Find flow as % of maximum at 0 %, 50 % and 80 % travel.",
             steps=["Equal percentage law: q/q<sub>max</sub> = R<sup>(x &minus; 1)</sup> where x is the "
                    "fraction of travel.",
                    "At x = 0: q/q<sub>max</sub> = 50<sup>&minus;1</sup> = 0.020 &rArr; 2.0 % of maximum.",
                    "At x = 0.50: 50<sup>&minus;0.5</sup> = 1/7.07 = 0.141 &rArr; 14.1 % of maximum.",
                    "At x = 0.80: 50<sup>&minus;0.2</sup> = e<sup>&minus;0.2 ln 50</sup> = 0.457 &rArr; 45.7 % of maximum. "
                    "Each equal 10 % of travel multiplies flow by 50<sup>0.1</sup> &asymp; 1.48."],
             ans="q/q<sub>max</sub> = 2.0 % at 0 travel, 14.1 % at 50 %, 45.7 % at 80 %."),
    ],
    viva=[
        ("What is the valve coefficient C<sub>v</sub>?",
         "US gallons per minute of water at 60 &deg;F passing with 1 psi pressure drop "
         "&mdash; the sizing number for a valve."),
        ("Compare quick-opening, linear and equal percentage trims.",
         "Quick-opening gives most flow early (on-off duty); linear is proportional to "
         "travel; equal percentage gives equal flow change per equal percent travel, "
         "suitable when process gain varies strongly."),
        ("What is a positioner and why is it needed?",
         "A local controller that forces valve position to match the signal despite "
         "friction and unbalance &mdash; it fixes stiction and improves stroking speed."),
        ("Why is valve sizing in terms of &Delta;P important?",
         "If available &Delta;P across the valve is small at high demand, the valve "
         "cavitates or simply cannot pass required flow even at full open."),
        ("What is cavitation and how is it avoided?",
         "Liquid flashes to vapour then collapses, pitting trim; avoided with pressure "
         "recovery trim, lower &Delta;P per stage, or operating above vapour pressure."),
        ("What tests are done during valve commissioning?",
         "Stroke travel, verify fail position, check travel vs mA linearity, tightness "
         "test, and travel time measurement."),
    ],
    summ="Control valves act as the final control element: actuator, positioner and "
         "internals working together to place flow exactly where the controller demands. "
         "Correct C<sub>v</sub> sizing, matched flow characteristic, explicit fail-safe "
         "action and healthy stroking mechanics are the four pillars. Without them the "
         "best tuning in the world cannot hold the process steady.",
    spec=[
        ("Parameter", "Typical specification", "Remark"),
        ("Body size", '1/2" to 12" DN15&ndash;DN300', "Match line velocity and C<sub>v</sub>"),
        ("C<sub>v</sub> range", "0.1 &ndash; 1000+", "From sizing equation and &Delta;P"),
        ("Characteristic", "Linear / equal % / quick", "Equal % most common in liquid service"),
        ("Actuation", "Spring-and-yoke pneumatic", "Air-to-open / air-to-close"),
        ("Fail action", "FC or FO (state it!)", "Chosen from process hazard"),
        ("Stroke", "Linear 10&ndash;25 mm; quarter-turn 90&deg;", "With position feedback"),
        ("Leak class", "ANSI Class IV&ndash;VI (soft seat)", "Shut-off tightness"),
        ("Positioner", "4&ndash;20 mA with feedback", "HART/fieldbus optional"),
    ],
)

# ------------------------------------------------------------------ 19
EXTRAS[19] = dict(
    prose=[
        "Power semiconductor devices are the industrial electrician's alphabet: SCR "
        "and TRIAC for controlled rectification of AC, MOSFET and IGBT for fast DC "
        "switching. What unites them is the need to manage heat and gate drive together. "
        "A device that switches kilowatts in microseconds will still melt if its "
        "heatsink is undersized, and a correctly rated device driven with a weak or "
        "ringing gate pulse will latch at the wrong time. Package, isolation and "
        "cooling are part of the electrical design, not an afterthought.",
        "Choosing between phase control and chopper control is a systems decision. "
        "Phase control with a TRIAC is cheapest for lamps, heaters and universal motors "
        "on 50/60 Hz mains, but it injects harmonics and lowers power factor. Chopper "
        "control with a MOSFET at tens of kilohertz keeps efficiency high and filters "
        "small, at the cost of more complex drive circuits. Modern dimmers and motor "
        "drives increasingly blend both techniques with power-factor correction to meet "
        "harmonic regulations.",
    ],
    num=[
        dict(given="A 230 V, 50 Hz supply feeds a resistive heater through a TRIAC at "
                   "firing angle &alpha; = 90&deg;. Find the RMS load voltage and power if "
                   "R = 48.4 &Omega;.",
             steps=["V<sub>rms</sub> = (V<sub>m</sub>/&radic;2) &times; &radic;(1 &minus; &alpha;/&pi; "
                    "+ sin2&alpha;/(2&pi;)) with &alpha; in radians, &alpha; = &pi;/2.",
                    "&radic;(1 &minus; 0.5 + 0) = &radic;0.5 = 0.707; V<sub>rms</sub> = 230 &times; 0.707 = 162.6 V.",
                    "P = V&sup2;/R = 162.6&sup2; / 48.4 = 545 W (full-on would be 1100 W)."],
             ans="V<sub>rms</sub> = 162.6 V, P &asymp; 545 W."),
        dict(given="A resistive heater of 10 &Omega; runs from a 120 V DC bus through a "
                   "MOSFET chopper with duty cycle D = 0.65. Find average current, power, "
                   "and MOSFET loss if R<sub>DS(on)</sub> = 0.05 &Omega;.",
             steps=["V<sub>load</sub> = D &times; V = 0.65 &times; 120 = 78 V; I = 78/10 = 7.8 A.",
                    "P<sub>load</sub> = 78 &times; 7.8 = 608 W.",
                    "Conduction loss = I&sup2; &times; R<sub>DS(on)</sub> &times; D = 7.8&sup2; &times; 0.05 &times; 0.65 = 1.98 W."],
             ans="I = 7.8 A, P<sub>load</sub> = 608 W, MOSFET loss &asymp; 2 W."),
        dict(given="An SCR circuit has supply 230 V RMS, R = 23 &Omega; and is fired at "
                   "&alpha; = 60&deg;. Find RMS current and conduction angle.",
             steps=["Conduction angle = 180&deg; &minus; 60&deg; = 120&deg;.",
                    "&alpha; = &pi;/3 rad; V<sub>rms</sub> = 230 &times; &radic;(1 &minus; 1/3 + sin120&deg;/(2&pi;))",
                    "= 230 &times; &radic;(0.667 + 0.138) = 230 &times; 0.897 = 206.4 V; I = 206.4/23 = 8.97 A."],
             ans="Conduction = 120&deg;; I<sub>rms</sub> &asymp; 9.0 A."),
    ],
    viva=[
        ("How does an SCR differ from a diode?",
         "An SCR is a latching four-layer device: it only conducts after a gate pulse "
         "once anode is positive, and then stays on until current falls below holding "
         "level."),
        ("What is latching current versus holding current?",
         "Latching current is the minimum anode current to keep the SCR on right after "
         "gate removal; holding current is the minimum to stay on once already latched."),
        ("Why can a TRIAC control AC but an SCR needs two for full control?",
         "A TRIAC conducts both half-cycles with either gate polarity; a single SCR blocks "
         "one half-cycle, so back-to-back SCRs or a BRCS pair are used for full-wave "
         "control."),
        ("What does 'firing angle' mean?",
         "The delay from the zero crossing of the AC waveform to the moment the device is "
         "triggered; it directly sets RMS power delivered."),
        ("Why is a snubber circuit placed across a TRIAC?",
         "To limit dV/dt that could cause false triggering, especially with inductive "
         "loads such as motors and transformers."),
        ("Compare MOSFET and SCR switching speed.",
         "MOSFETs switch in nanoseconds and can be PWM'd at tens of kHz; SCRs commutate "
         "with the AC line and are limited to line-frequency phase control unless forced "
         "commutated."),
    ],
    summ="SCRs, TRIACs and power MOSFETs form the core of electric power control: "
         "phase-controlled conduction for AC mains duty, high-frequency chopper switching "
         "for DC and inverter duty. Firing angle sets RMS output, duty cycle sets average "
         "output, and in both cases losses, heatsinking and protection snubbers must be "
         "sized with the same care as the switching device itself.",
    spec=[
        ("Parameter", "SCR (e.g. C106)", "TRIAC (e.g. BTA16)", "MOSFET (e.g. IRF540)"),
        ("Voltage rating", "400&ndash;1600 V", "400&ndash;800 V", "55&ndash;600 V (low R<sub>DS</sub>)"),
        ("Current rating", "10&ndash;100 A (heatsunk)", "16&ndash;40 A", "20&ndash;100 A pulsed"),
        ("Gate / drive", "Pulse, few mA", "Pulse, few mA", "Voltage driven, 10 V gate, low charge"),
        ("Switching speed", "Line frequency, &mu;s turn-off", "Line frequency", "ns &mdash; 100 kHz+ PWM"),
        ("Control method", "Phase angle", "Phase angle (AC)", "PWM duty cycle"),
        ("Typical use", "DC motor, heater, excitation", "Lamp dimmer, AC motor", "SMPS, inverter, DC chopper"),
    ],
)

# ------------------------------------------------------------------ 20
EXTRAS[20] = dict(
    prose=[
        "Relays and solenoids are the bridge between low-voltage control electronics "
        "and real-world power circuits, and they are where most field faults occur. "
        "Contacts pit and weld under inductive load switching, coils burn when a supply "
        "runs high, and solenoids jam from ingress or misalignment. Understanding the "
        "simple physics &mdash; magnetic force in the gap, contact resistance at the joint "
        "&mdash; lets you diagnose most failures at the bench with a multimeter and a "
        "datasheet.",
        "Practical selection habits prevent the classic mistakes. Always flyback-diode "
        "a DC coil when switching from a transistor, because the collapsed field will "
        "otherwise punch through the driver. Choose contact material and rating for the "
        "load type: a relay rated 10 A resistive may be good for only 1 A to a small "
        "motor or lamp inrush. And separate the coil circuit from the contact circuit "
        "clearly in drawings so maintenance can isolate either side safely.",
    ],
    num=[
        dict(given="A 24 V DC relay coil draws 60 mA. Find coil resistance, power "
                   "consumption, and the flyback energy stored in a 100 mH coil at "
                   "steady current.",
             steps=["R = V/I = 24/0.06 = 400 &Omega;.",
                    "P = V &times; I = 24 &times; 0.06 = 1.44 W.",
                    "E = ½ L I&sup2; = 0.5 &times; 0.1 &times; 0.06&sup2; = 180 &micro;J &mdash; small but enough to "
                    "damage an unclamped transistor."],
             ans="R = 400 &Omega;, P = 1.44 W, stored energy = 180 &micro;J."),
        dict(given="A relay contact pair is rated 8 A at 250 V AC resistive and is switching "
                   "a 24 V, 3 A lamp with 15&times; inrush (45 A for 80 ms). Assess suitability.",
             steps=["Steady current 3 A &lt; 8 A rating &mdash; OK for continuous duty.",
                    "Inrush 45 A for 80 ms is within typical lamp inrush allowance for "
                    "relay contacts if repeated rate is limited.",
                    "Check the manufacturer's max inrush table and derate if switching "
                    "many lamps on one contact."],
             ans="Suitable with margin; verify inrush table and switching frequency."),
        dict(given="A solenoid valve has coil resistance 220 &Omega; at 110 V AC and an "
                   "air gap force constant K = 0.8 N/mm&sup2; near seating. Estimate force "
                   "with 0.5 mm gap assuming F &prop; I&sup2;/g&sup2; normalised to "
                   "F(0.25 mm) = 40 N at rated current.",
             steps=["F &prop; I&sup2;/g&sup2;: F(0.5) = F(0.25) &times; (0.25/0.5)&sup2; = 40 &times; 0.25",
                    "F(0.5 mm) = 10 N at rated current.",
                    "Force rises steeply as the plunger seats &mdash; sealing pressure "
                    "increases near closure."],
             ans="F &asymp; 10 N at 0.5 mm gap, rising toward 40 N as it seats."),
    ],
    viva=[
        ("Why is a diode connected across a DC relay coil?",
         "It clips the high-voltage inductive spike when the coil is switched off, "
         "protecting the transistor driver."),
        ("What does '10 A resistive, 1 A inductive' contact rating mean?",
         "Inductive loads arc far more at break, so the same contacts must be derated "
         "heavily for solenoid, motor or transformer loads."),
        ("Difference between latching and non-latching relays?",
         "Non-latching returns to original state when coil de-energises; latching holds "
         "position with permanent or mechanical lock until a pulse of opposite polarity."),
        ("How does a solenoid produce linear motion?",
         "Current in the coil magnetises the core; the gap field pulls the plunger to "
         "reduce reluctance, converting electrical power into stroke force."),
        ("What is drop-out voltage of a relay?",
         "Coil voltage below which the armature releases &mdash; typically 70&ndash;80 % of "
         "nominal; a sagging supply can cause chatter."),
        ("Why might a relay chatter at turn-on?",
         "Coil voltage too low, AC ripple, mechanical stick, or supply dipping below "
         "pull-in voltage when the coil inrush hits."),
    ],
    summ="Relays provide galvanically isolated contact switching and solenoids provide "
         "direct linear or rotary actuation, both from magnetic circuits. Coil "
         "resistance, pull-in and drop-out voltages, contact ratings for the actual load "
         "type, and spike suppression are the numbers that decide reliability. Mounted "
         "clean, driven with proper flyback protection and derated for inrush, these "
         "simple devices run for millions of operations.",
    spec=[
        ("Parameter", "General purpose relay", "DC solenoid valve"),
        ("Coil", "5&ndash;240 V AC/DC, 0.1&ndash;2 W", "12/24 V DC, 5&ndash;30 W typical"),
        ("Pull-in / drop-out", "70&ndash;100 % / 10&ndash;40 % of V<sub>nom</sub>", "Pull-in rated, drop-out &lt; 70 %"),
        ("Contacts", "SPDT/DPDT, 8&ndash;10 A resistive", "&mdash; (valve is the load)"),
        ("Mechanical life", "10<sup>7</sup>&ndash;10<sup>8</sup> operations", "10<sup>6</sup>&ndash;10<sup>7</sup> cycles"),
        ("Electrical life", "10<sup>5</sup> at full load", "Depends on duty cycle"),
        ("Stroke / force", "&mdash;", "5&ndash;20 mm, 10&ndash;100 N"),
        ("Protection", "Flyback diode (DC), RC (AC)", "Coil snubber, manual override"),
    ],
)

# ------------------------------------------------------------------ 21
EXTRAS[21] = dict(
    prose=[
        "Electric motors are process actuators first and textbook machines second. "
        "Selection starts with the load: continuous torque needed, peak torque for "
        "acceleration, duty cycle, and environment. An induction motor is the default "
        "workhorse because it is cheap, brushless and rugged; a DC or brushless DC motor "
        "is chosen when wide speed range and simple torque control matter; steppers and "
        "servos take over when position accuracy is the point. The drive electronics "
        "have improved so much that motor and drive are now sized together as one "
        "system.",
        "Power electronics has quietly changed the rules. Variable-frequency drives "
        "let a standard induction motor run at any speed, which has retired many "
        "gearboxes and made damper and valve retrofits simpler. Stepper systems give "
        "open-loop precision that is hard to beat at low cost, provided the load never "
        "exceeds pull-out torque. Servo systems with encoders close the loop and give "
        "dynamic performance, at the price of tuning and commissioning skill. Matching "
        "the motor type to these real requirements &mdash; not to habit &mdash; is the essence "
        "of actuator selection.",
    ],
    num=[
        dict(given="A 4-pole induction motor runs at 1440 rpm on 50 Hz supply. Find "
                   "synchronous speed and slip.",
             steps=["N<sub>s</sub> = 120 f / P = 120 &times; 50 / 4 = 1500 rpm.",
                    "Slip s = (1500 &minus; 1440)/1500 = 0.04 = 4 %.",
                    "Rotor frequency = s &times; f = 0.04 &times; 50 = 2 Hz."],
             ans="N<sub>s</sub> = 1500 rpm, slip = 4 %."),
        dict(given="A stepper motor has 1.8&deg; full step angle and is driven at 1000 "
                   "pulses/s in half-step mode through a 64:1 gear. Find output shaft "
                   "speed in rpm and resolution.",
             steps=["Half step = 0.9&deg;; pulses per motor rev = 400.",
                    "Motor speed = 1000/400 = 2.5 rev/s = 150 rpm.",
                    "Output = 150/64 = 2.34 rpm; resolution = 0.9&deg;/64 = 0.014&deg;."],
             ans="Output = 2.34 rpm; resolution &asymp; 0.014&deg; per pulse."),
        dict(given="A DC motor on 24 V draws 2 A at 3000 rpm with R<sub>a</sub> = 1 &Omega;. "
                   "Find back-emf, torque constant if k<sub>t</sub> = 0.07 Nm/A, and torque.",
             steps=["E = V &minus; I R = 24 &minus; 2 &times; 1 = 22 V.",
                    "Torque = k<sub>t</sub> &times; I = 0.07 &times; 2 = 0.14 Nm.",
                    "k<sub>e</sub> = E/&omega; = 22 / (3000 &times; 2&pi;/60) = 0.070 V/(rad/s) &mdash; consistent "
                    "with k<sub>t</sub> in SI."],
             ans="E = 22 V, torque = 0.14 Nm."),
        dict(given="A three-phase motor drives a pump needing 7.5 kW at 1450 rpm. Find "
                   "rated torque and approximate full-load current at 400 V, 0.85 pf, "
                   "92 % efficiency.",
             steps=["T = 9550 &times; P(kW)/n(rpm) = 9550 &times; 7.5/1450 = 49.4 Nm.",
                    "P<sub>in</sub> = 7.5/0.92 = 8.15 kW.",
                    "I = P<sub>in</sub>/(3 &times; 400 &times; 0.85) = 8150/1020 = 8.0 A."],
             ans="T = 49.4 Nm; I<sub>FL</sub> &asymp; 8.0 A."),
    ],
    viva=[
        ("Why does an induction motor always run below synchronous speed?",
         "Torque is produced only by relative motion (slip) between rotating field and "
         "rotor bars; at synchronous speed there is no induced current and no torque."),
        ("What is pull-out torque?",
         "Maximum torque the motor can develop before it stalls; steppers lose steps if "
         "the load exceeds it."),
        ("How does a servo differ from a stepper?",
         "A servo closes a position/velocity loop with encoder feedback and can correct "
         "errors; a stepper moves open-loop per pulse and may stall silently if overloaded."),
        ("Why are steppers unsuitable at high speed?",
         "Torque falls rapidly with rate because inductance limits current rise; at high "
         "pps the motor behaves like a brake unless current-chopping drives are used."),
        ("What does a VFD do?",
         "Rectifies mains to DC and inverts it at variable frequency and voltage to control "
         "induction motor speed and torque smoothly."),
        ("Give one advantage of brushless DC over brushed DC motors.",
         "No brushes to wear or spark &mdash; longer life, less maintenance, better for "
         "hazardous or clean environments."),
    ],
    summ="Actuator motors span induction machines for general speed control, DC and "
         "brushless DC for wide range torque, steppers for open-loop positioning and "
         "servos for closed-loop precision. Slip, torque constants, gear reduction and "
         "drive choice connect the electrical input to the mechanical output, and correct "
         "sizing against load torque and duty cycle keeps the motor out of its stall and "
         "overheat zones.",
    spec=[
        ("Parameter", "3-ph induction", "Stepper (NEMA 17)", "Servo (with encoder)"),
        ("Speed control", "VFD, pole change", "Pulse rate (open loop)", "Closed-loop drive"),
        ("Position info", "None (open loop)", "Counted steps", "Encoder absolute/incremental"),
        ("Torque at 0 rpm", "High with VFD (150 %)", "Holds rated (until pull-out)", "Rated continuous"),
        ("Typical accuracy", "&mdash;", "3&ndash;5 % of step, no drift", "&plusmn;0.01&deg; to &plusmn;0.1&deg;"),
        ("Feedback", "Optional speed feedback", "None required", "Encoder mandatory"),
        ("Typical use", "Pumps, fans, conveyors", "3D printers, light CNC", "Robot arms, packaging axes"),
    ],
)

# ------------------------------------------------------------------ 22
EXTRAS[22] = dict(
    prose=[
        "Process automation exists because processes are too fast, too hot, too "
        "hazardous or too continuous for a human to sit and adjust by hand. The control "
        "loop simply copies what a careful operator would do &mdash; look at the "
        "measurement, compare with the target, turn the knob &mdash; and does it every few "
        "seconds without fatigue. Once this loop is closed on a PLC or DCS, the human "
        "role shifts from turning valves to managing alarms, recipes and maintenance, "
        "which is where real plants gain their productivity.",
        "The distinction between continuous and discrete control matters because the "
        "two need different mental models. Continuous control is about smooth "
        "proportional action, steady error and stability margins; discrete control is "
        "about interlocks, sequences and safe state machines where a step is either done "
        "or not. Most modern units are composite: a batch reactor runs a discrete "
        "sequence of valve operations while a continuous PID loop holds temperature "
        "inside each step. Recognising which layer a problem belongs to prevents "
        "mis-tuning a sequence issue or writing logic for a drift issue.",
    ],
    num=[
        dict(given="A level loop has set point 50 %, process variable 47 % and a "
                   "proportional-only controller with gain K<sub>c</sub> = 2.5 %/% and "
                   "bias of 40 %. Find controller output.",
             steps=["Error e = SP &minus; PV = 50 &minus; 47 = +3 %.",
                    "u = bias + K<sub>c</sub> e = 40 + 2.5 &times; 3 = 47.5 %.",
                    "Output drives valve to 47.5 % open (4&ndash;20 mA equivalent)."],
             ans="u = 47.5 %."),
        dict(given="A heat exchanger must hold outlet at 120 &deg;C with dead time of 15 s "
                   "and time constant 60 s. State the recommended controller scan time and "
                   "why.",
             steps=["Rule: scan at least 5&ndash;10&times; faster than the fastest loop element.",
                    "Fastest &tau; = dead time 15 s &rArr; sample every 1&ndash;3 s is ample; 1 s is "
                    "typical PLC analog task rate.",
                    "Too-fast scanning only wastes CPU; too-slow scanning adds phase lag."],
             ans="Scan every 1&ndash;3 s (1 s typical); faster than process dynamics, not faster than useful."),
        dict(given="An open-loop batch heater adds 40 kW to 2 m&sup3; of water (&rho; = 1000 "
                   "kg/m&sup3;, c<sub>p</sub> = 4.18 kJ/kg&deg;C) from 20 &deg;C. Find time to reach "
                   "80 &deg;C ignoring losses.",
             steps=["Mass = 2000 kg; energy needed = 2000 &times; 4.18 &times; (80 &minus; 20) = 501 600 kJ.",
                    "t = E/P = 501 600 / 40 = 12 540 s = 3.48 h.",
                    "Real time is longer due to losses &mdash; open loop never corrects the drift."],
             ans="t &asymp; 3.5 h ideal (longer with heat losses)."),
    ],
    viva=[
        ("What are the four elements of a process control loop?",
         "Measurement (sensor/transmitter), comparison (controller), final control element "
         "(valve, drive), and the process itself."),
        ("Difference between continuous and discrete state control?",
         "Continuous manipulates a variable proportionally over a range; discrete changes "
         "between fixed states (on/off, step sequences)."),
        ("What is open-loop control?",
         "Output is set without reference to the measured result &mdash; no correction of "
         "disturbances, used where the process is very predictable."),
        ("Why is feedback control preferred in plants?",
         "It automatically corrects unmeasured disturbances and model errors by acting on "
         "the measured error."),
        ("Name the signals carried on a typical analog loop.",
         "4&ndash;20 mA or 1&ndash;5 V measurement in, 4&ndash;20 mA output out, plus Hart or "
         "fieldbus digital overlay where used."),
        ("What is an interlock?",
         "A logic condition that prevents an unsafe action until safety criteria are "
         "satisfied &mdash; the discrete twin of feedback control."),
    ],
    summ="Process control systems close the loop between measurement, decision and "
         "action using sensors, controllers and final control elements. Continuous "
         "control handles smoothly varying quantities with feedback, discrete control "
         "handles states and sequences with logic, and composite systems combine both. "
         "Open loop is simpler but blind to disturbances; closed loop is the default "
         "wherever the process wanders.",
    spec=[
        ("Parameter", "Typical loop element", "Standard value"),
        ("Measurement", "Transmitter to controller", "4&ndash;20 mA / HART, fieldbus"),
        ("Controller", "PLC / DCS analog task", "Scan 0.1&ndash;1 s per loop"),
        ("Output", "To final control element", "4&ndash;20 mA, 0&ndash;10 V, discrete"),
        ("Final element", "Control valve, drive, heater", "Sized for max demand + margin"),
        ("Feedback", "PV compared with SP each scan", "Error drives corrective action"),
        ("Alarm layer", "High/low deviation alerts", "Independent of continuous action"),
        ("Safety layer", "SIS / interlocks", "Separate from basic control"),
    ],
)

# ------------------------------------------------------------------ 23
EXTRAS[23] = dict(
    prose=[
        "Process characteristics describe how stubborn the process is before any "
        "controller is chosen. Capacity tells you how much material or energy must move "
        "for a given change; dead time tells you how long you must wait before anything "
        "happens; lag tells you how slowly the response unfolds; and self-regulation "
        "tells you whether the process settles on its own after a disturbance. Together "
        "these four properties dominate the achievable control quality far more than the "
        "brand of the controller.",
        "The process reaction curve is the practical tool that exposes all of this. By "
        "giving the final control element a small deliberate step and charting the "
        "result, the engineer reads off gain, dead time and time constant directly, "
        "which then feed classical tuning rules. It also gives an early warning: if dead "
        "time is large compared with lag, even a perfect PID will be fighting physics, "
        "and the sensible fixes &mdash; shorter transport lines, faster elements, predictive "
        "control &mdash; are mechanical rather than software changes.",
    ],
    num=[
        dict(given="A well-stirred tank of time constant &tau; = 4 min receives a step "
                   "disturbance. Find how long until the temperature reaches 63.2 % of its "
                   "final change, and the % at 2 min.",
             steps=["First-order: y(t) = &Delta;y (1 &minus; e<sup>&minus;t/&tau;</sup>).",
                    "At t = &tau; = 4 min: y = 63.2 % of &Delta;y by definition.",
                    "At t = 2 min: 1 &minus; e<sup>&minus;0.5</sup> = 1 &minus; 0.607 = 39.3 %."],
             ans="63.2 % at 4 min; 39.3 % at 2 min."),
        dict(given="A process has dead time &theta; = 20 s and time constant &tau; = 80 s. "
                   "Classify difficulty and state the maximum useful controller gain "
                   "guideline &theta;/&tau;.",
             steps=["Ratio &theta;/&tau; = 20/80 = 0.25 &mdash; moderate dead time relative to lag.",
                    "Rule of thumb: if &theta;/&tau; &lt; 1, PID tuning works well; if much greater "
                    "than 1, control becomes oscillatory even at modest gain.",
                    "At 0.25, standard PID settings (e.g. Z&ndash;N) should hold comfortably."],
             ans="&theta;/&tau; = 0.25 &mdash; easily controllable with PID."),
        dict(given="A mixing tank holds 5000 L and inflow steps from 100 to 130 L/min with "
                   "outflow fixed at 100 L/min. Find initial rate of level rise and time to "
                   "gain 10 % level if cross-section gives 50 L per mm? (use 5000 L = 100 %).",
             steps=["Net accumulation = 130 &minus; 100 = 30 L/min.",
                    "10 % of 5000 L = 500 L.",
                    "t = 500 / 30 = 16.7 min &mdash; capacity buffers the disturbance linearly."],
             ans="Level rises 30 L/min; 10 % gain takes 16.7 min."),
    ],
    viva=[
        ("Define process lag.",
         "The exponential delay while the process variable moves toward its new steady "
         "value after a disturbance, characterised by time constant &tau; (63.2 % point)."),
        ("What is dead time and why is it the enemy of control?",
         "Pure transport or measurement delay with no output movement until it expires; "
         "it adds phase lag that forces lower controller gains to stay stable."),
        ("What does self-regulating mean?",
         "The process naturally finds a new equilibrium after a load change without "
         "integral action &mdash; e.g. a liquid level with fixed outlet characteristic."),
        ("Give an example of a non-self-regulating process.",
         "Liquid level in a tank with constant outflow: inflow step makes level run away "
         "until it overflows &mdash; the integrator process."),
        ("What is a process reaction curve test?",
         "A controlled step on the final element while recording PV; fitted to get gain, "
         "dead time and &tau; for tuning."),
        ("Why does large capacity improve controllability?",
         "Large capacity slows the process relative to disturbances, giving the "
         "controller more time to act with smaller corrections."),
    ],
    summ="Every process presents its own mix of capacity, dead time, lag and "
         "self-regulation. First-order responses reach 63.2 % of the change in one time "
         "constant, dead time adds pure delay measured in seconds or minutes, and the "
         "ratio &theta;/&tau; indicates how hard the loop will be to tune. Characterising "
         "the process before choosing controller settings turns tuning from trial and "
         "error into arithmetic.",
    spec=[
        ("Characteristic", "Symbol / unit", "Effect on control"),
        ("Process gain", "K (&Delta;PV/&Delta;manipulated)", "Sets required controller gain"),
        ("Dead time", "&theta; (s, min)", "Limits gain; causes oscillation if large"),
        ("Time constant", "&tau; (s, min)", "Response speed; 63.2 % at 1&tau;"),
        ("Capacity", "Volume, heat mass", "Buffers disturbances; slows PV"),
        ("Self-regulation", "Yes / no", "Whether P+I alone can hold set point"),
        ("Load change", "&Delta;disturbance", "Size of corrective action needed"),
        ("Reaction curve", "Step test record", "Source of K, &theta;, &tau; for tuning"),
    ],
)

# ------------------------------------------------------------------ 24
EXTRAS[24] = dict(
    prose=[
        "Control system parameters give precise names to ideas we already use "
        "informally. Error is simply the gap between wanted and actual, yet its "
        "definition &mdash; whether SP minus PV or PV minus SP &mdash; decides the sign of "
        "every controller output, so it must be fixed once and held consistently across "
        "the loop. Similarly, span versus range confuses students endlessly: range is "
        "what the instrument covers, span is the difference between its ends, and all "
        "percentage errors are quoted against one of the two, never against ambiguity.",
        "Cycling deserves special respect because it is the visible symptom of poor "
        "tuning or poor valve health. A loop that hunts around set point with growing or "
        "steady amplitude is telling the engineer something specific: gain too high, "
        "reset too fast, dead time too large, or a valve with stiction jumping in steps. "
        "Recording amplitude, period and whether the cycle follows a load change gives "
        "the starting clues for diagnosis before anyone touches a tuning knob.",
    ],
    num=[
        dict(given="A temperature transmitter spans 0&ndash;200 &deg;C with 4&ndash;20 mA "
                   "output. Find the mA at 75 &deg;C and the temperature represented by "
                   "13.6 mA.",
             steps=["% span = (75 &minus; 0)/(200 &minus; 0) &times; 100 = 37.5 %.",
                    "I = 4 + 0.16 &times; 75 = 4 + 12 = 16? No: 16 mA per 200 &deg;C &rArr; 16 &times; 0.375 = 6; I = 4 + 6 = 10 mA.",
                    "Reverse: &theta; = (13.6 &minus; 4)/16 &times; 200 = 120 &deg;C."],
             ans="75 &deg;C &rArr; 10 mA; 13.6 mA &rArr; 120 &deg;C."),
        dict(given="A level controller with proportional band of 40 % has an error of 5 %. "
                   "Find the change in controller output.",
             steps=["K = 100/PB = 100/40 = 2.5 %/%.",
                    "&Delta;u = K &times; e = 2.5 &times; 5 = 12.5 % of output range.",
                    "On a 4&ndash;20 mA output this is 0.16 &times; 12.5 &times; 16 mA scale &rArr; 2 mA change."],
             ans="&Delta;u = 12.5 % (2 mA on 4&ndash;20 mA)."),
        dict(given="A pressure loop cycles with amplitude &plusmn;0.8 bar at period 45 s "
                   "around a 10 bar set point. Express amplitude as % of set point and "
                   "comment on control time.",
             steps=["Amplitude % = 0.8/10 &times; 100 = 8 % of set point.",
                    "Period 45 s means the loop takes 45 s per oscillation &mdash; much longer "
                    "than dead time suggests gain/reset are too aggressive or valve "
                    "stiction exists.",
                    "Control time (settling into band) would be several periods &asymp; 2&ndash;3 min."],
             ans="Amplitude = 8 % of SP; period 45 s indicates mistuning or stiction."),
    ],
    viva=[
        ("Define error in a feedback loop.",
         "The algebraic difference between set point and process variable; conventionally "
         "e = SP &minus; PV so positive error calls for more output in heating/flow loops."),
        ("Differentiate range and span.",
         "Range is the complete set of values the instrument measures; span is URV minus "
         "LRV &mdash; e.g. range 0&ndash;200 &deg;C has span 200 &deg;C, but a range &minus;50 to +150 "
         "also has span 200."),
        ("What is proportional band?",
         "The percent change in input that drives output across its full range; it is the "
         "reciprocal view of gain: PB = 100/K."),
        ("What causes cycling in a loop?",
         "Excessive gain or reset, large dead time, valve stiction or backlash, or "
         "external periodic disturbance."),
        ("What does control time mean?",
         "Time taken after a disturbance for the process variable to return and stay "
         "within the required accuracy band."),
        ("Why is derivative action sometimes avoided?",
         "It amplifies measurement noise; on noisy loops (flow, level with surge) "
         "derivative can make output chatter worse than the original error."),
    ],
    summ="Error, range, span, proportional band, cycling and control time are the "
         "quantities used to describe loop performance in words and numbers. Percentage "
         "definitions must always name their denominator (span or reading), 4&ndash;20 mA "
         "scaling converts engineering values linearly, and cycling amplitude plus period "
         "provides the first diagnostic fingerprint when a loop misbehaves.",
    spec=[
        ("Parameter", "Definition", "Typical note"),
        ("Error e", "SP &minus; PV (or opposite &mdash; fix convention)", "Sign sets action direction"),
        ("Range", "Min to max measurable", "0&ndash;200 &deg;C, &minus;1 to 1 bar..."),
        ("Span", "URV &minus; LRV", "Denominator of % span error"),
        ("Proportional band", "100/K, % input for full output", "Small PB = high gain"),
        ("Offset", "Steady error with P-only action", "Removed by integral"),
        ("Cycling", "Sustained oscillation of PV", "Amplitude and period recorded"),
        ("Control time", "Time to re-enter tolerance band", "Spec after each load change"),
        ("Dead time", "&theta;, no response period", "Dominates difficulty"),
    ],
)

# ------------------------------------------------------------------ 25
EXTRAS[25] = dict(
    prose=[
        "Two-position control is the first loop everyone experiences: the home water "
        "heater that clicks on and off, the room thermostat, the refrigeration plant "
        "cycling its compressor. It needs only a comparator and a bit of differential gap "
        "to work, which is why it survives everywhere cost matters. The price is "
        "inherent oscillation &mdash; the process variable always swings between the two "
        "switch points &mdash; so the engineer's art is choosing a gap wide enough to "
        "protect the equipment yet narrow enough for the product to tolerate.",
        "Multi-position control sits between two-position and true proportional action. "
        "Three-position schemes, common on damper drives and some valve actuators, give "
        "an off band in the middle with fast drive above and below it, so small errors "
        "cost no energy while large errors get urgent attention. The same differential "
        "gap thinking applies: too narrow a gap causes hunting with mechanical wear; too "
        "wide a band lets the process wander far from target before anything happens.",
    ],
    num=[
        dict(given="A heater thermostat switches ON at 48 &deg;C and OFF at 52 &deg;C. "
                   "Find the differential gap, average temperature bias if the process "
                   "ramps linearly between extremes, and the cycle energy implication for "
                   "a 3 kW heater with 5 min on / 15 min off.",
             steps=["Differential gap = 52 &minus; 48 = 4 &deg;C (&plusmn;2 &deg;C around 50 &deg;C).",
                    "Set point usually marked at midpoint 50 &deg;C; mean follows mid-gap.",
                    "Duty = 5/(5+15) = 25 %; average heating power = 3 &times; 0.25 = 750 W."],
             ans="Gap = 4 &deg;C; average power = 750 W at 25 % duty."),
        dict(given="An ON-OFF controller drives a cooler with &plusmn;1.5 &deg;C differential "
                   "around 5 &deg;C set point. State switch points and the result of "
                   "narrowing the gap to &plusmn;0.2 &deg;C.",
             steps=["Switch points: cool ON at 6.5 &deg;C, OFF at 3.5 &deg;C (or ON at 3.5, OFF at 6.5 "
                    "depending on action).",
                    "Narrowing to &plusmn;0.2 &deg;C gives tighter control but cycles every few "
                    "seconds.",
                    "Short cycles stress compressor and contactor &mdash; minimum off-time "
                    "timers are mandatory."],
             ans="ON 6.5 / OFF 3.5 &deg;C; &plusmn;0.2 &deg;C would over-cycle equipment."),
        dict(given="A three-position damper drive has dead zone &plusmn;5 % around 50 %. "
                   "Find the no-action band and the drive output for error of +8 % if "
                   "each step drives 100 % in that direction.",
             steps=["Dead zone: 45 % to 55 % error-free region &rArr; no movement inside.",
                    "Error +8 % lies above 55 % upper edge &rArr; full drive one way.",
                    "Inside the band the drive holds position &mdash; energy-saving behaviour."],
             ans="No-action band = 45&ndash;55 %; +8 % error &rArr; full drive in opening direction."),
    ],
    viva=[
        ("What is differential gap?",
         "The difference between the switch-on and switch-off values of a two-position "
         "controller; it prevents excessively rapid cycling."),
        ("Why is a two-position loop always oscillatory?",
         "The output can only be fully on or off, so the process variable must swing "
         "between the two trip points; true steady state is impossible."),
        ("How is set point related to the switch points?",
         "It is normally the mid-gap value; switching occurs symmetrically above and "
         "below it unless the scheme is offset for load reasons."),
        ("Where is two-position control still preferred today?",
         "Domestic heating and refrigeration, small ovens, air compressors and any place "
         "where a proportional loop would be uneconomic."),
        ("What is the risk of too small a differential gap?",
         "Rapid cycling that burns out contactors, contactors and motors, and wears "
         "mechanical elements &mdash; the classic short-cycle failure."),
        ("How does three-position control differ?",
         "It adds a neutral middle state with drive in either direction, approximating "
         "proportional action with two thresholds."),
    ],
    summ="Discontinuous control switches output between fixed states: two-position with "
         "a differential gap for simple regulation, multi-position for graduated "
         "response. The differential gap sets the amplitude of the unavoidable "
         "oscillation and protects equipment from short cycling, while the midpoint "
         "defines the apparent set point. These loops are cheap, robust and perfectly "
         "adequate wherever a few degrees or a few percent of swing is acceptable.",
    spec=[
        ("Parameter", "Typical ON-OFF setting", "Remark"),
        ("Set point", "Mid-gap value", "Marked on dial or HMI"),
        ("Differential gap", "1&ndash;10 &deg;C or 2&ndash;10 % span", "Equipment protection + stability"),
        ("Output", "Discrete: energised / de-energised", "Relay, contactor, SSR"),
        ("Cycle period", "Minutes (process dependent)", "Too short = wear"),
        ("Oscillation amplitude", "&asymp; differential gap", "Inherent, cannot be tuned away"),
        ("Minimum off time", "Compressor/driver protection", "3&ndash;5 min typical for refrigeration"),
        ("Multi-position band", "&plusmn; dead zone + 2 drive states", "Damper and heater banks"),
    ],
)

# ------------------------------------------------------------------ 26
EXTRAS[26] = dict(
    prose=[
        "Proportional, integral and derivative actions are three different memories of "
        "the error. Proportional reacts to what is happening right now, integral "
        "remembers everything that has happened and keeps pushing until the last scrap of "
        "offset disappears, and derivative anticipates where the error is heading by "
        "looking at its slope. Using them together gives a controller that is at once "
        "responsive, accurate and well damped &mdash; provided each is given a sensible "
        "share rather than cranked to extremes.",
        "In the field the modes are recognised by their symptoms as much as by their "
        "equations. A loop with offset but steady readings needs more reset; a loop that "
        "oscillates with tight, fast cycles needs less gain or less reset; a loop that "
        "crawls toward set point and then overshoots slowly might benefit from a touch "
        "of rate &mdash; if its measurement is clean. This symptom-to-mode mapping lets "
        "engineers make first tuning moves quickly, before any formal tuning exercise "
        "with reaction curves or relay feedback.",
    ],
    num=[
        dict(given="A PID controller has K<sub>c</sub> = 2.0 %/%, T<sub>i</sub> = 0.5 min, "
                   "T<sub>d</sub> = 0.1 min. At one instant e = 3 %, de/dt = 5 %/min and "
                   "&int;e dt = 6 %&middot;min. Find controller output.",
             steps=["P term = K<sub>c</sub> e = 2.0 &times; 3 = 6 %.",
                    "I term = K<sub>c</sub> (&int;e dt)/T<sub>i</sub> = 2.0 &times; 6/0.5 = 24 %.",
                    "D term = K<sub>c</sub> T<sub>d</sub> de/dt = 2.0 &times; 0.1 &times; 5 = 1 %.",
                    "u = 6 + 24 + 1 = 31 % (plus bias if used)."],
             ans="u = 31 %."),
        dict(given="A P-only controller has K<sub>c</sub> = 4 %/% and output bias 30 %. After a "
                   "load change the plant needs 36 % output to hold set point. Find the "
                   "permanent offset.",
             steps=["In steady state the output must equal the demand: u = 36 %.",
                    "u = bias + K<sub>c</sub> e &rArr; 36 = 30 + 4e &rArr; e = (36 &minus; 30)/4 = 1.5 %.",
                    "This 1.5 % offset stays forever with P-only action; adding integral "
                    "action would drive it to zero."],
             ans="Offset = 1.5 % (integral action would remove it)."),
        dict(given="Reset rate is quoted as 3 repeats per minute. Find T<sub>i</sub> and the "
                   "integral contribution after 10 s of constant 2 % error with K<sub>c</sub> = 5.",
             steps=["T<sub>i</sub> = 60 s / 3 = 20 s = 0.333 min.",
                    "I contribution = K<sub>c</sub> &times; (e t)/T<sub>i</sub> = 5 &times; (2 &times; 10)/20 = 5 %.",
                    "After one full T<sub>i</sub> the integral term equals K<sub>c</sub> &times; e."],
             ans="T<sub>i</sub> = 20 s; integral term = 5 % after 10 s."),
    ],
    viva=[
        ("Why does proportional-only control leave an offset?",
         "Output must change to correct error, but a changed output requires some "
         "persistent error to sustain it &mdash; so error never reaches zero."),
        ("What does integral action do to stability?",
         "It adds phase lag and can cause slow hunting if too fast; its benefit is "
         "eliminating offset and rejecting steady load changes."),
        ("When is derivative action most useful?",
         "On slow, well-behaved processes with clean measurements &mdash; temperature, "
         "level &mdash; where anticipating the trend lets the controller brake early."),
        ("Define proportional band in terms of gain.",
         "PB (%) = 100/K<sub>c</sub>; a 10 % band means 10 % error swing moves output "
         "across its whole range."),
        ("What is reset windup and how is it prevented?",
         "Integral keeps accumulating while the output is saturated at a limit; anti-windup "
         "freezes or bleeds the integral when the output is clamped."),
        ("Why is derivative on measurement sometimes preferred?",
         "Differentiating PV instead of error avoids derivative kick on set-point steps "
         "and reacts only to real process movement."),
    ],
    summ="Continuous controller modes provide proportional action for immediate response, "
         "integral action for offset-free accuracy, and derivative action for damping. "
         "Gain and proportional band are reciprocal views of P strength; reset rate and "
         "T<sub>i</sub> set how fast offset vanishes; rate and T<sub>d</sub> set how much "
         "the controller anticipates. Symptom-based adjustment &mdash; offset, oscillation, "
         "slow crawl &mdash; guides the first tuning moves in the plant.",
    spec=[
        ("Mode", "Tuning parameter", "Main effect", "Main risk"),
        ("Proportional", "K<sub>c</sub> or PB", "Speed of immediate correction", "Offset if too small, oscillation if too big"),
        ("Integral", "T<sub>i</sub> or repeats/min", "Removes offset, rejects load change", "Windup, slow oscillation"),
        ("Derivative", "T<sub>d</sub> or rate", "Damps, reduces overshoot", "Amplifies noise"),
        ("Combined PID", "All three", "Fast, accurate, stable", "Retuning needed after process change"),
        ("Output", "4&ndash;20 mA to final element", "Continuous adjustment", "&mdash;"),
        ("Bias / initial", "Manual reset value", "Starting output before error acts", "Wrong bias causes start-up swing"),
    ],
)

# ------------------------------------------------------------------ 27
EXTRAS[27] = dict(
    prose=[
        "Composite modes exist because real processes rarely need only one flavour of "
        "action. PI is the workhorse of the process industries: proportional gives "
        "immediate push while integral quietly finishes the job, and the combination "
        "handles ordinary load changes with a single tuning pair. PD appears where "
        "integral would be too slow or would wind up against a hard limit &mdash; fast "
        "positioning axes and some pressure loops are typical. PID, with all three, is "
        "reserved for processes where lag is significant but dead time is manageable.",
        "Tuning philosophy matters as much as the mode chosen. Start with P alone until "
        "the loop responds promptly without sustained cycling, add just enough I to erase "
        "offset at a tolerable cost in phase, and introduce D only when the measurement "
        "is quiet enough to differentiate safely. The Ziegler&ndash;Nichols and Cohen&ndash;Coon "
        "tables give credible first guesses from known critical gain or reaction-curve "
        "data, but every plant loop should be documented with the final settings that "
        "were proven on the actual equipment, because theoretical first guesses are "
        "starting points, not finish lines.",
    ],
    num=[
        dict(given="Using ultimate-gain tuning (Ziegler&ndash;Nichols closed loop): a loop "
                   "oscillates with period P<sub>u</sub> = 40 s at K<sub>u</sub> = 6. Find "
                   "P, PI and PID settings.",
             steps=["P-only: K<sub>c</sub> = K<sub>u</sub>/2 = 3.",
                    "PI: K<sub>c</sub> = 0.45 K<sub>u</sub> = 2.7, T<sub>i</sub> = P<sub>u</sub>/1.2 = 33.3 s.",
                    "PID: K<sub>c</sub> = 0.6 K<sub>u</sub> = 3.6, T<sub>i</sub> = P<sub>u</sub>/2 = 20 s, "
                    "T<sub>d</sub> = P<sub>u</sub>/8 = 5 s."],
             ans="P: 3; PI: 2.7, 33 s; PID: 3.6, T<sub>i</sub> 20 s, T<sub>d</sub> 5 s."),
        dict(given="A PI controller with K<sub>c</sub> = 2 and T<sub>i</sub> = 30 s has been "
                   "in manual at 40 % output. Error has been +5 % for 90 s. Find the "
                   "bumpless-transfer output if the integrator is pre-loaded to match bias.",
             steps=["Integral pre-load = current output &minus; P term = 40 &minus; 2&times;5 = 30 %.",
                    "After auto entry the integral continues from 30 %, avoiding a bump.",
                    "Without pre-load, integral starts at 0 and output would jump to 40+ &mdash; "
                    "causing a process jerk."],
             ans="Pre-load integral to 30 % for bumpless transfer."),
        dict(given="A PID loop is tuned with K<sub>c</sub> = 4, T<sub>i</sub> = 40 s, "
                   "T<sub>d</sub> = 10 s. The process dead time later doubles (valve "
                   "stiction fix delayed). State the expected effect and first remedy.",
             steps=["More dead time erodes phase margin &rArr; loop becomes oscillatory at "
                    "same settings.",
                    "First remedy: reduce K<sub>c</sub> by 30&ndash;50 % and lengthen T<sub>i</sub>, "
                    "or reduce T<sub>d</sub> if rate was aggressive.",
                    "Better: fix the valve so dead time returns to original value, then "
                    "retune formally."],
             ans="Expect oscillation; reduce gain/reset or fix root cause, then retune."),
    ],
    viva=[
        ("Why prefer PI over P for most process loops?",
         "Integral eliminates the permanent offset of P-only action so the process lands "
         "exactly on set point after load changes."),
        ("When would you choose PD instead of PID?",
         "When integral is unnecessary (offset already small) or dangerous (windup at "
         "limits), but damping is needed &mdash; some fast position and pressure loops."),
        ("State the Ziegler&ndash;Nichols PID recipe from K<sub>u</sub> and P<sub>u</sub>.",
         "K<sub>c</sub> = 0.6 K<sub>u</sub>, T<sub>i</sub> = P<sub>u</sub>/2, T<sub>d</sub> = P<sub>u</sub>/8 &mdash; an aggressive "
         "starting point usually detuned in practice."),
        ("What is bumpless transfer?",
         "Pre-loading the integral term (or starting from matched output) so switching "
         "from manual to auto causes no output step."),
        ("How does cascade control improve on single-loop PID?",
         "A fast secondary loop is closed inside the primary loop, killing disturbances "
         "before they fully affect the main variable."),
        ("Give one modern alternative to classic PID.",
         "Model predictive control, fuzzy logic, or gain-scheduled PID &mdash; used when "
         "process nonlinearity or constraints exceed what fixed linear PID can handle."),
    ],
    summ="PI, PD and PID combine the three continuous actions to give offset-free, "
         "well-damped control of real processes. Ultimate-gain and reaction-curve methods "
         "produce credible first settings, anti-windup protects against saturation, and "
         "bumpless transfer protects against manual-auto transitions. The final "
         "deliverable of any tuning work is a documented, proven set of K<sub>c</sub>, "
         "T<sub>i</sub> and T<sub>d</sub> values stored with the loop &mdash; not memory alone.",
    spec=[
        ("Mode", "Best suited to", "Typical T<sub>i</sub>", "Typical T<sub>d</sub>"),
        ("PI", "Most process loops: flow, level, pressure, temperature", "0.2&ndash;5 min (fast loops to slow)", "&mdash;"),
        ("PD", "Fast loops where offset tolerable or windup risky", "&mdash;", "0.05&ndash;0.5 &times; dead time"),
        ("PID", "Large lag, moderate dead time (temp, batch)", "0.5&ndash;3 &times; &theta; or P<sub>u</sub>/2", "P<sub>u</sub>/8 or &theta;/4"),
        ("Z&ndash;N from K<sub>u</sub>, P<sub>u</sub>", "Universal first guess", "P<sub>u</sub>/2", "P<sub>u</sub>/8"),
        ("Z&ndash;N from reaction curve", "Open loop test data", "2&theta;", "&theta;/2"),
        ("Anti-windup", "Any loop with output limits", "Track on clamp", "Same"),
        ("Cascade", "Slow primary + fast secondary", "Outer slower than inner", "Inner usually PI"),
    ],
)
