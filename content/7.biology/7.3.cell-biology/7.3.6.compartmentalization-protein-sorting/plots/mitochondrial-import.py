"""Protein import into mitochondria: the main pathways (schematic).

All imported proteins cross the outer membrane through the TOM complex (Tom40 channel; Tom20 and
Tom22 receptors). Presequence pathway: the positively charged amphipathic presequence is pulled
through TIM23 (whose channel is formed mainly by Tim17) by the membrane potential across the inner
membrane (positive in the intermembrane space), and the chain is drawn into the matrix by the import
motor (mtHsp70 with Tim44); the presequence is cut off by the matrix processing peptidase (MPP).
Carrier pathway: hydrophobic inner-membrane carriers are escorted through the intermembrane space by
small Tim9-Tim10 chaperones and inserted by TIM22. Beta-barrel pathway: outer-membrane beta-barrel
proteins return from the intermembrane space to the SAM complex (Sam50). Disulfide relay: small
cysteine-rich proteins are oxidatively folded and trapped in the intermembrane space by Mia40 (MIA),
which is reoxidized by Erv1. Oxa1 inserts proteins into the inner membrane from the matrix side.
"""

import numpy as np
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)
yo, yi = 7.2, 3.8
MH = CB.MH
ax.add_patch(Rectangle((0.2, yo), 23.6, 3.6, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((0.2, yi), 23.6, yo - yi, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((0.2, 0.3), 23.6, yi - 0.3, facecolor=P.fill("matrix"), edgecolor="none", zorder=0))
bio.bilayer(ax, [(0.2, yo), (23.8, yo)])
bio.bilayer(ax, [(0.2, yi), (23.8, yi)])
bio.label(ax, (0.45, 10.4), "Cytosol", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.45, yo - 0.75), "Intermembrane space", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.45, 0.7), "Matrix", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (23.6, yo + 0.75), "outer membrane", size="tiny", ha="right", color=P.muted())
bio.label(ax, (23.6, yi + 0.75), "inner membrane", size="tiny", ha="right", color=P.muted())
ink = P.edge("protein")


def path(pts, lw=2.0, color=None):
    pts = np.asarray(pts, float)
    from scipy.interpolate import make_interp_spline
    t = np.linspace(0, 1, len(pts))
    q = make_interp_spline(t, pts, k=min(3, len(pts) - 1))(np.linspace(0, 1, 200))
    ax.plot(q[:, 0], q[:, 1], color=color or ink, lw=lw, solid_capstyle="round", zorder=14)
    return q


# TOM
xt = 4.2
CB.channel(ax, xt, yo, token="mitochondrion", width=1.6)
bio.protein(ax, (xt - 1.15, yo + 0.75), 0.7, 0.45, "receptor", wobble=0.06)
bio.protein(ax, (xt + 1.15, yo + 0.75), 0.7, 0.45, "receptor", wobble=0.06)
bio.label(ax, (xt + 0.5, yo + 1.5), "TOM", size="small", bold=True, ha="left")
bio.label(ax, (xt + 1.6, yo + 1.1), "Tom20/22", size="tiny", ha="left", color=P.muted())

# presequence pathway: TIM23 + motor + MPP
CB.channel(ax, xt, yi, token="enzyme", width=1.4)
bio.label(ax, (xt - 1.0, yi), "TIM23\n(Tim17)", size="tiny", bold=True, ha="right")
q = path([(2.6, 9.9), (3.6, 9.2), (xt, yo + 0.4), (xt, yo - 1.0), (xt, yi + 0.6), (xt, yi - 0.6), (xt + 0.3, 1.9)])
for k, p in enumerate(q[[8, 18, 28]]):
    bio.label(ax, (p[0] - 0.25, p[1] + 0.05), "+", size="small", bold=True, color=P.edge("negative"))
bio.protein(ax, (xt + 1.0, yi - 1.25), 1.2, 0.75, "positive", wobble=0.07, text="mtHsp70")
bio.protein(ax, (xt - 0.9, 1.6), 0.9, 0.6, "drug", wobble=0.07, text="MPP")
bio.label(ax, (xt + 0.6, 1.1), "presequence cut off", size="tiny", ha="left")
for xx in np.arange(1.2, 10.0, 0.8):
    bio.label(ax, (xx, yi + 0.75), "+", size="tiny", color=P.edge("negative"))
    bio.label(ax, (xx, yi - 0.75), "−", size="tiny", color=P.edge("dna"))
bio.label(ax, (2.3, 2.6), "Δψ pulls the\npresequence", size="tiny", ha="center")

# carrier pathway: small TIMs + TIM22
xs, x22 = 8.3, 10.6
bio.arrow(ax, (xt + 0.7, yo - 0.9), (xs - 0.6, yo - 1.4), kind="process", color=ink, bend=0.1)
bio.protein(ax, (xs, yo - 1.55), 1.35, 0.65, "lipid", wobble=0.07, text="Tim9–10")
bio.arrow(ax, (xs + 0.5, yo - 1.9), (x22 - 0.3, yi + 0.6), kind="process", color=ink, bend=0.15)
CB.channel(ax, x22, yi, token="channel", width=1.3)
bio.label(ax, (x22, yi - 1.0), "TIM22", size="tiny", bold=True)
for dx in (0.95, 1.25, 1.55):
    ax.add_patch(Rectangle((x22 + dx - 0.1, yi - MH), 0.2, 2 * MH, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.8, zorder=12))
bio.label(ax, (x22 + 1.25, yi - 1.0), "carrier", size="tiny")

# beta-barrel pathway: SAM
xsam = 13.4
bio.arrow(ax, (xs + 0.4, yo - 1.25), (xsam - 0.2, yo - 0.6), kind="process", color=ink, bend=-0.25)
CB.channel(ax, xsam, yo, token="bacterium", width=1.4)
bio.label(ax, (xsam, yo + 1.0), "SAM (Sam50)", size="tiny", bold=True)
ax.add_patch(Rectangle((xsam + 1.0, yo - MH), 0.6, 2 * MH, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"), lw=0.8, zorder=12))
bio.label(ax, (xsam + 1.3, yo + 0.65), "β-barrel", size="tiny")

# MIA disulfide relay
xm = 17.2
bio.protein(ax, (xm, yo - 1.6), 1.1, 0.7, "antibody", wobble=0.07, text="Mia40")
bio.protein(ax, (xm + 1.5, yo - 1.6), 0.9, 0.6, "metabolite", wobble=0.07, text="Erv1")
bio.label(ax, (xm, yo - 2.4), "S–S formed: protein trapped", size="tiny")
bio.arrow(ax, (xt + 0.5, yo - 0.5), (xm - 0.6, yo - 1.3), kind="process", color=ink, bend=-0.08, dashed=True)

# Oxa1
xo = 21.0
CB.channel(ax, xo, yi, token="protein", width=1.2)
bio.label(ax, (xo, yi - 1.0), "Oxa1", size="tiny", bold=True)
bio.arrow(ax, (xo - 1.6, 1.4), (xo - 0.3, yi - 0.55), kind="process", color=ink, bend=-0.2)
bio.label(ax, (xo - 1.7, 1.1), "from matrix (mtDNA-encoded)", size="tiny")

# pathway names
for x, t in ((xt, "presequence"), (x22, "carrier"), (xsam, "β-barrel"), (xm + 0.7, "disulfide relay"), (xo, "insertion from matrix")):
    bio.label(ax, (x, 10.4), t, size="small", bold=True, color=P.muted())
