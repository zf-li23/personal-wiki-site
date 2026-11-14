"""Maynard Smith's (1977) model of who should care: the evolutionarily stable combinations of care and desertion.

Eggs survive with probability P0, P1, P2 when cared for by no, one or two parents. A deserting male mates again
with probability p; a deserting female lays W eggs, a caring one w < W. A pair of strategies (female, male) is
an ESS if neither parent gains by switching while the other keeps its strategy:
female cares given male cares iff w P2 > W P1; given male deserts iff w P1 > W P0;
male cares given female cares iff P2 > P1 (1 + p); given female deserts iff P1 > P0 (1 + p).
The axes are the benefit of a second parent, P2/P1, and the female's gain in fecundity from deserting, W/w,
with P1/P0 = 3. A: a deserting male rarely remates (p = 0.3). B: deserting males often remate (p = 1.0).
Colors mark the ESSs present at each point; hatching marks two alternative ESSs.
"""

import numpy as np
from matplotlib.patches import Patch
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
R10 = 3.0
xs = np.linspace(1.0, 2.5, 301)
ys = np.linspace(1.0, 4.0, 301)
X, Y = np.meshgrid(xs, ys)
names = {(0, 0): "both desert", (0, 1): "male cares only", (1, 0): "female cares only", (1, 1): "both care"}
toks = {(0, 0): "neutral", (0, 1): "dna", (1, 0): "rna", (1, 1): "plant"}


def ess(p):
    # female care condition given male strategy m: m=1 -> X > Y ; m=0 -> R10 > Y
    fem = {1: X > Y, 0: R10 > Y}
    # male care condition given female strategy f: f=1 -> X > 1 + p ; f=0 -> R10 > 1 + p
    mal = {1: X > 1 + p, 0: np.full_like(X, R10 > 1 + p, dtype=bool)}
    out = {}
    for f in (0, 1):
        for m in (0, 1):
            fok = fem[m] if f == 1 else ~fem[m]
            mok = mal[f] if m == 1 else ~mal[f]
            out[(f, m)] = fok & mok
    return out


fig, ax = bio.canvas(30.0, 11.0)
for k, (p, title) in enumerate(((0.3, "deserting males rarely remate (p = 0.3)"),
                                (1.0, "deserting males often remate (p = 1.0)"))):
    a = Ch.axes_at(ax, (2.6 + 14.6 * k, 2.6, 10.8, 7.2))
    E = ess(p)
    count = sum(v.astype(int) for v in E.values())
    for key, mask in E.items():
        if mask.any():
            a.contourf(X, Y, mask.astype(float), levels=[0.5, 1.5], colors=[P.mix(P.fill(toks[key]), P.surface(), 0.7)], alpha=0.85)
    a.contourf(X, Y, (count >= 2).astype(float), levels=[0.5, 1.5], colors="none", hatches=["////"])
    for key, mask in E.items():
        only = mask & (count == 1)
        if only.sum() > 200:
            yy, xx = np.nonzero(only)
            a.text(xs[int(xx.mean())], ys[int(yy.mean())], names[key], ha="center", va="center",
                   fontsize=FS["tiny"], color=P.ink(), weight="bold")
    a.set_xlim(1, 2.5)
    a.set_ylim(1, 4)
    Ch.style_axes(a, "benefit of a second parent $P_2/P_1$", "female fecundity gain from deserting $W/w$")
    Ch.title(a, title)
    bio.panel(ax, "AB"[k], (0.3 + 14.6 * k, 10.8))
bio.label(ax, (15.0, 0.6), "hatched: two alternative ESSs (female only or male only);  P1/P0 = 3, so a male never deserts a deserting female", size="tiny", color=P.muted())
