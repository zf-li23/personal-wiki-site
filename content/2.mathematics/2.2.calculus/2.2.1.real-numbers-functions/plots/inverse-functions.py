"""A function and its inverse are mirror images in the line y = x."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(11, 3.9))

pairs = [
    ("$y=\\mathrm{e}^x$ and $y=\\ln x$", np.linspace(-3, 1.4, 300), np.exp, (-3, 4), "$\\mathrm{e}^x$", "$\\ln x$"),
    ("$y=\\sin x$ and $y=\\arcsin x$", np.linspace(-np.pi / 2, np.pi / 2, 300), np.sin, (-1.9, 1.9), "$\\sin x$", "$\\arcsin x$"),
    ("$y=\\tan x$ and $y=\\arctan x$", np.linspace(-1.35, 1.35, 300), np.tan, (-4, 4), "$\\tan x$", "$\\arctan x$"),
]

for ax, (title, x, f, lim, name_f, name_inv) in zip(axes, pairs):
    y = f(x)
    ax.plot(x, y, color="C0", lw=2, label=name_f)
    ax.plot(y, x, color="C1", lw=2, label=name_inv)
    ax.plot(lim, lim, color="0.6", lw=1, ls="--", label="$y=x$")
    # a point (a, b) on the graph and its mirror image (b, a)
    a = x[int(len(x) * 0.78)]
    b = f(a)
    ax.plot([a, b], [b, a], color="C2", lw=1, ls=":")
    ax.plot([a], [b], "o", color="C0", ms=5)
    ax.plot([b], [a], "o", color="C1", ms=5)
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
