"""Chromosomes in the light microscope (schematic).
(A) Human karyogram 46,XX; the acrocentric chromosomes 13, 14, 15, 21 and 22, which carry the nucleolar organizer
regions on their short arms, are highlighted. (B) Classification by centromere position: metacentric,
submetacentric, acrocentric (with stalk = secondary constriction/NOR and satellite) and telocentric.
(C) G-banded ideogram of the human X with XIST (Xq13.2) and DMD (Xp21.2)."""

from matplotlib.patches import Circle

import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(22.0, 8.8)

bio.panel(ax, "A", (0.1, 8.7))
formula = G.karyotype(ax, (0.3, 8.2), sex="XX", highlight={"13", "14", "15", "21", "22"}, highlight_token="rrna",
                      scale=0.0092, width=0.28, slot=1.2, row_gap=0.6)
bio.label(ax, (10.0, 0.6), formula, size="title", bold=True, ha="right")

bio.panel(ax, "B", (10.8, 8.7))
types = [("metacentric", 0.5), ("submetacentric", 0.33), ("acrocentric", 0.12), ("telocentric", 0.02)]
for k, (name, c) in enumerate(types):
    x = 11.6 + k * 2.05
    top = 6.9
    a = G.chromosome(ax, (x, top), length=3.6, centromere=c, width=0.62, anchor="top")
    if name == "acrocentric":
        ax.plot([x - 0.1, x - 0.1], [top + 0.05, top + 0.45], color=P.edge("chromatin"), lw=0.9)
        ax.plot([x + 0.1, x + 0.1], [top + 0.05, top + 0.45], color=P.edge("chromatin"), lw=0.9)
        for dx in (-0.1, 0.1):
            ax.add_patch(Circle((x + dx, top + 0.6), 0.15, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=0.8))
        bio.callout(ax, (x + 0.12, top + 0.28), (x + 0.75, top + 1.0), "stalk (NOR)")
        bio.callout(ax, (x + 0.22, top + 0.62), (x + 0.75, top + 1.45), "satellite")
    bio.label(ax, (x, top - 3.9), name, size="small", va="top")
    if k == 0:
        bio.callout(ax, a["centromere"], (x - 0.6, top - 4.6), "centromere")

bio.panel(ax, "C", (18.9, 8.7))
G.ideogram(ax, (20.0, 8.0), G.HUMAN_X, length=6.6, width=0.5, labels="major",
           loci=[("DMD", 31.1, 33.3), ("XIST", 73.8, 73.9)], label_side="right")
bio.label(ax, (20.0, 0.9), "X chromosome", size="small", va="top")
