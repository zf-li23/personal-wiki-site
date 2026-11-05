"""Where the meristems are (schematic). A: a eudicot plant. Apical meristems (red) at the tips of the
shoots, in the axillary buds and at the root tips lengthen the axes and make new leaves and branches;
lateral meristems (orange dashes: vascular cambium and cork cambium) in the older stem and root add
girth. B: a grass culm. Intercalary meristems (red bands) at the base of each internode and of the leaf
sheath keep growing after the shoot apex has turned into the inflorescence; they let the culm elongate
rapidly (jointing and heading of cereals) and let a mown leaf regrow from its base.
"""

import numpy as np
from matplotlib.patches import Ellipse, Polygon, Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 12.6)
AP, LAT = "negative", "atp"

bio.panel(ax, "A", (0.1, 12.5))
bio.icon(ax, "wikimedia/plant-body", at=(4.2, 6.1), height=11, mute="neutral")
off = (0.2, 0.1)


def dot(x, y, r=0.2):
    ax.add_patch(Circle((x + off[0], y + off[1]), r, facecolor=P.fill(AP), edgecolor=P.edge(AP), lw=0.9, zorder=30))


for x, y in ((0.73, 6.0), (7.13, 6.62), (4.04, 9.2), (4.69, 8.8), (3.95, 7.27), (4.55, 7.27), (3.92, 4.9), (4.6, 4.95)):
    dot(x, y, 0.17)
for x, y in ((4.33, 0.82), (0.66, 1.3), (7.42, 1.34)):
    dot(x, y, 0.17)
# lateral meristem along the older stem and the taproot
for xs, y0, y1 in ((4.18 + off[0], 3.4, 6.8), (4.48 + off[0], 3.4, 6.8), (4.18 + off[0], 1.8, 3.2), (4.48 + off[0], 1.8, 3.2)):
    ax.plot([xs, xs], [y0 + off[1], y1 + off[1]], color=P.edge(LAT), lw=2.0, ls=(0, (2.2, 1.4)), zorder=30)
bio.callout(ax, (7.13 + off[0], 6.62 + off[1]), (9.0, 7.6), "Shoot apical meristem", size="small")
bio.label(ax, (9.1, 7.15), "(tip of a shoot)", size="tiny", color=P.muted(), ha="left")
bio.callout(ax, (4.69 + off[0], 8.8 + off[1]), (9.0, 10.2), "Axillary buds", size="small")
bio.callout(ax, (4.48 + off[0], 5.6 + off[1]), (9.0, 5.2), "Lateral meristems", size="small")
bio.label(ax, (9.1, 4.75), "(vascular and cork cambium)", size="tiny", color=P.muted(), ha="left")
bio.callout(ax, (7.42 + off[0], 1.34 + off[1]), (9.0, 1.5), "Root apical meristem", size="small")

# B: grass culm with intercalary meristems
bio.panel(ax, "B", (12.6, 12.5))
cx = 15.6
nodes = [0.9, 3.4, 6.1, 8.7]
ax.add_patch(Polygon([(cx - 0.28, 0.6), (cx + 0.28, 0.6), (cx + 0.22, 11.0), (cx - 0.22, 11.0)], closed=True,
                     facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=3))
# inflorescence at the top (the shoot apex is used up)
for k in range(7):
    y = 11.0 + k * 0.22
    for s in (-1, 1):
        ax.add_patch(Ellipse((cx + s * 0.22, y + 0.1), 0.34, 0.16, angle=s * 35, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.6, zorder=4))
for i, y in enumerate(nodes):
    ax.add_patch(Ellipse((cx, y), 0.75, 0.22, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=6))
    # intercalary meristem just above the node (base of the internode)
    ax.add_patch(Polygon([(cx - 0.27, y + 0.13), (cx + 0.27, y + 0.13), (cx + 0.27, y + 0.62), (cx - 0.27, y + 0.62)], closed=True,
                         facecolor=P.fill(AP), edgecolor=P.edge(AP), lw=0.8, zorder=5))
    # leaf sheath wrapping the lower part of the internode, then the blade
    side = -1 if i % 2 else 1
    sh_top = y + 1.6
    ax.add_patch(Polygon([(cx + side * 0.3, y + 0.1), (cx + side * 0.42, y + 0.1), (cx + side * 0.42, sh_top), (cx + side * 0.3, sh_top)],
                         closed=True, facecolor=P.light("plant"), edgecolor=P.edge("plant"), lw=0.8, zorder=6))
    ax.add_patch(Polygon([(cx + side * 0.3, y + 0.12), (cx + side * 0.42, y + 0.12), (cx + side * 0.42, y + 0.42), (cx + side * 0.3, y + 0.42)],
                         closed=True, facecolor=P.fill(AP), edgecolor=P.edge(AP), lw=0.6, zorder=6.5))
    t = np.linspace(0, 1, 30)
    bx = cx + side * (0.42 + 2.6 * t)
    by = sh_top + 1.2 * np.sin(t * 1.4) - 0.2 * t
    w = 0.16 * (1 - t) + 0.02
    ax.add_patch(Polygon(np.r_[np.c_[bx, by + w], np.c_[bx, by - w][::-1]], closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.8, zorder=5))
bio.callout(ax, (cx + 0.2, nodes[1] + 0.4), (17.2 + 0.5, 2.2), "Intercalary meristem", size="small")
bio.callout(ax, (cx - 0.38, nodes[0] + 0.3), (13.4, 0.35), "at the sheath base", size="tiny")
bio.callout(ax, (cx, nodes[2]), (13.4, 6.9), "Node", size="small")
bio.callout(ax, (cx - 0.1, nodes[2] + 1.4), (13.4, 8.2), "Internode", size="small")
bio.callout(ax, (cx, 11.5), (13.4, 11.9), "Inflorescence", size="small")
