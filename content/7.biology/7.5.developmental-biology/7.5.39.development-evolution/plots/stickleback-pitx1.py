"""Modular enhancers of Pitx1 and the repeated loss of the pelvis in freshwater sticklebacks.

Top: marine threespine sticklebacks (Gasterosteus aculeatus) have pelvic spines; the Pitx1 locus has
separate enhancers for expression in the thymus, the pelvic (hindfin) bud, sensory neurons and the olfactory
(nasal) pit. Middle: in many freshwater populations a deletion removes the pelvic enhancer (Pel), recurrently
and independently in different lakes (Chan et al. 2010); Pitx1 is still expressed in the other tissues and
the protein is unchanged, but the pelvic bud does not form. Bottom: the logic of the evidence: genetic
mapping of the difference to the Pitx1 region; no coding change; loss of pelvic expression only; a 2.5 kb
marine Pel fragment drives GFP in the pelvis; the same fragment linked to Pitx1 restores pelvic spines in
freshwater fish. Schematic; enhancer positions not to scale.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 12.0)


def locus(y, deleted):
    ax.plot([2.0, 24.0], [y, y], color=P.ink(), lw=1.4, zorder=5)
    enh = (("thymus", 4.0, "neutral"), ("pelvis (Pel)", 8.2, "highlight"), ("sensory neurons", 12.6, "neutral"),
           ("nasal pit", 16.4, "neutral"))
    for name, x, tok in enh:
        if deleted and name.startswith("pelvis"):
            ax.plot([x - 1.3, x + 1.3], [y, y], color=P.surface(), lw=3.0, zorder=6)
            bio.label(ax, (x, y + 0.75), "deleted", size="tiny", color=charts_neg())
            ax.plot([x - 1.3, x + 1.3], [y + 0.35, y + 0.35], color=charts_neg(), lw=0.9, ls=(0, (2, 1.5)), zorder=6)
            continue
        bio.box(ax, (x, y), 2.6, 0.7, tok, None, radius=0.12)
        bio.label(ax, (x, y + 0.75), name, size="tiny")
    bio.box(ax, (21.0, y), 3.0, 0.9, "dna", None, radius=0.12)
    bio.label(ax, (21.0, y), "Pitx1", size="small", italic=True, color=P.on_fill())


def charts_neg():
    return P.edge("negative")


bio.label(ax, (2.0, 11.4), "Marine population: pelvic spines", size="small", bold=True, ha="left")
locus(9.6, False)
bio.icon(ax, "phylopic/stickleback", at=(27.4, 9.8), height=1.6, color="animal")
bio.label(ax, (27.4, 8.6), "spined", size="tiny", color=P.muted())
bio.label(ax, (2.0, 7.4), "Freshwater populations: pelvic enhancer deleted", size="small", bold=True, ha="left")
locus(5.6, True)
bio.icon(ax, "phylopic/stickleback", at=(27.4, 5.8), height=1.6, color="neutral")
bio.label(ax, (27.4, 4.6), "pelvis reduced", size="tiny", color=P.muted())

steps = ("1 crosses map the pelvic difference to the region of the gene",
         "2 the encoded protein is identical in both forms",
         "3 expression is lost only in the pelvic bud",
         "4 marine 2.5 kb Pel fragment drives GFP in the pelvis",
         "5 marine Pel + coding sequence restores spines in freshwater fish")
for i, st in enumerate(steps):
    bio.label(ax, (2.0 + 13.0 * (i % 2), 3.0 - 0.8 * (i // 2)), st, size="tiny", ha="left")
