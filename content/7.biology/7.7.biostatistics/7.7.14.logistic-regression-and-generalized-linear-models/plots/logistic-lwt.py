"""Low birth weight (< 2500 g) against the mother's weight at the last menstrual period (189 births,
Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt). A: the 0/1 outcomes (jittered),
the observed proportion in five groups of mother's weight (circles, at the group mean), the straight line
of a linear probability model and the logistic regression curve fitted by maximum likelihood.
B: the same groups on the logit scale (empirical log odds), where the logistic model is a straight line.
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
low = np.array([float(r["low"]) for r in rows])
lwt = np.array([float(r["lwt"]) for r in rows])


def logistic_fit(X, y, iters=30):
    """Maximum likelihood by iteratively reweighted least squares."""
    b = np.zeros(X.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-X @ b))
        w = p * (1 - p)
        b = b + np.linalg.solve(X.T @ (X * w[:, None]), X.T @ (y - p))
    return b


X = np.column_stack([np.ones(low.size), lwt])
b = logistic_fit(X, low)
lp = np.linalg.lstsq(X, low, rcond=None)[0]
edges = np.quantile(lwt, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
grp = np.clip(np.searchsorted(edges, lwt, side="right") - 1, 0, 4)
gx = np.array([lwt[grp == k].mean() for k in range(5)])
gp = np.array([low[grp == k].mean() for k in range(5)])
gn = np.array([(grp == k).sum() for k in range(5)])
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.87, wspace=0.3)
g = np.linspace(60, 320, 300)
ax = axs[0]
ax.scatter(lwt, low + rng.uniform(-0.04, 0.04, low.size), s=7, color=P.fill("neutral"), edgecolor=charts.line("neutral"),
           lw=0.4, alpha=0.8)
ax.plot(g, lp[0] + lp[1] * g, color=charts.line("dna"), lw=1.4, ls="--", label="linear probability")
ax.plot(g, 1 / (1 + np.exp(-(b[0] + b[1] * g))), color=charts.line("rna"), lw=1.8, label="logistic")
ax.plot(gx, gp, "o", ms=6, color=P.fill("enzyme"), mec=charts.line("enzyme"), label="group proportion")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-0.12, 1.12)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "mother's weight / lb", "P(low birth weight)")
charts.title(ax, "A  Probability scale")
ax = axs[1]
el = np.log((gp * gn + 0.5) / ((1 - gp) * gn + 0.5))
se = np.sqrt(1 / (gp * gn + 0.5) + 1 / ((1 - gp) * gn + 0.5))
ax.errorbar(gx, el, yerr=1.96 * se, fmt="o", color=charts.line("enzyme"), mfc=P.fill("enzyme"), capsize=3, lw=1.1)
ax.plot(g, b[0] + b[1] * g, color=charts.line("rna"), lw=1.8)
ax.text(0.97, 0.95, f"logit P = {b[0]:.3f} {b[1]:+.4f} x weight", transform=ax.transAxes, ha="right", va="top",
        fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "mother's weight / lb", "log odds of low birth weight")
charts.title(ax, "B  Logit scale")
