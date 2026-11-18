"""Reserve selection: richness ranking, greedy complementarity and the integer-programming optimum.

A region of 12 x 12 planning units (sites). 200 species; each has a range centre placed uniformly and a
range radius (in site widths) drawn from a lognormal distribution (median 2.4, log-sd 0.5), and occurs in
each site within that radius with probability 0.85 (at least one site). a_ij = 1 if species i occurs in site j.
Methods for choosing k sites:
  richness: the k richest sites ("hotspots");
  greedy: repeatedly add the site that contains the most species not yet represented (complementarity);
  optimum: the maximal coverage problem, maximize sum_i y_i subject to y_i <= sum_j a_ij x_j, sum_j x_j = k,
  x_j, y_i binary, solved exactly by mixed-integer linear programming (scipy.optimize.milp).
A: species richness per site (shading) and the sites chosen by the greedy algorithm, numbered in order,
until every species is represented once (the minimum-set problem); the exact minimum found by integer
programming is given for comparison.
B: number of species represented against the number of sites selected, for the three methods.
"""

import numpy as np
from matplotlib.patches import Rectangle
from scipy.optimize import LinearConstraint, Bounds, milp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(12)
g, nsp = 12, 200
m = g * g
xx, yy = np.meshgrid(np.arange(g), np.arange(g))
cx, cy = xx.ravel() + 0.5, yy.ravel() + 0.5
A = np.zeros((nsp, m), int)
for i in range(nsp):
    c = rng.random(2) * g
    rad = 2.4 * np.exp(0.5 * rng.standard_normal())
    d = np.hypot(cx - c[0], cy - c[1])
    occ = (d <= rad) & (rng.random(m) < 0.85)
    if not occ.any():
        occ[np.argmin(d)] = True
    A[i] = occ


def greedy(kmax=None):
    covered = np.zeros(nsp, bool)
    order, curve = [], []
    while not covered.all() and (kmax is None or len(order) < kmax):
        gain = A[~covered].sum(0)
        gain[order] = -1
        j = int(np.argmax(gain))
        order.append(j)
        covered |= A[:, j].astype(bool)
        curve.append(covered.sum())
    return order, curve


def max_cover(k):
    c = np.concatenate([np.zeros(m), -np.ones(nsp)])
    cons = [LinearConstraint(np.concatenate([-A, np.eye(nsp)], 1), -np.inf, 0),
            LinearConstraint(np.concatenate([np.ones(m), np.zeros(nsp)])[None, :], k, k)]
    res = milp(c, constraints=cons, integrality=np.ones(m + nsp), bounds=Bounds(0, 1))
    return int(round(-res.fun))


def min_set():
    c = np.ones(m)
    res = milp(c, constraints=[LinearConstraint(A, 1, np.inf)], integrality=np.ones(m), bounds=Bounds(0, 1))
    return int(round(res.fun))


order, gcurve = greedy()
nmin = min_set()
rich = A.sum(0)
ks = np.arange(1, 13)
rcurve = [A[:, np.argsort(-rich)[:k]].any(1).sum() for k in ks]
_, g15 = greedy(12)
ocurve = [max_cover(k) for k in ks]

fig, ax = bio.canvas(30.0, 11.5)
pa = C.axes_at(ax, (1.4, 1.2, 8.4, 8.4))
pa.imshow(rich.reshape(g, g), cmap="Greens", origin="lower", extent=[0, g, 0, g], vmax=rich.max() * 1.6)
for n_, j in enumerate(order, 1):
    pa.add_patch(Rectangle((cx[j] - 0.5, cy[j] - 0.5), 1, 1, fill=False, ec=Q.line_color("negative"), lw=1.4))
    pa.text(cx[j], cy[j], str(n_), ha="center", va="center", fontsize=FS["tiny"], color=P.ink(), weight="bold")
pa.set_xticks([])
pa.set_yticks([])
bio.panel(ax, "A", (0.5, 11.2))
bio.label(ax, (1.4, 10.8), f"Greedy: all {nsp} species in {len(order)} sites", size="small", bold=True, ha="left")
bio.label(ax, (1.4, 10.1), f"exact minimum (integer programming): {nmin} sites; shading: richness", size="tiny", ha="left")

pb = C.axes_at(ax, (15.0, 1.6, 13.6, 7.8))
pb.plot(ks, ocurve, "o-", color=Q.line_color("dna"), lw=1.6, ms=4, label="optimum (integer programming)")
pb.plot(ks, g15, "s--", color=Q.line_color("negative"), lw=1.4, ms=4, label="greedy complementarity")
pb.plot(ks, rcurve, "^-", color=Q.line_color("plant"), lw=1.4, ms=4, label="richest sites (hotspots)")
pb.axhline(nsp, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0.5, 12.5)
pb.set_ylim(0, nsp * 1.05)
C.style_axes(pb, "number of sites selected k", "species represented at least once")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (13.2, 11.2))
bio.label(ax, (15.0, 10.8), "Complementarity beats richness", size="small", bold=True, ha="left")
