"""Mechanical tissues (schematic). Top row, the four types of collenchyma in transverse section (living
cells with unevenly thickened primary walls, wall material shaded): angular, thickened at the corners
where cells meet; lacunar, thickened around intercellular spaces; lamellar, thickened on the tangential
walls; annular, evenly thickened with a rounded lumen. Bottom row, sclerenchyma (dead cells with
lignified secondary walls): a brachysclereid (stone cell, as in pear fruit) with concentric wall layers
and branched pit canals; an astrosclereid (star-shaped, as in water-lily leaves); an osteosclereid
(bone-shaped, in seed coats and leaves); macrosclereids (columnar, the palisade layer of legume seed
coats); a fibre in longitudinal view, long, tapering and with slit-like pits; and a fibre bundle in
transverse section, thick walls with narrow lumens.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(29.0, 12.6)
CW = "collenchyma"
SW = "sclerenchyma"


def rounded(c, r, n=8):
    c = np.asarray(c, float)
    out = []
    for i in range(len(c)):
        p0, p1, p2 = c[i - 1], c[i], c[(i + 1) % len(c)]
        a = p1 + (p0 - p1) / np.linalg.norm(p0 - p1) * r
        b = p1 + (p2 - p1) / np.linalg.norm(p2 - p1) * r
        for t in np.linspace(0, 1, n):
            out.append((1 - t) ** 2 * a + 2 * (1 - t) * t * p1 + t ** 2 * b)
    return np.array(out)


def hexgrid(x0, y0, nx, ny, r):
    cells = []
    for j in range(ny):
        for i in range(nx):
            cx = x0 + i * r * math.sqrt(3) + (r * math.sqrt(3) / 2 if j % 2 else 0)
            cy = y0 + j * r * 1.5
            cells.append(np.array([(cx + r * math.cos(math.radians(30 + 60 * k)), cy + r * math.sin(math.radians(30 + 60 * k))) for k in range(6)]))
    return cells


CLIP = [None]


def patch(x0, y0, w, h, tk):
    p = FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.3", facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=1.0, zorder=2)
    ax.add_patch(p)
    CLIP[0] = p


def add(pp):
    ax.add_patch(pp)
    pp.set_clip_path(CLIP[0])


def lumen(pts, z=4):
    add(Polygon(pts, closed=True, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(CW), lw=0.6, zorder=z))


def title(x, y, t):
    bio.label(ax, (x, y), t, size="small")


bio.panel(ax, "A", (0.1, 12.5))
bio.label(ax, (0.8, 12.45), "Collenchyma", size="title", ha="left", va="top")
YA = 7.3
r = 0.78
# angular
patch(0.6, YA - 0.2, 5.8, 3.8, CW)
for c in hexgrid(1.2, YA + 0.4, 4, 3, r):
    cen = c.mean(axis=0)
    lumen(rounded(cen + (c - cen) * 0.88, 0.42))
title(3.5, YA - 0.75, "angular")
# lacunar
patch(7.2, YA - 0.2, 5.8, 3.8, CW)
cells = hexgrid(7.8, YA + 0.4, 4, 3, r)
for c in cells:
    cen = c.mean(axis=0)
    lumen(rounded(cen + (c - cen) * 0.8, 0.12))
for c in cells:
    for v in c[::2]:
        if 7.4 < v[0] < 12.8 and YA < v[1] < YA + 3.4:
            add(Circle(v, 0.13, facecolor=P.fill("extracellular"), edgecolor=P.edge(CW), lw=0.6, zorder=5))
title(10.1, YA - 0.75, "lacunar")
# lamellar
patch(13.8, YA - 0.2, 5.8, 3.8, CW)
for j in range(4):
    for i in range(4):
        x = 14.1 + i * 1.33 + (0.5 if j % 2 else 0)
        y = YA + 0.1 + j * 0.85
        if x + 1.15 > 19.5:
            continue
        lumen(rounded(np.array([(x + 0.05, y + 0.22), (x + 1.2, y + 0.22), (x + 1.2, y + 0.6), (x + 0.05, y + 0.6)]), 0.08))
title(16.7, YA - 0.75, "lamellar")
# annular
patch(20.4, YA - 0.2, 5.8, 3.8, CW)
for c in hexgrid(21.0, YA + 0.4, 4, 3, r):
    cen = c.mean(axis=0)
    add(Circle(cen, r * 0.5, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(CW), lw=0.6, zorder=4))
    add(Polygon(c, closed=True, fill=False, edgecolor=P.edge(CW), lw=0.4, zorder=4))
title(23.3, YA - 0.75, "annular")
bio.callout(ax, (25.85, YA + 2.6), (27.0, 11.0), "Thickened wall", size="tiny")
bio.callout(ax, (24.95, YA + 1.6), (27.0, 9.6), "Living protoplast", size="tiny")

# ---------- B: sclerenchyma
bio.panel(ax, "B", (0.1, 5.9))
bio.label(ax, (0.8, 5.85), "Sclerenchyma", size="title", ha="left", va="top")
YB = 2.7
# brachysclereid
c = np.array([2.2, YB])
ax.add_patch(Circle(c, 1.3, facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=1.2, zorder=3))
for rr in (1.05, 0.8, 0.55):
    ax.add_patch(Circle(c, rr, fill=False, edgecolor=P.edge(SW), lw=0.4, zorder=4))
ax.add_patch(Circle(c, 0.25, facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=0.8, zorder=5))
for k in range(10):
    a = 2 * math.pi * k / 10 + 0.2
    p0 = c + 0.25 * np.array([math.cos(a), math.sin(a)])
    p1 = c + 0.75 * np.array([math.cos(a), math.sin(a)])
    for s in (-1, 1):
        p2 = c + 1.3 * np.array([math.cos(a + s * 0.12), math.sin(a + s * 0.12)])
        ax.plot([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], color=P.fill("extracellular"), lw=1.3, zorder=6)
title(2.2, 0.75, "brachysclereid")
bio.callout(ax, (2.2 + 0.95, YB + 0.35), (4.0, 5.0), "Branched pit canal", size="tiny")
# astrosclereid
c = np.array([6.4, YB])
pts = []
for k in range(14):
    a = 2 * math.pi * k / 14
    rr = 1.35 if k % 2 == 0 else 0.35
    pts.append(c + rr * np.array([math.cos(a), math.sin(a)]))
ax.add_patch(Polygon(rounded(pts, 0.08), closed=True, facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=1.1, zorder=3))
ax.add_patch(Polygon(rounded([c + (p - c) * 0.45 for p in pts], 0.05), closed=True, facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=0.6, zorder=4))
title(6.4, 0.75, "astrosclereid")
# osteosclereid
c = np.array([10.2, YB])
t = np.linspace(0, 2 * math.pi, 120)
xb = 0.28 * np.cos(t)
yb = 1.3 * np.sin(t)
bulge = 1 + 2.4 * np.exp(-((np.abs(np.sin(t)) - 1) / 0.18) ** 2)
ax.add_patch(Polygon(np.c_[c[0] + xb * bulge, c[1] + yb], closed=True, facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=1.1, zorder=3))
ax.add_patch(Polygon(np.c_[c[0] + 0.35 * xb * bulge, c[1] + 0.85 * yb], closed=True, facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=0.6, zorder=4))
title(10.2, 0.75, "osteosclereid")
# macrosclereids (palisade)
for k in range(5):
    x = 12.3 + k * 0.62
    ax.add_patch(FancyBboxPatch((x, YB - 1.3), 0.56, 2.6, boxstyle="round,pad=0,rounding_size=0.12", facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=1.0, zorder=3))
    ax.add_patch(FancyBboxPatch((x + 0.18, YB - 1.1), 0.2, 1.6, boxstyle="round,pad=0,rounding_size=0.08", facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=0.5, zorder=4))
title(13.8, 0.75, "macrosclereids")
# fibre, longitudinal
y = YB
x0, x1 = 16.8, 22.6
xs = np.linspace(x0, x1, 120)
half = 0.33 * np.clip(np.sin(np.pi * (xs - x0) / (x1 - x0)), 0, 1) ** 0.6
ax.add_patch(Polygon(np.r_[np.c_[xs, y + half], np.c_[xs[::-1], (y - half)[::-1]]], closed=True, facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=1.0, zorder=3))
ax.add_patch(Polygon(np.r_[np.c_[xs[10:-10], y + 0.25 * half[10:-10]], np.c_[xs[10:-10][::-1], (y - 0.25 * half[10:-10])[::-1]]], closed=True,
                     facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=0.4, zorder=4))
for xx in np.linspace(17.6, 21.8, 8):
    ax.plot([xx - 0.08, xx + 0.08], [y + 0.18, y + 0.3], color=P.edge(SW), lw=0.9, zorder=5)
title(19.7, 0.75, "fibre (longitudinal)")
bio.callout(ax, (19.8, y + 0.26), (20.6, 5.0), "Slit-like pits", size="tiny")
# fibre bundle in section
for c in hexgrid(23.6, YB - 1.0, 4, 3, 0.62):
    cen = c.mean(axis=0)
    ax.add_patch(Polygon(rounded(c, 0.1), closed=True, facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=1.0, zorder=3))
    ax.add_patch(Circle(cen, 0.12, facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=0.5, zorder=4))
title(25.4, 0.75, "fibre bundle (section)")
bio.callout(ax, (25.43, YB + 0.86), (27.5, 5.0), "Narrow lumen", size="tiny")
