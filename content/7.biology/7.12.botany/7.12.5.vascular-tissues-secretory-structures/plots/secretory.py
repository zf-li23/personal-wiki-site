"""Secretory structures (schematic). External: A, a glandular hair with a stalk and a multicellular
secretory head; the secretion collects under the cuticle, which lifts off as a blister. B, a hydathode at
a leaf margin: a vein ending of tracheids, a loose epithem and a water pore (a permanently open stoma)
through which guttation water is released. Internal: C, a lysigenous secretory cavity of a citrus peel:
secretory cells break down and their oil fills the cavity, lined by partly lysed cells. D, a schizogenous
resin duct of a pine: the middle lamellae between cells separate and a ring of living epithelial cells
secretes resin into the canal. E, laticifers: a non-articulated laticifer is a single, branching,
multinucleate cell that grows with the plant (Euphorbia, Nerium); an articulated laticifer is a file of
cells whose end walls dissolve (Hevea, Papaver, Lactuca).
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 11.0)
WALL = "cell_wall"
SEC = "lipid"


def cell(c, w, h, tk="cytoplasm", r=0.12, lw=0.9, z=3):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                facecolor=P.fill(tk), edgecolor=P.edge(WALL), lw=lw, zorder=z))


def title(x, y, t):
    bio.label(ax, (x, y), t, size="small")


# --- A glandular hair
bio.panel(ax, "A", (0.1, 10.9))
title(3.2, 10.4, "Glandular hair")
for k in range(6):
    cell((0.7 + k * 1.0, 2.2), 0.98, 0.9, tk="cytoplasm")
ax.plot([0.2, 6.2], [2.68, 2.68], color=P.edge(SEC), lw=1.6, zorder=4)
for k, y in enumerate((3.15, 3.75, 4.35)):
    cell((3.2, y), 0.55, 0.58, tk="cytoplasm")
head = (3.2, 5.6)
ax.add_patch(Ellipse(head, 2.6, 1.9, facecolor=P.fill(SEC), edgecolor=P.edge(SEC), lw=1.3, zorder=3))
for dx, dy in ((-0.55, -0.35), (0.0, -0.4), (0.55, -0.35), (-0.3, 0.1), (0.3, 0.1)):
    cell((head[0] + dx, head[1] + dy), 0.52, 0.48, tk="metabolite", r=0.15, z=4)
bio.callout(ax, (head[0] + 1.0, head[1] + 0.5), (5.6, 8.2), "Secretion under the cuticle", size="tiny")
bio.callout(ax, (head[0] - 0.3, head[1] - 0.3), (0.6, 7.6), "Secretory head cells", size="tiny")
bio.callout(ax, (3.2, 3.75), (0.6, 4.4), "Stalk", size="tiny")
bio.callout(ax, (5.2, 2.2), (5.6, 0.7), "Epidermis", size="tiny")

# --- B hydathode
bio.panel(ax, "B", (7.1, 10.9))
title(10.0, 10.4, "Hydathode")
leaf = [(7.6, 1.0), (12.6, 1.0), (12.6, 4.8), (11.4, 7.6), (10.2, 8.3), (8.8, 7.6), (7.6, 4.8)]
ax.add_patch(Polygon(leaf, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=2))
# vein of tracheids
ax.add_patch(Polygon([(9.9, 1.0), (10.5, 1.0), (10.45, 5.0), (9.95, 5.0)], closed=True, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=1.0, zorder=3))
for y in np.arange(1.3, 4.9, 0.4):
    ax.plot([9.95, 10.45], [y, y + 0.2], color=P.edge("xylem"), lw=0.6, zorder=4)
# epithem: loose cells
rng = np.random.default_rng(1)
for k in range(16):
    a = rng.uniform(0, math.pi)
    r = rng.uniform(0.3, 1.4)
    ax.add_patch(Circle((10.2 + r * math.cos(a) * 1.1, 5.4 + r * math.sin(a) * 0.95), 0.28, facecolor=P.light("cytoplasm"), edgecolor=P.edge(WALL), lw=0.7, zorder=4))
# water pore at the tip
for s in (-1, 1):
    ax.add_patch(Ellipse((10.2 + s * 0.22, 8.1), 0.36, 0.6, facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=0.8, zorder=6))
for k in range(3):
    ax.add_patch(Circle((10.2 + 0.15 * (k - 1), 8.75 + 0.35 * k), 0.12 + 0.03 * k, facecolor=P.fill("extracellular"), edgecolor=P.edge("dna"), lw=0.8, zorder=6))
bio.callout(ax, (10.4, 8.1), (12.8, 9.4), "Water pore", size="tiny")
bio.callout(ax, (10.9, 6.0), (13.0, 6.6), "Epithem", size="tiny")
bio.callout(ax, (10.45, 3.0), (13.0, 3.2), "Vein ending (tracheids)", size="tiny")
bio.label(ax, (9.0, 9.8), "guttation droplet", size="tiny", color=P.muted())

# --- C lysigenous cavity
bio.panel(ax, "C", (15.1, 10.9))
title(17.6, 10.4, "Lysigenous cavity")
c = np.array([17.6, 5.4])
for k in range(16):
    a = 2 * math.pi * k / 16
    cell(c + 2.5 * np.array([math.cos(a), math.sin(a)]), 0.75, 0.75, tk="cytoplasm", r=0.2)
ax.add_patch(Circle(c, 1.95, facecolor=P.fill(SEC), edgecolor=P.edge(SEC), lw=1.2, zorder=4))
for k in range(9):
    a = 2 * math.pi * k / 9
    p = c + 1.7 * np.array([math.cos(a), math.sin(a)])
    ax.add_patch(Polygon([p + 0.32 * np.array([math.cos(a + d), math.sin(a + d)]) for d in (-2.0, -1.0, 0.0, 1.0, 2.0)],
                         closed=False, fill=False, edgecolor=P.edge(WALL), lw=0.8, zorder=5))
bio.callout(ax, c, (20.6, 8.6), "Essential oil", size="tiny")
bio.callout(ax, c + np.array([1.2, -1.2]), (19.6, 1.3), "Remnants of lysed cells", size="tiny")

# --- D schizogenous resin duct
bio.panel(ax, "D", (21.4, 10.9))
title(23.9, 10.4, "Schizogenous resin duct")
c = np.array([23.9, 5.4])
for k in range(8):
    a = 2 * math.pi * k / 8 + 0.2
    p = c + 1.05 * np.array([math.cos(a), math.sin(a)])
    ax.add_patch(Polygon([c + 0.55 * np.array([math.cos(a - 0.39), math.sin(a - 0.39)]), c + 0.55 * np.array([math.cos(a + 0.39), math.sin(a + 0.39)]),
                          c + 1.5 * np.array([math.cos(a + 0.39), math.sin(a + 0.39)]), c + 1.5 * np.array([math.cos(a - 0.39), math.sin(a - 0.39)])],
                         closed=True, facecolor=P.fill("metabolite"), edgecolor=P.edge(WALL), lw=0.9, zorder=4))
    ax.add_patch(Circle(p, 0.13, facecolor=P.edge("nucleus"), edgecolor="none", zorder=5))
for k in range(12):
    a = 2 * math.pi * k / 12
    cell(c + 2.15 * np.array([math.cos(a), math.sin(a)]), 0.95, 0.95, tk="cytoplasm", r=0.25)
ax.add_patch(Circle(c, 0.53, facecolor=P.fill(SEC), edgecolor=P.edge(SEC), lw=1.0, zorder=5))
bio.callout(ax, c, (25.6, 1.3), "Resin canal", size="tiny")
bio.callout(ax, c + np.array([1.05, 0.25]), (26.6, 8.6), "Epithelial cells", size="tiny")

# --- E laticifers
bio.panel(ax, "E", (27.1, 10.9))
title(28.6, 10.4, "Laticifers")
t = np.linspace(0, 1, 80)
main = np.c_[27.8 + 0.15 * np.sin(t * 6), 1.2 + 7.6 * t]
ax.plot(main[:, 0], main[:, 1], color=P.edge("lipid_tail"), lw=6.5, solid_capstyle="round", zorder=4)
ax.plot(main[:, 0], main[:, 1], color=P.fill("lipid_tail"), lw=4.8, solid_capstyle="round", zorder=4.1)
for y0, s in ((3.0, 1), (5.2, -1), (6.8, 1)):
    br = np.c_[27.8 + s * 0.9 * t[:40] ** 0.7, y0 + 1.2 * t[:40]]
    ax.plot(br[:, 0], br[:, 1], color=P.edge("lipid_tail"), lw=5.0, solid_capstyle="round", zorder=4)
    ax.plot(br[:, 0], br[:, 1], color=P.fill("lipid_tail"), lw=3.4, solid_capstyle="round", zorder=4.1)
for y in (2.0, 4.0, 6.0, 8.0):
    ax.add_patch(Circle((27.8 + 0.15 * math.sin((y - 1.2) / 7.6 * 6), y), 0.07, facecolor=P.edge("nucleus"), edgecolor="none", zorder=5))
x = 29.4
for k in range(6):
    y = 1.3 + k * 1.25
    cell((x, y + 0.55), 0.5, 1.15, tk="lipid_tail", r=0.15)
    if k:
        ax.plot([x - 0.25, x - 0.12], [y - 0.05, y - 0.05], color=P.edge(WALL), lw=1.0, zorder=5)
        ax.plot([x + 0.12, x + 0.25], [y - 0.05, y - 0.05], color=P.edge(WALL), lw=1.0, zorder=5)
bio.label(ax, (27.8, 0.6), "non-articulated", size="tiny", color=P.muted())
bio.label(ax, (29.4, 0.2), "articulated", size="tiny", color=P.muted())
