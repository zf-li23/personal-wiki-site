"""Pseudoreplication (simulation). Two groups of 3 mice, 10 cells measured per mouse; no true group difference;
cells of the same mouse share a mouse effect, the intraclass correlation (ICC) being the fraction of the
variance between mice. A: one simulated data set (ICC 0.3): cells cluster by mouse. B: type I error rate
(20 000 simulated experiments per ICC, nominal 0.05) of a t test that treats the 30 cells per group as
independent, and of a t test on the 3 mouse means per group.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)


def sim(icc, R):
    a = rng.normal(0, np.sqrt(icc), (R, 2, 3, 1)) + rng.normal(0, np.sqrt(1 - icc), (R, 2, 3, 10))
    cells = a.reshape(R, 2, 30)
    t1 = stats.ttest_ind(cells[:, 0], cells[:, 1], axis=1).pvalue
    mice = a.mean(3)
    t2 = stats.ttest_ind(mice[:, 0], mice[:, 1], axis=1).pvalue
    return (t1 < 0.05).mean(), (t2 < 0.05).mean(), a


fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5), gridspec_kw=dict(width_ratios=[1, 1.15]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.28)
_, _, a = sim(0.3, 1)
ax = axs[0]
for gi, tok in ((0, "dna"), (1, "rna")):
    for mi in range(3):
        xs = gi * 4 + mi + rng.uniform(-0.15, 0.15, 10)
        ax.scatter(xs, a[0, gi, mi], s=12, color=P.fill(tok), edgecolor=charts.line(tok), lw=0.6)
        ax.plot([gi * 4 + mi - 0.3, gi * 4 + mi + 0.3], [a[0, gi, mi].mean()] * 2, color=P.ink(), lw=1.6)
ax.set_xticks([0, 1, 2, 4, 5, 6])
ax.set_xticklabels(["m1", "m2", "m3", "m4", "m5", "m6"], fontsize=FT["tiny"])
ax.text(1, ax.get_ylim()[1], "control", fontsize=FT["tiny"], color=P.ink(), ha="center", va="top")
ax.text(5, ax.get_ylim()[1], "treated", fontsize=FT["tiny"], color=P.ink(), ha="center", va="top")
charts.style_axes(ax, "mouse", "measurement (cells)")
charts.title(ax, "A  10 cells from each of 6 mice")
ax = axs[1]
iccs = np.array([0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5])
res = np.array([sim(i, 20000)[:2] for i in iccs])
ax.plot(iccs, res[:, 0], color=charts.line("rna"), lw=1.6, marker="o", ms=4, label="cells as units (n = 30 + 30)")
ax.plot(iccs, res[:, 1], color=charts.line("dna"), lw=1.6, marker="s", ms=4, label="mouse means (n = 3 + 3)")
ax.axhline(0.05, color=P.muted(), lw=0.8, ls=":")
ax.set_ylim(0, 0.5)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "intraclass correlation", "type I error rate")
charts.title(ax, "B  False positives without a true effect")
