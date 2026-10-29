"""Robustness of a gradient to its source, and scaling with tissue size.

Units D = 1. A: linear degradation (k = 1, decay length 1): doubling the influx j shifts a threshold position by
lambda ln 2 = 0.69. B: self-enhanced degradation, rate k C^2: the steady profile is C = 6D / [k (x + eps)^2] with
eps = (12 D^2 / k j)^(1/3); far from the source it forgets j, and doubling j shifts the same threshold by only
eps (1 - 2^(-1/3)) (k chosen so that the threshold lies at x = 2 for both models at the reference influx; in B the
influx is strong, so that eps is small).
C: expansion-repression in the quasi-steady limit of a uniform, long-lived expander that lowers the
degradation rate and whose production is repressed by the morphogen: the expander accumulates until the
morphogen at the far end has fallen to the repression threshold T, which fixes the decay length through
(j lambda / D) / sinh(L / lambda) = T. Profiles for L = 2, 4 and 8 (log scale, against x / L) change far less than
the tissue (lambda / L falls only from 0.31 to 0.23 as L grows fourfold), while a fixed decay length (dashed, lambda = 1) gives profiles that do not scale.
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(30.0, 9.6)
T = 0.05
x = np.linspace(0, 5, 400)
FS = bio.core.FONT

# A: linear
pa = C.axes_at(ax, (1.6, 1.4, 7.2, 6.4))
for j, tk, ls in ((1.0, "protein", "-"), (2.0, "negative", (0, (4, 2)))):
    pa.semilogy(x, j * np.exp(-x), color=Q.line_color(tk), lw=1.8, ls=ls, label=f"influx {j:g} j")
Tl = np.exp(-2.0)
pa.axhline(Tl, color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pa.set_xlim(0, 5)
pa.set_ylim(3e-3, 3)
C.style_axes(pa, "x / λ", "C (log scale)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink())
pa.text(2.05, Tl * 1.25, f"shift = ln 2 = {np.log(2):.2f}", color=P.ink(), fontsize=FS["tiny"])
bio.panel(ax, "A", (0.3, 9.0))
bio.label(ax, (1.6, 9.0), "Linear degradation", size="small", bold=True, ha="left")

# B: self-enhanced degradation, k chosen so that C(2) = Tl at j = 1
def prof(xx, j, k):
    eps = (12 / (k * j)) ** (1 / 3)
    return 6 / (k * (xx + eps) ** 2), eps
J0 = 30.0
k = brentq(lambda kk: prof(2.0, J0, kk)[0] - Tl, 1e-3, 1e6)
pb = C.axes_at(ax, (11.6, 1.4, 7.2, 6.4))
pos = []
for j, tk, ls in ((J0, "protein", "-"), (2 * J0, "negative", (0, (4, 2)))):
    c, eps = prof(x, j, k)
    pb.semilogy(x, c, color=Q.line_color(tk), lw=1.8, ls=ls, label=f"influx {j / J0:g} j")
    pos.append(np.sqrt(6 / (k * Tl)) - eps)
pb.axhline(Tl, color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pb.set_xlim(0, 5)
pb.set_ylim(3e-3, 300)
C.style_axes(pb, "x", "C (log scale)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink())
pb.text(2.05, Tl * 1.25, f"shift = {pos[1] - pos[0]:.2f}", color=P.ink(), fontsize=FS["tiny"])
bio.panel(ax, "B", (10.3, 9.0))
bio.label(ax, (11.6, 9.0), "Self-enhanced degradation (k C²)", size="small", bold=True, ha="left")

# C: expansion-repression, quasi-steady
pc = C.axes_at(ax, (21.6, 1.4, 7.6, 6.4))
toks = ["protein", "na", "negative"]
for L, tk in zip((2.0, 4.0, 8.0), toks):
    lam = brentq(lambda l: (l / np.sinh(L / l)) - T, 0.05, 50 * L)
    xs = np.linspace(0, L, 300)
    m = lam * np.cosh((L - xs) / lam) / np.sinh(L / lam)
    pc.semilogy(xs / L, m / m[0], color=Q.line_color(tk), lw=1.8, label=f"L = {L:g}: λ/L = {lam / L:.2f}")
    mf = np.cosh(L - xs) / np.cosh(L)
    pc.semilogy(xs / L, mf, color=Q.line_color(tk), lw=1.1, ls=(0, (3, 2)))
pc.set_xlim(0, 1)
pc.set_ylim(1e-4, 1.5)
C.style_axes(pc, "x / L", "C / C(0) (log scale)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "C", (20.3, 9.0))
bio.label(ax, (21.6, 9.0), "Expansion-repression: λ adapts to L", size="small", bold=True, ha="left")
