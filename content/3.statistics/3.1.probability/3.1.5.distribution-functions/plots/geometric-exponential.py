"""Geometric CDF on the grid n*delta versus the exponential CDF 1 - exp(-lambda x)."""

import numpy as np
import matplotlib.pyplot as plt

lam = 1.0
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
x = np.linspace(0, 5, 500)
for ax, delta in zip(axes, [0.5, 0.1]):
    p = 1 - np.exp(-lam * delta)
    n = np.floor(x / delta)
    ax.plot(x, 1 - (1 - p) ** n, color="C1", lw=1.5, label=f"geometric: 1 - (1 - p)^floor(x / delta), p = {p:.3f}")
    ax.plot(x, 1 - np.exp(-lam * x), color="C0", lw=2, label="exponential: 1 - exp(-x)")
    ax.set_title(f"delta = {delta}")
    ax.set_xlabel("x")
    ax.legend(fontsize=8, loc="lower right")
axes[0].set_ylabel("F(x)")
fig.tight_layout()
