"""Lateral inhibition by Notch-Delta signaling: the model of Collier, Monk, Maini and Lewis (1996).

A: the feedback between two neighbouring cells: Delta in one cell activates Notch in the other, and
Notch activity represses Delta in its own cell, so a small difference between neighbours is amplified.
B: the model on a sheet of hexagonal cells (14 x 12, periodic boundaries). For cell i with Notch activity
N_i and Delta level D_i (dimensionless),
    dN_i/dt = f(<D>_i) - N_i,      dD_i/dt = v [ g(N_i) - D_i ],
    f(x) = x^2 / (a + x^2),        g(x) = 1 / (1 + b x^2),
where <D>_i is the mean Delta of the six neighbours, a = 0.01, b = 100, v = 1 (time in units of the
lifetime of Notch activity). Starting from the uniform steady state with 1 % random noise, the sheet resolves
into a salt-and-pepper pattern: isolated high-Delta cells (the future neural precursors or hair cells, dark)
surrounded by low-Delta cells. C: Delta levels of a few cells against time: all start equal, and the
differences grow exponentially before saturating.
"""

import numpy as np
from matplotlib.patches import RegularPolygon

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(2)
nx, ny = 14, 12
a, b, v = 0.01, 100.0, 1.0


def f(x):
    return x**2 / (a + x**2)


def g(x):
    return 1 / (1 + b * x**2)


# neighbours on an "odd-r" offset hexagonal lattice with periodic boundaries
idx = np.arange(nx * ny).reshape(ny, nx)
nbrs = []
for r in range(ny):
    for c in range(nx):
        if r % 2 == 0:
            d = [(0, -1), (0, 1), (-1, -1), (-1, 0), (1, -1), (1, 0)]
        else:
            d = [(0, -1), (0, 1), (-1, 0), (-1, 1), (1, 0), (1, 1)]
        nbrs.append([idx[(r + dr) % ny, (c + dc) % nx] for dr, dc in d])
nbrs = np.array(nbrs)

# uniform steady state: N = f(D), D = g(N)
Ds = 0.5
for _ in range(200):
    Ds = 0.5 * Ds + 0.5 * g(f(Ds))
Ns = f(Ds)
N = np.full(nx * ny, Ns) * (1 + 0.01 * rng.standard_normal(nx * ny))
D = np.full(nx * ny, Ds) * (1 + 0.01 * rng.standard_normal(nx * ny))
dt, T = 0.02, 120.0
ts, rec = [], []
for i in range(int(T / dt)):
    Dm = D[nbrs].mean(axis=1)
    N, D = N + dt * (f(Dm) - N), D + dt * v * (g(N) - D)
    if i % 10 == 0:
        ts.append(i * dt)
        rec.append(D.copy())
rec = np.array(rec)

fig, ax = bio.canvas(28.0, 10.2)

# A: two-cell circuit
bio.panel(ax, "A", (0.1, 10.1))
for k, (x, txt) in enumerate(((1.9, "cell 1"), (5.5, "cell 2"))):
    ax.add_patch(RegularPolygon((x, 6.6), 6, radius=1.6, orientation=0, facecolor=P.fill("cytoplasm"),
                                edgecolor=P.edge("membrane"), lw=1.6, zorder=3))
    bio.label(ax, (x, 4.7), txt, size="tiny", color=P.muted())
for (x, side) in ((1.9, 1), (5.5, -1)):
    bio.box(ax, (x + side * 0.6, 7.4), 1.1, 0.5, "receptor", text="Delta", size="tiny")
    bio.box(ax, (x + side * 0.6, 5.8), 1.1, 0.5, "channel", text="Notch", size="tiny")
    bio.arrow(ax, (x + side * 0.6, 6.1), (x + side * 0.6, 7.1), kind="inhibition", bg=P.fill("cytoplasm"))
bio.arrow(ax, (3.1, 7.3), (4.3, 5.95), kind="activation", bg=P.surface())
bio.arrow(ax, (4.3, 7.3), (3.1, 5.95), kind="activation", bg=P.surface())
bio.label(ax, (3.7, 9.0), "Delta activates Notch in the neighbour;\nNotch represses Delta in its own cell", size="tiny")
bio.label(ax, (3.7, 3.6), "double negative loop between neighbours\n= positive feedback on the difference", size="tiny",
          color=P.muted())

# B: hexagonal sheet
bio.panel(ax, "B", (8.6, 10.1))
hexr = 0.42
Dfin = rec[-1]
lo, hi = Dfin.min(), Dfin.max()
for r in range(ny):
    for c in range(nx):
        x = 9.4 + c * hexr * np.sqrt(3) + (hexr * np.sqrt(3) / 2 if r % 2 else 0)
        y = 0.9 + r * hexr * 1.5
        t = (Dfin[idx[r, c]] - lo) / (hi - lo + 1e-12)
        col = P.mix(P.light("receptor"), P.edge("receptor"), t)
        ax.add_patch(RegularPolygon((x, y), 6, radius=hexr * 0.98, orientation=0, facecolor=col,
                                    edgecolor=P.edge("membrane"), lw=0.6, zorder=3))
bio.label(ax, (14.3, 9.9), f"Delta level after t = {T:.0f} (dark: high)", size="tiny")

# C: time courses
bio.panel(ax, "C", (19.8, 10.1))
pc = charts.axes_at(ax, (21.2, 1.4, 6.4, 7.6))
pick = [int(np.argmax(Dfin)), int(np.argmin(Dfin))] + list(rng.choice(nx * ny, 4, replace=False))
for k, i in enumerate(pick):
    tk = "receptor" if Dfin[i] > 0.5 * (lo + hi) else "channel"
    pc.plot(ts, rec[:, i], color=quant.line_color(tk), lw=1.6)
pc.set_xlim(0, T)
pc.set_ylim(0, 1.05)
pc.text(4, 0.9, "high Delta: precursor", fontsize=bio.core.FONT["tiny"], color=quant.line_color("receptor"))
pc.text(4, 0.15, "low Delta: inhibited", fontsize=bio.core.FONT["tiny"], color=quant.line_color("channel"))
charts.style_axes(pc, "time (Notch lifetimes)", "Delta level D")
charts.title(pc, "Symmetry breaking from noise")
