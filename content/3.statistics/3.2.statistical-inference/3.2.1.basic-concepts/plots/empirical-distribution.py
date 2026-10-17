"""Empirical distribution functions of standard normal samples of size 10 and 100."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
grid = np.linspace(-3.2, 3.2, 400)
for ax, n in zip(axes, [10, 100]):
    x = np.sort(np.random.normal(size=n))
    steps = np.concatenate([[-3.2], x, [3.2]])
    heights = np.arange(n + 1) / n
    ax.hlines(heights, steps[:-1], steps[1:], color="C0", lw=1.4, label="EDF $F_n(x)$")
    if n <= 20:
        ax.plot(x, heights[1:], "o", color="C0", ms=4)
    ax.plot(grid, norm.cdf(grid), color="C3", lw=1.4, label="true CDF $F(x)$")
    d = np.max(np.maximum(np.abs(heights[1:] - norm.cdf(x)), np.abs(heights[:-1] - norm.cdf(x))))
    ax.set_title(f"n = {n},  D_n = {d:.3f}")
    ax.set_xlabel("x")
    ax.set_xlim(-3.2, 3.2)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("probability")
axes[0].legend(loc="upper left")
fig.tight_layout()
