"""Motor proteins on microtubules and their directions (schematic; plus end of every microtubule on the right).

A: kinesin-1 walks towards the plus end carrying a vesicle (anterograde in axons); cytoplasmic dynein-1, with
dynactin and an activating adaptor (such as BICD2), walks towards the minus end (retrograde).
B: kinesin-5, a bipolar tetramer with motor domains at both ends, cross-links antiparallel microtubules and,
walking towards both plus ends, slides each microtubule towards its minus end (pushing spindle poles apart).
C: kinesin-13 does not walk: at microtubule ends it bends the terminal tubulin dimers and depolymerizes them.
"""

import numpy as np

import wikibio as bio
from wikibio import cytoskel as C
from wikibio import physiology as phys

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)

bio.panel(ax, "A", (0.1, 9.3))
C.tube(ax, (0.6, 5.4), (15.0, 5.4), width=0.42)
C.end_label(ax, (15.4, 5.4), "+", size="small")
C.end_label(ax, (0.3, 5.4), "-", size="small")
neck = phys.kinesin(ax, (10.0, 5.85), (11.0, 5.85), (10.9, 7.5), head=0.55)
bio.vesicle(ax, (11.0, 8.25), 0.75)
bio.arrow(ax, (12.0, 7.0), (14.2, 7.0), kind="process")
bio.label(ax, (11.6, 9.2), "kinesin-1 (to plus end)", size="small")
C.dynein(ax, (4.0, 5.65), (4.1, 7.6), size=0.42)
bio.vesicle(ax, (4.1, 8.25), 0.7)
bio.arrow(ax, (2.8, 7.0), (0.9, 7.0), kind="process")
bio.label(ax, (4.0, 9.2), "dynein–dynactin–adaptor (to minus end)", size="small")

bio.panel(ax, "B", (0.1, 4.2))
C.tube(ax, (0.6, 3.1), (8.2, 3.1), width=0.36)
C.tube(ax, (11.5, 1.6), (3.9, 1.6), width=0.36)
C.end_label(ax, (8.55, 3.1), "+", size="tiny")
C.end_label(ax, (3.6, 1.6), "+", size="tiny")
for x in (5.2, 6.9):
    for y, s in ((2.85, -1), (1.85, 1)):
        bio.protein(ax, (x, y), 0.36, 0.24, C.tok("kinesin"))
    ax.plot([x, x], [2.7, 2.0], color=P.edge(C.tok("kinesin")), lw=2.0, zorder=11)
bio.arrow(ax, (0.9, 3.75), (0.3, 3.75), kind="process")
bio.arrow(ax, (11.0, 0.95), (11.6, 0.95), kind="process")
bio.label(ax, (6.0, 0.4), "kinesin-5 slides antiparallel microtubules apart", size="tiny")

bio.panel(ax, "C", (13.2, 4.2))
C.microtubule_lattice(ax, (13.8, 2.3), (21.0, 2.3), width=1.1, rows=5, plus_end="shrinking", dimer=0.55, ends=False)
bio.protein(ax, (21.5, 3.15), 0.6, 0.42, C.tok("kinesin"))
bio.protein(ax, (21.6, 1.35), 0.6, 0.42, C.tok("kinesin"))
bio.label(ax, (22.0, 2.3), "kinesin-13\n(MCAK)", size="tiny", ha="left")
bio.label(ax, (17.4, 0.4), "depolymerizes ends", size="tiny")
