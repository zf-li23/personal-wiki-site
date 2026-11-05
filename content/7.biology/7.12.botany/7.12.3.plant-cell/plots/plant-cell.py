"""A mature, vacuolated parenchyma cell of a leaf in section, with parts of three neighbours (schematic,
not to scale). The cell wall (primary wall) of each cell is cemented to its neighbours by the middle
lamella; where three cells meet the walls round off and leave an intercellular space. Plasmodesmata cross
the shared wall. Inside the plasma membrane: a nucleus pushed to the side by the central vacuole
(nuclear envelope with pores, nucleolus), chloroplasts with grana, an amyloplast with starch grains,
mitochondria, rough and smooth endoplasmic reticulum, Golgi stacks, a peroxisome (microbody) with a
crystalline core, an oil body, and the cytosol, which forms a thin layer between wall and tonoplast.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 15.0)


def rounded(corners, r, n=10):
    c = np.asarray(corners, float)
    out = []
    for i in range(len(c)):
        p0, p1, p2 = c[i - 1], c[i], c[(i + 1) % len(c)]
        a = p1 + (p0 - p1) / np.linalg.norm(p0 - p1) * r
        b = p1 + (p2 - p1) / np.linalg.norm(p2 - p1) * r
        for t in np.linspace(0, 1, n):
            out.append((1 - t) ** 2 * a + 2 * (1 - t) * t * p1 + t ** 2 * b)
    return np.array(out)


def shrink(poly, d):
    """Offset a convex polygon inward by d (corner by corner, along the angle bisector)."""
    c = np.asarray(poly, float)
    out = []
    for i in range(len(c)):
        p0, p1, p2 = c[i - 1], c[i], c[(i + 1) % len(c)]
        u = (p0 - p1) / np.linalg.norm(p0 - p1)
        v = (p2 - p1) / np.linalg.norm(p2 - p1)
        b = u + v
        if np.linalg.norm(b) < 1e-6:  # straight corner: step along the edge normal (polygons are anticlockwise)
            out.append(p1 + np.array([-v[1], v[0]]) * d)
            continue
        b /= np.linalg.norm(b)
        s = math.sqrt(max(1e-9, (1 - np.dot(u, v)) / 2))
        out.append(p1 + b * d / s)
    return np.array(out)


# the main cell and three neighbours sharing its walls (a small tiling)
main = np.array([(6.2, 2.0), (17.6, 2.0), (19.0, 7.4), (17.6, 12.8), (6.2, 12.8), (4.8, 7.4)])
right = np.array([(17.6, 2.0), (23.6, 2.0), (25.0, 7.4), (23.6, 12.8), (17.6, 12.8), (19.0, 7.4)])
top = np.array([(6.2, 12.8), (17.6, 12.8), (17.6, 17.0), (6.2, 17.0)])
left = np.array([(-1.0, 2.0), (6.2, 2.0), (4.8, 7.4), (6.2, 12.8), (-1.0, 12.8)])
bottom = np.array([(-1.0, -3.0), (25.0, -3.0), (23.6, 2.0), (17.6, 2.0), (6.2, 2.0), (-1.0, 2.0)])

ax.add_patch(Polygon([(0, 0), (26, 0), (26, 15), (0, 15)], closed=True, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
WALL = 0.32
for k, poly in enumerate((main, right, top, left, bottom)):
    o = rounded(poly, 0.55)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=1.4, zorder=1))
    if k:
        inner = rounded(shrink(poly, WALL), 0.4)
        ax.add_patch(PathPatch(Path(inner, closed=True), facecolor=P.light("cytoplasm"), edgecolor=P.edge("membrane"), lw=0.6, zorder=2))
ax.set_xlim(0, 26)
ax.set_ylim(0, 15)

# protoplast of the main cell
proto = rounded(shrink(main, WALL), 0.45)
bio.membrane(ax, proto, "cytoplasm", thickness=0.08, zorder=3)
vac_outline = rounded(shrink(main, 1.25), 1.2)
ax.add_patch(PathPatch(Path(vac_outline, closed=True), facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=1.3, zorder=6))

# plasmodesmata across the wall shared with the right-hand neighbour (lower right face)
pd_pts = []
for t in (0.25, 0.45, 0.65):
    a, b = np.array([17.6, 2.0]), np.array([19.0, 7.4])
    p = a + (b - a) * t
    n = np.array([b[1] - a[1], -(b[0] - a[0])])
    n /= np.linalg.norm(n)
    q0, q1 = p - n * (WALL + 0.12), p + n * (WALL + 0.12)
    tang = (b - a) / np.linalg.norm(b - a) * 0.05
    for s in (-1, 1):
        ax.plot([q0[0] + s * tang[0], q1[0] + s * tang[0]], [q0[1] + s * tang[1], q1[1] + s * tang[1]],
                color=P.edge("membrane"), lw=0.8, zorder=7)
    ax.plot([q0[0], q1[0]], [q0[1], q1[1]], color=P.edge("er"), lw=0.5, zorder=7)
    pd_pts.append(p)

# nucleus pushed against the wall
nu = bio.nucleus(ax, (8.0, 9.6), 1.15, pores=12, seed=4, zorder=8)
# chloroplasts in the peripheral cytoplasm
for (x, y, a) in ((10.4, 12.08, 0), (13.4, 12.08, 0), (16.2, 12.0, -8), (18.15, 9.2, 75), (18.2, 5.6, -75),
                  (14.6, 2.72, 0), (11.2, 2.72, 0), (5.85, 5.4, 72)):
    bio.chloroplast(ax, (x, y), 1.55, 0.6, angle=a, grana=4, zorder=8)
# amyloplast with starch grains
am = (8.4, 2.95)
ax.add_patch(Ellipse(am, 1.45, 0.82, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=1.0, zorder=8))
for dx, dy, w, h in ((-0.32, 0.02, 0.5, 0.42), (0.26, -0.02, 0.55, 0.46)):
    ax.add_patch(Ellipse((am[0] + dx, am[1] + dy), w, h, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=0.6, zorder=9))
    for k in (0.55, 0.25):
        ax.add_patch(Ellipse((am[0] + dx, am[1] + dy), w * k, h * k, fill=False, edgecolor=P.edge("carbohydrate"), lw=0.35, zorder=9))
# mitochondria
for (x, y, a) in ((12.0, 11.75, 8), (17.2, 3.4, 60), (10.0, 3.35, -5), (6.0, 8.1, 85)):
    bio.mitochondrion(ax, (x, y), 1.0, 0.42, angle=a, cristae=5, zorder=8)
# rough ER beside the nucleus, smooth ER as tubules
bio.er(ax, (7.15, 11.45), 0.9, 0.75, sheets=3, angle=-10, zorder=7)
ser = np.array([(15.0, 12.05), (15.3, 11.8), (15.6, 12.05), (15.9, 11.8), (16.1, 11.95)])
for dy in (0.0,):
    ax.plot(ser[:, 0] - 3.0, ser[:, 1] - 9.45 + dy, color=P.edge("er"), lw=2.4, solid_capstyle="round", zorder=7)
    ax.plot(ser[:, 0] - 3.0, ser[:, 1] - 9.45 + dy, color=P.fill("er"), lw=1.3, solid_capstyle="round", zorder=7.1)
# Golgi stacks
bio.golgi(ax, (18.1, 7.4), 0.95, cisternae=4, curve=0.2, angle=90, zorder=7)
bio.golgi(ax, (6.0, 6.75), 0.8, cisternae=4, curve=0.18, angle=-90, zorder=7)
# peroxisome with crystalline core, oil body
px = (16.0, 2.8)
ax.add_patch(Circle(px, 0.3, facecolor=P.fill("peroxisome"), edgecolor=P.edge("peroxisome"), lw=1.0, zorder=8))
ax.add_patch(Polygon([(px[0] - 0.12, px[1] - 0.1), (px[0] + 0.12, px[1] - 0.1), (px[0] + 0.12, px[1] + 0.1), (px[0] - 0.12, px[1] + 0.1)],
                     closed=True, facecolor=P.edge("peroxisome"), edgecolor="none", zorder=9))
ob = (12.75, 2.72)
ax.add_patch(Circle(ob, 0.26, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=8))
# a cytoplasmic strand crossing the vacuole to the nucleus
strand = np.array([(9.2, 9.2), (11.5, 8.0), (14.0, 7.0), (17.2, 6.5)])
t = np.linspace(0, 1, 50)
xs = np.interp(t, np.linspace(0, 1, len(strand)), strand[:, 0])
ys = np.interp(t, np.linspace(0, 1, len(strand)), strand[:, 1])
ax.plot(xs, ys, color=P.edge("membrane"), lw=5.0, solid_capstyle="round", zorder=6.5)
ax.plot(xs, ys, color=P.fill("cytoplasm"), lw=3.6, solid_capstyle="round", zorder=6.6)
bio.label(ax, (11.8, 5.2), "Central vacuole", size="normal", color=P.ink())

# intercellular space at the triple junction (top right of the main cell)
ics = (17.6, 12.8)

L = [
    ((ics[0] - 0.05, ics[1] - 0.15), (21.5, 14.4), "Intercellular space"),
    ((12.0, 12.8), (11.0, 14.45), "Middle lamella"),
    ((14.5, 13.0), (15.2, 14.45), "Cell wall (primary wall)"),
    (pd_pts[1], (21.3, 4.6), "Plasmodesmata"),
    ((18.35, 7.9), (21.3, 7.6), "Golgi apparatus"),
    ((18.3, 9.6), (21.3, 9.4), "Chloroplast"),
    ((18.75, 10.9), (21.3, 11.2), "Plasma membrane"),
    ((16.0, 2.8), (17.4, 0.6), "Peroxisome (microbody)"),
    ((ob[0], ob[1] - 0.1), (14.2, 0.6), "Oil body"),
    ((10.0, 3.1), (8.6, 0.6), "Mitochondrion"),
    ((am[0] - 0.3, am[1] - 0.25), (5.6, 0.6), "Amyloplast (starch)"),
    ((12.3, 2.55), (11.0, 0.6), "Smooth ER"),
    ((7.3, 11.5), (2.6, 13.6), "Rough ER"),
    ((8.0, 10.65), (2.6, 12.2), "Nuclear envelope"),
    ((8.3, 9.8), (2.6, 10.9), "Nucleolus"),
    ((7.4, 9.0), (2.6, 9.6), "Nucleus"),
    ((6.15, 8.6), (2.6, 7.3), "Cytosol"),
    ((6.45, 5.0), (2.6, 6.1), "Tonoplast"),
]
for p, xy, txt in L:
    if txt:
        bio.callout(ax, p, xy, txt, size="small")
# nuclear pore: a dot on the envelope
bio.callout(ax, (8.95, 9.05), (2.6, 8.45), "Nuclear pore", size="small")
