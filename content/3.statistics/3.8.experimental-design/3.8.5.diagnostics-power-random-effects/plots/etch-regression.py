"""Etch rate against RF power: level means of the fixed-effects model, linear and quadratic fits."""

import numpy as np
import matplotlib.pyplot as plt

x = np.repeat([160, 180, 200, 220], 5).astype(float)
y = np.array([575, 542, 530, 539, 570, 565, 593, 590, 579, 610,
              600, 651, 610, 637, 629, 725, 700, 715, 685, 710], float)
b1 = np.polyfit(x, y, 1)
b2 = np.polyfit(x, y, 2)
grid = np.linspace(155, 225, 200)
levels = np.unique(x)
means = [y[x == v].mean() for v in levels]

fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.scatter(x, y, s=20, alpha=0.6, label="observations")
ax.plot(levels, means, "s", ms=8, color="C3", label="level means (fixed-effects model)")
ax.plot(grid, np.polyval(b1, grid), color="C1", label=f"linear: {b1[1]:.2f} + {b1[0]:.3f} x")
ax.plot(grid, np.polyval(b2, grid), color="C2", ls="--", label="quadratic fit")
ax.set_xlabel("RF power x (W)")
ax.set_ylabel("etch rate (angstrom/min)")
ax.set_title("Quantitative factor: regression vs fixed effects")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
