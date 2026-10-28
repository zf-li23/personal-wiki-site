"""Open reading frames in random sequence (Formula 14.3.1). A: lengths of ORFs (stop to stop, in codons)
in 3 Mb of random sequence with equal base frequencies, all six frames (bars), against the geometric law
P(length >= k) = (61/64)^k (line). B: expected number of chance ORFs of at least k codons in a random
sequence the size of the human genome (3.1 Gb, six frames), compared with about 20 000 protein-coding
genes; the median human protein is about 375 amino acids, but its ORF is split by introns into exons of
about 50 codons on average."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
seq = rng.integers(0, 4, 3_000_000)
comp = 3 - seq[::-1]
stops = {(3, 0, 0), (3, 0, 2), (3, 2, 0)}  # TAA TAG TGA with A=0 C=1 G=2 T=3
lengths = []
for s in (seq, comp):
    for f in range(3):
        cod = s[f:len(s) - (len(s) - f) % 3].reshape(-1, 3)
        is_stop = ((cod[:, 0] == 3) & (((cod[:, 1] == 0) & ((cod[:, 2] == 0) | (cod[:, 2] == 2))) | ((cod[:, 1] == 2) & (cod[:, 2] == 0))))
        idx = np.flatnonzero(is_stop)
        lengths += list(np.diff(idx) - 1)
lengths = np.array(lengths)
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.7))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
ax = axs[0]
k = np.arange(0, 200)
surv = np.array([(lengths >= kk).mean() for kk in k])
ax.semilogy(k[::5], surv[::5], "o", mfc="none", ms=3.5, color=charts.line("dna"), label="random sequence, 3 Mb")
ax.semilogy(k, (61 / 64) ** k, color=charts.line("dna"), lw=1.4, label="(61/64)^k")
ax.set_ylim(1e-5, 1.2)
charts.style_axes(ax, "ORF length k / codons", "fraction of ORFs ≥ k")
charts.title(ax, "A  ORF lengths are geometric")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
ax = axs[1]
k2 = np.arange(30, 501)
nstop = 3.1e9 / 3 * 3 / 64 * 6
ax.semilogy(k2, nstop * (61 / 64) ** k2, color=charts.line("receptor"), lw=1.5, label="chance ORFs in 3.1 Gb")
ax.axhline(2e4, color=charts.line("positive"), lw=1.2, ls="--", label="protein-coding genes (about 20 000)")
ax.axvline(50, color=P.muted(), lw=0.6, ls=":")
ax.text(54, 3e7, "mean exon\n≈ 50 codons", fontsize=bio.core.FONT["tiny"], color=P.muted(), va="top")
ax.set_ylim(1, 1e9)
charts.style_axes(ax, "minimum ORF length k / codons", "expected number")
charts.title(ax, "B  Chance ORFs in a human-sized genome")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
