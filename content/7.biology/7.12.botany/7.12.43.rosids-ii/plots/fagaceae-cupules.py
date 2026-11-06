# Cupules and nuts of Fagaceae (schematic). A: Fagus, a four-valved cupule with two triangular nuts.
# B: Castanea, a fully enclosing spiny cupule opening by four valves, two or three nuts. C: Castanopsis,
# a spiny cupule. D: Lithocarpus, a saucer-shaped cupule with imbricate scales and one nut. E:
# Cyclobalanopsis, a cup with scales fused into concentric rings. F: Quercus, a cup of imbricate scales
# half enclosing the acorn, and the long recurved scales of Q. acutissima. Bottom: male catkins erect in
# Castanea, pendulous in Quercus.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(36, 13)
XS = [3.0, 9.0, 15.0, 21.0, 27.0, 33.0]
Y = 7.0
NUT, CUP = "anther", "plant"


def nut(c, w, h, tri=False, z=6):
    if tri:
        pts = [(c[0], c[1] + h / 2), (c[0] + w / 2, c[1] - h / 2), (c[0] - w / 2, c[1] - h / 2)]
        ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(NUT), edgecolor=P.edge(NUT), lw=1.0, zorder=z,
                             joinstyle="round"))
    else:
        ax.add_patch(Ellipse(c, w, h, facecolor=P.fill(NUT), edgecolor=P.edge(NUT), lw=1.0, zorder=z))


def spines(c, rx, ry, n=40, L=0.35):
    for a in np.linspace(0, 2 * math.pi, n, endpoint=False):
        p = np.array([c[0] + rx * math.cos(a), c[1] + ry * math.sin(a)])
        q = p + L * np.array([math.cos(a), math.sin(a)])
        ax.plot(*zip(p, q), color=P.edge(CUP), lw=0.7, zorder=4)


names = ["Fagus", "Castanea", "Castanopsis", "Lithocarpus", "Cyclobalanopsis", "Quercus"]
for i, n in enumerate(names):
    bio.panel(ax, "ABCDEF"[i], (XS[i] - 2.6, 12.8))
    bio.label(ax, (XS[i], 12.3), n, size="title", italic=True)
# A Fagus
x = XS[0]
for s in (-1, 1):
    ax.add_patch(Polygon([(x, Y - 1.2), (x + s * 1.9, Y + 0.3), (x + s * 1.5, Y + 0.9), (x + s * 0.2, Y - 0.5)],
                         closed=True, facecolor=P.fill(CUP), edgecolor=P.edge(CUP), lw=1.0, zorder=4))
nut((x - 0.45, Y + 0.4), 0.8, 1.5, tri=True); nut((x + 0.45, Y + 0.4), 0.8, 1.5, tri=True)
bio.label(ax, (x, 4.4), "4 valves; 2 trigonous nuts", size="small")
# B Castanea
x = XS[1]
ax.add_patch(Ellipse((x, Y), 3.0, 2.6, facecolor=P.fill(CUP), edgecolor=P.edge(CUP), lw=1.0, zorder=3))
spines((x, Y), 1.5, 1.3, n=48, L=0.5)
for dx in (-0.7, 0, 0.7):
    nut((x + dx, Y + 0.1), 0.75, 1.0)
bio.label(ax, (x, 4.4), "Spiny, enclosing; 1-3 nuts", size="small")
# C Castanopsis
x = XS[2]
ax.add_patch(Ellipse((x, Y - 0.2), 2.2, 2.0, facecolor=P.fill(CUP), edgecolor=P.edge(CUP), lw=1.0, zorder=3))
spines((x, Y - 0.2), 1.1, 1.0, n=30, L=0.35)
nut((x, Y + 0.6), 0.9, 1.3)
bio.label(ax, (x, 4.4), "Spiny; nut partly exposed", size="small")
# D Lithocarpus
x = XS[3]
nut((x, Y + 0.6), 1.3, 1.7)
ax.add_patch(Ellipse((x, Y - 0.3), 2.0, 0.8, facecolor=P.fill(CUP), edgecolor=P.edge(CUP), lw=1.0, zorder=7))
for k in range(7):
    ax.add_patch(Ellipse((x - 0.75 + 0.25 * k, Y - 0.3), 0.3, 0.25, facecolor=P.light(CUP), edgecolor=P.edge(CUP),
                         lw=0.6, zorder=8))
bio.label(ax, (x, 4.4), "Saucer, imbricate scales; 1 nut", size="small")
# E Cyclobalanopsis
x = XS[4]
nut((x, Y + 0.6), 1.1, 1.9)
ax.add_patch(Polygon([(x - 1.0, Y + 0.2), (x - 0.8, Y - 0.8), (x + 0.8, Y - 0.8), (x + 1.0, Y + 0.2)], closed=True,
                     facecolor=P.fill(CUP), edgecolor=P.edge(CUP), lw=1.0, zorder=7))
for y in (Y - 0.5, Y - 0.2, Y + 0.05):
    ax.plot([x - 0.92, x + 0.92], [y, y], color=P.edge(CUP), lw=0.9, zorder=8)
bio.label(ax, (x, 4.4), "Scales in concentric rings", size="small")
# F Quercus
x = XS[5]
nut((x - 0.5, Y + 0.6), 1.0, 1.7)
ax.add_patch(Polygon([(x - 1.35, Y + 0.3), (x - 1.15, Y - 0.6), (x + 0.15, Y - 0.6), (x + 0.35, Y + 0.3)], closed=True,
                     facecolor=P.fill(CUP), edgecolor=P.edge(CUP), lw=1.0, zorder=7))
for k in range(6):
    for j in range(2):
        ax.add_patch(Ellipse((x - 1.1 + 0.25 * k, Y - 0.35 + 0.35 * j), 0.28, 0.22, facecolor=P.light(CUP),
                             edgecolor=P.edge(CUP), lw=0.5, zorder=8))
nut((x + 1.2, Y + 0.6), 0.9, 1.5)
ax.add_patch(Polygon([(x + 0.6, Y - 0.6), (x + 1.8, Y - 0.6), (x + 2.0, Y + 0.3), (x + 0.4, Y + 0.3)], closed=True,
                     facecolor=P.fill(CUP), edgecolor=P.edge(CUP), lw=1.0, zorder=7))
for k in range(6):
    a = math.radians(30 + 20 * k)
    p = (x + 0.6 + 0.25 * k, Y + 0.2)
    ax.plot([p[0], p[0] + 0.5 * math.cos(a)], [p[1], p[1] + 0.6], color=P.edge(CUP), lw=1.0, zorder=8)
bio.label(ax, (x, 4.4), "Imbricate cup; Q. acutissima (right)", size="small")
# catkins
for xc, up, lab in [(9.0, True, "Castanea: male catkins erect"), (33.0, False, "Quercus: male catkins pendulous")]:
    yb = 0.8 if up else 3.6
    ax.plot([xc - 2.4, xc + 2.4], [yb if up else yb + 0.2] * 2, color=P.edge("plant"), lw=2.0, zorder=4)
    for k in range(3):
        xs = xc - 0.9 + 0.9 * k
        pts = [(xs + 0.12 * math.sin(s * 3), yb + (s * 1.9 if up else -s * 1.9)) for s in np.linspace(0, 1, 20)]
        ax.plot(*zip(*pts), color=P.edge("plant"), lw=0.8, zorder=4)
        for q in pts[3::2]:
            ax.add_patch(Ellipse(q, 0.25, 0.18, facecolor=P.fill(NUT), edgecolor=P.edge(NUT), lw=0.5, zorder=5))
    bio.label(ax, (xc - 2.6, yb + (1.0 if up else -1.0)), lab, size="small", ha="right")
