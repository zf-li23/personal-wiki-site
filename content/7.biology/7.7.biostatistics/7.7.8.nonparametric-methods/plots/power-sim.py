"""Power of the two-sample t test (pooled) and the Wilcoxon rank-sum test, two-sided alpha = 0.05, 20
observations per group, 4000 simulated data sets per point, as a function of the shift between the two
distributions. A: normal data; the t test is slightly better (asymptotic relative efficiency 0.955).
B: t distribution with 3 df (heavy tails). C: log-normal data (sigma = 1, strongly right-skewed). Under
heavy tails and skewness the rank test is clearly more powerful. Simulated data.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
n, R = 20, 4000
shifts = np.linspace(0, 1.2, 7)
gens = [("A  Normal", lambda s: rng.normal(size=s)), ("B  t, 3 df", lambda s: rng.standard_t(3, size=s)),
        ("C  Log-normal", lambda s: rng.lognormal(0, 1, size=s))]
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3), sharey=True)
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.17, top=0.87, wspace=0.12)
for ax, (name, g) in zip(axs, gens):
    pt, pw = [], []
    for sh in shifts:
        x, y = g((R, n)), g((R, n)) + sh
        pt.append((stats.ttest_ind(x, y, axis=1).pvalue < 0.05).mean())
        pw.append((stats.mannwhitneyu(x, y, axis=1).pvalue < 0.05).mean())
    ax.plot(shifts, pt, "o-", ms=3.5, color=charts.line("dna"), lw=1.5, label="t test")
    ax.plot(shifts, pw, "s-", ms=3.5, color=charts.line("rna"), lw=1.5, label="Wilcoxon rank-sum")
    ax.axhline(0.05, color=P.muted(), lw=0.7, ls=":")
    charts.style_axes(ax, "shift", "power" if ax is axs[0] else None)
    charts.title(ax, name)
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
axs[0].set_ylim(0, 1.02)
