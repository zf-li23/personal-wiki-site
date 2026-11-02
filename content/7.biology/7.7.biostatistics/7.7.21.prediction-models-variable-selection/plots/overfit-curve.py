"""Training error, cross-validation error and the error on new data (simulation, seed 2). A training
sample of n = 30 points from y = sin(2 pi x) + noise (SD 0.3), x uniform on (0, 1), fitted by least-squares
polynomials of degree 1 to 12. A: the data with the fits of degree 1, 3 and 12. B: mean squared error
on the training data, by 10-fold cross-validation, and on 10000 new points from the same population;
dotted line: the noise variance 0.09, the smallest achievable error.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(2)
n = 30
x = rng.uniform(0, 1, n)
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.3, n)
xt = rng.uniform(0, 1, 10000)
yt = np.sin(2 * np.pi * xt) + rng.normal(0, 0.3, 10000)


def fit(xx, yy, d):
    return np.polynomial.polynomial.Polynomial.fit(xx, yy, d)


degs = np.arange(1, 13)
tr, cv, te = [], [], []
fold = rng.permutation(np.arange(n) % 10)
for d in degs:
    f = fit(x, y, d)
    tr.append(np.mean((y - f(x)) ** 2))
    te.append(np.mean((yt - f(xt)) ** 2))
    e = []
    for k in range(10):
        m = fold != k
        e.append(np.mean((y[~m] - fit(x[m], y[m], d)(x[~m])) ** 2))
    cv.append(np.mean(e))
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.8))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.27)
ax = axs[0]
ax.scatter(x, y, s=16, color=P.fill("neutral"), edgecolor=P.edge("neutral"), zorder=3)
g = np.linspace(0, 1, 400)
for d, tok in ((1, "dna"), (3, "enzyme"), (12, "rna")):
    ax.plot(g, fit(x, y, d)(g), color=charts.line(tok), lw=1.5, label=f"degree {d}")
ax.plot(g, np.sin(2 * np.pi * g), color=P.muted(), lw=0.9, ls="--", label="true mean")
ax.set_ylim(-2, 2)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left", ncol=2)
charts.style_axes(ax, "x", "y")
charts.title(ax, "A  Three polynomial fits, n = 30")
ax = axs[1]
ax.plot(degs, tr, "o-", color=charts.line("dna"), ms=3.5, lw=1.4, label="training")
ax.plot(degs, cv, "s-", color=charts.line("enzyme"), ms=3.5, lw=1.4, label="10-fold cross-validation")
ax.plot(degs, te, "^-", color=charts.line("rna"), ms=3.5, lw=1.4, label="new data")
ax.axhline(0.09, color=P.muted(), ls=":", lw=0.9)
ax.set_yscale("log")
ax.set_xticks(degs)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(ax, "polynomial degree (model complexity)", "mean squared error")
charts.title(ax, "B  Error against complexity")
