"""Alternative stable states of shallow lakes: the minimal model of Scheffer et al. (2001).

Turbidity E and vegetation cover V (relative to its maximum):
dE/dt = rE E (1 - E (hV + V) / (E0 hV)),   dV/dt = rV V (1 - V (hE^p + E^p) / hE^p),
hV = 0.2, hE = 2, p = 4. Vegetation reduces turbidity (E* = E0 hV / (hV + V)); turbidity above hE
suppresses vegetation. E0, the turbidity without vegetation, increases with nutrient loading.
Turbidity (phytoplankton) responds faster than vegetation, so E is set to its quasi-equilibrium and
the dynamics reduce to dV/dt = f(V; E0) = rV V [1 - V (1 + (E0 hV / (hE (hV + V)))^p)].
A: equilibrium turbidity against E0: a clear branch (vegetated) and a turbid branch (little
vegetation), both stable (solid), joined by an unstable branch (dashed) between the fold points
E0 = 5.15 and 7.29. Arrows: the path of a lake under slowly increasing and then decreasing nutrient
loading (hysteresis). B: potentials U(V) = -int f dV for three values of E0: one valley (clear),
two valleys separated by a hill (bistable), one valley (turbid).
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

hV, hE, p, rV = 0.2, 2.0, 4, 1.0


def f(V, E0):
    E = E0 * hV / (hV + V)
    return rV * V * (1 - V * (1 + (E / hE) ** p))


V = np.linspace(1e-4, 0.9999, 20000)
E0c = hE * ((1 - V) / V) ** (1 / p) * (hV + V) / hV  # E0 at which V is an equilibrium
Ec = hE * ((1 - V) / V) ** (1 / p)  # corresponding turbidity
dV = 1e-6
stable = (f(V + dV, E0c) - f(V - dV, E0c)) / (2 * dV) < 0
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
for st, ls in [(True, "-"), (False, "--")]:
    msk = stable == st
    y = np.where(msk, Ec, np.nan)
    pa.plot(E0c, y, color=Q.line_color("dna"), lw=2.0 if st else 1.3, ls=ls)
F1, F2 = 5.153, 7.289
pa.annotate("", xy=(F2, 7.0), xytext=(F2, 1.6), arrowprops=dict(arrowstyle="->", color=Q.line_color("negative"), lw=1.3))
pa.annotate("", xy=(F1, 0.9), xytext=(F1, 4.9), arrowprops=dict(arrowstyle="->", color=Q.line_color("positive"), lw=1.3))
pa.text(F2 + 0.15, 4.2, "collapse of\nvegetation", fontsize=FS["tiny"], color=P.ink())
pa.text(F1 - 2.2, 3.0, "recovery only at\nmuch lower loading", fontsize=FS["tiny"], color=P.ink())
pa.text(1.0, 0.75, "clear, vegetated", fontsize=FS["tiny"], color=P.ink())
pa.text(7.8, 8.4, "turbid", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 10)
pa.set_ylim(0, 10)
C.style_axes(pa, "nutrient level (turbidity without plants, E0)", "equilibrium turbidity E")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Hysteresis between clear and turbid states", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
Vg = np.linspace(0, 1.05, 600)
for E0, tok in [(4.0, "positive"), (6.2, "dna"), (8.5, "negative")]:
    U = -cumulative_trapezoid(f(Vg, E0), Vg, initial=0)
    pb.plot(Vg, U - U.min(), color=Q.line_color(tok), lw=1.8, label=f"E0 = {E0}")
pb.set_xlim(0, 1.05)
pb.set_ylim(-0.005, 0.2)
C.style_axes(pb, "vegetation cover V", "potential U(V)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "Stability landscapes", size="small", bold=True, ha="left")
