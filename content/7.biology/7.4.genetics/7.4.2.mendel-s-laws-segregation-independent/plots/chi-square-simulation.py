"""Sampling variation of F2 ratios and the chi-square test, by simulation (numpy, fixed seed).

A: fraction of recessive progeny in 10 000 simulated F2 families of n = 100 and n = 1000 under a true 3:1
ratio (binomial sampling); the standard deviation is sqrt(p(1-p)/n) = 0.043 and 0.014.
B: chi-square statistics of the n = 100 families (histogram, density scale) with the chi-square density
for 1 degree of freedom; the fraction above 3.84 is about 5%.
"""
import numpy as np
from scipy import stats

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
reps = 10000
fig, ax = bio.canvas(24.0, 8.6)

bio.panel(ax, "A", (0.2, 8.5))
a = charts.axes_at(ax, (1.9, 1.5, 9.4, 6.2))
for n, tok in ((100, "dna"), (1000, "trna")):
    k = rng.binomial(n, 0.25, reps)
    bins = np.arange(0.1, 0.42, 0.01 if n == 100 else 0.0025)
    a.hist(k / n, bins=bins, density=True, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.4, alpha=0.85,
           label=f"n = {n}")
a.axvline(0.25, color=P.ink(), lw=1.0, ls=(0, (3, 2)))
a.set_xlim(0.1, 0.4)
charts.style_axes(a, "fraction recessive in the F₂", "density")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())

bio.panel(ax, "B", (12.6, 8.5))
b = charts.axes_at(ax, (14.3, 1.5, 9.2, 6.2))
k = rng.binomial(100, 0.25, reps)
e = np.array([75.0, 25.0])
o = np.c_[100 - k, k]
chi = ((o - e) ** 2 / e).sum(axis=1)
b.hist(chi, bins=np.arange(0, 12.5, 0.5), density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4)
x = np.linspace(0.05, 12, 300)
b.plot(x, stats.chi2.pdf(x, 1), color=charts.line("negative"), lw=1.6, label="χ² density, 1 df")
b.axvline(3.84, color=P.ink(), lw=1.0, ls=(0, (3, 2)))
frac = (chi > 3.84).mean()
b.text(4.1, 0.9, f"{100 * frac:.1f}% of families\nexceed 3.84", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_ylim(0, 1.2)
b.set_xlim(0, 12)
charts.style_axes(b, "χ² statistic (n = 100)", "density")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
