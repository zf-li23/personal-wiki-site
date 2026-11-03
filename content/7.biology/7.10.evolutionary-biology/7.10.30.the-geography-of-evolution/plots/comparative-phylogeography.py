"""Comparative phylogeography (Section 30.5). For four codistributed species, an eastern and a western
population separated T generations ago (time measured in units of 2N generations, N the size of each
population); a gene copy sampled in the east and one in the west can coalesce only in the ancestral
population, so their divergence time is T plus an exponential waiting time with mean 1 (the
coalescent, 7.10.7). Curves: the distribution of east-west divergence times across 2000 unlinked
loci in each species. A: all four species were split by the same event (T = 1.5): the distributions
coincide, a signature of shared vicariance. B: the species were split at different times
(T = 0.3, 1.0, 2.0, 3.5), as expected if each crossed or met the barrier independently."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
toks = ["dna", "rna", "plant", "animal"]
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.3), sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.08)
grid = np.linspace(0, 8, 300)
for ax, Ts, title in ((axes[0], [1.5] * 4, "A  One shared split"),
                      (axes[1], [0.3, 1.0, 2.0, 3.5], "B  Independent splits")):
    for k, (T, tok) in enumerate(zip(Ts, toks)):
        t = T + rng.exponential(1.0, 2000)
        h, edges = np.histogram(t, bins=np.linspace(0, 8, 41), density=True)
        mids = (edges[:-1] + edges[1:]) / 2
        ax.plot(mids, h + 0.0 * k, color=charts.line(tok), lw=1.6, label=f"species {k + 1}")
        ax.axvline(T, color=charts.line(tok), lw=0.8, ls=(0, (3, 2)))
    charts.style_axes(ax, "east–west divergence time (units of 2N generations)", "density" if ax is axes[0] else None)
    charts.title(ax, title)
axes[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
