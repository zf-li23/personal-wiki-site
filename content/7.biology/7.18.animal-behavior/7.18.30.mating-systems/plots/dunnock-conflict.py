"""Sexual conflict over the mating system in dunnocks (Prunella modularis).

Number of young raised per season by each bird in three mating combinations, with maternity and paternity
measured by DNA fingerprinting (Burke et al. 1989; Davies 1992): monogamy (one male, one female), polygyny
(one male, two females, each female shown) and polyandry (alpha and beta males sharing one female). A female
does best in polyandry, where two males help to feed her young; an alpha male does best in polygyny. Arrows
mark the system each sex attempts to bring about.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(22.0, 10.5)
p = Ch.axes_at(ax, (2.6, 1.8, 18.5, 7.4))
groups = ["monogamy", "polygyny", "polyandry"]
data = [[("female", 5.0, "rna"), ("male", 5.0, "dna")],
        [("each female", 3.8, "rna"), ("male", 7.6, "dna")],
        [("female", 6.7, "rna"), ("alpha male", 3.7, "dna"), ("beta male", 3.0, "dna")]]
x = 0.0
centers = []
for g, bars in zip(groups, data):
    xs = []
    for name, v, tok in bars:
        light = name == "beta male"
        p.bar(x, v, width=0.8, color=P.mix(P.fill(tok), P.surface(), 0.7) if light else P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
        p.text(x, v + 0.12, f"{v:.1f}", ha="center", va="bottom", fontsize=FS["small"], color=P.ink())
        p.text(x, 0.15, name, ha="center", va="bottom", fontsize=FS["tiny"], color=P.on_fill(), rotation=90)
        xs.append(x)
        x += 1.0
    centers.append(np.mean(xs))
    x += 0.9
p.set_xticks(centers)
p.set_xticklabels(groups)
p.set_ylim(0, 9.4)
p.set_xlim(-0.7, x - 1.2)
Ch.style_axes(p, None, "young raised per season")
p.annotate("best for the female", (centers[2] - 1.0, 7.3), (centers[2] - 1.0, 8.7), ha="center",
           fontsize=FS["tiny"], color=Ch.line("rna"), arrowprops=dict(arrowstyle="->", color=Ch.line("rna")))
p.annotate("best for the male", (centers[1] + 0.5, 8.2), (centers[1] + 0.5, 9.1), ha="center",
           fontsize=FS["tiny"], color=Ch.line("dna"), arrowprops=dict(arrowstyle="->", color=Ch.line("dna")))
