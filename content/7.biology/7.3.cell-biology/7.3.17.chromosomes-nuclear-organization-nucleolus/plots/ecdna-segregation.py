"""Random segregation of ecDNA (Proposition 17.9.1): a daughter of a cell with X copies receives Bin(2X, 1/2).
(A) Copy-number distribution among 20 000 lineages started at 20 copies after 0, 10 and 40 generations
(no selection); a chromosomal amplicon stays at 20 (line). (B) Variance across lineages versus generation (points)
and the prediction g k / 2 (line). (C) Selection in a population of 5000 cells (Wright-Fisher resampling of cells
with weights w(x)): while a drug is present (generations 0-30) fitness rises with copy number,
w = exp(0.01 x); after withdrawal (30-60) high copy number is costly, w = exp(-0.01 x). Mean ecDNA copy number
(solid) and a chromosomal amplicon (dashed, inherited exactly, cannot respond)."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)

k0 = 20
L = 20000
X = np.full(L, k0)
hist = {0: X.copy()}
var = [0.0]
for g in range(1, 41):
    X = rng.binomial(2 * X, 0.5)
    var.append(X.var())
    if g in (10, 40):
        hist[g] = X.copy()

fig, ax = bio.canvas(22.0, 7.4)
bio.panel(ax, "A", (0.1, 7.3))
a = charts.axes_at(ax, (1.8, 1.3, 5.4, 5.6))
bins = np.arange(-0.5, 101.5, 2)
for g, tok in ((10, "positive"), (40, "negative")):
    a.hist(hist[g], bins=bins, density=True, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, alpha=0.75, label=f"ecDNA, g = {g}")
a.axvline(k0, color=charts.line("channel"), lw=1.8, label="g = 0; chromosomal amplicon")
a.set_xlim(0, 90)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "copies per cell", "fraction of cells per copy number")

bio.panel(ax, "B", (7.9, 7.3))
b = charts.axes_at(ax, (9.5, 1.3, 4.8, 5.6))
gs = np.arange(41)
b.plot(gs[::2], np.array(var)[::2], "o", color=charts.line("negative"), ms=3.5, label="simulation")
b.plot(gs, gs * k0 / 2, color=P.ink(), lw=1.2, label="g k / 2")
b.set_xlim(0, 40)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "generation g", "variance of copy number")

bio.panel(ax, "C", (15.0, 7.3))
c = charts.axes_at(ax, (16.6, 1.3, 5.0, 5.6))
N = 5000
X = np.full(N, k0)
means = [X.mean()]
for g in range(1, 61):
    X = rng.binomial(2 * X, 0.5)
    s = 0.01 if g <= 30 else -0.01
    w = np.exp(s * X)
    X = X[rng.choice(N, N, p=w / w.sum())]
    means.append(X.mean())
c.axvspan(0, 30, color=P.fill("highlight"), alpha=0.35, lw=0)
c.text(15, max(means) * 0.95, "drug present", fontsize=FT["tiny"], color=P.muted(), ha="center")
c.plot(np.arange(61), means, color=charts.line("negative"), lw=1.8, label="ecDNA")
c.plot([0, 60], [k0, k0], color=charts.line("channel"), lw=1.6, ls="--", label="chromosomal amplicon")
c.set_xlim(0, 60)
c.set_ylim(0, max(means) * 1.1)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(c, "generation", "mean copies per cell")
