"""Contact probability and the folding of chromosomes.

A: two compact folds on a 16 x 16 square lattice, colored from one end
(dark) to the other (light): a two-dimensional Hilbert curve of 256 monomers, an idealized fractal (crumpled) globule
in which every stretch of chain occupies its own compact region, and a random walk of 1024 steps
confined to the same square, whose stretches interpenetrate. B: contact probability P(s) of
two monomers separated by s along the chain, from Monte Carlo of 300 random walks of 4096 steps on
the simple cubic lattice (contact = neighboring sites; odd separations only, because of the lattice parity): free walks follow s^(-3/2); walks
confined to a cube of side 12 lattice units (an equilibrium globule) follow s^(-3/2) until a stretch
fills the cube and then level off at a plateau set by the volume. The fractal-globule prediction
s^(-1) and the exponent measured by Hi-C in human interphase chromosomes over 0.5-7 Mb (about -1.08)
are shown for comparison."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(7)


def hilbert2d(order):
    n = 2 ** order
    pts = []
    for d in range(n * n):
        x = y = 0
        t = d
        s = 1
        while s < n:
            rx = 1 & (t // 2)
            ry = 1 & (t ^ rx)
            if ry == 0:
                if rx == 1:
                    x, y = s - 1 - x, s - 1 - y
                x, y = y, x
            x += s * rx
            y += s * ry
            t //= 4
            s *= 2
        pts.append((x, y))
    return np.array(pts, dtype=float)


def confined_walk_2d(n, side):
    steps = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    x = np.zeros((n, 2))
    x[0] = side / 2
    for i in range(1, n):
        while True:
            y = x[i - 1] + steps[rng.integers(4)]
            if 0 <= y[0] < side and 0 <= y[1] < side:
                x[i] = y
                break
    return x


def colored(ax, pts):
    seg = np.stack([pts[:-1], pts[1:]], axis=1)
    lc = LineCollection(seg, cmap="viridis", lw=1.0)
    lc.set_array(np.linspace(0, 1, len(seg)))
    ax.add_collection(lc)
    ax.set_xlim(-1, 16)
    ax.set_ylim(-1, 16)
    ax.set_aspect("equal")
    ax.axis("off")


def walks(M, N, box=None):
    steps = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    s = steps[rng.integers(6, size=(M, N))]
    if box is None:
        return np.concatenate([np.zeros((M, 1, 3), int), np.cumsum(s, axis=1)], axis=1)
    x = np.zeros((M, N + 1, 3), int)
    x[:, 0] = box // 2
    for i in range(N):
        y = x[:, i] + s[:, i]
        bad = (y < 0) | (y >= box)
        y = np.where(bad, x[:, i] - s[:, i], y)  # reflect at the walls
        x[:, i + 1] = y
    return x


def contact(x, svals):
    out = []
    for s in svals:
        d = np.abs(x[:, s:] - x[:, :-s]).sum(axis=2)
        out.append((d == 1).mean())
    return np.array(out)


fig = plt.figure(figsize=(10.4, 3.6))
a1 = fig.add_axes([0.01, 0.08, 0.2, 0.75])
a2 = fig.add_axes([0.23, 0.08, 0.2, 0.75])
ax = fig.add_axes([0.55, 0.16, 0.42, 0.72])
colored(a1, hilbert2d(4))
colored(a2, confined_walk_2d(1024, 16))
for a, t in ((a1, "Hilbert curve\n(fractal globule)"), (a2, "confined random walk\n(equilibrium globule)")):
    a.set_title(t, fontsize=bio.core.FONT["tiny"], color=P.ink())
a1.text(0.0, 1.17, "A  Two compact folds", transform=a1.transAxes, fontsize=bio.core.FONT["small"], color=P.ink(),
        weight="bold")

svals = np.unique(np.logspace(0.5, np.log10(3000), 22).astype(int) // 2 * 2 + 1)
free = contact(walks(300, 4096), svals)
conf = contact(walks(300, 4096, box=12), svals)
ax.plot(svals, free, "o", color=charts.line("dna"), ms=3.5, label="free random walk")
ax.plot(svals, conf, "s", color=charts.line("protein"), ms=3.5, label="confined random walk")
ss = np.logspace(0.5, 3.5, 50)
ax.plot(ss, free[3] * (ss / svals[3]) ** -1.5, color=charts.line("dna"), lw=0.9, label=r"$s^{-3/2}$ (ideal chain)")
ax.plot(ss, 0.5 * free[3] * (ss / svals[3]) ** -1.0, color=charts.line("rna"), lw=0.9, ls="--",
        label=r"$s^{-1}$ (fractal globule)")
ax.plot(ss[20:40], 0.25 * free[3] * (ss[20:40] / svals[3]) ** -1.08, color=P.ink(), lw=2.0, alpha=0.5,
        label=r"human Hi-C, slope $-1.08$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "separation along the chain s (monomers)", "contact probability P(s)")
charts.title(ax, "B  Scaling of contacts")
