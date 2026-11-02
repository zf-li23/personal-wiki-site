"""Temporal order from activation thresholds: LIFO in a single-input module, FIFO in a multi-output FFL.

The master regulator X is produced from t = 0 to t = 4 and removed at rate 1:
X = 1 - exp(-t), then X(4) exp(-(t - 4)). Gene Z_i is ON when its input exceeds its threshold.
A: single-input module, thresholds of X: K = 0.3, 0.5, 0.7 for Z1, Z2, Z3. Genes turn on in the order
1, 2, 3 and off in the order 3, 2, 1 (last in, first out).
B: multi-output C1-FFL with OR (SUM-like) gates: Z_i is ON if X > K_i or Y > K'_i, with the same K_i and the
opposite order of Y thresholds, K' = 0.7, 0.5, 0.3. Y is activated by X (above 0.2) and removed at rate
0.5, so it outlasts X; the genes turn on in the order 1, 2, 3 and off in the order 1, 2, 3 (first in,
first out). The ON intervals of the three genes are drawn as bars below the regulator curves.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
dt = 1e-3
t = np.arange(0, 12, dt)
X = np.where(t < 4, 1 - np.exp(-t), (1 - np.exp(-4)) * np.exp(-(t - 4)))
Y = np.zeros_like(t)
for i in range(1, len(t)):
    Y[i] = Y[i - 1] + dt * (float(X[i - 1] > 0.2) - 0.5 * Y[i - 1])
Y = Y / 2.0  # steady state of Y would be 2; plot in units of that steady state
K = [0.3, 0.5, 0.7]
Kp = [0.7, 0.5, 0.3]
cols = [charts.line("dna"), charts.line("positive"), charts.line("rna")]

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.88, wspace=0.25)
for ax, mode in zip(axes, ["SIM", "FFL"]):
    ax.plot(t, X, color=P.ink(), lw=1.5, label="X")
    if mode == "FFL":
        ax.plot(t, Y, color=charts.line("protein"), lw=1.5, label="Y")
    for k in range(3):
        on = X > K[k]
        if mode == "FFL":
            on = on | (Y > Kp[k])
        idx = np.where(on)[0]
        y0 = -0.25 - 0.2 * k
        ax.plot([t[idx[0]], t[idx[-1]]], [y0, y0], color=cols[k], lw=6, solid_capstyle="butt")
        ax.text(-0.15, y0, f"Z{k + 1}", fontsize=7, color=P.ink(), ha="right", va="center")
        ax.axhline(K[k], xmax=0.33, color=cols[k], lw=0.8, ls=":")
    ax.set_ylim(-0.8, 1.1)
    ax.set_xlim(-0.8, 12)
    ax.set_yticks([0, 0.5, 1])
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    charts.style_axes(ax, "time (1/alpha_X)", "regulator level")
axes[0].text(4.6, 0.62, "X thresholds (Z1, Z2, Z3):\n0.3, 0.5, 0.7", fontsize=7, color=P.ink())
axes[1].text(6.6, 0.62, "X thresholds: 0.3, 0.5, 0.7\nY thresholds: 0.7, 0.5, 0.3", fontsize=7, color=P.ink())
charts.title(axes[0], "A  Single-input module: last in, first out")
charts.title(axes[1], "B  Multi-output FFL (OR): first in, first out")
