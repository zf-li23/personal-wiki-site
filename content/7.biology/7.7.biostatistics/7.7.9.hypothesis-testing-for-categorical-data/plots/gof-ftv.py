"""Goodness of fit of a Poisson distribution to the number of physician visits in the first trimester
(ftv) of 189 mothers in birthwt (Baystate Medical Center 1986). Bars: observed counts for 0, 1, 2 and
3 or more visits; points: expected counts under a Poisson distribution with the sample mean 0.794. Too
many mothers with no visit and with three or more, too few with one: chi-square 10.4 on 2 df, p = 0.006;
the variance (1.12) exceeds the mean, a sign of overdispersion.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("birthwt.csv") as fh:
    ftv = np.array([int(r["ftv"]) for r in csv.DictReader(fh)])
lam = ftv.mean()
obs = np.array([(ftv == 0).sum(), (ftv == 1).sum(), (ftv == 2).sum(), (ftv >= 3).sum()])
prob = np.array([stats.poisson.pmf(0, lam), stats.poisson.pmf(1, lam), stats.poisson.pmf(2, lam), stats.poisson.sf(2, lam)])
exp = prob * ftv.size
x2 = ((obs - exp) ** 2 / exp).sum()
fig, ax = plt.subplots(figsize=(6.6, 3.3))
fig.subplots_adjust(left=0.12, right=0.98, bottom=0.17, top=0.88)
pos = np.arange(4)
ax.bar(pos, obs, 0.6, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, label="observed")
ax.plot(pos, exp, "o", ms=6, color=charts.line("rna"), label="Poisson expected")
for k in pos:
    ax.text(k + 0.33, obs[k], f"{obs[k]}\n({exp[k]:.1f})", fontsize=FT["tiny"], color=P.ink(), va="bottom")
ax.text(2.0, 85, f"chi-square = {x2:.1f}, 2 df, p = {stats.chi2.sf(x2, 2):.3f}", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks(pos)
ax.set_xticklabels(["0", "1", "2", ">= 3"], fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1, 0.85))
charts.style_axes(ax, "first-trimester physician visits", "mothers")
charts.title(ax, "Poisson fit to visit counts")
