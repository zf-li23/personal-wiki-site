"""Vertex models: neighbour exchange (T1 transition) and the shape index.

A: a T1 transition between four cells: the junction shared by cells 1 and 3 shrinks to a four-fold
vertex and a new junction forms between cells 2 and 4, so cells 1 and 3 lose contact (the elementary
step of convergent extension and of tissue fluidity).
B: the shape index p = P / sqrt(A) of single regular shapes, and the rigidity transition of the
vertex model at a target shape index p0* ~ 3.81 (Bi, Lopez, Schwarz and Manning 2015): below it
energy barriers to T1 transitions are finite (solid-like tissue), above it they vanish (fluid-like).
"""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 9.0)
bio.panel(ax, "A", (0.1, 8.9))


def stage(x0, ell):
    """Four cells around a central junction of signed length ell (vertical if > 0, horizontal if < 0)."""
    c = np.array([x0, 4.6])
    a = abs(ell) / 2
    T, Bm, Lf, Rt = c + [0, 2.6], c + [0, -2.6], c + [-2.8, 0], c + [2.8, 0]
    TL, TR, BL, BR = c + [-2.0, 1.9], c + [2.0, 1.9], c + [-2.0, -1.9], c + [2.0, -1.9]
    if ell >= 0:
        v1, v2 = c + [0, a], c - [0, a]
        cells = {2: [TL, T, TR, v1], 4: [BL, v2, BR, Bm], 1: [TL, v1, v2, BL, Lf], 3: [TR, Rt, BR, v2, v1]}
    else:
        v1, v2 = c + [a, 0], c - [a, 0]
        cells = {2: [TL, T, TR, v1, v2], 4: [BL, v2, v1, BR, Bm], 1: [TL, v2, BL, Lf], 3: [TR, Rt, BR, v1]}
    toks = {1: "ectoderm", 3: "ectoderm", 2: "mesoderm", 4: "mesoderm"}
    for k, pts in cells.items():
        bio.shape(ax, np.array(pts), toks[k], lw=1.2, zorder=4)
    for k, off in ((1, [-1.7, 0]), (3, [1.7, 0]), (2, [0, 1.6]), (4, [0, -1.6])):
        bio.label(ax, tuple(c + off), str(k), size="small", color=P.on_fill())
    ax.plot([v1[0], v2[0]], [v1[1], v2[1]], color=P.ink(), lw=2.2, zorder=6)


stage(3.2, 1.6)
bio.arrow(ax, (6.4, 4.6), (7.6, 4.6), kind="process")
stage(10.8, 0.0)
bio.arrow(ax, (14.0, 4.6), (15.2, 4.6), kind="process")
stage(18.4, -1.6)
bio.label(ax, (3.2, 0.7), "1 and 3 in contact", size="tiny")
bio.label(ax, (10.8, 0.7), "four-fold vertex", size="tiny")
bio.label(ax, (18.4, 0.7), "2 and 4 in contact", size="tiny")

bio.panel(ax, "B", (22.0, 8.9))
x0, x1, yl = 22.8, 29.6, 4.0
lo, hi = 3.45, 4.15
X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
ax.plot([x0, x1], [yl, yl], color=P.muted(), lw=1.0)
ax.fill_between([X(lo), X(3.813)], yl - 0.25, yl + 0.25, color=P.light("ectoderm"), lw=0)
ax.fill_between([X(3.813), X(hi)], yl - 0.25, yl + 0.25, color=P.light("mesoderm"), lw=0)
bio.label(ax, ((X(lo) + X(3.813)) / 2, yl - 0.8), "solid", size="tiny")
bio.label(ax, ((X(3.813) + X(hi)) / 2, yl - 0.8), "fluid", size="tiny")
for v, name in ((2 * np.sqrt(np.pi), "circle 3.545"), (np.sqrt(8 * np.sqrt(3)), "hexagon 3.722"),
                (3.813, "p0* ≈ 3.81"), (4.0, "square 4.0")):
    ax.plot([X(v), X(v)], [yl - 0.3, yl + 0.3], color=P.ink(), lw=1.2)
    bio.label(ax, (X(v), yl + 0.7 + (0.6 if "p0" in name else 0)), name, size="tiny", rotation=0)
bio.label(ax, (26.2, 1.6), "shape index p = perimeter / √area", size="tiny")
