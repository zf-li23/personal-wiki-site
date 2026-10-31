# Sequence specificity in the energy-matrix (position weight matrix) model.
# A hypothetical transcription factor with a 10-bp site; binding energy E(s) = sum_i eps_i(s_i) in kT,
# zero for the consensus base at each position and 1-4 kT for the others (stronger penalties in the centre).
# A: the sequence logo of the sites expected if sites are Boltzmann samples, p_i(b) ~ exp(-eps_i(b)).
# B: the energy landscape along 600 bp of random sequence (equal base frequencies) containing one consensus
#    site at position 300; occupancy p = 1/(1 + exp(E - mu)) at mu = 2 kT.
# C: energies of all 4.6 x 10^6 positions of a random genome (histogram, logarithmic counts, computed from
#    10^6 positions and scaled) and the Fermi occupancy at three chemical potentials: the expected number of
#    occupied non-consensus sites is the overlap of the two.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts, sequence

P = bio.P
rng = np.random.default_rng(0)
Lw = 10
cons = rng.integers(0, 4, Lw)
scale = np.array([1.0, 1.5, 2.2, 3.0, 3.5, 3.5, 3.0, 2.2, 1.5, 1.0])
eps = np.zeros((Lw, 4))
for i in range(Lw):
    pen = scale[i] * rng.uniform(0.6, 1.2, 3)
    others = [b for b in range(4) if b != cons[i]]
    eps[i, others] = pen

fig = plt.figure(figsize=(13.5, 4.3))
gs = fig.add_gridspec(1, 3, width_ratios=[0.9, 1.3, 1.1])
ax = fig.add_subplot(gs[0])
ax.set_xlim(-1.2, 6.2)
ax.set_ylim(-1.0, 3.2)
ax.axis("off")
p = np.exp(-eps)
p /= p.sum(axis=1, keepdims=True)
sequence.logo(ax, p, at=(0.4, 0.2), col_width=0.55, height=2.2, kind="probs")
bio.label(ax, (3.1, 3.0), "A   Logo of Boltzmann-distributed sites", size="small", bold=True)
bio.label(ax, (3.1, -0.65), "position in site", size="small")

seq = rng.integers(0, 4, 600)
seq[300:310] = cons
E = np.array([eps[np.arange(Lw), seq[j:j + Lw]].sum() for j in range(600 - Lw)])
ax = fig.add_subplot(gs[1])
ax.plot(E, color=charts.line("dna"), lw=0.8)
ax.set_ylim(-1, E.max() + 1)
ax2 = ax.twinx()
ax2.plot(np.arange(E.size), 1 / (1 + np.exp(E - 2.0)), color=charts.line("rna"), lw=1.6, zorder=5)
ax2.set_ylim(0, 3)
ax2.set_yticks([0, 0.5, 1])
ax2.tick_params(colors=P.muted(), labelcolor=charts.line("rna"), labelsize=7)
ax2.set_ylabel("occupancy (μ = 2 kT)", color=charts.line("rna"), fontsize=8)
for sp in ax2.spines.values():
    sp.set_visible(False)
charts.style_axes(ax, "position / bp", "binding energy E / kT")
ax.text(305, -0.6, "consensus site", fontsize=7.5, color=P.ink())
charts.title(ax, "B   Energy landscape of a sequence")

G = 4.6e6
M = 1_000_000
g = rng.integers(0, 4, M + Lw)
win = np.lib.stride_tricks.sliding_window_view(g, Lw)[:M]
Eg = eps[np.arange(Lw), win].sum(axis=1)
ax = fig.add_subplot(gs[2])
h, e = np.histogram(Eg, bins=60)
c = 0.5 * (e[1:] + e[:-1])
ax.bar(c, h * G / M, width=e[1] - e[0], color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3)
ax.set_yscale("log")
ax.set_xlim(0, e[-1])
charts.style_axes(ax, "binding energy E / kT", "number of genomic sites")
ax2 = ax.twinx()
EE = np.linspace(0, e[-1], 300)
for mu, tok in ((0.0, "positive"), (3.0, "rna"), (6.0, "negative")):
    occ = (h * G / M * (1 / (1 + np.exp(c - mu)))).sum()
    ax2.plot(EE, 1 / (1 + np.exp(EE - mu)), color=charts.line(tok), lw=1.4,
             label=f"μ = {mu:g} kT: {occ:,.0f} occupied")
ax2.set_ylim(0, 1.05)
ax2.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=7)
ax2.set_ylabel("occupancy", fontsize=8, color=P.ink())
for sp in ax2.spines.values():
    sp.set_visible(False)
ax2.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.22, 0.6))
charts.title(ax, "C   Genomic background and occupancy")
fig.tight_layout()
