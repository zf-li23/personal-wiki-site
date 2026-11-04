# Binary fission of a rod-shaped bacterium (schematic, E. coli-like).
# A: one cell cycle. (1) A newborn cell with one nucleoid and one origin of replication (oriC). (2) The cell
#    elongates; replication has started and the two new origins move apart towards the cell quarters.
# (3) Replication is complete and the two nucleoids have segregated; FtsZ assembles a ring at midcell (the
#    Z ring) in the nucleoid-free gap. (4) The divisome builds the septum: the envelope constricts while
#    septal peptidoglycan is made. (5) Two daughter cells, each with one chromosome, separate.
# B: why the ring forms at midcell (model curves, arbitrary units). Time-averaged MinC, from the pole-to-pole
#    Min oscillation, is highest at the poles and lowest at midcell; nucleoid occlusion (SlmA in E. coli,
#    Noc in Bacillus subtilis) inhibits ring assembly over the two segregated nucleoids. Only where both
#    inhibitors are low (shaded) can the Z ring assemble.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
fig = plt.figure(figsize=(14.0, 4.4))
ax = fig.add_axes([0.0, 0.0, 0.68, 1.0])
ax.set_xlim(0, 22)
ax.set_ylim(0, 7)
ax.set_aspect("equal")
ax.axis("off")
bio.panel(ax, "A", (0.2, 6.9))
bio.label(ax, (1.0, 6.65), "One cycle of binary fission", size="small", bold=True, ha="left")

W = 0.95


def nucleoid(c, rx, ry, seed):
    bio.shape(ax, bio.blob(c, rx, ry, wobble=0.12, seed=seed), token="dna", lw=0.9, zorder=10)


def ori(c):
    ax.add_patch(plt.Circle(c, 0.09, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=12))


def zring(x, y, h):
    ax.add_patch(Ellipse((x, y), 0.28, h, facecolor="none", edgecolor=P.edge("negative"), lw=2.4, zorder=13))


y = 3.6
# 1 newborn
M.bacillus(ax, (1.9, y), 2.0, W, gram="-")
nucleoid((1.9, y), 0.55, 0.28, 1)
ori((1.9, y + 0.05))
# 2 elongating, replicating
M.bacillus(ax, (5.6, y), 3.0, W, gram="-")
nucleoid((5.6, y), 0.95, 0.3, 2)
ori((4.95, y + 0.05))
ori((6.25, y + 0.05))
bio.label(ax, (5.6, y - 1.0), "replication;\norigins move apart", size="tiny", color=P.muted())
# 3 segregated, Z ring
M.bacillus(ax, (10.0, y), 3.8, W, gram="-")
nucleoid((9.05, y), 0.55, 0.28, 3)
nucleoid((10.95, y), 0.55, 0.28, 4)
ori((8.75, y + 0.05))
ori((11.25, y + 0.05))
zring(10.0, y, W * 0.95)
bio.callout(ax, (10.0, y + W * 0.47), (10.6, y + 1.45), "Z ring (FtsZ)", size="tiny")
# 4 constricting
M.bacillus(ax, (14.6, y), 3.9, W, gram="-", dividing=True)
nucleoid((13.65, y), 0.55, 0.28, 5)
nucleoid((15.55, y), 0.55, 0.28, 6)
ori((13.35, y + 0.05))
ori((15.85, y + 0.05))
zring(14.6, y, W * 0.6)
bio.callout(ax, (14.6, y - W * 0.3), (15.3, y - 1.35), "divisome: septum", size="tiny")
# 5 daughters
for dx in (-1.05, 1.05):
    M.bacillus(ax, (19.6 + dx, y), 1.95, W, gram="-")
    nucleoid((19.6 + dx, y), 0.52, 0.27, 7 if dx < 0 else 8)
    ori((19.6 + dx, y + 0.05))
for k, (x0, x1) in enumerate(((3.0, 3.95), (7.2, 7.95), (12.0, 12.55), (16.65, 17.45))):
    bio.arrow(ax, (x0, y), (x1, y), kind="process", lw=1.1, head=0.18)
for x, n in ((1.9, "1"), (5.6, "2"), (10.0, "3"), (14.6, "4"), (19.6, "5")):
    bio.label(ax, (x, y + 1.25 if n != "3" else y + 1.25), n, size="small", bold=True)
# legend
lx = 1.2
nucleoid((lx, 1.0), 0.32, 0.17, 9)
bio.label(ax, (lx + 0.5, 1.0), "nucleoid (chromosome)", size="tiny", ha="left")
ori((6.0, 1.0))
bio.label(ax, (6.25, 1.0), "origin (oriC)", size="tiny", ha="left")
ax.add_patch(Ellipse((9.6, 1.0), 0.2, 0.55, facecolor="none", edgecolor=P.edge("negative"), lw=2.2))
bio.label(ax, (9.85, 1.0), "FtsZ ring", size="tiny", ha="left")
bio.label(ax, (13.0, 1.0), "about one generation: 20 min to many hours", size="tiny", ha="left", color=P.muted())

# ---- B: positioning ---------------------------------------------------------------------------------
bx = fig.add_axes([0.74, 0.2, 0.24, 0.62])
x = np.linspace(-0.5, 0.5, 400)
minc = 0.15 + 0.85 * (np.cosh(x / 0.17) - 1) / (np.cosh(0.5 / 0.17) - 1)
noc = 0.9 * (np.exp(-((x - 0.25) / 0.1) ** 2) + np.exp(-((x + 0.25) / 0.1) ** 2))
inhib = np.maximum(minc, noc)
ok = inhib < 0.3
bx.fill_between(x, 0, 1.05, where=ok, color=P.mix(P.fill("positive"), P.surface(), 0.75 if not P.is_dark() else 0.85), lw=0)
bx.plot(x, minc, color=charts.line("protein"), lw=2.0, label="MinC (time average)")
bx.plot(x, noc, color=charts.line("dna"), lw=2.0, ls="--", label="nucleoid occlusion")
bx.text(0, 1.08, "Z ring\npermitted", ha="center", va="bottom", fontsize=6.8, color=charts.line("positive"))
bx.set_xticks([-0.5, 0, 0.5], ["pole", "midcell", "pole"])
bx.set_yticks([])
bx.set_ylim(0, 1.3)
bx.legend(fontsize=6.8, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=1)
charts.style_axes(bx, None, "inhibitor (a.u.)")
charts.title(bx, "B   Finding the middle")
