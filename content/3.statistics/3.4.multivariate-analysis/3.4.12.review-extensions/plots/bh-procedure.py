"""Benjamini-Hochberg versus Bonferroni on simulated z-tests: 1000 hypotheses, 100 with a true effect."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

rng = np.random.default_rng(0)
m, m1, alpha = 1000, 100, 0.05
z = rng.normal(size=m)
z[:m1] += 3.0
p = 2 * norm.sf(np.abs(z))
order = np.argsort(p)
ps = p[order]
ranks = np.arange(1, m + 1)
below = np.nonzero(ps <= ranks / m * alpha)[0]
k = below.max() + 1 if below.size else 0
n_bonf = int(np.sum(p < alpha / m))
false_bh = int(np.sum(order[:k] >= m1))

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
show = 150
for ax, logscale in zip(axes, [False, True]):
    ax.scatter(ranks[:show], ps[:show], s=10, color="C0", label="sorted p-values")
    ax.plot(ranks[:show], ranks[:show] / m * alpha, color="C1", label="BH line i alpha / m")
    ax.axhline(alpha / m, color="C3", ls="--", label="Bonferroni alpha / m")
    ax.axvline(k + 0.5, color="gray", ls=":", lw=1)
    ax.set_xlabel("rank i")
    ax.set_ylabel("p-value")
    if logscale:
        ax.set_yscale("log")
        ax.set_title("log scale")
    else:
        ax.set_ylim(0, 0.02)
        ax.set_title(f"BH rejects {k} ({false_bh} false); Bonferroni rejects {n_bonf}")
axes[0].legend(fontsize=8, loc="upper left")
fig.tight_layout()
