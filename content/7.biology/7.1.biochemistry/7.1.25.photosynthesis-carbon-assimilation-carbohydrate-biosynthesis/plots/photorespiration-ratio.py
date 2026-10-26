"""Why photorespiration rises with temperature, and where C4 photosynthesis pays off.

Temperature dependence of the CO2 compensation point in the absence of day respiration (Gamma*), from
Bernacchi et al. (2001): Gamma*(T) = 42.75 exp[37.83 kJ/mol / R (1/298.15 K - 1/T)] umol/mol, on an
intercellular-gas basis. With phi = vo/vc = 2 Gamma*/Ci (Ci intercellular CO2 mole fraction):
A: phi and the fraction of carboxylated carbon lost again as CO2 (0.5 phi) for Ci = 280 umol/mol (open
stomata at 420 umol/mol ambient) and Ci = 200 umol/mol (partly closed stomata).
B: the aqueous specificity factor implied by Gamma*, S = 0.5 [O2]aq / Gamma*aq, and the ratio of dissolved
CO2 to O2 in water equilibrated with air (Henry constants 0.034 and 0.0013 M/atm at 25 C, temperature
coefficients 2400 and 1500 K): both fall with temperature.
C: ATP per net CO2 assimilated. C3: (3 + 3.5 phi) / (1 - 0.5 phi) (3 ATP per carboxylation, 3.5 per
oxygenation including refixation of NH3, and 0.5 CO2 lost per oxygenation). C4: 5 ATP per CO2 (2 for
PEP regeneration by PPDK), 5.5 with 20% leakage of CO2 from the bundle sheath; photorespiration in C4
leaves is neglected. The crossing marks the temperature above which the C4 pathway uses less ATP.
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
R = 8.314e-3
T = np.linspace(10, 40, 301)
Tk = T + 273.15


def arr(p25, h):
    return p25 * np.exp(h / R * (1 / 298.15 - 1 / Tk))


gstar = arr(42.75, 37.83)
kc = 0.034 * np.exp(2400 * (1 / Tk - 1 / 298.15))
ko = 0.0013 * np.exp(1500 * (1 / Tk - 1 / 298.15))
fig, ax = bio.canvas(27.0, 9.6)

a = charts.axes_at(ax, (1.9, 1.4, 6.2, 7.0))
for ci, tok in ((280, "dna"), (200, "negative")):
    phi = 2 * gstar / ci
    a.plot(T, phi, color=charts.line(tok), lw=2.0, label=rf"$v_\mathrm{{o}}/v_\mathrm{{c}}$, $C_\mathrm{{i}}$ = {ci}")
    a.plot(T, 0.5 * phi, color=charts.line(tok), lw=1.4, ls="--", label=rf"CO₂ lost / CO₂ fixed, $C_\mathrm{{i}}$ = {ci}")
a.set_xlim(10, 40)
a.set_ylim(0, 1.0)
charts.style_axes(a, "leaf temperature / °C", "ratio")
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.3, 9.4))

b = charts.axes_at(ax, (10.6, 1.4, 6.0, 7.0))
S = 0.5 * 0.2095 * ko / (gstar * 1e-6 * kc)
b.plot(T, S, color=charts.line("enzyme"), lw=2.0)
b.set_xlim(10, 40)
b.set_ylim(0, 220)
charts.style_axes(b, "temperature / °C", r"specificity factor $S_\mathrm{c/o}$")
b.text(11, 195, r"$S_\mathrm{c/o}$ (left axis)", fontsize=bio.core.FONT["tiny"], color=charts.line("enzyme"))
b2 = b.twinx()
b2.set_facecolor("none")
ratio = (420e-6 * kc) / (0.2095 * ko)
b2.plot(T, 1000 * ratio, color=charts.line("lipid"), lw=2.0, ls="-.")
b2.set_ylim(0, 110)
charts.style_axes(b2, None, "[CO₂]/[O₂] in water × 1000", box=True)
b2.spines["left"].set_visible(False)
b2.spines["top"].set_visible(False)
b2.text(39.5, 49, "[CO₂]/[O₂] (right axis)", fontsize=bio.core.FONT["tiny"], color=charts.line("lipid"),
        ha="right")
bio.panel(ax, "B", (9.0, 9.4))

c = charts.axes_at(ax, (20.0, 1.4, 6.4, 7.0))
for ci, tok in ((280, "dna"), (200, "negative")):
    phi = 2 * gstar / ci
    c.plot(T, (3 + 3.5 * phi) / (1 - 0.5 * phi), color=charts.line(tok), lw=2.0, label=rf"C3, $C_\mathrm{{i}}$ = {ci}")
c.axhline(5.0, color=charts.line("positive"), lw=2.0, label="C4 (no leakage)")
c.axhline(5.5, color=charts.line("positive"), lw=1.4, ls="--", label="C4, 20% leakage")
c.set_xlim(10, 40)
c.set_ylim(3, 9)
charts.style_axes(c, "temperature / °C", "ATP per net CO₂ fixed")
c.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (18.5, 9.4))
