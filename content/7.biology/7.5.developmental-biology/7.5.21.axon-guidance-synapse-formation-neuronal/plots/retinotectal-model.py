"""Formation of the retinotectal map by graded repulsion and competition (Formula 21.5.1, a stochastic model in the
spirit of Koulakov and Tsigankov). 120 retinal axons, each with an EphA level that rises from nasal to temporal
retina, compete for 120 tectal sites whose ephrin-A level rises from anterior to posterior; the repulsive energy
of an axon at a site is the product of the two levels, and Monte Carlo exchanges of neighbouring axons lower the
total energy. (A) Starting from a random arrangement, the map becomes ordered and inverted: temporal axons (high
EphA) end in the anterior tectum (low ephrin-A), nasal axons in the posterior. (B) The experiment of Brown et al.
(2000): in half of the retinal ganglion cells, scattered at random, EphA3 is added (knock-in). The model, like the
mice, forms two interleaved maps: knock-in axons, with uniformly higher EphA, take the anterior half of the
tectum in retinotopic order, the wild-type axons are displaced into the posterior half. Position on the tectum
therefore depends on the EphA level of an axon relative to its competitors."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
n = 120
u = np.linspace(0, 1, n)                  # retinal position: 0 nasal, 1 temporal
v = np.linspace(0, 1, n)                  # tectal position: 0 anterior, 1 posterior
L = np.exp(1.5 * v)                       # ephrin-A on the tectum


def anneal(R, seed=0, sweeps=1500, T0=2.0):
    rng = np.random.default_rng(seed)
    site = rng.permutation(n)             # axon i sits at tectal site site[i]
    at = np.empty(n, int)
    at[site] = np.arange(n)               # which axon is at each site
    for s in range(sweeps):
        T = T0 * (1 - s / sweeps) + 1e-3
        for _ in range(n):
            j = rng.integers(0, n - 1)    # exchange the axons at neighbouring sites j and j + 1
            a, b = at[j], at[j + 1]
            dE = (R[a] - R[b]) * (L[j + 1] - L[j])
            if dE < 0 or rng.random() < np.exp(-dE / T * 50):
                at[j], at[j + 1] = b, a
                site[a], site[b] = j + 1, j
    return site / (n - 1)


R = np.exp(1.5 * u)
wt = anneal(R)
rng = np.random.default_rng(1)
ki = rng.random(n) < 0.5
R2 = R + np.where(ki, 2.0, 0.0)
mut = anneal(R2, seed=2)
init = np.random.default_rng(0).permutation(n) / (n - 1)

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.28)
a.plot(u, init, "o", ms=2.5, color=P_.fill("neutral"), label="initial (random)")
a.plot(u, wt, "o", ms=3, color=charts.line("dna"), label="final")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(a, "retinal position (nasal 0, temporal 1)", "tectal position (anterior 0, posterior 1)")
charts.title(a, "A  Wild type")
b.plot(u[~ki], mut[~ki], "o", ms=3, color=charts.line("dna"), label="wild-type axons")
b.plot(u[ki], mut[ki], "o", ms=3, color=charts.line("negative"), label="EphA3 knock-in axons")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(b, "retinal position (nasal 0, temporal 1)", None)
charts.title(b, "B  Half the axons with extra EphA3")
