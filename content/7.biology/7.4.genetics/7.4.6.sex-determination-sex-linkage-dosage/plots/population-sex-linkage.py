"""Quantitative consequences of sex linkage. A: recombination between a pseudoautosomal locus and sex in male
meiosis, if the obligatory crossover falls uniformly in PAR1: r = d / (2L) at distance d from the
pseudoautosomal boundary (L = 2.7 Mb). B: frequency of an X-linked recessive phenotype in males (q) and
females (q^2; carriers 2pq) under Hardy-Weinberg proportions (7.4.22); the female to male
ratio of affected individuals equals q."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.3)
a = axs[0]
L = 2.7
d = np.linspace(0, L, 100)
a.plot(d, d / (2 * L), color=charts.line("dna"), lw=2)
a.axhline(0.5, color=P.muted(), ls=":", lw=0.9)
a.text(0.1, 0.52, "free recombination", fontsize=FT["tiny"], color=P.muted())
a.set_xlim(0, L)
a.set_ylim(0, 0.6)
charts.style_axes(a, "distance from the pseudoautosomal boundary / Mb", "recombination with sex")
charts.title(a, "A  PAR1 in male meiosis")
a.text(2.65, 0.03, "telomere →", fontsize=FT["tiny"], color=P.muted(), ha="right")
b = axs[1]
q = np.logspace(-4, -0.5, 200)
b.loglog(q, q, color=charts.line("dna"), lw=2, label="affected males: $q$")
b.loglog(q, q**2, color=charts.line("receptor"), lw=2, label="affected females: $q^2$")
b.loglog(q, 2 * q * (1 - q), color=charts.line("receptor"), lw=1.4, ls="--", label="carrier females: $2pq$")
for qq, name in ((0.08, "red-green\ncolor blindness"), (1 / 5000, "hemophilia A")):
    b.axvline(qq, color=P.muted(), lw=0.7, ls=":")
    b.text(qq * 1.1, 2e-8, name, fontsize=FT["tiny"], color=P.muted(), ha="left", va="bottom")
b.set_ylim(1e-8, 1)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "allele frequency q", "frequency")
charts.title(b, "B  X-linked recessive trait in a population")
