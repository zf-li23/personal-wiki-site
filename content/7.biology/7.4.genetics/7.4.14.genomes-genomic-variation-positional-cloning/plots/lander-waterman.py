"""The Lander-Waterman model of shotgun assembly (Formula 14.2.1). Reads of length L = 1 000 are placed at
random on a genome of G = 1 Mb; two reads are joined if they overlap by at least T = 100 bases
(sigma = 1 - T/L = 0.9). A: fraction of the genome not covered, exp(-c). B: expected number of contigs,
N exp(-c sigma) = (cG/L) exp(-c sigma), which is largest at c = 1/sigma. Circles: means of 20 simulated
assemblies at each coverage."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
G, L, T = 1_000_000, 1000, 100
sig = 1 - T / L
cs = np.linspace(0.05, 10, 300)
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.7))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
csim = [0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10]
unc, ncon = [], []
for c in csim:
    u, k = [], []
    for _ in range(20):
        N = int(round(c * G / L))
        s = np.sort(rng.integers(0, G, N))     # circular genome: no edge effects
        cov = np.zeros(G + L + 1, int)
        np.add.at(cov, s, 1)
        np.add.at(cov, s + L, -1)
        depth = np.cumsum(cov)[:G + L]
        depth[:L] += depth[G:G + L]
        u.append(np.mean(depth[:G] == 0))
        gaps = np.diff(s) > L - T           # next read does not overlap enough: a contig ends
        k.append(1 + gaps.sum())
    unc.append(np.mean(u))
    ncon.append(np.mean(k))
ax = axs[0]
ax.semilogy(cs, np.exp(-cs), color=charts.line("dna"), lw=1.5, label="exp(−c)")
ax.semilogy(csim, np.maximum(unc, 1e-6), "o", mfc="none", color=charts.line("dna"), ms=4, label="simulation")
ax.set_ylim(1e-5, 1.2)
charts.style_axes(ax, "coverage c = NL/G", "fraction of genome not covered")
charts.title(ax, "A  Gaps in coverage")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
ax = axs[1]
ax.plot(cs, cs * G / L * np.exp(-cs * sig), color=charts.line("receptor"), lw=1.5, label="N exp(−cσ)")
ax.plot(csim, ncon, "o", mfc="none", color=charts.line("receptor"), ms=4, label="simulation")
ax.axvline(1 / sig, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(ax, "coverage c = NL/G", "number of contigs")
charts.title(ax, "B  Contigs (G = 1 Mb, L = 1 kb, T = 100)")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
