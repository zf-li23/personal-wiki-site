"""Number of facets (ommatidia) in the eyes of Drosophila females with different numbers of copies of the
16A region (approximate values from Sturtevant's 1925 counts). Two genotypes with four copies differ:
three copies in tandem on one chromosome (BB/+) reduce the eye more than two plus two (B/B)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
geno = ["+/+", "B/+", "B/B", "BB/+", "BB/BB"]
copies = [2, 3, 4, 4, 6]
facets = [779, 358, 68, 45, 25]
toks = ["positive", "dna", "enzyme", "receptor", "negative"]
fig, ax = plt.subplots(figsize=(6.4, 3.6))
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.2, top=0.92)
x = np.arange(len(geno))
for xi, f, t in zip(x, facets, toks):
    ax.bar(xi, f, width=0.62, color=P.fill(t), edgecolor=P.edge(t), lw=1.0)
    ax.text(xi, f + 15, str(f), ha="center", va="bottom", fontsize=bio.core.FONT["small"], color=P.ink())
ax.set_xticks(x, [f"${g}$\n{c} copies" for g, c in zip(geno, copies)])
ax.set_ylim(0, 880)
charts.style_axes(ax, None, "facets per eye")
ax.annotate("", xy=(3, 165), xytext=(2, 165), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(2.5, 180, "same dose,\ndifferent arrangement", ha="center", va="bottom", fontsize=bio.core.FONT["tiny"],
        color=P.muted())
