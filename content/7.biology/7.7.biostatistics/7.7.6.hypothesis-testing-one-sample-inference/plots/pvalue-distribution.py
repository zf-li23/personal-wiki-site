"""Distribution of p-values from 10 000 simulated one-sample t tests (n = 20, H0 mu = 0, two-sided).
A: H0 true: the p-values are uniform on (0, 1), so 5 % fall below 0.05. B: H1 true with a standardized
effect of 0.5: p-values pile up near 0, and the proportion below 0.05 is the power (about 0.56).
C: a mixture of 80 % true nulls and 20 % true effects, as among thousands of genes: a uniform floor
plus a spike near 0. Simulated data, random seed 0.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
n, reps = 20, 10000


def pvals(effect, m):
    x = rng.normal(effect, 1.0, size=(m, n))
    return stats.ttest_1samp(x, 0.0, axis=1).pvalue


p0 = pvals(0.0, reps)
p1 = pvals(0.5, reps)
mix = np.concatenate([pvals(0.0, 8000), pvals(0.5, 2000)])
fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.2))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.86, wspace=0.25)
bins = np.linspace(0, 1, 41)
for ax, p, tok, name in [(axs[0], p0, "dna", "A  H0 true"), (axs[1], p1, "rna", "B  H1 true, effect 0.5 SD"),
                         (axs[2], mix, "enzyme", "C  80 % H0 + 20 % H1")]:
    ax.hist(p, bins=bins, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.4)
    ax.axvline(0.05, color=P.ink(), lw=0.8, ls="--")
    ax.text(0.97, 0.92, f"P(p < 0.05) = {np.mean(p < 0.05):.3f}", transform=ax.transAxes, ha="right",
            fontsize=FT["tiny"], color=P.ink())
    charts.style_axes(ax, "p-value", "number of tests" if ax is axs[0] else None)
    charts.title(ax, name)
axs[0].axhline(reps / 40, color=P.muted(), lw=0.8, ls=":")
