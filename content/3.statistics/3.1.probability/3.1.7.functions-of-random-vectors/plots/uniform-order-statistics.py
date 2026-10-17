"""Densities of the order statistics of n = 5 iid U(0,1) variables: U_(k) ~ Beta(k, n - k + 1)."""

from math import factorial

import numpy as np
import matplotlib.pyplot as plt

n = 5
x = np.linspace(0, 1, 400)
rng = np.random.default_rng(0)
samples = np.sort(rng.uniform(size=(20000, n)), axis=1)

fig, ax = plt.subplots(figsize=(7, 4.2))
for k in range(1, n + 1):
    c = factorial(n) / (factorial(k - 1) * factorial(n - k))
    dens = c * x ** (k - 1) * (1 - x) ** (n - k)
    ax.plot(x, dens, color=f"C{k - 1}", lw=1.8, label=f"k = {k}: Beta({k}, {n - k + 1})")
    ax.hist(samples[:, k - 1], bins=60, range=(0, 1), density=True, color=f"C{k - 1}", alpha=0.15)
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.set_title("order statistics of 5 uniform points (curves: exact, bars: simulation)")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
