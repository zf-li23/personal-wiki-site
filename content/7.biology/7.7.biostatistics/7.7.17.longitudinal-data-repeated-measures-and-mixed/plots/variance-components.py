"""Between-unit and within-unit variation: one-way random-effects ANOVA.

A: plasma estradiol measured twice (split blood samples, blinded) in 5 postmenopausal women, Nurses' Health
Study reproducibility substudy (published table in Rosner, Fundamentals of Biostatistics); ln scale.
B: optical density of the DNase ELISA at 0.78 ng/mL in 11 independent runs, 2 wells per run
(Davidian and Giltinan 1995; R data set DNase). C: for each of the 8 concentrations of the DNase standard,
the between-run and within-run standard deviations as coefficients of variation (percent of the mean)
and the intraclass correlation (right axis), all from the random-effects ANOVA mean squares.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def oneway(y):
    k, n = y.shape
    bms = n * ((y.mean(1) - y.mean()) ** 2).sum() / (k - 1)
    wms = ((y - y.mean(1, keepdims=True)) ** 2).sum() / (k * (n - 1))
    sa2 = max((bms - wms) / n, 0.0)
    return sa2, wms, sa2 / (sa2 + wms)


estr = np.array([[25.5, 30.4], [11.1, 15.0], [8.0, 8.1], [20.7, 16.9], [5.8, 8.4]])
rows = list(csv.DictReader(open("dnase.csv")))
run = np.array([int(r["run"]) for r in rows])
conc = np.array([float(r["conc"]) for r in rows])
od = np.array([float(r["density"]) for r in rows])
concs = np.unique(conc)


def table(c):
    m = np.isclose(conc, c)
    return np.array([od[m & (run == r)] for r in range(1, 12)])


fig, axs = plt.subplots(1, 3, figsize=(11, 3.5), gridspec_kw=dict(width_ratios=[0.8, 1.2, 1.3]))
fig.subplots_adjust(left=0.06, right=0.94, bottom=0.17, top=0.86, wspace=0.38)
ax = axs[0]
ly = np.log(estr)
sa2, s2, icc = oneway(ly)
for i in range(5):
    ax.plot([i + 1] * 2, ly[i], "o", ms=5, color=charts.line("dna"))
    ax.plot([i + 0.7, i + 1.3], [ly[i].mean()] * 2, color=charts.line("dna"), lw=1)
ax.axhline(ly.mean(), color=P.muted(), lw=0.7, ls="--")
ax.text(2.9, 3.55, f"between SD {np.sqrt(sa2):.3f}\nwithin SD {np.sqrt(s2):.3f}\nICC {icc:.2f}",
        fontsize=FT["tiny"], color=P.ink(), va="top")
ax.set_xticks(range(1, 6))
ax.set_xlim(0.4, 5.6)
ax.set_ylim(1.5, 3.6)
charts.style_axes(ax, "woman", "ln estradiol (pg/mL)")
charts.title(ax, "A  Estradiol, 2 aliquots")
ax = axs[1]
c0 = concs[3]
y0 = table(c0)
sa2, s2, icc = oneway(y0)
order = np.argsort(y0.mean(1))
for j, r in enumerate(order):
    ax.plot([j + 1] * 2, y0[r], "o", ms=4, color=charts.line("enzyme"))
    ax.plot([j + 0.7, j + 1.3], [y0[r].mean()] * 2, color=charts.line("enzyme"), lw=1)
ax.set_xticks(range(1, 12))
ax.set_xticklabels([str(r + 1) for r in order], fontsize=FT["tiny"])
ax.text(0.8, y0.max() + 0.002, f"between-run SD {np.sqrt(sa2):.4f}\nwithin-run SD {np.sqrt(s2):.4f}\nICC {icc:.2f}",
        fontsize=FT["tiny"], color=P.ink(), va="top")
charts.style_axes(ax, "run (ordered by mean)", f"optical density at {c0:.2f} ng/mL")
charts.title(ax, "B  DNase ELISA, 11 runs x 2 wells")
ax = axs[2]
cvb, cvw, iccs = [], [], []
for c in concs:
    t = table(c)
    a, w, i = oneway(t)
    cvb.append(100 * np.sqrt(a) / t.mean())
    cvw.append(100 * np.sqrt(w) / t.mean())
    iccs.append(i)
ax.plot(concs, cvb, "-o", ms=4, color=charts.line("rna"), label="between-run CV")
ax.plot(concs, cvw, "-s", ms=4, color=charts.line("dna"), label="within-run CV")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1, 80)
ax2 = ax.twinx()
ax2.plot(concs, iccs, ":^", ms=4, color=charts.line("plant"), label="ICC")
ax2.set_ylim(0, 1.05)
charts.style_axes(ax2, None, "ICC", box=True)
ax2.tick_params(labelcolor=charts.line("plant"))
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "DNase / (ng/mL)", "coefficient of variation / %")
charts.title(ax, "C  Variance components by concentration")
