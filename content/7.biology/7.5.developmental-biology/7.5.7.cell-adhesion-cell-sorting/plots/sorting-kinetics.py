"""Kinetics of sorting: local exchange rules get stuck, fluctuations let sorting proceed.

Each site of a 40 x 40 square lattice holds one cell of type A or B, or the medium M. A disk of radius 15
is filled with a random 50:50 mixture. The adhesive energy is a sum over the eight nearest and
next-nearest neighbour pairs, with adhesion energies E_AA = 4, E_BB = 1, E_AB = 1.5 per contact and
E_AM = E_BM = 0 (so gamma_AB = (E_AA + E_BB)/2 - E_AB = 1 > 0, the cells sort, and E_AB > E_BB, so
B should engulf A completely). One sweep is one attempted swap per site: a random site and a random
one of its four nearest neighbours exchange their contents.
Rule 1 (local, deterministic): a swap is made only if it does not decrease the adhesive energy.
Rule 2 (with fluctuations): a swap that changes the adhesive energy by dE is accepted with probability
min(1, exp(dE / T)), T = 0.7 (Metropolis; dE > 0 is a gain in adhesion).
Rule 3 (long-range exchange): as rule 2, but half of the attempts exchange an A cell and a B cell chosen
at random anywhere in the lattice (a stand-in for the long-range rearrangements allowed by pressure in
an incompressible tissue, in the spirit of Goel and Rogers).
A: start, rule 1 after 400 sweeps (no further change), rule 2 and rule 3 after 3000 sweeps;
B: fraction of the contacts of A cells that are with B cells.
"""

import math

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
L, R0 = 40, 15.0
E = [[0.0, 0.0, 0.0], [0.0, 4.0, 1.5], [0.0, 1.5, 1.0]]  # 0 medium, 1 A, 2 B
NB8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
NB4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def initial(seed):
    rng = np.random.default_rng(seed)
    g = np.zeros((L, L), dtype=int)
    c = (L - 1) / 2
    for y in range(L):
        for x in range(L):
            if math.hypot(x - c, y - c) < R0:
                g[y, x] = 1 if rng.random() < 0.5 else 2
    return g


def site_energy(g, y, x, t, skip):
    """Adhesion of a cell of type t placed at (y, x) with its neighbours (excluding site skip)."""
    s = 0.0
    for dy, dx in NB8:
        yy, xx = y + dy, x + dx
        if 0 <= yy < L and 0 <= xx < L and (yy, xx) != skip:
            s += E[t][g[yy][xx]]
    return s


def hetero(g):
    a = np.asarray(g)
    het = tot = 0
    for dy, dx in NB8:
        s1 = a[max(dy, 0):L + min(dy, 0), max(dx, 0):L + min(dx, 0)]
        s2 = a[max(-dy, 0):L + min(-dy, 0), max(-dx, 0):L + min(-dx, 0)]
        m = s1 == 1
        tot += (m & (s2 > 0)).sum()
        het += (m & (s2 == 2)).sum()
    return het / max(tot, 1)


def run(rule, sweeps, seed):
    rng = np.random.default_rng(seed)
    g = initial(1).tolist()
    curve = [(0, hetero(g))]
    marks = {1, 3, 10, 30, 100, 300, 1000, 3000}
    N = L * L
    for sw in range(1, sweeps + 1):
        ys = rng.integers(0, L, N).tolist()
        xs = rng.integers(0, L, N).tolist()
        ks = rng.integers(0, 4, N).tolist()
        us = rng.random(N).tolist()
        far = (rng.random(N) < (0.5 if rule == 3 else 0.0)).tolist()
        y2s = rng.integers(0, L, N).tolist()
        x2s = rng.integers(0, L, N).tolist()
        for y, x, k, u, f, yf, xf in zip(ys, xs, ks, us, far, y2s, x2s):
            if f:
                y2, x2 = yf, xf
                if g[y][x] == 0 or g[y2][x2] == 0:
                    continue
            else:
                dy, dx = NB4[k]
                y2, x2 = y + dy, x + dx
                if not (0 <= y2 < L and 0 <= x2 < L):
                    continue
            t1, t2 = g[y][x], g[y2][x2]
            if t1 == t2:
                continue
            before = site_energy(g, y, x, t1, (y2, x2)) + site_energy(g, y2, x2, t2, (y, x))
            after = site_energy(g, y, x, t2, (y2, x2)) + site_energy(g, y2, x2, t1, (y, x))
            dE = after - before
            if dE >= 0 or (rule > 1 and u < math.exp(dE / 0.7)):
                g[y][x], g[y2][x2] = t2, t1
        if sw in marks:
            curve.append((sw, hetero(g)))
    return np.array(g), np.array(curve)


g1, c1 = run(1, 400, 2)
g2, c2 = run(2, 3000, 2)
g3, c3 = run(3, 3000, 2)
g0 = initial(1)

fig, ax = bio.canvas(33.0, 9.4)
colA, colB = P.fill("mesoderm"), P.fill("ectoderm")


def draw(g, x0, y0, size):
    from matplotlib.colors import to_rgba
    img = np.zeros((L, L, 4))
    img[g == 1] = to_rgba(colA)
    img[g == 2] = to_rgba(colB)
    ax.imshow(img, extent=(x0, x0 + size, y0, y0 + size), origin="lower", interpolation="nearest", zorder=2)


bio.panel(ax, "A", (0.1, 9.3))
for k, (gg, text) in enumerate(((g0, "start"), (g1, "Rule 1: local, no losses"), (g2, "Rule 2: local + fluctuations"),
                               (g3, "Rule 3: + long-range exchange"))):
    x0 = 0.3 + 5.4 * k
    draw(gg, x0, 1.6, 5.2)
    bio.label(ax, (x0 + 2.6, 1.0), text, size="tiny")
for k, (tok, name) in enumerate((("mesoderm", "A (E_AA = 4)"), ("ectoderm", "B (E_BB = 1)"))):
    yy = 8.6 - 0.6 * k
    bio.box(ax, (1.0, yy), 0.4, 0.4, tok)
    bio.label(ax, (1.4, yy), name, size="tiny", ha="left")

bio.panel(ax, "B", (22.6, 9.3))
pc = charts.axes_at(ax, (24.4, 1.8, 8.2, 6.6))
for cc, tok, name in ((c1, "negative", "Rule 1"), (c2, "highlight", "Rule 2"), (c3, "positive", "Rule 3")):
    pc.plot(np.maximum(cc[:, 0], 0.5), cc[:, 1], color=quant.line_color(tok), lw=2.0, marker="o", ms=3.5, label=name)
pc.set_xscale("log")
pc.set_xlim(0.4, 4000)
pc.set_ylim(0, 0.55)
charts.style_axes(pc, "sweeps", "fraction of A contacts with B")
leg = pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper right")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pc, "Local rules stall; long-range moves finish")
