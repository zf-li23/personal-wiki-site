"""Four results of the course that need more than fractions, each computed from its own formula.

A: mapping functions (Formula 8.5.1, 8.5.2): a Poisson process of crossovers bends the line r = d.
B: the Luria-Delbrueck distribution (Formula 12.4.1): mutants per culture simulated under random
   mutation during growth, against a Poisson distribution with the same mean (induced mutation).
C: Kimura's fixation probability (Theorem 23.6.1), relative to the neutral value 1/(2N), for a
   new mutation as a function of S = 4 N_e s (diffusion approximation).
D: expected accuracy of a polygenic score (Formula 25.6.1) against GWAS sample size.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(2, 2, figsize=(10.0, 7.2))

# A: mapping functions
ax = axs[0, 0]
d = np.linspace(0, 1.5, 300)
ax.plot(d, d, color=P.muted(), lw=1.0, ls=":", label="r = d (additive)")
ax.plot(d, 0.5 * (1 - np.exp(-2 * d)), color=charts.line("dna"), lw=1.8, label="Haldane (no interference)")
ax.plot(d, 0.5 * np.tanh(2 * d), color=charts.line("rna"), lw=1.8, ls="--", label="Kosambi")
ax.axhline(0.5, color=P.muted(), lw=0.6)
ax.set_ylim(0, 0.6)
ax.set_xlim(0, 1.5)
ax.legend(frameon=False, fontsize=7.5, labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "map distance d (morgans)", "recombination frequency r")
charts.title(ax, "A  Poisson process: mapping functions")

# B: Luria-Delbrueck
ax = axs[0, 1]
N0, Nt, m, cultures = 1e3, 1e9, 3.0, 4000
counts = np.empty(cultures)
for c in range(cultures):
    k = rng.poisson(m)
    sizes = rng.uniform(N0, Nt, size=k)  # mutations occur uniformly in the number of divisions
    counts[c] = np.floor(Nt / sizes).sum()
mean = counts.mean()
edges = np.r_[0, 1, 10.0 ** np.arange(1, 8)]  # 0 | 1-9 | 10-99 | ...
names = ["0", "1–9", "10–\n99", "10²–\n10³", "10³–\n10⁴", "10⁴–\n10⁵", "10⁵–\n10⁶", "≥10⁶"]
h = np.histogram(counts, bins=np.r_[edges, np.inf])[0][: len(names)]
xs = np.arange(len(names))
ax.bar(xs, h / cultures, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.6,
       label="random mutation (simulated)")
pois = np.diff(stats.poisson.cdf(np.r_[edges, np.inf] - 1, mean))[: len(names)]
ax.plot(xs, np.maximum(pois, 1e-9), "o-", color=charts.line("dna"), ms=3.5, lw=1.2, label="Poisson, same mean")
ax.set_xticks(xs)
ax.set_xticklabels(names, fontsize=7)
ax.set_yscale("log")
ax.set_ylim(1e-4, 1.2)
ax.legend(frameon=False, fontsize=7.5, labelcolor=P.ink(), loc="upper right")
ax.text(0.97, 0.62, f"mean {mean:.0f}\nvariance / mean ≈ {counts.var() / mean:.1e}".replace("e+04", " × 10⁴"),
        transform=ax.transAxes, ha="right", fontsize=7.5, color=P.ink())
charts.style_axes(ax, "resistant mutants per culture", "fraction of cultures")
charts.title(ax, "B  Branching growth: fluctuation test")

# C: Kimura fixation probability
ax = axs[1, 0]
N = 1000
S = np.linspace(-6, 12, 400)
s = S / (4 * N)
p = 1 / (2 * N)
with np.errstate(divide="ignore", invalid="ignore"):
    u = np.where(np.abs(s) < 1e-12, p, (1 - np.exp(-4 * N * s * p)) / (1 - np.exp(-4 * N * s)))
ax.plot(S, u / p, color=charts.line("enzyme"), lw=1.8, label="diffusion, Eq. (23.13)")
ax.plot(S[S > 2], 2 * s[S > 2] / p, color=P.muted(), lw=1.0, ls="--", label="u = 2s (large S)")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.axvspan(-1, 1, color=P.light("neutral"), lw=0)
ax.text(0, 9.2, "nearly\nneutral", ha="center", fontsize=7.5, color=P.ink())
ax.set_yscale("log")
ax.set_ylim(0.01, 30)
ax.legend(frameon=False, fontsize=7.5, labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "$S = 4N_e s$", "fixation probability / neutral value")
charts.title(ax, "C  Diffusion: fate of a new mutation")

# D: polygenic score accuracy
ax = axs[1, 1]
n = np.logspace(3, 7, 300)
for h2, Me, tok, ls in [(0.5, 6e4, "dna", "-"), (0.2, 6e4, "rna", "-"), (0.5, 2e4, "enzyme", "--")]:
    ax.plot(n, h2 / (1 + Me / (n * h2)), color=charts.line(tok), lw=1.8, ls=ls,
            label=f"$h^2$ = {h2}, $M_e$ = {Me / 1e3:.0f} 000")
    ax.axhline(h2, color=P.muted(), lw=0.6, ls=":")
ax.set_xscale("log")
ax.set_ylim(0, 0.55)
ax.legend(frameon=False, fontsize=7.5, labelcolor=P.ink(), loc="center right", bbox_to_anchor=(1.0, 0.68))
charts.style_axes(ax, "GWAS sample size N", "expected R² of the score")
charts.title(ax, "D  High-dimensional regression: prediction")

fig.tight_layout()
