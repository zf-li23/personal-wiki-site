"""Genetic drift in the Wright-Fisher model (no selection, binomial sampling of 2N gene copies; seeds fixed).
A-C: 20 replicate populations of N = 10, 100 and 1000 diploids, all starting at p = 0.5, for 200 generations;
in small populations alleles are fixed or lost within tens of generations, in large ones frequencies barely
move. D: mean heterozygosity 2p(1 - p) over 2000 replicates (dots) against the prediction
H_t = H_0 (1 - 1/2N)^t (lines)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo
from wikibio import quant

P = bio.P
FT = bio.core.FONT
T = 200
fig, axs = plt.subplots(1, 4, figsize=(12.0, 3.4), gridspec_kw={"width_ratios": [1, 1, 1, 1.25]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.88, wspace=0.3)
g = np.arange(T + 1)
for k, (ax, N, seed) in enumerate(zip(axs[:3], (10, 100, 1000), (3, 4, 5))):
    tr = evo.wright_fisher(N, 0.0, 0.5, T, reps=20, rng=np.random.default_rng(seed))
    for j in range(tr.shape[1]):
        end = tr[-1, j]
        tok = "rna" if end == 1 else "dna" if end == 0 else "muted"
        ax.plot(g, tr[:, j], color=quant.line_color(tok), lw=0.9)
    ax.set_ylim(-0.02, 1.02)
    ax.set_xlim(0, T)
    charts.style_axes(ax, "generation", "allele frequency $p$" if k == 0 else None)
    fixed, lost = int((tr[-1] == 1).sum()), int((tr[-1] == 0).sum())
    charts.title(ax, f"{'ABC'[k]}  $N = {N}$")
    ax.text(T * 0.97, 0.03, f"fixed {fixed}, lost {lost}", ha="right", fontsize=FT["tiny"], color=P.muted())
d = axs[3]
for N, tok, seed in ((10, "negative", 6), (100, "enzyme", 7), (1000, "dna", 8)):
    tr = evo.wright_fisher(N, 0.0, 0.5, T, reps=2000, rng=np.random.default_rng(seed))
    H = (2 * tr * (1 - tr)).mean(1)
    d.scatter(g[::10], H[::10], s=10, color=charts.line(tok), zorder=3)
    d.plot(g, 0.5 * (1 - 1 / (2 * N)) ** g, color=charts.line(tok), lw=1.6, label=f"$N = {N}$")
d.set_xlim(0, T)
d.set_ylim(0, 0.52)
d.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(d, "generation", "mean heterozygosity")
charts.title(d, "D  $H_t = H_0(1 - 1/2N)^t$")
