"""Bisection for the zero of f(x) = x^3 + x - 1 on [0, 1]: nested intervals [a_n, b_n] shrinking to the zero."""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x ** 3 + x - 1
a, b = 0.0, 1.0
steps = []
for _ in range(7):
    steps.append((a, b))
    c = (a + b) / 2
    if f(c) < 0:
        a = c
    else:
        b = c

fig, axes = plt.subplots(1, 2, figsize=(11, 4), gridspec_kw={"width_ratios": [1.1, 1]})
ax = axes[0]
x = np.linspace(-0.1, 1.1, 300)
ax.plot(x, f(x), color="C0", lw=2, label="$f(x) = x^3 + x - 1$")
ax.axhline(0, color="0.7", lw=0.8)
ax.plot([0, 1], [f(0), f(1)], "o", color="C1", ms=6)
ax.annotate("$f(0) < 0$", (0, f(0)), xytext=(8, -4), textcoords="offset points", fontsize=10)
ax.annotate("$f(1) > 0$", (1, f(1)), xytext=(-60, 4), textcoords="offset points", fontsize=10)
root = 0.6823278038280193
ax.plot([root], [0], "o", color="C3", ms=6)
ax.annotate("$\\xi$", (root, 0), xytext=(-4, 8), textcoords="offset points", fontsize=11, color="C3")
ax.set_title("Opposite signs at the endpoints", fontsize=11)
ax.legend(loc="upper left", fontsize=9)

ax = axes[1]
for k, (a, b) in enumerate(steps):
    ax.plot([a, b], [k, k], color="C0", lw=4, solid_capstyle="butt")
    ax.plot([a, b], [k, k], "|", color="C0", ms=12)
    ax.text(1.03, k, f"$b_{k+1} - a_{k+1} = 2^{{-{k}}}$", va="center", fontsize=9)
ax.axvline(root, color="C3", lw=1, ls="--")
ax.set_xlim(-0.02, 1.35)
ax.set_ylim(len(steps) - 0.5, -0.5)
ax.set_yticks([])
ax.set_xlabel("$x$")
ax.set_title("Nested intervals $[a_n, b_n]$ from top to bottom", fontsize=11)
fig.tight_layout()
