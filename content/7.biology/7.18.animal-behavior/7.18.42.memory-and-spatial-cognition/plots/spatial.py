# How animals use landmarks and the geometry of space. A, B: landmark vectors in gerbils (after Collett,
# Cartwright and Smith 1986). A: gerbils were trained to find a seed hidden at a fixed position (star) relative
# to two identical landmarks. B: when the distance between the landmarks was doubled in a test, the animals
# searched mainly at two places, each at the trained distance and direction from one of the landmarks (dots:
# simulated search positions), rather than at one place midway; they had stored a separate vector for each
# landmark. C, D: the geometric module (after Cheng 1986). C: rats learned to find food in one corner of a
# rectangular box with a distinctive panel in each corner (colored squares). D: in tests they chose the
# correct corner (C) and the geometrically equivalent corner diagonally opposite (R, rotational error) about
# equally often, and the other two corners rarely, as if they reoriented by the shape of the box and ignored
# the panels (illustrative proportions of the reported pattern).
import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 9.0)


def landmark(xy):
    ax.add_patch(Rectangle((xy[0] - 0.22, xy[1] - 0.22), 0.44, 0.44, facecolor=P.fill("neutral"),
                           edgecolor=P.ink(), lw=1.0, zorder=8))


def arena(x0, y0, w, h):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.75),
                           edgecolor=P.ink(), lw=1.4, zorder=3))


bio.panel(ax, "A", (0.2, 8.8))
arena(0.8, 1.2, 6.0, 6.4)
L = [(2.8, 5.2), (4.8, 5.2)]
for l in L:
    landmark(l)
goal = (3.8, 3.4)
bio.label(ax, goal, "★", size="normal", color=P.edge("rna"))
for l in L:
    bio.arrow(ax, l, (goal[0] + (0.1 if l[0] > 4 else -0.1), goal[1] + 0.25), kind="link", dashed=True, color=P.muted())
bio.label(ax, (3.8, 0.7), "training", size="small")

bio.panel(ax, "B", (7.4, 8.8))
arena(8.0, 1.2, 6.0, 6.4)
L2 = [(9.0, 5.2), (13.0, 5.2)]
for l in L2:
    landmark(l)
for l in L2:
    tx, ty = l[0] + (goal[0] - (L[0][0] if l[0] < 11 else L[1][0])), l[1] + (goal[1] - L[0][1])
    pts = rng.normal([tx, ty], 0.3, (22, 2))
    for p in pts:
        ax.add_patch(Circle(p, 0.07, facecolor=P.edge("dna"), edgecolor="none", zorder=9))
bio.label(ax, (11.0, 3.4), "×", size="normal", color=P.muted())
bio.label(ax, (11.0, 2.8), "midway", size="tiny", color=P.muted())
bio.label(ax, (11.0, 0.7), "test: landmarks twice as far apart", size="small")

bio.panel(ax, "C", (15.0, 8.8))
arena(16.0, 2.4, 6.0, 3.6)
corners = {"C": (16.0, 6.0), "N1": (22.0, 6.0), "R": (22.0, 2.4), "N2": (16.0, 2.4)}
toks = {"C": "rna", "N1": "dna", "R": "positive", "N2": "atp"}
for k, (x, y) in corners.items():
    sx = 0.15 if x < 19 else -0.65
    sy = -0.65 if y > 4 else 0.15
    ax.add_patch(Rectangle((x + sx, y + sy), 0.5, 0.5, facecolor=P.fill(toks[k]), edgecolor=P.edge(toks[k]), lw=0.8, zorder=6))
    lx = x - 0.45 if x < 19 else x + 0.45
    bio.label(ax, (lx, y), k, size="small")
bio.label(ax, (17.3, 5.0), "food", size="tiny", ha="left", color=P.muted())
bio.label(ax, (19.0, 1.4), "rectangular box, a panel in each corner", size="tiny", color=P.muted())

pd = quant.Plot(ax, (25.0, 1.8, 4.4, 6.2), (0, 4), (0, 0.6), ylabel="Proportion of choices",
                xticks=[(0.5, "C"), (1.5, "R"), (2.5, "N1"), (3.5, "N2")], yticks=[0, 0.2, 0.4, 0.6])
bio.panel(ax, "D", (23.4, 8.8))
for i, (k, v) in enumerate((("C", 0.46), ("R", 0.40), ("N1", 0.07), ("N2", 0.07))):
    pd.bars([i + 0.15, i + 0.85], [v], toks[k])
