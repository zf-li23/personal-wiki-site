"""Competition-colonization trade-off: coexistence of two species in a metapopulation.

Hastings (1980), Tilman (1994): dp1/dt = c1 p1 (1 - p1) - e p1 for the superior competitor, which ignores
the inferior one, and dp2/dt = c2 p2 (1 - p1 - p2) - e p2 - c1 p1 p2 for the inferior competitor, which can
only colonize empty sites and is displaced wherever species 1 arrives (equal extinction rates e).
A: outcomes in the plane of e/c1 and c2/c1: species 1 persists if e < c1; species 2 then persists with it
if c2 > c1^2 / e (above the curve). Point: the example of B. B: dynamics for c1 = 0.2, c2 = 0.8, e = 0.1
per year from p1 = 0.01, p2 = 0.01: the poor competitor, a fast colonizer, spreads first and is then
partly displaced; both settle at p1* = 1 - e/c1 = 0.5 and p2* = 1 - p1* - (e + c1 p1*)/c2 = 0.25.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.0, 1.6, 9.0, 6.8))
x = np.linspace(0.02, 1.6, 400)
ymax = 8.0
curve = np.where(x < 1, 1 / x, np.nan)
pa.fill_between(x, np.where(x < 1, curve, ymax), ymax, where=x < 1,
                color=P.mix(P.fill("positive"), P.surface(), 0.5), lw=0)
pa.fill_between(x, 0, np.where(x < 1, curve, 0), where=x < 1, color=P.mix(P.fill("dna2"), P.surface(), 0.5), lw=0)
pa.fill_between(x, x, ymax, where=x >= 1, color=P.mix(P.fill("rna"), P.surface(), 0.5), lw=0)
pa.plot(x, curve, color=P.ink(), lw=1.2)
pa.axvline(1, color=P.ink(), lw=1.0)
pa.plot(x[x >= 1], x[x >= 1], color=P.ink(), lw=1.0, ls=(0, (3, 2)))
pa.text(0.45, 6.0, "coexistence", fontsize=FS["small"], color=P.ink(), ha="center")
pa.text(0.6, 0.6, "species 1 only", fontsize=FS["small"], color=P.ink(), ha="center")
pa.text(1.3, 6.0, "species 2\nonly", fontsize=FS["small"], color=P.ink(), ha="center")
pa.text(1.3, 0.5, "neither", fontsize=FS["small"], color=P.ink(), ha="center")
pa.plot([0.5], [4.0], "o", ms=5, color=Q.line_color("negative"))
pa.text(1 / 0.62 * 0 + 0.55, 2.2, "c2/c1 = c1/e", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 1.6)
pa.set_ylim(0, ymax)
C.style_axes(pa, "extinction rate e / c1", "colonization ratio c2 / c1")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Outcomes of the two-species model", size="small", bold=True, ha="left")

c1, c2, e = 0.2, 0.8, 0.1


def f(t, p):
    p1, p2 = p
    return [c1 * p1 * (1 - p1) - e * p1, c2 * p2 * (1 - p1 - p2) - e * p2 - c1 * p1 * p2]


sol = solve_ivp(f, (0, 150), [0.01, 0.01], dense_output=True, rtol=1e-8)
t = np.linspace(0, 150, 500)
y = sol.sol(t)
pb = C.axes_at(ax, (15.0, 1.6, 14.0, 6.8))
pb.plot(t, y[0], color=Q.line_color("dna"), lw=1.7, label="species 1: superior competitor, c1 = 0.2")
pb.plot(t, y[1], color=Q.line_color("negative"), lw=1.7, label="species 2: fugitive, c2 = 0.8")
pb.plot(t, 1 - y[0] - y[1], color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="empty sites")
pb.set_xlim(0, 150)
pb.set_ylim(0, 1)
C.style_axes(pb, "years", "fraction of sites")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (13.5, 9.6))
bio.label(ax, (15.0, 9.2), "Fugitive coexistence (e = 0.1)", size="small", bold=True, ha="left")
