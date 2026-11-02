"""Bonferroni and Benjamini-Hochberg in practice. A: the 18899 airway p-values (Wald tests of
dexamethasone, pydeseq2 model ~ cell + dex; Himes et al. 2014, Bioconductor airway) sorted, the
smallest 8000 shown against their rank; the BH line alpha i/m with alpha = 0.1 crosses the sorted
p-values at rank 4691, the Bonferroni threshold alpha/m with alpha = 0.05 at rank 1413. B: simulation
(seed 0): 500 replicates of 1000 tests, 100 of them non-null with z ~ N(3, 1); for four rules, the
false discovery proportion among the rejections (box plots) and the proportion of non-null tests
rejected (power, points with values).
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("airway_wald.csv") as fh:
    zz = np.array([float(r["z"]) for r in csv.DictReader(line for line in fh if not line.startswith("#"))])
p = np.sort(2 * stats.norm.sf(np.abs(zz)))
m = p.size
i = np.arange(1, m + 1)
k_bh = np.max(np.where(p <= 0.1 * i / m)[0]) + 1
k_bf = np.sum(p <= 0.05 / m)
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.7), gridspec_kw={"width_ratios": [1.1, 1]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.28)
ax = axs[0]
sh = slice(0, m)
ax.plot(i[sh], np.maximum(p[sh], 1e-300), color=charts.line("rna"), lw=1.4, label="sorted p-values")
ax.plot(i[sh], 0.1 * i[sh] / m, color=charts.line("dna"), lw=1.1, ls="--", label=r"BH line $0.1\,i/m$")
ax.axhline(0.05 / m, color=charts.line("enzyme"), lw=1.1, ls=":", label=r"Bonferroni $0.05/m$")
ax.axvline(k_bh, color=P.muted(), lw=0.7)
ax.axvline(k_bf, color=P.muted(), lw=0.7)
ax.text(k_bh * 1.04, 1e-8, f"BH: {k_bh}", fontsize=FT["tiny"], color=P.ink())
ax.text(k_bf * 1.04, 3e-8, f"Bonferroni: {k_bf}", fontsize=FT["tiny"], color=P.ink())
ax.set_yscale("log")
ax.set_xscale("log")
ax.set_ylim(1e-9, 1.5)
ax.set_xlim(300, m * 1.1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "rank i", "p-value")
charts.title(ax, "A  airway: where the rules cut")

rng = np.random.default_rng(0)
R, M, M1 = 500, 1000, 100
rules = ["none 0.05", "Bonferroni 0.05", "Holm 0.05", "BH 0.10"]
fdp = {r: [] for r in rules}
pw = {r: [] for r in rules}
for _ in range(R):
    z = rng.normal(size=M)
    z[:M1] += 3
    pv = 2 * stats.norm.sf(np.abs(z))
    o = np.argsort(pv)
    ps = pv[o]
    j = np.arange(1, M + 1)
    rej = {}
    rej["none 0.05"] = pv < 0.05
    rej["Bonferroni 0.05"] = pv < 0.05 / M
    h = np.zeros(M, bool)
    fail = np.where(ps > 0.05 / (M - j + 1))[0]
    h[o[: fail[0] if fail.size else M]] = True
    rej["Holm 0.05"] = h
    b = np.zeros(M, bool)
    ok = np.where(ps <= 0.1 * j / M)[0]
    if ok.size:
        b[o[: ok.max() + 1]] = True
    rej["BH 0.10"] = b
    for r in rules:
        n = rej[r].sum()
        fdp[r].append(rej[r][M1:].sum() / max(n, 1))
        pw[r].append(rej[r][:M1].mean())
ax = axs[1]
bp = ax.boxplot([fdp[r] for r in rules], positions=range(4), widths=0.5, patch_artist=True, showfliers=False)
for bx in bp["boxes"]:
    bx.set(facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"))
for kk in ("whiskers", "caps", "medians"):
    for l in bp[kk]:
        l.set_color(P.ink())
for x, r in enumerate(rules):
    ax.plot(x, np.mean(fdp[r]), "D", color=charts.line("rna"), ms=4)
    ax.plot(x, np.mean(pw[r]), "o", color=charts.line("enzyme"), ms=5)
    ax.text(x + 0.12, np.mean(pw[r]), f"{np.mean(pw[r]):.2f}", fontsize=FT["tiny"], color=P.ink(), va="center")
    ax.text(x + 0.12, np.mean(fdp[r]) + 0.03, f"{np.mean(fdp[r]):.3f}", fontsize=FT["tiny"], color=charts.line("rna"))
ax.plot([], [], "D", color=charts.line("rna"), ms=4, label="mean FDP (= FDR)")
ax.plot([], [], "o", color=charts.line("enzyme"), ms=5, label="power")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
ax.set_xticks(range(4))
ax.set_xticklabels(rules, fontsize=FT["tiny"])
ax.set_ylim(-0.02, 1.0)
charts.style_axes(ax, None, "proportion")
charts.title(ax, "B  Simulation: 1000 tests, 100 non-null")
