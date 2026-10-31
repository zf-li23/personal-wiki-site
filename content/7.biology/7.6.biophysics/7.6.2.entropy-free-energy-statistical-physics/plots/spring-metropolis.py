# Metropolis sampling of a bead in a harmonic trap, E(x) = k x^2 / 2, with k = 0.05 pN/nm (a soft optical trap)
# at T = 310 K (kBT = 4.28 pN nm). Proposed moves are uniform in [-12, 12] nm and accepted with probability
# min(1, exp(-dE/kBT)); 40 000 steps.
# A: the first 600 steps of the chain.
# B: histogram of all positions after a burn-in of 1000 steps, with the Boltzmann (Gaussian) density of
#    variance kBT/k (standard deviation 9.3 nm).
# C: running average of the energy in units of kBT, which converges to 1/2 (equipartition).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
k, kT = 0.05, 4.28
n, step = 40000, 12.0
x = np.empty(n)
x[0] = 40.0
acc = 0
for i in range(1, n):
    y = x[i - 1] + rng.uniform(-step, step)
    dE = 0.5 * k * (y * y - x[i - 1] ** 2)
    if dE <= 0 or rng.random() < np.exp(-dE / kT):
        x[i] = y
        acc += 1
    else:
        x[i] = x[i - 1]

fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.6), gridspec_kw={"width_ratios": [1.2, 1.0, 1.0]})
ax = axs[0]
ax.plot(np.arange(600), x[:600], color=charts.line("protein"), lw=0.9)
ax.axhline(0, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(ax, "Monte Carlo step", "x / nm")
ax.set_title("A   Markov chain", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
xs = x[1000:]
sig = np.sqrt(kT / k)
ax.hist(xs, bins=60, density=True, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.4)
g = np.linspace(-40, 40, 300)
ax.plot(g, np.exp(-g ** 2 / (2 * sig ** 2)) / np.sqrt(2 * np.pi * sig ** 2), color=charts.line("negative"), lw=1.8)
ax.text(14, 0.036, f"σ = √(kBT/k)\n= {sig:.1f} nm", fontsize=7, color=P.ink())
ax.set_xlim(-40, 40)
charts.style_axes(ax, "x / nm", "probability density / nm⁻¹")
ax.set_title("B   Boltzmann distribution", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
E = 0.5 * k * xs ** 2 / kT
run = np.cumsum(E) / np.arange(1, len(E) + 1)
ax.semilogx(np.arange(1, len(E) + 1), run, color=charts.line("dna"), lw=1.5)
ax.axhline(0.5, color=P.muted(), lw=0.9, ls=(0, (4, 3)))
ax.text(30, 0.36, "⟨E⟩ = kBT/2", fontsize=7, color=P.ink())
ax.set_ylim(0, 1.2)
charts.style_axes(ax, "number of samples", "running ⟨E⟩ / kBT")
ax.set_title("C   Equipartition", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
