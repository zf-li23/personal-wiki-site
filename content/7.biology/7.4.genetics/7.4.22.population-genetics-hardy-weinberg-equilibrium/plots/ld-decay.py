"""Decay of linkage disequilibrium under random mating, D_t = (1 - r)^t D_0. A: unlinked loci (r = 1/2)
lose half of their disequilibrium every generation, while tightly linked loci (r = 0.001, about 0.1 cM)
keep most of it for hundreds of generations. B: why LD dates mutations: the probability that the ancestral
haplotype survives unbroken over a distance of d morgans on one side of a mutation that is g generations
old is e^(-gd); the expected length of the shared haplotype around the mutation (both sides) is 2/g
morgans, about 2 cM after 100 generations."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.8))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.9, wspace=0.25)
a = axs[0]
t = np.arange(0, 1001)
for r, tok in ((0.5, "negative"), (0.1, "rna"), (0.01, "enzyme"), (0.001, "dna")):
    a.semilogx(t[1:], (1 - r) ** t[1:], color=charts.line(tok), lw=2, label=f"$r = {r:g}$")
    if r < 0.5:
        th = np.log(0.5) / np.log(1 - r)
        a.scatter([th], [0.5], s=14, color=charts.line(tok), zorder=4)
a.axhline(0.5, color=P.muted(), lw=0.8, ls=":")
a.text(1.2, 0.52, "half-life $\\ln 2/r$", fontsize=FT["tiny"], color=P.muted(), va="bottom")
a.set_ylim(0, 1.02)
a.set_xlim(1, 1000)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "generations $t$", "$D_t / D_0$")
charts.title(a, "A  LD decays at rate $r$")
b = axs[1]
d = np.linspace(0, 10, 400)  # cM
for g, tok in ((20, "dna"), (100, "enzyme"), (500, "rna")):
    b.plot(d, np.exp(-g * d / 100), color=charts.line(tok), lw=2, label=f"$g = {g}$: mean span $2/g$ = {200 / g:g} cM")
b.set_xlim(0, 10)
b.set_ylim(0, 1.02)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "distance from the mutation $d$ / cM", "P(ancestral haplotype intact)")
charts.title(b, "B  Old mutations sit on short haplotypes")
