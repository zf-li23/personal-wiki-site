"""Odds ratios for low birth weight (189 births, Baystate Medical Center 1986; Hosmer and Lemeshow; R
MASS::birthwt) from univariate logistic regressions (open circles) and from the multiple logistic
regression with mother's age, weight, race, smoking, previous premature labour and hypertension (filled
squares), with 95 % Wald intervals on a log scale. Age is per 5 years and weight per 10 lb.
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
col = {k: np.array([float(r[k]) for r in rows]) for k in ("low", "age", "lwt", "race", "smoke", "ptl", "ht")}
y = col["low"]
v = {
    "age (per 5 y)": col["age"] / 5,
    "weight (per 10 lb)": col["lwt"] / 10,
    "black vs white": (col["race"] == 2).astype(float),
    "other vs white": (col["race"] == 3).astype(float),
    "smoking": col["smoke"],
    "previous premature labour": (col["ptl"] > 0).astype(float),
    "hypertension": col["ht"],
}


def fit(X, y, iters=30):
    b = np.zeros(X.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-X @ b))
        info = X.T @ (X * (p * (1 - p))[:, None])
        b = b + np.linalg.solve(info, X.T @ (y - p))
    p = 1 / (1 + np.exp(-X @ b))
    cov = np.linalg.inv(X.T @ (X * (p * (1 - p))[:, None]))
    return b, np.sqrt(np.diag(cov))


one = np.ones(y.size)
names = list(v)
Xm = np.column_stack([one] + [v[k] for k in names])
bm, sm = fit(Xm, y)
uni = {}
race = np.column_stack([one, v["black vs white"], v["other vs white"]])
br, sr = fit(race, y)
for k in names:
    if k == "black vs white":
        uni[k] = (br[1], sr[1])
    elif k == "other vs white":
        uni[k] = (br[2], sr[2])
    else:
        b, s = fit(np.column_stack([one, v[k]]), y)
        uni[k] = (b[1], s[1])
fig, ax = plt.subplots(figsize=(7.6, 3.6))
fig.subplots_adjust(left=0.3, right=0.97, bottom=0.15, top=0.95)
for i, k in enumerate(names):
    yy = len(names) - i
    b, s = uni[k]
    ax.plot(np.exp([b - 1.96 * s, b + 1.96 * s]), [yy + 0.16] * 2, color=charts.line("neutral"), lw=1.1)
    ax.plot(np.exp(b), yy + 0.16, "o", ms=5, mfc="none", mec=charts.line("neutral"), mew=1.1)
    b, s = bm[i + 1], sm[i + 1]
    ax.plot(np.exp([b - 1.96 * s, b + 1.96 * s]), [yy - 0.16] * 2, color=charts.line("rna"), lw=1.4)
    ax.plot(np.exp(b), yy - 0.16, "s", ms=5, color=P.fill("rna"), mec=charts.line("rna"))
ax.set_yticks(range(len(names), 0, -1))
ax.set_yticklabels(names, fontsize=FT["tiny"])
ax.axvline(1, color=P.muted(), lw=0.8, ls="--")
ax.set_xscale("log")
ax.set_xticks([0.5, 1, 2, 5, 10, 20])
ax.set_xticklabels(["0.5", "1", "2", "5", "10", "20"])
ax.plot([], [], "o", mfc="none", mec=charts.line("neutral"), label="univariate")
ax.plot([], [], "s", color=P.fill("rna"), mec=charts.line("rna"), label="multiple model")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "odds ratio for low birth weight")
