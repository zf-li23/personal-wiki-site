"""Simulated type I error rates (20 000 replicates per setting, nominal alpha = 0.05, two-sided). A: pooled
and Welch two-sample t tests for normal data with equal means; settings are (n1, n2, SD1 : SD2). The pooled
test is badly off when the smaller group has the larger variance (or the reverse); Welch stays near 0.05.
B: the F test and the Levene test of equal variances (n = 25 per group, equal variances) for normal,
t with 4 df, log-normal and exponential data: the F test rejects far too often once the data are not normal.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
R = 20000
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.5))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.2, top=0.87, wspace=0.25)

cfgs = [(10, 10, 1, 1), (10, 10, 1, 3), (20, 10, 1, 3), (10, 20, 1, 3), (40, 10, 1, 1)]
pooled, welch = [], []
for n1, n2, s1, s2 in cfgs:
    x = rng.normal(0, s1, (R, n1))
    y = rng.normal(0, s2, (R, n2))
    pooled.append((stats.ttest_ind(x, y, axis=1).pvalue < 0.05).mean())
    welch.append((stats.ttest_ind(x, y, axis=1, equal_var=False).pvalue < 0.05).mean())
ax = axs[0]
pos = np.arange(len(cfgs))
ax.bar(pos - 0.2, pooled, 0.38, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, label="pooled t")
ax.bar(pos + 0.2, welch, 0.38, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.8, label="Welch t")
ax.axhline(0.05, color=P.ink(), lw=0.8, ls="--")
for i, v in enumerate(pooled):
    ax.text(i - 0.2, v + 0.003, f"{v:.3f}", fontsize=FT["tiny"] - 1, color=P.ink(), ha="center")
ax.set_xticks(pos)
ax.set_xticklabels([f"{a}, {b}\n{c}:{d}" for a, b, c, d in cfgs], fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "n1, n2 and SD1 : SD2", "type I error rate")
charts.title(ax, "A  Equal means: pooled vs Welch")

n = 25
gens = [("normal", lambda s: rng.normal(size=s)), ("t, 4 df", lambda s: rng.standard_t(4, size=s)),
        ("log-normal", lambda s: rng.lognormal(0, 0.6, size=s)), ("exponential", lambda s: rng.exponential(size=s))]
fr, lr = [], []
for _, g in gens:
    x, y = g((R, n)), g((R, n))
    F = x.var(axis=1, ddof=1) / y.var(axis=1, ddof=1)
    p = 2 * np.minimum(stats.f.sf(F, n - 1, n - 1), stats.f.cdf(F, n - 1, n - 1))
    fr.append((p < 0.05).mean())
    # Levene (Brown-Forsythe, median-centred) = one-way ANOVA on absolute deviations from the median
    zx = np.abs(x - np.median(x, axis=1, keepdims=True))
    zy = np.abs(y - np.median(y, axis=1, keepdims=True))
    lr.append((stats.ttest_ind(zx, zy, axis=1).pvalue < 0.05).mean())
ax = axs[1]
pos = np.arange(len(gens))
ax.bar(pos - 0.2, fr, 0.38, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8, label="F test")
ax.bar(pos + 0.2, lr, 0.38, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, label="Levene test")
ax.axhline(0.05, color=P.ink(), lw=0.8, ls="--")
for i, v in enumerate(fr):
    ax.text(i - 0.2, v + 0.005, f"{v:.2f}", fontsize=FT["tiny"] - 1, color=P.ink(), ha="center")
ax.set_xticks(pos)
ax.set_xticklabels([g[0] for g in gens], fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "distribution of the data (equal variances)", "type I error rate")
charts.title(ax, "B  Tests of equal variance")
