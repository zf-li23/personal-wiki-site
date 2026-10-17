"""Bivariate normal density: surface and contours for rho = 0 and rho = 0.75."""

import numpy as np
import matplotlib.pyplot as plt


def density(x, y, rho):
    q = (x**2 - 2 * rho * x * y + y**2) / (1 - rho**2)
    return np.exp(-q / 2) / (2 * np.pi * np.sqrt(1 - rho**2))


g = np.linspace(-3, 3, 121)
X, Y = np.meshgrid(g, g)
fig = plt.figure(figsize=(9, 8))
for j, rho in enumerate([0.0, 0.75]):
    Z = density(X, Y, rho)
    ax = fig.add_subplot(2, 2, j + 1, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0, antialiased=True, rstride=2, cstride=2)
    ax.set_title(f"density, rho = {rho}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zticks([])
    ax.view_init(elev=30, azim=-60)
    ax2 = fig.add_subplot(2, 2, j + 3)
    cs = ax2.contour(X, Y, Z, levels=[0.01, 0.03, 0.06, 0.1, 0.15, 0.2], cmap="viridis")
    ax2.clabel(cs, fontsize=7)
    ax2.set_aspect("equal")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_title(f"contours, rho = {rho}")
    ax2.grid(alpha=0.3)
fig.tight_layout()
