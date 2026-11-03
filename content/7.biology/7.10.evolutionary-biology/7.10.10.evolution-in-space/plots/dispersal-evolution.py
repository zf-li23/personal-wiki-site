"""The evolution of dispersal. A: the evolutionarily stable fraction of offspring that disperse when each
site holds one adult, offspring compete for vacant sites and a disperser survives with probability p
(Hamilton and May 1977): v* = 1 / (2 - p). Even when dispersal is almost always fatal, half of the offspring
should leave, because a dispersing offspring does not compete with its siblings. B: spatial sorting during
a range expansion, in an individual-based simulation (seed 0): individuals on a line of unit cells
reproduce with mean offspring number 2 / (1 + n / 20) (n: individuals in the cell), and offspring move a
normally distributed distance whose SD d is inherited from the parent with small mutations (SD 0.05).
Initial d is uniform on (0.5, 1.5) in 200 founders near x = 0. Lines: mean d in the core (x < 20) and in
the 20 cells at the expanding front, every 5 generations. Dispersal ability increases at the front
more than in the core, because the best dispersers arrive first and breed with each other. (Dispersal has
no cost in this model, so the mean rises slowly in the core as well, as better dispersers spread there.)"""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
a = axs[0]
p = np.linspace(0, 1, 200)
a.plot(p, 1 / (2 - p), color=charts.line("dna"), lw=2)
a.set_ylim(0, 1.05)
a.set_xlim(0, 1)
charts.style_axes(a, "survival of dispersers $p$", "ESS dispersal fraction $v^*$")
charts.title(a, "A  Kin competition favours dispersal")

b = axs[1]
rng = np.random.default_rng(0)
x = rng.uniform(0, 5, 200)
d = rng.uniform(0.5, 1.5, 200)
T = 80
gens, core, front = [], [], []
for t in range(T + 1):
    cell = np.floor(x).astype(int)
    counts = np.bincount(cell)
    if t % 5 == 0:
        xmax = x.max()
        gens.append(t)
        core.append(d[x < 20].mean())
        front.append(d[x > xmax - 20].mean())
    lam = 2 / (1 + counts[cell] / 20)
    k = rng.poisson(lam)
    par = np.repeat(np.arange(len(x)), k)
    dn = np.clip(d[par] + rng.normal(0, 0.05, len(par)), 0.05, None)
    xn = np.abs(x[par] + rng.normal(0, 1, len(par)) * dn)
    x, d = xn, dn
b.plot(gens, front, color=charts.line("rna"), lw=2, marker="o", ms=3, label="expanding front")
b.plot(gens, core, color=charts.line("dna"), lw=2, marker="o", ms=3, label="core of the range")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "generation", "mean dispersal distance $d$")
charts.title(b, "B  Spatial sorting during range expansion")
