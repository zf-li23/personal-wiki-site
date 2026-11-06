# The two large subfamilies of Papaveraceae. A: floral diagram of Papaver (Papaveroideae): two caducous
# sepals, four petals in two whorls, many stamens, a syncarpous one-locular ovary with parietal placentas
# under a radiating stigmatic disc. B: poricidal capsule of Papaver (pores under the stigmatic disc).
# C: floral diagram of Corydalis (Fumarioideae): zygomorphic, one outer petal spurred, six stamens in two
# bundles (one entire and two half stamens each), two carpels. D: Corydalis flower in side view, spur
# pointing backwards. E: Lamprocapnos (Dicentra), disymmetric: both outer petals pouched at the base.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(34, 13)
Y = 7.2

bio.panel(ax, "A", (0.3, 12.8))
bio.label(ax, (4.0, 12.3), "Papaver", size="title", italic=True)
plant.floral_diagram(ax, (4.0, Y), 2.8, [
    dict(organ="sepal", n=2, phase=0, width=60),
    dict(organ="petal", n=2, phase=90, width=55, r=0.8),
    dict(organ="petal", n=2, phase=0, width=50, r=0.7),
    dict(organ="stamen", n=14, r=0.55), dict(organ="stamen", n=14, r=0.46, phase=13),
    dict(organ="gynoecium", n=8, placentation="parietal", ovules=2, size=0.3)], symmetry="radial")
plant.floral_formula(ax, (4.0, 2.4), "* K2 C2+2 A∞ G_(8:1:∞)", style="cn", size="normal")
bio.label(ax, (4.0, 1.4), "sepals 2, caducous", size="small", color=P.muted())

# B: poricidal capsule
bio.panel(ax, "B", (8.6, 12.8))
cx, cy = 11.0, 6.6
ax.add_patch(Ellipse((cx, cy), 2.6, 3.4, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.2, zorder=5))
disc = [(cx + 1.6 * math.cos(a), cy + 1.75 + 0.35 * math.sin(a)) for a in np.linspace(0, 2 * math.pi, 40)]
ax.add_patch(Polygon(disc, closed=True, facecolor=P.light("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
for a in np.linspace(0, math.pi, 7)[1:-1]:
    ax.plot([cx, cx + 1.5 * math.cos(a)], [cy + 1.8, cy + 1.75 + 0.3 * math.sin(a)], color=P.edge("ovary"),
            lw=0.8, zorder=7)
for x in np.linspace(cx - 0.9, cx + 0.9, 5):
    ax.add_patch(Ellipse((x, cy + 1.3), 0.22, 0.14, facecolor=P.ink(), edgecolor="none", zorder=7))
ax.plot([cx, cx], [cy - 1.7, cy - 3.2], color=P.edge("plant"), lw=3, zorder=4)
for k in range(5):
    ax.add_patch(Ellipse((cx + 1.9 + 0.25 * k, cy + 0.9 - 0.45 * k), 0.12, 0.12, facecolor=P.muted(),
                         edgecolor="none", zorder=7))
bio.callout(ax, (cx + 1.2, cy + 1.85), (cx + 1.4, cy + 3.6), "Stigmatic disc", size="small")
bio.callout(ax, (cx + 0.9, cy + 1.3), (cx + 2.6, cy + 2.4), "Pores", size="small")
bio.label(ax, (cx, 1.9), "Capsule opening by pores", size="small")

bio.panel(ax, "C", (15.4, 12.8))
bio.label(ax, (19.0, 12.3), "Corydalis", size="title", italic=True)
plant.floral_diagram(ax, (19.0, Y), 2.8, [
    dict(organ="sepal", n=2, phase=90, width=25, r=0.98),
    dict(organ="petal", n=2, phase=0, width=60, r=0.86, members=[dict(scale=1.25), dict()]),
    dict(organ="petal", n=2, phase=90, width=40, r=0.7),
    dict(organ="stamen", n=6, phase=60, r=0.5, connate=[(0, 1), (1, 2), (3, 4), (4, 5)],
         members=[dict(scale=0.6), dict(), dict(scale=0.6), dict(scale=0.6), dict(), dict(scale=0.6)]),
    dict(organ="gynoecium", n=2, placentation="parietal", ovules=3, size=0.22)], symmetry="bilateral")
plant.floral_formula(ax, (19.0, 2.4), "↑ K2 C2+2 A(3)+(3) G_(2:1:∞)", style="cn", size="normal")
bio.label(ax, (19.0, 1.4), "upper outer petal spurred; stamens in 2 bundles", size="small", color=P.muted())


def side_flower(x0, y0, spurs, title, letter):
    bio.panel(ax, letter, (x0 - 2.2, 12.8))
    bio.label(ax, (x0 + 0.6, 12.3), title, size="title", italic=True)
    ax.plot([x0 + 0.6, x0 + 0.6], [y0 + 2.6, y0 + 0.62], color=P.edge("plant"), lw=2.0, zorder=3)
    body = [(x0, y0 + 0.6), (x0 + 2.6, y0 + 0.9), (x0 + 3.4, y0 + 0.2), (x0 + 2.6, y0 - 0.5), (x0, y0 - 0.3)]
    ax.add_patch(Polygon(body, closed=True, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=1.2,
                         zorder=5, joinstyle="round"))
    ax.add_patch(Ellipse((x0 + 3.1, y0 + 0.2), 0.7, 0.55, facecolor=P.light("petal"), edgecolor=P.edge("petal"),
                         lw=1.0, zorder=6))
    for s in spurs:
        sp = [(x0 + 0.1, y0 + 0.2 + 0.4 * s), (x0 - 1.6, y0 + 0.7 * s), (x0 - 1.4, y0 + 0.15 * s), (x0 + 0.1, y0 - 0.05 + 0.1 * s)]
        ax.add_patch(Polygon(sp, closed=True, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=1.2,
                             zorder=5, joinstyle="round"))
    return body


side_flower(25.4, 8.6, [1], "Corydalis", "D")
bio.callout(ax, (24.0, 9.2), (23.4, 10.8), "Spur (nectar)", size="small")
bio.callout(ax, (28.5, 8.8), (29.4, 10.6), "Inner petals enclose stamens", size="small")

bio.panel(ax, "E", (23.2, 5.6))
bio.label(ax, (27.6, 5.3), "Lamprocapnos", size="title", italic=True)
ex, ey = 27.6, 2.6
heart = [(ex + 1.6 * math.sin(t) ** 3, ey + 1.3 * math.cos(t) - 0.5 * math.cos(2 * t) - 0.2 * math.cos(3 * t))
         for t in np.linspace(0, 2 * math.pi, 80)]
ax.add_patch(Polygon(heart, closed=True, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=1.2, zorder=5))
ax.add_patch(Polygon([(ex - 0.3, ey - 1.2), (ex + 0.3, ey - 1.2), (ex + 0.2, ey - 2.2), (ex - 0.2, ey - 2.2)],
                     closed=True, facecolor=P.light("petal"), edgecolor=P.edge("petal"), lw=1.0, zorder=6))
ax.plot([ex, ex], [ey + 0.9, ey + 2.2], color=P.edge("plant"), lw=1.5, zorder=4)
bio.callout(ax, (ex - 1.4, ey + 0.4), (ex - 3.6, ey + 1.6), "Two pouched outer petals", size="small")
bio.callout(ax, (ex + 0.2, ey - 1.9), (ex + 2.4, ey - 1.9), "Inner petals", size="small")
