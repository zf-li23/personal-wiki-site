"""Sex determination in birds: a bilateral gynandromorph chicken and a Z-dosage model of DMRT1."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(10.4, 4.0))
ax = fig.add_axes([0.0, 0.05, 0.5, 0.88])
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis("off")
ax.set_aspect("equal")
bb = None
for side, tok in (("male", "drug"), ("female", "lipid")):
    n0 = len(ax.patches)
    bb = bio.icon(ax, "phylopic/chicken", at=(5.0, 4.0), height=6.0, color=tok)
    xm = bb[0] + bb[2] / 2
    r = Rectangle((0, 0), xm, 8, transform=ax.transData) if side == "male" else Rectangle((xm, 0), 10 - xm, 8, transform=ax.transData)
    for p in ax.patches[n0:]:
        p.set_clip_path(r)
ax.plot([xm, xm], [0.8, 7.3], color=P_.ink(), lw=0.8, ls="--")
bio.label(ax, (2.4, 0.5), "ZZ side: male", size="small")
bio.label(ax, (7.6, 0.5), "ZW side: female", size="small")
bio.label(ax, (0.2, 7.7), "A  Gynandromorph", bold=True, ha="left")
b = fig.add_axes([0.6, 0.17, 0.37, 0.7])
cases = [("ZZ", 2.0, "enzyme"), ("ZW", 1.0, "receptor"), ("ZZ, DMRT1 +/-", 1.0, "receptor"), ("ZZ, knockdown", 0.6, "receptor")]
for i, (lab, v, tok) in enumerate(cases):
    b.bar(i, v, color=P_.fill(tok), edgecolor=P_.edge(tok), width=0.6)
b.axhline(1.5, color=P_.ink(), lw=1.0, ls="--")
b.text(3.4, 1.55, "testis threshold", fontsize=FT["tiny"], color=P_.ink(), ha="right", va="bottom")
b.set_xticks(range(4))
b.set_xticklabels([c[0] for c in cases], fontsize=FT["tiny"], rotation=15)
b.set_ylim(0, 2.4)
charts.style_axes(b, None, "relative DMRT1 dose")
charts.title(b, "B  Z dosage: testis (teal) or ovary (pink)")
