"""A continuous X and a group indicator: Simpson's paradox, parallel lines, interaction."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))

# Simpson's paradox: positive slope within groups, negative pooled slope
ax = axes[0]
xs, ys = [], []
for g, (cx, cy, col) in enumerate([(2.5, 7.5, "C0"), (9.5, 2.5, "C3")]):
    x = cx + rng.uniform(-2, 2, 25)
    y = cy + 1.0 * (x - cx) + rng.normal(0, 0.6, 25)
    xs.append(x)
    ys.append(y)
    b, a = np.polyfit(x, y, 1)
    grid = np.array([x.min(), x.max()])
    ax.plot(x, y, "o", ms=4, color=col, alpha=0.8, label=f"group {g + 1}")
    ax.plot(grid, a + b * grid, color=col, lw=2)
x, y = np.concatenate(xs), np.concatenate(ys)
b, a = np.polyfit(x, y, 1)
grid = np.array([0, 12])
ax.plot(grid, a + b * grid, color="0.2", ls="--", lw=2, label="pooled")
ax.set_title("Simpson's paradox")
ax.legend(fontsize=8)

# additive model: parallel lines
x = rng.uniform(0, 10, 40)
g = rng.integers(0, 2, 40)
for ax, slopes, title in [(axes[1], (1.0, 1.0), "Additive: parallel lines"),
                          (axes[2], (1.0, 0.3), "Interaction: different slopes")]:
    y = 2 + 3 * g + np.where(g == 0, slopes[0], slopes[1]) * x + rng.normal(0, 0.8, 40)
    for k, col in [(0, "C0"), (1, "C3")]:
        m = g == k
        b, a = np.polyfit(x[m], y[m], 1)
        grid = np.array([0, 10])
        ax.plot(x[m], y[m], "o", ms=4, color=col, alpha=0.8, label=f"X2 = {k}")
        ax.plot(grid, a + b * grid, color=col, lw=2)
    ax.set_title(title)
    ax.legend(fontsize=8)
for ax in axes:
    ax.set_xlabel("X1")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("Y")
fig.tight_layout()
