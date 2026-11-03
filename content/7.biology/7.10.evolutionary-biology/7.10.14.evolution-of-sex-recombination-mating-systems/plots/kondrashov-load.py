"""Equilibrium mutation load with and without recombination (Theorem 14.2.1).

Distribution f(k) of the number of deleterious mutations, k = 0..250. Each generation: selection by w(k),
then Poisson(U) new mutations. Sexual populations: after mutation the distribution is replaced by a
Poisson distribution with the same mean (free recombination, linkage equilibrium). Load = 1 - mean w at
equilibrium. Multiplicative: w = 0.98^k. Synergistic: log w = -0.01 k - 0.002 k^2.
"""

import numpy as np
from scipy.stats import poisson
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
K = np.arange(0, 251)


def load(U, logw, sexual, iters=1200):
    w = np.exp(logw(K))
    f = poisson.pmf(K, 5.0)
    pm = poisson.pmf(K, U)
    wbar = 1.0
    for _ in range(iters):
        wbar = (f * w).sum()
        g = f * w / wbar
        f = np.convolve(g, pm)[: len(K)]
        f = f / f.sum()
        if sexual:
            f = poisson.pmf(K, (K * f).sum())
    return 1 - wbar


Us = np.linspace(0.05, 2.0, 24)
mult = lambda k: k * np.log(0.98)  # noqa: E731
syn = lambda k: -0.01 * k - 0.002 * k ** 2  # noqa: E731
fig, ax = bio.canvas(16.0, 10.0)
p = C.axes_at(ax, (2.4, 1.6, 12.6, 7.6))
p.plot(Us, 1 - np.exp(-Us), color=P.muted(), lw=3.0, alpha=0.5, label="1 − e^(−U)")
p.plot(Us, [load(U, mult, False) for U in Us], "o", ms=3.5, color=C.line("dna"), label="multiplicative, asexual")
p.plot(Us, [load(U, mult, True) for U in Us], "x", ms=4.5, color=C.line("dna"), label="multiplicative, sexual")
p.plot(Us, [load(U, syn, False) for U in Us], "-", lw=1.8, color=C.line("negative"), label="synergistic, asexual")
p.plot(Us, [load(U, syn, True) for U in Us], "-", lw=1.8, color=C.line("protein"), label="synergistic, sexual")
p.set_xlim(0, 2.05)
p.set_ylim(0, 1)
C.style_axes(p, "genomic deleterious mutation rate U", "equilibrium mutation load")
p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
