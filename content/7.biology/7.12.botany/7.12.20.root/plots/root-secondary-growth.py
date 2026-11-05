# Secondary growth of a tetrarch eudicot root (transverse sections; xylem blue, phloem orange, vascular
# cambium yellow, cork brown). (A) Primary structure. (B) Cambium strips arise in the parenchyma inside
# the four primary phloem strands. (C) Pericycle cells opposite the xylem poles join in: a continuous,
# wavy cambium; the early strips have already produced secondary xylem; a cork cambium arises in the
# pericycle. (D) The cambium has become circular; secondary xylem dominates, secondary phloem lies
# outside the cambium, the primary phloem is crushed, broad rays face the xylem poles and the periderm
# replaces the shed cortex and epidermis.
import math

import numpy as np
from matplotlib.patches import Circle, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32.0, 10.6)
TH = np.linspace(0, 2 * np.pi, 361)
ARMS = [math.pi / 4 + k * math.pi / 2 for k in range(4)]


def ring(c, r0, r1, tok, alpha=None, z=3, edge=True):
    o = np.c_[c[0] + r1 * np.cos(TH), c[1] + r1 * np.sin(TH)]
    i = np.c_[c[0] + r0 * np.cos(TH[::-1]), c[1] + r0 * np.sin(TH[::-1])]
    ax.add_patch(Polygon(np.vstack([o, i]), closed=True, facecolor=P.fill(tok), edgecolor="none", lw=0, zorder=z))
    if edge:
        for r in (r0, r1):
            ax.add_patch(Circle(c, r, facecolor="none", edgecolor=P.edge(tok), lw=0.7, zorder=z + 0.01))


def disk(c, r, tok, z=3):
    ax.add_patch(Circle(c, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=z))


def curve_r(c, rf, tok, lw=2.4, z=8, closed=True, fill=None):
    r = rf(TH)
    pts = np.c_[c[0] + r * np.cos(TH), c[1] + r * np.sin(TH)]
    if fill:
        ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(fill), edgecolor="none", zorder=z - 1))
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=lw, zorder=z)


def xylem_star(c, R=1.25, w=0.36, z=6):
    for a in ARMS:
        tip = c + R * np.array([math.cos(a), math.sin(a)])
        l = c + w * np.array([math.cos(a + math.pi / 2), math.sin(a + math.pi / 2)])
        r = c + w * np.array([math.cos(a - math.pi / 2), math.sin(a - math.pi / 2)])
        ax.add_patch(Polygon([l, tip, r], closed=True, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.8,
                             zorder=z))
    ax.add_patch(Circle(c, w * 1.05, facecolor=P.fill("xylem"), edgecolor="none", zorder=z + 0.1))


def _unused():
    pass


def phloem(c, R=1.18, r=0.3, z=6, tok="phloem", crushed=False):
    for a in ARMS:
        b = a + math.pi / 4
        p = c + R * np.array([math.cos(b), math.sin(b)])
        if crushed:
            t = np.linspace(b - 0.25, b + 0.25, 20)
            ax.plot(c[0] + R * np.cos(t), c[1] + R * np.sin(t), color=P.edge(tok), lw=2.5, zorder=z)
        else:
            ax.add_patch(Circle(p, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=z))


def primary(c, cortex=True):
    if cortex:
        ring(c, 1.75, 3.2, "cytoplasm", z=2)
        ring(c, 3.05, 3.2, "cell_wall", z=2.5)
        ring(c, 1.75, 1.95, "endodermis", z=3)
    disk(c, 1.75, "cytoplasm", z=3)
    ring(c, 1.55, 1.75, "pericycle", z=3.5)


cs = [np.array([4.0, 4.9]), np.array([12.0, 4.9]), np.array([20.0, 4.9]), np.array([28.0, 4.9])]
titles = ["Primary structure", "Cambium strips", "Wavy cambium ring", "Secondary structure"]
for k, c in enumerate(cs):
    bio.panel(ax, "ABCD"[k], (c[0] - 4.1, 10.4))
    bio.label(ax, (c[0], 10.0), titles[k], size="normal", bold=True)

# A
primary(cs[0])
xylem_star(cs[0])
phloem(cs[0])
# B
primary(cs[1])
xylem_star(cs[1])
phloem(cs[1])
for a in ARMS:
    b = a + math.pi / 4
    t = np.linspace(b - 0.45, b + 0.45, 30)
    ax.plot(cs[1][0] + 0.82 * np.cos(t), cs[1][1] + 0.82 * np.sin(t), color=P.edge("cambium"), lw=2.6, zorder=8)
# C
c = cs[2]
primary(c)
ring(c, 1.55, 1.68, "cork", z=3.8)


def wavy(th):
    return 1.2 + 0.32 * np.cos(4 * (th - ARMS[0]))


r_sx = lambda th: wavy(th) - 0.06
curve_r(c, r_sx, "xylem", lw=0.0, z=5, fill="xylem")
xylem_star(c, R=1.25, z=6)
phloem(c, R=1.32, r=0.24)
curve_r(c, wavy, "cambium", lw=2.6, z=8)
# D
c = cs[3]
ring(c, 3.05, 3.45, "cork", z=2)
ring(c, 2.55, 3.05, "phloem", z=2.5)
disk(c, 2.5, "xylem", z=3)
ax.add_patch(Circle(c, 2.5, facecolor=P.mix(P.fill("xylem"), P.surface(), 0.45), edgecolor="none", zorder=3.1))
for a in ARMS:  # broad rays opposite the xylem poles
    for d in (-0.05, 0.05):
        t = a + d
        ax.plot([c[0] + 1.3 * math.cos(t), c[0] + 3.0 * math.cos(t)], [c[1] + 1.3 * math.sin(t), c[1] + 3.0 * math.sin(t)],
                color=P.edge("lipid"), lw=1.0, zorder=4)
    for d in (0.4, 0.8, 1.2):  # narrow rays
        t = a + d
        ax.plot([c[0] + 1.7 * math.cos(t), c[0] + 2.95 * math.cos(t)], [c[1] + 1.7 * math.sin(t), c[1] + 2.95 * math.sin(t)],
                color=P.edge("lipid"), lw=0.6, zorder=4)
xylem_star(c, R=1.25, z=6)
phloem(c, R=3.0, crushed=True, z=5)
ring(c, 2.47, 2.57, "cambium", z=8)

L = []  # (panel, point, label x offset, label y, text)
L += [(0, 2.6 * np.array([0, 1]), -1.2, 9.3, "Cortex"), (0, 1.18 * np.array([0, 1]), 1.2, 9.3, "Primary phloem"),
      (0, 1.85 * np.array([0.71, -0.71]), 1.2, 0.5, "Endodermis"), (0, 1.65 * np.array([-0.71, -0.71]), -1.2, 0.5, "Pericycle")]
L += [(1, 0.82 * np.array([0, 1]), 1.2, 9.3, "Cambium strip"), (1, 1.0 * np.array([0.71, -0.71]), 1.2, 0.5, "Primary xylem pole")]
L += [(2, 0.95 * np.array([0, 1]), -1.2, 9.3, "Secondary xylem"), (2, 1.52 * np.array([0.71, 0.71]), 1.2, 9.3, "Vascular cambium"),
      (2, 1.61 * np.array([0, -1]), 1.2, 0.5, "Cork cambium (pericycle)")]
L += [(3, 3.25 * np.array([0, 1]), 1.0, 9.3, "Periderm"), (3, 2.8 * np.array([-0.5, 0.866]), -2.2, 8.6, "Secondary phloem"),
      (3, 2.1 * np.array([0.71, -0.71]), 2.0, 0.5, "Broad ray"), (3, 1.9 * np.array([-0.97, -0.26]), -2.4, 1.2, "Secondary xylem")]
for k, off, dx, y, text in L:
    bio.callout(ax, tuple(cs[k] + off), (cs[k][0] + dx, y), text, size="small")
