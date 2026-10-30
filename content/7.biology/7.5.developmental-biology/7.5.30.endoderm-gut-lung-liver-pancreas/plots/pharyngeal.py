"""The pharyngeal arches and pouches (frontal section, rostral up) and the fates of the pouch endoderm in
humans. Each arch has a core of paraxial mesoderm (muscle, red), surrounded by neural crest mesenchyme
(skeleton and connective tissue, green) and an arch artery; it is covered by ectoderm (blue) and lined by
endoderm (yellow). Between the arches the endoderm pushes out the pharyngeal pouches, which meet the ectodermal
clefts. Pouch 1: tympanic cavity of the middle ear and the auditory tube. Pouch 2: the epithelium of the palatine
tonsil. Pouch 3: the thymus (ventral part) and the inferior parathyroid glands (dorsal part). Pouch 4: the
superior parathyroid glands and the ultimobranchial body, which gives the calcitonin-producing C cells of the
thyroid (in mammals partly from crest-independent endoderm). The thyroid itself buds from the midline floor of
the pharynx between the first and second arches (the foramen caecum) and descends into the neck."""
import wikibio as bio
from wikibio import organogenesis as O

P = bio.P
fig, ax = bio.canvas(22, 11)
p = O.pharynx(ax, (7.0, 5.6), 6.4, 9.4)
fates = {1: ("middle ear, auditory tube", "channel"), 2: ("palatine tonsil", "receptor"), 3: ("thymus + inferior parathyroids", "protein"),
         4: ("superior parathyroids,\nultimobranchial body", "enzyme")}
for k in range(1, 5):
    x, y = p[f"pouch{k}"]
    ax.add_patch(bio.core.Circle((x + 0.05, y), 0.22, facecolor=P.fill(fates[k][1]), edgecolor=P.edge(fates[k][1]), lw=0.8, zorder=12))
    bio.callout(ax, (x + 0.05, y), (14.4, y + 0.1), f"Pouch {k}: {fates[k][0]}")
    bio.callout(ax, p[f"arch{k}_l"], (0.5, p[f"arch{k}_l"][1] + 0.35), f"Arch {k}")
bio.callout(ax, p["core1"], (14.4, 10.6), "Mesodermal core (muscle)")
bio.callout(ax, p["artery2"], (14.4, 9.8), "Arch artery")
bio.callout(ax, p["cleft1"], (14.4, 1.4), "Cleft 1: external ear canal")
bio.callout(ax, (7.0, 9.9), (9.8, 10.8), "Thyroid bud (midline)")
ax.add_patch(bio.core.Circle((7.0, 9.9), 0.22, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=0.8, zorder=12))
for k, (txt, tk) in enumerate((("ectoderm", "ectoderm"), ("endoderm", "endoderm"), ("neural crest", "cl"), ("mesoderm", "mesoderm"))):
    bio.box(ax, (0.6 + 1.8 * k, 0.5), 0.45, 0.3, tk)
    bio.label(ax, (0.95 + 1.8 * k, 0.5), txt, size="tiny", ha="left")
