"""Four kinds of underground stem (schematic). A: rhizome with nodes, scale leaves, adventitious roots and
an aerial shoot; B: potato tuber with helically arranged eyes, partly cut to show the skin (periderm)
and storage flesh; C: onion bulb in longitudinal section (wikibio.plantmorph); D: corm (water chestnut
type) with ring-like nodes, membranous scale leaves and a stout apical bud.
"""

import numpy as np
from matplotlib.patches import Ellipse, Polygon

import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(30.0, 9.6)
SOIL = 7.2


def soil(x0, x1):
    ax.plot([x0, x1], [SOIL, SOIL], color=P.muted(), lw=1.0, ls=(0, (4, 3)), zorder=2)


for k, (x, t) in enumerate([(0.4, "Rhizome"), (8.4, "Tuber (potato)"), (16.4, "Bulb (onion)"), (23.4, "Corm")]):
    bio.panel(ax, "ABCD"[k], (x - 0.2, 9.4))
    bio.label(ax, (x + 0.45, 9.37), t, size="title", ha="left", va="top")

# A rhizome
soil(0.3, 7.6)
r = PM.rhizome(ax, (0.8, 4.2), 6.4, nodes=5)
bio.callout(ax, r["node"], (1.2, 6.6), "Node", size="small")
bio.callout(ax, r["scale_leaf"], (3.4, 6.6), "Scale leaf", size="small")
bio.callout(ax, r["roots"], (2.5, 1.2), "Adventitious roots", size="small")
bio.callout(ax, r["shoot"], (7.2, 8.4), "Aerial shoot", size="small")

# B tuber
soil(8.3, 15.6)
bio.icon(ax, "wikimedia/potato-tuber", at=(12.0, 4.4), height=2.9)
bio.callout(ax, bio.icon_part("wikimedia/potato-tuber", "eye", at=(12.0, 4.4), height=2.9), (13.6, 1.0), "Eye (node, bud)", size="small")
bio.callout(ax, bio.icon_part("wikimedia/potato-tuber", "skin", at=(12.0, 4.4), height=2.9), (12.8, 6.6), "Skin (periderm)", size="small")
bio.callout(ax, bio.icon_part("wikimedia/potato-tuber", "flesh", at=(12.0, 4.4), height=2.9), (9.0, 1.3), "Storage parenchyma", size="small")

# C bulb
soil(16.3, 22.6)
b = PM.bulb(ax, (19.5, 2.3), 5.6)
bio.callout(ax, b["tunic"], (17.0, 7.9), "Dry outer scales", size="small")
bio.callout(ax, b["scale"], (21.8, 4.9), "Fleshy scales", size="small")
bio.callout(ax, b["bud"], (22.0, 7.9), "Apical bud", size="small")
bio.callout(ax, b["basal_plate"], (22.0, 1.6), "Basal plate (stem)", size="small")
bio.callout(ax, b["roots"], (22.0, 0.6), "Roots", size="small")

# D corm
soil(23.3, 29.8)
cx, cy, w, h = 26.4, 3.8, 2.4, 1.6
ax.add_patch(Ellipse((cx, cy), 2 * w, 2 * h, facecolor=P.fill("atp"),
                     edgecolor=P.edge("atp"), lw=1.2, zorder=5))
for f in (-0.55, 0.0, 0.55):
    t = np.linspace(-0.98, 0.98, 60)
    xs = cx + w * t
    ys = cy + h * f + 0.25 * h * np.sqrt(1 - t ** 2) * (1 if f <= 0 else 0.6)
    keep = ((xs - cx) / w) ** 2 + ((ys - cy) / h) ** 2 < 0.97
    ax.plot(xs[keep], ys[keep], color=P.edge("atp"), lw=1.0, zorder=6)
    # membranous scale leaf fringe on each node
    ax.plot(xs[keep][::6], ys[keep][::6] + 0.08, ls="none", marker=(3, 0, 0), ms=4, color=P.edge("animal"), zorder=6.5)
bud = np.array([(cx - 0.35, cy + h - 0.1), (cx, cy + h + 1.5), (cx + 0.35, cy + h - 0.1)])
ax.add_patch(Polygon(bud, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=7))
for dx in (-0.8, 0.8):
    sb = np.array([(cx + dx - 0.2, cy + h - 0.35), (cx + dx * 1.15, cy + h + 0.6), (cx + dx + 0.2, cy + h - 0.35)])
    ax.add_patch(Polygon(sb, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.8, zorder=6.8))
ax.plot([cx - w - 1.4, cx - w + 0.1], [cy - 0.2, cy], color=P.edge("animal"), lw=2.0, zorder=4)
bio.label(ax, (cx - w - 0.9, cy + 0.15), "stolon", size="tiny", color=P.muted())
bio.callout(ax, (cx, cy + h + 1.2), (28.3, 8.4), "Apical bud", size="small")
bio.callout(ax, (cx + 0.8, cy + h + 0.4), (29.0, 6.6), "Lateral bud", size="small")
bio.callout(ax, (cx + w * 0.7, cy + 0.35), (28.6, 1.6), "Node (ring)", size="small")
bio.callout(ax, (cx - w * 0.5, cy - h * 0.55 + 0.1), (24.0, 0.8), "Scale leaf", size="small")
