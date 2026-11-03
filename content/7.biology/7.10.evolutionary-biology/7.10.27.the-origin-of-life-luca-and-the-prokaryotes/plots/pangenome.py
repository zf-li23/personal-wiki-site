"""Pangenome accumulation in a simple model: 60 genomes, 2500 core genes, accessory genes drawn from a
pool with a neutral (1/frequency) frequency spectrum; core and pan genome against the number of genomes."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
G, CORE, POOL = 60, 2500, 6000
# accessory gene frequencies from the neutral infinitely-many-genes spectrum ~ 1/f on [1/G, 1)
u = rng.random(POOL)
f = (1 / G) ** (1 - u)                  # log-uniform: density proportional to 1/f
presence = rng.random((G, POOL)) < f[None, :]
presence = presence[:, presence.any(axis=0)]
orders = 50
core = np.zeros((orders, G))
pan = np.zeros((orders, G))
for o in range(orders):
    idx = rng.permutation(G)
    cum_any = np.zeros(presence.shape[1], bool)
    cum_all = np.ones(presence.shape[1], bool)
    for k, g in enumerate(idx):
        cum_any |= presence[g]
        cum_all &= presence[g]
        pan[o, k] = CORE + cum_any.sum()
        core[o, k] = CORE + cum_all.sum()
n = np.arange(1, G + 1)
fig, ax = bio.canvas(14, 9)
pax = charts.axes_at(ax, (2.2, 1.6, 10.8, 6.8))
for arr, tok, lab in ((pan, "rna", "pangenome"), (core, "dna", "core genome")):
    pax.fill_between(n, arr.min(0), arr.max(0), color=P.light(tok), lw=0)
    pax.plot(n, arr.mean(0), color=charts.line(tok), lw=1.8, label=lab)
pax.axhline(CORE, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pax.text(G, CORE - 150, "true core (2500 genes)", fontsize=FT["tiny"], color=P.muted(), ha="right", va="top")
pax.set_xlim(1, G)
pax.set_ylim(0, None)
charts.style_axes(pax, "number of genomes sampled", "number of genes")
pax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
