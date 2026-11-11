"""Divisive normalization in the Drosophila antennal lobe (model after Olsen, Bhandawat and Wilson 2010).

PN rate r = R_max x^n / (sigma^n + x^n + (m s)^n) with x the rate of the ORNs of its own glomerulus
and s the summed ORN input to the lobe, which drives the GABAergic local neurons
(R_max = 165 Hz, sigma = 12 Hz, n = 1.5, m = 0.05; illustrative values of the fitted magnitude).
A: input-output curves at four levels of total ORN input: lateral input shifts the curve to the right
(gain control) without changing its maximum. B: ORN rates across 50 glomeruli x 100 odours drawn from
an exponential distribution (mean 15 Hz; most responses weak) and the PN rates they produce with no
lateral input: the PN histogram is flatter, so the population uses its range of rates more evenly.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
Rmax, sig, n, m = 165.0, 12.0, 1.5, 0.05


def pn(x, s):
    return Rmax * x**n / (sig**n + x**n + (m * s) ** n)


fig, axs = plt.subplots(1, 2, figsize=(10, 4.0))
ax = axs[0]
x = np.linspace(0, 300, 400)
cols = [P.edge("dna"), P.edge("enzyme"), P.edge("rna"), P.edge("negative")]
for s, c in zip((0, 500, 1500, 4000), cols):
    ax.plot(x, pn(x, s), color=c, lw=2, label=f"total ORN input {s} Hz")
ax.set_xlabel("ORN rate x / Hz")
ax.set_ylabel("PN rate r / Hz")
ax.set_ylim(0, 175)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("A  Gain control by lateral inhibition", loc="left", fontsize=10)

ax = axs[1]
orn = rng.exponential(15.0, 5000)
p = pn(orn, 0.0)
bins = np.linspace(0, 1, 21)
ax.hist(orn / orn.max(), bins=bins, density=True, color=P.fill("dna"), edgecolor=P.edge("dna"),
        alpha=0.7, label="ORN rate / max")
ax.hist(p / Rmax, bins=bins, density=True, histtype="step", color=P.edge("rna"), lw=2,
        label="PN rate / R_max")
ax.set_xlabel("Normalized rate")
ax.set_ylabel("Probability density")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Spreading responses over the range", loc="left", fontsize=10)
fig.tight_layout()
