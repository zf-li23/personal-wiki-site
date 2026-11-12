# Where the beak arises in the three large suborders of Hemiptera (schematic lateral views of head and
# prothorax, not to scale; the labium, which forms the beak, is green as in the mouthpart figures of 7.17.23).
# Heteroptera: the beak arises from the front of the head, separated from the prothorax by a gula, and can be
# swung forward. Auchenorrhyncha: it arises from the back of the head capsule on its underside, close to the
# prothorax. Sternorrhyncha: the head is deflexed and the beak appears to arise between or behind the fore
# coxae.
import numpy as np
from matplotlib.patches import Ellipse, Polygon
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(25, 8.5)
LAB = zm.MOUTH["labium"]
panels = [("Heteroptera", "true bugs", "front of head;\ngula behind it", 0.0, (0.95, -0.4)),
          ("Auchenorrhyncha", "cicadas, leafhoppers", "back of head,\nunderside", 0.0, (0.25, -0.75)),
          ("Sternorrhyncha", "aphids, psyllids, scale insects", "between the\nfore coxae", -35.0, (-0.6, -0.75))]
for i, (name, common, where, tilt, origin) in enumerate(panels):
    cx = 4.2 + i * 8.2
    cy = 4.6
    bio.label(ax, (cx, 8.0), name, size="normal", bold=True)
    bio.label(ax, (cx, 7.45), common, size="tiny", color=P.muted())
    # prothorax and mesothorax
    ax.add_patch(Polygon([(cx - 2.6, cy - 1.0), (cx - 0.4, cy - 1.2), (cx - 0.4, cy + 1.3), (cx - 2.6, cy + 1.0)],
                         closed=True, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=4))
    ax.add_patch(Polygon([(cx - 4.0, cy - 0.9), (cx - 2.6, cy - 1.0), (cx - 2.6, cy + 1.0), (cx - 4.0, cy + 0.9)],
                         closed=True, facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=0.8, zorder=3))
    # head (tilted down in Sternorrhyncha)
    hx, hy = cx + 0.6, (cy - 0.5 if i == 2 else cy + 0.1)
    ax.add_patch(Ellipse((hx, hy), 2.1, 2.0, angle=tilt, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9,
                         zorder=5))
    ax.add_patch(Ellipse((hx + 0.35, hy + 0.45), 0.55, 0.65, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"),
                         lw=0.7, zorder=6))
    # fore coxa
    ax.add_patch(Ellipse((cx - 1.0, cy - 1.45), 0.75, 0.95, facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=0.8,
                         zorder=3))
    # beak: 3-4 segments along the underside, pointing backward
    o = (hx + origin[0], hy + origin[1])
    pts = [o, (o[0] - 0.4, o[1] - 0.9), (cx - 0.6, cy - 2.0), (cx - 2.2, cy - 2.2), (cx - 3.4, cy - 2.25)]
    if i == 2:
        pts = [o, (o[0] - 0.5, o[1] - 0.6), (cx - 1.6, cy - 2.1), (cx - 2.8, cy - 2.3)]
    for a, b in zip(pts[:-1], pts[1:]):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(LAB), lw=4.2, solid_capstyle="round", zorder=7)
        ax.plot([b[0]], [b[1]], "o", color=P.fill(LAB), ms=3, zorder=8)
    ax.plot([o[0]], [o[1]], "o", color=P.edge("negative"), ms=6, zorder=9)
    bio.callout(ax, o, (cx + 1.0, 1.3), "beak arises:\n" + where, size="small")
    if i == 0:
        bio.callout(ax, (hx - 0.2, hy - 0.9), (cx - 2.8, 7.0), "gula", size="small")
    bio.callout(ax, (cx - 1.0, cy - 1.45), (cx - 3.4, 1.0), "fore coxa", size="small")
bio.label(ax, (24.8, 0.15), "Schematic lateral views; head to the right", size="tiny", color=P.muted(), ha="right")
