"""Long-term response to artificial (truncation) selection in individual-based simulations of a diploid
population: each generation the 50 highest-scoring of 250 individuals are the parents, loci are unlinked,
the environmental variance is V_E = 1 and the trait is the sum of allelic effects plus environmental noise.
Three genetic architectures (two replicate lines each, seeds 1 and 2):
A: 10 loci with favourable alleles of large effect (0.5) at initial frequency 0.1 (initial h^2 about 0.3);
B: 400 loci of small effect (0.03) at frequency 0.5 plus two major loci (effect 0.5, frequency 0.1);
C: 100 loci of effect 0.1 at frequency 0.3 with mutation (each allele mutates with probability 0.001 per
generation, adding a normal effect of variance 0.0115, so that the mutational variance is V_M = 0.0023).
Top: change of the mean phenotype; bottom: additive genetic variance V_A among the 250 individuals. With
few major loci the variance first rises (favourable alleles reach intermediate frequency) and the response
stops when they fix, within about 15 generations; with many loci of small effect the response continues
for the whole run while the variance declines gradually (selection, the small number of parents and
linkage disequilibrium); with mutation the response is sustained at a higher rate."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
N, NSEL, T = 250, 50, 60


def simulate(effects, freqs, seed, mu=0.0, sm2=0.0):
    rng = np.random.default_rng(seed)
    L = len(effects)
    g = (rng.random((N, L, 2)) < freqs[None, :, None]) * effects[None, :, None]
    means, vas = [], []
    for t in range(T + 1):
        G = g.sum(axis=(1, 2))
        means.append(G.mean())
        vas.append(G.var())
        z = G + rng.normal(0, 1, N)
        par = np.argsort(z)[-NSEL:]
        # random mating among the selected; each parent passes one allele per locus
        m = rng.choice(par, N)
        f = rng.choice(par, N)
        pick_m = rng.integers(0, 2, (N, L))
        pick_f = rng.integers(0, 2, (N, L))
        idx = np.arange(L)[None, :]
        new = np.empty_like(g)
        new[:, :, 0] = g[m[:, None], idx, pick_m]
        new[:, :, 1] = g[f[:, None], idx, pick_f]
        if mu > 0:
            hit = rng.random(new.shape) < mu
            new = new + hit * rng.normal(0, np.sqrt(sm2), new.shape)
        g = new
    return np.array(means), np.array(vas)


cases = [
    ("A  10 major loci", np.full(10, 0.5), np.full(10, 0.1), {}),
    ("B  400 minor + 2 major loci", np.r_[np.full(400, 0.03), [0.5, 0.5]], np.r_[np.full(400, 0.5), [0.1, 0.1]], {}),
    ("C  100 loci with mutation", np.full(100, 0.1), np.full(100, 0.3), dict(mu=0.001, sm2=0.0115)),
]
fig, axs = plt.subplots(2, 3, figsize=(11.5, 5.0), sharex=True)
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.11, top=0.92, wspace=0.25, hspace=0.18)
tt = np.arange(T + 1)
for k, (title, eff, fr, kw) in enumerate(cases):
    for seed, tok in ((1, "dna"), (2, "rna")):
        m, v = simulate(eff, fr, seed, **kw)
        axs[0, k].plot(tt, m - m[0], color=charts.line(tok), lw=1.8)
        axs[1, k].plot(tt, v, color=charts.line(tok), lw=1.8)
    axs[0, k].set_ylim(-0.5, 22)
    axs[1, k].set_ylim(0, 1.0)
    charts.style_axes(axs[0, k], None, "change in mean" if k == 0 else None)
    charts.style_axes(axs[1, k], "generation", "$V_A$" if k == 0 else None)
    charts.title(axs[0, k], title)
