# Growth habits and branching. Left: erect stem; twining stems around a support (morning glory type:
# anticlockwise seen from above, a right-handed helix, Chinese "left-twining"; honeysuckle type:
# clockwise, a left-handed helix, "right-twining"; strands in front of the support solid, behind faded);
# a climber holding on with tendrils; a creeping stem rooting at the nodes. Right: branching patterns as
# module diagrams (wikibio.botany): monopodial, sympodial, false dichotomy (dichasial) and dichotomy.
import numpy as np
from matplotlib.patches import Polygon, Rectangle

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(34.4, 14.0)
G = 1.4  # ground line
ax.plot([0.4, 15.6], [G, G], color=P.edge("animal"), lw=1.0)
ST = P.edge("plant")


def leaf(x, y, sg, s=0.45):
    pts = bio.smooth_closed([(x, y), (x + sg * s * 0.6, y + s * 0.35), (x + sg * s * 1.2, y + s * 0.15),
                             (x + sg * s * 0.6, y - s * 0.15)], n=40)
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("plant"), edgecolor=ST, lw=0.6, zorder=7))


bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (0.85, 13.77), "Growth habits", size="title", ha="left", va="top")
# erect
ax.plot([1.6, 1.6], [G, 10.5], color=ST, lw=2.2, zorder=5)
for k, y in enumerate(np.arange(2.5, 10.0, 1.4)):
    leaf(1.6, y, 1 if k % 2 else -1)
bio.label(ax, (1.6, 0.8), "Erect", size="small")


def twiner(x, handed, label):
    ax.add_patch(Rectangle((x - 0.12, G), 0.24, 9.6, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.6, zorder=4))
    t = np.linspace(0, 6 * np.pi, 600)
    r = 0.55
    xs = x + r * np.cos(t)
    zs = -handed * r * np.sin(t)  # handed = +1: right-handed helix (front strands run "/")
    ys = G + 0.2 + t / (6 * np.pi) * 9.0
    front = zs > 0
    for mask, alpha, z in ((~front, 0.35, 3.5), (front, 1.0, 6)):
        seg = np.where(mask, ys, np.nan)
        ax.plot(xs, seg, color=ST, lw=2.0, alpha=alpha if alpha < 1 else None, zorder=z)
    for k in range(5):
        i = int(60 + k * 110)
        if front[i]:
            leaf(xs[i], ys[i], 1 if np.cos(t[i]) > 0 else -1, 0.4)
    bio.label(ax, (x, 0.8), label, size="small")


twiner(4.6, +1, "Twining (morning glory)")
twiner(8.0, -1, "Twining (honeysuckle)")
for x, txt in ((4.6, "anticlockwise\nfrom above"), (8.0, "clockwise\nfrom above")):
    bio.label(ax, (x, 11.8), txt, size="tiny", color=P.muted())
# climber with tendrils on a trellis
for yy in (3.5, 6.0, 8.5):
    ax.plot([10.2, 12.4], [yy, yy], color=P.edge("animal"), lw=1.2, zorder=3)
stem = np.c_[11.3 + 0.25 * np.sin(np.linspace(0, 5, 50)), np.linspace(G, 10.0, 50)]
ax.plot(stem[:, 0], stem[:, 1], color=ST, lw=2.0, zorder=5)
for yy in (3.5, 6.0, 8.5):
    i = int((yy - 0.5 - G) / (10.0 - G) * 49)
    p = stem[i]
    th = np.linspace(0, 4 * np.pi, 80)
    coil = np.c_[p[0] + 0.15 + np.linspace(0, 0.6, 80) + 0.12 * np.cos(th), yy + 0.1 * np.sin(th) + np.linspace(-0.4, 0, 80)]
    ax.plot(coil[:, 0], coil[:, 1], color=ST, lw=1.0, zorder=6)
    leaf(p[0], p[1] + 0.2, -1, 0.5)
bio.label(ax, (11.3, 0.8), "Climbing (tendrils)", size="small")
# creeping stem with adventitious roots at nodes
ax.plot([12.8, 15.4], [G + 0.12, G + 0.12], color=ST, lw=2.0, zorder=5)
for xn in (13.2, 14.4, 15.3):
    for d in (-0.15, 0.0, 0.15):
        ax.plot([xn, xn + d], [G, G - 0.5], color=P.edge("bone"), lw=0.8, zorder=4)
    leaf(xn, G + 0.15, 1, 0.35)
    leaf(xn, G + 0.15, -1, 0.35)
bio.label(ax, (14.2, 0.8), "Creeping", size="small")

bio.panel(ax, "B", (16.6, 13.8))
bio.label(ax, (17.25, 13.77), "Branching patterns", size="title", ha="left", va="top")
for k, (kind, name) in enumerate((("monopodial", "Monopodial"), ("sympodial", "Sympodial"), ("dichasial", "False dichotomy"),
                                  ("dichotomous", "Dichotomy"))):
    x = 18.4 + k * 4.1
    B.branching(ax, (x, 1.6), 6.4, kind=kind)
    bio.label(ax, (x, 0.8), name, size="small")
