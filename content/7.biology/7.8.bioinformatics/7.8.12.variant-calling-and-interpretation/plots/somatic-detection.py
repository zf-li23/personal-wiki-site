# Detecting a somatic variant depends on its allele fraction, not only on depth. A: the variant-allele
# fraction expected from Formula 12.7.1, f = p m / (p C_T + 2(1 - p)), for a heterozygous somatic
# mutation (m = 1) in a subclone that makes up a fraction p of the tumour cells, with the tumour locus
# diploid (C_T = 2, solid), hemizygous after loss of the other allele (C_T = 1, dashed) and duplicated
# with two mutant copies (m = 2, C_T = 3, dotted). B: the probability of seeing at least five supporting
# reads, 1 - P(Bin(n, f) <= 4), against depth, for allele fractions 0.02, 0.05, 0.10 and 0.25; the grey
# line is the probability that five or more reads carry the same wrong base by chance at Q30
# (f = 0.001/3): 3e-10 at depth 100 and 3e-5 at depth 1000, so deep sequencing needs either a higher
# threshold, error models per context, or molecular identifiers (7.8.9).
import numpy as np
from scipy.stats import binom
import wikibio as bio
from wikibio import charts as C

fig, ax = bio.canvas(24.0, 9.5)
a = C.axes_at(ax, (2.2, 1.5, 9.2, 7.0))
p = np.linspace(0.02, 1.0, 200)
for m, CT, style, lab in ((1, 2, "-", "heterozygous, diploid (m = 1, C = 2)"),
                          (1, 1, "--", "after loss of the other allele (m = 1, C = 1)"),
                          (2, 3, ":", "duplicated mutant allele (m = 2, C = 3)")):
    a.plot(p, p * m / (p * CT + 2 * (1 - p)), style, color=C.line("dna"), lw=1.6, label=lab)
a.axhline(0.05, color=C.line("neutral"), lw=0.7, ls=":")
C.style_axes(a, "fraction p of cells carrying the mutation", "variant-allele fraction f")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink(), loc="upper left")
C.title(a, "A  Allele fraction from purity and copy number")
b = C.axes_at(ax, (14.6, 1.5, 8.8, 7.0))
n = np.arange(10, 1201)
for f, tok in ((0.25, "positive"), (0.10, "dna"), (0.05, "rna"), (0.02, "negative")):
    b.plot(n, binom.sf(4, n, f), color=C.line(tok), lw=1.5, label=f"f = {f}")
b.plot(n, binom.sf(4, n, 1e-3 / 3), color=C.line("neutral"), lw=1.2, ls="--",
       label="same wrong base at Q30")
b.set_yscale("log")
b.set_ylim(1e-12, 2)
C.style_axes(b, "depth", "P(at least 5 supporting reads)")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink(), loc="lower right")
C.title(b, "B  Power of a five-read threshold")
for f in (0.02, 0.05, 0.10, 0.25):
    print(f, [round(float(binom.sf(4, nn, f)), 4) for nn in (100, 300, 1000)])
print("chance", float(binom.sf(4, 1000, 1e-3 / 3)))
