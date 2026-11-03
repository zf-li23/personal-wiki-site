"""Site frequency spectrum and estimators of theta. 2000 coalescent samples of n = 20 sequences with
theta = 10 per locus (infinite sites: each branch of length T carries Poisson(theta T / 2) mutations, the
derived allele carried by the tips below the branch). A: mean unfolded spectrum (bars) and theta / i (line).
B: distributions of Watterson's estimator S / a_n and Tajima's mean pairwise difference theta_pi over the
2000 samples; vertical line: theta."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(9)
n, theta, R = 20, 10.0, 2000


def sample():
    sizes = [1] * n                 # number of tips below each active lineage
    xi = np.zeros(n)
    while len(sizes) > 1:
        k = len(sizes)
        t = rng.exponential(2 / (k * (k - 1)))
        for s in sizes:
            xi[s] += rng.poisson(theta * t / 2)
        i, j = sorted(rng.choice(k, 2, replace=False))
        sizes[i] += sizes[j]
        sizes.pop(j)
    return xi[1:n]


X = np.array([sample() for _ in range(R)])
i = np.arange(1, n)
an = np.sum(1 / i)
S = X.sum(1)
tw = S / an
tp = (X * i * (n - i)).sum(1) / (n * (n - 1) / 2)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.7))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.27)
a.bar(i, X.mean(0), color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5, label="simulated mean")
a.plot(i, theta / i, color=P.ink(), lw=1.4, marker="o", ms=3, label="$\\theta/i$")
a.set_xlim(0.3, n - 0.3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "derived allele count $i$ (of 20)", "sites $\\xi_i$")
charts.title(a, "A  Neutral site frequency spectrum")
bins = np.linspace(0, 35, 50)
b.hist(tw, bins=bins, density=True, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.4, alpha=0.85,
       label=f"$\\hat\\theta_W$ (SD {tw.std():.1f})")
b.hist(tp, bins=bins, density=True, histtype="step", color=charts.line("rna"), lw=1.6,
       label=f"$\\hat\\theta_\\pi$ (SD {tp.std():.1f})")
b.axvline(theta, color=P.ink(), lw=1)
b.set_xlim(0, 35)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "estimate of $\\theta$ (per locus)", "density")
charts.title(b, "B  Two estimators, one genealogy each")
