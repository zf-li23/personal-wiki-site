"""Binomial PMFs Bin(n, p) for several n, with p = 0.2, 0.5, 0.8."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=True)
ns = [3, 6, 9, 12, 15, 30]
for ax, p in zip(axes, [0.2, 0.5, 0.8]):
    for i, n in enumerate(ns):
        k = np.arange(0, n + 1)
        ax.plot(k, stats.binom.pmf(k, n, p), "o-", ms=3, lw=1.2, color=f"C{i}", label=f"n = {n}")
    ax.set_title(f"Bin(n, p), p = {p}")
    ax.set_xlabel("k")
    ax.set_xlim(-0.5, 30.5)
axes[0].set_ylabel("P(X = k)")
axes[0].legend(fontsize=8)
fig.tight_layout()
