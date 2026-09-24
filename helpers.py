# -*- coding: utf-8 -*-
"""
helpers.py  --  shared machinery for the handwritten notes site.

  * SKETCH   : SVG <defs> block with hand-drawn style electronic symbols
  * wire()   : draws a wire as a slightly wobbly polyline (sketch look)
  * svgfig() : wraps drawing markup into a responsive <figure>
  * page()   : wraps topic content into a full HTML document with nav/footer
"""

import os
import re

# --------------------------------------------------------------------- #
#  hand-drawn sketchy filter + symbol library (all symbols fit a 100x100
#  box and are placed with <use href="#id" x=".." y=".." width="100"/>)
# --------------------------------------------------------------------- #

SKETCH = """
<defs>
  <filter id="sk" x="-12%" y="-12%" width="124%" height="124%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="9" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="1.7" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <marker id="ah" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto">
    <path d="M1,1.5 L10,6 L1,10.5 Z" fill="#1b3a6b"/>
  </marker>
  <marker id="ahR" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto">
    <path d="M1,1.5 L10,6 L1,10.5 Z" fill="#c62828"/>
  </marker>
  <marker id="ahG" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto">
    <path d="M1,1.5 L10,6 L1,10.5 Z" fill="#1b7a3d"/>
  </marker>

  <!-- battery / DC supply -->
  <symbol id="bat" viewBox="0 0 100 100">
    <path d="M50,4 L50,32 M26,32 L74,32 M38,46 L62,46 M26,60 L74,60 M50,60 L50,96"
          fill="none" stroke="#1b3a6b" stroke-width="3.2" stroke-linecap="round"/>
    <text x="82" y="30" font-size="20" fill="#c62828" font-family="Caveat,cursive">+</text>
    <text x="80" y="78" font-size="22" fill="#123c8c" font-family="Caveat,cursive">&#8211;</text>
  </symbol>

  <!-- resistor (horizontal) -->
  <symbol id="res" viewBox="0 0 100 100">
    <path d="M0,50 L18,50 L24,32 L34,68 L44,32 L54,68 L64,32 L74,68 L80,50 L100,50"
          fill="none" stroke="#1b3a6b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
  </symbol>

  <!-- resistor (vertical) -->
  <symbol id="resv" viewBox="0 0 100 100">
    <path d="M50,0 L50,18 L32,24 L68,34 L32,44 L68,54 L32,64 L68,74 L50,82 L50,100"
          fill="none" stroke="#1b3a6b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
  </symbol>

  <!-- fixed capacitor -->
  <symbol id="cap" viewBox="0 0 100 100">
    <path d="M50,4 L50,38 M24,38 L76,38 M24,62 L76,62 M50,62 L50,96"
          fill="none" stroke="#1b3a6b" stroke-width="3.4" stroke-linecap="round"/>
  </symbol>

  <!-- polarised capacitor -->
  <symbol id="capv" viewBox="0 0 100 100">
    <path d="M50,4 L50,38 M24,38 L76,38 M24,62 L76,62 M50,62 L50,96"
          fill="none" stroke="#1b3a6b" stroke-width="3.4" stroke-linecap="round"/>
    <path d="M82,22 L82,34 M76,28 L88,28" stroke="#c62828" stroke-width="2.6" stroke-linecap="round"/>
  </symbol>

  <!-- inductor / coil -->
  <symbol id="ind" viewBox="0 0 100 100">
    <path d="M0,50 L14,50 M14,50 A9,9 0 0 1 32,50 A9,9 0 0 1 50,50 A9,9 0 0 1 68,50 A9,9 0 0 1 86,50 M86,50 L100,50"
          fill="none" stroke="#1b3a6b" stroke-width="3.2" stroke-linecap="round"/>
  </symbol>

  <!-- relay coil -->
  <symbol id="coil" viewBox="0 0 100 100">
    <rect x="18" y="14" width="64" height="72" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M32,64 A9,9 0 0 1 50,64 A9,9 0 0 1 68,64" fill="none" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M50,14 L50,0 M50,86 L50,100" stroke="#1b3a6b" stroke-width="3.2"/>
    <text x="50" y="46" text-anchor="middle" font-size="22" fill="#c62828" font-family="Caveat,cursive">K</text>
  </symbol>

  <!-- SPDT / change-over relay contact -->
  <symbol id="contact" viewBox="0 0 100 100">
    <circle cx="26" cy="50" r="6" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <circle cx="76" cy="28" r="6" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <circle cx="76" cy="72" r="6" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M32,48 L70,30" stroke="#1b3a6b" stroke-width="3" stroke-linecap="round"/>
    <path d="M82,28 L100,28 M82,72 L100,72 M0,50 L20,50" stroke="#1b3a6b" stroke-width="3"/>
  </symbol>

  <!-- SPST push button -->
  <symbol id="pb" viewBox="0 0 100 100">
    <path d="M0,50 L32,50 M68,50 L100,50" stroke="#1b3a6b" stroke-width="3.2"/>
    <circle cx="34" cy="50" r="5" fill="#fffdf3" stroke="#1b3a6b" stroke-width="2.6"/>
    <circle cx="66" cy="50" r="5" fill="#fffdf3" stroke="#1b3a6b" stroke-width="2.6"/>
    <path d="M30,38 L70,32" stroke="#1b3a6b" stroke-width="3" stroke-linecap="round"/>
    <path d="M50,20 L50,34" stroke="#c62828" stroke-width="2.8"/>
    <circle cx="50" cy="17" r="6" fill="none" stroke="#c62828" stroke-width="2.6"/>
  </symbol>

  <!-- switch (manual) -->
  <symbol id="sw" viewBox="0 0 100 100">
    <path d="M0,50 L30,50 M70,50 L100,50" stroke="#1b3a6b" stroke-width="3.2"/>
    <circle cx="32" cy="50" r="5" fill="#fffdf3" stroke="#1b3a6b" stroke-width="2.6"/>
    <circle cx="68" cy="50" r="5" fill="#fffdf3" stroke="#1b3a6b" stroke-width="2.6"/>
    <path d="M34,47 L67,29" stroke="#1b3a6b" stroke-width="3" stroke-linecap="round"/>
  </symbol>

  <!-- NTC thermistor -->
  <symbol id="therm" viewBox="0 0 100 100">
    <path d="M50,0 L50,18 L32,24 L68,34 L32,44 L68,54 L32,64 L68,74 L50,82 L50,100"
          fill="none" stroke="#1b3a6b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M14,88 L84,14" stroke="#c62828" stroke-width="2.8" stroke-linecap="round"/>
    <path d="M14,88 L26,84 M14,88 L19,76" stroke="#c62828" stroke-width="2.8" stroke-linecap="round"/>
    <text x="20" y="24" font-size="19" fill="#c62828" font-family="Caveat,cursive">&#8211;t&#176;</text>
  </symbol>

  <!-- LDR -->
  <symbol id="ldr" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="32" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M50,0 L50,18 M50,82 L50,100" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M30,62 L38,62 L42,48 L48,72 L54,44 L60,66 L64,56 L72,56"
          fill="none" stroke="#1b3a6b" stroke-width="2.6" stroke-linecap="round"/>
    <path d="M6,22 L30,42 M18,8 L44,30" stroke="#c62828" stroke-width="2.6"/>
    <path d="M30,42 L20,40 M30,42 L27,31 M44,30 L34,28 M44,30 L41,19"
          stroke="#c62828" stroke-width="2.6" stroke-linecap="round"/>
  </symbol>

  <!-- 3-pin sensor module (e.g. DHT11, MQ-2, soil, sound module) -->
  <symbol id="mod3" viewBox="0 0 100 100">
    <rect x="10" y="18" width="80" height="64" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M26,18 L26,2 M50,18 L50,2 M74,18 L74,2" stroke="#1b3a6b" stroke-width="3.2"/>
    <text x="26" y="14" text-anchor="middle" font-size="15" fill="#c62828" font-family="Caveat,cursive">VCC</text>
    <text x="50" y="14" text-anchor="middle" font-size="15" fill="#1b7a3d" font-family="Caveat,cursive">OUT</text>
    <text x="74" y="14" text-anchor="middle" font-size="15" fill="#123c8c" font-family="Caveat,cursive">GND</text>
    <text x="50" y="58" text-anchor="middle" font-size="22" fill="#1b3a6b" font-family="Caveat,cursive">SENSOR</text>
  </symbol>

  <!-- soil / moisture probe pair -->
  <symbol id="probe" viewBox="0 0 100 100">
    <path d="M28,6 L28,84 M72,6 L72,84" stroke="#1b3a6b" stroke-width="4" stroke-linecap="round"/>
    <path d="M20,84 L36,84 M64,84 L80,84" stroke="#1b3a6b" stroke-width="4" stroke-linecap="round"/>
    <path d="M14,92 Q50,80 86,92" fill="none" stroke="#8a5a2b" stroke-width="3"/>
    <text x="50" y="30" text-anchor="middle" font-size="17" fill="#8a5a2b" font-family="Caveat,cursive">soil</text>
  </symbol>

  <!-- generic transducer / two-terminal block -->
  <symbol id="block" viewBox="0 0 100 100">
    <rect x="12" y="24" width="76" height="52" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M0,50 L12,50 M88,50 L100,50" stroke="#1b3a6b" stroke-width="3.2"/>
    <text x="50" y="56" text-anchor="middle" font-size="19" fill="#1b3a6b" font-family="Caveat,cursive">XDCR</text>
  </symbol>

  <!-- op-amp -->
  <symbol id="opamp" viewBox="0 0 100 100">
    <path d="M12,10 L88,50 L12,90 Z" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3.2" stroke-linejoin="round"/>
    <path d="M88,50 L100,50 M0,30 L12,30 M0,70 L12,70" stroke="#1b3a6b" stroke-width="3.2"/>
    <text x="24" y="36" font-size="24" fill="#123c8c" font-family="Caveat,cursive">+</text>
    <text x="24" y="80" font-size="26" fill="#c62828" font-family="Caveat,cursive">&#8211;</text>
  </symbol>

  <!-- ground -->
  <symbol id="gnd" viewBox="0 0 100 100">
    <path d="M50,0 L50,44 M18,46 L82,46 M30,60 L70,60 M42,74 L58,74"
          fill="none" stroke="#1b3a6b" stroke-width="3.2" stroke-linecap="round"/>
  </symbol>

  <!-- node / junction dot -->
  <symbol id="node" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="12" fill="#1b3a6b"/>
  </symbol>

  <!-- SCR -->
  <symbol id="scr" viewBox="0 0 100 100">
    <path d="M50,4 L50,26 M50,74 L50,96" stroke="#1b3a6b" stroke-width="3.4"/>
    <path d="M28,26 L72,26 M28,74 L72,74" stroke="#1b3a6b" stroke-width="3.4"/>
    <path d="M34,26 L34,74 L66,50 Z" fill="none" stroke="#1b3a6b" stroke-width="3" stroke-linejoin="round"/>
    <path d="M66,62 L88,62 L88,84" fill="none" stroke="#c62828" stroke-width="2.8"/>
    <text x="12" y="20" font-size="19" fill="#123c8c" font-family="Caveat,cursive">A</text>
    <text x="60" y="20" font-size="19" fill="#123c8c" font-family="Caveat,cursive">K</text>
    <text x="84" y="98" font-size="19" fill="#c62828" font-family="Caveat,cursive">G</text>
  </symbol>

  <!-- TRIAC -->
  <symbol id="triac" viewBox="0 0 100 100">
    <path d="M50,4 L50,24 M50,76 L50,96" stroke="#1b3a6b" stroke-width="3.4"/>
    <path d="M26,24 L74,24 M26,76 L74,76" stroke="#1b3a6b" stroke-width="3.4"/>
    <path d="M34,24 L34,58 L66,24 Z" fill="none" stroke="#1b3a6b" stroke-width="3" stroke-linejoin="round"/>
    <path d="M34,76 L34,44 L66,76 Z" fill="none" stroke="#1b3a6b" stroke-width="3" stroke-linejoin="round"/>
    <path d="M62,66 L86,66 L86,88" fill="none" stroke="#c62828" stroke-width="2.8"/>
    <text x="6" y="18" font-size="17" fill="#123c8c" font-family="Caveat,cursive">MT2</text>
    <text x="6" y="94" font-size="17" fill="#123c8c" font-family="Caveat,cursive">MT1</text>
    <text x="82" y="100" font-size="19" fill="#c62828" font-family="Caveat,cursive">G</text>
  </symbol>

  <!-- N-channel MOSFET -->
  <symbol id="nmos" viewBox="0 0 100 100">
    <path d="M6,50 L36,50" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M40,20 L40,80" stroke="#1b3a6b" stroke-width="4"/>
    <path d="M50,20 L50,40 M50,60 L50,80" stroke="#1b3a6b" stroke-width="3.4"/>
    <path d="M50,50 L74,50 L74,4" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M50,30 L74,30 L74,4" fill="none" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M74,66 L74,96 L50,70" fill="none" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M58,60 L70,66 L58,72 Z" fill="#1b3a6b"/>
    <text x="70" y="18" font-size="18" fill="#123c8c" font-family="Caveat,cursive">D</text>
    <text x="72" y="94" font-size="18" fill="#123c8c" font-family="Caveat,cursive">S</text>
    <text x="0" y="42" font-size="18" fill="#c62828" font-family="Caveat,cursive">G</text>
  </symbol>

  <!-- diode -->
  <symbol id="diode" viewBox="0 0 100 100">
    <path d="M50,4 L50,30 M50,70 L50,96" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M32,30 L68,30 L50,64 Z" fill="#1b3a6b" stroke="#1b3a6b" stroke-width="2"/>
    <path d="M30,66 L70,66" stroke="#1b3a6b" stroke-width="3.4"/>
  </symbol>

  <!-- lamp / bulb -->
  <symbol id="lamp" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="30" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M30,30 L70,70 M70,30 L30,70" stroke="#1b3a6b" stroke-width="2.6"/>
    <path d="M50,4 L50,20 M50,80 L50,96" stroke="#1b3a6b" stroke-width="3.2"/>
  </symbol>

  <!-- heater element -->
  <symbol id="heater" viewBox="0 0 100 100">
    <rect x="16" y="28" width="68" height="44" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M24,58 Q31,38 38,58 Q45,78 52,58 Q59,38 66,58 Q70,68 76,58"
          fill="none" stroke="#c62828" stroke-width="2.8"/>
    <path d="M0,50 L16,50 M84,50 L100,50" stroke="#1b3a6b" stroke-width="3.2"/>
  </symbol>

  <!-- DC motor -->
  <symbol id="dcmt" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="32" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3.2"/>
    <text x="50" y="60" text-anchor="middle" font-size="30" fill="#1b3a6b" font-family="Caveat,cursive">M</text>
    <path d="M50,4 L50,18 M50,82 L50,96" stroke="#1b3a6b" stroke-width="3.2"/>
  </symbol>

  <!-- servo motor (3 wires) -->
  <symbol id="servo" viewBox="0 0 100 100">
    <rect x="14" y="26" width="72" height="52" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <circle cx="50" cy="26" r="11" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M26,78 L26,94 M50,78 L50,94 M74,78 L74,94" stroke="#1b3a6b" stroke-width="3"/>
    <text x="26" y="62" text-anchor="middle" font-size="15" fill="#c62828" font-family="Caveat,cursive">V</text>
    <text x="50" y="62" text-anchor="middle" font-size="15" fill="#b45309" font-family="Caveat,cursive">S</text>
    <text x="74" y="62" text-anchor="middle" font-size="15" fill="#123c8c" font-family="Caveat,cursive">G</text>
  </symbol>

  <!-- stepper motor (4 leads) -->
  <symbol id="step" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="30" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3.2"/>
    <text x="50" y="56" text-anchor="middle" font-size="17" fill="#1b3a6b" font-family="Caveat,cursive">STP</text>
    <path d="M8,20 L28,34 M8,80 L28,66 M92,20 L72,34 M92,80 L72,66"
          stroke="#1b3a6b" stroke-width="3" stroke-linecap="round"/>
  </symbol>

  <!-- 3-phase induction motor -->
  <symbol id="acmt" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="30" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M30,56 Q38,38 46,56 Q54,74 62,56" fill="none" stroke="#1b3a6b" stroke-width="2.6"/>
    <path d="M6,30 L26,38 M6,70 L26,62 M6,50 L20,50" stroke="#1b3a6b" stroke-width="3"/>
    <text x="50" y="26" text-anchor="middle" font-size="16" fill="#c62828" font-family="Caveat,cursive">3&#966;</text>
  </symbol>

  <!-- solenoid with plunger -->
  <symbol id="solenoid" viewBox="0 0 100 100">
    <path d="M0,34 L14,34 M14,34 A9,9 0 0 1 32,34 A9,9 0 0 1 50,34 A9,9 0 0 1 68,34 A9,9 0 0 1 86,34 M86,34 L100,34"
          fill="none" stroke="#1b3a6b" stroke-width="3.2"/>
    <rect x="24" y="56" width="46" height="18" rx="6" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M70,65 L96,65" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M80,52 L98,65 L80,78" fill="none" stroke="#c62828" stroke-width="2.6"/>
    <path d="M0,65 L24,65" stroke="#1b3a6b" stroke-width="3"/>
  </symbol>

  <!-- strain gauge grid on a bar -->
  <symbol id="gauge" viewBox="0 0 100 100">
    <rect x="14" y="14" width="72" height="72" rx="6" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M26,74 L26,30 L40,30 L40,70 L54,70 L54,30 L68,30 L68,70 L74,70"
          fill="none" stroke="#c62828" stroke-width="2.6"/>
    <path d="M26,74 L14,84 M74,70 L86,84" stroke="#1b3a6b" stroke-width="2.6"/>
  </symbol>

  <!-- microcontroller / Arduino block -->
  <symbol id="mcu" viewBox="0 0 100 100">
    <rect x="8" y="8" width="84" height="84" rx="10" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3.2"
          stroke-dasharray="12 7"/>
    <text x="50" y="48" text-anchor="middle" font-size="20" fill="#1b3a6b" font-family="Caveat,cursive">&#181;C /</text>
    <text x="50" y="70" text-anchor="middle" font-size="18" fill="#1b3a6b" font-family="Caveat,cursive">Arduino</text>
  </symbol>

  <!-- DAC / converter block -->
  <symbol id="dac" viewBox="0 0 100 100">
    <rect x="10" y="24" width="80" height="52" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <text x="50" y="58" text-anchor="middle" font-size="24" fill="#1b3a6b" font-family="Caveat,cursive">DAC</text>
    <path d="M0,50 L10,50 M90,50 L100,50" stroke="#1b3a6b" stroke-width="3.2"/>
  </symbol>

  <!-- amplifier block -->
  <symbol id="amp" viewBox="0 0 100 100">
    <rect x="10" y="24" width="80" height="52" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <text x="50" y="58" text-anchor="middle" font-size="24" fill="#1b3a6b" font-family="Caveat,cursive">A</text>
    <path d="M0,50 L10,50 M90,50 L100,50" stroke="#1b3a6b" stroke-width="3.2"/>
  </symbol>

  <!-- ADC block -->
  <symbol id="adc" viewBox="0 0 100 100">
    <rect x="10" y="24" width="80" height="52" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <text x="50" y="58" text-anchor="middle" font-size="22" fill="#1b3a6b" font-family="Caveat,cursive">ADC</text>
    <path d="M0,50 L10,50 M90,50 L100,50" stroke="#1b3a6b" stroke-width="3.2"/>
  </symbol>

  <!-- comparator with hysteresis (schmitt) -->
  <symbol id="comp" viewBox="0 0 100 100">
    <path d="M12,10 L88,50 L12,90 Z" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3.2" stroke-linejoin="round"/>
    <path d="M88,50 L100,50 M0,30 L12,30 M0,70 L12,70" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M30,58 L44,58 L44,44 L58,44" fill="none" stroke="#c62828" stroke-width="2.4"/>
    <path d="M24,36 L38,36 L38,22 L52,22" fill="none" stroke="#123c8c" stroke-width="2.4"/>
  </symbol>

  <!-- potentiometer (vertical, wiper to the left) -->
  <symbol id="potv" viewBox="0 0 100 100">
    <path d="M50,4 L50,20 L32,26 L68,36 L32,46 L68,56 L32,66 L68,76 L50,82 L50,96"
          fill="none" stroke="#1b3a6b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M6,50 L30,50" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M22,42 L32,50 L22,58" fill="none" stroke="#1b3a6b" stroke-width="3" stroke-linejoin="round"/>
  </symbol>

  <!-- speaker / buzzer -->
  <symbol id="spk" viewBox="0 0 100 100">
    <path d="M14,36 L34,36 L56,18 L56,82 L34,64 L14,64 Z" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M0,50 L14,50" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M68,32 Q80,50 68,68 M78,22 Q96,50 78,78" fill="none" stroke="#c62828" stroke-width="2.6"/>
  </symbol>

  <!-- microphone -->
  <symbol id="mic" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="30" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <text x="50" y="60" text-anchor="middle" font-size="24" fill="#1b3a6b" font-family="Caveat,cursive">M</text>
    <path d="M0,50 L20,50" stroke="#1b3a6b" stroke-width="3.2"/>
  </symbol>

  <!-- LVDT -->
  <symbol id="lvdt" viewBox="0 0 100 100">
    <rect x="6" y="22" width="88" height="56" rx="8" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M14,34 L30,34 M14,50 L30,50 M14,66 L30,66" stroke="#1b3a6b" stroke-width="2.6"/>
    <path d="M70,34 L86,34 M70,50 L86,50 M70,66 L86,66" stroke="#1b3a6b" stroke-width="2.6"/>
    <path d="M30,22 L30,78 M70,22 L70,78" stroke="#1b3a6b" stroke-width="3"/>
    <rect x="38" y="30" width="24" height="40" rx="5" fill="#fffdf3" stroke="#c62828" stroke-width="2.8"/>
    <path d="M50,8 L50,30" stroke="#c62828" stroke-width="2.8"/>
    <text x="50" y="94" text-anchor="middle" font-size="16" fill="#1b3a6b" font-family="Caveat,cursive">core</text>
  </symbol>

  <!-- bellows -->
  <symbol id="bellows" viewBox="0 0 100 100">
    <path d="M12,26 L26,40 L26,26 L40,40 L40,26 L54,40 L54,26 L68,40 L68,26 L82,40 L82,26"
          fill="none" stroke="#1b3a6b" stroke-width="2.8"/>
    <path d="M12,74 L26,60 L26,74 L40,60 L40,74 L54,60 L54,74 L68,60 L68,74 L82,60 L82,74"
          fill="none" stroke="#1b3a6b" stroke-width="2.8"/>
    <path d="M12,26 L12,74 M82,26 L82,74" stroke="#1b3a6b" stroke-width="2.8"/>
    <path d="M82,50 L100,50" stroke="#1b3a6b" stroke-width="3"/>
    <text x="47" y="56" text-anchor="middle" font-size="15" fill="#c62828" font-family="Caveat,cursive">P</text>
  </symbol>

  <!-- Bourdon tube (C type) -->
  <symbol id="bourdon" viewBox="0 0 100 100">
    <path d="M20,80 A40,40 0 1 1 78,30" fill="none" stroke="#1b3a6b" stroke-width="4"/>
    <path d="M20,80 L8,92" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M78,30 L94,22" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M78,30 L94,40" stroke="#c62828" stroke-width="2.6"/>
    <text x="18" y="72" font-size="16" fill="#1b3a6b" font-family="Caveat,cursive">P</text>
  </symbol>

  <!-- float and tank -->
  <symbol id="float" viewBox="0 0 100 100">
    <path d="M14,14 L14,90 L86,90 L86,14" fill="none" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M14,62 Q32,54 50,62 Q68,70 86,62 L86,90 L14,90 Z" fill="#cfe6f7" opacity=".75"/>
    <circle cx="50" cy="60" r="13" fill="#fffdf3" stroke="#c62828" stroke-width="3"/>
    <path d="M50,47 L50,14" stroke="#1b3a6b" stroke-width="2.6" stroke-dasharray="6 5"/>
  </symbol>

  <!-- orifice plate in a pipe -->
  <symbol id="orifice" viewBox="0 0 100 100">
    <path d="M0,30 L100,30 M0,70 L100,70" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M50,30 L50,44 M50,56 L50,70" stroke="#c62828" stroke-width="3.4"/>
    <path d="M18,30 L18,12 M82,30 L82,12" stroke="#1b3a6b" stroke-width="2.6"/>
    <text x="12" y="10" font-size="16" fill="#123c8c" font-family="Caveat,cursive">P&#8321;</text>
    <text x="76" y="10" font-size="16" fill="#c62828" font-family="Caveat,cursive">P&#8322;</text>
    <path d="M8,50 L38,50" stroke="#1b7a3d" stroke-width="2.8" marker-end="url(#ahG)"/>
  </symbol>

  <!-- globe control valve with actuator -->
  <symbol id="valve" viewBox="0 0 100 100">
    <path d="M0,74 L32,74 L50,58 L68,74 L100,74" fill="none" stroke="#1b3a6b" stroke-width="3.2"/>
    <path d="M32,74 L68,74 L50,58 Z" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M50,58 L50,34" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M26,34 L74,34 L74,10 L26,10 Z" fill="#fffdf3" stroke="#1b3a6b" stroke-width="3"/>
    <text x="50" y="28" text-anchor="middle" font-size="15" fill="#1b3a6b" font-family="Caveat,cursive">diaphragm</text>
    <path d="M62,46 L82,46" stroke="#c62828" stroke-width="2.6"/>
    <text x="60" y="42" font-size="15" fill="#c62828" font-family="Caveat,cursive">signal</text>
  </symbol>

  <!-- relay driver block (BJT + diode + base resistor) -->
  <symbol id="drv" viewBox="0 0 100 100">
    <path d="M4,42 L20,42" stroke="#1b3a6b" stroke-width="3"/>
    <path d="M10,42 L14,34 L18,50 L22,34" fill="none" stroke="#1b3a6b" stroke-width="2.6"/>
    <circle cx="42" cy="46" r="22" fill="#fffdf3" stroke="#1b3a6b" stroke-width="2.8"/>
    <path d="M20,42 L30,46 M36,36 L52,30 M36,58 L52,64" stroke="#1b3a6b" stroke-width="2.8"/>
    <path d="M44,40 L52,30 L48,30 M52,30 L52,34" fill="none" stroke="#1b3a6b" stroke-width="2.4"/>
    <path d="M52,30 L52,12 M52,64 L52,86" stroke="#1b3a6b" stroke-width="2.8"/>
    <path d="M52,12 L74,12 L74,26 M74,40 L74,54" stroke="#1b3a6b" stroke-width="2.8"/>
    <path d="M66,26 L82,26 L74,40 Z" fill="#c62828" opacity=".85"/>
    <rect x="62" y="54" width="24" height="16" rx="4" fill="#fffdf3" stroke="#1b3a6b" stroke-width="2.6"/>
    <path d="M74,70 L74,86" stroke="#1b3a6b" stroke-width="2.8"/>
    <text x="74" y="66" text-anchor="middle" font-size="13" fill="#1b3a6b" font-family="Caveat,cursive">K</text>
  </symbol>
</defs>
"""


def wire(points, **kw):
    """points = [(x,y), ...]  ->  sketchy polyline (auto arrow head option)."""
    style = ("fill:none;stroke:#1b3a6b;stroke-width:%s;stroke-linecap:round;stroke-linejoin:round"
             % kw.get("w", 3))
    if kw.get("color"):
        style = style.replace("#1b3a6b", kw["color"])
    if kw.get("dash"):
        style += ";stroke-dasharray:%s" % kw["dash"]
    marker = ""
    if kw.get("arrow"):
        m = {"blue": "ah", "red": "ahR", "green": "ahG"}.get(kw["arrow"], "ah")
        marker = ' marker-end="url(#%s)"' % m
    pts = " ".join("%g,%g" % (float(x), float(y)) for x, y in points)
    return '<polyline points="%s" style="%s"%s/>' % (pts, style, marker)


def use(sid, x, y, w=100, h=100):
    return '<use href="#%s" x="%g" y="%g" width="%g" height="%g"/>' % (sid, x, y, w, h)


def node(x, y, r=10):
    return '<use href="#node" x="%g" y="%g" width="%g" height="%g"/>' % (x - r / 2, y - r / 2, r, r)


def t(x, y, s, size=18, fill="#1b3a6b", anchor="middle", family="Caveat,cursive", weight="normal"):
    return ('<text x="%g" y="%g" font-size="%g" fill="%s" text-anchor="%s" '
            'font-family="%s" font-weight="%s">%s</text>'
            % (x, y, size, fill, anchor, family, weight, s))


# HTML named entities are NOT part of XML, so inside an <svg> they must be
# written as numeric character references.  Browsers forgive this, but strict
# SVG/XML parsers (and some validators, e-book readers and converters) do not.
_ENTITIES = {
    "amp": 38, "lt": 60, "gt": 62, "quot": 34, "apos": 39, "nbsp": 160,
    "deg": 176, "plusmn": 177, "micro": 181, "sup2": 178, "sup3": 179,
    "times": 215, "minus": 8722, "sdot": 8901, "radic": 8730, "prop": 8733,
    "int": 8747, "asymp": 8776, "ne": 8800, "le": 8804, "ge": 8805,
    "ndash": 8211, "mdash": 8212, "lsquo": 8216, "rsquo": 8217,
    "ldquo": 8220, "rdquo": 8221, "dagger": 8224, "bull": 8226,
    "hellip": 8230, "prime": 8242, "larr": 8592, "uarr": 8593,
    "rarr": 8594, "darr": 8595, "harr": 8596, "part": 8706,
    "Delta": 916, "Sigma": 931, "Omega": 937, "alpha": 945, "beta": 946,
    "gamma": 947, "delta": 948, "epsilon": 949, "zeta": 950, "eta": 951,
    "theta": 952, "lambda": 955, "mu": 956, "pi": 960, "rho": 961,
    "sigma": 963, "tau": 964, "phi": 966, "chi": 967, "psi": 968,
    "omega": 969, "rArr": 8658, "lArr": 8656, "hArr": 8660,
}
_ENT_RE = re.compile(r"&([A-Za-z][A-Za-z0-9]*);")


def _to_numeric(match):
    name = match.group(1)
    if name in _ENTITIES:
        return "&#%d;" % _ENTITIES[name]
    raise ValueError("SVG contains the entity &%s; which is not valid XML - "
                     "use the numeric form &#..; instead" % name)


def safe_svg(text):
    """make a piece of SVG markup strict-XML safe"""
    return _ENT_RE.sub(_to_numeric, text)


def _n(v):
    return str(int(v)) if float(v) == int(v) else ("%g" % v)


def svgfig(inner, caption, w=760, h=440, bg="#fffef7"):
    """wrap drawing markup into a responsive <figure>.

    NB: plain % / .format formatting is not used here on purpose - SKETCH
    contains literal percent signs (filter region x="-12%") and curly braces
    (CSS style blocks) which would break both.
    """
    label = caption.replace('"', "'").replace("&", " and ")
    return (
        '\n<figure class="fig">\n'
        '<svg viewBox="0 0 ' + _n(w) + ' ' + _n(h) + '" role="img" aria-label="' + label + '" '
        'style="background:' + bg + ';border-radius:12px">\n'
        + SKETCH + '\n' + safe_svg(inner) + '\n</svg>\n'
        '<figcaption>' + caption + '</figcaption>\n</figure>\n'
    )


def g(inner):
    """wrap inner markup in the sketch filter group"""
    return '<g filter="url(#sk)">\n%s\n</g>' % inner


# --------------------------------------------------------------------- #
#  page assembly
# --------------------------------------------------------------------- #

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Sensors &amp; Process Control Systems Notes</title>
<meta name="description" content="Handwritten study notes on {title} - Sensors and Process Control Systems.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&amp;family=Patrick+Hand&amp;display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23fdf9ec'/%3E%3Cpath d='M8 20h12l5-10 8 22 6-16 5 10h12' fill='none' stroke='%23123c8c' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M8 46h48' stroke='%23c62828' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="stylesheet" href="css/notes.css">
</head>
<body>
<div class="paper">
"""

TOPBAR = """  <div class="topbar">
    <span class="brand">Sensors &amp; Process Control</span>
    <button class="btn" onclick="ink('brown')" title="blue-black ink">Blue</button>
    <button class="btn" onclick="ink('red')" title="red pen">Red</button>
    <button class="btn" onclick="ink('green')" title="green pen">Green</button>
    <button class="btn" onclick="window.print()" title="print this note">Print</button>
    <a class="btn" href="index.html" style="text-decoration:none">Index</a>
  </div>
"""

SCRIPT = """<script>
/* pen-colour switch: recolours the body text only, diagrams keep their own ink */
function ink(c){
  var m = {brown:'#4a3728', red:'#9b1c1c', green:'#155724'};
  document.body.style.color = m[c] || m.brown;
  var bs = document.querySelectorAll('.btn');
  for (var i = 0; i < bs.length; i++) { bs[i].classList.remove('active'); }
  event.currentTarget.classList.add('active');
}
</script>
"""


def page(slug, unit, title, subtitle, body, prev=None, nxt=None, extra_head=""):
    nav = ['<div class="pager">']
    if prev:
        nav.append('<a href="%s">&#8592; %s</a>' % (prev[0], prev[1]))
    else:
        nav.append('<span></span>')
    nav.append('<a class="home" href="index.html">&#8962; Index</a>')
    if nxt:
        nav.append('<a href="%s">%s &#8594;</a>' % (nxt[0], nxt[1]))
    else:
        nav.append('<span></span>')
    nav.append('</div>')

    sub = '<span class="sub">%s</span>' % subtitle if subtitle else ""
    html = HEAD.format(title=title)
    html += TOPBAR
    html += ('  <span class="unit-tag">%s</span>\n'
             '  <h1 class="title">%s%s</h1>\n  <div class="rule"></div>\n'
             % (unit, title, sub))
    html += body
    html += "\n" + "\n".join(nav)
    html += ('\n  <p class="sig">~ handwritten notes &middot; Sensors &amp; Process Control Systems '
             '&middot; save &amp; revise daily ~</p>\n')
    html += "</div>\n" + SCRIPT + "</body>\n</html>\n"
    return html
