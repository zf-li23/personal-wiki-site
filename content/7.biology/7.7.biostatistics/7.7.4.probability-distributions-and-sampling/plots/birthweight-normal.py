"""Birth weight and the normal distribution (birthwt data, 189 births at Baystate Medical Center, 1986;
Hosmer and Lemeshow; R package MASS). A: histogram of birth weight with the fitted normal density
N(2945, 729^2); the shaded area below 2500 g is the normal estimate of the proportion of low birth weight.
B: the same comparison by maternal smoking. The normal curve describes the centre well but underestimates
the lower tail, where the observed proportions are higher.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rows = list(csv.DictReader(open("birthwt.csv")))
bwt = np.array([float(r["bwt"]) for r in rows])
smoke = np.array([int(r["smoke"]) for r in rows])

fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.5))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.22)
x = np.linspace(500, 5500, 500)

ax = axs[0]
mu, sd = bwt.mean(), bwt.std(ddof=1)
ax.hist(bwt, bins=np.arange(500, 5250, 250), density=True, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5)
ax.plot(x, stats.norm.pdf(x, mu, sd), color=charts.line("enzyme"), lw=1.7)
xs = x[x <= 2500]
ax.fill_between(xs, stats.norm.pdf(xs, mu, sd), color=P.fill("rna"), alpha=0.55, lw=0)
ax.axvline(2500, color=P.muted(), lw=0.8, ls="--")
ax.text(0.02, 0.97, f"below 2500 g\nobserved {np.mean(bwt < 2500):.3f}\nnormal {stats.norm.cdf(2500, mu, sd):.3f}",
        transform=ax.transAxes, va="top", fontsize=FT["tiny"], color=P.ink())
ax.text(0.98, 0.97, f"mean {mu:.0f} g\nSD {sd:.0f} g", transform=ax.transAxes, va="top", ha="right",
        fontsize=FT["tiny"], color=P.ink())
ax.set_ylim(0, 7.2e-4)
ax.set_yticks([])
charts.style_axes(ax, "birth weight (g)", "density")
charts.title(ax, "A  All 189 births")

ax = axs[1]
for g, tok, name in [(0, "dna", "non-smokers"), (1, "rna", "smokers")]:
    b = bwt[smoke == g]
    m, s = b.mean(), b.std(ddof=1)
    ax.plot(x, stats.norm.pdf(x, m, s), color=charts.line(tok), lw=1.7,
            label=f"{name} (n {len(b)}): observed {np.mean(b < 2500):.3f}, normal {stats.norm.cdf(2500, m, s):.3f}")
    xs = x[x <= 2500]
    ax.fill_between(xs, stats.norm.pdf(xs, m, s), color=P.fill(tok), alpha=0.35, lw=0)
    ax.plot(b, np.full(len(b), -2.2e-5 if g == 0 else -5.5e-5), "|", color=charts.line(tok), ms=5, mew=0.6)
ax.axvline(2500, color=P.muted(), lw=0.8, ls="--")
leg = ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right",
                title="proportion below 2500 g", title_fontsize=FT["tiny"])
leg.get_title().set_color(P.ink())
ax.set_yticks([])
ax.set_ylim(-8e-5, 7.4e-4)
charts.style_axes(ax, "birth weight (g)", None)
charts.title(ax, "B  By maternal smoking (ticks: individual births)")
