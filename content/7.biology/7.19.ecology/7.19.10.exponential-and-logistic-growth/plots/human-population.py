"""Human population growth (Section 10.1.3).

A: the dates at which world population reached 1, 2, ..., 8 billion (United Nations Population Division
estimates: 1804, 1927, 1960, 1974, 1987, 1999, 2011, 2022), on a logarithmic axis; the right axis gives the
mean exponential growth rate between successive milestones, r = ln(N_{k+1}/N_k)/(t_{k+1} - t_k).
B: a model of the demographic transition (illustrative parameters): crude death and birth rates fall
logistically from 38 per 1000 per year to 10 and 11 per 1000, deaths centered on year 60 and births on
year 120 (width 18 years); the population follows dN/dt = (b(t) - d(t)) N from N = 1.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT

years = np.array([1804, 1927, 1960, 1974, 1987, 1999, 2011, 2022])
pop = np.arange(1, 9)

fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.9))
ax = axes[0]
ax.plot(years, pop, "o-", color=C.line("dna"), lw=1.8, ms=5)
for y, n in zip(years, pop):
    ax.text(y - 4, n * 1.06, str(y), fontsize=FS["tiny"], color=P.muted(), ha="right")
ax.set_yscale("log")
ax.set_yticks([1, 2, 4, 8], ["1", "2", "4", "8"])
ax.yaxis.set_minor_formatter(plt.NullFormatter())
ax.set_xlim(1790, 2035)
C.style_axes(ax, "year", "world population (billions, log scale)")
ax2 = ax.twinx()
mid = (years[1:] + years[:-1]) / 2
rate = np.log(pop[1:] / pop[:-1]) / np.diff(years) * 100
ax2.step(np.concatenate([years[:-1], [years[-1]]]), np.concatenate([rate, [rate[-1]]]), where="post",
         color=C.line("rna"), lw=1.4)
ax2.set_ylim(0, 2.6)
C.style_axes(ax2, None, "mean growth rate (% per year)")
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(P.muted())
ax2.yaxis.label.set_color(C.line("rna"))
ax2.text(1905, 2.3, "2.1% (1960–74)", fontsize=FS["tiny"], color=C.line("rna"))
ax2.text(1810, 0.68, "0.56% (1804–1927)", fontsize=FS["tiny"], color=C.line("rna"))
C.title(ax, "A  World population milestones")

ax = axes[1]
t = np.linspace(0, 200, 2001)
d = 10 + 28 / (1 + np.exp((t - 60) / 18))
b = 11 + 27 / (1 + np.exp((t - 120) / 18))
ax.plot(t, b, color=C.line("positive"), lw=2, label="birth rate")
ax.plot(t, d, color=C.line("negative"), lw=2, label="death rate")
ax.fill_between(t, d, b, where=b > d, color=P.fill("highlight"), alpha=0.5, lw=0)
C.style_axes(ax, "time (years)", "per 1000 per year")
ax.set_ylim(0, 45)
for x0, txt in ((5, "1"), (75, "2"), (140, "3"), (185, "4")):
    ax.text(x0, 42, f"stage {txt}", fontsize=FS["tiny"], color=P.muted())
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center left")
ax3 = ax.twinx()
N = np.exp(np.concatenate([[0], np.cumsum((b - d)[:-1] / 1000 * np.diff(t))]))
ax3.plot(t, N, color=C.line("dna"), lw=1.8, ls=(0, (4, 2)))
C.style_axes(ax3, None, "population (relative)")
ax3.spines["right"].set_visible(True)
ax3.spines["right"].set_color(P.muted())
ax3.yaxis.label.set_color(C.line("dna"))
ax3.set_ylim(0, N.max() * 1.15)
C.title(ax, "B  Demographic transition (model)")
fig.tight_layout()
