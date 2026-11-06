# Caryophyllaceae. A: floral diagram of Dianthus (connate calyx, five clawed petals, ten stamens in two
# whorls, two carpels, one locule with free-central placentation). B: Stellaria (free sepals, five
# bifid petals, ten stamens, three carpels). C: Dianthus flower in longitudinal section (epicalyx-like
# bracts below the calyx tube, long-clawed petals, free-central placenta with many ovules).
# D: a dichasium (two-branched cyme): the terminal flower opens first, numbers give the order.
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 13)

bio.panel(ax, "A", (0.3, 12.8))
bio.label(ax, (4.4, 12.2), "Dianthus", italic=True, size="title")
plant.floral_diagram(ax, (4.4, 6.9), 2.8, [
    dict(organ="sepal", n=5, phase=0, connate=True, r=1.0, width=34),
    dict(organ="petal", n=5, r=0.82, width=30),
    dict(organ="stamen", n=5, r=0.62), dict(organ="stamen", n=5, r=0.5),
    dict(organ="gynoecium", n=2, placentation="free-central", ovules=6, size=0.28)], symmetry="radial")
plant.floral_formula(ax, (4.4, 1.4), "* K(5) C5 A5+5 G_(2:1:∞)", style="cn", size="normal")

bio.panel(ax, "B", (9.2, 12.8))
bio.label(ax, (13.2, 12.2), "Stellaria", italic=True, size="title")
pet = [dict(), dict(), dict(), dict(), dict()]
plant.floral_diagram(ax, (13.2, 6.9), 2.8, [
    dict(organ="sepal", n=5, phase=0, r=1.0, width=30),
    dict(organ="petal", n=5, phase=36 - 8, r=0.82, width=7), dict(organ="petal", n=5, phase=36 + 8, r=0.82, width=7),
    dict(organ="stamen", n=5, phase=0, r=0.62), dict(organ="stamen", n=5, phase=36, r=0.5),
    dict(organ="gynoecium", n=3, placentation="free-central", ovules=6, size=0.28)], symmetry="radial")
plant.floral_formula(ax, (13.2, 1.4), "* K5 C5 A5+5 G_(3:1:∞)", style="cn", size="normal")
bio.label(ax, (13.2, 0.4), "each petal deeply bifid", size="tiny")

# C: longitudinal section of Dianthus
bio.panel(ax, "C", (18.0, 12.8))
cx = 22.0
ax.plot([cx, cx], [0.6, 2.0], color=P.edge("plant"), lw=2.0, zorder=3)
for s in (-1, 1):
    bio.shape(ax, [(cx + s * 0.2, 1.9), (cx + s * 0.55, 2.0), (cx + s * 0.95, 3.0), (cx + s * 0.75, 3.05)], token="bract", lw=0.8, zorder=6)
    bio.shape(ax, [(cx + s * 0.5, 2.0), (cx + s * 0.75, 2.0), (cx + s * 0.85, 6.6), (cx + s * 0.62, 6.7)], token="sepal", lw=0.9, zorder=6)
    # petal: claw inside the calyx tube, limb at right angle
    bio.shape(ax, [(cx + s * 0.28, 2.3), (cx + s * 0.4, 2.3), (cx + s * 0.5, 6.9), (cx + s * 3.2, 7.4), (cx + s * 3.3, 7.9),
                   (cx + s * 0.42, 7.3)], token="petal", lw=0.9, zorder=5)
    for k in range(4):
        ax.plot([cx + s * (3.3 - 0.6 * k), cx + s * (3.1 - 0.6 * k)], [7.9 - 0.1 * k, 8.15 - 0.1 * k], color=P.edge("petal"), lw=0.7, zorder=6)
    for h in (6.2, 7.0):
        ax.plot([cx + s * 0.15, cx + s * 0.3], [2.4, h], color=P.edge("anther"), lw=0.8, zorder=4)
        ax.add_patch(Ellipse((cx + s * 0.3, h + 0.15), 0.18, 0.35, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.5, zorder=5))
bio.shape(ax, [(cx - 0.28, 2.2), (cx + 0.28, 2.2), (cx + 0.25, 4.2), (cx - 0.25, 4.2)], token="ovary", lw=0.9, zorder=7)
ax.plot([cx, cx], [2.3, 4.0], color=P.edge("ovary"), lw=1.6, zorder=8)
for y in np.linspace(2.6, 3.8, 4):
    for s in (-1, 1):
        ax.add_patch(Circle((cx + s * 0.12, y), 0.07, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.4, zorder=9))
for s in (-1, 1):
    ax.plot([cx + s * 0.05, cx + s * 0.35], [4.2, 7.6], color=P.edge("ovary"), lw=1.0, zorder=7)
bio.callout(ax, (cx + 3.0, 7.6), (26.6, 10.6), "Petal limb (fringed)")
bio.callout(ax, (cx + 0.44, 5.0), (26.6, 5.6), "Claw")
bio.callout(ax, (cx + 0.8, 5.5), (26.6, 7.0), "Calyx tube")
bio.callout(ax, (cx - 0.85, 2.7), (18.4, 3.4), "Bracts")
bio.callout(ax, (cx, 3.4), (26.6, 2.6), "Free-central placenta")
bio.callout(ax, (cx - 0.3, 7.0), (18.4, 9.0), "Stamens (10)")
bio.callout(ax, (cx - 0.35, 7.6), (18.4, 10.6), "Styles (2)")

# D: dichasium
bio.panel(ax, "D", (28.4, 12.8))


def dich(p, level, length, order):
    bio.label(ax, (p[0], p[1] + 0.55), str(order), size="tiny")
    ax.add_patch(Circle(p, 0.32, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=0.8, zorder=6))
    if level == 0:
        return
    for s in (-1, 1):
        q = (p[0] + s * length, p[1] - length * 1.15)
        ax.plot([p[0], q[0]], [p[1] - 0.3, q[1]], color=P.edge("plant"), lw=1.2, zorder=4)
        dich(q, level - 1, length * 0.5, order + 1)


ax.plot([32.2, 32.2], [0.8, 8.8], color=P.edge("plant"), lw=1.4, zorder=4)
dich((32.2, 9.4), 3, 1.9, 1)
bio.label(ax, (32.2, 0.3), "dichasium", size="small")
