# Brains of five vertebrates in schematic dorsal view (animalmorph.brain), regions coloured alike.
import numpy as np
import wikibio as bio
from wikibio import animalmorph as am

fig, ax = bio.canvas(24, 9.2)
cls = [("fish", "A  Teleost"), ("amphibian", "B  Frog"), ("reptile", "C  Lizard"), ("bird", "D  Bird"), ("mammal", "E  Mammal")]
for i, (c, t) in enumerate(cls):
    cx = 2.4 + i * 4.8
    bio.label(ax, (cx, 8.8), t, size="small")
    am.brain(ax, (cx, 4.8), 6.0, c, labels=False)
lx = 2.0
for k, t in (("olfactory-bulb", "olfactory bulb"), ("cerebrum", "telencephalon"), ("optic-lobe", "optic lobe (tectum)"),
             ("cerebellum", "cerebellum"), ("medulla", "medulla")):
    bio.shape(ax, np.array([(lx, 0.4), (lx + 0.45, 0.4), (lx + 0.45, 0.72), (lx, 0.72)]), token=am.BRAIN[k], lw=0.6)
    bio.label(ax, (lx + 0.6, 0.56), t, size="tiny", ha="left")
    lx += 4.2
