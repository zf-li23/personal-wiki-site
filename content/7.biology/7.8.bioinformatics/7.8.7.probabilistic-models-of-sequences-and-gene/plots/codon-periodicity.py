# The three-base periodicity of protein-coding DNA in Escherichia coli K-12. A: base composition at the
# three codon positions of the 4297 annotated protein-coding genes (codon position 1 is G-rich, position 2
# T- and A-rich, position 3 reflects codon choice). B: power spectrum of the four base indicator sequences,
# averaged over 360-bp windows from every fourth gene (2252 windows, gray: 746 windows from intergenic
# regions longer than 360 bp), normalized by its median: coding windows have a peak at frequency 1/3
# (period 3 bp) about 4.7 times the background level, intergenic windows a weaker one (2.3), contributed
# by unannotated or overlapping coding fragments (spectrum.csv).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
POS = np.array([[0.2519, 0.2426, 0.3480, 0.1575], [0.2889, 0.2258, 0.1809, 0.3043],
                [0.1802, 0.2686, 0.2918, 0.2593]])
d = np.genfromtxt("spectrum.csv", delimiter=",", names=True)
fig, ax = bio.canvas(22.0, 8.6)
a = C.axes_at(ax, (1.8, 1.5, 6.4, 6.4))
w = 0.2
for j, (b, tok) in enumerate(zip("ACGT", ["positive", "dna", "rna", "negative"])):
    a.bar(np.arange(3) + (j - 1.5) * w, POS[:, j], width=w, color=bio.P.NUCLEOTIDE[b], label=b, lw=0)
a.axhline(0.25, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
a.set_xticks(range(3))
a.set_xticklabels(["position 1", "position 2", "position 3"])
a.set_ylim(0, 0.4)
C.style_axes(a, "codon position", "base frequency")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), ncol=4, loc="upper center")
b = C.axes_at(ax, (11.0, 1.5, 10.0, 6.4))
f = d["freq"][1:]
for col, tok, lab in [("intergenic", "neutral", "intergenic"), ("coding", "dna", "coding")]:
    y = d[col][1:]
    b.plot(f, y / np.median(y), color=C.line(tok), lw=1.0, label=lab)
b.axvline(1 / 3, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
b.text(1 / 3 + 0.005, 4.5, "1/3", fontsize=bio.core.FONT["tiny"], color=P.muted())
b.set_xlim(0, 0.5)
C.style_axes(b, "frequency (cycles per base)", "power / median")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())
bio.panel(ax, "A", (0.2, 8.3))
bio.panel(ax, "B", (9.6, 8.3))
