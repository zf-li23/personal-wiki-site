"""Zero-order ultrasensitivity in a covalent modification cycle (Goldbeter and Koshland, 1981).

A: the cycle. A kinase (maximal rate V1, Michaelis constant K1) converts W to W-P, a phosphatase
(V2, K2) converts it back; total W_T = [W] + [W-P].
B: steady-state fraction modified, w = [W-P]/W_T, against the ratio of maximal rates V1/V2, for
J = K1/W_T = K2/W_T = 10, 1, 0.1, 0.01. From V1 (1 - w)/(J + 1 - w) = V2 w/(J + w),
V1/V2 = w (J + 1 - w) / ((1 - w)(J + w)), which is plotted parametrically. For J >> 1 both enzymes
work in the first-order regime and the response is hyperbolic; for J << 1 both are saturated
(zero order) and the cycle switches sharply at V1 = V2.
C: response coefficient R = (V1/V2 at w = 0.9)/(V1/V2 at w = 0.1) = 81 ((J + 0.1)/(J + 0.9))^2,
from 81 (Michaelis-Menten-like) to 1 (a perfect switch); the equivalent Hill coefficient is
ln 81 / ln R."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22.0, 8.4)

# --- A: the cycle ------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.3))
w0, w1 = (1.3, 4.0), (5.3, 4.0)
bio.protein(ax, w0, 1.2, 0.8, "protein", text="W")
bio.protein(ax, w1, 1.4, 0.8, "protein", text="W–P")
bio.arrow(ax, (1.8, 4.6), (4.7, 4.6), kind="process", bend=-0.35)
bio.arrow(ax, (4.7, 3.4), (1.8, 3.4), kind="process", bend=-0.35)
bio.protein(ax, (3.25, 6.6), 1.6, 0.7, "enzyme", text="kinase")
bio.protein(ax, (3.25, 1.4), 1.9, 0.7, "drug", text="phosphatase")
bio.arrow(ax, (3.25, 6.22), (3.25, 5.35), kind="catalysis")
bio.arrow(ax, (3.25, 1.78), (3.25, 2.65), kind="catalysis")
bio.label(ax, (3.25, 7.45), r"$V_1, K_1$", size="small")
bio.label(ax, (3.25, 0.6), r"$V_2, K_2$", size="small")
bio.label(ax, (5.15, 6.3), "ATP → ADP", size="tiny", color=P.muted())
bio.label(ax, (1.35, 1.75), "P$_\\mathrm{i}$ released", size="tiny", color=P.muted())

# --- B: steady-state response ------------------------------------------------------------
bio.panel(ax, "B", (7.0, 8.3))
b = charts.axes_at(ax, (8.3, 1.0, 6.4, 6.4))
w = np.linspace(1e-4, 1 - 1e-4, 2000)
for J, tok in ((10.0, "neutral"), (1.0, "channel"), (0.1, "enzyme"), (0.01, "protein")):
    r = w * (J + 1 - w) / ((1 - w) * (J + w))
    b.plot(r, w, color=charts.line(tok), lw=2.0, label=f"$J$ = {J:g}")
b.set_xscale("log")
b.set_xlim(0.1, 10)
b.set_ylim(0, 1.02)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, r"$V_1/V_2$ (kinase / phosphatase)", "fraction modified $w$")
charts.title(b, "Saturated enzymes make a switch")

# --- C: response coefficient -------------------------------------------------------------
bio.panel(ax, "C", (15.5, 8.3))
c = charts.axes_at(ax, (16.8, 1.0, 4.8, 6.4))
J = np.logspace(-3, 2, 300)
R = 81 * ((J + 0.1) / (J + 0.9)) ** 2
c.plot(J, R, color=charts.line("protein"), lw=2.0)
c.axhline(81, color=P.muted(), lw=0.8, ls="--")
c.text(1.2e-3, 55, "Michaelis–Menten: 81", fontsize=bio.core.FONT["tiny"], color=P.ink())
c.set_xscale("log")
c.set_yscale("log")
c.set_ylim(0.8, 150)
charts.style_axes(c, r"$J = K/W_\mathrm{T}$", r"response coefficient $R$")
charts.title(c, "Sharpness")
