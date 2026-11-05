# Floral organs of a water lily (Nymphaea). A: the flower (IAN symbol). B: organs removed from the outside
# inwards: a sepal (green outside), an outer and an inner petal, an outer stamen that is petal-like with
# pollen sacs only near the tip, and an inner stamen with a distinct filament and anther; there is no
# sharp boundary between perianth and androecium. C: cross-section of the syncarpous ovary with many
# locules separated by septa; the ovules are borne over the surfaces of the septa (laminar placentation).
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

P = bio.P
fig, ax = bio.canvas(32, 12)


def organ(cx, base, length, width, token, tip=0.0, anther=None):
    """A flat floral organ: outline from base to tip; ``anther`` = fraction of the length bearing pollen sacs."""
    t = np.linspace(0, 1, 60)
    half = width / 2 * np.sin(np.pi * np.clip(t, 0, 1) ** (0.8 - tip)) + width * 0.06
    xs = np.r_[cx + half, (cx - half)[::-1]]
    ys = np.r_[base + t * length, (base + t * length)[::-1]]
    ax.add_patch(Polygon(np.c_[xs, ys], closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.2,
                         zorder=5))
    ax.plot([cx, cx], [base + 0.1, base + length * 0.92], color=P.edge(token), lw=0.7, zorder=6)
    if anther:
        y0 = base + length * (1 - anther)
        for s in (-1, 1):
            ax.add_patch(Ellipse((cx + s * width * 0.16, y0 + length * anther / 2), width * 0.22, length * anther * 0.9,
                                 facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.0, zorder=7))


bio.panel(ax, "A", (0.3, 11.7))
bio.icon(ax, "ian/water-lily", at=(4.2, 6.0), height=5.0)
bio.label(ax, (4.2, 2.4), r"$\it{Nymphaea}$", size="title")

bio.panel(ax, "B", (8.4, 11.7))
SERIES = [("Sepal", 3.2, 1.7, "sepal", None), ("Outer petal", 3.4, 1.6, "petal", None),
          ("Inner petal", 3.1, 1.25, "petal", None), ("Outer stamen", 2.9, 0.9, "petal", 0.35),
          ("Inner stamen", 2.4, 0.45, "anther", 0.55)]
for i, (name, L, W, tok, an) in enumerate(SERIES):
    cx = 10.2 + i * 2.6
    if name == "Inner stamen":  # distinct filament and anther
        ax.add_patch(Polygon([(cx - 0.09, 4.0), (cx + 0.09, 4.0), (cx + 0.07, 6.6), (cx - 0.07, 6.6)], closed=True,
                             facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=1.0, zorder=5))
        for sx in (-1, 1):
            ax.add_patch(Ellipse((cx + sx * 0.14, 7.7), 0.3, 2.3, facecolor=P.fill("anther"), edgecolor=P.edge("anther"),
                                 lw=1.0, zorder=6))
    else:
        organ(cx, 4.0, L * 1.9, W, tok, anther=an)
    bio.label(ax, (cx, 3.3), name, size="small")
ax.annotate("", xy=(21.0, 2.4), xytext=(10.0, 2.4), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=1.1))
bio.label(ax, (15.5, 1.8), "outside  to  inside", size="small", color=P.muted())

bio.panel(ax, "C", (23.0, 11.7))
c = np.array([27.6, 6.6])
Rr = 3.6
ax.add_patch(Circle(c, Rr, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.4, zorder=4))
ax.add_patch(Circle(c, Rr * 0.86, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("ovary"), lw=0.9, zorder=5))
ax.add_patch(Circle(c, Rr * 0.2, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9, zorder=7))
N = 12
for k in range(N):
    a = 2 * math.pi * k / N
    u = np.array([math.cos(a), math.sin(a)])
    ax.plot(*zip(c + 0.2 * Rr * u, c + 0.86 * Rr * u), color=P.edge("ovary"), lw=1.8, zorder=6)
    for j, rr in enumerate(np.linspace(0.32, 0.78, 5)):
        for side in (-1, 1):
            v = np.array([-u[1], u[0]]) * side
            p = c + rr * Rr * u + 0.12 * v * (1 + rr)
            ax.add_patch(Ellipse(p, 0.2, 0.14, angle=math.degrees(a), facecolor=P.fill("ovule"),
                                 edgecolor=P.edge("ovule"), lw=0.5, zorder=8))
bio.callout(ax, c + 0.55 * Rr * np.array([math.cos(0.26), math.sin(0.26)]), (31.6, 10.8), "Septum with ovules",
            size="small")
bio.callout(ax, c + 0.93 * Rr * np.array([0.0, -1.0]), (31.0, 2.0), "Ovary wall", size="small")
bio.label(ax, (27.6, 1.4), "Laminar placentation", size="small")
