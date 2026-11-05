# Magnoliaceae. A: longitudinal section of a Yulan magnolia flower (Magnolia denudata): an elongate
# columnar receptacle bearing numerous spirally arranged stamens (short filaments, long anthers) on its
# lower part and numerous free carpels on its upper part, surrounded by tepals in whorls of three; the
# ring on the pedicel is the scar left by the stipule. B: an aggregate of follicles opening along the
# dorsal suture, the red seeds hanging on threads (unrolled spiral thickenings of the funicle). C: in
# Michelia the gynoecium is raised on a stalk (gynophore). D: leaf and aggregate of samaras of the tulip
# tree (Liriodendron chinense). Top right: PhyloPic silhouette of Magnolia.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

P = bio.P
fig, ax = bio.canvas(34, 15)


def tepal(base, angle, length, width, tok="tepal"):
    t = np.linspace(0, 1, 40)
    a = math.radians(angle)
    u, v = np.array([math.cos(a), math.sin(a)]), np.array([-math.sin(a), math.cos(a)])
    half = width / 2 * np.sin(np.pi * t) ** 0.7
    bend = 0.18 * length * t ** 2
    left = [base + u * (length * s) + v * (h + b) for s, h, b in zip(t, half, bend)]
    right = [base + u * (length * s) + v * (-h + b) for s, h, b in zip(t, half, bend)]
    ax.add_patch(Polygon(left + right[::-1], closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1,
                         zorder=4))


def stamen(p, side):
    ax.plot([p[0], p[0] + side * 0.25], [p[1], p[1] + 0.05], color=P.edge("anther"), lw=1.0, zorder=6)
    ax.add_patch(Ellipse((p[0] + side * 0.75, p[1] + 0.14), 1.0, 0.24, angle=side * 12, facecolor=P.fill("anther"),
                         edgecolor=P.edge("anther"), lw=0.8, zorder=6))


def carpel(p, side, size=0.5):
    ax.add_patch(Ellipse((p[0] + side * size * 0.55, p[1]), size * 1.1, size * 0.62, angle=side * 25,
                         facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9, zorder=6))
    ax.plot([p[0] + side * size, p[0] + side * size * 1.35], [p[1] + 0.12, p[1] + 0.38], color=P.edge("ovary"),
            lw=1.0, zorder=6)


# A: longitudinal section
bio.panel(ax, "A", (0.3, 14.7))
cx = 5.2
ax.add_patch(FancyBboxPatch((cx - 0.35, 2.6), 0.7, 8.4, boxstyle="round,pad=0.05,rounding_size=0.3",
                            facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=5))
ax.plot([cx, cx], [0.4, 2.6], color=P.edge("plant"), lw=5, zorder=3, solid_capstyle="butt")
ax.plot([cx - 0.32, cx + 0.32], [1.4, 1.4], color=P.ink(), lw=1.4, zorder=6)
bio.callout(ax, (cx + 0.32, 1.4), (7.6, 0.9), "Stipular scar (ring)", size="small")
for k, (ang, L) in enumerate([(38, 5.4), (28, 6.0), (18, 6.4)]):
    for s in (-1, 1):
        tepal(np.array([cx + s * 0.3, 2.8 + 0.2 * k]), 90 - s * ang, L, 0.75)
for i, y in enumerate(np.linspace(3.2, 6.6, 12)):
    side = 1 if i % 2 == 0 else -1
    stamen((cx + side * 0.35, y), side)
for i, y in enumerate(np.linspace(7.2, 10.6, 10)):
    side = 1 if i % 2 == 0 else -1
    carpel((cx + side * 0.35, y), side)
bio.callout(ax, (cx + 1.25, 6.1), (9.6, 5.6), "Stamens", size="small")
bio.callout(ax, (cx + 0.75, 9.9), (9.6, 10.4), "Carpels", size="small")
bio.callout(ax, (cx, 7.0), (9.6, 7.8), "Receptacle", size="small")
bio.callout(ax, (cx - 3.4, 6.9), (0.8, 10.6), "Tepals", size="small")
bio.label(ax, (5.2, 14.0), r"$\it{Magnolia\ denudata}$", size="title")

# B: aggregate of follicles
bio.panel(ax, "B", (11.6, 14.7))
bx = 15.0
ax.add_patch(FancyBboxPatch((bx - 0.3, 3.0), 0.6, 8.0, boxstyle="round,pad=0.05,rounding_size=0.3",
                            facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=5))
ax.plot([bx, bx], [0.6, 3.0], color=P.edge("plant"), lw=4.5, zorder=3, solid_capstyle="butt")
for i, y in enumerate(np.linspace(3.6, 10.4, 9)):
    side = 1 if i % 2 == 0 else -1
    p = np.array([bx + side * 0.95, y])
    ax.add_patch(Ellipse(p, 1.5, 0.85, angle=side * 20, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0,
                         zorder=6))
    if i in (1, 4, 6):
        q = p + np.array([side * 0.6, -0.2])
        ax.plot([q[0], q[0] + side * 0.15], [q[1], q[1] - 1.1], color=P.muted(), lw=0.7, zorder=7)
        ax.add_patch(Ellipse((q[0] + side * 0.15, q[1] - 1.45), 0.55, 0.65, facecolor=P.fill("negative"),
                             edgecolor=P.edge("negative"), lw=0.9, zorder=8))
bio.callout(ax, (bx + 1.95, 7.6), (19.6, 8.6), "Red seed on a thread", size="small")
bio.label(ax, (bx, 14.0), "Aggregate of follicles", size="title")

# C: gynophore of Michelia
bio.panel(ax, "C", (20.6, 14.7))
mx = 23.0
ax.plot([mx, mx], [1.0, 9.6], color=P.edge("plant"), lw=4, zorder=3)
for i, y in enumerate(np.linspace(2.2, 4.0, 6)):
    stamen((mx + (0.2 if i % 2 == 0 else -0.2), y), 1 if i % 2 == 0 else -1)
for i, y in enumerate(np.linspace(7.4, 9.6, 6)):
    carpel((mx + (0.2 if i % 2 == 0 else -0.2), y), 1 if i % 2 == 0 else -1, size=0.45)
ax.annotate("", xy=(mx + 1.5, 7.1), xytext=(mx + 1.5, 4.5), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=1))
bio.label(ax, (mx + 1.7, 5.8), "Gynophore", size="small", ha="left")
bio.label(ax, (mx, 14.0), r"$\it{Michelia}$", size="title")

# D: Liriodendron leaf and samaras
bio.panel(ax, "D", (26.6, 14.7))
lx, ly = 30.4, 9.0
leaf = [(0, -2.6), (0.9, -2.0), (2.3, -1.6), (2.0, -0.4), (2.6, 0.6), (1.4, 0.9), (1.0, 1.8), (0.0, 1.8),
        (-1.0, 1.8), (-1.4, 0.9), (-2.6, 0.6), (-2.0, -0.4), (-2.3, -1.6), (-0.9, -2.0)]
ax.add_patch(Polygon([(lx + x, ly + y) for x, y in leaf], closed=True, facecolor=P.fill("plant"),
                     edgecolor=P.edge("plant"), lw=1.2, zorder=4))
ax.plot([lx, lx], [ly - 4.0, ly + 1.8], color=P.edge("plant"), lw=1.2, zorder=5)
for s in (-1, 1):
    ax.plot([lx, lx + s * 2.2], [ly - 1.0, ly - 1.5], color=P.edge("plant"), lw=0.8, zorder=5)
    ax.plot([lx, lx + s * 2.3], [ly + 0.1, ly + 0.55], color=P.edge("plant"), lw=0.8, zorder=5)
bio.label(ax, (lx, ly + 2.6), "truncate tip", size="tiny", color=P.muted())
sx, sy = 30.4, 2.4
ax.plot([sx, sx], [0.6, sy + 1.6], color=P.edge("plant"), lw=2.5, zorder=3)
for k in range(7):
    for s in (-1, 1):
        ang = 90 - s * (14 + k * 6)
        a = math.radians(ang)
        c = np.array([sx, sy + 0.25 * k]) + 1.25 * np.array([math.cos(a), math.sin(a)])
        ax.add_patch(Ellipse(c, 2.4, 0.42, angle=ang, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.8,
                             zorder=4 + k))
bio.label(ax, (sx, 0.2), "Aggregate of samaras", size="small")
bio.label(ax, (lx, 14.0), r"$\it{Liriodendron}$", size="title")
bio.icon(ax, "phylopic/magnolia", at=(33.0, 12.2), height=1.2, color="petal")
