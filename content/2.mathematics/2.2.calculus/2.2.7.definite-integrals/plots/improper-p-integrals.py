"""The functions 1/x^p: on [1, oo) the area is finite iff p > 1,
on (0, 1] it is finite iff p < 1. Right: the gamma function on (0, 5]."""

import numpy as np
import matplotlib.pyplot as plt
from math import gamma, factorial

fig, axes = plt.subplots(1, 3, figsize=(13, 3.9))
ps = [0.5, 1.0, 2.0]
colors = ["C0", "C1", "C2"]

ax = axes[0]
x = np.linspace(1, 12, 400)
for p, c in zip(ps, colors):
    tail = "converges" if p > 1 else "diverges"
    ax.plot(x, x**-p, color=c, linewidth=1.6, label=rf"$p = {p:g}$: {tail}")
ax.fill_between(x, x**-2.0, color="C2", alpha=0.2)
ax.set_title(r"$\int_1^{+\infty} x^{-p}\,\mathrm{d}x$ converges iff $p > 1$", fontsize=10)
ax.set_ylim(0, 1.1)

ax = axes[1]
x = np.linspace(0.01, 1, 400)
for p, c in zip(ps, colors):
    near = "converges" if p < 1 else "diverges"
    ax.plot(x, x**-p, color=c, linewidth=1.6, label=rf"$p = {p:g}$: {near}")
ax.fill_between(x, x**-0.5, color="C0", alpha=0.2)
ax.set_title(r"$\int_0^1 x^{-p}\,\mathrm{d}x$ converges iff $p < 1$", fontsize=10)
ax.set_ylim(0, 8)

for ax in axes[:2]:
    ax.set_xlabel(r"$x$")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

ax = axes[2]
s = np.linspace(0.08, 5, 400)
ax.plot(s, [gamma(v) for v in s], color="C3", linewidth=1.6)
k = np.arange(1, 6)
ax.plot(k, [factorial(int(v) - 1) for v in k], "o", color="C3", markersize=5,
        label=r"$\Gamma(n) = (n-1)!$")
ax.plot([0.5], [gamma(0.5)], "s", color="C0", markersize=5, label=r"$\Gamma(1/2) = \sqrt{\pi}$")
ax.set_ylim(0, 26)
ax.set_xlabel(r"$s$")
ax.set_title(r"$\Gamma(s) = \int_0^{+\infty} x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$, $s > 0$", fontsize=10)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
