"""Personality and behavioral syndromes (simulated data, illustrative parameters).

A: boldness of 12 individuals measured in five trials. Each individual has its own mean (between-individual
variance 1) plus trial-to-trial noise (within-individual variance 1), so the repeatability
R = V_ind / (V_ind + V_within) is about 0.5; the estimate from the data (one-way ANOVA) is shown.
B, C: individual means of boldness and of aggression towards a conspecific in two populations, one in which the
two traits are correlated across individuals (a behavioral syndrome, true r = 0.6) and one in which they are not.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(4)

fig, ax = bio.canvas(33.0, 10.0)

# ---- A: repeatability ----------------------------------------------------------------------------------------
n, k = 12, 5
mu = np.sort(rng.normal(0, 1, n))
y = mu[:, None] + rng.normal(0, 1, (n, k))
y = y[np.argsort(y.mean(1))]
ms_b = k * np.var(y.mean(1), ddof=1)
ms_w = np.sum((y - y.mean(1, keepdims=True)) ** 2) / (n * (k - 1))
R = (ms_b - ms_w) / (ms_b + (k - 1) * ms_w)
pa = Ch.axes_at(ax, (2.4, 1.7, 8.0, 7.0))
cmap = [P.mix(Ch.line("dna"), Ch.line("rna"), i / (n - 1)) for i in range(n)]
for i in range(n):
    xs = i + np.linspace(-0.25, 0.25, k)
    pa.plot(xs, y[i], "o", ms=3, color=cmap[i])
    pa.plot([i - 0.32, i + 0.32], [y[i].mean()] * 2, color=cmap[i], lw=1.8)
pa.set_xlim(-0.8, n - 0.2)
pa.set_xticks(range(n))
pa.set_xticklabels([str(i + 1) for i in range(n)])
pa.text(0, 3.4, f"repeatability R = {R:.2f}", fontsize=FS["tiny"], color=P.ink())
pa.set_ylim(-3.8, 4)
Ch.style_axes(pa, "individual (ranked by mean)", "boldness score (5 trials)")
bio.panel(ax, "A", (0.3, 9.8))

# ---- B, C: syndromes -------------------------------------------------------------------------------------------
for j, (r, title, tok) in enumerate(((0.6, "population with a syndrome", "rna"), (0.0, "no syndrome", "dna"))):
    x0 = 13.6 + 11.0 * j
    p = Ch.axes_at(ax, (x0, 1.7, 7.0, 7.0))
    m = 40
    cov = np.array([[1, r], [r, 1]])
    z = rng.multivariate_normal([0, 0], cov, m)
    p.plot(z[:, 0], z[:, 1], "o", ms=3.5, color=Ch.line(tok), mfc="none")
    b = np.polyfit(z[:, 0], z[:, 1], 1)
    xx = np.array([-2.6, 2.6])
    p.plot(xx, np.polyval(b, xx), color=Ch.line(tok), lw=1.3)
    rr = np.corrcoef(z.T)[0, 1]
    p.text(-2.8, 2.6, f"r = {rr:.2f}", fontsize=FS["tiny"], color=P.ink())
    p.set_xlim(-3, 3)
    p.set_ylim(-3, 3)
    Ch.style_axes(p, "boldness (individual mean)", "aggression (individual mean)")
    Ch.title(p, title)
    bio.panel(ax, "BC"[j], (x0 - 2.0, 9.8))
