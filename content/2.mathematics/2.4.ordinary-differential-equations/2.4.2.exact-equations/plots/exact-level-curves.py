"""Integral curves of an exact equation as level curves of Phi = x^2 sin y + x^3 y + y^3/3."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
y = np.linspace(-2.5, 2.5, 400)
X, Y = np.meshgrid(x, y)
Phi = X**2 * np.sin(Y) + X**3 * Y + Y**3 / 3

fig, ax = plt.subplots(figsize=(6.5, 6))
levels = np.linspace(-6, 6, 25)
cs = ax.contour(X, Y, Phi, levels=levels, cmap="viridis", linewidths=1.2, linestyles="solid")
fig.colorbar(cs, ax=ax, label="C")
ax.contour(X, Y, Phi, levels=[0], colors="C3", linewidths=2.0)
ax.plot([], [], color="C3", lw=2, label="Phi = 0")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Level curves Phi(x, y) = x^2 sin y + x^3 y + y^3/3 = C")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
