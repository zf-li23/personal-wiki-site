# Open reading frames in the Escherichia coli K-12 genome and in a shuffled genome. For every stop codon in
# all six frames, the ORF from the first ATG after the preceding in-frame stop was taken (minimum 30
# codons). Counts in 25-codon bins (orf_hist.csv): the real genome (blue), the same genome with its bases
# randomly permuted (gray; same composition, no genes) and the 4297 annotated protein-coding genes of
# RefSeq NC_000913.3 (orange). In the shuffled genome ORF lengths fall off geometrically, as
# Formula 14.3.1 of 7.4.14 predicts (no ORF reaches 300 codons); the real genome has a long tail of
# ORFs that are almost all annotated genes. Logarithmic vertical axis; ORFs longer than 1200 codons
# are counted in the last bin.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
d = np.genfromtxt("orf_hist.csv", delimiter=",", names=True)
fig, ax = bio.canvas(16.0, 9.0)
a = C.axes_at(ax, (2.0, 1.5, 13.0, 7.0))
x = d["left"] + 12.5
for col, tok, lab in [("shuffled", "neutral", "shuffled genome"), ("genome", "dna", "genome, all ORFs"),
                      ("annotated", "rna", "annotated genes")]:
    y = np.where(d[col] > 0, d[col], np.nan)
    a.semilogy(x, y, "o-", ms=3, lw=1.1, color=C.line(tok), label=lab)
a.set_xlim(0, 1210)
a.set_ylim(0.7, 3e4)
C.style_axes(a, "ORF length (codons)", "number of ORFs per 25 codons")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())
