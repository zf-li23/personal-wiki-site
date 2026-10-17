"""Variance of the portfolio w X + (1 - w) Y with Var X = Var Y = 1 for several correlations."""

import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0, 1, 300)
fig, ax = plt.subplots(figsize=(7, 4.2))
for i, rho in enumerate([1.0, 0.5, 0.0, -0.5, -1.0]):
    v = w**2 + (1 - w) ** 2 + 2 * w * (1 - w) * rho
    ax.plot(w, v, color=f"C{i}", lw=1.8, label=f"rho = {rho}")
ax.set_xlabel("weight w on asset X")
ax.set_ylabel("Var(w X + (1 - w) Y)")
ax.set_title("diversification: lower correlation gives lower risk")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
