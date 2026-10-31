# The Zwanzig-Szabo-Bagchi model of folding (1992), solved exactly as a birth-death chain.
# Each of N residues is either correct (1 conformation) or incorrect (nu conformations); every incorrect
# residue costs an energy U. Lumping states by the number n of incorrect residues gives a random walk on
# n = 0..N with rates n -> n-1: n k0 and n -> n+1: (N - n) nu k0 exp(-U/kT) (detailed balance).
# A: free-energy profile F(n)/kT = n U/kT - ln[C(N, n) nu^n] for N = 100: without bias the profile slopes
#    away from the native state (entropy wins); a bias of a few kT per residue tilts it towards n = 0.
# B: exact mean first-passage time from n = N to n = 0 against chain length, for several biases, compared
#    with the Levinthal time (1 + nu)^N / k0 of a random search.
# C: equilibrium population of the fully native state n = 0, with an extra stabilization dE of that state:
#    with independent residues the native state is negligible unless it is stabilized cooperatively.
import math

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
nu, k0 = 2.0, 1e9  # incorrect conformations per residue; elementary rate (1/s)


def log_weights(N, bU, dE=0.0):
    """ln of the equilibrium weight of each n (number of incorrect residues)."""
    n = np.arange(N + 1)
    lw = np.array([math.lgamma(N + 1) - math.lgamma(k + 1) - math.lgamma(N - k + 1) for k in n]) + n * (math.log(nu) - bU)
    lw[0] += dE
    return lw


def mfpt(N, bU, dE=0.0):
    """Exact mean first-passage time from n = N to n = 0 (seconds)."""
    lw = log_weights(N, bU, dE)
    T = 0.0
    for j in range(1, N + 1):
        # time to step from j to j-1: sum_{i>=j} pi_i / (d_j pi_j), with death rate d_j = j k0
        tail = np.logaddexp.reduce(lw[j:])
        T += math.exp(tail - lw[j]) / (j * k0)
    return T


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
cols = [charts.line(t) for t in ("neutral", "dna", "rna", "positive")]

N = 100
n = np.arange(N + 1)
for bU, c in zip((0.0, 1.0, 2.0, 3.0), cols):
    F = -log_weights(N, bU)
    axs[0].plot(n, F - F[0], color=c, lw=1.8, label=f"U = {bU:g} kT")
charts.style_axes(axs[0], "incorrect residues n", "F(n) − F(0)  /  kT")
axs[0].axhline(0, color=P.muted(), lw=0.6)
axs[0].legend(fontsize=7.5, frameon=False)
charts.title(axs[0], "A   Free-energy profile, N = 100, ν = 2")

Ns = np.arange(10, 151, 5)
for bU, c in zip((0.0, 1.0, 2.0, 3.0), cols):
    axs[1].semilogy(Ns, [mfpt(k, bU) for k in Ns], color=c, lw=1.8, label=f"U = {bU:g} kT")
axs[1].semilogy(Ns, (1 + nu) ** Ns / k0, color=P.muted(), lw=1.0, ls="--", label="Levinthal (1+ν)ᴺ/k₀")
for y, txt in ((1.0, "1 s"), (4.3e17, "age of universe")):
    axs[1].axhline(y, color=P.muted(), lw=0.5, ls=":")
    axs[1].text(12, y * 2.5, txt, fontsize=7, color=P.muted())
axs[1].set_ylim(1e-9, 1e60)
charts.style_axes(axs[1], "chain length N", "mean folding time / s")
axs[1].legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.93))
charts.title(axs[1], "B   Exact first-passage time")

dEs = np.linspace(0, 60, 121)
for bU, c in zip((1.0, 2.0, 3.0), cols[1:]):
    p0 = [math.exp(log_weights(N, bU, d)[0] - np.logaddexp.reduce(log_weights(N, bU, d))) for d in dEs]
    axs[2].plot(dEs, p0, color=c, lw=1.8, label=f"U = {bU:g} kT")
    axs[2].axvline(N * math.log(1 + nu * math.exp(-bU)), color=c, lw=0.7, ls=":")
axs[2].set_ylim(-0.02, 1.02)
charts.style_axes(axs[2], "extra stability of the native state ΔE / kT", "equilibrium fraction native")
axs[2].legend(fontsize=7.5, frameon=False, loc="lower right")
charts.title(axs[2], "C   Stability needs cooperativity")
fig.tight_layout()
