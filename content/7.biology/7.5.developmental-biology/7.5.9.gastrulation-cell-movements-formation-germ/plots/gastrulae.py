"""Gastrulae of the model species in section, coloured by germ layer (ectoderm blue, mesoderm red, endoderm
yellow). Sea urchin: the archenteron invaginated from the vegetal plate, primary mesenchyme cells in the
blastocoel, secondary mesenchyme at the archenteron tip extending filopodia to the animal wall. Frog
(mid-gastrula, sagittal, dorsal right): bottle cells at the dorsal lip, mesoderm that has involuted under
the dorsal ectoderm, the archenteron, the shrinking blastocoel and the yolk plug. Zebrafish (shield stage,
dorsal right): the blastoderm covering about 60 % of the yolk, the germ ring of involuted hypoblast, the
shield on the dorsal side, the enveloping layer and the yolk syncytial layer. Chick (transverse section
through the primitive streak): epiblast cells converge on the streak, ingress through the primitive groove
and spread as mesoderm, while others enter the lower layer as endoderm and displace the hypoblast. Mouse
(egg cylinder at about E7, anterior left): epiblast cup around the proamniotic cavity, extraembryonic
ectoderm above, visceral endoderm outside, the anterior visceral endoderm, mesoderm leaving the primitive
streak on the posterior side, and the node at the distal tip. Human (about day 14): the bilaminar disc
between amniotic cavity and yolk sac, suspended by the connecting stalk in the chorionic cavity, within
the trophoblast invading the endometrium."""
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(24, 15.2)
ax.set_ylim(-0.6, 14.6)
a = E.gastrula(ax, (3.2, 10.6), 1.75, "sea-urchin")
bio.label(ax, (3.2, 14.1), "Sea urchin", size="title", bold=True)
bio.callout(ax, a["archenteron"], (0.4, 8.0), "Archenteron", size="tiny")
bio.callout(ax, a["pmc"], (0.3, 12.8), "Primary\nmesenchyme", size="tiny")
bio.callout(ax, a["smc"], (5.6, 13.6), "Secondary mesenchyme", size="tiny")
bio.callout(ax, a["blastopore"], (5.6, 8.3), "Blastopore", size="tiny")
bio.callout(ax, a["blastocoel"], (6.0, 12.4), "Blastocoel", size="tiny")

a = E.gastrula(ax, (11.6, 10.6), 1.75, "frog")
bio.label(ax, (11.6, 14.1), "Frog (Xenopus)", size="title", bold=True)
bio.callout(ax, a["ectoderm"], (8.6, 13.4), "Ectoderm", size="tiny")
bio.callout(ax, a["mesoderm"], (13.9, 13.0), "Involuted\nmesoderm", size="tiny")
bio.callout(ax, a["archenteron"], (14.4, 11.9), "Archenteron", size="tiny")
bio.callout(ax, a["blastocoel"], (8.2, 11.4), "Blastocoel", size="tiny")
bio.callout(ax, a["bottle_cells"], (14.6, 8.6), "Bottle cells,\ndorsal lip", size="tiny")
bio.callout(ax, a["yolk_plug"], (12.4, 8.2), "Yolk plug", size="tiny")
bio.callout(ax, a["endoderm"], (8.2, 9.0), "Endoderm", size="tiny")

a = E.gastrula(ax, (20.0, 10.3), 1.75, "zebrafish", epiboly=0.6)
bio.label(ax, (20.0, 14.1), "Zebrafish", size="title", bold=True)
bio.callout(ax, a["shield"], (23.2, 10.4), "Shield", size="tiny")
bio.callout(ax, a["germ_ring"], (16.8, 10.6), "Germ ring", size="tiny")
bio.callout(ax, a["evl"], (23.0, 13.2), "Enveloping layer", size="tiny")
bio.callout(ax, a["epiblast"], (23.0, 13.9), "Epiblast", size="tiny")
bio.callout(ax, a["ysl"], (23.2, 9.5), "YSL", size="tiny")
bio.callout(ax, a["yolk"], (22.6, 8.3), "Yolk cell", size="tiny")

a = E.gastrula(ax, (3.4, 3.6), 1.75, "chick")
bio.label(ax, (3.4, 6.9), "Chick", size="title", bold=True)
bio.callout(ax, a["groove"], (3.4, 6.2), "Primitive groove", size="tiny")
bio.callout(ax, a["epiblast"], (0.6, 5.6), "Epiblast", size="tiny")
bio.callout(ax, a["mesoderm"], (6.4, 5.4), "Mesoderm", size="tiny")
bio.callout(ax, a["endoderm"], (1.8, 1.6), "Endoderm", size="tiny")
bio.callout(ax, a["hypoblast"], (5.8, 1.6), "Hypoblast", size="tiny")

a = E.gastrula(ax, (11.6, 3.0), 1.75, "mouse")
bio.label(ax, (11.6, 6.9), "Mouse", size="title", bold=True)
bio.callout(ax, a["epiblast"], (8.6, 2.6), "Epiblast", size="tiny")
bio.callout(ax, a["proamniotic"], (8.8, 4.0), "Proamniotic\ncavity", size="tiny")
bio.callout(ax, a["exe"], (14.0, 5.9), "Extraembryonic\nectoderm", size="tiny")
bio.callout(ax, a["ve"], (14.4, 1.5), "Visceral endoderm", size="tiny")
bio.callout(ax, a["ave"], (8.6, 1.2), "AVE", size="tiny")
bio.callout(ax, a["streak"], (14.4, 2.8), "Primitive streak,\nmesoderm", size="tiny")
bio.callout(ax, a["node"], (13.6, 0.6), "Node", size="tiny")

a = E.gastrula(ax, (20.0, 3.4), 1.55, "human")
bio.label(ax, (20.0, 6.9), "Human (day 14)", size="title", bold=True)
bio.callout(ax, a["amniotic_cavity"], (22.9, 5.7), "Amniotic cavity", size="tiny")
bio.callout(ax, a["epiblast"], (23.2, 4.4), "Epiblast", size="tiny")
bio.callout(ax, a["hypoblast"], (16.6, 3.5), "Hypoblast", size="tiny")
bio.callout(ax, a["yolk_sac"], (22.9, 2.0), "Yolk sac", size="tiny")
bio.callout(ax, a["chorionic_cavity"], (23.2, 1.2), "Chorionic cavity", size="tiny")
bio.callout(ax, a["syncytiotrophoblast"], (23.0, 6.3), "Syncytiotrophoblast", size="tiny")
bio.callout(ax, a["lacuna"], (16.7, 6.1), "Maternal blood\nin lacunae", size="tiny")
bio.callout(ax, a["stalk"], (16.8, 4.7), "Connecting stalk", size="tiny")
E.legend(ax, (4.5, -0.3), ("ectoderm", "mesoderm", "endoderm", "epiblast", "hypoblast", "trophoblast", "amnion"), step=2.2, size="tiny",
         swatch=0.26)
