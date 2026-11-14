"""Dispersal in a stable habitat (Hamilton and May 1977).

N sites each hold one asexual adult, which produces many offspring and dies; a fraction v of the offspring
disperse at random over the sites and survive the journey with probability s; each site is then taken by one
offspring chosen at random from those present. A: the ESS dispersal fraction v* = 1/(2 - s): at least half of
the offspring should disperse however costly dispersal is. B: the expected number of sites won by a mutant
dispersing a fraction v' in a population at v*, for three values of s; each curve peaks at v' = v*.
C: individual-based simulation (400 sites, 20 offspring per adult, heritable v with small mutations): mean
dispersal fraction over generations from v = 0.1, for s = 0.2 and s = 0.8, with the predicted ESS (dashed).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(1)
fig, ax = bio.canvas(33.0, 10.0)

pa = Ch.axes_at(ax, (2.4, 1.7, 7.4, 7.2))
s = np.linspace(0, 1, 200)
pa.plot(s, 1 / (2 - s), color=Ch.line("rna"), lw=1.8)
pa.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(0.25, 0.47, "v* = 1/2 when dispersal is almost always fatal", fontsize=FS["tiny"], color=P.muted(),
        va="top")
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.05)
Ch.style_axes(pa, "survival of dispersers s", "ESS dispersal fraction v*")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (13.4, 1.7, 7.4, 7.2))
vm = np.linspace(0, 1, 300)
for sv, tok in ((0.2, "dna"), (0.5, "protein"), (0.9, "rna")):
    v = 1 / (2 - sv)
    W = (1 - vm) / (1 - vm + sv * v) + sv * vm / (1 - v + sv * v)
    pb.plot(vm, W, color=Ch.line(tok), lw=1.6)
    pb.plot([v], [(1 - v) / (1 - v + sv * v) + sv * v / (1 - v + sv * v)], "o", color=Ch.line(tok), ms=4)
    pb.text(v, 1.02, f"s = {sv:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="bottom", ha="center")
pb.set_xlim(0, 1)
pb.set_ylim(0.6, 1.25)
Ch.style_axes(pb, "dispersal fraction of a mutant v'", "sites won (resident = 1)")
bio.panel(ax, "B", (11.3, 9.8))

pc = Ch.axes_at(ax, (24.4, 1.7, 7.8, 7.2))
N, K, G = 400, 20, 3000
for sv, tok in ((0.2, "dna"), (0.8, "rna")):
    v = np.full(N, 0.1)
    mean = []
    for g in range(G):
        stay = K * (1 - v)
        pool = (K * v * sv).sum() / N
        local = rng.random(N) < stay / (stay + pool)
        parent = np.where(local, np.arange(N), rng.choice(N, N, p=v / v.sum()))
        v = np.clip(v[parent] + rng.normal(0, 0.01, N), 0.001, 0.999)
        mean.append(v.mean())
    pc.plot(np.arange(G), mean, color=Ch.line(tok), lw=1.4)
    pc.axhline(1 / (2 - sv), color=Ch.line(tok), lw=0.8, ls=(0, (3, 2)))
    pc.text(G * 0.6, 1 / (2 - sv) + 0.07, f"s = {sv:g}", fontsize=FS["tiny"], color=Ch.line(tok), ha="right",
            va="bottom")
pc.set_xlim(0, G)
pc.set_ylim(0, 1)
Ch.style_axes(pc, "generation", "mean dispersal fraction")
bio.panel(ax, "C", (22.3, 9.8))
