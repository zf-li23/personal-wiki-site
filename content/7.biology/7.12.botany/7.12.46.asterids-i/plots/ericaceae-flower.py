# Ericaceae. A: Rhododendron flower in section (funnel-shaped, slightly zygomorphic corolla with spots on
# the upper lobe, ten free stamens of unequal length arising from the disc, superior five-locular ovary).
# B: a Rhododendron stamen: anther opening by two apical pores, pollen tetrads linked by viscin threads.
# C: Vaccinium urceolate flower in section (pendent, inferior ovary); anther with two dorsal spurs and two
# apical tubules ending in pores. D: buzz pollination: a bumblebee vibrates the anthers and pollen is
# shaken out of the pores. E: a pollen tetrad (tetrahedral).
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(36, 13)

# A: Rhododendron
bio.panel(ax, "A", (0.3, 12.8))
cx, y0 = 4.6, 2.0
ax.plot([cx, cx], [0.6, y0], color=P.edge("plant"), lw=1.8, zorder=3)
bio.shape(ax, [(cx - 0.7, y0), (cx + 0.7, y0), (cx + 0.55, y0 + 0.5), (cx - 0.55, y0 + 0.5)], token="sepal", lw=0.8, zorder=4)
t = np.linspace(0, 1, 40)
for s, top in ((-1, 3.4), (1, 4.2)):                     # upper (right) lobe longer: slight zygomorphy
    inner = np.c_[cx + s * (0.4 + 2.6 * t ** 2), y0 + 0.5 + 6.2 * t]
    outer = np.c_[cx + s * (0.65 + top * t ** 1.8), y0 + 0.5 + 6.0 * t]
    bio.shape(ax, np.vstack([inner, outer[::-1]]), token="petal", lw=0.9, zorder=4)
for k in range(5):
    ax.add_patch(Circle((cx + 2.2 + 0.25 * k, y0 + 5.0 + 0.3 * k), 0.08, color=P.edge("petal"), zorder=5))
bio.shape(ax, [(cx - 0.45, y0 + 0.5), (cx + 0.45, y0 + 0.5), (cx + 0.4, y0 + 1.6), (cx - 0.4, y0 + 1.6)], token="ovary", lw=0.9, zorder=6)
ax.plot([cx, cx + 0.9], [y0 + 1.6, y0 + 8.2], color=P.edge("ovary"), lw=1.3, zorder=6)
ax.add_patch(Circle((cx + 0.9, y0 + 8.3), 0.18, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.7, zorder=7))
for i, (dx, h) in enumerate([(-0.6, 5.2), (-0.3, 6.0), (0.0, 6.6), (0.3, 7.0), (0.6, 6.4)]):
    ax.plot([cx + 0.1 * dx, cx + dx + 0.5], [y0 + 1.0, y0 + h], color=P.edge("anther"), lw=0.9, zorder=5)
    ax.add_patch(Ellipse((cx + dx + 0.5, y0 + h + 0.2), 0.22, 0.45, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=6))
bio.label(ax, (4.6, 12.3), "Rhododendron", italic=True, size="title")
bio.callout(ax, (cx + 3.0, y0 + 5.9), (8.4, 10.6), "Spotted upper lobe")
bio.callout(ax, (cx + 0.8, y0 + 7.2), (0.8, 10.4), "Free stamens (5-10)")
bio.callout(ax, (cx - 0.3, y0 + 1.0), (0.8, 4.0), "Superior ovary")

# B: stamen with apical pores and tetrads
bio.panel(ax, "B", (9.6, 12.8))
ax.plot([12.0, 12.0], [1.4, 7.0], color=P.edge("anther"), lw=1.4, zorder=4)
bio.shape(ax, [(11.5, 7.0), (12.5, 7.0), (12.55, 9.4), (12.2, 9.8), (11.8, 9.8), (11.45, 9.4)], token="anther", lw=0.9, zorder=5)
for x in (11.8, 12.2):
    ax.add_patch(Circle((x, 9.7), 0.1, facecolor=P.surface(), edgecolor=P.edge("anther"), lw=0.7, zorder=6))
for k, (x, y) in enumerate([(12.6, 10.6), (13.1, 11.2), (13.7, 11.6)]):
    for d in ((0, 0), (0.18, 0), (0.09, 0.15), (0.09, 0.06)):
        ax.add_patch(Circle((x + d[0], y + d[1]), 0.1, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.4, zorder=7))
ax.plot([12.2, 12.6, 13.1, 13.7], [9.8, 10.6, 11.2, 11.6], color=P.muted(), lw=0.5, zorder=6)
bio.callout(ax, (12.2, 9.7), (14.6, 9.0), "Apical pores")
bio.callout(ax, (13.15, 11.25), (11.4, 12.4), "Tetrads on viscin threads")

# C: Vaccinium
bio.panel(ax, "C", (16.0, 12.8))
cx, yt = 19.4, 10.2
ax.plot([cx, cx], [yt, yt + 1.6], color=P.edge("plant"), lw=1.6, zorder=3)
bio.shape(ax, [(cx - 0.8, yt), (cx + 0.8, yt), (cx + 0.7, yt - 1.4), (cx - 0.7, yt - 1.4)], token="ovary", lw=0.9, zorder=5)
ang = np.linspace(0.15 * np.pi, 1.85 * np.pi, 80)
urn = np.c_[cx + 1.6 * np.sin(ang) * (1 - 0.2 * np.cos(ang)), yt - 1.4 - 2.6 * (1 - np.cos(ang)) / 2 - 0.3]
bio.shape(ax, urn, token="petal", lw=1.0, zorder=4)
ax.plot([cx, cx], [yt - 1.4, yt - 6.2], color=P.edge("ovary"), lw=1.2, zorder=6)
for s in (-1, 1):
    x = cx + s * 0.55
    ax.plot([x, x], [yt - 1.5, yt - 3.2], color=P.edge("anther"), lw=0.9, zorder=6)
    bio.shape(ax, [(x - 0.18, yt - 3.2), (x + 0.18, yt - 3.2), (x + 0.1, yt - 4.4), (x - 0.1, yt - 4.4)], token="anther", lw=0.7, zorder=7)
    ax.plot([x + s * 0.15, x + s * 0.55], [yt - 3.4, yt - 3.0], color=P.edge("anther"), lw=1.0, zorder=7)
bio.label(ax, (19.4, 12.3), "Vaccinium", italic=True, size="title")
bio.callout(ax, (cx + 0.6, yt - 0.7), (23.0, 10.6), "Inferior ovary")
bio.callout(ax, (cx + 1.1, yt - 3.0), (23.0, 7.6), "Spur")
bio.callout(ax, (cx + 0.55, yt - 4.3), (23.0, 4.6), "Tubule with pore")
bio.callout(ax, (cx - 1.5, yt - 3.6), (16.4, 4.0), "Urceolate corolla")

# D: buzz pollination
bio.panel(ax, "D", (24.6, 12.8))
cx = 28.2
for s in (-1, 1):
    bio.shape(ax, [(cx + s * 0.3, 9.6), (cx + s * 0.6, 9.6), (cx + s * 0.5, 5.6), (cx + s * 0.2, 5.6)], token="anther", lw=0.8, zorder=5)
ax.add_patch(Ellipse((cx + 0.2, 7.4), 2.2, 1.4, angle=80, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=6))
ax.add_patch(Ellipse((cx + 0.4, 5.2), 1.6, 2.6, angle=10, facecolor=P.fill("atp"), edgecolor=P.edge("atp"), lw=0.9, zorder=6))
for k in range(3):
    ax.plot([cx - 0.5 + 0.4 * k, cx - 0.3 + 0.4 * k], [8.1 + 0.2 * k, 8.4 + 0.2 * k], color=P.ink(), lw=0.8, zorder=7)
for k in range(10):
    ax.add_patch(Circle((cx - 0.1 + 0.25 * np.sin(k), 4.6 - 0.32 * k), 0.06, color=P.edge("anther"), zorder=7))
bio.label(ax, (cx, 11.4), "~ vibration (sonication)", size="small")
bio.callout(ax, (cx - 0.1, 2.6), (31.2, 1.8), "Pollen shaken out of pores")
bio.callout(ax, (cx + 0.6, 7.6), (31.2, 9.6), "Bee (thorax)")

# E: tetrad
bio.panel(ax, "E", (32.0, 12.8))
c = np.array([34.0, 6.6])
for d in ((-0.45, -0.3), (0.45, -0.3), (0.0, 0.45), (0.0, -0.02)):
    ax.add_patch(Circle(c + d, 0.5, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.8, zorder=6))
bio.label(ax, (34.0, 4.8), "pollen tetrad", size="small")
