# Sequence and specificity of a DNA-binding protein. A transcription factor recognizes a site of
# L = 12 bp; each mismatch to the consensus costs eps (in kBT), and the occupancy of a site with k
# mismatches is the Fermi function p(k) = 1/(1 + exp(k eps - mu')), with mu' set so that the consensus
# site is 99 % occupied. A: occupancy against the number of mismatches for eps = 1, 2 and 3 kBT.
# B: expected number of occupied sites with k mismatches in a random genome of 4.6 Mb (both strands),
# 2G C(L, k) 3^k / 4^L times p(k): with weak discrimination the protein is soaked up by the thousands of
# near-consensus sites. C: Berg and von Hippel's selection theory tested by simulation: binding sites
# evolving under selection for occupancy (fitness = occupancy, weak-mutation dynamics, stationary
# distribution proportional to fitness^(N-1) with N = 200, sampled by Metropolis Monte Carlo) with a
# random energy matrix (mismatch energies 0.5-3 kBT, position and base specific): the log frequency of
# each base relative to the consensus at each position is proportional to minus its energy, as for a
# Boltzmann distribution with an effective temperature.
import math

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
L, G = 12, 4.6e6
k = np.arange(L + 1)
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
for eps, tok in ((1.0, "rna"), (2.0, "enzyme"), (3.0, "dna")):
    mu = np.log(99)
    p = 1 / (1 + np.exp(k * eps - mu))
    Nk = 2 * G * np.array([math.comb(L, i) * 3**i for i in k]) / 4**L
    axs[0].plot(k, p, "o-", ms=4, color=charts.line(tok), lw=1.4, label=f"$\\varepsilon$ = {eps:g} $k_{{\\mathrm{{B}}}}T$")
    axs[1].plot(k, Nk * p, "o-", ms=4, color=charts.line(tok), lw=1.4, label=f"$\\varepsilon$ = {eps:g}: total {np.sum(Nk * p):.0f}")
axs[0].legend(fontsize=7.5, frameon=False)
charts.style_axes(axs[0], "mismatches to consensus $k$", "occupancy $p(k)$")
charts.title(axs[0], "A   Binding falls off with mismatches")
Nk = 2 * G * np.array([math.comb(L, i) * 3**i for i in k]) / 4**L
axs[1].plot(k, Nk, color=P.muted(), lw=1.0, ls="--", label="sites in genome")
axs[1].set_yscale("log")
axs[1].set_ylim(1e-4, 1e7)
axs[1].legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(axs[1], "mismatches to consensus $k$", "expected occupied sites")
charts.title(axs[1], "B   The genome is a sea of decoys")

eps_m = np.zeros((L, 4))
cons = rng.integers(0, 4, L)
for i in range(L):
    for b in range(4):
        if b != cons[i]:
            eps_m[i, b] = rng.uniform(0.5, 3.0)
Npop = 200
mu = 6.0  # chemical potential term: consensus energy 0, occupancy 1/(1+exp(E - mu))


def logfit(E):
    return -np.log1p(np.exp(E - mu))


seq = cons.copy()
E = 0.0
counts = np.zeros((L, 4))
for step in range(300000):
    i = rng.integers(L)
    b = (seq[i] + rng.integers(1, 4)) % 4
    En = E - eps_m[i, seq[i]] + eps_m[i, b]
    if np.log(rng.random()) < (Npop - 1) * (logfit(En) - logfit(E)):
        seq[i] = b
        E = En
    if step > 20000 and step % 10 == 0:
        counts[np.arange(L), seq] += 1
freq = counts / counts.sum(1, keepdims=True)
xs, ys = [], []
for i in range(L):
    for b in range(4):
        if b != cons[i] and freq[i, b] > 0:
            xs.append(eps_m[i, b])
            ys.append(np.log(freq[i, b] / freq[i, cons[i]]))
ax = axs[2]
ax.plot(xs, ys, "o", ms=4.5, color=charts.line("protein"))
sl, ic = np.polyfit(xs, ys, 1)
xx = np.linspace(0.4, 3.1, 20)
ax.plot(xx, sl * xx + ic, color=P.muted(), lw=1.0, ls="--", label=f"slope $-\\lambda$ = {sl:.2f}")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "mismatch energy $\\varepsilon_{i,b}$ / $k_{\\mathrm{B}}T$", "$\\ln(f_{i,b}/f_{i,\\mathrm{cons}})$ in evolved sites")
charts.title(ax, "C   Selection makes a Boltzmann distribution")
fig.tight_layout()
