"""Stomatal complexes in surface view (schematic). Guard cells green (with chloroplasts), subsidiary
cells orange, ordinary epidermal cells pale. A: anomocytic (Ranunculaceae type), no subsidiary cells,
the stoma is surrounded by ordinary epidermal cells. B: anisocytic (Brassicaceae type), three subsidiary
cells, one distinctly smaller. C: paracytic (Rubiaceae type), one subsidiary cell on each side, its long
axis parallel to the pore. D: diacytic (Caryophyllaceae type), two subsidiary cells whose common walls
are at right angles to the guard cells. E: grass stoma: dumbbell-shaped guard cells, flanked by two
subsidiary cells, in a file of long and short epidermal cells. F: sunken stoma of a pine needle in
transverse section: guard cells (with partly lignified walls) lie below the thick-walled subsidiary
cells; the epistomatal chamber above them is plugged with wax, and the substomatal chamber below opens
into the mesophyll.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32.5, 10.8)
GC, SC, EP = "chloroplast", "atp", "cytoplasm"
WALL = P.edge("cell_wall")


def poly(pts, tk, lw=1.0, z=3):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tk), edgecolor=WALL, lw=lw, zorder=z))


def ring_cell(c, r0, r1, a0, a1, tk, ry=1.0, n=30):
    t = np.linspace(math.radians(a0), math.radians(a1), n)
    outer = np.c_[c[0] + r1 * np.cos(t), c[1] + r1 * ry * np.sin(t)]
    inner = np.c_[c[0] + r0 * np.cos(t[::-1]), c[1] + r0 * ry * np.sin(t[::-1])]
    poly(np.vstack([outer, inner]), tk)


def guard_pair(c, h=1.5, w=0.42, angle=90, pore=0.12):
    """Two kidney-shaped guard cells around a pore; long axis along ``angle``."""
    a = math.radians(angle)
    u = np.array([math.cos(a), math.sin(a)])
    v = np.array([-u[1], u[0]])
    t = np.linspace(0, 2 * math.pi, 60)
    for s in (-1, 1):
        cen = np.asarray(c) + v * s * (w * 0.8)
        pts = cen + np.outer(h / 2 * np.cos(t), u) + np.outer(w * np.sin(t), v)
        poly(pts, GC, lw=1.0, z=5)
        for k in (-0.45, 0.0, 0.45):
            p = cen + u * k * h / 2 + v * s * w * 0.25
            ax.add_patch(Circle(p, 0.07, facecolor=P.edge(GC), edgecolor="none", zorder=6))
    pp = np.asarray(c) + np.outer(h * 0.36 * np.cos(t), u) + np.outer(pore * np.sin(t), v)
    ax.add_patch(Polygon(pp, closed=True, facecolor=P.fill("extracellular"), edgecolor=P.edge(GC), lw=0.8, zorder=6))


def epid_ring(c, r0, r1, cuts, ry=1.0):
    for a0, a1 in zip(cuts, cuts[1:] + [cuts[0] + 360]):
        ring_cell(c, r0, r1, a0, a1, EP, ry=ry)


def title(x, t1, t2):
    bio.label(ax, (x, 9.9), t1, size="small")
    bio.label(ax, (x, 9.35), t2, size="tiny", color=P.muted())


Y = 5.6
# A anomocytic
c = (2.6, Y)
epid_ring(c, 0.8, 2.3, [10, 75, 140, 200, 255, 320], ry=1.15)
guard_pair(c)
bio.panel(ax, "A", (0.1, 10.7))
title(2.6, "Anomocytic", "Ranunculaceae type")
# B anisocytic
c = (7.6, Y)
epid_ring(c, 1.7, 2.4, [0, 70, 150, 220, 290], ry=1.15)
ring_cell(c, 0.8, 1.7, -40, 85, SC, ry=1.1)
ring_cell(c, 0.8, 1.7, 85, 230, SC, ry=1.1)
ring_cell(c, 0.8, 1.35, 230, 320, SC, ry=1.1)
ring_cell(c, 1.35, 1.7, 230, 320, EP, ry=1.1)
guard_pair(c)
bio.panel(ax, "B", (5.1, 10.7))
title(7.6, "Anisocytic", "Brassicaceae type")
# C paracytic
c = (12.6, Y)
epid_ring(c, 0.8, 2.4, [60, 120, 180, 240, 300, 360], ry=1.1)
for a0, a1 in ((118, 242), (-62, 62)):
    ring_cell(c, 0.8, 1.45, a0, a1, SC, ry=1.1)
guard_pair(c)
bio.panel(ax, "C", (10.1, 10.7))
title(12.6, "Paracytic", "Rubiaceae type")
# D diacytic
c = (17.6, Y)
epid_ring(c, 1.55, 2.4, [30, 100, 170, 240, 310], ry=1.15)
ring_cell(c, 0.8, 1.55, 0, 180, SC, ry=1.1)
ring_cell(c, 0.8, 1.55, 180, 360, SC, ry=1.1)
guard_pair(c, angle=90)
bio.panel(ax, "D", (15.1, 10.7))
title(17.6, "Diacytic", "Caryophyllaceae type")

# E grass stoma (horizontal pore in a file of cells)
bio.panel(ax, "E", (20.1, 10.7))
title(22.4, "Grass (Poaceae)", "dumbbell-shaped guard cells")
x0, x1 = 20.3, 24.5
for yy, hh in ((Y + 1.0, 1.0), (Y - 2.0, 1.0)):
    poly([(x0, yy), (x1, yy), (x1, yy + hh), (x0, yy)][:3] + [(x0, yy + hh)], EP)
poly([(x0, Y - 1.0), (21.4, Y - 1.0), (21.4, Y + 1.0), (x0, Y + 1.0)], EP)
poly([(23.4, Y - 1.0), (x1, Y - 1.0), (x1, Y + 1.0), (23.4, Y + 1.0)], EP)
gx = (21.4, 23.4)
poly([(gx[0], Y + 0.3), (gx[1], Y + 0.3), (gx[1] - 0.25, Y + 1.0), (gx[0] + 0.25, Y + 1.0)], SC)
poly([(gx[0], Y - 0.3), (gx[1], Y - 0.3), (gx[1] - 0.25, Y - 1.0), (gx[0] + 0.25, Y - 1.0)], SC)
for s in (-1, 1):
    xs = np.linspace(gx[0] + 0.05, gx[1] - 0.05, 60)
    rel = (xs - (gx[0] + gx[1]) / 2) / ((gx[1] - gx[0]) / 2)
    half = 0.07 + 0.19 * rel ** 6
    mid = Y + s * (0.04 + half)
    pts = np.r_[np.c_[xs, mid + half], np.c_[xs[::-1], (mid - half)[::-1]]]
    poly(pts, GC, z=5)
    for xe in (gx[0] + 0.2, gx[1] - 0.2):
        ax.add_patch(Circle((xe, Y + s * 0.25), 0.06, facecolor=P.edge(GC), edgecolor="none", zorder=6))
ax.plot([gx[0] + 0.5, gx[1] - 0.5], [Y, Y], color=P.edge(GC), lw=1.2, zorder=6)
bio.callout(ax, (22.9, Y + 0.15), (24.0, 2.4), "Guard cell", size="tiny")
bio.callout(ax, (21.9, Y - 0.7), (21.0, 2.4), "Subsidiary cell", size="tiny")

# F pine: sunken stoma in section
bio.panel(ax, "F", (25.1, 10.7))
title(27.5, "Pine needle", "sunken stoma, section")
cx = 27.5
top = 7.0
# thick-walled epidermis on both sides
for xs in ((25.2, 26.2), (28.8, 29.8)):
    poly([(xs[0], top - 1.2), (xs[1], top - 1.2), (xs[1], top), (xs[0], top)], "sclerenchyma")
    ax.add_patch(Polygon([(xs[0] + 0.35, top - 0.85), (xs[1] - 0.35, top - 0.85), (xs[1] - 0.35, top - 0.35), (xs[0] + 0.35, top - 0.35)],
                         closed=True, facecolor=P.fill("extracellular"), edgecolor="none", zorder=4))
# subsidiary cells overarching the pit
for s in (-1, 1):
    pts = [(cx + s * 1.3, top), (cx + s * 0.55, top), (cx + s * 0.45, top - 1.4), (cx + s * 1.3, top - 1.9)]
    poly(pts, SC)
# guard cells below them
for s in (-1, 1):
    ax.add_patch(Ellipse((cx + s * 0.42, top - 2.25), 0.62, 0.8, facecolor=P.fill(GC), edgecolor=WALL, lw=1.0, zorder=5))
    ax.add_patch(Ellipse((cx + s * 0.55, top - 2.05), 0.25, 0.3, facecolor=P.edge("sclerenchyma"), edgecolor="none", zorder=6))
# wax plug in the epistomatal chamber
ax.add_patch(Polygon([(cx - 0.5, top - 0.05), (cx + 0.5, top - 0.05), (cx + 0.38, top - 1.35), (cx - 0.38, top - 1.35)], closed=True,
                     facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.6, zorder=4))
# hypodermis and mesophyll with the substomatal chamber
for k, xs in enumerate(((25.2, 26.3), (28.7, 29.8))):
    poly([(xs[0], top - 2.6), (xs[1], top - 2.6), (xs[1], top - 1.2), (xs[0], top - 1.2)], "sclerenchyma", z=3)
for k in range(5):
    xx = 25.3 + k * 1.0
    if 2 <= k <= 2:
        continue
    poly([(xx, top - 4.2), (xx + 0.9, top - 4.2), (xx + 0.9, top - 2.8), (xx, top - 2.8)], "plant", z=3)
bio.callout(ax, (cx, top - 0.6), (30.2, 8.4), "Wax plug", size="tiny")
bio.callout(ax, (cx + 0.9, top - 1.0), (30.2, 6.4), "Subsidiary cell", size="tiny")
bio.callout(ax, (cx + 0.42, top - 2.35), (30.2, 4.4), "Guard cell", size="tiny")
bio.callout(ax, (cx, top - 3.4), (26.3, 1.2), "Substomatal chamber", size="tiny")
bio.callout(ax, (29.3, top - 1.9), (30.2, 2.6), "Hypodermis", size="tiny")

# labels for A-D
bio.callout(ax, (2.6 + 0.33, Y + 0.3), (1.0, 2.0), "Guard cell", size="tiny")
bio.callout(ax, (2.6 + 1.6, Y + 1.5), (4.6, 2.0), "Epidermal cell", size="tiny")
bio.callout(ax, (7.6 + 1.2, Y + 0.6), (8.6, 2.0), "Subsidiary cell", size="tiny")
bio.callout(ax, (12.6, Y), (12.6, 2.0), "Pore", size="tiny")
