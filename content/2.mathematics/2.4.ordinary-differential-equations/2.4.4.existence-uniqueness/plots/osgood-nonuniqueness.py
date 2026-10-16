"""Solutions of y' = |y|^(1/2) through the origin: the zero solution and branches leaving it."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 800)


def branch(c1, c2):
    y = np.zeros_like(x)
    y = np.where(x > c2, (x - c2) ** 2 / 4, y)
    y = np.where(x < c1, -((c1 - x) ** 2) / 4, y)
    return y


fig, ax = plt.subplots(figsize=(7, 4.8))
pairs = [(0.0, 0.0), (-1.0, 0.5), (-2.0, 1.0), (-0.5, 2.0), (-3.0, 3.0)]
for i, (c1, c2) in enumerate(pairs):
    ax.plot(x, branch(c1, c2), lw=1.7, color=f"C{i}", label=f"c1 = {c1:g}, c2 = {c2:g}")
ax.axhline(0, color="C3", lw=2.6, alpha=0.5, label="y = 0")
ax.plot([0], [0], "o", color="k", ms=6)
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y' = |y|^(1/2), y(0) = 0: non-unique solutions")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
