"""Exact density of S_n = sum of n iid U(-1,1) variables versus the normal approximation N(0, n/3)."""

from math import comb, factorial

import numpy as np
import matplotlib.pyplot as plt


def exact_density(x, n):
    out = np.zeros_like(x)
    inside = np.abs(x) <= n
    xi = x[inside]
    total = np.zeros_like(xi)
    for k in range(n + 1):
        term = (n + xi - 2 * k)
        total += np.where(term > 0, (-1) ** k * comb(n, k) * np.clip(term, 0, None) ** (n - 1), 0.0)
    out[inside] = total / (2**n * factorial(n - 1))
    return out


fig, axes = plt.subplots(2, 3, figsize=(10, 5.6), sharey=False)
for ax, n in zip(axes.flat, [1, 2, 3, 4, 6, 10]):
    x = np.linspace(-n - 0.5, n + 0.5, 800)
    if n == 1:
        f = np.where(np.abs(x) <= 1, 0.5, 0.0)
    else:
        f = exact_density(x, n)
    s2 = n / 3
    g = np.exp(-x**2 / (2 * s2)) / np.sqrt(2 * np.pi * s2)
    ax.plot(x, f, color="C0", lw=1.8, label="exact")
    ax.plot(x, g, color="C3", lw=1.3, ls="--", label="N(0, n/3)")
    ax.set_title(f"n = {n}")
    ax.set_xlabel("x")
    ax.grid(alpha=0.3)
axes[0, 0].legend(fontsize=8)
fig.tight_layout()
