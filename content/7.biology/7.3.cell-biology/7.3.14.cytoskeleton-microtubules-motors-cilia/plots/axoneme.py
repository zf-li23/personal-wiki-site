"""Cilia and flagella (schematic).

A: a motile axoneme in cross-section, viewed from the base towards the tip: nine outer doublets (complete A
tubule with 13 protofilaments, incomplete B tubule with 10) around a central pair of singlet microtubules;
outer and inner dynein arms on each A tubule reach towards the B tubule of the next doublet; radial spokes
(gold) run to the central sheath; nexin-dynein regulatory complexes (grey) link neighbouring doublets.
B: a primary cilium (9+0): no central pair, no dynein arms; a sensory antenna.
C: why sliding becomes bending. Dynein arms on one doublet walk towards the minus end (the base) of the
neighbouring doublet and push it towards the tip. Left: when the links between doublets have been digested
by protease, doublets slide apart (telescoping), as Summers and Gibbons (1971) observed after adding ATP.
Right: in the intact axoneme the nexin links and the basal body resist sliding and the sliding is converted
into bending.
D: intraflagellar transport: kinesin-2 carries IFT trains with axonemal cargo to the tip; dynein-2 brings
them back to the base; the transition zone at the base gates which membrane proteins enter.
"""

import numpy as np

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(26.0, 11.0)

bio.panel(ax, "A", (0.1, 10.9))
an = C.axoneme(ax, (4.2, 6.2), 2.6, kind="9+2")
c0 = np.array([4.2, 6.2])
A = [d["A"] for d in an["doublets"]]
bio.callout(ax, an["doublets"][1]["B"], (7.4, 10.5), "outer doublet (A + B tubules)", size="tiny")
bio.callout(ax, an["outer_arm"], (1.0, 10.5), "outer dynein arm", size="tiny")
bio.callout(ax, A[7] + (A[7] - c0) * -0.12, (0.2, 8.8), "inner dynein arm", size="tiny")
bio.callout(ax, c0 + (A[3] - c0) * 0.55, (8.6, 4.3), "radial spoke", size="tiny")
bio.callout(ax, c0 + (0.3, -0.25), (6.6, 1.6), "central pair", size="tiny")
bio.callout(ax, (A[5] + A[6]) / 2 + (0, 0.25), (1.6, 1.6), "nexin link", size="tiny")
bio.label(ax, (4.2, 2.35), "9 + 2 (motile)", size="small")

bio.panel(ax, "B", (9.6, 10.9))
C.axoneme(ax, (12.0, 7.9), 1.5, kind="9+0", arms=False, spokes=False)
bio.label(ax, (12.0, 5.55), "9 + 0 (primary cilium)", size="small")

bio.panel(ax, "C", (9.6, 4.9))
# protease-treated: telescoping
for k, (x0, dx) in enumerate(((10.2, 0.0), (10.75, 1.6))):
    ax.plot([x0, x0], [1.0 + dx, 4.0 + dx], color=P.edge("channel"), lw=4.5, solid_capstyle="round", zorder=8)
for y in (1.8, 2.6, 3.4):
    bio.protein(ax, (10.47, y + 0.4), 0.28, 0.18, C.tok("dynein"))
bio.arrow(ax, (11.4, 3.5), (11.4, 5.0), kind="process")
bio.label(ax, (10.5, 0.55), "protease-treated:\nsliding", size="tiny")
# intact: bending
s = np.linspace(0, 1, 60)
for off in (0.0, 0.5):
    xx = 13.4 + off + 1.6 * s**2
    yy = 1.0 + 3.6 * s
    ax.plot(xx, yy, color=P.edge("channel"), lw=4.5, solid_capstyle="round", zorder=8)
for t in (0.3, 0.6, 0.85):
    p0 = (13.4 + 1.6 * t**2, 1.0 + 3.6 * t)
    ax.plot([p0[0], p0[0] + 0.5], [p0[1], p0[1]], color=P.edge(C.tok("nexin")), lw=1.2, zorder=9)
ax.add_patch(FancyBboxPatch((13.0, 0.6), 1.3, 0.4, boxstyle="round,pad=0,rounding_size=0.1",
                                     facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=9))
bio.label(ax, (14.8, 0.55), "intact (nexin links,\nbasal body): bending", size="tiny", ha="left")

bio.panel(ax, "D", (17.0, 10.9))
base_y, tip_y = 1.6, 9.6
from matplotlib.patches import Rectangle
ax.add_patch(FancyBboxPatch((19.0, base_y), 3.2, tip_y - base_y, boxstyle="round,pad=0,rounding_size=1.4",
                                     facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=2.4, zorder=2))
for x in (19.7, 21.5):
    C.mt_line(ax, (x, base_y + 0.2), (x, tip_y - 0.8), lw=2.6, zorder=4)
C.centriole(ax, (20.6, base_y - 0.4), length=1.0, width=1.8, angle=90)
bio.label(ax, (23.2, base_y - 0.4), "basal body", size="tiny", ha="left")
ax.plot([18.9, 22.3], [base_y + 0.55] * 2, color=P.muted(), lw=1.0, ls=(0, (2, 1.5)), zorder=5)
bio.label(ax, (23.2, base_y + 0.6), "transition zone", size="tiny", ha="left")
for y in (3.2, 5.6):
    bio.protein(ax, (19.95, y), 0.32, 0.26, C.tok("kinesin"))
    ax.add_patch(FancyBboxPatch((19.75, y + 0.18), 0.5, 0.7, boxstyle="round,pad=0,rounding_size=0.12",
                                         facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=11))
for y in (4.4, 7.0):
    bio.protein(ax, (21.25, y), 0.36, 0.3, C.tok("dynein"))
    ax.add_patch(FancyBboxPatch((20.92, y - 0.95), 0.5, 0.7, boxstyle="round,pad=0,rounding_size=0.12",
                                         facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=11))
bio.arrow(ax, (18.6, 3.0), (18.6, 7.5), kind="process")
bio.label(ax, (18.4, 5.3), "kinesin-2\n(anterograde)", size="tiny", ha="right")
bio.arrow(ax, (22.6, 7.5), (22.6, 3.0), kind="process")
bio.label(ax, (22.8, 5.3), "dynein-2\n(retrograde)", size="tiny", ha="left")
bio.label(ax, (20.6, 10.2), "tip (plus ends)", size="tiny")
bio.label(ax, (20.6, 8.75), "IFT trains with cargo", size="tiny")
