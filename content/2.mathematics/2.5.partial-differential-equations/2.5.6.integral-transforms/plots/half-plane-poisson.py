"""Dirichlet problem in the upper half-plane: Poisson kernel and the solution for indicator boundary data."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
x = np.linspace(-4, 4, 801)
for i, y in enumerate([0.25, 0.5, 1.0, 2.0]):
    ax.plot(x, y / (np.pi * (x**2 + y**2)), color=f"C{i}", lw=1.8, label=f"y = {y}")
ax.set_xlim(-4, 4)
ax.set_xlabel("x")
ax.set_title("Poisson kernel P_y(x) = y / (pi (x^2 + y^2))")
ax.legend(fontsize=9)

ax = axes[1]
X, Y = np.meshgrid(np.linspace(-3, 3, 400), np.linspace(1e-3, 3, 300))
U = (np.arctan((1 - X) / Y) + np.arctan((1 + X) / Y)) / np.pi
pc = ax.pcolormesh(X, Y, U, cmap="viridis", vmin=0, vmax=1, shading="auto")
cs = ax.contour(X, Y, U, levels=[0.1, 0.2, 0.3, 0.5, 0.7, 0.9], colors="w", linewidths=1)
ax.clabel(cs, fontsize=8, fmt="%.1f")
ax.plot([-1, 1], [0, 0], color="C3", lw=4)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("u = 1 on |x| < 1, u = 0 elsewhere on y = 0")
fig.colorbar(pc, ax=ax, shrink=0.8)
fig.tight_layout()
