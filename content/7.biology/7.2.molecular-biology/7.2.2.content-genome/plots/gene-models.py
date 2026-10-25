# Two human genes on the same scale (coordinates in bp from the transcription start site).
# HBB (beta-globin): three exons (142, 223 and 261 bp) and two introns (130 and 850 bp); the 626-nt mRNA
# carries a 50-nt 5' UTR, a 444-nt coding sequence (146 amino acids after removal of Met, plus the stop
# codon) and a 132-nt 3' UTR. A replication-dependent histone H4 gene: a single exon, a 312-bp coding
# sequence (102 amino acids after removal of Met, plus the stop codon) and short untranslated regions
# (lengths drawn approximately); its mRNA ends in a stem-loop instead of a poly(A) tail.
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(16, 6.2)
sc = 0.0068
g = G.gene(ax, 1.9, 4.4, [(0, 142), (272, 495), (1345, 1606)], cds=(50, 1474), scale=sc, promoter=(-110, -20),
           codons=("ATG", "TAA"), polya_signal=1586, name="HBB", flank=150, scale_bar=None, intron="hat")
X = g["x"]
for (a, b), t in zip(((142, 272), (495, 1345)), ("Intron 1\n130 bp", "Intron 2\n850 bp")):
    bio.label(ax, ((X(a) + X(b)) / 2, 4.4 - 0.4), t, size="small", va="top")
h = G.gene(ax, 1.9, 1.7, [(0, 400)], cds=(30, 342), scale=sc, promoter=(-110, -20), codons=("ATG", "TAA"),
           name="H4", flank=150, scale_bar=200, intron="hat")
bio.label(ax, (h["x"](560) + 0.15, 1.7), "stem-loop, no poly(A) signal", size="tiny", color=bio.P.muted(), ha="left")
