"""Extraembryonic membranes and the placenta. A: a bird egg at about day 5. The embryo lies in the
fluid-filled amnion; the chorion lines the shell; the allantois, an outgrowth of the hindgut, spreads under
the chorion (forming the chorioallantoic membrane that exchanges gases through the shell) and stores
waste; the yolk sac, its blood vessels spreading over the yolk, absorbs nutrients. B: a chorionic villus of
the human placenta (haemochorial type). Maternal blood enters the intervillous space from spiral arteries
and drains through endometrial veins; fetal blood arrives through the umbilical arteries (deoxygenated,
blue) and returns through the umbilical vein (oxygenated, red) in capillaries inside the villi. The two
circulations do not mix: oxygen and nutrients cross the syncytiotrophoblast covering of the villus into
fetal blood, and carbon dioxide and waste the other way."""
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(23, 9.4)
bio.label(ax, (0.4, 9.0), "A  Bird egg, about day 5", size="small", bold=True, ha="left")
a = E.amniote_egg(ax, (5.2, 4.4), 3.2)
bio.callout(ax, a["amnion"], (0.5, 5.4), "Amnion", size="tiny")
bio.callout(ax, a["embryo"], (3.0, 8.4), "Embryo", size="tiny")
bio.callout(ax, a["chorion"], (8.8, 8.4), "Chorion", size="tiny")
bio.callout(ax, a["allantois"], (10.2, 6.2), "Allantois", size="tiny")
bio.callout(ax, a["yolk_sac"], (0.4, 3.9), "Yolk sac", size="tiny")
bio.callout(ax, a["yolk"], (7.4, 0.6), "Yolk", size="tiny")
bio.callout(ax, a["albumen"], (0.4, 1.2), "Albumen", size="tiny")
bio.callout(ax, a["shell"], (0.5, 6.4), "Shell", size="tiny")

bio.label(ax, (12.0, 9.0), "B  Human chorionic villus", size="small", bold=True, ha="left")
v = E.villus(ax, (12.2, 0.9, 9.4, 7.4))
bio.callout(ax, v["spiral_artery"], (12.0, 0.4), "Spiral artery", size="tiny")
bio.callout(ax, v["vein"], (22.6, 0.4), "Endometrial vein", size="tiny")
bio.callout(ax, v["intervillous"], (12.0, 5.4), "Intervillous space\n(maternal blood)", size="tiny")
bio.callout(ax, v["villus"], (22.5, 4.5), "Villus: syncytiotrophoblast\nover fetal capillaries", size="tiny")
bio.callout(ax, v["umbilical_artery"], (12.0, 8.6), "Umbilical arteries", size="tiny")
bio.callout(ax, v["umbilical_vein"], (22.6, 8.6), "Umbilical vein", size="tiny")
bio.label(ax, (16.9, 1.55), "decidua (maternal)", size="tiny", color=P.muted())
bio.label(ax, (16.9, 8.25), "chorionic plate (fetal)", size="tiny", color=P.muted())
bio.arrow(ax, (14.4, 3.3), (15.4, 3.9), kind="process", head=0.15, color=P.edge("blood"))
bio.label(ax, (13.6, 2.95), "O₂, nutrients", size="tiny", color=P.edge("blood"))
bio.arrow(ax, (19.4, 3.9), (20.4, 3.3), kind="process", head=0.15, color=P.edge("dna"))
bio.label(ax, (21.0, 2.95), "CO₂, urea", size="tiny", color=P.edge("dna"))
