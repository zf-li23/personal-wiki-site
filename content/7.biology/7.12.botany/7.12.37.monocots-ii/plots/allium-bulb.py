# Allium (Amaryllidaceae: Allioideae), schematic. A: onion bulb in longitudinal section: a flat basal
# plate (the stem) bearing adventitious roots, concentric fleshy scale leaves (bases of foliage leaves)
# around the apical bud, and dry outer tunic scales. B: garlic bulb in transverse section: several
# cloves (axillary bulblets, each with its own bud) inside a common papery tunic, around the remains of
# the scape. C: umbel on a leafless scape, enclosed in bud by a membranous spathe; in garlic the umbel
# bears bulbils among sterile flowers.
import numpy as np
from matplotlib.patches import PathPatch, Ellipse, Circle
from matplotlib.path import Path
import wikibio as bio
from wikibio import botany
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(30, 13)


def onion(cx, cy, w, h, neck):
    t = np.linspace(0, 1, 60)
    right = [(cx + w * np.sin(np.pi * s) ** 0.9 * (1 - 0.35 * s) + neck * s, cy + h * s) for s in t]
    left = [(cx - x + cx, y) for x, y in right[::-1]]
    return np.array(right + left)


# ---- A
bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (5.2, 12.6), "Onion bulb (section)", size="title")
cx, cy = 5.2, 3.2
for k, (w, tok) in enumerate([(3.6, "neutral"), (3.3, "neutral"), (3.0, "plant"), (2.5, "plant"), (2.0, "plant"),
                               (1.5, "plant"), (1.0, "plant")]):
    pts = onion(cx, cy, w, 7.5 - k * 0.55, 0.25)
    light = tok == "plant"
    ax.add_patch(PathPatch(Path(pts, closed=True), facecolor=P.light("plant") if light else P.light("neutral"),
                           edgecolor=P.edge(tok), lw=1.1, zorder=3 + k))
ax.add_patch(Ellipse((cx, cy + 1.4), 0.5, 1.6, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=12))
ax.add_patch(PathPatch(Path(smooth_closed([(cx - 1.6, cy + 0.2), (cx, cy + 0.55), (cx + 1.6, cy + 0.2), (cx + 1.3, cy - 0.35),
                                           (cx - 1.3, cy - 0.35)], n=80), closed=True),
                       facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=1.2, zorder=13))
for k, x in enumerate(np.linspace(cx - 1.2, cx + 1.2, 7)):
    ax.plot([x, x + 0.3 * np.sin(k), x + 0.15 * np.sin(2 * k)], [cy - 0.3, cy - 1.4, cy - 2.4], color=P.edge("neutral"),
            lw=0.9, zorder=2)
bio.callout(ax, (cx + 2.9, cy + 3.2), (9.6, 7.8), "Dry tunic")
bio.callout(ax, (cx + 2.0, cy + 2.4), (9.6, 6.6), "Fleshy scale leaves")
bio.callout(ax, (cx, cy + 1.9), (9.6, 9.6), "Apical bud")
bio.callout(ax, (cx + 1.0, cy), (9.6, 2.0), "Basal plate (stem)")
bio.callout(ax, (cx - 1.0, cy - 1.6), (0.8, 0.6), "Adventitious roots")

# ---- B
bio.panel(ax, "B", (11.2, 12.7))
bio.label(ax, (15.4, 12.6), "Garlic bulb (cross-section)", size="title")
bc = np.array([15.4, 6.6])
ax.add_patch(Circle(bc, 3.3, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=1.3, zorder=3))
n = 8
for k in range(n):
    a = 2 * np.pi * k / n
    u = np.array([np.cos(a), np.sin(a)])
    v = np.array([-u[1], u[0]])
    loc = [(0.55, 0.0), (1.6, 0.85), (2.95, 0.55), (3.05, 0.0), (2.95, -0.55), (1.6, -0.85)]
    pts = [bc + u * r + v * s * 0.95 for r, s in loc]
    ax.add_patch(PathPatch(Path(smooth_closed(pts, n=80), closed=True), facecolor=P.fill("tepal"),
                           edgecolor=P.edge("tepal"), lw=1.0, zorder=4))
    ax.add_patch(Circle(bc + u * 1.7, 0.16, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.8, zorder=5))
ax.add_patch(Circle(bc, 0.4, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=5))
bio.callout(ax, bc + [0, 0.35], (19.4, 11.0), "Scape remains")
bio.callout(ax, bc + [2.2, 0.4], (19.6, 9.4), "Clove (bulblet)")
bio.callout(ax, bc + [1.7 * np.cos(np.pi / 4), 1.7 * np.sin(np.pi / 4)], (19.8, 8.2), "Bud of clove")
bio.callout(ax, bc + [0, -3.3], (19.4, 2.6), "Common tunic")

# ---- C
bio.panel(ax, "C", (21.6, 12.7))
bio.label(ax, (25.6, 12.6), "Umbel and spathe", size="title")
a = botany.inflorescence(ax, (25.2, 0.6), 10.0, kind="umbel", flowers=9, bracts=False)
top = np.array([25.2, 9.4])
for s in (-1, 1):
    pts = [top + [0, -0.2], top + [s * 1.2, -0.6], top + [s * 1.9, -1.6], top + [s * 0.4, -0.9]]
    ax.add_patch(PathPatch(Path(smooth_closed(pts, n=60), closed=True), facecolor=P.light("neutral"),
                           edgecolor=P.edge("neutral"), lw=1.0, zorder=3))
bio.callout(ax, top + [1.5, -1.3], (27.6, 11.4), "Spathe (split)")
bio.callout(ax, (25.2, 4.0), (28.0, 3.4), "Leafless scape")
