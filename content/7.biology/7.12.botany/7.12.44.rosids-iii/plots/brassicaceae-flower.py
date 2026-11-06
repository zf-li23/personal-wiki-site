# Brassicaceae flower and fruits. A: floral diagram (sepals 2 + 2, cruciform petals, tetradynamous
# stamens, two carpels with parietal placentation divided by the false septum). B: a dehiscing silique:
# the two valves fall away from below, the seeds stay on the replum and false septum, beak at the top.
# C: silique cross-section. D: a silicle of Capsella (obcordate, laterally compressed). E: the three
# positions of radicle and cotyledons in the seed (accumbent, incumbent, conduplicate).
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 13)

# ---------------- A
bio.panel(ax, "A", (0.3, 12.8))
plant.floral_diagram(ax, (4.4, 7.0), 2.9, [
    dict(organ="sepal", n=2, phase=0, width=40, r=0.98),
    dict(organ="sepal", n=2, phase=90, width=40, r=0.9),
    dict(organ="petal", n=4, phase=45, width=30, r=0.78),
    dict(organ="stamen", n=2, phase=90, r=0.56, size=0.11),
    dict(organ="stamen", n=2, phase=-22, r=0.44, size=0.12),
    dict(organ="stamen", n=2, phase=22, r=0.44, size=0.12),
    dict(organ="gynoecium", n=2, placentation="parietal", ovules=2, size=0.24, phase=90),
], symmetry="radial")
plant.floral_formula(ax, (4.4, 1.6), "* K2+2 C4 A2+4 G_(2:2:∞)", style="cn")

# ---------------- B: dehiscing silique
bio.panel(ax, "B", (9.4, 12.8))
x0, yb, yt = 12.0, 1.4, 10.4
ax.plot([x0, x0], [yb - 0.8, yb], color=P.edge("plant"), lw=2.0, zorder=5)  # pedicel
# replum frame (two rims) and septum
bio.shape(ax, [(x0 - 0.42, yb), (x0 + 0.42, yb), (x0 + 0.42, yt), (x0 - 0.42, yt)], token="neutral", lw=0.6, zorder=4)
for s in (-1, 1):
    ax.plot([x0 + s * 0.42, x0 + s * 0.42], [yb, yt], color=P.edge("plant"), lw=1.8, zorder=6)
for y in np.linspace(yb + 0.6, yt - 0.6, 9):
    for s in (-1, 1):
        ax.add_patch(Circle((x0 + s * 0.2, y), 0.17, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.6, zorder=7))
bio.shape(ax, [(x0 - 0.3, yt), (x0 + 0.3, yt), (x0 + 0.1, yt + 1.3), (x0 - 0.1, yt + 1.3)], token="plant", lw=0.9)  # beak
# valves peeling off from the base
for s in (-1, 1):
    t = np.linspace(0, 1, 40)
    xs = x0 + s * (0.5 + 1.6 * (1 - t) ** 2)
    ys = yb + 0.3 + (yt - yb - 0.4) * t
    pts = np.vstack([np.c_[xs, ys], np.c_[xs[::-1] + s * 0.38, ys[::-1]]])
    bio.shape(ax, pts, token="plant", lw=1.0, zorder=5)
bio.callout(ax, (x0, yt + 0.9), (15.0, 11.6), "Beak")
bio.callout(ax, (x0 + 0.42, 7.5), (15.0, 8.8), "Replum")
bio.callout(ax, (x0, 6.2), (15.0, 6.4), "False septum")
bio.callout(ax, (x0 - 0.2, 3.5), (15.0, 4.1), "Seed")
bio.callout(ax, (x0 + 1.5, 2.4), (15.0, 1.8), "Valve")

# ---------------- C: cross-section
bio.panel(ax, "C", (17.6, 12.8))
c = np.array([20.4, 7.4])
ax.add_patch(Ellipse(c, 4.4, 2.6, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.2, zorder=4))
for s in (-1, 1):
    ax.add_patch(Ellipse(c + np.array([0, s * 0.62]), 3.7, 1.0, facecolor=P.surface(), edgecolor=P.edge("plant"), lw=0.6, zorder=5))
ax.plot([c[0] - 1.9, c[0] + 1.9], [c[1], c[1]], color=P.edge("neutral"), lw=1.0, zorder=6)
for s in (-1, 1):
    ax.add_patch(Circle(c + np.array([s * 2.0, 0]), 0.3, facecolor=P.fill("neutral"), edgecolor=P.edge("plant"), lw=1.0, zorder=7))
    for d in (-1, 1):
        ax.add_patch(Circle(c + np.array([s * 1.45, d * 0.45]), 0.25, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.6, zorder=7))
bio.callout(ax, c + np.array([0, 1.15]), (20.4, 10.4), "Valve")
bio.callout(ax, c + np.array([2.0, 0]), (23.0, 5.0), "Replum (placenta)")
bio.callout(ax, c + np.array([0.2, 0]), (19.0, 4.4), "False septum")

# ---------------- D: silicle of Capsella
bio.panel(ax, "D", (24.6, 12.8))
cx = 27.0
t = np.linspace(-1, 1, 80)
right = np.c_[cx + 1.8 * np.sin(np.pi / 2 * (t + 1) / 2) * (1 + 0.1 * t), 4.0 + 3.6 * (t + 1) / 2]
pts = np.vstack([[(cx, 4.0)], np.c_[cx + 0.15 + 1.9 * ((t + 1) / 2) ** 0.8, 4.0 + 3.4 * ((t + 1) / 2)],
                 [(cx + 0.9, 7.6), (cx, 7.0), (cx - 0.9, 7.6)],
                 np.c_[cx - 0.15 - 1.9 * ((t[::-1] + 1) / 2) ** 0.8, 4.0 + 3.4 * ((t[::-1] + 1) / 2)]])
bio.shape(ax, pts, token="plant", lw=1.2)
ax.plot([cx, cx], [4.0, 7.0], color=P.edge("plant"), lw=1.0, zorder=7)
ax.plot([cx, cx], [2.6, 4.0], color=P.edge("plant"), lw=1.8, zorder=5)
bio.label(ax, (cx, 9.2), "Capsella", size="small", italic=True)
bio.label(ax, (cx, 8.5), "silicle", size="small")

# ---------------- E: embryo folding
bio.panel(ax, "E", (30.2, 12.8))
names = ["Accumbent", "Incumbent", "Conduplicate"]
for i, nm in enumerate(names):
    cc = np.array([33.0, 10.0 - i * 3.4])
    ax.add_patch(Circle(cc, 1.2, facecolor=P.light("ovule"), edgecolor=P.edge("ovule"), lw=0.9, zorder=4))
    if i == 0:      # radicle against the edges of both cotyledons
        for d in (-0.22, 0.22):
            ax.add_patch(Ellipse(cc + np.array([-0.25, d]), 1.5, 0.36, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.6, zorder=5))
        ax.add_patch(Circle(cc + np.array([0.75, 0]), 0.24, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=6))
    elif i == 1:    # radicle against the back of one cotyledon
        for d in (-0.2, 0.2):
            ax.add_patch(Ellipse(cc + np.array([d, -0.15]), 0.36, 1.5, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.6, zorder=5))
        ax.add_patch(Circle(cc + np.array([0, 0.82]), 0.24, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=6))
    else:           # cotyledons folded around the radicle
        for r in (0.72, 0.42):
            th = np.linspace(0.25 * np.pi, 1.75 * np.pi, 40)
            ax.plot(cc[0] + r * np.cos(th), cc[1] + r * np.sin(th), color=P.edge("plant"), lw=4.0 if r > 0.5 else 3.0,
                    solid_capstyle="round", zorder=5)
        ax.add_patch(Circle(cc + np.array([0.05, 0]), 0.22, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=6))
    bio.label(ax, (cc[0], cc[1] - 1.55), nm, size="small")
bio.label(ax, (33.0, 0.6), "radicle (yellow), cotyledons (green)", size="tiny")
bio.icon(ax, "phylopic/brassica", at=(35.3, 12.2), height=1.4, color="plant")
