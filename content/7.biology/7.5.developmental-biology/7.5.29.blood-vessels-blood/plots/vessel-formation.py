"""Three ways of making vessels and blood. A: vasculogenesis. In the yolk sac, mesodermal cells aggregate into
blood islands, whose inner cells become primitive blood cells and outer cells angioblasts; the islands and
scattered angioblasts coalesce into a primary capillary plexus (FGF2 induces hemangioblasts, VEGF-A acting
through VEGFR2/Flk1 makes angioblasts proliferate and form tubes). B: angiogenesis. An endothelial cell of an
existing vessel facing a gradient of VEGF-A becomes a tip cell, extends filopodia rich in VEGFR2 and migrates up
the gradient; the cells behind it, stalk cells, proliferate and form the lumen of the sprout. C: the
endothelial-to-hematopoietic transition. In the floor of the embryonic dorsal aorta (AGM region), hemogenic
endothelial cells (lilac) round up and leave the endothelium as clusters of hematopoietic stem and progenitor
cells (purple) that bud into the lumen (mouse, human) or, in zebrafish, into the space beneath the aorta."""
import numpy as np
import wikibio as bio
from wikibio import organogenesis as O

P = bio.P
fig, ax = bio.canvas(27, 9.5)
bio.panel(ax, "A", (0.2, 9.3))
b = O.blood_island(ax, (1.9, 6.0), 1.0, seed=2)
O.blood_island(ax, (4.0, 7.3), 0.7, n=4, seed=5)
bio.callout(ax, b["angioblast"], (3.5, 4.2), "Angioblasts")
bio.callout(ax, b["blood"], (0.5, 8.6), "Primitive blood cells")
bio.arrow(ax, (3.2, 3.6), (3.2, 2.7), kind="process", color=P.muted())
O.plexus(ax, (0.6, 0.4, 5.6, 2.2), cell=0.8)
bio.label(ax, (7.0, 1.5), "primary\nplexus", size="tiny", ha="left")

bio.panel(ax, "B", (9.0, 9.3))
for k in range(16):  # VEGF gradient (dots denser towards the top)
    pass
rng = np.random.default_rng(3)
pts = rng.uniform([9.4, 2.4], [16.8, 8.8], (220, 2))
keep = rng.random(len(pts)) < (pts[:, 1] - 2.0) / 7.5
for p in pts[keep]:
    ax.add_patch(bio.core.Circle(tuple(p), 0.05, facecolor=P.fill("atp"), edgecolor="none", zorder=2))
s = O.sprout(ax, (13.0, 1.6), 88, 4.0, stalk=4)
bio.callout(ax, s["tip"], (16.4, 7.4), "Tip cell")
bio.callout(ax, s["filopodium"], (10.0, 8.8), "Filopodia (VEGFR2)")
bio.callout(ax, s["stalk"], (16.2, 4.0), "Stalk cells")
bio.label(ax, (17.2, 8.9), "VEGF-A", size="small", ha="right", color=P.edge("atp"))
bio.label(ax, (13.0, 0.6), "existing vessel", size="tiny", color=P.muted())

bio.panel(ax, "C", (18.4, 9.3))
a = O.aorta_section(ax, (22.6, 5.4), 2.0)
bio.callout(ax, a["hemogenic"], (19.0, 1.2), "Hemogenic endothelium")
bio.callout(ax, a["cluster"], (26.6, 1.4), "Intra-aortic cluster")
bio.callout(ax, a["eht"], (26.8, 3.6), "Cell rounding up")
bio.callout(ax, a["endothelium"], (26.4, 8.9), "Dorsal aorta endothelium")
bio.label(ax, (22.6, 9.0), "dorsal", size="tiny", color=P.muted())
