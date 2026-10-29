"""Timeline of eye development in the mouse (approximate; embryonic day E, postnatal day P). Top: the inductive
sequence, from the specification of a single eye field in the anterior neural plate to the lens vesicle and the
first lens fibres. Bottom: the birth periods of the seven main cell classes of the retina, which are born in a
conserved, overlapping order from the same multipotent progenitors: ganglion cells, horizontal cells, cones and
amacrine cells first, rods, bipolar cells and Mueller glia last (after Young 1985 and Cepko and colleagues)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
# days: E0 = 0; birth (P0) at E19
ev = [("eye field (Pax6, Rx, Six3)", 7.5, 8.5, "protein"), ("Shh splits the eye field", 7.7, 8.5, "drug"),
      ("optic vesicle evaginates", 8.5, 9.2, "protein"), ("contact with surface ectoderm", 9.0, 9.6, "channel"),
      ("lens placode", 9.3, 9.8, "receptor"), ("optic cup and lens pit", 9.8, 10.5, "receptor"),
      ("lens vesicle detaches", 10.5, 11.0, "receptor"), ("primary lens fibres", 11.0, 12.5, "receptor")]
cells = [("ganglion cells", 11.0, 18.0), ("horizontal cells", 11.0, 14.5), ("cones", 11.5, 17.5), ("amacrine cells", 12.0, 20.0),
         ("rods", 13.0, 26.0), ("bipolar cells", 17.0, 27.0), ("Mueller glia", 18.0, 27.0)]
fig, ax = plt.subplots(figsize=(9.6, 4.8))
fig.subplots_adjust(left=0.27, right=0.98, bottom=0.12, top=0.97)
y = 0
labels = []
for name, a, b, tok in ev:
    ax.barh(y, b - a, left=a, height=0.6, color=P_.fill(tok), edgecolor=P_.edge(tok), lw=0.8)
    labels.append(name)
    y += 1
y += 0.5
toks = ["enzyme", "antibody", "k", "carbohydrate", "dna", "metabolite", "cl"]
for (name, a, b), tok in zip(cells, toks):
    ax.barh(y, b - a, left=a, height=0.6, color=P_.fill(tok), edgecolor=P_.edge(tok), lw=0.8)
    labels.append(name)
    y += 1
ax.set_yticks(list(range(len(ev))) + list(np.arange(len(cells)) + len(ev) + 0.5), labels)
ax.invert_yaxis()
ax.axvline(19, color=P_.muted(), lw=0.8, ls="--")
ax.text(19.2, 0.2, "birth", fontsize=FT["tiny"], color=P_.muted())
ax.set_xticks([8, 10, 12, 14, 16, 18, 19, 22, 25, 28], ["E8", "E10", "E12", "E14", "E16", "E18", "P0", "P3", "P6", "P9"])
ax.set_xlim(7, 28)
charts.style_axes(ax, "age", None)
ax.text(27.5, len(ev) - 0.6, "retinal cell birth", fontsize=FT["small"], color=P_.ink(), ha="right")
ax.text(27.5, -0.5, "induction and morphogenesis", fontsize=FT["small"], color=P_.ink(), ha="right")
