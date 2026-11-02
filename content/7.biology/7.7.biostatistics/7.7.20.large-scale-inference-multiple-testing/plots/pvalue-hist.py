"""Histograms of p-values from many tests. A: 10000 tests in which every null hypothesis is true
(simulation, z ~ N(0, 1), seed 0): the p-values are uniform. B: 10000 tests of which 10% have an effect
(z ~ N(3, 1) for the non-null tests): a flat floor from the null tests plus a peak near 0. C: the Wald
tests of dexamethasone against untreated for the 18899 airway genes kept by independent filtering
(Himes et al. 2014, GEO GSE52778; Bioconductor airway; DESeq2 model ~ cell + dex fitted with pydeseq2);
dashed line: the floor of null genes estimated with Storey's lambda = 0.5, pi0 = 0.65.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
m = 10000
pA = 2 * stats.norm.sf(np.abs(rng.normal(size=m)))
z = rng.normal(size=m)
z[: m // 10] += 3
pB = 2 * stats.norm.sf(np.abs(z))
with open("airway_wald.csv") as fh:
    zz = np.array([float(r["z"]) for r in csv.DictReader(line for line in fh if not line.startswith("#"))])
pC = 2 * stats.norm.sf(np.abs(zz))
bins = np.linspace(0, 1, 41)
fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.3))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
for ax, p, name, tok in ((axs[0], pA, "A  all nulls true", "neutral"), (axs[1], pB, "B  10% non-null", "enzyme"),
                         (axs[2], pC, "C  airway, 18899 genes", "rna")):
    ax.hist(p, bins=bins, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.5)
    pi0 = min(1, np.mean(p > 0.5) / 0.5)
    floor = pi0 * len(p) / 40
    ax.axhline(floor, color=P.ink(), ls="--", lw=0.9)
    ax.text(0.98, floor * 1.12 if ax is not axs[2] else floor * 1.6, f"$\\hat\\pi_0$ = {pi0:.2f}", ha="right",
            fontsize=FT["tiny"], color=P.ink(), transform=ax.get_yaxis_transform())
    charts.style_axes(ax, "p-value", "number of tests" if ax is axs[0] else None)
    charts.title(ax, name)
axs[2].set_ylim(0, 1400)
axs[2].text(0.08, 1330, f"first bin: {np.sum(pC < 0.025)}", fontsize=FT["tiny"], color=P.ink(), va="top")
