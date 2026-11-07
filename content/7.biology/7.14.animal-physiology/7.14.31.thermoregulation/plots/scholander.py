"""Scholander-Irving model of endotherm heat production against ambient temperature.

Below the lower critical temperature (LCT) heat production must equal dry heat loss, M = C (Tb - Ta), a line that
extrapolates to M = 0 at Ta = Tb; within the thermoneutral zone M = BMR and conductance C is adjusted by
vasomotion, piloerection and posture; above the upper critical temperature (UCT) active evaporative cooling costs
energy. With M in units of BMR, C = BMR/(Tb - LCT), so better insulation (smaller C) gives a shallower slope and a
lower LCT. A: three illustrative animals (LCT 27, 10 and -40 C; Tb 37-38 C), the last like Scholander's arctic fox.
B: allometric prediction Tb - LCT = BMR/C with BMR = 3.4 M^0.75 W and wet conductance C = 1.0 M^-0.5 mL O2 per g h C
(Herreid and Kessel 1967; 20.1 J per mL O2), i.e. Tb - LCT proportional to M^0.25, compared with two outliers.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 4.6))
ta = np.linspace(-60, 45, 400)
for lct, ucr, tb, c, lab in ((27, 33, 37, P.edge("blood"), "tropical mammal (LCT 27 $^\\circ$C)"),
                             (10, 30, 38, P.edge("animal"), "temperate mammal (LCT 10 $^\\circ$C)"),
                             (-40, 25, 38, P.edge("dna"), "arctic fox (LCT $-40$ $^\\circ$C)")):
    m = np.where(ta < lct, (tb - ta) / (tb - lct), 1.0)
    m = np.where(ta > ucr, 1 + 0.12 * (ta - ucr), m)
    ax.plot(ta, m, color=c, lw=2.2, label=lab)
    sel = ta > lct
    ax.plot(ta[sel & (ta < tb)], ((tb - ta) / (tb - lct))[sel & (ta < tb)], color=c, lw=0.9, ls=":")
    ax.plot([lct], [1], "o", color=c, ms=5)
ax.annotate("lower critical\ntemperature", (-40, 1), xytext=(-55, 2.2), fontsize=8, color=P.muted(),
            arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
ax.text(29, 0.35, "lines extrapolate\nto M = 0 at Ta = Tb", fontsize=8, color=P.muted())
ax.axhline(1, color=P.muted(), lw=0.6, ls="--")
ax.set_xlim(-60, 45)
ax.set_ylim(0, 4.2)
ax.set_xlabel("Ambient temperature $T_{\\mathrm{a}}$ / $^\\circ$C")
ax.set_ylabel("Metabolic rate / basal metabolic rate")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  Thermoneutral zones and Scholander lines", loc="left", fontsize=10)

M = np.logspace(-2.3, 2, 100)  # kg
bmr = 3.4 * M ** 0.75
cond = 1.0 * (M * 1e3) ** -0.5 * (M * 1e3) * 20.1 / 3600  # W per C
lct = 37.5 - bmr / cond
bx.plot(M, lct, color=P.edge("dna"), lw=2.2, label="allometric prediction, $T_b - $LCT $\\propto M^{0.25}$")
bx.plot([3.5], [-40], "s", color=P.edge("dna2"), ms=7, label="arctic fox: insulation about 4x better")
bx.plot([70], [28], "^", color=P.edge("blood"), ms=8, label="nude human: much poorer insulation")
bx.set_xscale("log")
bx.set_xlabel("Body mass $M$ / kg")
bx.set_ylabel("Lower critical temperature / $^\\circ$C")
bx.legend(frameon=False, fontsize=8, loc="lower left")
bx.set_title("B  Larger animals tolerate colder air without extra heat", loc="left", fontsize=10)
fig.tight_layout()
