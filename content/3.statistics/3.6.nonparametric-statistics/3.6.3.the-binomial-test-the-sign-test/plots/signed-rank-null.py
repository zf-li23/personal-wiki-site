"""Exact null distribution of the Wilcoxon signed-rank statistic, without and with ties."""

import itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def exact_dist(scores):
    """Null distribution of the sum of the scores receiving a + sign (all 2^n sign patterns)."""
    totals = {}
    for signs in itertools.product([0, 1], repeat=len(scores)):
        s = round(sum(a * b for a, b in zip(signs, scores)), 6)
        totals[s] = totals.get(s, 0) + 1
    v = np.array(sorted(totals))
    return v, np.array([totals[t] for t in v]) / 2 ** len(scores)


fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))

# Left: n = 12, no ties, with the normal approximation
n = 12
v, pr = exact_dist(range(1, n + 1))
mu, sd = n * (n + 1) / 4, np.sqrt(n * (n + 1) * (2 * n + 1) / 24)
ax = axes[0]
ax.bar(v, pr, width=0.8, color="C0", alpha=0.6, label="exact, 4096 sign patterns")
xx = np.linspace(0, n * (n + 1) / 2, 400)
ax.plot(xx, stats.norm.pdf(xx, mu, sd), color="C3", lw=1.5, label="normal, mean 39, var 162.5")
ax.axvline(7, color="C2", lw=1.5, ls="--", label="observed S- = 7 (drug data)")
ax.set_xlabel("S+ (or S-)")
ax.set_ylabel("probability")
ax.set_title("Null distribution of the signed-rank statistic, n = 12", fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Right: n = 7 with ties (midranks 2.5, 2.5, 2.5, 2.5, 6, 6, 6) versus ranks 1..7
ax = axes[1]
v1, p1 = exact_dist(range(1, 8))
v2, p2 = exact_dist([2.5, 2.5, 2.5, 2.5, 6, 6, 6])
ax.bar(v1 - 0.18, p1, width=0.36, color="C0", alpha=0.6, label="no ties: ranks 1, ..., 7")
ax.bar(v2 + 0.18, p2, width=0.36, color="C1", alpha=0.8,
       label="ties: scores 2.5 (x4), 6 (x3)")
ax.set_xlabel("S-")
ax.set_ylabel("probability")
ax.set_title("Null distribution of S-, n = 7, with and without ties", fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
