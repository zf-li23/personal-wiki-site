# The three main vesicle coats. A: where they act: COPII (green) buds vesicles from ER exit sites towards the
# Golgi; COPI (blue) returns vesicles from the Golgi to the ER and between cisternae; clathrin (yellow) with
# AP1 buds from the trans-Golgi network towards endosomes and with AP2 from the plasma membrane (endocytosis).
# B: the coats in section, with their small GTPase, inner (adaptor) layer and outer layer.
import numpy as np
import wikibio as bio
from wikibio import traffic as T

fig, ax = bio.canvas(22, 10.5)
P = bio.P
bio.panel(ax, "A", (0.2, 10.3))
cell = bio.cell(ax, (5.6, 5.0), 5.3, 4.6, kind="animal", seed=3)
bio.nucleus(ax, (2.2, 5.0), 1.4, pores=10)
bio.er(ax, (4.6, 5.0), 2.6, 1.4, sheets=4, angle=90)
bio.golgi(ax, (7.3, 5.0), 2.4, cisternae=5, angle=-90)
bio.vesicle(ax, (8.0, 8.0), 0.55, token="vesicle", cargo="highlight")
bio.label(ax, (8.0, 8.85), "Endosome", size="small")
bio.label(ax, (4.6, 2.4), "ER", size="small")
bio.label(ax, (7.3, 3.0), "Golgi", size="small")
bio.label(ax, (2.2, 2.9), "Nucleus", size="small")
col = {"copii": P.edge(T.tok("copii_outer")), "copi": P.edge(T.tok("copi")), "clathrin": P.edge(T.tok("clathrin"))}
for (a, b, k, bend) in (((5.3, 5.6), (6.6, 5.6), "copii", 0.15), ((6.6, 4.4), (5.3, 4.4), "copi", 0.15),
                        ((7.6, 3.7), (7.6, 6.3), "copi", -0.25), ((8.3, 6.0), (8.0, 7.35), "clathrin", -0.1),
                        ((10.5, 6.7), (8.6, 7.9), "clathrin", 0.15)):
    bio.arrow(ax, a, b, kind="process", color=col[k], bend=bend, lw=2.0)
for xy, k in (((5.95, 5.95), "copii"), ((5.95, 4.0), "copi"), ((8.4, 5.0), "copi"), ((8.55, 6.7), "clathrin"),
              ((9.6, 7.6), "clathrin")):
    T.coated_vesicle(ax, xy, 0.17, kind=None, thickness=0.06)
    ax.add_patch(bio.core.Circle(xy, 0.26, fill=False, edgecolor=col[k], lw=2.2, zorder=12))
bio.label(ax, (9.3, 8.75), "endocytosis\n(AP2)", size="tiny", ha="left")
bio.label(ax, (8.75, 4.2), "TGN → endosome\n(AP1)", size="tiny", ha="left")

bio.panel(ax, "B", (12.0, 10.3))
rows = [
    ("copii", "COPII", "Sar1 (GEF Sec12)", "Sec23/24 (cargo, Sar1 GAP)", "Sec13/31 cage", "ER → Golgi; 60–90 nm"),
    ("copi", "COPI", "Arf1 (GEF GBF1)", "coatomer F-subcomplex", "coatomer B-subcomplex", "Golgi → ER, intra-Golgi"),
    ("clathrin", "Clathrin", "Arf1 (AP1) / PI(4,5)P₂ (AP2)", "AP1, AP2, other adaptors", "clathrin triskelia", "TGN, plasma membrane → endosomes; 60–150 nm"),
]
for k, (kind, name, g, inner, outer, route) in enumerate(rows):
    y = 8.3 - k * 3.0
    T.coated_vesicle(ax, (13.4, y), 0.7, kind=kind, cargo=3)
    bio.label(ax, (14.9, y + 0.85), name, size="normal", bold=True, ha="left")
    for j, (h, txt) in enumerate((("GTPase", g), ("inner layer", inner), ("outer layer", outer), ("route", route))):
        bio.label(ax, (14.9, y + 0.35 - 0.42 * j), h, size="tiny", ha="left", color=P.muted())
        bio.label(ax, (16.4, y + 0.35 - 0.42 * j), txt, size="tiny", ha="left")
