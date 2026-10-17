"""Poisson PMFs, the Poisson approximation of Bin(n, lambda/n), and Rutherford-Geiger alpha-particle counts."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(14, 4.2))

ax = axes[0]
k = np.arange(0, 16)
for i, lam in enumerate([1, 2, 3, 4, 5, 6]):
    ax.plot(k, stats.poisson.pmf(k, lam), "o-", ms=3, lw=1.2, color=f"C{i}", label=f"lambda = {lam}")
ax.set_title("Poi(lambda)")
ax.set_xlabel("k")
ax.set_ylabel("P(X = k)")
ax.legend(fontsize=8)

ax = axes[1]
lam = 3
k = np.arange(0, 12)
w = 0.2
for j, n in enumerate([6, 15, 60]):
    ax.bar(k + (j - 1.5) * w, stats.binom.pmf(k, n, lam / n), width=w, color=f"C{j}", label=f"Bin({n}, {lam}/{n})")
ax.bar(k + 1.5 * w, stats.poisson.pmf(k, lam), width=w, color="C3", label="Poi(3)")
ax.set_title("Bin(n, lambda/n) approaches Poi(lambda)")
ax.set_xlabel("k")
ax.legend(fontsize=8)

ax = axes[2]
counts = np.array([57, 203, 383, 525, 532, 408, 273, 139, 45, 27, 16])
N = counts.sum()
lam = 10094 / N
k = np.arange(0, 11)
pois = stats.poisson.pmf(k, lam)
pois[-1] = stats.poisson.sf(9, lam)
ax.plot(k, counts / N, "o-", color="C3", label="observed frequency m_k / N")
ax.plot(k, pois, "s--", color="C0", label=f"Poi({lam:.2f})")
ax.set_xticks(k)
ax.set_xticklabels([str(i) for i in range(10)] + ["10+"])
ax.set_title("Rutherford-Geiger (1910), N = 2608 intervals")
ax.set_xlabel("alpha particles per 7.5 s")
ax.legend(fontsize=8)
fig.tight_layout()
