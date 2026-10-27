"""Two special chromosomes (schematic) and the ecdysone puffing cascade (schematic kinetics).
(A) Polytene chromosome: aligned chromatids with bands and interbands; a puff with nascent RNA (dashed halo).
(B) Lampbrush chromosome: chromomere axis with paired lateral loops; RNP fibrils lengthen along each loop.
(C) Ashburner model as ODEs (arbitrary units): ecdysone H = 1 from t = 0; early-gene activity
dE/dt = H/(1 + (P/K)^4) - E (early proteins P repress their own genes), dP/dt = s E - 0.3 P;
late-gene activity dL/dt = 0.5 (P^2/(K^2 + P^2) - L). With cycloheximide (s = 0, no protein synthesis)
the early puffs appear but do not regress, and late puffs never form (dashed)."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts
from wikibio import nuclear as N

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(22.0, 7.4)

bio.panel(ax, "A", (0.1, 7.3))
pc = N.polytene(ax, 0.6, 12.6, 5.6, 0.9, puff=0.55, puff_width=1.6, seed=4)
bio.callout(ax, (3.0, 5.6 + 0.48), (2.6, 7.0), "band")
bio.callout(ax, pc["puff"], (8.6, 7.0), "puff (transcribed)")
bio.label(ax, (6.6, 4.3), "polytene chromosome: about 1000 aligned chromatids", size="small")

bio.panel(ax, "B", (0.1, 3.6))
lb = N.lampbrush(ax, 0.8, 12.4, 2.05, loops=7, loop_height=1.0)
bio.callout(ax, (0.95, 2.05), (0.4, 0.3), "chromomere axis")
bio.callout(ax, lb["loops"][2], (5.2, 3.55), "lateral loop (transcription unit)")
bio.label(ax, (8.0, 0.3), "lampbrush chromosome (diplotene oocyte)", size="small")

bio.panel(ax, "C", (13.8, 7.3))
c = charts.axes_at(ax, (15.2, 1.3, 6.3, 5.6))
K = 1.0


def rhs(t, y, s):
    E, Pp, L = y
    return [1 / (1 + (Pp / K) ** 4) - E, s * E - 0.3 * Pp, 0.5 * (Pp**2 / (K**2 + Pp**2) - L)]


t = np.linspace(0, 20, 400)
for s, ls, tag in ((1.0, "-", ""), (0.0, "--", " + cycloheximide")):
    sol = solve_ivp(rhs, (0, 20), [0, 0, 0], args=(s,), t_eval=t, rtol=1e-8)
    c.plot(t, sol.y[0], color=charts.line("positive"), lw=1.8, ls=ls, label="early puffs" + tag)
    c.plot(t, sol.y[2], color=charts.line("negative"), lw=1.8, ls=ls, label="late puffs" + tag)
c.set_xlim(0, 20)
c.set_ylim(0, 1.25)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(c, "time after ecdysone (arbitrary units)", "puff size (activity)")
