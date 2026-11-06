# Homology of tendrils and inflorescences in Vitaceae (schematic). A: sympodial shoot of Vitis: at each node
# the shoot apex becomes a tendril or an inflorescence and is pushed to the side opposite the leaf, while the
# axillary bud continues the axis (successive sympodial units in alternating shades). B: series from a
# branched tendril through a tendril bearing a few flowers to an inflorescence. C: Parthenocissus: tendril
# branches end in adhesive pads attached to a wall.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle

P = bio.P
fig, ax = bio.canvas(34, 14)


def leaf(base, side, size=1.15):
    x, y = base
    t = np.linspace(0, 2 * math.pi, 7, endpoint=False)
    c = np.array([x + side * (size * 1.25), y + 0.4])
    pts = [c + size * (0.75 + 0.25 * math.cos(5 * a)) * np.array([math.cos(a), math.sin(a)]) for a in np.linspace(0, 2 * math.pi, 120)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=4))
    ax.plot([x, c[0] - side * size * 0.6], [y, c[1] - 0.1], color=P.edge("plant"), lw=1.2, zorder=4)


def tendril(base, side, n=2, length=2.0):
    x, y = base
    tip = np.array([x + side * length * 0.6, y + length * 0.5])
    ax.plot([x, tip[0]], [y, tip[1]], color=P.edge("plant"), lw=1.3, zorder=5)
    for k in range(n):
        t = np.linspace(0, 3.5 * math.pi, 60)
        d = np.array([side * (0.4 + 0.3 * k), 0.5 - 0.6 * k])
        coil = [tip + d * s / (3.5 * math.pi) + 0.18 * np.array([math.cos(s), math.sin(s)]) for s in t]
        ax.plot(*np.array(coil).T, color=P.edge("plant"), lw=1.1, zorder=5)


def flowers(base, side, n=6, spread=1.4):
    x, y = base
    ax.plot([x, x + side * 1.4], [y, y + 1.2], color=P.edge("plant"), lw=1.3, zorder=5)
    for k in range(n):
        p = (x + side * (0.6 + 0.25 * k) + 0.2 * math.sin(k * 1.7), y + 0.9 + 0.3 * k * 0.6 + 0.4 * math.cos(k))
        ax.add_patch(Circle(p, 0.16, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=0.7, zorder=6))


# A: sympodial shoot
bio.panel(ax, "A", (0.3, 13.8))
toks = ["plant", "neutral", "plant", "neutral"]
x = 5.0
for i in range(4):
    y0, y1 = 1.0 + 3.0 * i, 4.0 + 3.0 * i
    xs = x + (0.25 if i % 2 else -0.25)
    ax.plot([xs, xs], [y0, y1], color=P.edge(toks[i]), lw=4.5, solid_capstyle="round", zorder=3)
    side = 1 if i % 2 == 0 else -1
    if i == 3:
        continue
    leaf((xs, y1 - 0.2), side)
    if i == 1:
        flowers((xs, y1 - 0.2), -side)
    elif i < 3:
        tendril((xs, y1 - 0.2), -side)
bio.callout(ax, (6.9, 7.5), (10.4, 9.4), "Inflorescence opposite the leaf", size="small")
bio.callout(ax, (3.4, 4.4), (0.6, 2.2), "Tendril opposite the leaf", size="small")
bio.label(ax, (5.6, 13.6), "Sympodial units (alternating shades)", size="small")

# B: series tendril -> inflorescence
bio.panel(ax, "B", (12.2, 13.8))
for j, (nf, title) in enumerate([(0, "Tendril"), (3, "Tendril with flowers"), (9, "Inflorescence")]):
    bx = 14.0 + j * 5.2
    by = 3.0
    ax.plot([bx, bx], [by, by + 4.0], color=P.edge("plant"), lw=1.6, zorder=5)
    ax.plot([bx, bx + 1.5], [by + 2.0, by + 4.6], color=P.edge("plant"), lw=1.4, zorder=5)
    for k, tip in enumerate([(bx, by + 4.0), (bx + 1.5, by + 4.6)]):
        if j == 0 or (j == 1 and k == 0):
            t = np.linspace(0, 4 * math.pi, 80)
            ax.plot(tip[0] + 0.3 * np.cos(t) * (1 - t / 15), tip[1] + t * 0.1, color=P.edge("plant"), lw=1.1, zorder=5)
        else:
            for m in range(nf // 2 + (1 if j == 2 else 0) + 2):
                p = (tip[0] + 0.45 * math.cos(m * 1.3), tip[1] + 0.25 * m + 0.2 * math.sin(m))
                ax.add_patch(Circle(p, 0.18, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=0.7, zorder=6))
    bio.label(ax, (bx + 0.6, 1.8), title, size="small")
bio.arrow(ax, (16.3, 10.2), (26.0, 10.2), kind="process")
bio.label(ax, (21.2, 10.8), "Same position, branching and gene expression (LEAFY homologue)", size="small")

# C: Parthenocissus pads
bio.panel(ax, "C", (28.4, 13.8))
ax.add_patch(Rectangle((32.4, 1.0), 1.2, 11.5, facecolor=P.light("neutral"), edgecolor=P.muted(), lw=0.8, zorder=2))
bx, by = 29.4, 6.0
ax.plot([bx, bx + 1.4], [by, by + 0.4], color=P.edge("plant"), lw=1.4, zorder=5)
for k, (dx, dy) in enumerate([(3.0, 2.4), (3.0, 1.0), (3.0, -0.4), (3.0, -1.8)]):
    ax.plot([bx + 1.4, bx + dx], [by + 0.4, by + dy], color=P.edge("plant"), lw=1.1, zorder=5)
    ax.add_patch(Ellipse((bx + dx + 0.05, by + dy), 0.3, 0.42, facecolor=P.fill("petal"), edgecolor=P.edge("petal"),
                         lw=0.8, zorder=6))
bio.callout(ax, (bx + 3.05, by + 2.4), (29.6, 11.0), "Adhesive pad", size="small")
bio.label(ax, (33.0, 0.5), "Wall", size="small")
bio.label(ax, (30.6, 2.6), r"$\it{Parthenocissus}$", size="small")
