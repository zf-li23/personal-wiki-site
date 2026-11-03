"""Cumulative selection (Section 3.4.3). A haploid population in which a favorable allele at each of
20 freely recombining loci starts at frequency 0.05 and multiplies fitness by 1 + s, with s = 0.1
(linkage equilibrium assumed). A: the frequency of the favorable allele at each locus,
p_t = p_0 e^{st} / (1 - p_0 + p_0 e^{st}). B: the frequency of the genotype carrying all 20 favorable
alleles, p_t^20, on a log scale: initially about 10^-26, a combination that would never be found by
sampling, it makes up more than half of the population within about 65 generations (s = 0.1), because selection raises the
frequencies of the individually favorable alleles one generation at a time."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
L, p0 = 20, 0.05
t = np.linspace(0, 100, 400)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.3))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.17, top=0.88, wspace=0.3)
for s, tok in ((0.05, "dna2"), (0.1, "dna"), (0.2, "enzyme")):
    e = np.exp(s * t)
    p = p0 * e / (1 - p0 + p0 * e)
    a.plot(t, p, color=charts.line(tok), lw=1.5, label=f"$s = {s}$")
    b.semilogy(t, p ** L, color=charts.line(tok), lw=1.5, label=f"$s = {s}$")
b.axhline(p0 ** L, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
b.text(100, p0 ** L * 8, "initial frequency $0.05^{20}$", ha="right", va="bottom", fontsize=FT["tiny"], color=P.muted())
b.axhline(1e-9, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
b.text(100, 2e-9, "one in a billion", ha="right", va="bottom", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(a, "generation $t$", "frequency of a favorable allele")
charts.title(a, "A  One locus")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "generation $t$", "frequency of the best genotype")
charts.title(b, "B  All 20 favorable alleles together")
b.set_ylim(1e-28, 3)
