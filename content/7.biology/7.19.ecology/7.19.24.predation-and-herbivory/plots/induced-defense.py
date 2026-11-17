"""Costs and benefits of constitutive and inducible defense (a simple fitness model, simulated values).

A plant is attacked with probability p during a season. Undefended: fitness 1 - p D (D = 0.6, the loss
to an attack). Constitutive defense: 1 - C - p d (cost C = 0.15 paid always, residual loss d = 0.1).
Inducible defense: 1 - k - p (C_i + d + l), with a small fixed cost of the capacity to respond
(k = 0.02), the cost of producing the defense when attacked (C_i = 0.05) and the extra damage during
the lag before the defense is in place (l = 0.15). A: fitness against p: undefended plants do best when
attack is rare, inducible defense at intermediate risk, constitutive defense when attack is nearly
certain. B: the best strategy in the plane of p and the cost of constitutive defense C (other values
as in A): inducible defense is favored when attacks are variable and the lag is short, constitutive
defense when it is cheap or attack is predictable.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
D, d, k, Ci, lag = 0.6, 0.1, 0.02, 0.05, 0.15


def w(p, Cc):
    return np.array([1 - p * D, 1 - Cc - p * d, 1 - k - p * (Ci + d + lag)])


p = np.linspace(0, 1, 400)
W = w(p, 0.15)
pa = C.axes_at(ax, (2.4, 1.8, 11.5, 8.6))
names = ["undefended", "constitutive", "inducible"]
toks = ["negative", "dna", "positive"]
for i in range(3):
    pa.plot(p, W[i], color=Q.line_color(toks[i]), lw=1.8, label=names[i])
best = W.argmax(axis=0)
for i in range(3):
    sel = best == i
    if sel.any():
        pa.fill_between(p, 0.35, 1.02, where=sel, color=P.mix(P.fill(toks[i]), P.surface(), 0.8), lw=0)
pa.set_xlim(0, 1)
pa.set_ylim(0.35, 1.02)
C.style_axes(pa, "probability of attack p", "relative fitness")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Fitness of three strategies (C = 0.15)", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
pp, cc = np.meshgrid(np.linspace(0, 1, 300), np.linspace(0, 0.4, 300))
Z = w(pp, cc).argmax(axis=0)
from matplotlib.colors import ListedColormap
cmap = ListedColormap([P.mix(P.fill(t), P.surface(), 0.5) for t in toks])
pb.pcolormesh(pp, cc, Z, cmap=cmap, vmin=-0.5, vmax=2.5, shading="auto")
pb.text(0.04, 0.3, "undefended", fontsize=FS["small"], color=P.ink())
pb.text(0.35, 0.3, "inducible", fontsize=FS["small"], color=P.ink())
pb.text(0.75, 0.04, "constitutive", fontsize=FS["small"], color=P.ink())
pb.set_xlim(0, 1)
pb.set_ylim(0, 0.4)
C.style_axes(pb, "probability of attack p", "cost of constitutive defense C")
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "Best strategy", size="small", bold=True, ha="left")
