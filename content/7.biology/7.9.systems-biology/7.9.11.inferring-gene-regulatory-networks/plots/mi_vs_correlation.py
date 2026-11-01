"""Correlation and mutual information for six kinds of dependence (simulated, n = 400 samples each).
Each panel shows the expression of a target y against a regulator x, with the Pearson correlation r,
the Spearman correlation rho and the mutual information I estimated by the k-nearest-neighbor
estimator of Kraskov, Stoegbauer and Grassberger (k = 4), in bits. Linear and saturating (Hill)
responses are detected by all three; the non-monotone responses (a U-shape, a periodic response,
a ring) have correlations near zero but clearly positive mutual information; independent data give
values near zero for all three."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
from scipy.special import digamma
from scipy.stats import spearmanr
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n = 400


def ksg_mi(x, y, k=4):
    """Kraskov-Stoegbauer-Grassberger estimator (algorithm 1), in bits."""
    x = (x - x.mean()) / x.std() + rng.normal(0, 1e-10, len(x))
    y = (y - y.mean()) / y.std() + rng.normal(0, 1e-10, len(y))
    pts = np.column_stack([x, y])
    d, _ = cKDTree(pts).query(pts, k + 1, p=np.inf)
    eps = d[:, k]
    xs, ys = np.sort(x), np.sort(y)
    nx = np.searchsorted(xs, x + eps, "left") - np.searchsorted(xs, x - eps, "right") - 1
    ny = np.searchsorted(ys, y + eps, "left") - np.searchsorted(ys, y - eps, "right") - 1
    mi = digamma(k) + digamma(len(x)) - np.mean(digamma(nx + 1) + digamma(ny + 1))
    return max(mi, 0.0) / np.log(2)


cases = []
x = rng.normal(0, 1, n)
cases.append(("Linear", x, 0.8 * x + rng.normal(0, 0.6, n)))
x = rng.uniform(0, 4, n)
cases.append(("Saturating (Hill, n = 4)", x, x**4 / (1 + x**4) + rng.normal(0, 0.08, n)))
x = rng.uniform(-2, 2, n)
cases.append(("U-shaped", x, x**2 + rng.normal(0, 0.4, n)))
x = rng.uniform(0, 4 * np.pi, n)
cases.append(("Periodic", x, np.sin(x) + rng.normal(0, 0.25, n)))
t = rng.uniform(0, 2 * np.pi, n)
cases.append(("Ring", np.cos(t) + rng.normal(0, 0.08, n), np.sin(t) + rng.normal(0, 0.08, n)))
cases.append(("Independent", rng.normal(0, 1, n), rng.normal(0, 1, n)))

fig, axes = plt.subplots(2, 3, figsize=(9.6, 6.0))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.08, top=0.9, wspace=0.28, hspace=0.55)
for ax, (name, x, y) in zip(axes.flat, cases):
    r = np.corrcoef(x, y)[0, 1]
    rho = spearmanr(x, y)[0]
    mi = ksg_mi(x, y)
    ax.scatter(x, y, s=5, color=charts.line("dna"), alpha=0.6, lw=0)
    charts.style_axes(ax, "regulator x", "target y")
    charts.title(ax, name)
    ax.text(0.02, 1.0, f"r = {r:.2f}   rho = {rho:.2f}   I = {mi:.2f} bit", transform=ax.transAxes,
            fontsize=7, color=P.ink(), va="bottom")
    ax.set_title(name, fontsize=8.5, color=P.ink(), loc="left", weight="bold", pad=14)
