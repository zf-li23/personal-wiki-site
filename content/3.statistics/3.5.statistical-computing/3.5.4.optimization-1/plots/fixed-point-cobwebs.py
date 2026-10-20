"""Cobweb diagrams of three fixed-point iterations for x + log(x) = 0."""

import numpy as np
import matplotlib.pyplot as plt

maps = [
    ("G1(x) = -log(x): |G1'(x*)| = 1.76, diverges", lambda x: -np.log(x), 0.6, (0.25, 0.95)),
    ("G2(x) = exp(-x): |G2'(x*)| = 0.57", lambda x: np.exp(-x), 0.15, (0.0, 1.05)),
    ("G3(x) = (x + exp(-x))/2: |G3'(x*)| = 0.22", lambda x: (x + np.exp(-x)) / 2, 0.15, (0.0, 1.05)),
]

fig, axes = plt.subplots(1, 3, figsize=(13, 4.4))
for ax, (title, G, x0, (lo, hi)) in zip(axes, maps):
    grid = np.linspace(max(lo, 1e-3), hi, 300)
    ax.plot(grid, G(grid), color="C0", lw=1.8, label="y = G(x)")
    ax.plot(grid, grid, color="gray", lw=1, label="y = x")
    x = x0
    for _ in range(12):
        y = G(x)
        if not (lo <= y <= hi and lo <= G(y) <= hi):
            break
        ax.plot([x, x], [x, y], color="C3", lw=0.9)
        ax.plot([x, y], [y, y], color="C3", lw=0.9)
        x = y
    ax.plot(0.567143, 0.567143, "o", color="black", ms=5)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("x")
    ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
