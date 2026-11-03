"""Haldane's rule in two groups of mosquitoes. Numbers of species crosses in which hybrid sterility or
inviability affects only females, only males, or both sexes. Data from Barton et al. (2007), Table 22.3,
after Presgraves and Orr (1998). In Aedes the X and Y are homomorphic (sex is determined by a single
locus, and the Y carries a full set of genes), so the dominance theory predicts no excess of affected males;
in Anopheles the Y is degenerate, as in Drosophila. Male-only sterility in Aedes therefore reflects faster
evolution of male fertility genes; male-only inviability in Anopheles reflects the dominance theory."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
data = {
    "Aedes\n(homomorphic X/Y)": {"sterility": (0, 11, 10), "inviability": (1, 1, 11)},
    "Anopheles\n(degenerate Y)": {"sterility": (0, 56, 20), "inviability": (3, 21, 40)},
}
cats = ["females only", "males only", "both sexes"]
toks = ["rna", "dna", "neutral"]
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8), sharey=False)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.88, wspace=0.25)
for ax, (genus, d) in zip(axs, data.items()):
    for j, phen in enumerate(("sterility", "inviability")):
        vals = d[phen]
        for i, v in enumerate(vals):
            x = j * 4 + i
            ax.bar([x], [v], color=P.fill(toks[i]), edgecolor=P.edge(toks[i]), lw=0.8,
                   label=cats[i] if j == 0 else None)
            ax.text(x, v + 0.8, str(v), ha="center", fontsize=FT["tiny"], color=P.ink())
    ax.set_xticks([1, 5])
    ax.set_xticklabels(["hybrid sterility", "hybrid inviability"], fontsize=FT["tiny"])
    charts.style_axes(ax, None, "number of crosses")
    charts.title(ax, genus.replace("\n", " "))
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
axs[0].set_ylim(0, 14)
axs[1].set_ylim(0, 62)
