"""Type I error, type II error and power for a one-sided z test of mean birth weight in a low-income
population: H0 mu = 120 oz against H1 mu < 120 oz, sigma = 24 oz, alpha = 0.05. Curves: sampling
distributions of the sample mean under H0 (mu = 120) and under the alternative mu = 115. A: n = 100,
standard error 2.4 oz, H0 rejected when the mean is below 116.05 oz; the power is 0.67. B: n = 10,
standard error 7.6 oz; the same alternative is detected with probability only 0.16. Exact normal
calculations.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
mu0, mu1, sigma, alpha = 120.0, 115.0, 24.0, 0.05

fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.4))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.16, top=0.87, wspace=0.18)
for ax, n, name in [(axs[0], 100, "A  n = 100"), (axs[1], 10, "B  n = 10")]:
    se = sigma / np.sqrt(n)
    crit = mu0 - stats.norm.isf(alpha) * se
    x = np.linspace(mu1 - 4 * se, mu0 + 4 * se, 600)
    f0, f1 = stats.norm.pdf(x, mu0, se), stats.norm.pdf(x, mu1, se)
    ax.plot(x, f0, color=charts.line("dna"), lw=1.7, label="under H0: mu = 120")
    ax.plot(x, f1, color=charts.line("rna"), lw=1.7, label="under H1: mu = 115")
    ax.fill_between(x[x <= crit], f0[x <= crit], color=P.fill("dna"), alpha=0.8, lw=0, label=f"alpha = {alpha}")
    ax.fill_between(x[x > crit], f1[x > crit], color=P.fill("rna"), alpha=0.45, lw=0,
                    label=f"beta = {stats.norm.sf(crit, mu1, se):.2f}")
    ax.axvline(crit, color=P.ink(), lw=0.9, ls="--")
    power = stats.norm.cdf(crit, mu1, se)
    ax.text(0.02, 0.95, f"SE = {se:.2f} oz\nreject H0 if mean < {crit:.2f}\npower = {power:.2f}", transform=ax.transAxes,
            va="top", fontsize=FT["tiny"], color=P.ink())
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
    ax.set_yticks([])
    charts.style_axes(ax, "sample mean birth weight (oz)", "density" if ax is axs[0] else None)
    charts.title(ax, name)
