# Embryology atlas (wikibio.embryology): yolk distribution, cleavage patterns, blastulae and gastrulae of
# the model species, the six epithelial movements, the bird egg membranes and a placental villus.
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(24, 30)
y = 28.3
for k, (kind, name) in enumerate((("iso", "Isolecithal"), ("meso", "Mesolecithal"), ("telo", "Telolecithal"), ("centro", "Centrolecithal"))):
    E.egg(ax, (2.6 + 5.8 * k, y), 1.1, kind)
    bio.label(ax, (2.6 + 5.8 * k, y - 1.6), name, size="small")
y = 24.2
for k, pat in enumerate(("radial", "unequal", "spiral", "spiral-sinistral")):
    a = E.cleavage(ax, (2.6 + 5.8 * k, y), 1.1, pat)
    bio.label(ax, (2.6 + 5.8 * k, y - 1.7), pat, size="small")
y = 20.2
for k, pat in enumerate(("bilateral", "rotational", "discoidal", "superficial")):
    E.cleavage(ax, (2.6 + 5.8 * k, y), 1.1, pat)
    bio.label(ax, (2.6 + 5.8 * k, y - 1.7), pat, size="small")
y = 15.8
for k, sp in enumerate(("sea-urchin", "frog", "zebrafish", "mouse")):
    E.blastula(ax, (2.6 + 5.8 * k, y), 1.3, sp)
    bio.label(ax, (2.6 + 5.8 * k, y - 1.9), sp, size="small")
E.blastula(ax, (4.5, 12.6), 1.2, "chick")
E.blastula(ax, (14.5, 12.6), 1.0, "fly")
E.streak(ax, (21.0, 12.4), 1.4)
y = 8.0
for k, sp in enumerate(("sea-urchin", "frog", "zebrafish", "mouse")):
    E.gastrula(ax, (2.6 + 5.8 * k, y), 1.3, sp)
    bio.label(ax, (2.6 + 5.8 * k, y - 1.9), sp, size="small")
E.gastrula(ax, (4.0, 3.2), 1.3, "chick")
E.gastrula(ax, (11.5, 3.0), 1.2, "human")
E.amniote_egg(ax, (19.5, 3.4), 1.6)
fig2, ax2 = bio.canvas(24, 9)
for k, kind in enumerate(("invagination", "involution", "epiboly", "ingression", "delamination", "convergent-extension")):
    E.sheet(ax2, (2.0 + 4.0 * k, 6.5), 3.2, kind)
    bio.label(ax2, (2.0 + 4.0 * k, 4.6), kind, size="small")
E.villus(ax2, (1, 0.2, 9, 4))
E.legend(ax2, (11.5, 2.5), ("ectoderm", "mesoderm", "endoderm", "yolk", "epiblast", "hypoblast", "trophoblast", "amnion"), rows=2, step=3.3)
