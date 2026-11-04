"""Bacterial versus archaeal membrane lipids and membranes (schematic). A: ester-linked fatty acids on
glycerol 3-phosphate, bilayer. B: ether-linked phytanyl chains on glycerol 1-phosphate, bilayer.
C: membrane-spanning tetraethers (biphytanyl, some with cyclopentane rings), monolayer."""
import numpy as np
from matplotlib.patches import Circle, RegularPolygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 12)
HEAD, TAIL = "lipid_head", "lipid_tail"


def chain(x, y0, y1, branched, rings=(), lw=1.3):
    ys = np.linspace(y0, y1, 60)
    xs = x + 0.05 * np.sin((ys - y0) * 18)
    ax.plot(xs, ys, color=P.edge(TAIL), lw=lw, solid_capstyle="round", zorder=5)
    if branched:
        n = int(abs(y1 - y0) / 0.22)
        for k in range(1, n):
            yy = y0 + (y1 - y0) * k / n
            ax.plot([x, x + 0.11], [yy, yy + 0.04], color=P.edge(TAIL), lw=0.9, zorder=5)
    for yr in rings:
        ax.add_patch(RegularPolygon((x, yr), 5, radius=0.1, facecolor=P.surface(), edgecolor=P.edge(TAIL), lw=0.9,
                                    zorder=6))


def head(x, y, r=0.2):
    ax.add_patch(Circle((x, y), r, facecolor=P.fill(HEAD), edgecolor=P.edge(HEAD), lw=0.9, zorder=7))


def link(x, y, kind):
    # small square = glycerol; ester vs ether marked by a little symbol under the head
    tok = "carbohydrate"
    ax.add_patch(RegularPolygon((x, y), 4, radius=0.12, orientation=np.pi / 4, facecolor=P.fill(tok),
                                edgecolor=P.edge(tok), lw=0.8, zorder=7))


def lipid(x, ytop, down, kind, length=1.5):
    s = 1 if down else -1
    head(x, ytop)
    link(x, ytop - s * 0.3, kind)
    for dx in (-0.09, 0.09):
        chain(x + dx, ytop - s * 0.42, ytop - s * (0.42 + length), branched=(kind != "ester"))


def bilayer(x0, n, ymid, kind):
    for k in range(n):
        x = x0 + 0.55 * k
        lipid(x, ymid + 2.0, True, kind, 1.5)
        lipid(x, ymid - 2.0, False, kind, 1.5)


def sides(x, ymid):
    bio.label(ax, (x, ymid + 2.6), "Out", size="small", color=P.muted(), ha="left")
    bio.label(ax, (x, ymid - 2.6), "In", size="small", color=P.muted(), ha="left")


ymid = 4.6
# A
bio.panel(ax, "A", (0.2, 11.8))
bio.label(ax, (4.2, 11.4), "Bacteria: ester lipids, bilayer", size="normal", bold=True)
bilayer(1.4, 10, ymid, "ester")
sides(6.9, ymid)
bio.callout(ax, (1.4, ymid + 2.2), (1.8, 9.9), "head group (phosphate + polar group)")
bio.callout(ax, (2.07, ymid + 1.7), (2.4, 9.2), "glycerol 3-phosphate, ester bonds")
bio.callout(ax, (3.2, ymid + 1.0), (3.6, 8.5), "straight fatty acid chains")
# B
bio.panel(ax, "B", (9.2, 11.8))
bio.label(ax, (13.2, 11.4), "Archaea: diether lipids, bilayer", size="normal", bold=True)
bilayer(10.4, 10, ymid, "ether")
sides(15.9, ymid)
bio.callout(ax, (11.07, ymid + 1.7), (11.4, 9.6), "glycerol 1-phosphate, ether bonds")
bio.callout(ax, (12.2, ymid + 1.0), (12.6, 8.8), "phytanyl chains (C20,\nmethyl-branched)")
# C
bio.panel(ax, "C", (18.2, 11.8))
bio.label(ax, (22.3, 11.4), "Archaea: tetraether lipids, monolayer", size="normal", bold=True)
for k in range(10):
    x = 19.4 + 0.55 * k
    head(x, ymid + 2.0)
    head(x, ymid - 2.0)
    link(x, ymid + 1.7, "ether")
    link(x, ymid - 1.7, "ether")
    rings = (ymid + 0.6, ymid - 0.5) if k % 3 == 1 else ()
    for dx in (-0.09, 0.09):
        chain(x + dx, ymid + 1.58, ymid - 1.58, branched=True, rings=rings if dx < 0 else ())
sides(24.9, ymid)
bio.callout(ax, (19.4 + 0.55 * 4 - 0.09, ymid + 0.6), (21.4, 9.2), "biphytanyl chains span the\nmembrane; cyclopentane rings")
