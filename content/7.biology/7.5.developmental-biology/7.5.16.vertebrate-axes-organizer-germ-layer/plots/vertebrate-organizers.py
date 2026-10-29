# Equivalent signalling centres in four vertebrates (schematic). Xenopus: Nieuwkoop centre in the dorsal vegetal cells,
# organizer at the dorsal blastopore lip. Chick: Koller's sickle and the posterior marginal zone (PMZ, Vg1 and Wnt8c)
# initiate the primitive streak; Hensen's node at its anterior end is the organizer; the hypoblast (Cerberus)
# keeps the streak single and protects the anterior. Mouse (E6.5, anterior left): the anterior visceral endoderm (AVE,
# green), having migrated from the distal tip, secretes Nodal and Wnt antagonists; the primitive streak forms
# opposite it in the posterior epiblast; the node (yellow) forms at its distal end and is the organizer.
import wikibio as bio
from wikibio import bodyaxes as BA

fig, ax = bio.canvas(22.0, 8.6)
P = bio.P
b = BA.amphibian(ax, (3.2, 4.2), 2.0, stage="blastula")
bio.callout(ax, b["nieuwkoop"], (4.6, 0.5), "Nieuwkoop centre")
bio.callout(ax, b["organizer"], (5.9, 7.2), "Organizer")
bio.label(ax, (3.2, 8.2), "Xenopus, late blastula", size="normal", bold=True, italic=False)
c1 = BA.chick_blastoderm(ax, (11.0, 4.3), 1.9, stage="prestreak")
bio.callout(ax, c1["sickle"], (9.6, 0.4), "Koller's sickle")
bio.callout(ax, c1["pmz"], (13.8, 1.0), "PMZ")
bio.label(ax, (13.3, 8.2), "Chick, pre-streak and streak", size="normal", bold=True)
c2 = BA.chick_blastoderm(ax, (15.6, 4.3), 1.6, stage="streak")
bio.callout(ax, c2["node"], (17.6, 7.4), "Hensen's node")
m = BA.egg_cylinder(ax, (20.2, 4.4), 1.1, 3.4)
bio.callout(ax, m["ave"], (18.4, 1.4), "AVE")
bio.callout(ax, m["node"], (21.6, 0.6), "Node")
bio.callout(ax, m["streak"], (21.9, 6.6), "Streak")
bio.label(ax, (20.2, 8.2), "Mouse, E6.5", size="normal", bold=True)
