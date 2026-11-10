"""Smoothing splines for the simulated temperature series with three values of the penalty
lambda: a small lambda nearly interpolates, a large one approaches the least squares line."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_smoothing_spline

rng = np.random.default_rng(42)
x = np.linspace(1900, 2025, 80)
trend = 14 + 1.2 * (x - 1900) / (40 + (x - 1900))
y = trend + 0.15 * np.sin(x / 2) + rng.normal(0, 0.08, len(x))
grid = np.linspace(1900, 2025, 600)

fig, ax = plt.subplots(figsize=(8.4, 4.4))
ax.plot(x, y, "o", color="0.55", ms=3.5)
for lam, color in [(0.5, "C1"), (500.0, "C0"), (1e7, "C2")]:
    spline = make_smoothing_spline(x, y, lam=lam)
    ax.plot(grid, spline(grid), color=color, lw=1.7, label=f"lambda = {lam:g}")
b1, b0 = np.polyfit(x, y, 1)
ax.plot(grid, b0 + b1 * grid, color="0.2", ls=":", lw=1.2, label="least squares line")
ax.set_xlabel("year")
ax.set_ylabel("annual mean temperature / °C")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
