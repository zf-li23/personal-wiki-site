"""Threats to species listed on the IUCN Red List.

Percentage of 8688 threatened or near-threatened species assessed by 2016 that are affected by each major
class of threat (a species can face several, so the percentages sum to more than 100), approximate values
read from Maxwell, Fuller, Brooks and Watson (2016), Nature 536: 143-145, based on the IUCN threat
classification. Overexploitation (hunting, fishing, logging, collection) and agriculture (crops, livestock,
plantations, aquaculture) dominate; climate change affected fewer species then, but is increasing.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT

threats = [
    ("overexploitation", 72, "negative"),
    ("agricultural activity", 62, "negative"),
    ("urban development", 35, "enzyme"),
    ("invasive species and disease", 26, "enzyme"),
    ("pollution", 22, "dna"),
    ("ecosystem modification (fire, dams)", 21, "dna"),
    ("climate change", 19, "plant"),
]

fig, ax = bio.canvas(22.0, 9.0)
pa = C.axes_at(ax, (8.6, 1.4, 12.0, 6.6))
y = np.arange(len(threats))[::-1]
for yi, (name, v, tok) in zip(y, threats):
    pa.barh(yi, v, height=0.62, color=P.light(tok), edgecolor=Q.line_color(tok), lw=0.9)
    pa.text(v + 1, yi, f"{v} %", va="center", fontsize=FS["tiny"], color=P.ink())
pa.set_yticks(y)
pa.set_yticklabels([t[0] for t in threats])
pa.set_xlim(0, 85)
C.style_axes(pa, "threatened or near-threatened species affected (%)", None)
bio.label(ax, (0.4, 8.6), "Major threats to 8688 Red List species (after Maxwell et al. 2016)", size="small", bold=True, ha="left")
