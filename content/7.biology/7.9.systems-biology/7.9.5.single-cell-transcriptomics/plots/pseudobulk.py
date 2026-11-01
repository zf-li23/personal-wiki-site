"""Pseudoreplication in single-cell differential expression (simulated null genes: no difference between
the conditions). Three donors per condition; each donor's mean expression of a gene varies around the
common mean (log-normal, s.d. 0.3), cell counts are negative binomial (shape 2) with log-normal size
factors. A: histograms of p-values for 2000 null genes with 200 cells per donor, from a Wilcoxon rank-sum
test that treats the 600 cells of each condition as independent replicates, and from a t-test on the
pseudobulk values of the six donors (log2 of summed counts over summed size factors). Under the null
hypothesis p-values should be uniform (dashed line). B: the share of null genes called significant at
p < 0.05 as the number of cells per donor grows: the cell-level test becomes ever more confident about
a donor effect it mistakes for a condition effect, the pseudobulk test stays at the nominal level."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
D, mu0, sd_donor, theta = 3, 1.0, 0.3, 2.0


def run(G, C):
    size = rng.lognormal(0, 0.3, size=(2, D, C))
    pc, pp = np.empty(G), np.empty(G)
    for g in range(G):
        lam = mu0 * np.exp(rng.normal(0, sd_donor, size=(2, D)))
        m = lam[:, :, None] * size
        x = rng.negative_binomial(theta, theta / (theta + m))
        pc[g] = stats.mannwhitneyu(x[0].ravel(), x[1].ravel(), alternative="two-sided").pvalue
        pb = np.log2((x.sum(2) + 0.5) / size.sum(2))
        pp[g] = stats.ttest_ind(pb[0], pb[1]).pvalue
    return pc, pp


fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.88, wspace=0.3)
pc, pp = run(2000, 200)
ax = axs[0]
bins = np.linspace(0, 1, 21)
ax.hist(pc, bins=bins, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.4, alpha=0.9,
        label=f"cells as replicates: {100 * np.mean(pc < 0.05):.0f}% below 0.05")
ax.hist(pp, bins=bins, histtype="step", color=charts.line("dna"), lw=1.6,
        label=f"pseudobulk, donors as replicates: {100 * np.mean(pp < 0.05):.1f}%")
ax.axhline(2000 / 20, color=P.muted(), lw=0.8, ls="--")
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(ax, "p-value", "number of null genes")
charts.title(ax, "A  p-values of 2000 null genes")
print("A", np.mean(pc < 0.05), np.mean(pp < 0.05))

ax = axs[1]
Cs = [10, 25, 50, 100, 200, 400]
fc, fp = [], []
for C in Cs:
    a, b = run(400, C)
    fc.append(np.mean(a < 0.05)); fp.append(np.mean(b < 0.05))
ax.plot(Cs, 100 * np.array(fc), "o-", color=charts.line("rna"), ms=4, lw=1.4, label="cells as replicates")
ax.plot(Cs, 100 * np.array(fp), "s-", color=charts.line("dna"), ms=4, lw=1.4, label="pseudobulk")
ax.axhline(5, color=P.muted(), lw=0.7, ls="--")
ax.set_xscale("log")
ax.set_ylim(0, 100)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
charts.style_axes(ax, "cells per donor", "false positives at p < 0.05 (%)")
charts.title(ax, "B  More cells, more false positives")
print("B", list(zip(Cs, fc, fp)))
