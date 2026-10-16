"""Integral curves 2x^2 y + y^2 = C and the solution with y(0) = 2."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500)
y = np.linspace(-6, 4, 500)
X, Y = np.meshgrid(x, y)
F = 2 * X**2 * Y + Y**2

fig, ax = plt.subplots(figsize=(7, 5))
ax.contour(X, Y, F, levels=[-12, -6, -2, -0.5, 0.5, 1, 2, 8, 12], colors="0.55",
           linewidths=0.9, linestyles="solid")
ax.contour(X, Y, F, levels=[0], colors="0.55", linewidths=0.9, linestyles="solid")
ax.plot(x, -x**2 + np.sqrt(x**4 + 4), color="C0", lw=2.4,
        label="y(0) = 2:  y = -x^2 + sqrt(x^4 + 4)  (C = 4)")
ax.plot([0], [2], "o", color="C3")
ax.set_xlim(-3, 3)
ax.set_ylim(-6, 4)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Integral curves 2x^2 y + y^2 = C")
ax.legend(loc="lower center", fontsize=9)
fig.tight_layout()
