"""Aggregation of macroparasites among hosts (Section 28.1.3).

A: the distribution of worm burdens in a host population with mean burden 10: Poisson (random
infection) versus negative binomial with k = 0.5 (typical of helminths); with k = 0.5 about a quarter
of hosts carry no worms at all and a long tail of hosts carries most of them.
B: the cumulative fraction of all worms carried by the most heavily infected hosts (hosts ranked
by burden) for the Poisson and negative binomial distributions with k = 2, 0.5 and 0.2; the dotted
lines mark the "20/80" pattern: the most infected 20 % of hosts carry about two thirds of the
worms for k = 0.5 and about 85 % for k = 0.2.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
mean = 10.0
i = np.arange(0, 61)
pois = stats.poisson.pmf(i, mean)


def nb(k):
    return stats.nbinom(k, k / (k + mean))


fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3))
ax = axes[0]
ax.bar(i - 0.2, pois, width=0.4, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5, label="Poisson")
ax.bar(i + 0.2, nb(0.5).pmf(i), width=0.4, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.5,
       label="negative binomial, k = 0.5")
ax.set_xlim(-1, 50)
ax.text(1.5, nb(0.5).pmf(0) * 0.97, f"{nb(0.5).pmf(0):.0%} uninfected", fontsize=FS["tiny"], color=P.ink(), va="top")
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
C.style_axes(ax, "Worms per host", "Proportion of hosts")
C.title(ax, "A  Mean burden 10: random versus clumped")

ax = axes[1]
x = np.arange(0, 3000)
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.7, ls=(0, (2, 2)))
for dist, col, lab in [(stats.poisson(mean), C.line("neutral"), "Poisson"),
                       (nb(2.0), C.line("dna"), "k = 2"), (nb(0.5), C.line("negative"), "k = 0.5"),
                       (nb(0.2), C.line("highlight"), "k = 0.2")]:
    p = dist.pmf(x)[::-1]
    worms = (x[::-1] * p)
    hosts_c = np.concatenate([[0], np.cumsum(p)])
    worms_c = np.concatenate([[0], np.cumsum(worms) / mean])
    ax.plot(hosts_c, worms_c, color=col, lw=1.5, label=lab)
ax.axvline(0.2, color=P.muted(), lw=0.7, ls=(0, (1, 2)))
ax.axhline(0.8, color=P.muted(), lw=0.7, ls=(0, (1, 2)))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.02)
ax.legend(fontsize=FS["tiny"], frameon=False, loc="lower right")
C.style_axes(ax, "Fraction of hosts (most infected first)", "Fraction of all worms")
C.title(ax, "B  A few hosts carry most parasites")
fig.tight_layout()
