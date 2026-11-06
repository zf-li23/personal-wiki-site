# Catkins and flowers of Populus and Salix. A: pendulous male catkin of Populus; A': a male flower: bract
# with a fimbriate tip, cup-shaped disc bearing many stamens; A'': a female flower: bract, disc and a
# bicarpellate ovary. B: erect male catkin of Salix; B': a male flower: entire bract, two stamens and one or
# two nectar glands; B'': a female flower: gland and ovary. C: dehisced capsule releasing seeds with a tuft
# of silky hairs.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(36, 14)


def catkin(top, length, angle, n=14):
    a = math.radians(angle)
    u = np.array([math.cos(a), math.sin(a)])
    v = np.array([-u[1], u[0]])
    p0 = np.array(top)
    ax.plot([p0[0] - u[0] * 0.8, p0[0]], [p0[1] - u[1] * 0.8, p0[1]], color=P.edge("plant"), lw=1.6)
    for k in range(n):
        c = p0 + u * (0.2 + length * k / n)
        for s in (-1, 1):
            ax.add_patch(Ellipse(c + v * s * 0.28, 0.55, 0.36, angle=angle + s * 30, facecolor=P.fill("anther"),
                                 edgecolor=P.edge("anther"), lw=0.6, zorder=5))
        ax.add_patch(Ellipse(c, 0.42, 0.3, angle=angle, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.6,
                             zorder=6))


def bract(base, fimbriate, z=4):
    x, y = base
    if fimbriate:
        pts = [(x - 0.9, y + 2.2)]
        for k in range(9):
            pts.append((x - 0.9 + 0.2 * k, y + 2.6 + (0.35 if k % 2 else 0)))
        pts += [(x + 0.9, y + 2.2), (x + 0.3, y), (x - 0.3, y)]
    else:
        pts = [(x - 0.8, y + 2.2), (x, y + 2.8), (x + 0.8, y + 2.2), (x + 0.3, y), (x - 0.3, y)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=1.0, zorder=z))


def stamens(base, n, spread):
    x, y = base
    for k in range(n):
        dx = (k - (n - 1) / 2) * spread
        ax.plot([x + dx * 0.4, x + dx], [y, y + 1.4], color=P.edge("anther"), lw=0.9, zorder=7)
        ax.add_patch(Ellipse((x + dx, y + 1.55), 0.3, 0.4, facecolor=P.fill("anther"), edgecolor=P.edge("anther"),
                             lw=0.6, zorder=8))


def ovary(base):
    x, y = base
    ax.add_patch(Ellipse((x, y + 0.9), 0.8, 1.6, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=8))
    for s in (-1, 1):
        ax.plot([x, x + 0.4 * s], [y + 1.7, y + 2.2], color=P.edge("ovary"), lw=1.0, zorder=8)


bio.label(ax, (5.5, 13.6), r"$\it{Populus}$", size="title")
bio.panel(ax, "A", (0.3, 13.6))
catkin((1.6, 12.2), 6.5, -80)
bio.label(ax, (1.8, 4.2), "Pendulous", size="small")
for L, x, female in [("A'", 5.4, False), ("A''", 9.0, True)]:
    bio.panel(ax, L, (x - 1.4, 11.6))
    bract((x, 6.0), True)
    ax.add_patch(Polygon([(x - 0.8, 7.4), (x + 0.8, 7.4), (x + 0.4, 6.8), (x - 0.4, 6.8)], closed=True,
                         facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=7))
    if female:
        ovary((x, 7.3))
    else:
        stamens((x, 7.4), 8, 0.22)
bio.callout(ax, (5.4 + 0.75, 7.15), (7.0, 4.6), "Cup-shaped disc", size="small")
bio.callout(ax, (5.4 - 0.6, 8.7), (3.4, 10.6), "Fimbriate bract", size="small")

bio.label(ax, (18.8, 13.6), r"$\it{Salix}$", size="title")
bio.panel(ax, "B", (13.0, 13.6))
catkin((14.6, 5.6), 5.0, 80, n=11)
bio.label(ax, (14.8, 4.2), "Erect", size="small")
for L, x, female in [("B'", 18.6, False), ("B''", 22.2, True)]:
    bio.panel(ax, L, (x - 1.4, 11.6))
    bract((x, 6.0), False)
    ax.add_patch(Ellipse((x + 0.55, 7.0), 0.35, 0.5, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                         lw=1.0, zorder=7))
    if female:
        ovary((x - 0.1, 7.0))
    else:
        stamens((x - 0.1, 7.0), 2, 0.5)
bio.callout(ax, (18.6 + 0.7, 7.0), (20.0, 4.6), "Nectar gland", size="small")
bio.callout(ax, (18.6 - 0.5, 8.4), (16.4, 10.6), "Entire bract", size="small")

bio.panel(ax, "C", (25.6, 13.6))
cx, cy = 29.5, 5.0
for s in (-1, 1):
    pts = [(cx, cy), (cx + s * 0.5, cy + 1.6), (cx + s * 1.4, cy + 3.0), (cx + s * 0.6, cy + 1.4)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=5))
ax.plot([cx, cx], [cy - 1.2, cy], color=P.edge("plant"), lw=1.6)
rng = np.random.default_rng(0)
for k in range(5):
    sx, sy = cx - 0.6 + 0.9 * k + 0.3, cy + 4.0 + 1.3 * math.sin(k * 1.7) + 0.6 * k
    ax.add_patch(Ellipse((sx, sy), 0.22, 0.14, facecolor=P.ink(), edgecolor="none", zorder=7))
    for j in range(9):
        th = math.radians(40 + 100 * j / 8)
        ax.plot([sx, sx + 0.9 * math.cos(th)], [sy, sy + 0.9 * math.sin(th)], color=P.muted(), lw=0.6, zorder=6)
bio.label(ax, (cx, 2.6), "Capsule; seeds with silky hairs", size="small")
