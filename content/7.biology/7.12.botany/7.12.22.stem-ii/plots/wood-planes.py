# The three planes of section of wood, on a block cut from the outer part of a (slightly tapering) trunk;
# the pith lies off to the left. Transverse face (top): growth rings as concentric arcs, rays as radial
# lines. Radial face (front, through the pith): rings as near-parallel vertical bands, rays as horizontal
# ribbons ("brick wall"). Tangential face (right, perpendicular to a radius): rings as nested V-shaped
# curves (because of the taper), rays cut across as small spindles. Bark (with cambium and secondary phloem) drawn lifted off to the right.
import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 14.0)
rng = np.random.default_rng(7)
O = np.array([3.0, 1.4])
X0, X1, Yd, Z1 = 0.0, 10.0, 4.0, 7.0  # block: radial x, tangential y, vertical z
PITH = np.array([-6.0, 2.0])  # pith position in (x, y)
TAPER = 0.12
RINGS = np.array(np.arange(6.5, 17.3, 0.3)[::4].tolist() + [16.2, 16.45, 16.7, 16.95])


def pr(x, y, z):
    return np.c_[O[0] + np.asarray(x) + 0.55 * np.asarray(y), O[1] + np.asarray(z) + 0.42 * np.asarray(y)]


def face(pts, tok, z=3):
    return ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=z))


top = face(pr([X0, X1, X1, X0], [0, 0, Yd, Yd], [Z1] * 4), "earlywood")
front = face(pr([X0, X1, X1, X0], [0, 0, 0, 0], [0, 0, Z1, Z1]), "earlywood")
side = face(pr([X1] * 4, [0, Yd, Yd, 0], [0, 0, Z1, Z1]), "earlywood")


def clipped_line(pts, clip, color, lw, z=5, ls="-"):
    (l,) = ax.plot(pts[:, 0], pts[:, 1], color=color, lw=lw, zorder=z, solid_capstyle="butt", ls=ls)
    l.set_clip_path(clip)


LW = P.edge("latewood")
# transverse face: ring arcs and rays
for r in RINGS:
    rz = r - TAPER * Z1
    t = np.linspace(-0.6, 0.6, 200)
    xs, ys = PITH[0] + rz * np.cos(t), PITH[1] + rz * np.sin(t)
    clipped_line(pr(xs, ys, np.full_like(xs, Z1)), top, LW, 3.0)
for k in range(14):
    a = rng.uniform(-0.25, 0.3)
    rr = np.linspace(4, 20, 30)
    xs, ys = PITH[0] + rr * np.cos(a), PITH[1] + rr * np.sin(a)
    clipped_line(pr(xs, ys, np.full_like(xs, Z1)), top, P.edge("lipid"), 0.7, z=5.5)
# radial face (y = 0): rings are near-vertical lines; rays are horizontal ribbons
for r in RINGS:
    zs = np.linspace(0, Z1, 50)
    rz = r - TAPER * zs
    xs = PITH[0] + np.sqrt(np.maximum(rz ** 2 - (0 - PITH[1]) ** 2, 0))
    clipped_line(pr(xs, np.zeros_like(xs), zs), front, LW, 3.0)
for k in range(26):
    zc, x0 = rng.uniform(0.3, Z1 - 0.3), rng.uniform(X0, X1 - 2.0)
    L = rng.uniform(1.0, 3.0)
    q = pr([x0, x0 + L, x0 + L, x0], [0, 0, 0, 0], [zc - 0.07, zc - 0.07, zc + 0.07, zc + 0.07])
    p = ax.add_patch(Polygon(q, closed=True, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.4, zorder=5.5))
    p.set_clip_path(front)
# tangential face (x = X1): rings as V curves
for r in RINGS:
    ys = np.linspace(0, Yd, 80)
    d = np.hypot(X1 - PITH[0], ys - PITH[1])
    zs = (r - d) / TAPER
    ok = (zs >= -1) & (zs <= Z1 + 1)
    if ok.sum() > 2:
        clipped_line(pr(np.full(ok.sum(), X1), ys[ok], zs[ok]), side, LW, 3.0)
for k in range(40):
    yc, zc = rng.uniform(0.2, Yd - 0.2), rng.uniform(0.3, Z1 - 0.3)
    h = rng.uniform(0.25, 0.5)
    t = np.linspace(0, 2 * np.pi, 20)
    q = pr(np.full(20, X1), yc + 0.05 * np.cos(t), zc + h * np.sin(t))
    p = ax.add_patch(Polygon(q, closed=True, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.4, zorder=5.5))
    p.set_clip_path(side)
# bark and cambium slab beyond the tangential face
GAP = 3.2  # bark drawn detached (exploded view) so that the tangential face of the wood is visible
for x_a, x_b, tok in ((X1 + GAP, X1 + GAP + 0.15, "cambium"), (X1 + GAP + 0.15, X1 + GAP + 0.9, "phloem"), (X1 + GAP + 0.9, X1 + GAP + 2.0, "cork")):
    face(pr([x_a, x_b, x_b, x_a], [0, 0, 0, 0], [0, 0, Z1, Z1]), tok, z=6)
    face(pr([x_a, x_b, x_b, x_a], [0, 0, Yd, Yd], [Z1] * 4), tok, z=6)
    face(pr([x_b] * 4, [0, Yd, Yd, 0], [0, 0, Z1, Z1]), tok, z=5.8)
for xy, txt, at in ((pr(5, 2, Z1)[0], "Transverse section", (8.0, 13.3)), (pr(4, 0, 2.5)[0], "Radial section", (1.0, 0.5)),
                    (pr(X1, 2, 3.0)[0], "Tangential section", (12.8, 0.4))):
    bio.callout(ax, tuple(xy), at, txt, size="normal")
bio.callout(ax, tuple(pr(X1 + GAP + 0.08, 0, 6.0)[0]), (22.0, 12.6), "Vascular cambium", size="small")
bio.callout(ax, tuple(pr(X1 + GAP + 0.5, 0, 5.0)[0]), (22.0, 11.8), "Secondary phloem", size="small")
bio.callout(ax, tuple(pr(X1 + GAP + 1.5, 0, 4.0)[0]), (22.0, 11.0), "Outer bark", size="small")
bio.callout(ax, tuple(pr(2.3, 1.0, Z1)[0]), (1.0, 12.6), "Growth ring", size="small")
bio.callout(ax, tuple(pr(7.5, 0, 5.2)[0]), (1.0, 11.6), "Ray", size="small")
bio.label(ax, (1.0, 9.8), "← towards pith", size="small", color=P.muted(), ha="left")
bio.label(ax, tuple(pr(X1 + GAP + 1.0, Yd, Z1)[0] + [0, 0.5]), "bark, lifted off", size="tiny", color=P.muted())
