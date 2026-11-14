"""Hamilton's (1971) selfish herd: domains of danger as Voronoi cells.

A predator appears at a random point of the arena and attacks the nearest prey, so each prey's risk is
proportional to the area of its Voronoi cell, its domain of danger. A: 40 prey scattered at random.
B: after 25 steps in which every prey moves a short distance towards the centre of its three nearest neighbours
(stopping when its nearest neighbour is closer than a minimum spacing), the prey have formed clumps; cells at the edge remain large, those in the middle small. Cells are
shaded by area. C: mean domain of danger of the prey that end up in the interior of the group and of those on its
edge (convex hull vertices), against time, averaged over 30 runs.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
L, N = 10.0, 40
gx, gy = np.meshgrid(np.linspace(0, L, 200), np.linspace(0, L, 200))
grid = np.c_[gx.ravel(), gy.ravel()]
CMAP = LinearSegmentedColormap.from_list("danger", [P.surface(), P.fill("rna")])


cg = np.c_[[a.ravel() for a in np.meshgrid(np.linspace(0, L, 70), np.linspace(0, L, 70))]].T


def domains(x, g=grid):
    d = ((g[:, None, :] - x[None, :, :]) ** 2).sum(-1)
    lab = d.argmin(1)
    area = np.bincount(lab, minlength=len(x)) * (L * L / len(g))
    return lab, area


def step(x, dist=0.15, gap=0.35):
    d = ((x[:, None, :] - x[None, :, :]) ** 2).sum(-1)
    np.fill_diagonal(d, np.inf)
    near = np.argsort(d, 1)[:, :3]
    v = x[near].mean(1) - x
    r = np.hypot(v[:, 0], v[:, 1])[:, None]
    move = (np.sqrt(d.min(1)) > gap)[:, None]
    return x + np.where(move, v / np.maximum(r, 1e-9) * np.minimum(dist, r), 0.0)


def hull_idx(x):
    pts = sorted(range(len(x)), key=lambda i: (x[i, 0], x[i, 1]))

    def cross(o, a, b):
        return (x[a, 0] - x[o, 0]) * (x[b, 1] - x[o, 1]) - (x[a, 1] - x[o, 1]) * (x[b, 0] - x[o, 0])
    lo, up = [], []
    for i in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], i) <= 0:
            lo.pop()
        lo.append(i)
    for i in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], i) <= 0:
            up.pop()
        up.append(i)
    return set(lo[:-1] + up[:-1])


fig, ax = bio.canvas(33.0, 10.5)
x0 = rng.uniform(1.0, 9.0, (N, 2))
x = x0.copy()
for _ in range(25):
    x = step(x)
for k, (pts, title) in enumerate(((x0, "random positions"), (x, "after 25 steps towards neighbors"))):
    p = Ch.axes_at(ax, (1.0 + 10.6 * k, 1.0, 8.6, 8.6))
    lab, area = domains(pts)
    shade = np.clip(area / 12.0, 0, 1)
    img = shade[lab].reshape(gx.shape)
    p.imshow(img, origin="lower", extent=(0, L, 0, L), cmap=CMAP, vmin=0, vmax=1)
    edges = (np.diff(lab.reshape(gx.shape), axis=0, prepend=lab[0]) != 0) | \
            (np.diff(lab.reshape(gx.shape), axis=1, prepend=lab.reshape(gx.shape)[:, :1]) != 0)
    p.contour(gx, gy, edges.astype(float), levels=[0.5], colors=[P.muted()], linewidths=0.4)
    p.plot(pts[:, 0], pts[:, 1], "o", ms=3.2, color=P.ink())
    p.set_xlim(0, L)
    p.set_ylim(0, L)
    p.set_xticks([])
    p.set_yticks([])
    for sp in p.spines.values():
        sp.set_color(P.muted())
    Ch.title(p, title)
    bio.panel(ax, "AB"[k], (0.2 + 10.6 * k, 10.4))

pc = Ch.axes_at(ax, (24.6, 1.6, 7.6, 7.4))
T, runs = 26, 30
inner, outer = np.zeros(T), np.zeros(T)
for r in range(runs):
    xs = [rng.uniform(1.0, 9.0, (N, 2))]
    for _ in range(T - 1):
        xs.append(step(xs[-1]))
    h = hull_idx(xs[-1])
    edge = np.array([i in h for i in range(N)])
    for t in range(T):
        _, a = domains(xs[t], cg)
        inner[t] += a[~edge].mean() / runs
        outer[t] += a[edge].mean() / runs
pc.plot(range(T), outer, color=Ch.line("rna"), lw=1.7)
pc.plot(range(T), inner, color=Ch.line("dna"), lw=1.7)
pc.text(T - 1, outer[-1] + 0.3, "edge of group", color=Ch.line("rna"), fontsize=FS["tiny"], ha="right", va="bottom")
pc.text(T - 1, inner[-1] + 0.3, "interior", color=Ch.line("dna"), fontsize=FS["tiny"], ha="right", va="bottom")
pc.set_xlim(0, T - 1)
pc.set_ylim(0, max(outer) * 1.15)
Ch.style_axes(pc, "time / steps", "mean domain of danger / area units")
bio.panel(ax, "C", (22.6, 10.4))
