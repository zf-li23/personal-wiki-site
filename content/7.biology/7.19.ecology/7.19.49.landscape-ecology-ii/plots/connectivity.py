"""Least-cost paths and circuit theory on a resistance surface.

Resistance surface: a 72 x 72 grid; the resistance of a cell is r = exp(1.6 z), z a standardized fractal
surface (spectral synthesis, H = 0.6), so that r spans about 1 (good habitat) to several hundred. A road
crosses the map from top to bottom (two columns, r = 500) except at crossing structures (r = 1). A
source patch on the left and a target patch on the right (5 x 5 cells, r = 1).
A: resistance (log scale), least-cost path (computed with Dijkstra's algorithm on the 8-neighbour grid
graph, the cost of a step being the mean resistance of the two cells times the step length) and the
least-cost corridor (cells whose cost through them exceeds the minimum by less than 10 %), with two
crossings.
B: current density from circuit theory: neighbouring cells (4-neighbour) are joined by resistors of
resistance equal to the mean of the two cell resistances; the source patch is held at potential 1 and the
target patch at 0, and Kirchhoff's equations L v = 0 are solved at the other nodes (sparse Laplacian).
Current density at a cell is half the sum of the absolute currents through its edges. Current spreads over
several routes and concentrates at pinch points such as the crossings.
C: effect of adding crossings (1-6, placed at fixed rows, the first being on the best route): the least-cost
distance does not change, because it measures only the single best route, while the effective resistance
between the patches keeps falling, because circuit theory counts parallel routes.
"""

import numpy as np
from matplotlib.patches import Rectangle
import scipy.sparse as sp
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.linalg import spsolve

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(5)
n = 72


def fractal(H=0.6):
    fx = np.fft.fftfreq(n)[:, None]
    fy = np.fft.fftfreq(n)[None, :]
    f = np.sqrt(fx ** 2 + fy ** 2)
    f[0, 0] = 1.0
    amp = f ** (-(H + 1.0))
    amp[0, 0] = 0.0
    z = np.real(np.fft.ifft2(np.fft.fft2(rng.standard_normal((n, n))) * amp))
    return (z - z.mean()) / z.std()


base = np.exp(1.6 * fractal())
road_cols = [43, 44]
all_cross = [12, 58, 33, 22, 48, 5]
src = [(r, c) for r in range(34, 39) for c in range(3, 8)]
tgt = [(r, c) for r in range(34, 39) for c in range(n - 8, n - 3)]


def surface(crossings):
    r = base.copy()
    for c in road_cols:
        r[:, c] = 500.0
        for k in crossings:
            r[k - 1:k + 2, c] = 1.0
    for rc in src + tgt:
        r[rc] = 1.0
    return r


idx = np.arange(n * n).reshape(n, n)


def edges(r, diag):
    steps = [(0, 1, 1.0), (1, 0, 1.0)] + ([(1, 1, np.sqrt(2)), (1, -1, np.sqrt(2))] if diag else [])
    I, J, W = [], [], []
    for di, dj, d in steps:
        i0, i1 = max(0, -di), n - max(0, di)
        j0, j1 = max(0, -dj), n - max(0, dj)
        a = idx[i0:i1, j0:j1].ravel()
        b = idx[i0 + di:i1 + di, j0 + dj:j1 + dj].ravel()
        w = 0.5 * (r.ravel()[a] + r.ravel()[b]) * d
        I += [a, b]
        J += [b, a]
        W += [w, w]
    return np.concatenate(I), np.concatenate(J), np.concatenate(W)


def least_cost(r):
    I, J, W = edges(r, True)
    G = sp.csr_matrix((W, (I, J)), shape=(n * n, n * n))
    s = [idx[x] for x in src]
    t = [idx[x] for x in tgt]
    ds, pred, _ = dijkstra(G, indices=s, min_only=True, return_predecessors=True)
    dt_ = dijkstra(G, indices=t, min_only=True)
    end = t[int(np.argmin(ds[t]))]
    path = [end]
    while pred[path[-1]] >= 0:
        path.append(pred[path[-1]])
    tot = ds + dt_
    return ds[t].min(), np.array(path), (tot <= 1.10 * tot.min()).reshape(n, n)


def circuit(r):
    I, J, W = edges(r, False)
    g = 1.0 / W
    G = sp.csr_matrix((g, (I, J)), shape=(n * n, n * n))
    Lp = sp.diags(np.asarray(G.sum(1)).ravel()) - G
    v = np.zeros(n * n)
    fixed = np.zeros(n * n, bool)
    s = np.array([idx[x] for x in src])
    t = np.array([idx[x] for x in tgt])
    v[s] = 1.0
    fixed[s] = fixed[t] = True
    free = ~fixed
    Lp = Lp.tocsr()
    v[free] = spsolve(Lp[free][:, free].tocsc(), -Lp[free][:, fixed] @ v[fixed])
    cur = g * np.abs(v[I] - v[J])
    dens = np.zeros(n * n)
    np.add.at(dens, I, 0.5 * cur)
    total = (Lp[s] @ v).sum()
    return dens.reshape(n, n), 1.0 / total


fig, ax = bio.canvas(32.0, 11.0)
r2 = surface(all_cross[:2])
cost, path, corr = least_cost(r2)
dens, reff = circuit(r2)
ext = [0, n, n, 0]

pa = C.axes_at(ax, (1.2, 1.4, 8.0, 8.0))
pa.imshow(np.log10(r2), cmap="Greys", interpolation="nearest", extent=ext)
pa.contour(np.arange(n) + 0.5, np.arange(n) + 0.5, corr.astype(float), levels=[0.5], colors=[Q.line_color("highlight")], linewidths=1.0)
py, px = np.unravel_index(path, (n, n))
pa.plot(px + 0.5, py + 0.5, color=Q.line_color("negative"), lw=1.8)
for rc_set, tok in ((src, "plant"), (tgt, "plant")):
    rr = np.array(rc_set)
    pa.add_patch(Rectangle((rr[:, 1].min(), rr[:, 0].min()), 5, 5, fill=False, ec=Q.line_color(tok), lw=1.6))
pa.set_xticks([])
pa.set_yticks([])
bio.panel(ax, "A", (0.3, 10.6))
bio.label(ax, (1.2, 10.2), "Least-cost path and corridor", size="small", bold=True, ha="left")
bio.label(ax, (1.2, 9.7), "grey: resistance (log); red: path; yellow: corridor (+10 %)", size="tiny", ha="left")

pb = C.axes_at(ax, (11.6, 1.4, 8.0, 8.0))
pb.imshow(np.log10(dens + 1e-6), cmap="magma", interpolation="nearest", extent=ext, vmin=np.log10(dens.max()) - 3.5)
pb.set_xticks([])
pb.set_yticks([])
bio.panel(ax, "B", (10.7, 10.6))
bio.label(ax, (11.6, 10.2), "Current density (circuit theory)", size="small", bold=True, ha="left")
bio.label(ax, (11.6, 9.7), "bright: much current; road crossings are pinch points", size="tiny", ha="left")

ks = np.arange(1, 7)
lcd, rf = [], []
for k in ks:
    rk = surface(all_cross[:k])
    lcd.append(least_cost(rk)[0])
    rf.append(circuit(rk)[1])
lcd = np.array(lcd) / lcd[0]
rf = np.array(rf) / rf[0]
pc = C.axes_at(ax, (23.6, 1.8, 7.6, 7.2))
pc.plot(ks, lcd, "o-", color=Q.line_color("negative"), lw=1.5, ms=4, label="least-cost distance")
pc.plot(ks, rf, "s-", color=Q.line_color("dna"), lw=1.5, ms=4, label="effective resistance")
pc.set_ylim(0, 1.1)
C.style_axes(pc, "number of road crossings", "relative to one crossing")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "C", (21.8, 10.6))
bio.label(ax, (23.6, 10.2), "Parallel routes count", size="small", bold=True, ha="left")
