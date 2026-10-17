"""Density of Y = r cos X for X ~ U(0, 2 pi): two inverse branches give 1 / (pi sqrt(r^2 - y^2))."""

import numpy as np
import matplotlib.pyplot as plt

r = 1.0
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axes[0]
x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, r * np.cos(x), color="C0", lw=2, label="y = r cos x")
y0 = 0.3
x1 = np.arccos(y0 / r)
ax.axhline(y0, color="C3", ls="--", lw=1)
for xi in [x1, 2 * np.pi - x1]:
    ax.plot([xi, xi], [0, y0], color="C3", lw=1)
    ax.plot([xi], [y0], "o", color="C3")
ax.text(x1 + 0.1, y0 + 0.08, "h1(y)", fontsize=9)
ax.text(2 * np.pi - x1 + 0.1, y0 + 0.08, "h2(y)", fontsize=9)
ax.axhline(0, color="gray", lw=0.6)
ax.set_xlabel("x")
ax.set_title("Two preimages of each y in (-r, r)")
ax.legend(fontsize=8, loc="lower left")

ax = axes[1]
rng = np.random.default_rng(0)
sample = r * np.cos(rng.uniform(0, 2 * np.pi, 100000))
ax.hist(sample, bins=60, density=True, color="C1", alpha=0.5, label="100000 simulated values")
y = np.linspace(-0.995, 0.995, 400)
ax.plot(y, 1 / (np.pi * np.sqrt(r**2 - y**2)), color="C0", lw=2, label="1 / (pi sqrt(r^2 - y^2))")
ax.set_ylim(0, 3)
ax.set_xlabel("y")
ax.set_title("Density of Y = r cos X, r = 1")
ax.legend(fontsize=8)
fig.tight_layout()
