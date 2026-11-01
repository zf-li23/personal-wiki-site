"""Exact one-sample tests. A: bladder cancer deaths in a cohort of rubber workers (Andjelkovic et al. 1976):
21 observed against 18.1 expected from general-population rates. Bars: Poisson(18.1) distribution; the
two-sided p-value doubles the upper tail at and above 21 (filled), p = 0.55, standardized mortality ratio
116 %. B: variance of the difference between two observers' blood-pressure readings with a new device,
s^2 = 8.178 from n = 10, against the standard device's variance 35: the statistic (n - 1) s^2 / 35 = 2.10
lies below the lower 2.5 % point 2.70 of chi-square with 9 degrees of freedom (rejection regions filled).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.4))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.2)

O, E = 21, 18.1
k = np.arange(0, 41)
pmf = stats.poisson.pmf(k, E)
tail = k >= O
axs[0].bar(k, pmf, width=0.8, color=[P.fill("rna") if t else P.fill("neutral") for t in tail],
           edgecolor=[P.edge("rna") if t else P.edge("neutral") for t in tail], lw=0.5)
axs[0].axvline(E, color=P.ink(), lw=0.8, ls="--")
p = min(1.0, 2 * stats.poisson.sf(O - 1, E))
axs[0].text(0.98, 0.95, f"expected E = {E}\nobserved O = {O}\nSMR = {100 * O / E:.0f} %\ntwo-sided p = {p:.2f}",
            transform=axs[0].transAxes, ha="right", va="top", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(axs[0], "bladder cancer deaths", "probability under H0")
charts.title(axs[0], "A  One-sample Poisson test")

df, s2, s20 = 9, 8.178, 35.0
x = np.linspace(0.01, 30, 500)
f = stats.chi2.pdf(x, df)
lo, hi = stats.chi2.ppf(0.025, df), stats.chi2.isf(0.025, df)
axs[1].plot(x, f, color=charts.line("dna"), lw=1.7)
axs[1].fill_between(x[x <= lo], f[x <= lo], color=P.fill("dna"), lw=0)
axs[1].fill_between(x[x >= hi], f[x >= hi], color=P.fill("dna"), lw=0)
X2 = df * s2 / s20
axs[1].axvline(X2, color=charts.line("rna"), lw=1.4)
axs[1].text(X2 + 0.4, 0.09, f"observed {X2:.2f}", fontsize=FT["tiny"], color=P.ink())
axs[1].text(hi - 1.0, 0.02, f"{hi:.2f}", fontsize=FT["tiny"], color=P.ink(), ha="right")
axs[1].text(lo - 0.2, 0.03, f"{lo:.2f}", fontsize=FT["tiny"], color=P.ink(), ha="right")
axs[1].text(0.98, 0.95, f"two-sided p = {2 * stats.chi2.cdf(X2, df):.3f}", transform=axs[1].transAxes,
            ha="right", va="top", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(axs[1], "(n - 1) s^2 / 35", "density")
charts.title(axs[1], "B  Chi-square test for a variance, df = 9")
