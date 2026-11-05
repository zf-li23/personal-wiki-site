# External morphology of the stem. (A) A leafy shoot (alternate leaves): nodes, internodes, terminal bud
# and axillary buds (wikibio.botany). (B) A three-year-old winter twig of a deciduous tree: scaly
# terminal bud, axillary buds above leaf scars with bundle scars, lenticels and the rings of bud-scale
# scars that separate the annual increments. (C) Longitudinal section of a vegetative bud: apical
# meristem, leaf primordia and young leaves, axillary bud primordia, and the unexpanded bud axis.
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(30.0, 15.0)

# ---- A
bio.panel(ax, "A", (0.2, 14.8))
bio.label(ax, (0.85, 14.77), "Leafy shoot", size="title", ha="left", va="top")
s = B.shoot(ax, (5.0, 0.8), 11.5, arrangement="alternate", nodes=4, leaf_length=2.6)
bio.callout(ax, s["apical_bud"], (7.6, 13.6), "Terminal bud")
if s.get("axillary_bud") is not None:
    bio.callout(ax, s["axillary_bud"], (1.2, 9.0), "Axillary bud")
nodes = s.get("nodes") or []
if len(nodes) >= 2:
    bio.callout(ax, nodes[1], (1.2, 6.2), "Node")
    mid = ((nodes[0][0] + nodes[1][0]) / 2, (nodes[0][1] + nodes[1][1]) / 2)
    bio.callout(ax, mid, (1.2, 3.4), "Internode")

# ---- B: winter twig
bio.panel(ax, "B", (10.2, 14.8))
bio.label(ax, (10.85, 14.77), "Winter twig (3 years)", size="title", ha="left", va="top")
x = 14.0
segs = [(0.8, 5.0, 0.55), (5.0, 9.0, 0.45), (9.0, 12.6, 0.36)]  # year 3 (oldest, bottom) ... year 1
for y0, y1, w in segs:
    ax.add_patch(Polygon([(x - w, y0), (x + w, y0), (x + w * 0.92, y1), (x - w * 0.92, y1)], closed=True,
                         facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.0, zorder=4))
rng = np.random.default_rng(2)
for y0, y1, w in segs:  # lenticels
    for _ in range(int((y1 - y0) * 2)):
        yy = rng.uniform(y0 + 0.3, y1 - 0.3)
        ax.add_patch(Ellipse((x + rng.uniform(-w * 0.6, w * 0.6), yy), 0.08, 0.22, facecolor=P.light("animal"),
                             edgecolor=P.edge("animal"), lw=0.4, zorder=5))
for yy, w in ((5.0, 0.5), (9.0, 0.4)):  # bud-scale scar rings
    for d in np.linspace(-0.12, 0.12, 5):
        ax.plot([x - w, x + w], [yy + d, yy + d], color=P.edge("animal"), lw=0.7, zorder=5.5)
# terminal scaly bud
tb = bio.smooth_closed([(x - 0.34, 12.6), (x - 0.36, 13.2), (x - 0.15, 13.9), (x, 14.15), (x + 0.15, 13.9), (x + 0.36, 13.2),
                        (x + 0.34, 12.6)], n=100)
ax.add_patch(Polygon(tb, closed=True, facecolor=P.fill("sepal"), edgecolor=P.edge("sepal"), lw=1.0, zorder=6))
for k, yy in enumerate((12.9, 13.3, 13.7)):
    ax.plot([x - 0.3 + 0.08 * k, x + 0.05, x + 0.3 - 0.08 * k], [yy - 0.15, yy + 0.08, yy - 0.15], color=P.edge("sepal"), lw=0.6,
            zorder=6.5)
# leaf scars with bundle scars and axillary buds, alternate
scars = [(1.9, 1), (3.6, -1), (6.2, 1), (7.8, -1), (10.2, 1), (11.6, -1)]
for yy, sg in scars:
    w = [ww for y0, y1, ww in segs if y0 <= yy < y1][0]
    cx = x + sg * (w + 0.05)
    ax.add_patch(Ellipse((cx, yy), 0.5, 0.32, facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=0.8, zorder=6))
    for d in (-0.12, 0, 0.12):
        ax.add_patch(Ellipse((cx + d, yy - 0.02), 0.06, 0.06, color=P.edge("animal"), zorder=6.5))
    bud = Ellipse((cx + sg * 0.05, yy + 0.42), 0.32, 0.5, angle=-sg * 25, facecolor=P.fill("sepal"), edgecolor=P.edge("sepal"),
                  lw=0.8, zorder=6)
    ax.add_patch(bud)
bio.callout(ax, (x + 0.1, 13.6), (17.0, 13.9), "Terminal bud (scaly)")
bio.callout(ax, (x + 0.4, 10.62), (17.0, 11.6), "Axillary bud")
bio.callout(ax, (x + 0.45, 10.2), (17.0, 10.4), "Leaf scar")
bio.callout(ax, (x + 0.45, 10.18), (17.0, 9.6), "Bundle scars", size="small")
bio.callout(ax, (x + 0.35, 9.0), (17.0, 8.6), "Bud-scale scars")
bio.callout(ax, (x - 0.2, 7.0), (17.0, 7.2), "Lenticel")
for (y0, y1, w), t in zip(segs, ("3rd year", "2nd year", "1st year")):
    ax.plot([x - 1.0, x - 1.0], [y0 + 0.1, y1 - 0.1], color=P.muted(), lw=0.8)
    bio.label(ax, (x - 1.15, (y0 + y1) / 2), t, size="tiny", color=P.muted(), ha="right")

# ---- C: bud section
bio.panel(ax, "C", (20.2, 14.8))
bio.label(ax, (20.85, 14.77), "Vegetative bud (section)", size="title", ha="left", va="top")
cx, y0 = 24.4, 2.0
axis = Polygon([(cx - 0.9, y0), (cx + 0.9, y0), (cx + 0.55, y0 + 8.6), (cx - 0.55, y0 + 8.6)], closed=True,
               facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=4)
ax.add_patch(axis)
dome = bio.smooth_closed([(cx - 0.55, y0 + 8.5), (cx - 0.4, y0 + 9.1), (cx, y0 + 9.35), (cx + 0.4, y0 + 9.1), (cx + 0.55, y0 + 8.5)],
                         n=80)
ax.add_patch(Polygon(dome, closed=True, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.0, zorder=5))
leaves = [(y0 + 8.4, 0.5, 0.6), (y0 + 7.6, 1.0, 1.3), (y0 + 6.3, 1.6, 2.6), (y0 + 4.7, 2.2, 4.4), (y0 + 2.9, 2.8, 6.3),
          (y0 + 1.2, 3.3, 8.0)]
for k, (yb, reach, h) in enumerate(leaves):
    sg = 1 if k % 2 == 0 else -1
    base_x = cx + sg * (0.5 + 0.06 * k)
    tip = (cx + sg * min(reach * 0.55, 1.6) * 0.6, min(yb + h, y0 + 10.6 + 0.0 * k))
    outer = (cx + sg * (0.6 + reach * 0.5), yb + h * 0.45)
    leaf = bio.smooth_closed([(base_x, yb), outer, tip, (base_x + sg * 0.1, yb + h * 0.35)], n=80)
    ax.add_patch(Polygon(leaf, closed=True, facecolor=P.fill("plant") if k > 1 else P.light("plant"), edgecolor=P.edge("plant"),
                         lw=0.8, zorder=5 - 0.01 * k))
    if 1 <= k <= 4:  # axillary bud primordia in the axils
        ax.add_patch(Ellipse((base_x - sg * 0.02, yb + 0.25), 0.32, 0.4, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                             lw=0.7, zorder=5.5))
bio.callout(ax, (cx, y0 + 9.2), (28.0, 12.2), "Apical meristem")
bio.callout(ax, (cx - 0.75, y0 + 7.8), (21.0, 10.8), "Leaf primordium")
bio.callout(ax, (cx + 1.6, y0 + 5.5), (28.0, 8.4), "Young leaf")
bio.callout(ax, (cx + 0.56, y0 + 6.55), (28.0, 6.6), "Axillary bud primordium")
bio.callout(ax, (cx, y0 + 1.0), (21.0, 2.4), "Bud axis")
