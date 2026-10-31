# A biophysical fitness landscape: fitness from folding stability.
# A: fraction folded f = 1/(1 + exp(dG/RT)) against the folding free energy dG (RT = 0.6 kcal/mol):
# a sigmoid, flat for stable proteins and steep at the threshold dG = 0.
# B: threshold robustness. Lineages of a protein accumulate random mutations with destabilizing effects
# ddG drawn from a normal distribution (mean +1.0, standard deviation 1.7 kcal/mol, the order of measured
# distributions); fraction of 5000 lineages still folded (dG < 0) after n mutations for proteins starting
# at dG = -3 and -8 kcal/mol: stability buffers mutations, and the same mutation is neutral in one
# background and lethal in another (epistasis through stability).
# C: stationary distribution of stability under mutation and selection (Sella-Hirsh, weak mutation):
# P(dG) proportional to the number of sequences with that stability times fitness^(N-1), for a protein of
# 100 sites, each either optimal or one of 19 suboptimal residues costing 1 kcal/mol, dG = -40 + k.
# The sequence entropy pushes towards instability, selection towards stability, and proteins end up
# marginally stable, more so in small populations.
import math

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
RT = 0.6
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
dG = np.linspace(-12, 4, 300)
axs[0].plot(dG, 1 / (1 + np.exp(dG / RT)), color=charts.line("protein"), lw=2.0)
axs[0].axvline(0, color=P.muted(), lw=0.6)
charts.style_axes(axs[0], "folding free energy $\\Delta G$ / kcal mol$^{-1}$", "fraction folded (fitness)")
charts.title(axs[0], "A   Fitness is a sigmoid of stability")

ax = axs[1]
n = np.arange(0, 21)
for g0, tok in ((-3.0, "negative"), (-8.0, "dna")):
    walk = g0 + np.cumsum(np.c_[np.zeros(5000), rng.normal(1.0, 1.7, (5000, 20))], axis=1)
    alive = np.cumprod(walk < 0, axis=1).mean(0)
    ax.plot(n, alive, "o-", ms=3.5, lw=1.6, color=charts.line(tok), label=f"start $\\Delta G$ = {g0:g} kcal/mol")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "random mutations accumulated", "fraction of lineages still folded")
charts.title(ax, "B   Stability buffers mutations")

ax = axs[2]
Ls = 100
k = np.arange(Ls + 1)
G = -40.0 + k
lnOmega = np.array([math.lgamma(Ls + 1) - math.lgamma(i + 1) - math.lgamma(Ls - i + 1) for i in k]) + k * np.log(19)
lnf = -np.log1p(np.exp(G / RT))
for N, tok in ((10, "rna"), (1e3, "enzyme"), (1e5, "dna")):
    lp = lnOmega + (N - 1) * lnf
    p = np.exp(lp - lp.max()); p /= p.sum()
    ax.plot(G, p, color=charts.line(tok), lw=1.8, label=f"$N$ = {N:g}")
ax.axvline(0, color=P.muted(), lw=0.6)
ax.set_xlim(-25, 5)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "$\\Delta G$ / kcal mol$^{-1}$", "stationary probability")
charts.title(ax, "C   Evolution makes proteins marginally stable")
fig.tight_layout()
