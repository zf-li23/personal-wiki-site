"""Conditional densities of X given Y = y for a standard bivariate normal with rho = 0.75."""

import numpy as np
import matplotlib.pyplot as plt

rho = 0.75
x = np.linspace(-4, 4, 400)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

ax = axes[0]
g = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(g, g)
Z = np.exp(-(X**2 - 2 * rho * X * Y + Y**2) / (2 * (1 - rho**2))) / (2 * np.pi * np.sqrt(1 - rho**2))
ax.contour(X, Y, Z, levels=8, cmap="Greys", linewidths=0.8)
ys = [-1.5, 0.0, 1.5]
colors = ["C0", "C1", "C2"]
for y0, c in zip(ys, colors):
    ax.axhline(y0, color=c, lw=1.4, ls="--")
ax.plot(rho * g, g, color="C3", lw=1.6, label="E(X | Y = y) = rho * y")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal")
ax.set_title("slices of the joint density at fixed y")
ax.legend(loc="upper left", fontsize=8)

ax = axes[1]
s = np.sqrt(1 - rho**2)
for y0, c in zip(ys, colors):
    f = np.exp(-((x - rho * y0) ** 2) / (2 * s**2)) / (np.sqrt(2 * np.pi) * s)
    ax.plot(x, f, color=c, lw=1.8, label=f"f(x | y = {y0})")
ax.plot(x, np.exp(-x**2 / 2) / np.sqrt(2 * np.pi), color="0.5", lw=1.2, ls=":", label="marginal f_X(x)")
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.set_title("conditional densities N(rho y, 1 - rho^2)")
ax.legend(fontsize=8)
fig.tight_layout()
