# Coverage statistics of shotgun sequencing. A: with reads placed at random, the number covering a given base is
# Poisson distributed with mean c (the coverage); the bars are P(k) for c = 1, 5 and 30 and the dashed lines mark
# the fraction of bases left uncovered, exp(-c): 37 % at 1x, 0.7 % at 5x, 1e-13 at 30x. B: the fraction of the
# genome not covered, exp(-c), and the probability of calling a heterozygous site correctly when at least 3
# reads of each allele are required, computed from the binomial distribution of allele counts given k = Poisson(c)
# reads; it is this second requirement, not genome coverage, that sets the 30x standard for human resequencing.
import numpy as np
from scipy.stats import binom, poisson
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(19.0, 8.0)

a = C.axes_at(ax, (1.5, 1.4, 8.0, 5.2))
for c, tok, off in [(1, "protein", -0.3), (5, "enzyme", 0.0), (30, "receptor", 0.3)]:
    k = np.arange(0, 56)
    a.bar(k + off, poisson.pmf(k, c), width=0.3 if c < 30 else 0.3, color=P.fill(tok), edgecolor=C.line(tok), lw=0.5,
          label=f"c = {c}×, uncovered {np.exp(-c):.2g}")
a.set_xlim(-1, 55)
a.set_ylim(0, 0.42)
C.style_axes(a, "reads covering a base, k", "P(k)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.1, 7.9))
bio.label(ax, (0.6, 7.55), "Poisson coverage", size="normal", bold=True, ha="left")

b = C.axes_at(ax, (11.6, 1.4, 6.6, 5.2))
cs = np.linspace(1, 40, 200)
b.semilogy(cs, np.exp(-cs), color=C.line("dna"), lw=2.0, label="base not covered")
het = []
for c in cs:
    k = np.arange(0, 200)
    pk = poisson.pmf(k, c)
    # both alleles seen at least 3 times, given k reads and p = 1/2 per allele
    good = np.where(k >= 6, binom.cdf(k - 3, k, 0.5) - binom.cdf(2, k, 0.5), 0.0)
    het.append(np.sum(pk * (1 - good)))
b.semilogy(cs, np.array(het), color=C.line("negative"), lw=2.0, label="heterozygote missed (<3 reads of an allele)")
b.axvline(30, color=P.muted(), lw=0.9, ls=(0, (4, 3)))
b.text(29.2, 2e-2, "30× standard", rotation=90, ha="right", fontsize=bio.core.FONT["tiny"], color=P.muted())
b.set_xlim(1, 40)
b.set_ylim(1e-8, 1)
C.style_axes(b, "coverage c", "probability")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.93))
bio.panel(ax, "B", (10.3, 7.9))
bio.label(ax, (10.8, 7.55), "Why 30×?", size="normal", bold=True, ha="left")
