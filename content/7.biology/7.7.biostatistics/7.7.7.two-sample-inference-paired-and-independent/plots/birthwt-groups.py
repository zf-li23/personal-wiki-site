"""Birth weight of infants of 115 non-smoking and 74 smoking mothers (birthwt, Hosmer and Lemeshow,
Baystate Medical Center 1986). A: every infant, the group means and their 95 % t intervals. B: the
estimated difference in means (non-smoker minus smoker) with its 95 % interval, from the pooled-variance
and from the Welch t procedure; both exclude 0.
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
groups = [bwt[smoke == 0], bwt[smoke == 1]]
TOK = ["dna", "rna"]
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5), gridspec_kw=dict(width_ratios=[1.5, 1]))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.35)
rng = np.random.default_rng(0)

ax = axs[0]
for g, x in enumerate(groups):
    ax.scatter(g + rng.uniform(-0.18, 0.18, x.size), x, s=7, color=charts.line(TOK[g]), alpha=0.55, lw=0)
    h = stats.t.isf(0.025, x.size - 1) * x.std(ddof=1) / np.sqrt(x.size)
    ax.errorbar(g + 0.33, x.mean(), h, fmt="o", ms=5, color=P.ink(), capsize=4, lw=1.2)
    ax.text(g + 0.42, x.mean(), f"{x.mean():.0f} g", fontsize=FT["tiny"], color=P.ink(), va="center")
ax.axhline(2500, color=P.muted(), lw=0.7, ls=":")
ax.text(1.62, 2430, "2500 g", fontsize=FT["tiny"], color=P.muted(), ha="right", va="top")
ax.set_xticks([0, 1])
ax.set_xticklabels([f"non-smoker\nn = {groups[0].size}", f"smoker\nn = {groups[1].size}"], fontsize=FT["tiny"])
ax.set_xlim(-0.5, 1.75)
charts.style_axes(ax, None, "birth weight / g")
charts.title(ax, "A  Data, means and 95% CIs")

ax = axs[1]
for k, (eq, lab) in enumerate([(True, "pooled t"), (False, "Welch t")]):
    res = stats.ttest_ind(groups[0], groups[1], equal_var=eq)
    ci = res.confidence_interval()
    est = groups[0].mean() - groups[1].mean()
    ax.errorbar(est, k, xerr=[[est - ci.low], [ci.high - est]], fmt="o", ms=5, color=charts.line("enzyme"),
                capsize=4, lw=1.4)
    ax.text(est, k + 0.22, f"{lab}: {est:.0f} g ({ci.low:.0f} to {ci.high:.0f}), p = {res.pvalue:.4f}",
            fontsize=FT["tiny"], color=P.ink(), ha="center")
ax.axvline(0, color=P.muted(), lw=0.8)
ax.set_ylim(-0.6, 1.7)
ax.set_xlim(-100, 650)
ax.set_yticks([])
charts.style_axes(ax, "difference in mean birth weight / g", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "B  Non-smoker minus smoker")
