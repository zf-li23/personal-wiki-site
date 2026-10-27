"""Three ways to polarize a cell (schematic).

A: budding yeast. Cdc42-GTP (red) at a random spot recruits a scaffold (Bem1) that carries its own GEF
(Cdc24) and the kinase PAK: positive feedback concentrates active Cdc42 at one site, which competes with
others for the limited pool of Cdc42 and GEF until a single cap wins. The cap activates the formin Bni1, which
nucleates actin cables (plus ends at the cap) along which myosin V carries secretory vesicles to the
growing bud; septins form a ring at the bud neck.
B: the one-cell Caenorhabditis elegans embryo. The sperm centrosome marks the posterior; local loss of
Rho activity and actomyosin contraction there make the cortex flow anteriorly, carrying the anterior PAR
proteins (PAR-3, PAR-6, aPKC, Cdc42) forward; the posterior PAR proteins (PAR-1, PAR-2) bind the cleared
posterior cortex. The two domains exclude each other (aPKC phosphorylates PAR-1 and PAR-2; PAR-1
phosphorylates PAR-3).
C: an epithelial cell. The PAR and Crumbs complexes define the apical domain, the Scribble module
(Scribble, Dlg, Lgl) the basolateral domain, with mutual antagonism; tight and adherens junctions separate
the two domains (7.3.23).
"""

import numpy as np

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(26.0, 9.6)

# ---- A: yeast
bio.panel(ax, "A", (0.1, 9.5))
mother = bio.blob((3.6, 4.0), 2.4, 2.3, wobble=0.03, seed=2, k=10)
bio.membrane(ax, mother, "cytoplasm")
bud = bio.blob((3.6, 7.0), 1.0, 0.9, wobble=0.03, seed=4, k=9)
bio.membrane(ax, bud, "cytoplasm", zorder=3)
for x in (2.95, 4.25):
    ax.add_patch(Ellipse((x, 6.2), 0.22, 0.32, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.6, zorder=12))
bio.label(ax, (4.6, 6.15), "septin ring", size="tiny", ha="left")
th = np.linspace(np.pi * 0.25, np.pi * 0.75, 30)
cap = np.c_[3.6 + 0.88 * np.cos(th), 7.0 + 0.78 * np.sin(th)]
ax.plot(cap[:, 0], cap[:, 1], color=P.edge("negative"), lw=4.5, solid_capstyle="round", zorder=13)
bio.label(ax, (3.6, 8.25), "Cdc42-GTP cap", size="tiny")
for x0 in (2.2, 3.0, 4.2, 5.0):
    C.filament(ax, (x0, 2.6), (3.6 + (x0 - 3.6) * 0.15, 7.4), lw=1.3, plus="dot", zorder=9)
for k, p in enumerate(((3.25, 4.8), (3.95, 5.6), (3.45, 3.6))):
    bio.vesicle(ax, p, 0.17)
bio.label(ax, (6.3, 3.6), "actin cables\n(formin), myosin V\ncarries vesicles", size="tiny", ha="left")
bio.label(ax, (3.6, 1.0), "positive feedback:\nCdc42-GTP → Bem1–GEF → Cdc42-GTP", size="tiny")

# ---- B: C. elegans zygote
bio.panel(ax, "B", (8.9, 9.5))
cx, cy = 13.2, 5.0
emb = bio.blob((cx, cy), 3.6, 2.2, wobble=0.01, seed=1, k=12)
bio.membrane(ax, emb, "cytoplasm")
th = np.linspace(0, 2 * np.pi, 300)
ex, ey = cx + 3.48 * np.cos(th), cy + 2.1 * np.sin(th)
ant = np.cos(th) < -0.05
pos = np.cos(th) > 0.25
ax.plot(np.where(ant, ex, np.nan), np.where(ant, ey, np.nan), color=P.edge("negative"), lw=4, zorder=12)
ax.plot(np.where(pos, ex, np.nan), np.where(pos, ey, np.nan), color=P.edge("positive"), lw=4, zorder=12)
bio.label(ax, (10.2, 7.7), "anterior PAR: PAR-3, PAR-6,\naPKC, Cdc42", size="tiny")
bio.label(ax, (16.2, 7.7), "posterior PAR:\nPAR-1, PAR-2", size="tiny")
C.centrosome(ax, (15.9, 5.0), size=0.22, microtubules=8, length=0.9, centrioles=False, lw=0.8)
bio.label(ax, (15.9, 4.25), "sperm\ncentrosome", size="tiny")
bio.nucleus(ax, (11.2, 5.0), 0.55, chromatin=False, nucleolus=False)
for y in (6.4, 3.6):
    bio.arrow(ax, (14.6, y), (12.0, y), kind="process", color=P.muted(), head=0.18)
bio.label(ax, (13.3, 5.0), "cortical flow", size="tiny", color=P.muted())
bio.label(ax, (9.3, 2.3), "anterior", size="tiny", ha="left")
bio.label(ax, (17.1, 2.3), "posterior", size="tiny", ha="right")

# ---- C: epithelial cell
bio.panel(ax, "C", (18.6, 9.5))
x0, x1, y0, y1 = 20.3, 23.6, 1.6, 8.0
outline = bio.smooth_closed([(x0, y1), ((x0 + x1) / 2, y1 + 0.15), (x1, y1), (x1 + 0.05, (y0 + y1) / 2), (x1, y0),
                             ((x0 + x1) / 2, y0 - 0.1), (x0, y0), (x0 - 0.05, (y0 + y1) / 2)], n=300)
bio.membrane(ax, outline, "cytoplasm")
bio.nucleus(ax, ((x0 + x1) / 2, 3.2), 0.75, chromatin=False, nucleolus=False)
ax.plot([x0 + 0.2, x1 - 0.2], [y1 + 0.1, y1 + 0.1], color=P.edge("negative"), lw=4.5, solid_capstyle="round", zorder=12)
for xx in (x0 - 0.05, x1 + 0.05):
    ax.plot([xx, xx], [y0 + 0.2, 6.6], color=P.edge("positive"), lw=4.5, solid_capstyle="round", zorder=12)
    ax.add_patch(Rectangle((xx - 0.14, 7.3), 0.28, 0.35, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                                    lw=0.6, zorder=13))
    ax.add_patch(Rectangle((xx - 0.14, 6.75), 0.28, 0.35, facecolor=P.fill("protein"), edgecolor=P.edge("protein"),
                                    lw=0.6, zorder=13))
bio.label(ax, ((x0 + x1) / 2, 8.75), "apical: PAR, Crumbs", size="tiny")
bio.label(ax, (x1 + 0.3, 7.5), "tight junction", size="tiny", ha="left")
bio.label(ax, (x1 + 0.3, 6.9), "adherens junction", size="tiny", ha="left")
bio.label(ax, (x1 + 0.3, 4.4), "basolateral:\nScribble, Dlg, Lgl", size="tiny", ha="left")
bio.label(ax, ((x0 + x1) / 2, 1.0), "basal (matrix)", size="tiny", color=P.muted())
