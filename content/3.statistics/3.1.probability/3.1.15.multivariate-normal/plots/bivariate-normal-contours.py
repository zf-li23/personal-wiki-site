"""Density contours of the standard bivariate normal with correlation rho, and the regression line E(Y | X = x) = rho x."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(x, x)
fig, axes = plt.subplots(1, 3, figsize=(13, 4.3), sharey=True)
for ax, rho in zip(axes, [-0.7, 0.0, 0.7]):
    q = (X**2 - 2 * rho * X * Y + Y**2) / (1 - rho**2)
    f = np.exp(-q / 2) / (2 * np.pi * np.sqrt(1 - rho**2))
    ax.contour(X, Y, f, levels=8, cmap="viridis")
    ax.plot(x, rho * x, color="C3", lw=1.5, label="E(Y | X = x) = rho x")
    ax.set_aspect("equal")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_title(f"rho = {rho}")
    ax.set_xlabel("x")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("y")
axes[0].legend(loc="lower left", fontsize=8)
fig.tight_layout()
