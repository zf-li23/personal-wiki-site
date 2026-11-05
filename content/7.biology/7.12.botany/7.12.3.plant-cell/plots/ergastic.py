"""Ergastic substances (schematic). Top row, starch grains: a simple grain with a central hilum and
concentric lamellae (legumes, wheat); a simple grain with an eccentric hilum (potato tuber); a compound grain
of many small angular granules in one amyloplast (rice, oat); a half-compound grain, two hila each with
its own lamellae inside common outer lamellae (potato). Bottom row: an aleurone grain (protein body) of
castor bean with a protein crystalloid and a globoid of phytin in amorphous protein; and crystals in
crystal idioblasts: a druse (a spherical cluster of calcium oxalate crystals), a bundle of raphides (needle
crystals), a prismatic crystal, and a cystolith of calcium carbonate on a cellulose stalk hanging from the
outer wall of an enlarged epidermal cell (lithocyst) of Ficus.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 11.8)
ST = "carbohydrate"


def grain(c, rx, ry, hilum=(0.0, 0.0), n=6, z=5):
    """Lamellae: ellipses shrinking towards the hilum (offset given as a fraction of the radii)."""
    hx, hy = c[0] + hilum[0] * rx, c[1] + hilum[1] * ry
    for k in range(n, 0, -1):
        f = k / n
        cx, cy = hx + (c[0] - hx) * f, hy + (c[1] - hy) * f
        ax.add_patch(Ellipse((cx, cy), 2 * rx * f, 2 * ry * f, facecolor=P.fill(ST) if k == n else "none",
                             edgecolor=P.edge(ST), lw=0.9 if k == n else 0.45, zorder=z))
    ax.add_patch(Circle((hx, hy), 0.07, color=P.edge(ST), zorder=z + 1))
    return (hx, hy)


def title(x, y, t):
    bio.label(ax, (x, y), t, size="small")


# ---------------- starch grains
bio.panel(ax, "A", (0.1, 11.7))
bio.label(ax, (0.8, 11.65), "Starch grains", size="title", ha="left", va="top")
h1 = grain((3.0, 9.0), 1.25, 1.05, (0, 0), n=6)
title(3.0, 7.2, "simple, concentric")
h2 = grain((8.6, 9.0), 1.0, 1.45, (0.0, -0.72), n=8)
title(8.6, 7.2, "simple, eccentric")
# compound grain: polygonal granules inside one outline
c3 = (14.4, 9.0)
ax.add_patch(Ellipse(c3, 2.7, 2.3, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.9, zorder=4))
rng = np.random.default_rng(3)
pts = []
for r, nn in ((0.0, 1), (0.5, 6), (0.95, 11)):
    for k in range(nn):
        a = 2 * math.pi * k / nn + r
        pts.append((c3[0] + r * 1.15 * math.cos(a), c3[1] + r * 0.95 * math.sin(a)))
for p in pts:
    m = 6
    poly = [(p[0] + 0.23 * math.cos(2 * math.pi * j / m + rng.uniform(0, 0.4)), p[1] + 0.21 * math.sin(2 * math.pi * j / m + rng.uniform(0, 0.4))) for j in range(m)]
    ax.add_patch(Polygon(poly, closed=True, facecolor=P.fill(ST), edgecolor=P.edge(ST), lw=0.5, zorder=5))
title(14.4, 7.2, "compound (rice, oat)")
# half-compound: two hila, own lamellae, common outer lamellae
c4 = (20.6, 9.0)
for k, (rx, ry) in enumerate(((1.55, 1.25), (1.4, 1.1))):
    ax.add_patch(Ellipse(c4, 2 * rx, 2 * ry, facecolor=P.fill(ST) if k == 0 else "none", edgecolor=P.edge(ST), lw=0.9 if k == 0 else 0.5, zorder=5))
grain((c4[0] - 0.55, c4[1]), 0.62, 0.9, (0, 0), n=4, z=6)
grain((c4[0] + 0.62, c4[1]), 0.62, 0.9, (0, 0), n=4, z=6)
title(20.6, 7.2, "half-compound (potato)")
bio.callout(ax, h2, (10.9, 7.95), "Hilum", size="tiny")
bio.callout(ax, (8.6 + 0.62, 9.35), (10.9, 10.4), "Lamellae", size="tiny")

# ---------------- protein body and crystals
bio.panel(ax, "B", (0.1, 6.2))
bio.label(ax, (0.8, 6.15), "Protein bodies and crystals", size="title", ha="left", va="top")
# aleurone grain
a = (2.8, 3.0)
ax.add_patch(Circle(a, 1.25, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=4))
ax.add_patch(Polygon([(a[0] - 0.75, a[1] - 0.2), (a[0] + 0.25, a[1] - 0.55), (a[0] + 0.45, a[1] + 0.35), (a[0] - 0.4, a[1] + 0.7)],
                     closed=True, facecolor=P.light("protein"), edgecolor=P.edge("protein"), lw=0.9, zorder=5))
ax.add_patch(Circle((a[0] + 0.62, a[1] - 0.6), 0.3, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"), lw=0.8, zorder=5))
bio.callout(ax, (a[0] - 0.2, a[1] + 0.15), (1.0, 0.6), "Crystalloid", size="tiny")
bio.callout(ax, (a[0] + 0.62, a[1] - 0.6), (4.4, 0.6), "Globoid", size="tiny")
title(2.8, 4.65, "aleurone grain")


def idioblast(c, w, h):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.35",
                                facecolor=P.fill("vacuole"), edgecolor=P.edge("cell_wall"), lw=1.6, zorder=3))


XT = "neutral"
# druse
d = (8.0, 3.0)
idioblast(d, 2.6, 2.6)
for k in range(16):
    ang = 2 * math.pi * k / 16 + 0.1 * (k % 2)
    L = 0.95 if k % 2 == 0 else 0.75
    tip = (d[0] + L * math.cos(ang), d[1] + L * math.sin(ang))
    b1 = (d[0] + 0.32 * math.cos(ang - 0.32), d[1] + 0.32 * math.sin(ang - 0.32))
    b2 = (d[0] + 0.32 * math.cos(ang + 0.32), d[1] + 0.32 * math.sin(ang + 0.32))
    ax.add_patch(Polygon([b1, tip, b2], closed=True, facecolor=P.fill(XT), edgecolor=P.edge(XT), lw=0.6, zorder=5))
ax.add_patch(Circle(d, 0.36, facecolor=P.fill(XT), edgecolor=P.edge(XT), lw=0.6, zorder=6))
title(8.0, 4.65, "druse")
# raphides
r = (12.6, 3.0)
idioblast(r, 3.2, 1.9)
for k in range(13):
    yy = r[1] - 0.45 + k * 0.075
    ax.plot([r[0] - 1.25, r[0] + 1.25], [yy + 0.06 * math.sin(k), yy - 0.06 * math.sin(k)], color=P.edge(XT), lw=0.9, zorder=5)
title(12.6, 4.65, "raphides")
# prismatic crystal
q = (16.9, 3.0)
idioblast(q, 2.2, 2.2)
ax.add_patch(Polygon([(q[0] - 0.55, q[1] - 0.2), (q[0] - 0.05, q[1] - 0.75), (q[0] + 0.6, q[1] - 0.25), (q[0] + 0.5, q[1] + 0.45),
                      (q[0], q[1] + 0.8), (q[0] - 0.62, q[1] + 0.35)], closed=True, facecolor=P.fill(XT), edgecolor=P.edge(XT), lw=0.9, zorder=5))
ax.plot([q[0] - 0.05, q[0] - 0.05, q[0] - 0.62], [q[1] - 0.75, q[1] + 0.1, q[1] + 0.35], color=P.edge(XT), lw=0.6, zorder=6)
ax.plot([q[0] - 0.05, q[0] + 0.5], [q[1] + 0.1, q[1] + 0.45], color=P.edge(XT), lw=0.6, zorder=6)
title(16.9, 4.65, "prismatic crystal")
# cystolith in a lithocyst below the leaf surface
x0, ys = 19.6, 4.0
for k in range(5):
    xx = x0 + k * 1.2
    if k == 2:
        continue
    ax.add_patch(FancyBboxPatch((xx, ys - 0.9), 1.1, 0.85, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=1.0, zorder=3))
lc = (x0 + 2.95, ys - 1.4)
ax.add_patch(Ellipse(lc, 1.6, 2.6, facecolor=P.fill("vacuole"), edgecolor=P.edge("cell_wall"), lw=1.4, zorder=3))
ax.plot([lc[0], lc[0]], [ys - 0.12, lc[1] + 0.3], color=P.edge("cell_wall"), lw=2.2, zorder=5)
cy = (lc[0], lc[1] - 0.1)
ax.add_patch(Ellipse(cy, 0.95, 1.3, facecolor=P.fill(XT), edgecolor=P.edge(XT), lw=0.9, zorder=6))
for k in range(18):
    a_ = 2 * math.pi * k / 18
    ax.add_patch(Circle((cy[0] + 0.32 * math.cos(a_), cy[1] + 0.47 * math.sin(a_)), 0.06, color=P.edge(XT), zorder=7))
ax.plot([x0, x0 + 6.0], [ys + 0.05, ys + 0.05], color=P.edge("lipid"), lw=1.6, zorder=4)
bio.callout(ax, (lc[0], ys - 0.45), (25.4, 3.6), "Stalk", size="tiny")
bio.callout(ax, (cy[0] + 0.4, cy[1] - 0.2), (25.4, 1.6), "Cystolith", size="tiny")
bio.callout(ax, (x0 + 0.6, ys + 0.05), (21.2, 5.0), "Cuticle", size="tiny")
title(22.1, 0.35, "cystolith in a lithocyst,")
bio.label(ax, (24.35, 0.35), "Ficus", size="small", italic=True, ha="left")
bio.label(ax, (8.0, 0.9), "calcium oxalate crystals in crystal idioblasts", size="tiny", color=P.muted(), ha="left")
