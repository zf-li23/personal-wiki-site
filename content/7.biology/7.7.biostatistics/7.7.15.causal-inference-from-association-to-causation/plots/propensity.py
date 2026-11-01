"""Propensity scores for maternal smoking (189 births, Baystate Medical Center 1986; Hosmer and Lemeshow;
R MASS::birthwt), estimated by logistic regression on age, weight, race, previous premature labour,
hypertension, uterine irritability and any first-trimester visit. A: distribution of the propensity score
in smokers (orange, upward) and non-smokers (blue, downward). B: standardized mean differences of the
covariates before adjustment (grey), after inverse probability weighting (orange), after weighting with
truncation of the weights at their 1st and 99th percentiles (light orange) and with overlap weights
(green, exact balance by construction); the band marks |SMD| < 0.1.
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
c = {k: np.array([float(r[k]) for r in rows]) for k in ("age", "lwt", "race", "smoke", "ptl", "ht", "ui", "ftv")}
cov = {
    "age": c["age"], "weight": c["lwt"], "black": (c["race"] == 2) * 1.0, "other race": (c["race"] == 3) * 1.0,
    "prev. premature": (c["ptl"] > 0) * 1.0, "hypertension": c["ht"], "uterine irrit.": c["ui"],
    "any visit": (c["ftv"] > 0) * 1.0,
}
t = c["smoke"]
X = np.column_stack([np.ones(t.size)] + list(cov.values()))
b = np.zeros(X.shape[1])
for _ in range(40):
    p = 1 / (1 + np.exp(-X @ b))
    b = b + np.linalg.solve(X.T @ (X * (p * (1 - p))[:, None]), X.T @ (t - p))
ps = 1 / (1 + np.exp(-X @ b))
w_ipw = np.where(t == 1, 1 / ps, 1 / (1 - ps))
lo, hi = np.quantile(w_ipw, [0.01, 0.99])
w_tr = np.clip(w_ipw, lo, hi)
w_ov = np.where(t == 1, 1 - ps, ps)


def smd(x, w):
    m1 = np.average(x[t == 1], weights=w[t == 1])
    m0 = np.average(x[t == 0], weights=w[t == 0])
    s = np.sqrt((x[t == 1].var(ddof=1) + x[t == 0].var(ddof=1)) / 2)
    return (m1 - m0) / s


fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.9), gridspec_kw=dict(width_ratios=[1, 1.15]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.14, top=0.88, wspace=0.42)
ax = axs[0]
bins = np.linspace(0, 1, 21)
h1, _ = np.histogram(ps[t == 1], bins)
h0, _ = np.histogram(ps[t == 0], bins)
ctr = (bins[:-1] + bins[1:]) / 2
ax.bar(ctr, h1, 0.045, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.6, label="smokers (74)")
ax.bar(ctr, -h0, 0.045, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.6, label="non-smokers (115)")
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_yticks([-20, -10, 0, 10])
ax.set_yticklabels(["20", "10", "0", "10"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "propensity score P(smoke | covariates)", "number of mothers")
charts.title(ax, "A  Overlap of propensity scores")
ax = axs[1]
names = list(cov)
ys = np.arange(len(names))[::-1]
ax.axvspan(-0.1, 0.1, color=P.light("neutral"), lw=0)
for (w, tok, mk, lab) in ((np.ones(t.size), "neutral", "o", "unadjusted"), (w_ipw, "rna", "s", "IPW"),
                          (w_tr, "drug", "^", "IPW, truncated"), (w_ov, "plant", "D", "overlap weights")):
    vals = [smd(cov[k], w) for k in names]
    ax.plot(vals, ys, mk, ms=5, color=P.fill(tok), mec=charts.line(tok), label=lab)
ax.axvline(0, color=P.muted(), lw=0.8)
ax.set_yticks(ys)
ax.set_yticklabels(names, fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "standardized mean difference (smokers - non-smokers)")
charts.title(ax, "B  Covariate balance")
