"""Which sex cares in teleost fishes, by mode of fertilization.

Number of teleost families with male, female or no parental care under internal and external fertilization
(Gross and Shine 1981; a family can be counted in more than one care category, but appears under "no care" only
if care is unknown in it). Among families with uniparental care, female care predominates with internal
fertilization (14 of 16 families, 88 percent) and male care with external fertilization (61 of 85, 72 percent).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
data = {"internal fertilization": (2, 14, 5), "external fertilization": (61, 24, 100)}
fig, ax = bio.canvas(22.0, 10.0)
p = Ch.axes_at(ax, (2.8, 1.8, 18.0, 7.2))
cats = [("male care", "dna"), ("female care", "rna"), ("no care", "neutral")]
x0 = 0
ticks = []
for g, vals in data.items():
    for k, ((name, tok), v) in enumerate(zip(cats, vals)):
        x = x0 + k
        p.bar(x, v, 0.8, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
        p.text(x, v + 1.5, str(v), ha="center", va="bottom", fontsize=FS["small"], color=P.ink())
        p.text(x, -6, name, ha="center", va="top", fontsize=FS["tiny"], color=P.ink())
    ticks.append(x0 + 1)
    x0 += 4
p.set_xticks(ticks)
p.set_xticklabels(list(data), fontsize=FS["small"])
p.tick_params(axis="x", pad=24, length=0)
p.set_ylim(0, 112)
p.set_xlim(-0.7, x0 - 1.3)
Ch.style_axes(p, None, "number of teleost families")
p.text(1, 30, "female care: 14 of 16\nuniparental families", ha="center", fontsize=FS["tiny"], color=Ch.line("rna"))
p.text(4.5, 78, "male care: 61 of 85\nuniparental families", ha="center", fontsize=FS["tiny"], color=Ch.line("dna"))
