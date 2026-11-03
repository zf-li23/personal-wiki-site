"""Brownian motion and the Ornstein-Uhlenbeck model (Eqs. (26.5)-(26.6)). A: sample paths of a trait starting
at 0 under Brownian motion (alpha = 0) and under OU models pulled towards the optimum theta = 1 with
alpha = 1 and alpha = 5 (sigma^2 = 1, time in units of the tree height; three paths each, exact
transition distributions on a grid of 400 steps); dotted lines: the stationary band theta +- 2 sigma
/ sqrt(2 alpha) for alpha = 5. B: the correlation between two species that share a path of length s
from the root on a tree of height 1, Eq. (26.7): under Brownian motion it equals s, while under OU it
decays with the time since divergence 1 - s, so species separated by much more than 1/(2 alpha)
behave as nearly independent."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(6)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
n, T, th = 400, 1.0, 1.0
dt = T / n
t = np.linspace(0, T, n + 1)
for al, tok, name in ((0.0, "neutral", "BM ($\\alpha = 0$)"), (1.0, "dna", "OU, $\\alpha = 1$"),
                      (5.0, "rna", "OU, $\\alpha = 5$")):
    for k in range(3):
        x = np.zeros(n + 1)
        for i in range(n):
            if al == 0:
                x[i + 1] = x[i] + rng.normal(0, np.sqrt(dt))
            else:
                m = th + (x[i] - th) * np.exp(-al * dt)
                v = (1 - np.exp(-2 * al * dt)) / (2 * al)
                x[i + 1] = rng.normal(m, np.sqrt(v))
        a.plot(t, x, color=charts.line(tok), lw=0.9, alpha=0.9, label=name if k == 0 else None)
for sgn in (-1, 1):
    a.axhline(th + sgn * 2 / np.sqrt(10), color=charts.line("rna"), lw=0.7, ls=":")
a.axhline(th, color=P.muted(), lw=0.7, ls="--")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "time", "trait value")
charts.title(a, "A  Pulled towards an optimum")
s = np.linspace(0, 1, 200)
b.plot(s, s, color=P.ink(), lw=1.5, label="BM")
for al, tok in ((0.5, "positive"), (2.0, "dna"), (8.0, "rna")):
    cov = np.exp(-2 * al * (1 - s)) * (1 - np.exp(-2 * al * s)) / (2 * al)
    var = (1 - np.exp(-2 * al)) / (2 * al)
    b.plot(s, cov / var, color=charts.line(tok), lw=1.5, label=f"OU, $\\alpha = {al:g}$")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "shared path length $s$ (tree height 1)", "correlation of the two tips")
charts.title(b, "B  Phylogenetic signal decays under OU")
