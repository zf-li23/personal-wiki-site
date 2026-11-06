# Crassulaceae: succulent leaf and the anatomical basis of CAM (schematic). A: cross-section of a
# succulent leaf: epidermis with a thick cuticle and few sunken stomata; mesophyll of large water-storing
# parenchyma cells with peripheral chloroplasts and a large central vacuole; small vascular bundles.
# B: day-night course of stomatal opening and vacuolar malate in a CAM plant (qualitative). C: plantlets
# with roots formed in the marginal notches of a Kalanchoe leaf.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle

P = bio.P
fig, ax = bio.canvas(36, 13)

# A: leaf cross-section
bio.panel(ax, "A", (0.3, 12.8))
cx, cy, a, b = 7.0, 6.4, 6.0, 4.0
t = np.linspace(0, 2 * math.pi, 200)
ax.add_patch(Polygon(np.c_[cx + (a + 0.25) * np.cos(t), cy + (b + 0.25) * np.sin(t)], closed=True,
                     facecolor=P.light("plant"), edgecolor=P.edge("plant"), lw=2.4, zorder=3))
ax.add_patch(Polygon(np.c_[cx + a * np.cos(t), cy + b * np.sin(t)], closed=True, facecolor=P.fill("vacuole"),
                     edgecolor=P.edge("plant"), lw=0.8, zorder=4))
rng = np.random.default_rng(0)
for x in np.arange(cx - a + 0.9, cx + a, 1.35):
    for y in np.arange(cy - b + 0.9, cy + b, 1.35):
        if ((x - cx) / (a - 0.5)) ** 2 + ((y - cy) / (b - 0.5)) ** 2 < 1:
            ax.add_patch(Circle((x, y), 0.62, facecolor=P.light("vacuole"), edgecolor=P.edge("plant"), lw=0.6,
                                zorder=5))
            for k in range(5):
                th = rng.uniform(0, 2 * math.pi)
                ax.add_patch(Ellipse((x + 0.5 * math.cos(th), y + 0.5 * math.sin(th)), 0.18, 0.1,
                                     angle=math.degrees(th), facecolor=P.fill("chloroplast"), edgecolor="none",
                                     zorder=6))
for x in (cx - 2.2, cx, cx + 2.2):
    ax.add_patch(Circle((x, cy - 0.2), 0.38, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.8, zorder=7))
for ang in (115, 250, 300):
    th = math.radians(ang)
    p = np.array([cx + a * math.cos(th), cy + b * math.sin(th)])
    ax.add_patch(Ellipse(p * 0.97 + np.array([cx, cy]) * 0.03, 0.55, 0.3, angle=ang, facecolor=P.fill("chloroplast"),
                         edgecolor=P.edge("plant"), lw=0.8, zorder=8))
th = math.radians(250)
bio.callout(ax, (cx + a * math.cos(th), cy + b * math.sin(th)), (2.0, 0.9), "Sunken stoma", size="small")
bio.callout(ax, (cx + 0.2, cy + b + 0.2), (cx + 3.5, 12.2), "Thick cuticle, epidermis", size="small")
bio.callout(ax, (cx - 1.35, cy + 1.3), (1.0, 12.0), "Water-storing cell (large vacuole)", size="small")
bio.callout(ax, (cx + 2.2, cy - 0.2), (13.4, 3.0), "Vascular bundle", size="small")

# B: day-night chart
bio.panel(ax, "B", (14.6, 12.8))
x0, y0, W, H = 16.0, 2.6, 9.0, 7.6
for k, (s, e) in enumerate([(0, 0.25), (0.75, 1.0)]):
    ax.add_patch(Rectangle((x0 + s * W, y0), (e - s) * W, H, facecolor=P.light("neutral"), edgecolor="none", zorder=2))
ax.plot([x0, x0 + W], [y0, y0], color=P.ink(), lw=1.0)
ax.plot([x0, x0], [y0, y0 + H], color=P.ink(), lw=1.0)
h = np.linspace(0, 1, 200)
stoma = 0.15 + 0.75 * (np.cos(2 * math.pi * h) + 1) / 2 * ((h < 0.3) | (h > 0.72))
malate = 0.5 + 0.38 * np.cos(2 * math.pi * (h - 0.25))
ax.plot(x0 + h * W, y0 + stoma * H * 0.9, color=P.edge("dna"), lw=2.2)
ax.plot(x0 + h * W, y0 + malate * H * 0.9, color=P.edge("rna"), lw=2.2, ls=(0, (5, 2)))
for f, txt in [(0.12, "Night"), (0.5, "Day"), (0.88, "Night")]:
    bio.label(ax, (x0 + f * W, y0 + H + 0.4), txt, size="small")
bio.label(ax, (x0 + W / 2, y0 - 0.6), "Time (24 h, midnight at both ends)", size="small")
bio.label(ax, (x0 + 0.62 * W, y0 + 0.93 * H), "Stomata open (night)", size="small", ha="left", color=P.edge("dna"))
bio.label(ax, (x0 + 0.4 * W, y0 + 0.2 * H), "Vacuolar malate", size="small", ha="left", color=P.edge("rna"))

# C: Kalanchoe leaf with plantlets
bio.panel(ax, "C", (26.4, 12.8))
lx, ly = 31.0, 6.4
L, Wd = 4.6, 2.4
pts = []
nn = 6
for i in range(0, 101):
    s = i / 100
    w = Wd * math.sin(math.pi * s) ** 0.8
    notch = 0.25 * abs(math.sin(nn * math.pi * s))
    pts.append((lx - w + notch, ly - L + 2 * L * s))
leaf = pts + [(2 * lx - x, y) for x, y in pts[::-1]]
ax.add_patch(Polygon(leaf, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=4))
ax.plot([lx, lx], [ly - L - 1.0, ly + L], color=P.edge("plant"), lw=1.2, zorder=5)
for i in range(1, nn):
    s = i / nn
    w = Wd * math.sin(math.pi * s) ** 0.8
    for side in (-1, 1):
        px, py = lx + side * w, ly - L + 2 * L * s
        for dx in (-0.25, 0.25):
            ax.add_patch(Ellipse((px + side * 0.45 + dx, py + 0.35), 0.4, 0.22, angle=side * 40,
                                 facecolor=P.light("plant"), edgecolor=P.edge("plant"), lw=0.7, zorder=6))
        for dx in (-0.15, 0.1):
            ax.plot([px + side * 0.45, px + side * 0.45 + dx], [py + 0.25, py - 0.35], color=P.muted(), lw=0.6, zorder=6)
bio.callout(ax, (lx + Wd * 0.95 + 0.45, ly + 0.9), (lx + 1.5, 12.0), "Plantlet with roots", size="small")
bio.label(ax, (lx, 0.6), r"$\it{Kalanchoe\ pinnata}$", size="small")
