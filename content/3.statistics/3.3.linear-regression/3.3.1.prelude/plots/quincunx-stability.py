"""Galton's quincunx as a model of heredity: contraction by the chutes plus spreading by the pegs."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sigma1 = 1.0          # parent standard deviation
c = 0.8               # contraction factor of the inclined chutes
sigma = np.sqrt(sigma1**2 - c**2 * sigma1**2)   # peg noise that keeps the population stable

x = np.linspace(-4, 4, 400)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
ax.plot(x, stats.norm.pdf(x, 0, sigma1), color="C0", lw=2, label="parents F ~ N(0, 1)")
ax.plot(x, stats.norm.pdf(x, 0, c * sigma1), color="C1", lw=2, ls="--", label="after chutes Z = 0.8 F ~ N(0, 0.64)")
ax.plot(x, stats.norm.pdf(x, 0, sigma), color="C2", lw=1.5, ls=":", label="pegs X ~ N(0, 0.36)")
ax.plot(x, stats.norm.pdf(x, 0, np.sqrt(c**2 * sigma1**2 + sigma**2)), color="C3", lw=1.2,
        label="offspring S = Z + X ~ N(0, 1)")
ax.set_title("Contraction plus spreading keeps the dispersion stable", fontsize=10)
ax.set_xlabel("deviation from the center")
ax.set_ylabel("density")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)

ax = axes[1]
groups = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
weights = stats.norm.pdf(groups, 0, sigma1)
weights = weights / weights.sum()
total = np.zeros_like(x)
for k, (f, w) in enumerate(zip(groups, weights)):
    comp = w * stats.norm.pdf(x, c * f, sigma)
    total += comp
    ax.fill_between(x, comp, alpha=0.35, color=f"C{k}")
    ax.annotate("", xy=(c * f, w * stats.norm.pdf(0, 0, sigma) + 0.02), xytext=(f, w * stats.norm.pdf(0, 0, sigma) + 0.12),
                arrowprops=dict(arrowstyle="->", color=f"C{k}", lw=1.2))
ax.plot(x, total, color="black", lw=1.5, label="sum of the five offspring groups")
ax.set_title("Offspring of parent groups f = -2, ..., 2 land near 0.8 f", fontsize=10)
ax.set_xlabel("deviation from the center")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
