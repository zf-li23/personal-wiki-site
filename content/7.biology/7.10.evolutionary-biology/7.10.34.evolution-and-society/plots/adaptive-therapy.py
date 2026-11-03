"""Adaptive therapy of cancer (Section 34.6.4), in a minimal competition model. A tumor contains drug-
sensitive cells S and resistant cells R that compete for space: dS/dt = 0.3 S (1 - (S + R)/K) - d S,
dR/dt = 0.1 R (1 - (S + R)/K), with K = 1 and the resistant cells growing more slowly (a cost of
resistance); the drug kills sensitive cells at rate d = 0.5 per day while it is given. Initially
S = 0.75 and R = 0.0001.
Continuous maximal treatment (A) eliminates the sensitive cells, releasing the resistant clone from
competition, and the tumor regrows as a resistant tumor. Adaptive treatment (B) starts the drug when the
tumor burden exceeds 0.8 and stops it when the burden falls below 0.6; the sensitive cells
that survive keep suppressing the resistant clone and control lasts much longer."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
dt, T = 0.02, 600
t = np.arange(0, T, dt)


def run(adaptive):
    S, R, on = 0.75, 1e-4, True
    out = np.zeros((t.size, 3))
    for k in range(t.size):
        tot = S + R
        if adaptive:
            if tot > 0.8:
                on = True
            elif tot < 0.6:
                on = False
        d = 0.5 if on else 0.0
        S += (0.3 * S * (1 - tot) - d * S) * dt
        R += 0.1 * R * (1 - tot) * dt
        out[k] = S, R, on
    return out


fig, axes = plt.subplots(1, 2, figsize=(9.8, 3.4), sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.08)
for ax, adaptive, title in ((axes[0], False, "A  Continuous maximal dose"), (axes[1], True, "B  Adaptive therapy")):
    X = run(adaptive)
    ax.fill_between(t, 0, 1.05, where=X[:, 2] > 0.5, color=P.fill("drug"), alpha=0.35, lw=0, label="drug given")
    ax.plot(t, X[:, 0] + X[:, 1], color=P.ink(), lw=2, label="total tumor")
    ax.plot(t, X[:, 0], color=charts.line("dna"), lw=1.4, label="sensitive")
    ax.plot(t, X[:, 1], color=charts.line("negative"), lw=1.4, label="resistant")
    ax.set_ylim(0, 1.05)
    charts.style_axes(ax, "time (days)", "tumor burden (fraction of K)" if ax is axes[0] else None)
    charts.title(ax, title)
axes[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
