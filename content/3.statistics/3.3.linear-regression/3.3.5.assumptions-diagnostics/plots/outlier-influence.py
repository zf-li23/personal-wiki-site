"""An outlier near the center of X shifts the line; an outlier at an extreme X tilts it."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = np.arange(1, 100, 5, dtype=float)
y = 30 + 50 * x + 200 * rng.normal(size=x.size)
cases = [
    ("outlier at X = 50 (near the mean of X)", 50.0, 30 + 50 * 50 + 10000, "upper right"),
    ("outlier at X = 100 (extreme X)", 100.0, 30 + 50 * 100 - 10000, "upper left"),
]
grid = np.array([-2.0, 102.0])
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
for ax, (title, xo, yo, loc) in zip(axes, cases):
    xa, ya = np.append(x, xo), np.append(y, yo)
    b1a, b0a = np.polyfit(xa, ya, 1)
    b1, b0 = np.polyfit(x, y, 1)
    ax.plot(x, y, "o", color="C0", ms=4)
    ax.plot([xo], [yo], "s", color="C3", ms=7)
    ax.plot(grid, b0a + b1a * grid, color="C3", lw=1.5, label=f"with outlier: b1 = {b1a:.1f}")
    ax.plot(grid, b0 + b1 * grid, color="C0", lw=1.5, ls="--", label=f"without outlier: b1 = {b1:.1f}")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend(fontsize=9, loc=loc)
    ax.grid(alpha=0.3)
fig.tight_layout()
