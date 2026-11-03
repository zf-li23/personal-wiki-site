"""Why measured rates of evolution fall with the time interval over which they are measured (Section
32.4.1). A trait (in units of its within-population standard deviation) evolves for 10^5 generations
in three ways: a random walk (Brownian motion with variance 0.01 per generation), stasis (fluctuation
around a fixed optimum, an Ornstein-Uhlenbeck process with the same short-term variance and a
restoring rate of 0.01 per generation), and sustained directional change (0.001 per generation plus
the same noise). For pairs of samples separated by an interval of t generations, the rate in haldanes
is |change| / t. A: example trajectories. B: median rate against interval on logarithmic axes. The
slope is -1/2 for a random walk, -1 for stasis (the net change stays bounded) and approaches 0 only
for sustained directional change; a negative slope therefore does not mean that evolution was faster
over short intervals in any absolute sense."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(4)
G = 100000
sd = 0.1
noise = sd * rng.standard_normal((3, G))
bm = np.cumsum(noise[0])
ou = np.zeros(G)
for i in range(1, G):
    ou[i] = ou[i - 1] * (1 - 0.01) + noise[1, i]
dr = np.cumsum(0.001 + noise[2])
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.5))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.28)
gens = np.arange(G)
for z, tok, lab in ((bm, "dna", "random walk"), (ou, "plant", "stasis"), (dr, "rna", "directional")):
    a.plot(gens[::50], z[::50], color=charts.line(tok), lw=1.2, label=lab)
charts.style_axes(a, "generation", "trait mean (SD units)")
charts.title(a, "A  Trajectories")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
ints = np.unique(np.logspace(0, 4.7, 30).astype(int))
for z, tok in ((bm, "dna"), (ou, "plant"), (dr, "rna")):
    med = []
    for t in ints:
        starts = rng.integers(0, G - t, 400)
        med.append(np.median(np.abs(z[starts + t] - z[starts]) / t))
    b.loglog(ints, med, "o-", ms=3, lw=1.3, color=charts.line(tok))
b.loglog(ints, 0.07 * ints ** -0.5, color=P.muted(), lw=0.8, ls=":")
b.text(3000, 0.07 * 3000 ** -0.5 * 1.6, "slope -1/2", fontsize=FT["tiny"], color=P.muted())
b.loglog(ints, 0.07 * ints ** -1.0, color=P.muted(), lw=0.8, ls="--")
b.text(1500, 0.07 / 1500 * 0.45, "slope -1", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(b, "interval (generations)", "rate (haldanes)")
charts.title(b, "B  Rate against interval")
