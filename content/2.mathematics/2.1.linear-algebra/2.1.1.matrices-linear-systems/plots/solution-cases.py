"""The three possible solution sets of a system of two equations in two unknowns."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 4, 100)
cases = [
    ("Unique solution", [("$x_1 + x_2 = 2$", 1, 1, 2), ("$x_1 - x_2 = 0$", 1, -1, 0)], (1, 1)),
    ("No solution", [("$x_1 + x_2 = 2$", 1, 1, 2), ("$x_1 + x_2 = 3$", 1, 1, 3)], None),
    ("Infinitely many solutions", [("$x_1 + x_2 = 2$", 1, 1, 2), ("$2x_1 + 2x_2 = 4$", 2, 2, 4)], None),
]

fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.7))
for ax, (title, lines, point) in zip(axes, cases):
    for k, (label, p, q, c) in enumerate(lines):
        style = dict(color=f"C{2 * k}", lw=3.2 if k == 0 else 1.6, label=label)
        if k == 1 and title.startswith("Infinitely"):
            style.update(ls="--", color="C2")
        ax.plot(t, (c - p * t) / q, **style)
    if point is not None:
        ax.plot(*point, "o", color="C3", ms=7, zorder=5)
    ax.axhline(0, color="0.6", lw=0.6)
    ax.axvline(0, color="0.6", lw=0.6)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title(title, fontsize=11)
    ax.legend(loc="upper right", fontsize=8.5)
fig.tight_layout()
