"""Exact density of a sum of n i.i.d. U(-1,1) variables versus the normal approximation N(0, n/3)."""

import numpy as np
import matplotlib.pyplot as plt
from math import comb, factorial
from scipy import stats


def density(x, n):
    out = np.zeros_like(x)
    for i, xi in enumerate(x):
        if abs(xi) > n:
            continue
        top = int(np.floor((n + xi) / 2))
        s = sum((-1) ** k * comb(n, k) * (n + xi - 2 * k) ** (n - 1) for k in range(top + 1))
        out[i] = s / (2**n * factorial(n - 1))
    return out


fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
for ax, n in zip(axes, [2, 4, 10]):
    x = np.linspace(-n, n, 600)
    ax.plot(x, density(x, n), lw=1.8, label="exact density")
    ax.plot(x, stats.norm.pdf(x, 0, np.sqrt(n / 3)), lw=1.5, ls="--", label="N(0, n/3)")
    ax.set_title(f"n = {n}")
    ax.set_xlabel("x")
    ax.grid(alpha=0.3)
axes[0].legend(fontsize=8)
fig.tight_layout()
