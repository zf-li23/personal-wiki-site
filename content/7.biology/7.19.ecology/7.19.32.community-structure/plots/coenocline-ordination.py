"""A simulated coenocline and three ordinations of the same data.

Twenty species have Gaussian responses y = h exp(-(x - u)^2 / (2 t^2)) along one environmental gradient
x from 0 to 100, with optima u spread over -10 to 110, tolerances t between 6 and 14 and maxima h between
20 and 100 (random, seed 1). Forty sites are placed evenly along the gradient; observed abundances are
Poisson draws around the expected values.
A: the response curves (coenocline).
B: principal component analysis (covariance of the abundances): sites, colored by their true position
on the gradient, lie on a horseshoe, with the two ends folded toward each other.
C: correspondence analysis: an arch; axis 2 is a quadratic function of axis 1 (the arch effect), and the
ends of the gradient are compressed.
D: nonmetric multidimensional scaling of Bray-Curtis dissimilarities in one dimension (best of 8 starts),
plotted against the true position: the order of the sites is recovered almost perfectly (Spearman rho
printed) and the scores are nearly linear in x.
In two dimensions NMDS of these data also bends, because sites at the two ends share no species.
"""

import numpy as np
from sklearn.manifold import MDS
from scipy.spatial.distance import pdist, squareform

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(1)
ns, nsite = 20, 40
u = np.sort(rng.uniform(-10, 110, ns))
t = rng.uniform(6, 14, ns)
h = rng.uniform(20, 100, ns)
xs = np.linspace(0, 100, nsite)
mu = h[None, :] * np.exp(-((xs[:, None] - u[None, :]) ** 2) / (2 * t[None, :] ** 2))
Y = rng.poisson(mu).astype(float)
keep = Y.sum(0) > 0
Y = Y[:, keep]

fig, ax = bio.canvas(34.0, 10.5)
cmap = __import__("matplotlib").colormaps["viridis"]
pa = C.axes_at(ax, (1.8, 1.8, 7.0, 7.0))
xx = np.linspace(0, 100, 300)
for i in range(ns):
    pa.plot(xx, h[i] * np.exp(-((xx - u[i]) ** 2) / (2 * t[i] ** 2)), color=Q.line_color("plant"), lw=1.0)
pa.set_xlim(0, 100)
pa.set_ylim(0, 105)
C.style_axes(pa, "environmental gradient x", "expected abundance")
bio.panel(ax, "A", (0.2, 10.3))
bio.label(ax, (1.8, 9.6), "Coenocline: 20 species", size="small", bold=True, ha="left")

# PCA
Yc = Y - Y.mean(0)
U_, s_, Vt = np.linalg.svd(Yc, full_matrices=False)
pcs = U_[:, :2] * s_[:2]
# CA
Pm = Y / Y.sum()
r = Pm.sum(1)
c = Pm.sum(0)
Sm = (Pm - np.outer(r, c)) / np.sqrt(np.outer(r, c))
Uc, sc, Vc = np.linalg.svd(Sm, full_matrices=False)
ca = (Uc[:, :2] * sc[:2]) / np.sqrt(r)[:, None]
# NMDS
Dm = squareform(pdist(Y, "braycurtis"))
nm = MDS(n_components=1, metric_mds=False, metric="precomputed", n_init=8, random_state=0, max_iter=500,
         init="random").fit(Dm)
co = nm.embedding_[:, 0]
if np.corrcoef(co, xs)[0, 1] < 0:
    co = -co
from scipy.stats import spearmanr
rho = spearmanr(co, xs)[0]
co = np.column_stack([xs, co])

for k, (Z, title, letter, xl, yl) in enumerate(((pcs, "PCA: horseshoe", "B", "PC 1", "PC 2"),
                                                (ca, "CA: arch", "C", "CA axis 1", "CA axis 2"),
                                                (co, f"1-D NMDS, Bray-Curtis (rho = {rho:.3f})", "D", "true position x", "NMDS score"))):
    x0 = 10.6 + 8.0 * k
    pb = C.axes_at(ax, (x0, 1.8, 6.2, 7.0))
    pb.plot(Z[:, 0], Z[:, 1], color=P.mix(P.muted(), P.surface(), 0.4), lw=0.7, zorder=1)
    pb.scatter(Z[:, 0], Z[:, 1], c=xs, cmap=cmap, s=16, zorder=2, edgecolors="none")
    pb.set_xticks([])
    pb.set_yticks([])
    C.style_axes(pb, xl, yl, box=True)
    bio.panel(ax, letter, (x0 - 0.9, 10.3))
    bio.label(ax, (x0, 9.6), title, size="small", bold=True, ha="left")
