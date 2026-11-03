"""How much genetic variation is there? A: allozyme surveys by protein electrophoresis: the proportion
of enzyme loci that are polymorphic and the average gene diversity H at those loci, in mammals,
Drosophila and Escherichia coli. B: nucleotide diversity, the average proportion of sites at which two
randomly chosen copies of the genome differ, in humans and in Drosophila melanogaster (log scale).
Data from Barton et al. (2007), Chapter 13."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.3), gridspec_kw={"width_ratios": [1.5, 1]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.35)
groups = ["Mammals", "Drosophila", "E. coli"]
poly = [19, 48, 90]
H = [4.1, 12, 47]
x = np.arange(3)
a.bar(x - 0.18, poly, 0.34, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.6, label="loci polymorphic (%)")
a.bar(x + 0.18, H, 0.34, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.6, label="gene diversity $H$ (%)")
for i in range(3):
    a.text(x[i] - 0.18, poly[i] + 1.5, f"{poly[i]}", ha="center", fontsize=FT["tiny"], color=P.ink())
    a.text(x[i] + 0.18, H[i] + 1.5, f"{H[i]:g}", ha="center", fontsize=FT["tiny"], color=P.ink())
a.set_xticks(x)
a.set_xticklabels(groups)
for lab in a.get_xticklabels()[1:]:
    lab.set_style("italic")
a.set_ylim(0, 100)
charts.style_axes(a, None, "percent")
charts.title(a, "A  Allozymes")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
b.bar([0, 1], [0.0008, 0.01], 0.5, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.6)
b.set_yscale("log")
b.set_ylim(1e-4, 0.05)
b.set_xticks([0, 1])
b.set_xticklabels(["humans", "D. melanogaster"])
b.get_xticklabels()[1].set_style("italic")
for i, v in enumerate((0.0008, 0.01)):
    b.text(i, v * 1.2, f"{v:g}", ha="center", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(b, None, r"nucleotide diversity $\pi$")
charts.title(b, "B  DNA sequences")
