"""The prokaryotic cytoskeleton (schematic).

A: a rod-shaped bacterium (Escherichia coli, Bacillus subtilis): MreB, an actin homolog, forms short
membrane-bound filaments that move around the cell circumference together with the cell-wall synthesis
machinery, inserting peptidoglycan hoops that keep the rod shape; FtsZ, a tubulin homolog, forms the
treadmilling Z ring at midcell that recruits the divisome. B: plasmid segregation by ParM, an actin homolog:
a bipolar spindle of antiparallel ParM filaments, each capped by the ParR/parC complex on a plasmid, pushes
the two plasmids to opposite poles; ParM filaments show dynamic instability (their ATP cap). C: crescentin,
an intermediate-filament-like coiled-coil protein of Caulobacter crescentus, lies along the inner curvature
and bends the cell into a crescent.
"""

import numpy as np

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import cytoskel as C
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(25.0, 7.6)

bio.panel(ax, "A", (0.1, 7.5))
M.bacillus(ax, (4.6, 3.8), 7.2, 2.6)
for k, x in enumerate(np.linspace(2.0, 7.2, 6)):
    y0 = 2.8 if k % 2 else 4.8
    ax.plot([x - 0.25, x + 0.25], [y0 - 0.15, y0 + 0.15], color=P.edge("actin"), lw=3.2, solid_capstyle="round", zorder=20)
    bio.arrow(ax, (x + 0.1, y0 - 0.55 if k % 2 == 0 else y0 + 0.55), (x + 0.1, y0 - 0.95 if k % 2 == 0 else y0 + 0.95),
              kind="process", head=0.14, lw=0.8, color=P.muted())
for y in np.linspace(2.75, 4.85, 7):
    ax.add_patch(Circle((4.6, y), 0.13, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.6, zorder=21))
bio.callout(ax, (4.6, 4.9), (6.0, 6.7), "FtsZ ring (tubulin homolog)", size="tiny")
bio.callout(ax, (2.0, 4.8), (0.6, 6.7), "MreB filaments (actin homolog)", size="tiny")
bio.label(ax, (4.6, 0.9), "rod shape and division", size="small")

bio.panel(ax, "B", (9.3, 7.5))
M.bacillus(ax, (13.2, 3.8), 6.4, 2.2)
for y in (3.55, 3.8, 4.05):
    ax.plot([11.0, 15.4], [y, y], color=P.edge("enzyme"), lw=2.0, zorder=20)
for x in (10.7, 15.7):
    ax.add_patch(Circle((x, 3.8), 0.42, facecolor="none", edgecolor=P.edge("dna"), lw=1.6, zorder=21))
    bio.protein(ax, (x + (0.35 if x < 13 else -0.35), 3.8), 0.3, 0.5, "antibody")
bio.arrow(ax, (12.2, 5.2), (10.8, 5.2), kind="process", head=0.16)
bio.arrow(ax, (14.2, 5.2), (15.6, 5.2), kind="process", head=0.16)
bio.label(ax, (13.2, 5.75), "ParM filaments push plasmids apart", size="tiny")
bio.label(ax, (13.2, 0.9), "plasmid segregation", size="small")

bio.panel(ax, "C", (17.8, 7.5))
M.vibrio(ax, (21.3, 3.6), 6.0, 1.5, bend=0.55, flagella=None)
# crescentin along the inner (concave, upper) side, just inside the envelope
xx = np.linspace(19.3, 23.3, 60)
inner = np.c_[xx, 3.82 + 0.42 * ((xx - 21.3) / 2.2) ** 2]
ax.plot(inner[:, 0], inner[:, 1], color=P.edge(C.tok("if")), lw=2.6, solid_capstyle="round", zorder=20)
bio.callout(ax, tuple(inner[30]), (21.3, 6.6), "crescentin (IF-like)", size="tiny")
bio.label(ax, (21.3, 0.9), "Caulobacter: curvature", size="small")
