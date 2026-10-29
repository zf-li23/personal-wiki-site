"""Blastulae of the model species in section, coloured by the germ layer each region will form (animal pole
up). Sea urchin: a hollow sphere one cell thick, the vegetal plate thickened (skeletogenic micromere
descendants red, endoderm yellow). Frog: a multilayered animal cap over a blastocoel displaced towards the
animal pole, marginal zone (prospective mesoderm), large yolky vegetal cells. Zebrafish: the blastoderm on
the yolk cell, covered by the enveloping layer, with the yolk syncytial layer beneath. Chick: the area
pellucida over the subgerminal cavity, the area opaca resting on the yolk, hypoblast islands and Koller's
sickle at the posterior edge (right). Drosophila: the cellular blastoderm around the yolk, pole cells at the
posterior end (right). Mouse: the blastocyst, with the inner cell mass already split into epiblast and
primitive endoderm."""
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(24, 13.2)
y1, y2 = 9.6, 3.2
a = E.blastula(ax, (3.0, y1), 1.6, "sea-urchin")
bio.label(ax, (3.0, 12.7), "Sea urchin", size="title", bold=True)
bio.callout(ax, a["blastocoel"], (0.5, 11.8), "Blastocoel", size="tiny")
bio.callout(ax, a["vegetal_plate"], (5.4, 7.6), "Vegetal plate", size="tiny")
bio.callout(ax, a["skeletogenic"], (3.0, 7.35), "Micromere\ndescendants", size="tiny")
bio.callout(ax, a["hyaline"], (5.6, 11.9), "Hyaline layer", size="tiny")

a = E.blastula(ax, (11.0, y1), 1.6, "frog")
bio.label(ax, (11.0, 12.7), "Frog (Xenopus)", size="title", bold=True)
bio.callout(ax, a["animal_cap"], (8.3, 12.0), "Animal cap", size="tiny")
bio.callout(ax, a["blastocoel"], (13.6, 12.0), "Blastocoel", size="tiny")
bio.callout(ax, a["marginal_zone"], (13.7, 9.0), "Marginal zone", size="tiny")
bio.callout(ax, a["vegetal"], (13.5, 7.6), "Vegetal cells", size="tiny")

a = E.blastula(ax, (19.5, y1 + 0.2), 1.7, "zebrafish")
bio.label(ax, (19.5, 12.7), "Zebrafish", size="title", bold=True)
bio.callout(ax, a["evl"], (17.0, 12.0), "Enveloping layer", size="tiny")
bio.callout(ax, a["deep"], (22.4, 12.0), "Deep cells", size="tiny")
bio.callout(ax, a["ysl"], (22.6, 10.3), "Yolk syncytial\nlayer", size="tiny")
bio.callout(ax, a["yolk"], (22.4, 7.6), "Yolk cell", size="tiny")

a = E.blastula(ax, (4.0, y2 + 0.4), 1.75, "chick")
bio.label(ax, (4.0, 6.0), "Chick", size="title", bold=True)
bio.callout(ax, a["area_pellucida"], (2.4, 5.2), "Area pellucida", size="tiny")
bio.callout(ax, a["area_opaca"], (0.4, 4.6), "Area opaca", size="tiny")
bio.callout(ax, a["subgerminal_cavity"], (4.0, 1.4), "Subgerminal cavity", size="tiny")
bio.callout(ax, a["hypoblast"], (1.4, 1.9), "Hypoblast islands", size="tiny")
bio.callout(ax, a["kollers_sickle"], (6.5, 5.2), "Koller's sickle", size="tiny")
bio.label(ax, (7.2, y2 + 1.0), "posterior", size="tiny", color=P.muted())

a = E.blastula(ax, (12.2, y2), 1.35, "fly")
bio.label(ax, (12.2, 6.0), "Drosophila", size="title", bold=True, italic=True)
bio.callout(ax, a["blastoderm"], (10.4, 5.0), "Cellular blastoderm", size="tiny")
bio.callout(ax, a["yolk"], (12.4, 1.0), "Yolk", size="tiny")
bio.callout(ax, a["pole_cells"], (14.9, 4.6), "Pole cells", size="tiny")
bio.callout(ax, a["ventral"], (10.0, 1.2), "Prospective\nmesoderm", size="tiny")

a = E.blastula(ax, (20.2, y2), 1.5, "mouse")
bio.label(ax, (20.2, 6.0), "Mouse", size="title", bold=True)
bio.callout(ax, a["epiblast"], (22.6, 5.3), "Epiblast", size="tiny")
bio.callout(ax, a["primitive_endoderm"], (23.0, 4.4), "Primitive\nendoderm", size="tiny")
bio.callout(ax, a["mural_te"], (22.8, 1.2), "Trophectoderm", size="tiny")
bio.callout(ax, a["blastocoel"], (18.0, 0.8), "Blastocoel", size="tiny")
bio.callout(ax, a["zona"], (17.3, 5.2), "Zona pellucida", size="tiny")
E.legend(ax, (6.2, 0.35), ("ectoderm", "mesoderm", "endoderm", "yolk", "epiblast", "hypoblast", "trophoblast", "germline"), step=2.05,
         size="tiny", swatch=0.26)
