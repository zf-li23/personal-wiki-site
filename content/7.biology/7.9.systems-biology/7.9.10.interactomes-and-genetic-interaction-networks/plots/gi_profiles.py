"""Genetic-interaction profiles group genes into modules (simulation). 72 query genes in six modules
of 12 genes (for example complexes or linear pathways) are crossed with 300 array genes. Each module
has a characteristic pattern of interactions with the array (sparse negative scores with 4% of the
array genes, positive with 1%), shared by its members with gene-specific noise; within a module,
pairs also have positive interactions, as expected for genes acting in the same complex.
A: the matrix of interaction scores epsilon (queries x the first 120 array genes), with queries in
random order. B: the Pearson correlations between query profiles, ordered by average-linkage
hierarchical clustering on 1 - r; the dendrogram cut into six clusters recovers the modules."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.cluster.hierarchy import linkage, leaves_list, fcluster
from scipy.spatial.distance import squareform
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
nm, per, na = 6, 12, 300
nq = nm * per
module = np.repeat(np.arange(nm), per)
pattern = np.zeros((nm, na))
for k in range(nm):
    u = rng.random(na)
    pattern[k, u < 0.04] = -rng.uniform(0.15, 0.5, (u < 0.04).sum())
    pattern[k, (u >= 0.04) & (u < 0.05)] = rng.uniform(0.1, 0.3, ((u >= 0.04) & (u < 0.05)).sum())
present = rng.random((nq, na)) < 0.7            # each member shares 70% of the module's interactions
eps = np.where(present, pattern[module], 0) + rng.normal(0, 0.06, (nq, na))
shuffle = rng.permutation(nq)
eps, module = eps[shuffle], module[shuffle]

r = np.corrcoef(eps)
within = r[module[:, None] == module[None, :]]
between = r[module[:, None] != module[None, :]]
Z = linkage(squareform(1 - r, checks=False), "average")
order = leaves_list(Z)
clusters = fcluster(Z, nm, "maxclust")
# purity of the recovered clusters
purity = sum(np.bincount(module[clusters == c]).max() for c in np.unique(clusters)) / nq

cmap = LinearSegmentedColormap.from_list("gi", [P.edge("negative"), P.surface(), P.edge("positive")])
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.3), gridspec_kw=dict(width_ratios=[1.45, 1]))
fig.subplots_adjust(left=0.07, right=0.96, bottom=0.12, top=0.9, wspace=0.25)
im = a.imshow(eps[:, :120], aspect="auto", cmap=cmap, vmin=-0.4, vmax=0.4, interpolation="nearest")
charts.style_axes(a, "array genes", "query genes (random order)", box=True)
charts.title(a, "A  Interaction scores")
cb = fig.colorbar(im, ax=a, fraction=0.04, pad=0.02)
cb.set_label("epsilon (red: negative, green: positive)", fontsize=7, color=P.ink())
cb.ax.tick_params(labelsize=6, colors=P.muted(), labelcolor=P.ink())
cmap2 = LinearSegmentedColormap.from_list("r", [P.surface(), P.edge("dna")])
im2 = b.imshow(r[np.ix_(order, order)], cmap=cmap2, vmin=0, vmax=1, interpolation="nearest")
for k in range(nq):
    b.add_patch(plt.Rectangle((-4.5, k - 0.5), 3, 1, color=P.fill(P.protein(int(module[order][k]))), clip_on=False, lw=0))
b.set_xlim(-0.5, nq - 0.5)
charts.style_axes(b, "query genes (clustered)", None, box=True)
b.set_yticks([])
charts.title(b, f"B  Profile correlations, clustered (purity {purity:.2f})")
cb2 = fig.colorbar(im2, ax=b, fraction=0.04, pad=0.02)
cb2.set_label("Pearson r", fontsize=7, color=P.ink())
cb2.ax.tick_params(labelsize=6, colors=P.muted(), labelcolor=P.ink())
