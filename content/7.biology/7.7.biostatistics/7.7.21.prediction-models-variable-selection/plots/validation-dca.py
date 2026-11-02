"""Internal validation and decision curve of the birthwt logistic model of chapter 14 (low birth weight
on mother's age, weight, race, smoking, previous premature labour and hypertension; 189 births,
Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt). A: AUC and calibration slope
estimated in the data used for fitting (apparent), by 10-fold cross-validation (average over 20 random
splits) and by the bootstrap optimism correction (200 resamples); seed 0. B: decision curve: net benefit
of acting on the cross-validated predicted risks at each threshold probability, compared with acting
on everyone and on no one.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("birthwt.csv") as fh:
    rows = list(csv.DictReader(fh))
c = {k: np.array([float(r[k]) for r in rows]) for k in ("low", "age", "lwt", "race", "smoke", "ptl", "ht")}
y = c["low"]
X = np.column_stack([np.ones(y.size), c["age"], c["lwt"], c["race"] == 2, c["race"] == 3, c["smoke"],
                     c["ptl"] > 0, c["ht"]]).astype(float)
n = y.size


def fit(X, y):
    b = np.zeros(X.shape[1])
    for _ in range(30):
        pr = 1 / (1 + np.exp(-np.clip(X @ b, -30, 30)))
        b = b + np.linalg.solve(X.T @ (X * (pr * (1 - pr))[:, None]) + 1e-9 * np.eye(X.shape[1]), X.T @ (y - pr))
    return b


def auc(s, y):
    r = np.argsort(np.argsort(s)) + 1.0
    for v in np.unique(s):
        m = s == v
        r[m] = r[m].mean()
    n1 = y.sum()
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * (y.size - n1))


def cslope(lp, y):
    return fit(np.column_stack([np.ones(y.size), lp]), y)[1]


rng = np.random.default_rng(0)
b = fit(X, y)
lp = X @ b
app = (auc(lp, y), 1.0)
cv_auc, cv_sl, cvp = [], [], []
for rep in range(20):
    fold = rng.permutation(np.arange(n) % 10)
    lpc = np.zeros(n)
    for k in range(10):
        m = fold != k
        lpc[~m] = X[~m] @ fit(X[m], y[m])
    cv_auc.append(auc(lpc, y))
    cv_sl.append(cslope(lpc, y))
    cvp.append(1 / (1 + np.exp(-lpc)))
opt_a, opt_s = [], []
for _ in range(200):
    i = rng.integers(0, n, n)
    bb = fit(X[i], y[i])
    opt_a.append(auc(X[i] @ bb, y[i]) - auc(X @ bb, y))
    opt_s.append(1 - cslope(X @ bb, y))
res = {"apparent": app, "10-fold CV": (np.mean(cv_auc), np.mean(cv_sl)),
       "bootstrap": (app[0] - np.mean(opt_a), 1 - np.mean(opt_s))}
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.9), gridspec_kw={"width_ratios": [0.85, 1.15]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.27)
ax = axs[0]
toks = ["neutral", "enzyme", "rna"]
for k, (name, (a, s)) in enumerate(res.items()):
    for j, v in enumerate((a, s)):
        x = j * 4 + k
        ax.bar(x, v, color=P.fill(toks[k]), edgecolor=P.edge(toks[k]), width=0.85, label=name if j == 0 else None)
        ax.text(x, v + 0.02, f"{v:.3f}", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks([1, 5])
ax.set_xticklabels(["AUC", "calibration slope"])
ax.set_ylim(0, 1.18)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=3)
charts.style_axes(ax, None, "estimate")
charts.title(ax, "A  Apparent and validated performance")
ax = axs[1]
pc = cvp[0]
th = np.linspace(0.01, 0.7, 70)
nb = [np.mean((pc >= t) & (y == 1)) - np.mean((pc >= t) & (y == 0)) * t / (1 - t) for t in th]
nball = [y.mean() - (1 - y.mean()) * t / (1 - t) for t in th]
ax.plot(th, nb, color=charts.line("rna"), lw=1.6, label="model (cross-validated risks)")
ax.plot(th, nball, color=charts.line("dna"), lw=1.2, ls="--", label="treat all")
ax.axhline(0, color=P.ink(), lw=0.9, label="treat none")
ax.set_ylim(-0.05, 0.35)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "threshold probability", "net benefit")
charts.title(ax, "B  Decision curve")
