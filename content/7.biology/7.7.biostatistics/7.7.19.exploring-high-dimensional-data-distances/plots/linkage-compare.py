"""The same points clustered by four linkage criteria (simulation, seed 0): a compact group of 40
points, an elongated group of 60 points and a sparse group of 25 points, the first two joined by a thin
bridge of 8 points; Euclidean distance, tree cut into three clusters. Single linkage chains along the
bridge into one cluster of 108 points and splits off a single outlying point of the sparse group;
complete and average linkage put the near end of the elongated group (10 points) together with the
compact group; Ward's method recovers the three generating groups, dividing the bridge between them.
Lower row: the dendrograms with the cut (dashed); note the different height scales.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster import hierarchy as hc
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
a = rng.normal([0, 0], 0.35, (40, 2))
t = rng.uniform(-1, 1, 60)
b = np.column_stack([5.2 + 2.2 * t, 0.3 * t]) + rng.normal(0, 0.18, (60, 2))
c = rng.normal([2.0, 3.2], 0.45, (25, 2))
bridge = np.column_stack([np.linspace(0.8, 2.7, 8), np.zeros(8)]) + rng.normal(0, 0.05, (8, 2))
X = np.vstack([a, b, c, bridge])
toks = ["dna", "rna", "enzyme"]
fig, axs = plt.subplots(2, 4, figsize=(11.6, 4.4), gridspec_kw={"height_ratios": [1.0, 0.8]})
fig.subplots_adjust(left=0.04, right=0.99, bottom=0.05, top=0.93, wspace=0.18, hspace=0.18)
for k, meth in enumerate(["single", "complete", "average", "ward"]):
    Z = hc.linkage(X, meth)
    lab = hc.fcluster(Z, 3, "maxclust")
    sizes = np.bincount(lab)[1:]
    order = np.argsort(-sizes)
    ax = axs[0, k]
    for rank, cl in enumerate(order):
        m = lab == cl + 1
        ax.scatter(X[m, 0], X[m, 1], s=14, color=P.fill(toks[rank]), edgecolor=P.edge(toks[rank]), lw=0.5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(P.muted())
    charts.title(ax, f"{'ABCD'[k]}  {meth}: sizes {', '.join(str(sizes[o]) for o in order)}")
    ax2 = axs[1, k]
    hc.dendrogram(Z, ax=ax2, no_labels=True, color_threshold=0, above_threshold_color=P.ink())
    for coll in ax2.collections:
        coll.set_linewidth(0.6)
    cut = 0.5 * (Z[-3, 2] + Z[-2, 2])
    ax2.axhline(cut, color=charts.line("rna"), lw=0.9, ls="--")
    ax2.set_xticks([])
    ax2.tick_params(labelsize=FT["tiny"], colors=P.ink())
    for s in ("top", "right", "bottom"):
        ax2.spines[s].set_visible(False)
    ax2.spines["left"].set_color(P.muted())
    if k == 0:
        ax2.set_ylabel("merge height", fontsize=FT["tiny"], color=P.ink())
