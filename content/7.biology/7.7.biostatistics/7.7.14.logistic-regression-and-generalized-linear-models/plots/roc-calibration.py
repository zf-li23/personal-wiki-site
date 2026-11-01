"""Discrimination and calibration of the multiple logistic model for low birth weight (189 births,
Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt; model with mother's age, weight, race,
smoking, previous premature labour and hypertension). A: ROC curve of the fitted probabilities (AUC 0.750)
and of smoking alone (AUC 0.585). B: calibration plot: observed proportion against the mean predicted
probability in ten groups of predicted risk (19 or 18 births each), with 95 % Wilson intervals; the
Hosmer-Lemeshow statistic is 8.65 on 8 degrees of freedom (p = 0.37). The model is evaluated on the
data it was fitted to, which flatters both measures.
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
b = np.zeros(X.shape[1])
for _ in range(30):
    p = 1 / (1 + np.exp(-X @ b))
    b = b + np.linalg.solve(X.T @ (X * (p * (1 - p))[:, None]), X.T @ (y - p))
p = 1 / (1 + np.exp(-X @ b))


def roc(score, y):
    thr = np.unique(score)[::-1]
    tpr = [0.0] + [((score >= t) & (y == 1)).sum() / (y == 1).sum() for t in thr]
    fpr = [0.0] + [((score >= t) & (y == 0)).sum() / (y == 0).sum() for t in thr]
    return np.array(fpr), np.array(tpr)


fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.88, wspace=0.3)
ax = axs[0]
for score, tok, name in ((p, "rna", "multiple model"), (c["smoke"], "dna", "smoking only")):
    f, t = roc(score, y)
    auc = np.trapezoid(t, f)
    ax.plot(f, t, color=charts.line(tok), lw=1.7, label=f"{name}, AUC {auc:.3f}")
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.8, ls="--")
ax.set_aspect("equal")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "1 - specificity", "sensitivity")
charts.title(ax, "A  Discrimination")
ax = axs[1]
order = np.argsort(p, kind="stable")
ranks = np.empty(y.size)
ranks[order] = np.arange(1, y.size + 1)
cuts = np.quantile(ranks, np.linspace(0, 1, 11))
gid = np.clip(np.searchsorted(cuts, ranks, side="left") - 1, 0, 9)
groups = [np.where(gid == k)[0] for k in range(10)]
hl = sum((y[g].sum() - p[g].sum()) ** 2 / (p[g].sum() * (1 - p[g].mean())) for g in groups)
for g in groups:
    n, o, e = len(g), y[g].sum(), p[g].mean()
    ph = o / n
    z = 1.96
    centre = (ph + z * z / (2 * n)) / (1 + z * z / n)
    half = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    ax.errorbar(e, ph, yerr=[[ph - (centre - half)], [centre + half - ph]], fmt="o", color=charts.line("enzyme"),
                mfc=P.fill("enzyme"), capsize=2.5, lw=1.0, ms=5)
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.8, ls="--")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.text(0.03, 0.96, f"Hosmer-Lemeshow {hl:.2f}, df 8", transform=ax.transAxes, va="top",
        fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "mean predicted probability", "observed proportion")
charts.title(ax, "B  Calibration (10 risk groups)")
