# Vertebrate brains in dorsal view (rostral end up; schematic, drawn to the same length, so proportions
# not absolute sizes are compared). The same five regions are present in every class: olfactory bulbs,
# cerebrum (telencephalon), optic lobes (midbrain tectum), cerebellum and medulla oblongata, continuous
# with the spinal cord. In fishes the optic lobes are the largest dorsal structure and the cerebrum small;
# amphibians have a very small cerebellum; in reptiles the cerebrum enlarges; in birds the cerebrum and a
# large folded cerebellum dominate, with the optic lobes pushed to the sides and olfactory bulbs small; in
# mammals the cerebrum (neocortex, folded into gyri in large species) covers the midbrain. Relative
# cerebral enlargement occurred independently in birds and mammals. Left: a trout brain (template).
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(26, 11.4)
REG = {"olfactory-bulb": "Olfactory bulb", "cerebrum": "Cerebrum", "optic-lobe": "Optic lobe (tectum)",
       "cerebellum": "Cerebellum", "medulla": "Medulla"}

bio.panel(ax, "A", (0.2, 11.2))
tr = AM.Specimen("wikimedia/brain-fish-dorsal", at=(2.4, 5.6), height=8.0)
tr.draw(ax, parts={"olfactory-bulb": AM.BRAIN["olfactory-bulb"], "telencephalon": AM.BRAIN["cerebrum"],
                   "optic-tectum": AM.BRAIN["optic-lobe"], "cerebellum": AM.BRAIN["cerebellum"],
                   "medulla": AM.BRAIN["medulla"]})
AM.callouts(ax, [(tr.point(p, where="right"), REG[r], "right") for p, r in (("olfactory-bulb", "olfactory-bulb"),
                                                                            ("telencephalon", "cerebrum"),
                                                                            ("optic-tectum", "optic-lobe"),
                                                                            ("cerebellum", "cerebellum"),
                                                                            ("medulla", "medulla"))], right=4.3, gap=0.6)
bio.label(ax, (3.2, 0.7), "Trout", size="normal", bold=True)

bio.panel(ax, "B", (8.4, 11.2))
CLS = [("fish", "Fish"), ("amphibian", "Amphibian"), ("reptile", "Reptile"), ("bird", "Bird"), ("mammal", "Mammal")]
for k, (c, name) in enumerate(CLS):
    x = 10.2 + k * 3.5
    AM.brain(ax, (x, 6.0), 7.2, c)
    bio.label(ax, (x, 0.7), name, size="normal", bold=True)
AM.part_legend(ax, (10.0, 10.9), {r: AM.BRAIN[r] for r in REG}, names=REG)
