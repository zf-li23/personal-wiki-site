"""Spindle diagram of the vascular plant groups through geological time. The width of each spindle is the
approximate share of the group among the vascular plant species in fossil floras of that time: a schematic
redrawing of the overall pattern reported by Niklas, Tiffney and Knoll (1983) and later compilations, not
their data points. Silurian-Devonian early vascular plants; Carboniferous lycophyte, sphenophyte, fern and
seed fern floras; Permian-Jurassic gymnosperm floras; Cretaceous rise of the angiosperms. ICS time scale
on the left."""
import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import phylo

P = bio.P
T = np.array([430, 410, 395, 380, 365, 345, 320, 300, 280, 255, 230, 200, 170, 145, 125, 110, 95, 80, 66, 40, 20, 0])
SHARE = {  # schematic relative shares (rows are normalised to 100 at each time below)
    "Early vascular plants": [100, 85, 60, 25, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Lycophytes": [0, 15, 25, 25, 25, 25, 25, 20, 10, 5, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    "Sphenophytes": [0, 0, 0, 8, 12, 15, 15, 15, 12, 8, 8, 5, 4, 3, 3, 2, 1, 1, 1, 1, 1, 1],
    "Ferns": [0, 0, 10, 20, 25, 25, 25, 25, 22, 22, 25, 25, 25, 25, 25, 20, 15, 12, 10, 8, 6, 5],
    "Progymnosperms and\nseed ferns": [0, 0, 5, 22, 30, 35, 35, 30, 20, 12, 8, 5, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0],
    "Gymnosperms": [0, 0, 0, 0, 0, 0, 0, 10, 36, 53, 55, 62, 66, 68, 64, 50, 35, 24, 18, 12, 10, 8],
    "Angiosperms": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 26, 48, 62, 70, 78, 82, 85],
}
TOK = ["bract", "animal", "neuron", "plant", "carbohydrate", "ovule", "petal"]
M = np.array(list(SHARE.values()), dtype=float)
M = 100 * M / M.sum(axis=0)

fig, ax = bio.canvas(26, 16)
Y0, Y1 = 1.4, 14.4  # 430 Ma at Y0, 0 Ma at Y1


def y(age):
    return Y0 + (430 - age) / 430 * (Y1 - Y0)


phylo.geo_scale(ax, (Y0, Y1), (430, 0), 0.4, ranks=("era", "period"), height=0.6, orientation="vertical",
                size="tiny")
for a in (400, 300, 200, 100, 0):
    ax.plot([1.6, 25.6], [y(a), y(a)], color=P.muted(), lw=0.4, ls=":")
    bio.label(ax, (1.75, y(a) + 0.18), f"{a} Ma", size="tiny", ha="left", color=P.muted())

X0, DX = 4.6, 3.1
HALF = 1.45 / 100 * 2  # half-width per percentage point (100 % -> about 2.9 units wide)
for k, (name, tok) in enumerate(zip(SHARE, TOK)):
    cx = X0 + k * DX
    w = M[k] * HALF / 2
    nz = np.nonzero(M[k] > 0)[0]
    lo, hi = max(nz[0] - 1, 0), min(nz[-1] + 1, len(T) - 1)
    w, ys = w[lo:hi + 1], [y(a) for a in T[lo:hi + 1]]
    pts = [(cx - wi, yi) for wi, yi in zip(w, ys)] + [(cx + wi, yi) for wi, yi in zip(w[::-1], ys[::-1])]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=4))
    bio.label(ax, (cx, Y1 + 0.75), name, size="small", ha="center", bold=True)
# scale bar for the width
bx = X0 + 6 * DX - 1.0
ax.plot([bx, bx + 50 * HALF], [0.65, 0.65], color=P.ink(), lw=1.2)
bio.label(ax, (bx + 25 * HALF, 0.3), "50 % of species", size="tiny", ha="center")
bio.label(ax, (4.0, 0.45), "Schematic shares, after the pattern in Niklas, Tiffney & Knoll (1983)", size="tiny",
          ha="left", color=P.muted())
