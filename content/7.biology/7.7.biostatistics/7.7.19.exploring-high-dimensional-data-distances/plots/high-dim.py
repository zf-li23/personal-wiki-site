"""Two properties of high-dimensional data (simulation, seed 0). A: concentration of distances. For 100
points drawn from a standard normal or a uniform distribution in p dimensions, the relative contrast
(largest minus smallest distance to a query point, divided by the smallest) falls as p grows: in high
dimensions all points are nearly equally far apart, unless the data have low-dimensional structure.
B: eigenvalues of the sample covariance matrix of n = 20 observations of p = 50 independent standard
normal variables. All population eigenvalues equal 1 (dashed), but the sample eigenvalues spread from
0 to 6.3, and 31 of them are exactly 0, since the rank is at most n - 1 = 19: the matrix is
singular, the Mahalanobis distance is undefined, and the leading sample components overstate variance.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
ps = np.unique(np.round(np.logspace(0, 4, 17)).astype(int))
fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.5))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.87, wspace=0.3)
ax = axs[0]
for tok, name, gen in (("dna", "normal", lambda p: rng.normal(size=(101, p))),
                       ("rna", "uniform", lambda p: rng.uniform(size=(101, p)))):
    rc = []
    for p in ps:
        vals = []
        for _ in range(20):
            X = gen(p)
            d = np.sqrt(((X[1:] - X[0]) ** 2).sum(1))
            vals.append((d.max() - d.min()) / d.min())
        rc.append(np.median(vals))
    ax.plot(ps, rc, "o-", color=charts.line(tok), ms=3.5, lw=1.4, label=name)
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "dimension p", "(d_max - d_min) / d_min")
charts.title(ax, "A  Distances concentrate")
ax = axs[1]
n, p = 20, 50
X = rng.normal(size=(n, p))
ev = np.sort(np.linalg.eigvalsh(np.cov(X, rowvar=False)))[::-1]
ev[ev < 1e-10] = 0
ax.bar(np.arange(1, p + 1), ev, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), width=0.8)
ax.axhline(1, color=P.muted(), ls="--", lw=0.9)
ax.text(p, 1.12, "population eigenvalues = 1", ha="right", fontsize=FT["tiny"], color=P.ink())
ax.text(35, 0.35, f"{(ev == 0).sum()} eigenvalues = 0", ha="center", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "rank", "eigenvalue of sample covariance")
charts.title(ax, f"B  n = {n}, p = {p}")
