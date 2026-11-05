"""Planes of cell division in a cylindrical organ (schematic). A: transverse section. In a periclinal
(tangential) division the new wall (red) is parallel to the surface of the organ, adding a layer: the
organ thickens. In a radial anticlinal division the new wall (blue) lies along a radius, perpendicular to
the surface, adding a cell to the ring: the circumference grows. B: longitudinal section. In a transverse
anticlinal division the new wall (orange) is perpendicular to the long axis, adding a cell to a
longitudinal file: the organ lengthens. Radial and transverse divisions together are the anticlinal
divisions.
"""

import math

import numpy as np
from matplotlib.patches import Polygon, Wedge

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)
C = np.array([5.6, 5.2])
R0, R1, R2 = 1.6, 2.9, 4.2
NC = 18


def sector(r0, r1, a0, a1, tk="cytoplasm", lw=0.9, z=3):
    t = np.linspace(a0, a1, 20)
    outer = np.c_[C[0] + r1 * np.cos(t), C[1] + r1 * np.sin(t)]
    inner = np.c_[C[0] + r0 * np.cos(t[::-1]), C[1] + r0 * np.sin(t[::-1])]
    ax.add_patch(Polygon(np.vstack([outer, inner]), closed=True, facecolor=P.fill(tk), edgecolor=P.edge("cell_wall"), lw=lw, zorder=z))


bio.panel(ax, "A", (0.1, 10.9))
bio.label(ax, (0.8, 10.85), "Transverse section", size="title", ha="left", va="top")
ax.add_patch(Wedge(C, R0, 0, 360, facecolor=P.light("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=0.9, zorder=2))
da = 2 * math.pi / NC
for k in range(NC):
    for r0, r1 in ((R0, R1), (R1, R2)):
        hl = (k == 2 and r0 == R1) or (k == 7 and r0 == R1)
        sector(r0, r1, k * da, (k + 1) * da, tk="highlight" if hl else "cytoplasm")
# periclinal (tangential) new wall in cell k = 2, outer ring
t = np.linspace(2 * da, 3 * da, 20)
rm = (R1 + R2) / 2
ax.plot(C[0] + rm * np.cos(t), C[1] + rm * np.sin(t), color=P.edge("negative"), lw=2.6, zorder=6)
# radial anticlinal new wall in cell k = 7
am = 7.5 * da
ax.plot([C[0] + R1 * math.cos(am), C[0] + R2 * math.cos(am)], [C[1] + R1 * math.sin(am), C[1] + R2 * math.sin(am)],
        color=P.edge("dna"), lw=2.6, zorder=6)
# a radius and the tangent through the periclinal cell
ar = 2.5 * da
ax.plot([C[0], C[0] + (R2 + 1.1) * math.cos(ar)], [C[1], C[1] + (R2 + 1.1) * math.sin(ar)], color=P.muted(), lw=0.8, ls=(0, (3, 2)), zorder=7)
tp = C + (R2 + 0.55) * np.array([math.cos(ar), math.sin(ar)])
tv = np.array([-math.sin(ar), math.cos(ar)])
ax.plot([tp[0] - 1.4 * tv[0], tp[0] + 1.4 * tv[0]], [tp[1] - 1.4 * tv[1], tp[1] + 1.4 * tv[1]], color=P.muted(), lw=0.8, ls=(0, (3, 2)), zorder=7)
bio.label(ax, (C[0] + (R2 + 1.45) * math.cos(ar) + 0.2, C[1] + (R2 + 1.45) * math.sin(ar)), "radius", size="tiny", color=P.muted())
bio.label(ax, (tp[0] + 1.6 * tv[0] + 0.5, tp[1] + 1.6 * tv[1]), "tangent", size="tiny", color=P.muted())
bio.callout(ax, (C[0] + rm * math.cos(2.7 * da), C[1] + rm * math.sin(2.7 * da)), (12.6, 7.6), "Periclinal (tangential) division", size="small")
bio.label(ax, (12.7, 7.05), "new wall parallel to the surface: adds a layer", size="tiny", color=P.muted(), ha="left")
pr = (C[0] + (R1 + 0.8) * math.cos(am), C[1] + (R1 + 0.8) * math.sin(am))
bio.callout(ax, pr, (12.6, 3.6), "Radial (anticlinal) division", size="small")
bio.label(ax, (12.7, 3.05), "new wall along a radius: widens the ring", size="tiny", color=P.muted(), ha="left")

# B: longitudinal section, a file of cells
bio.panel(ax, "B", (17.4, 10.9))
bio.label(ax, (18.1, 10.85), "Longitudinal section", size="title", ha="left", va="top")
x0, w = 19.6, 1.6
ys = np.arange(1.0, 9.6, 1.2)
for col in range(2):
    for k, y in enumerate(ys[:-1]):
        hl = col == 0 and k == 3
        xx = x0 + col * w
        ax.add_patch(Polygon([(xx, y), (xx + w, y), (xx + w, y + 1.2), (xx, y + 1.2)], closed=True,
                             facecolor=P.fill("highlight" if hl else "cytoplasm"), edgecolor=P.edge("cell_wall"), lw=0.9, zorder=3))
ym = ys[3] + 0.6
ax.plot([x0, x0 + w], [ym, ym], color=P.edge("atp"), lw=2.6, zorder=6)
ax.annotate("", xy=(x0 - 0.6, 9.4), xytext=(x0 - 0.6, 1.0), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.9), zorder=7)
bio.label(ax, (x0 - 1.0, 5.2), "long axis", size="tiny", color=P.muted(), rotation=90)
bio.callout(ax, (x0 + 0.4, ym), (17.6, 0.6), "Transverse (anticlinal) division", size="small")
bio.label(ax, (17.5, 0.1), "adds a cell to the file: lengthens", size="tiny", color=P.muted(), ha="right")
