# Vertebrate hearts in schematic ventral view, chambers coloured by the blood they carry (animalmorph.heart).
import wikibio as bio
from wikibio import animalmorph as am

fig, ax = bio.canvas(25, 5.0)
kinds = [("fish", "A  Teleost"), ("amphibian", "B  Amphibian"), ("reptile", "C  Lizard"),
         ("crocodilian", "D  Crocodylian"), ("bird", "E  Bird"), ("mammal", "F  Mammal")]
for i, (k, t) in enumerate(kinds):
    cx = 2.2 + i * 4.1
    bio.label(ax, (cx, 4.7), t, size="small")
    am.heart(ax, (cx, 2.2), 2.6, k, labels=True)
