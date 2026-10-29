# Body axes of early embryos (wikibio.bodyaxes). A: a Drosophila egg chamber at stage 10 with bicoid mRNA at the
# anterior of the oocyte, oskar at the posterior pole and gurken next to the oocyte nucleus in the dorsal-anterior
# corner. B: a transverse section of the syncytial blastoderm with the nuclear Dorsal gradient and its target
# domains. C-E: a Xenopus egg after cortical rotation, a blastula with the Nieuwkoop centre and the organizer, an
# early gastrula. F: chick blastoderm with streak and node. G: mouse egg cylinder with AVE and streak.
# H: the mouse node in ventral view; I: one tilted node cilium.
import numpy as np
import wikibio as bio
from wikibio import bodyaxes as BA

fig, ax = bio.canvas(26.0, 17.0)
P = bio.P

bio.panel(ax, "A", (0.2, 16.8))
ch = BA.EggChamber(ax, (5.6, 13.6), 9.0, 4.0)
ch.microtubules()
ch.anterior_cap("receptor")
ch.cortex(-25, 25, "positive")
ch.cortex(70, 110, "highlight")
a = ch.anchors
bio.callout(ax, a["nurse"], (1.2, 16.2), "Nurse cells")
bio.callout(ax, a["nucleus"], (8.3, 16.3), "Oocyte nucleus")
bio.callout(ax, a["posterior"], (10.6, 12.0), "Posterior pole")
bio.callout(ax, a["follicle_ventral"], (7.6, 11.0), "Follicle cells")
bio.callout(ax, a["ring_canal"], (3.6, 11.0), "Ring canal")

bio.panel(ax, "B", (12.2, 16.8))
xs = BA.FlyCrossSection(ax, (15.3, 13.3), 2.0, values=lambda s: np.exp(-s ** 2 / (2 * 0.15 ** 2)), token="dna")
xs.domain(0, 0.22, "muscle")
xs.domain(0.22, 0.42, "channel")
xs.domain(0.55, 1.0, "highlight")
bio.label(ax, (15.3, 16.2), "Dorsal", size="small", color=P.muted())
bio.label(ax, (15.3, 10.5), "Ventral", size="small", color=P.muted())

bio.panel(ax, "C", (19.4, 16.8))
e = BA.amphibian(ax, (22.3, 13.4), 1.9, stage="egg", rotation=30)
bio.callout(ax, e["sperm_entry"], (19.8, 15.9), "Sperm entry")
bio.callout(ax, e["grey_crescent"], (25.3, 11.2), "Grey crescent")

bio.panel(ax, "D", (0.2, 9.6))
b = BA.amphibian(ax, (3.2, 6.3), 2.1, stage="blastula")
bio.callout(ax, b["nieuwkoop"], (5.9, 3.6), "Nieuwkoop centre")
bio.callout(ax, b["organizer"], (6.1, 8.9), "Organizer")
bio.callout(ax, b["blastocoel"], (0.6, 9.1), "Blastocoel")

bio.panel(ax, "E", (7.0, 9.6))
g = BA.amphibian(ax, (9.8, 6.3), 2.1, stage="gastrula")
bio.callout(ax, g["dorsal_lip"], (12.4, 4.0), "Dorsal lip")
bio.callout(ax, g["archenteron"], (12.6, 8.8), "Archenteron")

bio.panel(ax, "F", (13.6, 9.6))
c = BA.chick_blastoderm(ax, (16.2, 6.3), 2.0)
bio.callout(ax, c["node"], (18.9, 8.9), "Hensen's node")
bio.callout(ax, c["pmz"], (13.7, 3.4), "PMZ")

bio.panel(ax, "G", (20.2, 9.6))
m = BA.egg_cylinder(ax, (22.6, 6.4), 1.2, 3.2)
bio.callout(ax, m["ave"], (20.3, 4.0), "AVE")
bio.callout(ax, m["streak"], (25.4, 4.6), "Streak")
bio.callout(ax, m["exe"], (20.3, 8.6), "ExE")

bio.panel(ax, "H", (0.2, 3.4))
n = BA.node_pit(ax, (4.4, 1.5), 4.4)
bio.label(ax, n["left"], "L", size="small", bold=True, ha="left")
bio.label(ax, n["right"], "R", size="small", bold=True, ha="right")

bio.panel(ax, "I", (10.0, 3.4))
k = BA.cilium_cone(ax, (13.8, 0.6), 2.0, tilt=35, cone=30)
bio.label(ax, (16.9, 0.35), "posterior", size="tiny", color=P.muted())
