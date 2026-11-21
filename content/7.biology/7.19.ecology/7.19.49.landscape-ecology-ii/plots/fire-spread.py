"""Fire spread on a landscape as a cellular automaton, and the percolation of fuel.

A 150 x 150 grid; each cell carries fuel (forest) with probability p (the fuel density), otherwise it is
non-flammable. The whole left column is ignited. At each step every burning cell ignites each of its four
neighbors that carries unburned fuel with probability q (q = 1: fire always spreads to adjacent fuel; q < 1:
weather or fuel moisture make spread uncertain), and then burns out. Since each edge is tried only once, the
burned area is computed exactly as the cluster of the ignition line in site-bond percolation (sparse graph,
breadth-first distances), and the duration as the largest distance from the line within it.
A, B: final burned area for p = 0.55 and p = 0.65 with q = 1 (black: burned; green: unburned fuel). Below the
percolation threshold the fire dies out near the ignition line; above it, it sweeps across the map.
C: proportion of the fuel that burns against p, for q = 1, 0.9 and 0.8 (mean of 20 grids per value); with
q = 1 the transition is at the site-percolation threshold p_c = 0.593, and lower spread probability moves it
to higher fuel densities (site-bond percolation).
D: number of time steps until the fire stops (q = 1), which peaks at the threshold, where the burned cluster
is tortuous and the front advances slowly (critical slowing down of spread).
"""

import numpy as np
from matplotlib.colors import ListedColormap
import scipy.sparse as sparse
from scipy.sparse.csgraph import shortest_path

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(2)
n = 150


idx = np.arange(n * n).reshape(n, n)


def burn(p, q):
    """Burned set and duration. Each fuel-fuel edge transmits fire with probability q; because an edge is
    tried only once (from the cell that burns first), the burned set is the cluster of the ignition line in
    site-bond percolation and the duration is the largest graph distance from the line within it."""
    fuel = rng.random((n, n)) < p
    I, J = [], []
    for a, b in ((idx[:, :-1], idx[:, 1:]), (idx[:-1, :], idx[1:, :])):
        a, b = a.ravel(), b.ravel()
        ok = fuel.ravel()[a] & fuel.ravel()[b] & (rng.random(a.size) < q)
        I.append(a[ok])
        J.append(b[ok])
    src = idx[:, 0][fuel[:, 0]]
    I.append(np.full(src.size, n * n))
    J.append(src)
    I, J = np.concatenate(I), np.concatenate(J)
    G = sparse.csr_matrix((np.ones(I.size), (I, J)), shape=(n * n + 1, n * n + 1))
    d = shortest_path(G, directed=False, unweighted=True, indices=n * n)[:-1]
    burnt = np.isfinite(d)
    state = fuel.astype(np.int8)
    state[burnt.reshape(n, n)] = 2
    steps = d[burnt].max() if burnt.any() else 0
    return state, burnt.sum() / max(fuel.sum(), 1), steps


fig, ax = bio.canvas(32.0, 14.0)
cmap = ListedColormap([P.surface(), P.fill("plant"), P.ink()])
for j, p in enumerate((0.55, 0.65)):
    st, frac, _ = burn(p, 1.0)
    x0 = 1.2 + 10.6 * j
    pa = C.axes_at(ax, (x0, 1.6, 10.0, 10.0))
    pa.imshow(st, cmap=cmap, vmin=0, vmax=2, interpolation="nearest")
    pa.set_xticks([])
    pa.set_yticks([])
    for sp in pa.spines.values():
        sp.set_color(P.muted())
    bio.panel(ax, "AB"[j], (x0 - 0.9, 13.6))
    bio.label(ax, (x0, 13.2), f"p = {p:.2f}: {100 * frac:.0f} % of fuel burned", size="small", bold=True, ha="left")
bio.label(ax, (1.2, 12.3), "ignition along the left edge; black: burned, green: unburned fuel", size="tiny", ha="left")

ps = np.linspace(0.40, 0.90, 26)
res = {}
for q in (1.0, 0.9, 0.8):
    out = np.array([[burn(p, q)[1:] for _ in range(20)] for p in ps])
    res[q] = out.mean(axis=1)
pc = C.axes_at(ax, (24.0, 7.9, 7.6, 4.6))
for q, tok in ((1.0, "negative"), (0.9, "enzyme"), (0.8, "dna")):
    pc.plot(ps, res[q][:, 0], "o-", color=Q.line_color(tok), ms=3, lw=1.4, label=f"q = {q}")
pc.axvline(0.5927, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(0.505, 0.55, "p_c = 0.593", fontsize=FS["tiny"], color=P.muted())
pc.set_xlim(0.4, 0.9)
pc.set_ylim(-0.02, 1.02)
C.style_axes(pc, "fuel density p", "proportion of fuel burned")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (22.4, 13.6))
bio.label(ax, (24.0, 13.2), "A threshold in fuel continuity", size="small", bold=True, ha="left")

pd_ = C.axes_at(ax, (24.0, 1.4, 7.6, 4.0))
pd_.plot(ps, res[1.0][:, 1], "o-", color=Q.line_color("negative"), ms=3, lw=1.4)
pd_.axvline(0.5927, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pd_.set_xlim(0.4, 0.9)
C.style_axes(pd_, "fuel density p", "duration (steps)")
bio.panel(ax, "D", (22.4, 6.6))
bio.label(ax, (24.0, 6.2), "Slowest spread at the threshold (q = 1)", size="small", bold=True, ha="left")
