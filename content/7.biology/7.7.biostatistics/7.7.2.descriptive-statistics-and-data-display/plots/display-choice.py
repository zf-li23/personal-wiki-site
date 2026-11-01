"""Four displays of the same data: birth weight of 115 infants of non-smoking and 74 of smoking mothers
(birthwt, Hosmer and Lemeshow). A: bar chart of the means with standard-error bars hides the spread and
the sample size. B: every observation with the mean and standard deviation. C: box plots (median,
quartiles, 1.5 IQR whiskers). D: violin plots (kernel density) with the median.
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
    rows = list(csv.DictReader(fh))
bwt = np.array([float(r["bwt"]) for r in rows])
smoke = np.array([int(r["smoke"]) for r in rows])
data = [bwt[smoke == 0], bwt[smoke == 1]]
TOK = ["dna", "rna"]
labels = ["non-smoker", "smoker"]
fig, axs = plt.subplots(1, 4, figsize=(11.2, 3.4), sharey=True)
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.14, top=0.87, wspace=0.12)
rng = np.random.default_rng(0)
pos = [0, 1]

ax = axs[0]
for g, x in enumerate(data):
    se = x.std(ddof=1) / np.sqrt(x.size)
    ax.bar(g, x.mean(), 0.6, color=P.fill(TOK[g]), edgecolor=P.edge(TOK[g]), lw=0.8)
    ax.errorbar(g, x.mean(), se, color=P.ink(), capsize=4, lw=1)
charts.title(ax, "A  Mean +/- SE")

ax = axs[1]
for g, x in enumerate(data):
    ax.scatter(g + rng.uniform(-0.2, 0.2, x.size), x, s=6, color=charts.line(TOK[g]), alpha=0.6, lw=0)
    ax.errorbar(g + 0.32, x.mean(), x.std(ddof=1), fmt="o", ms=4, color=P.ink(), capsize=3, lw=1)
charts.title(ax, "B  All points, mean +/- SD")

ax = axs[2]
bp = ax.boxplot(data, positions=pos, widths=0.5, patch_artist=True,
                medianprops=dict(color=P.ink(), lw=1.6), whiskerprops=dict(color=P.ink()), capprops=dict(color=P.ink()),
                flierprops=dict(marker="o", ms=3, mfc="none", mec=P.ink()))
for g, patch in enumerate(bp["boxes"]):
    patch.set_facecolor(P.fill(TOK[g]))
    patch.set_edgecolor(P.edge(TOK[g]))
charts.title(ax, "C  Box plot")

ax = axs[3]
grid = np.linspace(500, 5300, 300)
for g, x in enumerate(data):
    dens = stats.gaussian_kde(x)(grid)
    w = 0.38 * dens / dens.max()
    ax.fill_betweenx(grid, g - w, g + w, color=P.fill(TOK[g]), lw=0)
    ax.plot(g - w, grid, color=P.edge(TOK[g]), lw=0.8)
    ax.plot(g + w, grid, color=P.edge(TOK[g]), lw=0.8)
    ax.plot([g - 0.15, g + 0.15], [np.median(x)] * 2, color=P.ink(), lw=1.6)
charts.title(ax, "D  Violin plot")

for k, ax in enumerate(axs):
    ax.set_xticks(pos)
    ax.set_xticklabels([f"{l}\nn = {d.size}" for l, d in zip(labels, data)], fontsize=FT["tiny"])
    ax.set_xlim(-0.6, 1.6)
    charts.style_axes(ax, None, "birth weight / g" if k == 0 else None)
axs[0].set_ylim(0, 5300)
