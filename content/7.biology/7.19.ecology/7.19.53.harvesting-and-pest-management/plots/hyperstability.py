"""Catchability that rises as the stock falls (schooling fish, Proposition 53.1.6), dimensionless.

Catch per unit effort q(N) N with q(N) = q0 (K/N)^beta, so the harvest is e x^(1 - beta) and
dx/dtau = x(1 - x) - e x^(1 - beta), 0 <= beta < 1 (beta = 0: ordinary fixed effort).
Positive equilibria solve g(x) = (1 - x) x^beta = e; g has its maximum at x_m = beta/(1 + beta),
so for beta > 0 there is a fold (saddle-node) at e_c = g(x_m), and x = 0 is locally attracting.
A: per capita growth 1 - x against per capita harvest e x^(-beta) (beta = 0.6, e = 0.25);
B: equilibria against effort for beta = 0, 0.5, 0.8 (solid stable, dashed unstable);
C: catch per unit effort, relative to its value at K, against stock: hyperstability for beta > 0.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
cols = {0.0: C.line("dna"), 0.5: C.line("rna"), 0.8: C.line("negative")}

fig, axes = plt.subplots(1, 3, figsize=(12.8, 3.9))

ax = axes[0]
x = np.linspace(0.005, 1.05, 500)
b, e = 0.6, 0.25
ax.plot(x, 1 - x, color=C.line("plant"), lw=2.2, label="per capita growth 1 − x")
ax.plot(x, e * x ** (-b), color=cols[0.8], lw=2, label="per capita harvest e x^(−β)")
g = (1 - x) * x ** b
roots = x[np.where(np.diff(np.sign(g - e)))[0]]
ax.plot([roots[0]], [1 - roots[0]], "o", ms=7, mfc=P.surface(), mec=cols[0.8], mew=1.6, zorder=5)
ax.plot([roots[1]], [1 - roots[1]], "o", ms=7, color=cols[0.8], zorder=5)
ax.text(roots[0] + 0.03, 1 - roots[0] + 0.05, "threshold", fontsize=FS["tiny"], color=cols[0.8])
ax.set_xlim(0, 1.05)
ax.set_ylim(0, 1.3)
C.style_axes(ax, "stock x = N / K", "per capita rate (units of r)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "A  Harvest rate rises as the stock falls")

ax = axes[1]
for b, col in cols.items():
    if b == 0:
        ee = np.linspace(0, 1, 200)
        ax.plot(ee, 1 - ee, color=col, lw=2, label="β = 0")
        ax.plot(ee, 0 * ee, color=col, lw=1, ls=(0, (3, 2)))
        continue
    xm = b / (1 + b)
    xu = np.linspace(xm, 1, 300)
    xl = np.linspace(1e-4, xm, 300)
    ax.plot((1 - xu) * xu ** b, xu, color=col, lw=2, label=f"β = {b:g}")
    ax.plot((1 - xl) * xl ** b, xl, color=col, lw=1.4, ls=(0, (3, 2)))
    ax.plot([(1 - xm) * xm ** b], [xm], "o", color=col, ms=5)
ax.set_xlim(0, 1)
ax.set_ylim(-0.02, 1.02)
C.style_axes(ax, "effort e = q0 E / r", "equilibrium stock x*")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "B  A fold appears for β > 0")

ax = axes[2]
x = np.linspace(0, 1, 300)
for b, col in cols.items():
    ax.plot(x, x ** (1 - b), color=col, lw=2, label=f"β = {b:g}")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.05)
C.style_axes(ax, "stock x = N / K", "catch per unit effort (relative)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
C.title(ax, "C  Hyperstable catch rates hide decline")
fig.tight_layout()
