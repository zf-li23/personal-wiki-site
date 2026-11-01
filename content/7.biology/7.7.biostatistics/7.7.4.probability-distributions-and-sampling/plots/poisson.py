"""Poisson counts. A: Poisson distributions with means 1, 4 and 10 become more symmetric as the mean grows.
B: 200 simulated agar plates with a mean of 10 colonies per plate (counts drawn from a Poisson
distribution) against the Poisson expectation. C: 200 simulated plates with the same mean but extra
plate-to-plate variation (negative binomial, variance 30): the counts are overdispersed and the Poisson
expectation is too narrow. Simulated data, random seed 0.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)

fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.3))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.86, wspace=0.28)

k = np.arange(0, 23)
for mu, tok, mk in [(1, "dna", "o"), (4, "rna", "s"), (10, "enzyme", "^")]:
    axs[0].plot(k, stats.poisson.pmf(k, mu), color=charts.line(tok), marker=mk, ms=3.5, lw=1.0, label=f"mean {mu}")
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(axs[0], "count k", "P(X = k)")
charts.title(axs[0], "A  Poisson distributions")

n_plates = 200
mean = 10.0
size = 5.0                                    # NB dispersion: variance = mean + mean^2 / size = 30
pois = rng.poisson(mean, n_plates)
nb = rng.negative_binomial(size, size / (size + mean), n_plates)
for ax, data, tok, name in [(axs[1], pois, "dna", "B  Poisson plates"), (axs[2], nb, "rna", "C  Overdispersed plates")]:
    kk = np.arange(0, 36)
    obs = np.bincount(data, minlength=36)[:36]
    ax.bar(kk, obs, width=0.85, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, label="observed plates")
    ax.plot(kk, n_plates * stats.poisson.pmf(kk, data.mean()), color=charts.line("neutral"), marker="o", ms=2.5,
            lw=1.0, label="Poisson expectation")
    ax.text(0.97, 0.80, f"mean {data.mean():.1f}\nvariance {data.var(ddof=1):.1f}", transform=ax.transAxes,
            ha="right", fontsize=FT["tiny"], color=P.ink())
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
    ax.set_ylim(0, 37)
    charts.style_axes(ax, "colonies per plate", "number of plates" if ax is axs[1] else None)
    charts.title(ax, name)
