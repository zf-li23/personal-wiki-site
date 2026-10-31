# Statistics of sequence comparison. Pairs of random DNA sequences (uniform base composition), scored
# +1 per match and -1 per mismatch (expected score per position -1/2), and the best ungapped local
# alignment found by Kadane's maximum-subarray scan over all diagonals (equivalent to Smith-Waterman
# without gaps). A: distribution of the best score for 1000 random pairs of length 200 against the
# Gumbel (extreme-value) distribution fitted by its moments, and for 1000 related pairs (one ancestral
# random sequence, each copy mutated independently at 20 % of sites): the related pairs score far above
# the random tail. B: mean best score of random pairs against log(m n), with m = n the sequence length:
# a straight line of slope 1/lambda, with lambda = ln 3 solving (1/4) e^lambda + (3/4) e^-lambda = 1, the logarithmic growth of chance similarity (Karlin and Altschul 1990).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def best_local(a, b):
    """Best ungapped local alignment score of integer sequences a, b (match +1, mismatch -1)."""
    n, m = a.size, b.size
    best = 0
    for d in range(-(n - 1), m):
        if d >= 0:
            s = np.where(a[: min(n, m - d)] == b[d: d + min(n, m - d)], 1, -1)
        else:
            L = min(n + d, m)
            s = np.where(a[-d: -d + L] == b[:L], 1, -1)
        cur = 0
        c = np.cumsum(s)
        # max over subarrays = max_j (c_j - min_{i<j} c_i) with c_{-1} = 0
        run_min = np.minimum.accumulate(np.r_[0, c[:-1]])
        best = max(best, int((c - np.minimum(run_min, 0)).max()) if c.size else 0)
    return best


def mutate(s, frac):
    t = s.copy()
    hit = rng.random(s.size) < frac
    t[hit] = (t[hit] + rng.integers(1, 4, hit.sum())) % 4
    return t


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
n = 200
rand = np.array([best_local(rng.integers(0, 4, n), rng.integers(0, 4, n)) for _ in range(1000)])
rel = []
for _ in range(1000):
    anc = rng.integers(0, 4, n)
    rel.append(best_local(mutate(anc, 0.2), mutate(anc, 0.2)))
rel = np.array(rel)
ax = axs[0]
bins = np.arange(0.5, 90.5, 1)
ax.hist(rand, bins=bins, density=True, color=P.fill("neutral"), edgecolor=P.edge("neutral"), label="random pairs")
ax.hist(rel, bins=bins, density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), alpha=0.8, label="related pairs (20 % mutated each)")
beta = rand.std() * np.sqrt(6) / np.pi
mu = rand.mean() - 0.5772 * beta
x = np.linspace(5, 40, 300)
z = (x - mu) / beta
ax.plot(x, np.exp(-z - np.exp(-z)) / beta, color=charts.line("negative"), lw=1.8, label="Gumbel fit to random pairs")
ax.set_xlim(0, 90)
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "best local alignment score", "probability density")
charts.title(ax, "A   Chance similarity has an extreme-value tail")

ax = axs[1]
Ls = np.array([25, 50, 100, 200, 400, 800])
means = [np.mean([best_local(rng.integers(0, 4, L), rng.integers(0, 4, L)) for _ in range(max(40, 6000 // L))]) for L in Ls]
lmn = np.log(Ls.astype(float) ** 2)
ax.plot(lmn, means, "o", color=charts.line("dna"), ms=6)
sl, ic = np.polyfit(lmn, means, 1)
xx = np.linspace(lmn[0], lmn[-1], 50)
ax.plot(xx, sl * xx + ic, color=P.muted(), lw=1.0, ls="--", label=f"fitted slope {sl:.2f}; theory 1/$\\lambda$ = 1/ln 3 = 0.91")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "$\\ln(mn)$", "mean best score of random pairs")
charts.title(ax, "B   Logarithmic growth with search space")
fig.tight_layout()
