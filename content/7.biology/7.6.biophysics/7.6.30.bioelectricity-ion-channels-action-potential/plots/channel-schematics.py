"""Two schematics of single-channel biophysics. A: the four patch-clamp configurations. A glass pipette
pressed onto a cell forms a gigaohm seal (cell-attached); suction ruptures the patch and gives access to
the whole cell (whole-cell); pulling the pipette away from a cell-attached seal excises a patch with its
cytoplasmic face to the bath (inside-out); pulling away from the whole-cell configuration lets the
membrane reseal into a patch with its extracellular face to the bath (outside-out). B: the selectivity
filter of a K+ channel (KcsA-type, two of the four subunits shown): the backbone carbonyl oxygens of the
signature sequence TVGYG line four sites S1-S4, each a cage of eight oxygens that mimics the hydration
shell of K+. In the conducting state ions occupy alternate sites (S1 and S3, or S2 and S4) with water
between them, and the entry of a third ion pushes the queue forward (knock-on). Not to scale."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyBboxPatch, Wedge
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.6), gridspec_kw=dict(width_ratios=[2.0, 1.0]))
fig.subplots_adjust(wspace=0.08, left=0.01, right=0.99, bottom=0.03, top=0.9)

ax = axs[0]
ax.set_xlim(0, 20)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
mem, cyt = P.edge("membrane"), P.fill("cytoplasm")


def pipette(x, ytip, open_tip=True):
    ax.add_patch(Polygon([[x - 0.35, ytip], [x - 1.0, ytip + 4.2], [x + 1.0, ytip + 4.2], [x + 0.35, ytip]],
                         closed=False, fill=False, edgecolor=P.ink(), lw=1.1))


# cell-attached
ax.add_patch(Circle((2.5, 1.8), 1.6, facecolor=cyt, edgecolor=mem, lw=1.6))
pipette(2.5, 3.35)
ax.text(2.5, 7.6, "cell-attached", ha="center", fontsize=FT["small"], color=P.ink())
# whole-cell
ax.add_patch(Circle((7.5, 1.8), 1.6, facecolor=cyt, edgecolor=mem, lw=1.6))
ax.add_patch(Wedge((7.5, 1.8), 1.62, 77, 103, width=0.12, facecolor="white", edgecolor="none"))
ax.add_patch(Polygon([[7.15, 3.35], [7.85, 3.35], [8.5, 7.5], [6.5, 7.5]], facecolor=cyt, edgecolor="none", alpha=0.6))
pipette(7.5, 3.35)
ax.text(7.5, 7.6, "whole-cell", ha="center", fontsize=FT["small"], color=P.ink())
# inside-out
pipette(12.5, 3.35)
ax.plot([12.15, 12.5, 12.85], [3.35, 3.0, 3.35], color=mem, lw=1.6)
ax.text(12.5, 2.3, "cytoplasmic face\nto the bath", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.text(12.5, 7.6, "inside-out", ha="center", fontsize=FT["small"], color=P.ink())
# outside-out
pipette(17.5, 3.35)
ax.add_patch(Polygon([[17.15, 3.35], [17.85, 3.35], [18.5, 7.5], [16.5, 7.5]], facecolor=cyt, edgecolor="none", alpha=0.6))
ax.plot([17.15, 17.5, 17.85], [3.35, 3.0, 3.35], color=mem, lw=1.6)
ax.text(17.5, 2.3, "extracellular face\nto the bath", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.text(17.5, 7.6, "outside-out", ha="center", fontsize=FT["small"], color=P.ink())
for xa, xb, lab in [(4.3, 5.7, "suction"), (9.3, 10.7, None)]:
    ax.annotate("", (xb, 4.5), (xa, 4.5), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=1))
    if lab:
        ax.text((xa + xb) / 2, 4.8, lab, ha="center", fontsize=FT["tiny"], color=P.muted())
ax.text(10.0, 4.8, "pull\n(from cell-attached)", ha="center", fontsize=FT["tiny"], color=P.muted(), va="bottom")
ax.annotate("", (15.7, 4.5), (14.3, 4.5), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=1))
ax.text(15.0, 4.8, "pull\n(from whole-cell)", ha="center", fontsize=FT["tiny"], color=P.muted(), va="bottom")
charts.title(ax, "A  Patch-clamp configurations")

ax = axs[1]
ax.set_xlim(0, 6)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
for xs, sgn in [(1.2, 1), (4.8, -1)]:
    ax.add_patch(FancyBboxPatch((xs - 0.45, 1.6), 0.9, 4.8, boxstyle="round,pad=0.1", facecolor=P.fill("channel"),
                                edgecolor=P.edge("channel"), lw=1))
ys = [5.6, 4.6, 3.6, 2.6, 1.9]
res = ["G", "Y", "G", "V", "T"]
for y, rname in zip([5.9, 4.9, 3.9, 2.9, 1.9], res):
    for xs, sgn in [(1.2, 1), (4.8, -1)]:
        ax.plot([xs + 0.45 * sgn, xs + 0.95 * sgn], [y, y], color=P.edge("channel"), lw=1)
        ax.add_patch(Circle((xs + 1.05 * sgn, y), 0.12, facecolor=P.edge("negative"), edgecolor="none"))
    ax.text(0.35, y, rname, fontsize=FT["tiny"], color=P.ink(), va="center")
for (y, kind, lab) in [(5.4, "k", "S1"), (4.4, "w", "S2"), (3.4, "k", "S3"), (2.4, "w", "S4")]:
    if kind == "k":
        ax.add_patch(Circle((3.0, y), 0.36, facecolor=P.fill("k"), edgecolor=P.edge("k"), lw=1))
        ax.text(3.0, y, "K$^+$", fontsize=FT["tiny"], ha="center", va="center", color=P.on_fill())
    else:
        ax.add_patch(Circle((3.0, y), 0.2, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8))
    ax.text(5.75, y, lab, fontsize=FT["tiny"], color=P.ink(), va="center")
ax.text(3.0, 7.2, "outside", ha="center", fontsize=FT["tiny"], color=P.muted())
ax.text(3.0, 0.7, "central cavity (inside)", ha="center", fontsize=FT["tiny"], color=P.muted())
ax.add_patch(Circle((3.0, 1.35), 0.36, facecolor=P.fill("k"), edgecolor=P.edge("k"), lw=1))
charts.title(ax, "B  K$^+$ selectivity filter")
