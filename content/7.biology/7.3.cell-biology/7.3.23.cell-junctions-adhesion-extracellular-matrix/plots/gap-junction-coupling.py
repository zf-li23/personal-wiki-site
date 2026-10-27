"""Electrical and chemical coupling through gap junctions: a chain of identical cells.

A: current injected into cell 0 spreads through the junctional conductance g_j between neighbours and leaks
through the membrane conductance g_m of each cell (shading: steady-state voltage for g_j / g_m = 10).
B: steady state. Kirchhoff's law at cell n, g_j (V_{n-1} - 2 V_n + V_{n+1}) = g_m V_n, gives V_n = V_0 r^n with
r + 1/r = 2 + g_m / g_j, that is a coupling length lambda = -1 / ln r (in cells), close to sqrt(g_j / g_m) when
g_j >> g_m (the discrete cable equation). Curves for g_j / g_m = 1, 10 and 100.
C: a small dye injected as a pulse into cell 0 of a chain of 40 cells spreads by
dc_n/dt = k (c_{n-1} - 2 c_n + c_{n+1}), where k = P a / v is the junctional permeability P times the junction
area a over the cell volume v; k = 0.05 per s here. The concentration in cells 1, 3 and 6 rises later and
lower with distance: transfer through junctions behaves like diffusion with D_eff = k l^2 (l, cell length).
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import charts, quant
from wikibio import junctions as J

P = bio.P
fig, ax = bio.canvas(28.0, 9.4)

# A: chain of cells
bio.panel(ax, "A", (0.1, 9.3))
g = 1 / 10
r = 1 + g / 2 - np.sqrt(g + g * g / 4)
n = 7
w, gap = 1.25, 0.18
for k in range(n):
    x0 = 0.6 + k * (w + gap)
    v = r**k
    col = P.mix(P.fill("cytoplasm"), P.fill("ca"), 0.15 + 0.85 * v)
    ax.add_patch(FancyBboxPatch((x0, 5.0), w, 2.4, boxstyle="round,pad=0,rounding_size=0.25", facecolor=col,
                                edgecolor=P.edge("membrane"), lw=1.6, zorder=3))
    bio.label(ax, (x0 + w / 2, 4.6), str(k), size="tiny")
    if k < n - 1:
        gx = x0 + w + gap / 2
        for dy in (-0.3, 0.0, 0.3):
            ax.plot([gx - 0.12, gx + 0.12], [6.2 + dy, 6.2 + dy], color=P.edge(J.tok("connexin")), lw=2.4, solid_capstyle="butt", zorder=4)
ax.plot([0.9, 1.25], [8.6, 6.6], color=P.ink(), lw=1.2, zorder=5)
bio.label(ax, (0.95, 8.85), "current injection", size="tiny", ha="left")
bio.callout(ax, (0.6 + w + gap / 2, 6.5), (2.6, 8.2), r"gap junctions ($g_\mathrm{j}$)", size="tiny")
bio.label(ax, (5.5, 4.0), "cell index n", size="tiny", color=P.muted())

# circuit sketch
yc = 2.4
for k in range(4):
    x = 1.0 + 2.3 * k
    ax.plot([x, x], [yc, yc - 0.5], color=P.ink(), lw=1.0)
    ax.add_patch(FancyBboxPatch((x - 0.12, yc - 1.2), 0.24, 0.6, boxstyle="square,pad=0", facecolor=P.surface(), edgecolor=P.ink(), lw=1.0))
    ax.plot([x, x], [yc - 1.2, yc - 1.5], color=P.ink(), lw=1.0)
    bio.label(ax, (x + 0.2, yc - 0.9), r"$g_\mathrm{m}$", size="tiny", ha="left")
    bio.label(ax, (x, yc + 0.25), f"$V_{k}$", size="tiny")
    if k < 3:
        ax.plot([x, x + 0.8], [yc, yc], color=P.ink(), lw=1.0)
        ax.add_patch(FancyBboxPatch((x + 0.8, yc - 0.12), 0.7, 0.24, boxstyle="square,pad=0", facecolor=P.surface(), edgecolor=P.ink(), lw=1.0))
        ax.plot([x + 1.5, x + 2.3], [yc, yc], color=P.ink(), lw=1.0)
        bio.label(ax, (x + 1.15, yc + 0.35), r"$g_\mathrm{j}$", size="tiny")
ax.plot([0.8, 8.1], [yc - 1.5, yc - 1.5], color=P.ink(), lw=1.0)
bio.label(ax, (8.3, yc - 1.5), "ground", size="tiny", ha="left", color=P.muted())

# B: steady state
bio.panel(ax, "B", (10.4, 9.3))
pb = charts.axes_at(ax, (11.8, 1.4, 6.6, 6.9))
nn = np.arange(0, 21)
for ratio, tk in ((1, "neutral"), (10, "ca"), (100, "drug")):
    gg = 1 / ratio
    rr = 1 + gg / 2 - np.sqrt(gg + gg * gg / 4)
    lam = -1 / np.log(rr)
    pb.plot(nn, rr**nn, color=quant.line_color(tk), lw=2.0, marker="o", ms=3, label=rf"$g_\mathrm{{j}}/g_\mathrm{{m}}$ = {ratio}  ($\lambda$ = {lam:.1f} cells)")
pb.set_xlim(0, 20)
pb.set_ylim(0, 1.03)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "cell $n$", "$V_n / V_0$")
charts.title(pb, "Electrical coupling decays with distance")

# C: dye spreading
bio.panel(ax, "C", (19.6, 9.3))
pc = charts.axes_at(ax, (21.0, 1.4, 6.6, 6.9))
N, kk = 40, 0.05
dt, T = 0.5, 600.0
c = np.zeros(N)
c[0] = 1.0
ts, rec = [], []
for i in range(int(T / dt) + 1):
    ts.append(i * dt)
    rec.append(c.copy())
    lap = np.zeros(N)
    lap[1:-1] = c[:-2] - 2 * c[1:-1] + c[2:]
    lap[0] = c[1] - c[0]
    lap[-1] = c[-2] - c[-1]
    c = c + dt * kk * lap
rec = np.array(rec)
for cell, tk in ((1, "ca"), (3, "drug"), (6, "protein")):
    pc.plot(ts, rec[:, cell], color=quant.line_color(tk), lw=2.0, label=f"cell {cell}")
pc.plot(ts, rec[:, 0], color=quant.line_color("neutral"), lw=1.4, ls=(0, (4, 2)), label="cell 0 (injected)")
pc.set_xlim(0, T)
pc.set_ylim(0, 0.4)
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pc, "time / s", "dye concentration (fraction injected)")
charts.title(pc, "Dye coupling: diffusion cell to cell")
