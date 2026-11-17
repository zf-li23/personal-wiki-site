"""The mu/g rule for ontogenetic habitat shifts (Werner and Gilliam 1984).

A fish grows from size 5 to 150 mm. In a refuge habitat (vegetation) it grows at g1(s) = 0.02 s mm per day
and dies at mu1 = 0.002 per day; in open water it grows faster, g2(s) = 0.04 s, but suffers gape-limited
predation mu2(s) = 0.02 (10 / s) per day.
Survival from size s0 to S in a habitat sequence is exp(-integral of mu/g ds), so the best rule is to be,
at each size, in the habitat with the smaller mu/g.
A: mu/g in the two habitats against size (log axes); the switch size s* = 50 mm is where the curves
cross. B: with twice the predation in open water (more predators), s* doubles to 100 mm.
C: probability of surviving to 150 mm for fish that switch at size s_switch (line), with the optimum at
s*, compared with fish that stay in one habitat throughout (dashed lines).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
s = np.logspace(np.log10(5), np.log10(150), 400)


def ratio1(s):
    return 0.002 / (0.02 * s)


def ratio2(s, k=1.0):
    return k * 0.02 * (10 / s) / (0.04 * s)


for j, (k, title) in enumerate([(1.0, "Switch where mu/g curves cross"), (2.0, "More predators in open water")]):
    pa = C.axes_at(ax, (2.0 + 10.0 * j, 1.6, 7.0, 6.8))
    pa.loglog(s, ratio1(s), color=Q.line_color("positive"), lw=1.6, label="refuge (vegetation)")
    pa.loglog(s, ratio2(s, k), color=Q.line_color("dna"), lw=1.6, label="open water")
    sstar = 50 * k
    pa.axvline(sstar, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    pa.text(sstar * 1.08, 2e-3, f"s* = {sstar:.0f} mm", fontsize=FS["tiny"], color=P.ink())
    pa.set_xlim(5, 150)
    pa.set_ylim(1e-4, 2e-1)
    C.style_axes(pa, "body size s (mm)", "mortality / growth, mu/g (per mm)")
    pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
    bio.panel(ax, "AB"[j], (0.3 + 10.0 * j, 9.6))
    bio.label(ax, (2.0 + 10.0 * j, 9.2), title, size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
s0, S = 5.0, 150.0


def I1(a, b):
    return 0.1 * np.log(b / a)


def I2(a, b):
    return 5.0 * (1 / a - 1 / b)


sw = np.linspace(5, 150, 300)
surv = np.exp(-(I1(s0, sw) + I2(sw, S)))
pc.plot(sw, surv, color=Q.line_color("protein"), lw=1.6, label="refuge, then open water")
pc.axhline(np.exp(-I1(s0, S)), color=Q.line_color("positive"), lw=1.0, ls=(0, (4, 2)), label="refuge only")
pc.axhline(np.exp(-I2(s0, S)), color=Q.line_color("dna"), lw=1.0, ls=(0, (4, 2)), label="open water only")
k = int(np.argmax(surv))
pc.plot(sw[k], surv[k], "o", ms=5, color=Q.line_color("protein"))
pc.set_xlim(5, 150)
pc.set_ylim(0, 0.8)
C.style_axes(pc, "size at switch (mm)", "survival to 150 mm")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Survival under switching rules", size="small", bold=True, ha="left")
