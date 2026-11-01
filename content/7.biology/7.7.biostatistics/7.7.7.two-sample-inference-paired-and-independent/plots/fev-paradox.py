"""The FEV paradox in a two-sample comparison (654 children, East Boston; Tager et al. 1979, public
version Kahn 2005). A: FEV of 589 non-smokers and 65 smokers; the two-sample t test says smokers blow
more. B: mean FEV by year of age for the two groups (marker area proportional to the number of
children); among children of the same age the smokers do not have higher FEV, and they are older.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("fev.csv") as fh:
    rows = list(csv.DictReader(fh))
fev = np.array([float(r["fev"]) for r in rows])
age = np.array([int(float(r["age"])) for r in rows])
smoke = np.array([int(r["smoke"]) for r in rows])
TOK = ["dna", "rna"]
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.5), gridspec_kw=dict(width_ratios=[1, 1.6]))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.15, top=0.87, wspace=0.25)
rng = np.random.default_rng(0)

ax = axs[0]
for g in (0, 1):
    x = fev[smoke == g]
    ax.scatter(g + rng.uniform(-0.2, 0.2, x.size), x, s=5, color=charts.line(TOK[g]), alpha=0.45, lw=0)
    ax.plot([g - 0.28, g + 0.28], [x.mean()] * 2, color=P.ink(), lw=1.8)
    ax.text(g + 0.31, x.mean(), f"{x.mean():.2f}", fontsize=FT["tiny"], color=P.ink(), va="center")
ax.set_xticks([0, 1])
ax.set_xticklabels(["non-smoker\nn = 589", "smoker\nn = 65"], fontsize=FT["tiny"])
ax.set_xlim(-0.5, 1.6)
charts.style_axes(ax, None, "FEV / L")
charts.title(ax, "A  Pooled over ages")

ax = axs[1]
ages = np.arange(3, 20)
for g, lab in [(0, "non-smoker"), (1, "smoker")]:
    xs, ys, ns = [], [], []
    for a in ages:
        m = (age == a) & (smoke == g)
        if m.sum() > 0:
            xs.append(a + (0.15 if g else -0.15))
            ys.append(fev[m].mean())
            ns.append(m.sum())
    ax.plot(xs, ys, color=charts.line(TOK[g]), lw=1.0, alpha=0.7)
    ax.scatter(xs, ys, s=6 * np.sqrt(np.array(ns)) * 3, color=P.fill(TOK[g]), edgecolor=charts.line(TOK[g]),
               lw=0.8, label=lab, zorder=3)
leg = ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", markerscale=0.6)
ax.set_xticks(ages[::2])
charts.style_axes(ax, "age / years", "mean FEV / L")
charts.title(ax, "B  Within each year of age")
