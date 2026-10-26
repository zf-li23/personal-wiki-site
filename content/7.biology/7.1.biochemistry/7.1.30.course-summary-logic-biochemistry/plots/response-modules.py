"""Four ways a protein turns an input into a response, compared on one normalized axis.

Input x is the ligand concentration relative to its half-saturating value (binding curves) or the
ratio of kinase to phosphatase maximal rates V1/V2 (modification cycle), so every curve passes
through 0.5 at x = 1.
- hyperbolic binding, theta = x/(1 + x) (Formula 7.1.1; Michaelis-Menten has the same shape)
- cooperative binding, Hill equation with nH = 2.8 (hemoglobin, Formula 7.3.1)
- the MAPK of a three-tier cascade, apparent nH = 4.9 (Formula 15.1.1, Huang and Ferrell)
- a modification cycle with both enzymes saturated, J = 0.01 (Formula 9.6.1)
B: the response coefficient R, the fold change in input from 10% to 90% response:
R = 81 for hyperbolic, 81**(1/nH) for Hill curves, 81((J + 0.1)/(J + 0.9))**2 for the cycle.
"""

import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio.core import FONT

P = bio.P
fig, ax = bio.canvas(24, 9.5, scale=0.5)

x = np.logspace(-2, 2, 600)
curves = [
    ("Hyperbolic binding (nH = 1)", x / (1 + x), "neutral", 81.0),
    ("Hemoglobin (nH = 2.8)", x**2.8 / (1 + x**2.8), "blood", 81 ** (1 / 2.8)),
    ("MAPK cascade (nH ≈ 4.9)", x**4.9 / (1 + x**4.9), "enzyme", 81 ** (1 / 4.9)),
]
# Goldbeter-Koshland: invert V1/V2 = w (J + 1 - w) / ((1 - w)(J + w)) on a fine grid of w
J = 0.01
w = np.linspace(1e-4, 1 - 1e-4, 4000)
u = w * (J + 1 - w) / ((1 - w) * (J + w))
gk = np.interp(x, u, w)
curves.append(("Saturated modification cycle (J = 0.01)", gk, "receptor", 81 * ((J + 0.1) / (J + 0.9)) ** 2))

a = charts.axes_at(ax, (1.8, 1.6, 11.0, 6.9))
for name, yv, tok, _ in curves:
    a.plot(x, yv, color=charts.line(tok), lw=2.0, label=name)
a.axhspan(0.1, 0.9, color=P.mix(P.muted(), P.surface(), 0.85), zorder=0)
a.axvline(1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
a.set_xscale("log")
a.set_xlim(0.01, 100)
a.set_ylim(0, 1.02)
charts.style_axes(a, "relative input ([L]/K₀.₅ or V₁/V₂)", "fractional response")
charts.title(a, "A  Input–response curves")
leg = a.legend(frameon=False, fontsize=FONT["tiny"], loc="upper left")
for t in leg.get_texts():
    t.set_color(P.ink())

b = charts.axes_at(ax, (16.6, 1.6, 6.6, 6.9))
labels = ["Hyperbolic", "Hemoglobin", "MAPK", "Cycle\n(J = 0.01)"]
Rs = [c[3] for c in curves]
pos = np.arange(len(Rs))
b.bar(pos, Rs, 0.6, color=[charts.line(c[2]) for c in curves])
for p, r in zip(pos, Rs):
    b.text(p, r * 1.15, f"{r:.2g}", ha="center", fontsize=FONT["tiny"], color=P.ink())
b.set_yscale("log")
b.set_ylim(1, 200)
b.set_xticks(pos)
b.set_xticklabels(labels, fontsize=FONT["tiny"])
charts.style_axes(b, None, "fold change in input, 10% → 90%")
charts.title(b, "B  Response coefficient R")
