"""Differential expression in the airway data (dexamethasone against untreated, design ~ cell + dex,
DESeq2 model fitted with pydeseq2; 22369 genes with at least 10 reads in total). A: MA plot of the
maximum-likelihood log2 fold changes against the mean normalized count; genes with adjusted p < 0.1
in colour. Fold changes of weakly expressed genes scatter widely. B: the same after shrinkage of the
fold changes towards zero (an adaptive prior on the log fold changes, as in apeglm): noisy fold
changes of weak genes shrink, well-measured ones hardly change. C: volcano plot, -log10 adjusted p
against the shrunken log2 fold change, with the thresholds padj = 0.05 and |log2 FC| = 1. D: the
histogram of the raw p-values of the genes kept by independent filtering: a uniform floor (null
genes, dashed: the Storey estimate of its height) and a peak near zero (true changes)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
d = np.loadtxt("airway_de.csv", delimiter=",", comments="#", skiprows=3)
bm, lfc, shr, mlp = 10 ** (d[:, 0] / 100), d[:, 1] / 100, d[:, 2] / 100, d[:, 3] / 10
has = mlp >= 0
sig = has & (mlp > 1)  # padj < 0.1
fig, axs = plt.subplots(1, 4, figsize=(13.5, 3.5))
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.87, wspace=0.33)
for ax, y, ttl in [(axs[0], lfc, "A  MA plot, MLE"), (axs[1], shr, "B  MA plot, shrunken")]:
    ax.scatter(bm[~sig], np.clip(y[~sig], -6, 6), s=1.5, color=P.fill("neutral"), lw=0, rasterized=True)
    up, dn = sig & (y > 0), sig & (y < 0)
    ax.scatter(bm[up], np.clip(y[up], -6, 6), s=2, color=charts.line("rna"), lw=0, rasterized=True)
    ax.scatter(bm[dn], np.clip(y[dn], -6, 6), s=2, color=charts.line("dna"), lw=0, rasterized=True)
    ax.axhline(0, color=P.muted(), lw=0.7)
    ax.set_xscale("log")
    ax.set_ylim(-6.3, 6.3)
    charts.style_axes(ax, "mean of normalized counts", "log2 fold change")
    charts.title(ax, ttl)

ax = axs[2]
y = np.minimum(mlp, 60)
hit = has & (mlp > -np.log10(0.05)) & (np.abs(shr) > 1)
ax.scatter(shr[has & ~hit], y[has & ~hit], s=1.5, color=P.fill("neutral"), lw=0, rasterized=True)
ax.scatter(shr[hit & (shr > 0)], y[hit & (shr > 0)], s=2.5, color=charts.line("rna"), lw=0, rasterized=True)
ax.scatter(shr[hit & (shr < 0)], y[hit & (shr < 0)], s=2.5, color=charts.line("dna"), lw=0, rasterized=True)
ax.axhline(-np.log10(0.05), color=P.muted(), lw=0.7, ls="--")
ax.axvline(1, color=P.muted(), lw=0.7, ls="--")
ax.axvline(-1, color=P.muted(), lw=0.7, ls="--")
ax.text(0.03, 0.92, f"down {np.sum(hit & (shr < 0))}", transform=ax.transAxes, fontsize=7.5, color=charts.line("dna"))
ax.text(0.97, 0.92, f"up {np.sum(hit & (shr > 0))}", transform=ax.transAxes, fontsize=7.5, color=charts.line("rna"), ha="right")
ax.set_xlim(-6, 6)
charts.style_axes(ax, "shrunken log2 fold change", "-log10 adjusted p (capped at 60)")
charts.title(ax, "C  Volcano plot")

h = np.loadtxt("airway_pvalue_hist.csv", delimiter=",", comments="#", skiprows=2)
ax = axs[3]
ax.bar(h[:, 0], h[:, 2], width=0.025, align="edge", color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.4)
pi0_height = h[h[:, 0] >= 0.5, 2].mean()
ax.axhline(pi0_height, color=charts.line("dna"), lw=1, ls="--")
pi0 = pi0_height * 40 / h[:, 2].sum()
ax.text(0.35, 0.9, f"estimated share of null genes\npi0 = {pi0:.2f}", transform=ax.transAxes, fontsize=7.5, color=P.ink())
charts.style_axes(ax, "raw p-value", "number of genes")
charts.title(ax, "D  p-value histogram")
