"""The central limit theorem by simulation. Leftmost panel: a right-skewed population, a gamma distribution
with shape 1.5 and mean 6 days, as a model of length of hospital stay. Other panels: histograms of 10 000
sample means for samples of size n = 5, 10 and 30, with the normal density N(mu, sigma^2/n) predicted by
the theorem. The skewness of the mean, 2/sqrt(1.5 n), falls as 1/sqrt(n). Simulated data, random seed 0.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
shape, scale = 1.5, 4.0
pop = stats.gamma(shape, scale=scale)
mu, sigma = pop.mean(), pop.std()

fig, axs = plt.subplots(1, 4, figsize=(10.8, 2.9))
fig.subplots_adjust(left=0.05, right=0.995, bottom=0.19, top=0.85, wspace=0.25)
x = np.linspace(0, 30, 400)
axs[0].fill_between(x, pop.pdf(x), color=P.fill("neutral"), lw=0)
axs[0].plot(x, pop.pdf(x), color=charts.line("neutral"), lw=1.4)
axs[0].axvline(mu, color=P.muted(), lw=0.8, ls="--")
axs[0].text(mu + 0.6, pop.pdf(1.5) * 0.9, f"mean {mu:.0f}, SD {sigma:.1f}\nskewness {2 / np.sqrt(shape):.2f}",
            fontsize=FT["tiny"], color=P.ink())
axs[0].set_yticks([])
charts.style_axes(axs[0], "length of stay (days)", "density")
charts.title(axs[0], "Population")

for ax, n in zip(axs[1:], [5, 10, 30]):
    means = rng.gamma(shape, scale, size=(10000, n)).mean(axis=1)
    se = sigma / np.sqrt(n)
    ax.hist(means, bins=50, density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3)
    g = np.linspace(mu - 4 * se, mu + 4.5 * se, 300)
    ax.plot(g, stats.norm.pdf(g, mu, se), color=charts.line("rna"), lw=1.5)
    ax.text(0.97, 0.80, f"SE {se:.2f}\nskewness {2 / np.sqrt(shape * n):.2f}", transform=ax.transAxes, ha="right",
            fontsize=FT["tiny"], color=P.ink())
    ax.set_yticks([])
    charts.style_axes(ax, "sample mean (days)", None)
    charts.title(ax, f"Means, n = {n}")
