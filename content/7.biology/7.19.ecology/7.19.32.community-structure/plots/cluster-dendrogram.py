"""Numerical classification of simulated community samples by hierarchical clustering.

Thirty sites, ten from each of three community types; each type has its own mean abundances of 25
species (log-normal, with overlap between types), and site samples are Poisson draws (seed 2).
A: site-by-species abundance matrix (rows in dendrogram order, log scale shading).
B: UPGMA (average-linkage) dendrogram of Bray-Curtis dissimilarities; cutting at 0.6 recovers the three
types (colours: true type of each site).
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from scipy.spatial.distance import pdist

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(2)
nsp, ntype, nper = 25, 3, 10
base = np.exp(rng.normal(1.0, 1.2, (ntype, nsp)))
for k in range(ntype):
    favored = rng.choice(nsp, 8, replace=False)
    base[k, favored] *= 8
X = np.vstack([rng.poisson(base[k], (nper, nsp)) for k in range(ntype)]).astype(float)
types = np.repeat(np.arange(ntype), nper)
D = pdist(X, "braycurtis")
Z = linkage(D, "average")
cut = 0.6
lab = fcluster(Z, cut, "distance")

fig, ax = bio.canvas(30.0, 11.0)
toks = ["dna", "plant", "negative"]
pb = C.axes_at(ax, (15.0, 1.8, 14.0, 7.6))
dn = dendrogram(Z, ax=pb, color_threshold=0, above_threshold_color=P.ink(), no_labels=True)
order = dn["leaves"]
xt = 5 + 10 * np.arange(len(order))
for xx, i in zip(xt, order):
    pb.plot([xx], [-0.02], "s", color=Q.line_color(toks[types[i]]), ms=5, clip_on=False)
pb.axhline(cut, color=P.muted(), lw=0.9, ls=(0, (4, 2)))
pb.text(xt[-1], cut + 0.015, "cut at 0.6: 3 groups", fontsize=FS["tiny"], color=P.ink(), ha="right")
pb.set_ylim(-0.04, max(Z[:, 2]) * 1.08)
C.style_axes(pb, "sites (squares: true community type)", "Bray-Curtis dissimilarity")
pb.spines["bottom"].set_visible(False)
pb.set_xticks([])
bio.panel(ax, "B", (13.3, 10.7))
bio.label(ax, (15.0, 10.0), f"UPGMA dendrogram ({len(set(lab))} groups at the cut)", size="small", bold=True, ha="left")

pa = C.axes_at(ax, (2.0, 1.8, 9.5, 7.6))
cmap = LinearSegmentedColormap.from_list("ab", [P.surface(), P.fill("plant"), P.edge("plant")])
pa.imshow(np.log1p(X[order]), cmap=cmap, aspect="auto", interpolation="nearest")
for r, i in enumerate(order):
    pa.plot([-1.6], [r], "s", color=Q.line_color(toks[types[i]]), ms=4, clip_on=False)
pa.set_xlim(-2.2, nsp - 0.5)
pa.set_xticks([])
pa.set_yticks([])
C.style_axes(pa, "species", "sites (dendrogram order)", box=True)
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Abundance matrix, log(1 + n)", size="small", bold=True, ha="left")
