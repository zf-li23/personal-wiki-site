"""Wright's stationary distribution with symmetric mutation, phi(p) ~ p^(4N mu - 1) (1 - p)^(4N mu - 1), for
4N mu = 0.2, 1 and 5 (curves), compared with the frequencies of one simulated Wright-Fisher population of
N = 50 with two-way mutation (sampled every 10 generations for 200 000 generations; histograms). Dashed: with
genic selection 4Ns = 2 added to 4N mu = 1, phi ~ exp(4Nsp) (flat case tilted toward the favored allele)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.4))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.88, wspace=0.28)
N = 50
rng = np.random.default_rng(5)
for ax, th, tok in zip(axs, (0.2, 1.0, 5.0), ("rna", "enzyme", "dna")):
    mu = th / (4 * N)
    p, samp = 0.5, []
    for g in range(200000):
        pm = p * (1 - mu) + (1 - p) * mu
        p = rng.binomial(2 * N, pm) / (2 * N)
        if g % 10 == 0:
            samp.append(p)
    bins = np.linspace(0, 1, 21)
    ax.hist(samp, bins=bins, density=True, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.5)
    x = np.linspace(0.005, 0.995, 300)
    f = lambda y: y ** (th - 1) * (1 - y) ** (th - 1)
    Z = quad(f, 0, 1)[0]
    ax.plot(x, f(x) / Z, color=P.ink(), lw=1.6)
    if th == 1.0:
        g = lambda y: np.exp(2 * y)
        Zg = quad(g, 0, 1)[0]
        ax.plot(x, g(x) / Zg, color=P.ink(), lw=1.2, ls="--")
        ax.text(0.98, 1.85, "with $4Ns = 2$", ha="right", fontsize=FT["tiny"], color=P.ink())
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.5 if th < 1 else 2.6)
    charts.style_axes(ax, "allele frequency $p$", "density" if th == 0.2 else None)
    charts.title(ax, f"{'ABC'[[0.2, 1.0, 5.0].index(th)]}  $4N\\mu = {th}$")
