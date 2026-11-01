"""Analysis of covariance for birth weight (189 births, Baystate Medical Center 1986; Hosmer and Lemeshow;
R MASS::birthwt). A: birth weight against the mother's weight at the last menstrual period (lb), by race;
lines: the model with race, smoking and mother's weight (common slope), drawn for non-smokers.
B: crude mean birth weight of each race and the adjusted mean (at the average mother's weight and the
average smoking proportion) with 95 % intervals.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("birthwt.csv") as fh:
    rows = list(csv.DictReader(fh))
bwt = np.array([float(r["bwt"]) for r in rows])
lwt = np.array([float(r["lwt"]) for r in rows])
smoke = np.array([float(r["smoke"]) for r in rows])
race = np.array([int(r["race"]) for r in rows])
names = {1: "white", 2: "black", 3: "other"}
tok = {1: "dna", 2: "rna", 3: "plant"}
X = np.column_stack([np.ones(bwt.size), race == 2, race == 3, smoke, lwt]).astype(float)
beta, *_ = np.linalg.lstsq(X, bwt, rcond=None)
res = bwt - X @ beta
df = bwt.size - X.shape[1]
cov = res @ res / df * np.linalg.inv(X.T @ X)
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6), gridspec_kw=dict(width_ratios=[1.35, 1]))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.3)
ax = axs[0]
g = np.linspace(80, 250, 10)
for rc in (1, 2, 3):
    m = race == rc
    ax.scatter(lwt[m], bwt[m], s=10, color=P.fill(tok[rc]), edgecolor=charts.line(tok[rc]), lw=0.5, alpha=0.8,
               label=names[rc])
    x0 = np.array([1, rc == 2, rc == 3, 0, 0], float)
    ax.plot(g, x0 @ beta + beta[4] * g, color=charts.line(tok[rc]), lw=1.5)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "mother's weight / lb", "birth weight / g")
charts.title(ax, "A  Parallel lines (non-smokers)")
ax = axs[1]
t = stats.t.ppf(0.975, df)
for k, rc in enumerate((1, 2, 3)):
    yy = bwt[race == rc]
    se0 = yy.std(ddof=1) / np.sqrt(yy.size)
    ax.errorbar(k - 0.12, yy.mean(), yerr=stats.t.ppf(0.975, yy.size - 1) * se0, color=P.muted(), marker="o",
                ms=5, capsize=3, lw=1.2, mfc="none")
    x0 = np.array([1, rc == 2, rc == 3, smoke.mean(), lwt.mean()], float)
    est = x0 @ beta
    se = np.sqrt(x0 @ cov @ x0)
    ax.errorbar(k + 0.12, est, yerr=t * se, color=charts.line(tok[rc]), marker="s", ms=5, capsize=3, lw=1.5,
                mfc=P.fill(tok[rc]))
ax.set_xticks(range(3))
ax.set_xticklabels(["white", "black", "other"], fontsize=FT["tiny"])
ax.set_xlim(-0.5, 2.5)
ax.text(0.02, 0.98, "circles: crude means;  squares: adjusted means", transform=ax.transAxes, va="top",
        fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, None, "mean birth weight / g")
charts.title(ax, "B  Crude and adjusted means")
