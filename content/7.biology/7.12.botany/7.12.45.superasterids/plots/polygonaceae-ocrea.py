# Polygonaceae. A: a stem of Persicaria with swollen nodes and membranous ocreae (fused stipules
# sheathing the node, ciliate rim), alternate leaves. B: Fagopyrum flower in section (five tepals,
# eight stamens, three fused carpels, one basal orthotropous ovule) and the trigonous achene.
# C: Rumex fruit: three small outer tepals and three inner tepals enlarged into wings, each with a
# tubercle, around the achene. D: Fallopia (He Shou Wu) fruit with winged outer tepals.
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(34, 13)

# A: stem with ocreae
bio.panel(ax, "A", (0.3, 12.8))
x = 4.0
pts = [(x - 0.22, 0.5), (x + 0.22, 0.5), (x + 0.2, 12.0), (x - 0.2, 12.0)]
bio.shape(ax, pts, token="plant", lw=0.9, zorder=3)
for i, y in enumerate((3.0, 6.6, 10.2)):
    s = 1 if i % 2 == 0 else -1
    ax.add_patch(Ellipse((x, y), 0.62, 0.4, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.9, zorder=4))
    # ocrea: translucent sheath above the node
    bio.shape(ax, [(x - 0.42, y), (x + 0.42, y), (x + 0.48, y + 1.3), (x - 0.48, y + 1.3)], token="neutral", lw=0.8, zorder=5)
    for k in range(7):
        xx = x - 0.45 + 0.15 * k
        ax.plot([xx, xx + 0.03], [y + 1.3, y + 1.6], color=P.edge("neutral"), lw=0.6, zorder=5)
    # leaf (petiole from below the ocrea)
    t = np.linspace(0, 1, 40)
    base = np.array([x + s * 0.3, y + 0.1])
    L = 3.5
    up = np.c_[base[0] + s * L * t, base[1] + 0.8 * t + 0.75 * np.sin(np.pi * t)]
    lo = np.c_[base[0] + s * L * t[::-1], base[1] + 0.8 * t[::-1] - 0.75 * np.sin(np.pi * t[::-1])]
    bio.shape(ax, np.vstack([up, lo]), token="plant", lw=0.9, zorder=4)
    ax.plot([base[0], base[0] + s * L], [base[1], base[1] + 0.8], color=P.edge("plant"), lw=0.6, zorder=5)
bio.callout(ax, (x + 0.45, 7.3), (7.8, 5.5), "Ocrea")
bio.callout(ax, (x - 0.3, 6.6), (0.6, 5.0), "Swollen node")

# B: Fagopyrum flower and achene
bio.panel(ax, "B", (9.4, 12.8))
cx = 12.4
for s in (-1, 1):
    bio.shape(ax, [(cx + s * 0.3, 4.0), (cx + s * 0.5, 4.0), (cx + s * 2.1, 6.8), (cx + s * 1.6, 7.1)], token="petal", lw=0.9, zorder=5)
    for h in (5.4, 6.0):
        ax.plot([cx + s * 0.45, cx + s * 0.9], [4.1, h], color=P.edge("anther"), lw=0.8, zorder=6)
        ax.add_patch(Ellipse((cx + s * 0.9, h + 0.12), 0.22, 0.3, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.5, zorder=7))
bio.shape(ax, [(cx - 0.45, 4.0), (cx + 0.45, 4.0), (cx + 0.35, 5.3), (cx, 5.6), (cx - 0.35, 5.3)], token="ovary", lw=0.9, zorder=6)
ax.add_patch(Ellipse((cx, 4.6), 0.3, 0.6, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.6, zorder=7))
for d in (-0.25, 0, 0.25):
    ax.plot([cx, cx + d * 2], [5.6, 6.5], color=P.edge("ovary"), lw=0.9, zorder=6)
ax.plot([cx, cx], [2.8, 4.0], color=P.edge("plant"), lw=1.6, zorder=3)
bio.callout(ax, (cx, 4.6), (15.8, 3.0), "Basal ovule")
bio.callout(ax, (cx - 1.4, 6.2), (9.6, 8.6), "Tepal (5)")
bio.callout(ax, (cx + 0.9, 6.1), (15.8, 8.6), "Stamens (8)")
# trigonous achene
c = np.array([12.4, 10.4])
tri = [c + 1.0 * np.array([np.sin(a), np.cos(a)]) for a in np.radians([0, 120, 240])]
ax.add_patch(Polygon(tri, closed=True, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=1.0, zorder=5))
for p in tri:
    ax.plot([c[0], p[0]], [c[1], p[1]], color=P.edge("rna"), lw=0.6, zorder=6)
bio.label(ax, (12.4, 11.9), "trigonous achene", size="small")

# C: Rumex
bio.panel(ax, "C", (18.0, 12.8))
c = np.array([21.6, 6.6])
for k in range(3):
    a = np.radians(90 + 120 * k)
    d = np.array([np.cos(a), np.sin(a)])
    ax.add_patch(Ellipse(c + 1.25 * d, 2.6, 1.6, angle=np.degrees(a), facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.9, zorder=4))
    ax.add_patch(Ellipse(c + 0.9 * d, 0.55, 0.3, angle=np.degrees(a), facecolor=P.edge("rna"), edgecolor=P.edge("rna"), lw=0.5, zorder=5))
tri = [c + 0.55 * np.array([np.sin(a), np.cos(a)]) for a in np.radians([60, 180, 300])]
ax.add_patch(Polygon(tri, closed=True, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.9, zorder=6))
bio.label(ax, (21.6, 11.6), "Rumex", italic=True, size="title")
bio.callout(ax, c + (0.45, 1.9), (25.0, 10.4), "Inner tepal (wing)")
bio.callout(ax, c + (0.0, 0.9), (25.0, 8.6), "Tubercle")
bio.callout(ax, c + (0.0, -0.2), (25.0, 3.4), "Achene")

# D: Fallopia
bio.panel(ax, "D", (26.4, 12.8))
c = np.array([30.4, 6.6])
for s in (-1, 1, 0):
    off = np.array([s * 0.85, 0.0])
    w = 1.0 if s else 0.7
    ax.add_patch(Ellipse(c + off, w, 3.4, facecolor=P.light("plant") if s else P.fill("plant"), edgecolor=P.edge("plant"), lw=0.9, zorder=4 + (s == 0)))
ax.add_patch(Ellipse(c, 0.5, 1.2, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.8, zorder=6))
ax.plot([c[0], c[0]], [c[1] - 2.8, c[1] - 1.7], color=P.edge("plant"), lw=1.3, zorder=3)
bio.label(ax, (30.4, 11.6), "Fallopia", italic=True, size="title")
bio.callout(ax, c + (-0.95, 1.0), (27.0, 9.6), "Winged outer tepal")
bio.callout(ax, c + (0.1, 0.0), (33.6, 4.0), "Achene")
