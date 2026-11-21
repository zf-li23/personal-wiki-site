"""Rocket propellant Latin square: burning rate against batch, operator and formulation."""

import numpy as np
import matplotlib.pyplot as plt

letters = ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"]
rate = np.array([[24, 20, 19, 24, 24],
                 [17, 24, 30, 27, 36],
                 [18, 38, 26, 27, 21],
                 [26, 31, 26, 23, 22],
                 [22, 30, 20, 29, 31]])
batch = np.repeat(np.arange(5), 5)
operator = np.tile(np.arange(5), 5)
formulation = np.array([letters[i][k] for i in range(5) for k in range(5)])
y = rate.ravel()

groups = [("batch", batch, [0, 1, 2, 3, 4], [str(i + 1) for i in range(5)]),
          ("operator", operator, [0, 1, 2, 3, 4], [str(i + 1) for i in range(5)]),
          ("formulation", formulation, list("ABCDE"), list("ABCDE"))]

rng = np.random.default_rng(0)
fig, axes = plt.subplots(1, 3, figsize=(10, 3.8), sharey=True)
for ax, (name, f, levels, labels) in zip(axes, groups):
    for pos, lev in enumerate(levels):
        vals = y[f == lev]
        ax.scatter(pos + rng.uniform(-0.12, 0.12, vals.size), vals, s=22, alpha=0.7, color="C0")
        ax.plot([pos - 0.28, pos + 0.28], [vals.mean()] * 2, color="C3", lw=2.2)
    ax.axhline(y.mean(), color="gray", lw=0.8, ls="--")
    ax.set_xticks(range(5))
    ax.set_xticklabels(labels)
    ax.set_xlabel(name)
    ax.grid(alpha=0.3, axis="y")
axes[0].set_ylabel("burning rate")
axes[1].set_title("Observations (dots) and level means (bars); dashed: grand mean")
fig.tight_layout()
