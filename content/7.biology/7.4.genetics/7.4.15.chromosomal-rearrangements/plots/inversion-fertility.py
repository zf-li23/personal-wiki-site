"""Fraction of unbalanced meiotic products of an inversion heterozygote as a function of the genetic length
d of the inverted segment (Formula 15.4.1). A chromatid is unbalanced if it took part in an odd number of
crossovers inside the loop. Without interference the number of crossovers in the segment per bivalent is
Poisson with mean 2d, and each chromatid is involved in a crossover with probability 1/2, giving
(1 - exp(-2d))/2 (the Haldane relation); with complete interference (at most one crossover) it is d, up to
d = 1/2. A simulation of 20 000 meioses with random chromatid choice checks the first curve."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
d = np.linspace(0, 1.0, 201)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.16, top=0.93)
ax.plot(100 * d, (1 - np.exp(-2 * d)) / 2, color=charts.line("dna"), lw=1.6, label="no interference")
ax.plot(100 * d, np.minimum(d, 0.5), color=charts.line("receptor"), lw=1.6, ls="--", label="complete interference")
ds = np.linspace(0.05, 1.0, 12)
sim = []
for dd in ds:
    n = 20000
    k = rng.poisson(2 * dd, n)
    unbalanced = 0
    for m in k:
        counts = np.zeros(4, int)
        for _ in range(m):
            a = rng.integers(0, 2)        # chromatid of the normal homologue
            b = 2 + rng.integers(0, 2)    # chromatid of the inverted homologue
            counts[a] += 1
            counts[b] += 1
        unbalanced += np.sum(counts % 2 == 1)
    sim.append(unbalanced / (4 * n))
ax.plot(100 * ds, sim, "o", color=charts.line("dna"), ms=4, mfc="none", label="simulation")
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_ylim(0, 0.56)
ax.set_xlim(0, 100)
charts.style_axes(ax, "genetic length of the inverted segment d / cM", "unbalanced products")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
