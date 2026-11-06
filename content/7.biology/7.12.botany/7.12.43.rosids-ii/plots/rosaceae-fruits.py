# Floral cups and fruit types of Rosaceae. Top row: schematic longitudinal sections of flowers (grey:
# receptacle and floral cup; green: carpels): A Spiraea, shallow cup with five free carpels; B Fragaria,
# convex receptacle with many free carpels; C Rosa, urn-shaped cup bearing many free carpels on its inner
# wall; D Prunus, cup-shaped hypanthium around a single carpel; E Malus, carpels fused with the cup,
# ovary inferior. Bottom row: the corresponding fruits (aggregate of follicles, strawberry, hip, drupe,
# pome) and, at right, the aggregate of drupelets of Rubus.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(38, 15)
XS = [3.5, 10.5, 17.5, 24.5, 31.5]
Y0 = 9.0
REC = "neutral"


def cup(x, pts):
    ax.add_patch(Polygon([(x + a, Y0 + b) for a, b in pts], closed=True, facecolor=P.light(REC), edgecolor=P.edge(REC),
                         lw=1.1, zorder=3))


def car(x, y, w=0.45, h=0.9, ang=0):
    ax.add_patch(Ellipse((x, y), w, h, angle=ang, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9, zorder=5))
    ax.plot([x, x + 0.1 * math.sin(math.radians(-ang))], [y + h / 2, y + h / 2 + 0.5], color=P.edge("ovary"), lw=0.9,
            zorder=5)


def rim(x, y, s):
    ax.add_patch(Ellipse((x + s * 0.55, y + 0.5), 1.3, 0.5, angle=s * 35, facecolor=P.fill("petal"),
                         edgecolor=P.edge("petal"), lw=0.8, zorder=4))
    for k in range(3):
        ax.plot([x, x + s * (0.1 + 0.15 * k)], [y, y + 0.9 + 0.1 * k], color=P.edge("anther"), lw=0.7, zorder=4)


titles = ["Spiraea", "Fragaria", "Rosa", "Prunus", "Malus"]
for i, (x, name) in enumerate(zip(XS, titles)):
    bio.panel(ax, "ABCDE"[i], (x - 3.0, 14.8))
    bio.label(ax, (x, 14.4), name, size="title", italic=True)
    ax.plot([x, x], [Y0 - 2.4, Y0 - 0.6], color=P.edge("plant"), lw=2.0, zorder=2)
# A Spiraea
x = XS[0]
cup(x, [(-1.6, 0.4), (-0.6, -0.6), (0.6, -0.6), (1.6, 0.4), (1.4, 0.5), (0.5, -0.3), (-0.5, -0.3), (-1.4, 0.5)])
for dx in (-0.6, -0.2, 0.2, 0.6):
    car(x + dx, Y0 + 0.4, 0.38, 0.9)
rim(x + 1.5, Y0 + 0.4, 1); rim(x - 1.5, Y0 + 0.4, -1)
# B Fragaria
x = XS[1]
dome = [(x + 1.2 * math.cos(t), Y0 - 0.4 + 1.8 * math.sin(t)) for t in np.linspace(0, math.pi, 30)]
ax.add_patch(Polygon(dome, closed=True, facecolor=P.light(REC), edgecolor=P.edge(REC), lw=1.1, zorder=3))
for t in np.linspace(0.3, math.pi - 0.3, 7):
    car(x + 1.25 * math.cos(t), Y0 - 0.4 + 1.85 * math.sin(t), 0.3, 0.45, ang=math.degrees(t) - 90)
rim(x + 1.3, Y0 - 0.4, 1); rim(x - 1.3, Y0 - 0.4, -1)
# C Rosa
x = XS[2]
cup(x, [(-1.2, 2.0), (-1.6, 0.5), (-0.8, -0.8), (0.8, -0.8), (1.6, 0.5), (1.2, 2.0), (0.9, 2.0), (1.2, 0.5),
        (0.6, -0.4), (-0.6, -0.4), (-1.2, 0.5), (-0.9, 2.0)])
for dx, dy in [(-0.6, 0.2), (0.6, 0.2), (-0.3, -0.1), (0.3, -0.1), (-0.85, 0.9), (0.85, 0.9)]:
    car(x + dx, Y0 + dy, 0.3, 0.6)
rim(x + 1.05, Y0 + 2.0, 1); rim(x - 1.05, Y0 + 2.0, -1)
# D Prunus
x = XS[3]
cup(x, [(-1.6, 1.4), (-1.0, -0.4), (1.0, -0.4), (1.6, 1.4), (1.3, 1.4), (0.8, -0.1), (-0.8, -0.1), (-1.3, 1.4)])
car(x, Y0 + 0.5, 0.75, 1.1)
rim(x + 1.45, Y0 + 1.4, 1); rim(x - 1.45, Y0 + 1.4, -1)
# E Malus
x = XS[4]
cup(x, [(-1.3, 1.4), (-1.5, 0.2), (-0.8, -0.8), (0.8, -0.8), (1.5, 0.2), (1.3, 1.4)])
for dx in (-0.45, 0.0, 0.45):
    ax.add_patch(Ellipse((x + dx, Y0 + 0.2), 0.4, 1.0, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9,
                         zorder=5))
for dx in (-0.2, 0.2):
    ax.plot([x + dx, x + dx * 1.5], [Y0 + 1.4, Y0 + 2.2], color=P.edge("ovary"), lw=0.9, zorder=5)
rim(x + 1.3, Y0 + 1.4, 1); rim(x - 1.3, Y0 + 1.4, -1)
bio.label(ax, (XS[4] + 2.4, Y0 - 0.3), "ovary inferior", size="small", ha="left", color=P.muted())

# bottom row: fruits
YF = 3.2
x = XS[0]
for dx in (-0.7, -0.25, 0.25, 0.7):
    ax.add_patch(Ellipse((x + dx, YF), 0.42, 1.3, angle=dx * 12, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"),
                         lw=0.9, zorder=5))
    ax.plot([x + dx, x + dx], [YF - 0.5, YF + 0.5], color=P.edge("ovary"), lw=0.6, zorder=6)
bio.label(ax, (x, 0.9), "Aggregate of follicles", size="small")
bio.icon(ax, "wikimedia/fruit-accessory-strawberry", at=(XS[1], YF), height=3.2)
bio.label(ax, (XS[1], 0.9), "Aggregate of achenes\n(fleshy receptacle)", size="small")
x = XS[2]
hip = [(x + 1.1 * math.sin(t) * (1 - 0.3 * math.cos(t)), YF + 1.5 * math.cos(t)) for t in np.linspace(0, 2 * math.pi, 60)]
ax.add_patch(Polygon(hip, closed=True, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.1, zorder=4))
for dx, dy in [(-0.35, -0.4), (0.35, -0.4), (0, 0.1), (-0.3, 0.5), (0.3, 0.5)]:
    ax.add_patch(Ellipse((x + dx, YF + dy), 0.3, 0.42, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                         lw=0.7, zorder=5))
bio.label(ax, (x, 0.9), "Hip (achenes in\nfleshy floral cup)", size="small")
bio.icon(ax, "wikimedia/fruit-drupe", at=(XS[3], YF), height=3.2)
bio.label(ax, (XS[3], 0.9), "Drupe", size="small")
bio.icon(ax, "wikimedia/fruit-pome-apple", at=(XS[4] - 0.9, YF), height=3.0)
bio.icon(ax, "wikimedia/fruit-aggregate-rubus", at=(XS[4] + 2.6, YF), height=2.4)
bio.label(ax, (XS[4] - 0.9, 0.9), "Pome", size="small")
bio.label(ax, (XS[4] + 2.6, 0.9), "Drupelets (Rubus)", size="small")
