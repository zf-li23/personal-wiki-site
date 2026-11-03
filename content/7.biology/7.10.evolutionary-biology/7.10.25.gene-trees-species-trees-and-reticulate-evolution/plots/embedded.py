"""Gene trees inside a species tree. The species tree ((A, B), C) is drawn as tubes, whose width
stands for the population size; one gene copy is sampled from each species. A: the lineages of A and
B coalesce within their common ancestral population AB, so the gene tree matches the species tree.
B: they fail to coalesce in AB; in the ancestral population ABC the first coalescence happens to join
A and B, so the gene tree again matches. C: the lineages of A and B pass through AB without
coalescing and the first coalescence in ABC joins B and C, producing the discordant gene tree
(A, (B, C)): incomplete lineage sorting. Time runs upward."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
tAB, tABC, top = 1.0, 2.0, 3.4
tube = P.light("neutral")
edge = P.muted()


def species_tree(ax):
    shape = [(0.0, 0.0), (1.2, 0.0), (1.2, tAB), (2.3, tAB), (2.3, 0.0), (3.5, 0.0), (3.5, tAB + 0.0),
             (3.0, tABC), (4.4, tABC), (4.4, 0.0), (5.6, 0.0), (5.6, tABC), (4.6, top), (1.2, top),
             (0.6, tABC), (0.0, tAB)]
    ax.add_patch(Polygon(shape, closed=True, facecolor=tube, edgecolor=edge, lw=0.9))
    for x, s in ((0.6, "A"), (2.9, "B"), (5.0, "C")):
        ax.text(x, -0.25, s, ha="center", va="top", fontsize=FT["normal"], color=P.ink(), style="italic")
    ax.text(1.9, (tAB + tABC) / 2, "AB", fontsize=FT["tiny"], color=P.muted(), ha="center")
    ax.text(3.0, top - 0.35, "ABC", fontsize=FT["tiny"], color=P.muted(), ha="center")


def draw(ax, events, title):
    species_tree(ax)
    col = charts.line("dna")
    for path in events:
        xs, ys = zip(*path)
        ax.plot(xs, ys, color=col, lw=2.0, solid_capstyle="round")
    ax.set_xlim(-0.3, 5.9)
    ax.set_ylim(-0.6, top + 0.2)
    ax.axis("off")
    charts.title(ax, title)


fig, axs = plt.subplots(1, 3, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.04, top=0.9, wspace=0.08)
cA, cB, cC = 0.6, 2.9, 5.0
# A: coalescence in AB at 1.5, then with C at 2.6
draw(axs[0], [[(cA, 0), (cA, tAB), (1.6, 1.5)], [(cB, 0), (cB, tAB), (1.6, 1.5)],
              [(1.6, 1.5), (1.8, tABC), (2.6, 2.6)], [(cC, 0), (cC, tABC), (2.6, 2.6)], [(2.6, 2.6), (2.6, 3.1)]],
     "A  Coalescence in AB")
# B: no coalescence in AB; A and B join at 2.5 in ABC, then C at 3.0
draw(axs[1], [[(cA, 0), (cA, tAB), (1.4, tABC), (2.2, 2.5)], [(cB, 0), (cB, tAB), (2.1, tABC), (2.2, 2.5)],
              [(2.2, 2.5), (2.7, 3.0)], [(cC, 0), (cC, tABC), (3.4, 3.0)], [(3.4, 3.0), (2.7, 3.0)], [(2.7, 3.0), (2.7, 3.25)]],
     "B  No coalescence in AB, A and B first")
# C: no coalescence in AB; B and C join at 2.4, then A at 3.0
draw(axs[2], [[(cA, 0), (cA, tAB), (1.3, tABC), (1.8, 3.0)], [(cB, 0), (cB, tAB), (2.3, tABC), (3.2, 2.4)],
              [(cC, 0), (cC, tABC), (3.2, 2.4)], [(3.2, 2.4), (2.6, 3.0)], [(1.8, 3.0), (2.6, 3.0)], [(2.2, 3.0), (2.2, 3.25)]],
     "C  Incomplete lineage sorting")
