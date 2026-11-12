"""Eggs and the patterns of cleavage (drawn with wikibio.embryology).

Top row: eggs classified by the amount and distribution of yolk (beige): isolecithal (little, evenly
spread: sea urchins, lancelets, mammals), mesolecithal (moderate, in the vegetal half: amphibians),
telolecithal (most of the egg: birds, reptiles, fishes, cephalopods) and centrolecithal (central: most
arthropods). Bottom row: the corresponding cleavage patterns. Radial cleavage (8-cell stage, side view):
the blastomeres of each tier lie directly above those of the tier below (echinoderms, chordates). Spiral
cleavage (8-cell stage from the animal pole): the first quartet of micromeres (1a-1d) is turned by 45
degrees and sits over the furrows between the macromeres (annelids, molluscs, nemerteans, polyclad
flatworms). Unequal holoblastic cleavage of an amphibian, discoidal meroblastic cleavage restricted to a
blastodisc on the yolk, and superficial cleavage of insects, in which nuclei divide in a syncytium and
migrate to the cortex.
"""

import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(27.0, 10.6)
X = [2.8, 8.2, 13.6, 19.0, 24.4]
eggs = [("iso", "Isolecithal"), ("meso", "Mesolecithal"), ("telo", "Telolecithal"), ("centro", "Centrolecithal")]
for x, (k, name) in zip([X[0], X[2], X[3], X[4]], eggs):
    E.egg(ax, (x, 7.6), 1.3, k)
    bio.label(ax, (x, 5.75), name + " egg", size="small", bold=True)
bio.label(ax, (X[1], 7.6), "(spiralian eggs:\nisolecithal, often\nwith more yolk)", size="tiny", color=P.muted())
pats = [("radial", "Radial cleavage"), ("spiral", "Spiral cleavage"), ("unequal", "Unequal holoblastic"),
        ("discoidal", "Discoidal (meroblastic)"), ("superficial", "Superficial")]
for x, (k, name) in zip(X, pats):
    a = E.cleavage(ax, (x, 2.9), 1.3, k)
    bio.label(ax, (x, 0.7), name, size="small", bold=True)
bio.label(ax, (X[0], 0.25), "echinoderms, chordates", size="tiny", color=P.muted())
bio.label(ax, (X[1], 0.25), "annelids, molluscs", size="tiny", color=P.muted())
bio.label(ax, (X[2], 0.25), "amphibians", size="tiny", color=P.muted())
bio.label(ax, (X[3], 0.25), "birds, fishes, cephalopods", size="tiny", color=P.muted())
bio.label(ax, (X[4], 0.25), "insects", size="tiny", color=P.muted())
ax.plot([0.5, 26.5], [5.3, 5.3], color=P.muted(), lw=0.5, ls=":")
bio.label(ax, (0.4, 10.2), "Egg types", size="small", ha="left", color=P.muted())
bio.label(ax, (0.4, 4.9), "Cleavage patterns", size="small", ha="left", color=P.muted())
