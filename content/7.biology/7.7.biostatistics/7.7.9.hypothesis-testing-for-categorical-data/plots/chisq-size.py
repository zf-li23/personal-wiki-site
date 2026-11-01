"""Actual type I error of three tests for a 2 x 2 table when the expected counts are small. Two groups of
equal size n, the same true proportion in both (A: p = 0.1; B: p = 0.3), two-sided nominal alpha = 0.05.
The rejection probability is computed exactly by summing over all pairs of binomial outcomes. The
uncorrected Pearson chi-square is close to 0.05 once the expected counts are moderate, sometimes above it
(0.059 at n = 40, p = 0.1); the Yates-corrected test and Fisher's exact test are conservative, with an
actual size often less than half the nominal level.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
ns = np.arange(8, 61, 4)


def size(n, p):
    k = np.arange(n + 1)
    a, c = np.meshgrid(k, k, indexing="ij")
    prob = stats.binom.pmf(a, n, p) * stats.binom.pmf(c, n, p)
    m = a + c
    N = 2 * n
    ok = (m > 0) & (m < N)
    num = np.abs(a * (n - c) - c * (n - a)).astype(float)
    den = np.where(ok, n * n * m * (N - m), 1.0)
    x2 = np.where(ok, N * num**2 / den, 0.0)
    y2 = np.where(ok, N * np.maximum(num - N / 2, 0) ** 2 / den, 0.0)
    pear = ok & (stats.chi2.sf(x2, 1) < 0.05)
    yates = ok & (stats.chi2.sf(y2, 1) < 0.05)
    fish = np.zeros_like(pear)
    for mm in range(1, N):
        sup = np.arange(max(0, mm - n), min(n, mm) + 1)
        pm = stats.hypergeom.pmf(sup, N, n, mm)
        pv = np.array([pm[pm <= q * (1 + 1e-7)].sum() for q in pm])
        for aa, pvv in zip(sup, pv):
            fish[aa, mm - aa] = pvv < 0.05
    return np.array([prob[pear].sum(), prob[yates].sum(), prob[fish].sum()])


fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.4), sharey=True)
fig.subplots_adjust(left=0.08, right=0.99, bottom=0.16, top=0.87, wspace=0.1)
for ax, p, lab in [(axs[0], 0.1, "A  True proportion 0.1"), (axs[1], 0.3, "B  True proportion 0.3")]:
    res = np.array([size(n, p) for n in ns])
    for j, (name, tok, mk) in enumerate([("Pearson", "rna", "o"), ("Yates", "dna", "s"), ("Fisher", "enzyme", "^")]):
        ax.plot(ns, res[:, j], marker=mk, ms=3.5, lw=1.4, color=charts.line(tok), label=name)
    ax.axhline(0.05, color=P.ink(), lw=0.8, ls="--")
    charts.style_axes(ax, "n per group", "actual type I error" if ax is axs[0] else None)
    charts.title(ax, lab)
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
axs[0].set_ylim(0, 0.1)
