"""Sample distances and clustering in the airway RNA-seq experiment (Himes et al. 2014, GEO GSE52778;
Bioconductor package airway): eight samples from four airway smooth-muscle cell lines, untreated or
treated with dexamethasone. Variance-stabilized expression (pydeseq2 vst) of the 500 most variable genes.
A: Euclidean distances between samples, ordered by average-linkage hierarchical clustering (dendrogram
on top). B: the 40 most variable genes, centred and scaled per gene (z-scores), genes clustered by
average linkage on correlation distance, samples in the order of panel A.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from scipy.cluster import hierarchy as hc
from scipy.spatial.distance import pdist, squareform
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("airway_expr.csv") as fh:
    rows = [r for r in csv.reader(line for line in fh if not line.startswith("#"))]
head, rows = rows[0], rows[1:]
vcols = [j for j, h in enumerate(head) if h.startswith("v:")]
genes = [r[0] for r in rows]
V = np.array([[float(r[j]) for j in vcols] for r in rows])
lab = [head[j].split(":")[2] for j in vcols]
trt = [head[j].split(":")[3] == "trt" for j in vcols]
names = [f"{c} {'dex' if t else 'ctrl'}" for c, t in zip(lab, trt)]
top = np.argsort(-V.var(1, ddof=1), kind="stable")[:500]
X = V[top].T
D = pdist(X)
Z = hc.linkage(D, "average")
order = hc.leaves_list(Z)

fig = plt.figure(figsize=(10.4, 4.9))
cmap_d = LinearSegmentedColormap.from_list("d", [P.edge("dna"), P.fill("dna"), P.surface()])
axd = fig.add_axes([0.13, 0.80, 0.30, 0.13])
dn = hc.dendrogram(Z, ax=axd, no_labels=True, color_threshold=0, above_threshold_color=P.ink())
for coll in axd.collections:
    coll.set_linewidth(1.0)
axd.axis("off")
axm = fig.add_axes([0.13, 0.17, 0.30, 0.62])
M = squareform(D)[np.ix_(order, order)]
im = axm.imshow(M, cmap=cmap_d, vmin=0, vmax=M.max())
axm.set_xticks(range(8))
axm.set_yticks(range(8))
axm.set_xticklabels([names[i] for i in order], rotation=60, ha="right", fontsize=FT["tiny"], color=P.ink())
axm.set_yticklabels([names[i] for i in order], fontsize=FT["tiny"], color=P.ink())
for i in range(8):
    for j in range(8):
        if i != j:
            axm.text(j, i, f"{M[i, j]:.0f}", ha="center", va="center", fontsize=5.8,
                     color=P.on_fill() if M[i, j] < 0.6 * M.max() else P.ink())
for s in axm.spines.values():
    s.set_visible(False)
axm.tick_params(length=0)
cb = fig.colorbar(im, cax=fig.add_axes([0.445, 0.17, 0.012, 0.62]))
cb.ax.tick_params(labelsize=FT["tiny"], colors=P.ink())
cb.outline.set_visible(False)
cb.set_label("Euclidean distance", fontsize=FT["tiny"], color=P.ink())
axd.set_title("A  Sample distances, average linkage", loc="left", fontsize=FT["small"], color=P.ink())

g40 = top[:40]
Y = V[g40][:, order]
Y = (Y - Y.mean(1, keepdims=True)) / Y.std(1, ddof=1, keepdims=True)
Zg = hc.linkage(pdist(V[g40], "correlation"), "average")
og = hc.leaves_list(Zg)
cmap_z = LinearSegmentedColormap.from_list("z", [P.edge("dna"), P.surface(), P.edge("rna")])
axg = fig.add_axes([0.61, 0.17, 0.22, 0.73])
im2 = axg.imshow(Y[og], cmap=cmap_z, vmin=-2, vmax=2, aspect="auto")
axg.yaxis.tick_right()
axg.set_yticks(range(40))
axg.set_yticklabels([genes[g40[k]] for k in og], fontsize=4.8, color=P.ink(), fontstyle="italic")
axg.set_xticks(range(8))
axg.set_xticklabels([names[i] for i in order], rotation=60, ha="right", fontsize=FT["tiny"], color=P.ink())
axg.tick_params(length=0)
for s in axg.spines.values():
    s.set_visible(False)
axt = fig.add_axes([0.545, 0.17, 0.063, 0.73])
hc.dendrogram(Zg, ax=axt, orientation="left", no_labels=True, color_threshold=0, above_threshold_color=P.ink())
axt.invert_yaxis()
for coll in axt.collections:
    coll.set_linewidth(0.8)
axt.axis("off")
cb2 = fig.colorbar(im2, cax=fig.add_axes([0.91, 0.17, 0.012, 0.73]))
cb2.ax.tick_params(labelsize=FT["tiny"], colors=P.ink())
cb2.outline.set_visible(False)
cb2.set_label("z-score of vst expression", fontsize=FT["tiny"], color=P.ink())
axg.set_title("B  40 most variable genes", loc="left", fontsize=FT["small"], color=P.ink())
