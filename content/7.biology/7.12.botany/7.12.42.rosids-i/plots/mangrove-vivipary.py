# Vivipary in Rhizophora (schematic). A: flowering and fruiting; the ripe fruit stays on the parent tree.
# B: the seed germinates inside the fruit and the hypocotyl grows out through the pericarp. C: the
# hypocotyl becomes a long club-shaped propagule hanging from the branch. D: the propagule drops and
# lodges in the mud of the intertidal zone, or floats away and strands elsewhere. E: lateral roots and the
# first leaves develop; a young tree. Background: high- and low-tide lines; the parent tree stands on
# stilt roots.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon, Rectangle

P = bio.P
fig, ax = bio.canvas(36, 14)
MUD, LOW, HIGH = 2.0, 3.4, 5.6
ax.add_patch(Rectangle((0, 0.2), 36, MUD - 0.2, facecolor=P.light("neutral"), edgecolor="none", zorder=1))
for y, t in [(HIGH, "High tide"), (LOW, "Low tide")]:
    ax.plot([0.2, 35.8], [y, y], color=P.edge("dna"), lw=1.0, ls=(0, (5, 3)), zorder=2)
    bio.label(ax, (35.8, y + 0.3), t, size="small", ha="right", color=P.edge("dna"))
bio.label(ax, (0.4, 1.0), "Mud", size="small", ha="left")

# parent tree with stilt roots
tx = 7.0
ax.plot([tx, tx], [6.5, 12.0], color=P.edge("plant"), lw=6, solid_capstyle="round", zorder=3)
for s, d in [(-1, 2.6), (-1, 1.5), (1, 1.4), (1, 2.7), (-1, 3.6)]:
    xs = np.linspace(0, 1, 30)
    ax.plot(tx + s * d * xs, 6.8 - 1.0 * xs + (MUD - 6.8 + 1.0) * xs ** 2.2 + 0.6 * np.sin(math.pi * xs),
            color=P.edge("plant"), lw=2.2, zorder=3)
ax.plot([tx, tx + 6.5], [11.0, 12.2], color=P.edge("plant"), lw=3, zorder=3)
ax.plot([tx, tx - 5.0], [11.4, 12.4], color=P.edge("plant"), lw=3, zorder=3)
for x, y in [(tx - 4.4, 12.3), (tx - 2.8, 12.1), (tx + 2.2, 11.6), (tx + 4.4, 12.1), (tx + 6.2, 12.3)]:
    for s in (-1, 1):
        ax.add_patch(Ellipse((x + s * 0.5, y + 0.5), 1.1, 0.5, angle=s * 30, facecolor=P.fill("plant"),
                             edgecolor=P.edge("plant"), lw=0.8, zorder=4))
# stages along the right branch
stages = [("A", tx + 1.6, 11.3, 0.0), ("B", tx + 3.4, 11.6, 1.2), ("C", tx + 5.4, 12.0, 4.0)]
for L, x, y, hyp in stages:
    ax.add_patch(Ellipse((x, y - 0.6), 0.6, 0.9, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
    for s in (-1, 1):
        ax.plot([x, x + s * 0.5], [y - 0.4, y - 0.9], color=P.edge("sepal"), lw=1.4, zorder=6)
    if hyp:
        ax.add_patch(Polygon([(x - 0.12, y - 1.0), (x + 0.12, y - 1.0), (x + 0.2, y - 1.0 - hyp),
                              (x, y - 1.2 - hyp), (x - 0.2, y - 1.0 - hyp)], closed=True, facecolor=P.fill("plant"),
                             edgecolor=P.edge("plant"), lw=0.9, zorder=6))
    bio.panel(ax, L, (x - 0.3, y + 0.9))
bio.callout(ax, (tx + 1.6, 10.6), (tx + 0.4, 9.0), "Fruit on tree", size="small")
bio.callout(ax, (tx + 5.4, 8.6), (tx + 7.6, 9.8), "Hypocotyl (propagule)", size="small")

# D: propagule lodged and floating
bio.panel(ax, "D", (17.0, 9.0))
px = 19.0
ax.add_patch(Polygon([(px - 0.15, MUD + 3.0), (px + 0.15, MUD + 3.0), (px + 0.2, MUD - 0.6), (px, MUD - 0.8),
                      (px - 0.2, MUD - 0.6)], closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"),
                     lw=0.9, zorder=6))
bio.arrow(ax, (tx + 5.6, 7.6), (px - 0.3, MUD + 3.2), kind="process", bend=-0.25)
fx = 23.5
ax.add_patch(Polygon([(fx - 1.8, HIGH + 0.1), (fx + 1.8, HIGH + 0.4), (fx + 1.9, HIGH + 0.2), (fx - 1.7, HIGH - 0.1)],
                     closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.9, zorder=6))
bio.arrow(ax, (fx + 2.2, HIGH + 0.6), (fx + 4.2, HIGH + 0.6), kind="process")
bio.label(ax, (fx, HIGH + 1.2), "Floats, strands elsewhere", size="small")
bio.label(ax, (px, 8.2), "Lodges in mud", size="small")

# E: young tree
bio.panel(ax, "E", (29.0, 9.0))
ex = 31.0
ax.plot([ex, ex], [MUD - 0.6, MUD + 3.4], color=P.edge("plant"), lw=2.6, zorder=5)
for s in (-1, 1):
    ax.add_patch(Ellipse((ex + s * 0.7, MUD + 3.7), 1.3, 0.55, angle=s * 25, facecolor=P.fill("plant"),
                         edgecolor=P.edge("plant"), lw=0.9, zorder=6))
for k in range(5):
    a = math.radians(200 + 35 * k)
    ax.plot([ex, ex + 1.2 * math.cos(a)], [MUD - 0.3, MUD - 0.3 + 0.8 * math.sin(a)], color=P.muted(), lw=0.9, zorder=5)
bio.label(ax, (ex, 7.0), "Lateral roots, first leaves", size="small")
bio.label(ax, (tx, 13.5), r"Parent tree ($\it{Rhizophora}$) on stilt roots", size="small")
