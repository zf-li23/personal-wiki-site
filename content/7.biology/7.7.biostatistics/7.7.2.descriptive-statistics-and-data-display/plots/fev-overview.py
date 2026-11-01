"""A first look at the FEV data (654 children aged 3-19, East Boston; Tager et al. 1979).

A: histogram of FEV with a kernel density estimate; the mean (2.64 L) lies to the right of the median
(2.55 L) because the distribution is skewed to the right. B: box plots with every observation overlaid,
by smoking status; the 65 smokers have the higher median. C: FEV against age; the smokers are all aged 9 or
older, which explains panel B.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("fev.csv") as fh:
    rows = list(csv.DictReader(fh))
fev = np.array([float(r["fev"]) for r in rows])
age = np.array([float(r["age"]) for r in rows])
smoke = np.array([int(r["smoke"]) for r in rows])
TOK = {0: "dna", 1: "rna"}
NAME = {0: "non-smoker", 1: "smoker"}

fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.7), gridspec_kw={"width_ratios": [1.15, 0.8, 1.15]})
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.15, top=0.88, wspace=0.3)

ax = axs[0]
ax.hist(fev, bins=np.arange(0.5, 6.01, 0.25), density=True, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6)
grid = np.linspace(0.3, 6.2, 300)
ax.plot(grid, stats.gaussian_kde(fev)(grid), color=charts.line("dna"), lw=1.8, label="kernel density")
for v, name, ls in ((fev.mean(), "mean", "-"), (np.median(fev), "median", "--")):
    ax.axvline(v, color=charts.line("rna"), lw=1.1, ls=ls, label=f"{name} {v:.2f} L")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "FEV / L", "density")
charts.title(ax, "A  Distribution of FEV (n = 654)")

ax = axs[1]
rng = np.random.default_rng(0)
data = [fev[smoke == g] for g in (0, 1)]
for g, x in enumerate(data):
    ax.scatter(g + rng.uniform(-0.18, 0.18, x.size), x, s=4, color=charts.line(TOK[g]), alpha=0.45, lw=0)
bp = ax.boxplot(data, positions=[0, 1], widths=0.5, patch_artist=True, showfliers=False,
                medianprops=dict(color=P.ink(), lw=1.6), whiskerprops=dict(color=P.ink()), capprops=dict(color=P.ink()))
for patch in bp["boxes"]:
    patch.set_facecolor("none")
    patch.set_edgecolor(P.ink())
ax.set_xticks([0, 1])
ax.set_xticklabels([f"{NAME[g]}\n(n = {data[g].size})" for g in (0, 1)])
charts.style_axes(ax, None, "FEV / L")
charts.title(ax, "B  By smoking status")

ax = axs[2]
for g in (0, 1):
    m = smoke == g
    ax.scatter(age[m] + rng.uniform(-0.25, 0.25, m.sum()), fev[m], s=7 if g else 5, color=charts.line(TOK[g]),
               alpha=0.9 if g else 0.5, lw=0, label=NAME[g])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "age / years", "FEV / L")
charts.title(ax, "C  FEV against age")
