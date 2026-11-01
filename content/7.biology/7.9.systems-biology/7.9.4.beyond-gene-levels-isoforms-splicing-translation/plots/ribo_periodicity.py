"""Ribosome profiling reads and the three-nucleotide periodicity (simulated reads). A: positions of the 5'
ends of 29-nt footprints relative to the A of the annotated start codon, summed over genes (a metagene):
the peak 12 nt upstream marks ribosomes initiating with the start codon in the P site, and downstream the
counts repeat every three nucleotides. B: after shifting each read length by its P-site offset (12 nt for
28 and 29 nt, 13 nt for 30 nt), the fraction of P sites in each reading frame of coding sequences;
lengths whose reads are poorly phased (here 30 nt) are often discarded. C: a test of active translation
for candidate ORFs in the style of RiboCode: for each codon the P-site counts in frames 0, 1 and 2 are
compared by one-sided Wilcoxon signed-rank tests (frame 0 above frame 1, frame 0 above frame 2), and the
two p-values are combined by Stouffer's method. A translated ORF (top) and a region covered by reads
without phase (bottom, as from a non-ribosomal protected fragment)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.6), gridspec_kw={"width_ratios": [1.5, 0.9, 1.3]})
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.88, wspace=0.32)

# A: metagene of 5' ends for 29-nt reads
pos = np.arange(-30, 61)
psite = np.zeros(len(pos))
cds = pos >= 0
frame_w = np.array([0.72, 0.14, 0.14])
psite[cds] = 40 * frame_w[pos[cds] % 3] / frame_w.mean()
psite[pos == 0] += 260            # initiating ribosomes, P site on AUG
psite[(pos >= -30) & (pos < 0)] = 3
counts5 = np.zeros(len(pos))
for i, p in enumerate(pos):
    j = np.searchsorted(pos, p + 12)  # 5' end = P site - 12
    if j < len(pos) and pos[j] == p + 12:
        counts5[i] = rng.poisson(psite[j])
ax = axs[0]
cols = [charts.line("dna"), P.fill("neutral"), P.fill("neutral")]
ax.bar(pos, counts5, width=0.85, color=[charts.line("dna") if (p + 12) % 3 == 0 and p + 12 >= 0 else P.fill("neutral") for p in pos], lw=0)
ax.annotate("start codon in P site\n(5' end at -12)", xy=(-12, counts5[pos == -12][0]), xytext=(-29, 230),
            fontsize=7.5, color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.axvline(0, color=P.muted(), lw=0.7, ls="--")
ax.text(1, 300, "AUG", fontsize=7.5, color=P.muted())
ax.set_xlim(-31, 46)
charts.style_axes(ax, "5' end of read relative to start codon (nt)", "reads (29 nt)")
charts.title(ax, "A  Metagene at the start codon")

# B: frame fractions by read length
ax = axs[1]
fr = {28: [0.68, 0.17, 0.15], 29: [0.74, 0.13, 0.13], 30: [0.41, 0.30, 0.29]}
x = np.arange(3)
for k, (ln, f) in enumerate(fr.items()):
    n = rng.multinomial(20000, f)
    ax.bar(k + (x - 1) * 0.26, n / n.sum(), width=0.24,
           color=[charts.line("dna"), P.fill("rna"), P.fill("neutral")], edgecolor="none")
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["28 nt", "29 nt", "30 nt"])
ax.set_ylim(0, 0.85)
for c, t in zip([charts.line("dna"), P.fill("rna"), P.fill("neutral")], ["frame 0", "frame +1", "frame +2"]):
    ax.bar([0], [0], color=c, label=t)
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(ax, "read length", "fraction of P sites")
charts.title(ax, "B  Phase by read length")

# C: RiboCode-style test on two candidate ORFs
ax = axs[2]
ncod = 60
orfs = {"translated ORF": [0.7, 0.15, 0.15], "unphased coverage": [0.34, 0.33, 0.33]}
for r, (name, w) in enumerate(orfs.items()):
    dens = rng.gamma(2.0, 1.5, ncod)          # codon-to-codon variation of ribosome density
    F = rng.poisson(dens[:, None] * np.array(w)[None, :] * 3)
    p1 = stats.wilcoxon(F[:, 0], F[:, 1], alternative="greater").pvalue
    p2 = stats.wilcoxon(F[:, 0], F[:, 2], alternative="greater").pvalue
    z = (stats.norm.isf(p1) + stats.norm.isf(p2)) / np.sqrt(2)
    pc = stats.norm.sf(z)
    base = 1.25 - 1.25 * r
    for f, c in zip(range(3), [charts.line("dna"), charts.line("rna"), P.muted()]):
        ax.vlines(np.arange(ncod) + f / 3, base, base + 0.8 * F[:, f] / F.max(), color=c, lw=1.1)
    ax.text(0, base + 0.95, f"{name}: p(F0>F1) = {p1:.1g}, p(F0>F2) = {p2:.1g}, combined p = {pc:.1g}",
            fontsize=7, color=P.ink())
    print(name, p1, p2, pc)
ax.set_ylim(-0.05, 2.35)
ax.set_yticks([])
ax.set_xlim(-1, ncod + 1)
charts.style_axes(ax, "codon of candidate ORF (bars: P sites in frame 0, +1, +2)", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "C  Testing the phase of an ORF")
