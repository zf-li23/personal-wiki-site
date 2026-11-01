"""Weighted co-expression network analysis on simulated data. Expression of 600 genes is simulated
in 60 samples: five modules of 140, 110, 80, 50 and 20 genes follow a module eigengene (each gene
with its own loading between 0.6 and 0.95 and a random sign) plus noise, and 200 genes are pure
noise. A: the scale-free topology fit index (signed R squared of the regression of log10 p(k) on
log10 k over ten bins of connectivity) for the soft threshold beta of the unsigned adjacency
|r|^beta; the dashed line is the conventional cutoff 0.8, first exceeded at beta = 4 (dotted).
B: the mean connectivity, which falls steeply with beta (dotted: beta = 6). C: the topological overlap matrix at
beta = 6, the usual default, with genes ordered by
average-linkage hierarchical clustering on 1 - TOM; the bar on the left marks the simulated modules
(grey: noise genes). Cutting the tree at height 0.97 and keeping branches of at least 15 genes
gives five modules that agree with the simulated ones (adjusted Rand index 0.99); no noise gene is
placed in a module and 3 module genes are left unassigned."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.cluster.hierarchy import linkage, leaves_list, fcluster
from scipy.spatial.distance import squareform
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
ns, sizes, nnoise = 60, [140, 110, 80, 50, 20], 200
blocks, labels = [], []
for m, s in enumerate(sizes):
    eig = rng.normal(0, 1, ns)
    load = rng.uniform(0.6, 0.95, s) * rng.choice([-1, 1], s)
    blocks.append(np.outer(load, eig) + rng.normal(0, 1, (s, ns)) * np.sqrt(1 - load[:, None] ** 2))
    labels += [m] * s
blocks.append(rng.normal(0, 1, (nnoise, ns)))
labels = np.array(labels + [-1] * nnoise)
X = np.vstack(blocks)
R = np.corrcoef(X)
np.fill_diagonal(R, 0)

betas = np.arange(1, 21)
fit, meank = [], []
for b in betas:
    A = np.abs(R) ** b
    k = A.sum(1)
    h, edges = np.histogram(k, 10)
    mid = 0.5 * (edges[1:] + edges[:-1])
    ok = h > 0
    lx, ly = np.log10(mid[ok]), np.log10(h[ok] / h.sum())
    slope, icpt = np.polyfit(lx, ly, 1)
    r2 = np.corrcoef(lx, ly)[0, 1] ** 2
    fit.append(-np.sign(slope) * r2)
    meank.append(k.mean())
fit = np.array(fit)
first = int(betas[np.argmax(fit > 0.8)])          # first beta with fit index above 0.8
beta = 6                                          # the usual default for unsigned networks
A = np.abs(R) ** beta
k = A.sum(1)
L = A @ A
TOM = (L + A) / (np.minimum.outer(k, k) + 1 - A)
np.fill_diagonal(TOM, 1)
Z = linkage(squareform(1 - TOM, checks=False), "average")
order = leaves_list(Z)
clusters = fcluster(Z, 0.97, "distance")              # cut the tree at height 0.97
size = np.bincount(clusters)
clusters = np.where(size[clusters] >= 15, clusters, 0)  # modules of at least 15 genes; 0: unassigned
from sklearn.metrics import adjusted_rand_score
ari = adjusted_rand_score(labels, clusters)

fig = plt.figure(figsize=(10, 4.2))
a = fig.add_axes([0.06, 0.58, 0.27, 0.32])
b = fig.add_axes([0.06, 0.12, 0.27, 0.32])
c = fig.add_axes([0.45, 0.08, 0.36, 0.84])
a.plot(betas, fit, "o-", ms=3, color=charts.line("dna"))
a.axhline(0.8, ls="--", color=P.muted(), lw=0.8)
a.axvline(first, ls=":", color=charts.line("highlight"), lw=0.8)
charts.style_axes(a, None, "fit index (signed R^2)")
charts.title(a, "A  Scale-free fit")
b.semilogy(betas, meank, "o-", ms=3, color=charts.line("rna"))
b.axvline(beta, ls=":", color=charts.line("highlight"), lw=0.8)
charts.style_axes(b, "soft threshold beta", "mean connectivity")
charts.title(b, "B  Connectivity")
cmap = LinearSegmentedColormap.from_list("tom", [P.surface(), P.edge("dna")])
c.imshow(TOM[np.ix_(order, order)], cmap=cmap, vmin=0, vmax=0.3, interpolation="nearest")
lab = labels[order]
for i, m in enumerate(lab):
    col = P.fill(P.protein(int(m))) if m >= 0 else P.muted()
    c.add_patch(plt.Rectangle((-22, i - 0.5), 16, 1, color=col, clip_on=False, lw=0))
c.set_xlim(-0.5, len(lab) - 0.5)
c.set_xticks([]); c.set_yticks([])
charts.title(c, f"C  Topological overlap (beta = {beta}), clustered")
