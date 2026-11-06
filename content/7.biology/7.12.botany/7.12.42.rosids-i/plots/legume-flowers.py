# Legume flowers. A: dissected papilionaceous flower of the pea: whole flower in side view, standard,
# two wings, the two connate keel petals, and diadelphous stamens (nine filaments fused into a tube, the
# adaxial one free) around the single carpel. B-D: floral diagrams and formulae of the three flower types:
# B mimosoid (actinomorphic, valvate connate petals, many stamens drawn as two whorls); C Cercis
# (pseudopapilionaceous, the adaxial petal innermost, ten free stamens); D papilionoid (the standard
# outermost, odd sepal abaxial, diadelphous stamens).
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 15)


def petal(c, w, h, ang=0, tok="petal", z=5):
    t = np.linspace(0, 2 * math.pi, 80)
    x, y = w / 2 * np.cos(t), h / 2 * np.sin(t) * (1 - 0.35 * np.sin(t))
    a = math.radians(ang)
    pts = np.c_[c[0] + x * math.cos(a) - y * math.sin(a), c[1] + x * math.sin(a) + y * math.cos(a)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=z))


bio.panel(ax, "A", (0.3, 14.8))
bio.label(ax, (9.0, 14.4), r"$\it{Pisum\ sativum}$: papilionaceous flower", size="title")
# whole flower
petal((2.6, 10.6), 2.6, 3.2, ang=-15)
petal((3.3, 9.0), 2.4, 1.0, ang=-20, tok="petal")
petal((3.6, 8.5), 2.2, 0.8, ang=-25, tok="ovary")
ax.add_patch(Polygon([(1.4, 8.3), (2.4, 8.9), (2.0, 7.9)], closed=True, facecolor=P.fill("sepal"),
                     edgecolor=P.edge("sepal"), lw=1.0, zorder=6))
ax.plot([1.4, 0.9], [8.3, 7.6], color=P.edge("plant"), lw=1.6)
bio.label(ax, (3.2, 7.4), "Flower (side)", size="small")
petal((7.3, 10.2), 3.0, 3.4)
bio.label(ax, (7.3, 7.9), "Standard (1)", size="small")
petal((10.6, 10.6), 1.2, 2.6, ang=10)
petal((11.9, 10.6), 1.2, 2.6, ang=-10)
bio.label(ax, (11.2, 7.9), "Wings (2)", size="small")
keel = [(14.0, 11.6), (15.6, 11.4), (16.4, 10.0), (15.6, 9.2), (14.4, 9.6)]
ax.add_patch(Polygon(keel, closed=True, facecolor=P.light("petal"), edgecolor=P.edge("petal"), lw=1.1, zorder=5))
ax.plot([14.2, 16.0], [10.9, 9.7], color=P.edge("petal"), lw=0.8, ls=(0, (2, 2)), zorder=6)
bio.label(ax, (15.2, 7.9), "Keel (2 connate)", size="small")
# stamens
sx = 19.5
ax.add_patch(Polygon([(sx, 9.0), (sx + 3.0, 9.2), (sx + 3.0, 9.9), (sx, 9.8)], closed=True,
                     facecolor=P.light("anther"), edgecolor=P.edge("anther"), lw=1.0, zorder=5))
for k in range(9):
    x = sx + 3.0 + 0.2 * k
    ax.plot([sx + 3.0, x + 0.4], [9.5, 10.4 + 0.15 * k], color=P.edge("anther"), lw=0.8, zorder=6)
    ax.add_patch(Ellipse((x + 0.45, 10.5 + 0.15 * k), 0.28, 0.16, facecolor=P.fill("anther"), edgecolor=P.edge("anther"),
                         lw=0.6, zorder=7))
ax.plot([sx + 0.2, sx + 4.8], [10.3, 11.2], color=P.edge("anther"), lw=0.9, zorder=6)
ax.add_patch(Ellipse((sx + 4.95, 11.25), 0.28, 0.16, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6))
ax.plot([sx - 0.2, sx + 4.6], [9.45, 9.0], color=P.edge("ovary"), lw=2.0, zorder=4)
bio.callout(ax, (sx + 2.5, 10.75), (sx + 6.2, 12.6), "Free (vexillary) stamen", size="small")
bio.callout(ax, (sx + 1.4, 9.4), (sx + 6.2, 8.2), "Staminal tube (9 fused)", size="small")
bio.callout(ax, (sx + 4.6, 9.0), (sx + 6.2, 7.0), "Style of single carpel", size="small")

# B-D diagrams
specs = [("B", "Mimosoid clade", "* K(5) C(5) A∞ G_1:1:∞"),
         ("C", "Cercis", "↑ K5 C5 A10 G_1:1:∞"),
         ("D", "Papilionoideae", "↑ K(5) C1+2+(2) A(9)+1 G_1:1:∞")]
XS = [5.0, 17.0, 29.0]
Y = 3.6
for i, (L, name, f) in enumerate(specs):
    bio.panel(ax, L, (XS[i] - 4.6, 6.6))
    bio.label(ax, (XS[i] + 3.4, 5.0), name, size="normal", italic=(name == "Cercis"), ha="left")
    plant.floral_formula(ax, (XS[i] + 3.4, 3.6), f, style="cn", size="normal", ha="left")
plant.floral_diagram(ax, (XS[0], Y), 2.3, [
    dict(organ="sepal", n=5, phase=180, connate=True, width=30),
    dict(organ="petal", n=5, connate=True, width=34, r=0.8),
    dict(organ="stamen", n=10, r=0.58), dict(organ="stamen", n=10, r=0.46, phase=18),
    dict(organ="gynoecium", n=1, placentation="marginal", ovules=2, size=0.22)], symmetry="radial")
plant.floral_diagram(ax, (XS[1], Y), 2.3, [
    dict(organ="sepal", n=5, phase=180, width=30),
    dict(organ="petal", n=5, phase=0, r=0.78, members=[dict(scale=0.7, r=0.62), dict(scale=1.1), dict(scale=1.2, r=0.82),
                                                        dict(scale=1.2, r=0.82), dict(scale=1.1)]),
    dict(organ="stamen", n=5, phase=36, r=0.5), dict(organ="stamen", n=5, phase=0, r=0.42),
    dict(organ="gynoecium", n=1, placentation="marginal", ovules=2, size=0.2)], symmetry="bilateral")
plant.floral_diagram(ax, (XS[2], Y), 2.3, [
    dict(organ="sepal", n=5, phase=180, connate=True, width=30),
    dict(organ="petal", n=5, phase=216, r=0.74, members=[
        dict(scale=0.9, r=0.66), dict(scale=1.05, r=0.74), dict(scale=1.45, width=44, r=0.8),
        dict(scale=1.05, r=0.74), dict(scale=0.9, r=0.66)], connate=[(4, 0)]),
    dict(organ="stamen", n=10, phase=0, r=0.47, size=0.12, connate=True, free=[0]),
    dict(organ="gynoecium", n=1, placentation="marginal", phase=0, ovules=2, size=0.22)], symmetry="bilateral")
