"""Species concepts as criteria met at different stages of lineage divergence (after the general lineage
concept of de Queiroz). Schematic: an ancestral lineage splits into two, which diverge over time (the
widening band shows increasing differences). Along the way the daughter lineages acquire properties that
different species concepts use as criteria: differences in some characters, fixed diagnosable differences
(phylogenetic species concept), reciprocal monophyly of gene trees (genealogical species concept), ecological
divergence, prezygotic and postzygotic reproductive isolation (biological species concept). The order shown is
one possibility; it differs between cases. Before all criteria are met there is a grey zone in which
different concepts disagree about whether there are one or two species."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = plt.subplots(figsize=(10.5, 4.2))
fig.subplots_adjust(left=0.04, right=0.99, bottom=0.14, top=0.95)
t = np.linspace(0, 10, 300)
split = 1.0
sep = np.where(t < split, 0, 1.6 * (1 - np.exp(-(t - split) / 3)))
ax.plot(t[t <= split], np.zeros((t <= split).sum()), color=P.edge("neutral"), lw=6, solid_capstyle="butt")
for sgn, tok in ((1, "dna"), (-1, "rna")):
    m = t >= split
    ax.plot(t[m], sgn * sep[m], color=P.edge(tok), lw=6, solid_capstyle="butt")
ax.fill_between([2.2, 8.2], -2.3, 2.3, color=P.fill("neutral"), alpha=0.35, lw=0)
ax.text(5.2, 2.15, "grey zone: concepts disagree", ha="center", fontsize=FT["tiny"], color=P.muted())
events = [(2.2, "character\ndifferences"), (3.3, "diagnosable\n(PSC)"), (4.4, "ecological\ndivergence"),
          (5.5, "prezygotic\nisolation"), (6.8, "reciprocal\nmonophyly"), (8.2, "postzygotic\nisolation (BSC\ncomplete)")]
for x, lab in events:
    y = 1.6 * (1 - np.exp(-(x - split) / 3))
    ax.plot([x, x], [-y, y], color=P.ink(), lw=0.8, ls=":")
    ax.scatter([x, x], [y, -y], s=22, color=P.ink(), zorder=4)
    ax.text(x, -2.05, lab, ha="center", va="top", fontsize=FT["tiny"], color=P.ink())
ax.text(0.5, 0.2, "ancestral\nspecies", ha="center", va="bottom", fontsize=FT["tiny"], color=P.ink())
ax.text(9.9, 1.75, "species A", ha="right", fontsize=FT["small"], color=P.edge("dna"))
ax.text(9.9, -1.85, "species B", ha="right", fontsize=FT["small"], color=P.edge("rna"))
ax.annotate("", xy=(10, -2.95), xytext=(0, -2.95), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.9),
            annotation_clip=False)
ax.text(5, -3.15, "time since divergence", ha="center", va="top", fontsize=FT["small"], color=P.muted())
ax.set_xlim(-0.2, 10.2)
ax.set_ylim(-3.4, 2.4)
ax.axis("off")
