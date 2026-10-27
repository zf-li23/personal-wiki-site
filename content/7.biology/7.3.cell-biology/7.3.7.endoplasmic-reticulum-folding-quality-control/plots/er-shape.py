# The shape of the ER. A: top view of an ER network in a spread animal cell: sheets (with fenestrations)
# near the nucleus, continuous with the nuclear envelope, and a peripheral network of tubules joined at
# three-way junctions. B: a sheet in cross-section: two flat membranes about 50 nm apart, held by
# luminal spacers (Climp-63), with highly curved rims. C: a tubule in cross-section (diameter 30-100 nm):
# reticulons and REEPs (DP1/Yop1) insert wedge-shaped hairpins into the cytosolic leaflet and stabilize the
# curvature of tubules and sheet rims. D: atlastin, a dynamin-related GTPase, tethers two tubules by GTP-
# dependent dimerization and fuses them into a three-way junction.
import math

import numpy as np
import wikibio as bio
from wikibio import traffic as T

fig, ax = bio.canvas(22, 10)
P = bio.P

# ---- A: network ------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 9.9))
cx, cy = 5.0, 4.8
cellout = bio.blob((cx, cy), 4.6, 4.2, wobble=0.05, seed=4, k=10)
bio.membrane(ax, cellout, inside="cytoplasm", thickness=0.1)
rng = np.random.default_rng(3)
# honeycomb lattice: every vertex has three neighbours
a = 0.75
pts, edges = {}, []
for i in range(-8, 9):
    for j in range(-8, 9):
        for s in (0, 1):
            x = a * math.sqrt(3) * (i + 0.5 * j)
            y = a * 1.5 * j + (a if s else 0)
            pts[(i, j, s)] = np.array([x, y]) + rng.normal(0, 0.12, 2) + (cx, cy)
for (i, j, s), p in pts.items():
    if s == 0:
        for q in ((i, j, 1), (i, j - 1, 1), (i + 1, j - 1, 1)):
            if q in pts:
                edges.append(((i, j, s), q))
from matplotlib.path import Path
inside = Path(cellout * 0.96 + (1 - 0.96) * np.array([cx, cy]))
for e in edges:
    p, q = pts[e[0]], pts[e[1]]
    if inside.contains_point(p) and inside.contains_point(q) and np.hypot(*(p - q)) < 1.4:
        mid = (p + q) / 2 + rng.normal(0, 0.08, 2)
        t = np.linspace(0, 1, 20)[:, None]
        curve = (1 - t) ** 2 * p + 2 * (1 - t) * t * mid + t ** 2 * q
        ax.plot(curve[:, 0], curve[:, 1], color=P.edge("er"), lw=3.0, zorder=4, solid_capstyle="round")
        ax.plot(curve[:, 0], curve[:, 1], color=P.fill("er"), lw=1.6, zorder=4.1, solid_capstyle="round")
nx, ny = cx - 0.6, cy + 0.2
sheet = bio.blob((nx, ny), 2.4, 2.1, wobble=0.12, seed=8, k=11)
ax.add_patch(bio.core.PathPatch(Path(sheet, closed=True), facecolor=P.fill("er"), edgecolor=P.edge("er"), lw=1.2, zorder=5))
for k in range(9):
    th = k * 2 * math.pi / 9 + 0.3
    rr = 1.8 + 0.15 * (k % 2)
    ax.add_patch(bio.core.Circle((nx + rr * math.cos(th), ny + 0.88 * rr * math.sin(th)), 0.09, facecolor=P.fill("cytoplasm"),
                                 edgecolor=P.edge("er"), lw=0.7, zorder=5.5))
bio.nucleus(ax, (nx, ny), 1.3, pores=0, nucleolus=True, chromatin=False)
bio.callout(ax, (nx + 1.6, ny + 1.25), (7.2, 9.4), "Sheets (rough ER)")
bio.callout(ax, (8.6, 3.1), (9.6, 1.0), "Tubules, three-way junctions")
bio.callout(ax, (nx - 1.25, ny - 0.3), (0.7, 1.0), "Nuclear envelope")

# ---- B: sheet cross-section -------------------------------------------------------------------------
bio.panel(ax, "B", (10.6, 9.9))
y0, half, L = 7.6, 0.45, 4.2
x0 = 12.0
t = np.linspace(-math.pi / 2, math.pi / 2, 30)
right = np.c_[x0 + L + half * np.cos(t), y0 + half * np.sin(t)]
left = np.c_[x0 - half * np.cos(t), y0 - half * np.sin(t)]
outline = np.vstack([np.c_[np.linspace(x0, x0 + L, 30), np.full(30, y0 - half)], right,
                     np.c_[np.linspace(x0 + L, x0, 30), np.full(30, y0 + half)], left])
ax.add_patch(bio.core.Polygon(outline, closed=True, facecolor=P.fill("er"), edgecolor="none", zorder=3))
T.band(ax, np.vstack([outline, outline[:1]]), zorder=4)
for xx in np.linspace(x0 + 0.5, x0 + L - 0.5, 5):
    ax.plot([xx, xx], [y0 - half + 0.1, y0 + half - 0.1], color=P.edge("protein"), lw=2.2, zorder=6)
for side in (-1, 1):
    xr = x0 + L / 2 + side * (L / 2 + half)
    for dy in (-0.25, 0.0, 0.25):
        ax.add_patch(bio.core.Polygon([(xr + side * 0.09, y0 + dy - 0.07), (xr + side * 0.09, y0 + dy + 0.07),
                                       (xr - side * 0.03, y0 + dy)], closed=True, facecolor=P.edge("receptor"),
                                      edgecolor="none", zorder=7))
bio.label(ax, (x0 + L / 2, y0 + 1.05), "Sheet: spacers (Climp-63) set the ~50 nm lumen", size="small")
bio.callout(ax, (x0 + L + half + 0.05, y0 - 0.2), (x0 + L + 1.3, y0 - 0.9), "Curved rim:\nreticulons", size="tiny")

# ---- C: tubule cross-section --------------------------------------------------------------------------
bio.panel(ax, "C", (10.6, 5.6))
tc = np.array([12.6, 3.0])
r = 0.75
ax.add_patch(bio.core.Circle(tc, r - 0.08, facecolor=P.fill("er"), edgecolor="none", zorder=3))
ring = np.c_[tc[0] + r * np.cos(np.linspace(0, 2 * np.pi, 200)), tc[1] + r * np.sin(np.linspace(0, 2 * np.pi, 200))]
T.band(ax, ring, zorder=4)
for k in range(7):
    th = 2 * math.pi * k / 7
    d = np.array([math.cos(th), math.sin(th)])
    n = np.array([-d[1], d[0]])
    base = tc + d * (r + 0.09)
    ax.add_patch(bio.core.Polygon([base + n * 0.09, base - n * 0.09, tc + d * (r - 0.01)], closed=True,
                                  facecolor=P.edge("receptor"), edgecolor="none", zorder=7))
bio.label(ax, (tc[0], tc[1] - 1.35), "Tubule: wedge-shaped hairpins\nin the cytosolic leaflet", size="tiny")
bio.label(ax, (tc[0], tc[1]), "lumen", size="tiny", color=P.muted())

# ---- D: atlastin fusion -----------------------------------------------------------------------------------
bio.panel(ax, "D", (15.4, 5.6))


def tube(*paths):
    for z, c, w in ((4, P.edge("er"), 9), (4.1, P.fill("er"), 6.5)):
        for pts in paths:
            pts = np.asarray(pts, float)
            ax.plot(pts[:, 0], pts[:, 1], color=c, lw=w, zorder=z, solid_capstyle="round", solid_joinstyle="round")


tube([(15.9, 3.0), (17.9, 3.0)])
tube([(18.4, 0.9), (18.4, 2.4)])
bio.protein(ax, (18.15, 3.0), 0.38, 0.3, "drug")
bio.protein(ax, (18.4, 2.68), 0.38, 0.3, "drug")
bio.label(ax, (17.4, 3.7), "atlastin dimer (GTP)", size="tiny")
bio.label(ax, (17.2, 0.6), "tubule tip meets tubule", size="tiny")
bio.arrow(ax, (19.0, 2.2), (19.7, 2.2), kind="process")
bio.label(ax, (19.35, 2.55), "GTP\nhydrolysis", size="tiny")
tube([(19.9, 3.0), (21.0, 2.4), (21.7, 3.4)], [(21.0, 2.4), (21.0, 0.9)])
bio.label(ax, (21.0, 0.5), "three-way junction", size="tiny")
