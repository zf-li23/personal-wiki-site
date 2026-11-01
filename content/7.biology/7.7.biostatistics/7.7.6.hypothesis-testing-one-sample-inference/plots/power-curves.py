"""Power and sample size for tests of a normal mean. A: power of the one-sided z test of H0 mu = 120 oz
(sigma = 24 oz, alpha = 0.05) as a function of the true mean, for n = 10, 25 and 100; at mu = 120 every
curve equals alpha. B: sample size needed by a two-sided z test at alpha = 0.05 against the standardized
difference Delta / sigma, for 80 % and 90 % power (logarithmic axis). Exact normal calculations.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
mu0, sigma, alpha = 120.0, 24.0, 0.05
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.4))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.22)

mu1 = np.linspace(100, 122, 400)
for n, tok in [(10, "neutral"), (25, "dna"), (100, "rna")]:
    pw = stats.norm.cdf((mu0 - mu1) * np.sqrt(n) / sigma - stats.norm.isf(alpha))
    axs[0].plot(mu1, pw, color=charts.line(tok), lw=1.7, label=f"n = {n}")
    axs[0].plot(115, stats.norm.cdf(5 * np.sqrt(n) / sigma - stats.norm.isf(alpha)), "o", color=charts.line(tok), ms=4)
axs[0].axhline(alpha, color=P.muted(), lw=0.7, ls=":")
axs[0].axvline(115, color=P.muted(), lw=0.7, ls="--")
axs[0].text(115.3, 0.9, "true mean 115 oz", fontsize=FT["tiny"], color=P.ink())
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(axs[0], "true mean birth weight (oz)", "power")
charts.title(axs[0], "A  Power curves, one-sided alpha = 0.05")

es = np.linspace(0.1, 1.5, 400)
for pw, tok in [(0.8, "dna"), (0.9, "rna")]:
    n = (stats.norm.isf(0.025) + stats.norm.ppf(pw)) ** 2 / es ** 2
    axs[1].semilogy(es, n, color=charts.line(tok), lw=1.7, label=f"power {pw:.0%}")
for e in [0.2, 0.5, 0.8]:
    n80 = (stats.norm.isf(0.025) + stats.norm.ppf(0.8)) ** 2 / e ** 2
    axs[1].plot(e, n80, "o", color=charts.line("dna"), ms=4)
    axs[1].text(e + 0.03, n80 * 1.15, f"{np.ceil(n80):.0f}", fontsize=FT["tiny"], color=P.ink())
axs[1].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(axs[1], "standardized difference Delta / sigma", "sample size n")
charts.title(axs[1], "B  Sample size, two-sided alpha = 0.05")
