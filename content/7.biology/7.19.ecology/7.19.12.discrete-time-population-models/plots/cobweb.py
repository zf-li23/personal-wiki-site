"""Cobweb diagrams of the discrete logistic model (Section 12.2).

x_{t+1} = x_t [1 + r (1 - x_t)] (x = N/K) for r = 0.8 (monotonic approach), 1.6 (damped oscillation),
2.3 (stable 2-cycle), 2.5 (stable 4-cycle) and 2.8 (chaos), started at x0 = 0.1.
Top: the map (curve), the diagonal and the cobweb of the first iterates (transient faded).
Bottom: the time series.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rs = [(0.8, "monotonic"), (1.6, "damped oscillation"), (2.3, "2-cycle"), (2.5, "4-cycle"), (2.8, "chaos")]
fig, axes = plt.subplots(2, 5, figsize=(14.0, 5.6), gridspec_kw=dict(height_ratios=[1.5, 1]))
for k, (r, name) in enumerate(rs):
    top = (1 + r) ** 2 / (4 * r)
    xmax = (1 + r) / r
    f = lambda x: x * (1 + r * (1 - x))
    ax = axes[0, k]
    xs = np.linspace(0, xmax, 300)
    ax.plot(xs, f(xs), color=C.line("dna"), lw=1.8)
    ax.plot([0, xmax], [0, xmax], color=P.muted(), lw=0.8)
    x = 0.1
    traj = [x]
    n_total = 60 if r > 2 else 25
    for i in range(n_total):
        y = f(x)
        col = C.line("rna")
        alpha = 0.35 if (r > 2 and i < 30) else 1.0
        ax.plot([x, x], [x if i else 0, y], color=col, lw=0.8, alpha=alpha)
        ax.plot([x, y], [y, y], color=col, lw=0.8, alpha=alpha)
        x = y
        traj.append(x)
    ax.set_xlim(0, min(xmax, 1.6))
    ax.set_ylim(0, min(xmax, 1.6))
    ax.set_aspect("equal")
    C.style_axes(ax, "xₜ", "xₜ₊₁" if k == 0 else None)
    C.title(ax, f"r = {r:g}: {name}")
    ax2 = axes[1, k]
    ax2.plot(range(len(traj)), traj, "o-", ms=2.2, lw=0.9, color=C.line("rna"))
    ax2.axhline(1, color=P.muted(), lw=0.6, ls=(0, (3, 2)))
    ax2.set_ylim(0, 1.45)
    C.style_axes(ax2, "t", "xₜ" if k == 0 else None)
fig.tight_layout()
