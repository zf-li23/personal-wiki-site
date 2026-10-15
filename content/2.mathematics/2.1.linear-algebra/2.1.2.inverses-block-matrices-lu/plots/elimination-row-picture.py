"""Row picture of each step of Gauss-Jordan elimination for Example 2.1.1: every elementary
row operation changes the lines but keeps their intersection point (5, 3)."""

import numpy as np
import matplotlib.pyplot as plt

# Each stage: rows [a, b, c] of the augmented matrix, meaning a x1 + b x2 = c
stages = [
    ("Original system", [[1, 1, 8], [2, 4, 22]]),
    ("After $E_{21;-2}$", [[1, 1, 8], [0, 2, 6]]),
    ("After $E_{22;1/2}$", [[1, 1, 8], [0, 1, 3]]),
    ("After $E_{12;-1}$", [[1, 0, 5], [0, 1, 3]]),
]


def equation(a, b, c):
    def term(coef, name, first):
        if coef == 0:
            return ""
        sign = "" if first else (" + " if coef > 0 else " - ")
        if first and coef < 0:
            sign = "-"
        mag = abs(coef)
        return f"{sign}{'' if mag == 1 else f'{mag:g}'}{name}"
    left = term(a, "x_1", True) + term(b, "x_2", a == 0)
    return f"${left} = {c:g}$"


s = np.linspace(-1, 10, 200)
fig, axes = plt.subplots(1, 4, figsize=(13, 3.8))
for ax, (title, rows) in zip(axes, stages):
    for k, (a, b, c) in enumerate(rows):
        color = "C0" if k == 0 else "C2"
        if b != 0:
            ax.plot(s, (c - a * s) / b, color=color, lw=1.8, label=equation(a, b, c))
        else:
            ax.axvline(c / a, color=color, lw=1.8, label=equation(a, b, c))
    ax.plot(5, 3, "o", color="C3", ms=6, zorder=5)
    ax.axhline(0, color="0.6", lw=0.6)
    ax.axvline(0, color="0.6", lw=0.6)
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 9)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_title(title, fontsize=11)
    ax.legend(loc="upper right", fontsize=8.5)
axes[0].set_ylabel("$x_2$")
fig.tight_layout()
