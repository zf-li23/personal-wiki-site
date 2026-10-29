"""Gastrulation in the chick. A: the blastoderm seen from above at the definitive-streak stage (about 18 h of
incubation, anterior up): the primitive streak extends from the posterior margin of the area pellucida to
Hensen's node, and epiblast cells on both sides converge on it (arrows). B: the fate of ingressing cells
depends on where and when they pass through the streak (schematic, after fate-mapping studies). Cells
through the node and anterior streak form endoderm, prechordal mesoderm, notochord and somites; cells
through progressively more posterior levels form intermediate, lateral plate and extraembryonic mesoderm.
C: regression: the node moves posteriorly, laying down the notochord in its wake, while somites form on both
sides; the streak shortens."""
import numpy as np
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(23, 9.6)
bio.label(ax, (0.4, 9.2), "A  Definitive streak (from above)", size="small", bold=True, ha="left")
a = E.streak(ax, (4.0, 4.6), 3.5)
bio.callout(ax, a["node"], (7.8, 7.4), "Hensen's node", size="tiny")
bio.callout(ax, a["streak"], (7.9, 4.0), "Primitive streak\n(with groove)", size="tiny")
bio.callout(ax, a["area_pellucida"], (0.3, 7.9), "Area pellucida", size="tiny")
bio.callout(ax, a["area_opaca"], (0.4, 1.0), "Area opaca", size="tiny")
bio.label(ax, (4.0, 8.4), "anterior", size="tiny", color=P.muted())
bio.label(ax, (4.0, 0.8), "posterior", size="tiny", color=P.muted())

bio.label(ax, (9.6, 9.2), "B  Fate by level of ingression", size="small", bold=True, ha="left")
levels = [("node", "endoderm, prechordal\nplate, notochord", "endoderm"), ("anterior streak", "somites (paraxial)", "mesoderm"),
          ("middle streak", "intermediate mesoderm,\nheart", "mesoderm"), ("posterior streak", "lateral plate", "mesoderm"),
          ("posterior end", "extraembryonic\nmesoderm, blood", "extraembryonic-mesoderm")]
x0, ytop = 11.2, 8.0
for k, (lvl, fate, t) in enumerate(levels):
    y = ytop - 1.45 * k
    bio.box(ax, (x0, y), 2.4, 0.8, E.tok(t), lvl, size="tiny")
    bio.arrow(ax, (x0 + 1.3, y), (x0 + 2.1, y), kind="process", head=0.15)
    bio.label(ax, (x0 + 2.25, y), fate, size="tiny", ha="left")
bio.label(ax, (x0, 0.6), "later ingression: more lateral, more posterior fates", size="tiny", color=P.muted())

bio.label(ax, (17.6, 9.2), "C  Regression", size="small", bold=True, ha="left")
for k, (yn, ns) in enumerate(((7.0, 0), (5.6, 3), (4.4, 6))):
    xc = 18.6 + 1.8 * k
    ax.plot([xc, xc], [1.4, yn], color=P.edge("mesoderm"), lw=3.0, solid_capstyle="round", zorder=5)
    ax.plot([xc, xc], [yn, 8.0], color=P.edge("channel"), lw=2.0, zorder=5)
    ax.add_patch(Circle((xc, yn), 0.2, facecolor=P.fill("mesoderm"), edgecolor=P.edge("mesoderm"), zorder=6))
    for j in range(ns):
        for s in (-1, 1):
            bio.box(ax, (xc + s * 0.42, 7.6 - 0.55 * j), 0.42, 0.42, "muscle", None, radius=0.06)
bio.label(ax, (21.6, 8.4), "notochord (blue)\nand somites", size="tiny", color=P.muted())
bio.arrow(ax, (17.7, 6.8), (17.7, 4.6), kind="process", head=0.18, color=P.muted())
bio.label(ax, (17.5, 5.7), "node moves\nposteriorly", size="tiny", color=P.muted(), ha="right")
