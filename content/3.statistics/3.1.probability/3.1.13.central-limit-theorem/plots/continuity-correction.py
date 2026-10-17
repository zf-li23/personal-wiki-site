"""Bin(36, 0.5) pmf with the N(18, 9) density; shaded area over [k - 0.5, k + 0.5] approximates P(S_n = k)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n, p = 36, 0.5
mu, sd = n * p, np.sqrt(n * p * (1 - p))
k = np.arange(6, 31)
x = np.linspace(5, 31, 600)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.vlines(k, 0, stats.binom.pmf(k, n, p), color="C0", lw=3, label="P(S_n = k), exact")
ax.plot(x, stats.norm.pdf(x, mu, sd), color="C3", lw=1.5, label="N(18, 9) density")
k0 = 19
xs = np.linspace(k0 - 0.5, k0 + 0.5, 50)
ax.fill_between(xs, stats.norm.pdf(xs, mu, sd), color="C1", alpha=0.5, label="area for k = 19")
xs = np.linspace(5, 21.5, 300)
ax.fill_between(xs, stats.norm.pdf(xs, mu, sd), color="C2", alpha=0.15, label="P(S_n <= 21) with correction")
ax.axvline(21.5, color="C2", lw=1, ls="--")
ax.set_xlabel("k")
ax.set_ylabel("probability / density")
ax.set_title("Continuity correction for Bin(36, 0.5)")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
