"""Selection bias in cross-validation (simulation in the design of Simon and colleagues, 2003).
Each data set has 20 specimens, 10 per class, with 6000 genes whose log-ratios are independent
standard normal in both classes: there is nothing to predict. The classifier is the compound
covariate predictor built from the 10 genes with the largest two-sample t statistics (score =
sum of t_j x_j; threshold halfway between the class means of the score). For 300 simulated data sets,
the cumulative proportion of data sets with at most a given number of misclassifications out of 20:
estimated on the training data themselves (resubstitution), by leave-one-out cross-validation after
selecting the genes on all 20 specimens, and by leave-one-out cross-validation with the selection
repeated inside each fold. Only the last is centered on 10, the expected number for a random guess."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n, g, top, reps = 20, 6000, 10, 300
y = np.r_[np.zeros(10, bool), np.ones(10, bool)]


def tstat(X, yy):
    a, b = X[~yy], X[yy]
    sp = np.sqrt(((a.var(0, ddof=1) * (len(a) - 1)) + b.var(0, ddof=1) * (len(b) - 1)) / (len(yy) - 2))
    return (b.mean(0) - a.mean(0)) / (sp * np.sqrt(1 / len(a) + 1 / len(b)))


def fit(X, yy, genes=None):
    t = tstat(X, yy)
    if genes is None:
        genes = np.argsort(-np.abs(t))[:top]
    w = np.zeros(X.shape[1])
    w[genes] = t[genes]
    s = X @ w
    return w, (s[yy].mean() + s[~yy].mean()) / 2


errs = np.zeros((reps, 3), int)
for r in range(reps):
    X = rng.normal(0, 1, (n, g))
    w, c = fit(X, y)
    errs[r, 0] = np.sum((X @ w > c) != y)
    sel = np.flatnonzero(w)
    e_out = e_in = 0
    for i in range(n):
        tr = np.arange(n) != i
        w1, c1 = fit(X[tr], y[tr], genes=sel)
        e_out += (X[i] @ w1 > c1) != y[i]
        w2, c2 = fit(X[tr], y[tr])
        e_in += (X[i] @ w2 > c2) != y[i]
    errs[r, 1], errs[r, 2] = e_out, e_in

fig, ax = plt.subplots(figsize=(6.5, 3.6))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.16, top=0.88)
k = np.arange(0, 21)
labels = ["resubstitution", "LOOCV, genes selected before", "LOOCV, selection inside each fold"]
for j, (lab, tok) in enumerate(zip(labels, ["negative", "highlight", "positive"])):
    ax.step(k, [(errs[:, j] <= kk).mean() for kk in k], where="post", color=charts.line(tok), lw=1.8, label=lab)
ax.axvline(10, color=P.muted(), ls=":", lw=0.8)
ax.set_xticks(range(0, 21, 2))
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "number of misclassifications (of 20)", "cumulative proportion of data sets")
charts.title(ax, "Error estimates on data with no signal")
