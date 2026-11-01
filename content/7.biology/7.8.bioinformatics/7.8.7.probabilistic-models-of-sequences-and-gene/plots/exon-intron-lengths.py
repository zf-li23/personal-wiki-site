# Length distributions of human internal exons and introns: the 1711 internal exons and 1883 introns of
# the longest RefSeq (NM) transcript of each of the 228 curated protein-coding genes on chromosome 21
# (GRCh38). A: internal exons (median 126 bp), histogram in 10-bp bins with the geometric distribution of
# the same mean (143 bp), which an ordinary hidden Markov state with a self-transition would impose; the
# observed distribution has a mode near 100-150 bp and few exons shorter than 50 bp. B: introns, on a
# logarithmic length axis (median 1.9 kb, mean 6.1 kb, longest 339 kb). The gap between such
# distributions and the geometric is the reason for explicit length distributions in generalized HMMs.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
ex = np.genfromtxt("exon-lengths.csv", skip_header=1)
it = np.genfromtxt("intron-lengths.csv", skip_header=1)
fig, ax = bio.canvas(22.0, 8.6)
a = C.axes_at(ax, (1.9, 1.5, 8.4, 6.4))
bins = np.arange(0, 610, 10)
a.hist(np.clip(ex, 0, 605), bins=bins, density=True, color=P.light("dna"), edgecolor=C.line("dna"), lw=0.5,
       label="internal exons")
m = ex.mean()
xx = np.arange(1, 600)
a.plot(xx, (1 / m) * (1 - 1 / m) ** (xx - 1), color=C.line("negative"), lw=1.4, label=f"geometric, mean {m:.0f} bp")
a.set_xlim(0, 600)
C.style_axes(a, "exon length (bp)", "density")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())
b = C.axes_at(ax, (12.8, 1.5, 8.4, 6.4))
lb = np.logspace(1.5, 6, 46)
b.hist(it, bins=lb, color=P.light("rna"), edgecolor=C.line("rna"), lw=0.5)
b.set_xscale("log")
C.style_axes(b, "intron length (bp, log scale)", "number of introns")
bio.panel(ax, "A", (0.2, 8.3))
bio.panel(ax, "B", (11.4, 8.3))
