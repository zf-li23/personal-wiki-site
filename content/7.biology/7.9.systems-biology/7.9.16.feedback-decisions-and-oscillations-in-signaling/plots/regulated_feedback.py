"""Memory in the regulated-feedback motif (logic input functions, all production and removal rates 1,
all thresholds 0.5; time in units of the removal time).

The input factor X is produced from t = 0 to t = 3 and then decays.
A: double-positive loop (lock-on). Y1 and Y2 activate each other, X activates both; each promoter is an
OR gate (Y1 is made if X > 0.5 or Y2 > 0.5, and vice versa). Starting from Y1 = Y2 = 0, the transient X
switches both on, and they stay on after X has gone.
B: double-negative loop (toggle). Y1 and Y2 repress each other; X activates Y1 and represses Y2
(Y1 is made if X > 0.5 or Y2 < 0.5; Y2 is made if X < 0.5 and Y1 < 0.5). Starting from Y1 = 0, Y2 = 1,
the transient X flips the toggle, and the new state persists.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
K, dt = 0.5, 1e-3
t = np.arange(0, 12, dt)


def run(mode):
    X, Y1, Y2 = np.zeros_like(t), np.zeros_like(t), np.zeros_like(t)
    if mode == "toggle":
        Y2[0] = 1.0
    for i in range(1, len(t)):
        x, a, b = X[i - 1], Y1[i - 1], Y2[i - 1]
        px = 1.0 if t[i - 1] < 3 else 0.0
        if mode == "lock":
            pa = float(x > K or b > K)
            pb = float(x > K or a > K)
        else:
            pa = float(x > K or b < K)
            pb = float(x < K and a < K)
        X[i] = x + dt * (px - x)
        Y1[i] = a + dt * (pa - a)
        Y2[i] = b + dt * (pb - b)
    return X, Y1, Y2


fig, axes = plt.subplots(1, 2, figsize=(10, 3.4))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.25)
for ax, mode, title in [(axes[0], "lock", "A  Double-positive loop: lock-on"),
                        (axes[1], "toggle", "B  Double-negative loop: toggle")]:
    X, Y1, Y2 = run(mode)
    ax.axvspan(0, 3, color=P.muted(), alpha=0.15, lw=0)
    ax.plot(t, X, color=P.ink(), lw=1.4, label="X (input)")
    ax.plot(t, Y1, color=charts.line("protein"), lw=1.8, label="Y1")
    ax.plot(t, Y2, color=charts.line("receptor"), lw=1.8, ls="--", label="Y2")
    ax.axhline(K, color=P.muted(), lw=0.7, ls=":")
    ax.set_ylim(0, 1.35)
    ax.legend(fontsize=7, frameon=False, loc="upper right", ncol=3)
    charts.style_axes(ax, "time (1/alpha)", "level")
    charts.title(ax, title)
