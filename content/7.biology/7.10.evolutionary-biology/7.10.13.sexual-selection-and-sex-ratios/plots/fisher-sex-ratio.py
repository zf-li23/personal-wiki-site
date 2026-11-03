"""Fisher's principle (Theorem 13.3.1).

A: value of a son relative to a daughter, (1 - x)/x, against the population proportion of males x.
B: deterministic two-sex model with haploid inheritance and maternal control of the sex ratio. Resident
mothers produce a fraction 0.2 of sons, mutant mothers produce only sons (initial frequency 0.01 in both
sexes). Each female has K = 2 offspring; fathers are drawn at random from the males; an offspring
inherits the maternal or paternal allele with probability 1/2 each.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
x = np.linspace(0.08, 0.92, 300)
pa.plot(x, (1 - x) / x, color=C.line("dna"), lw=2.0)
pa.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.axvline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.set_yscale("log")
pa.set_xlim(0, 1)
pa.set_ylim(0.08, 12)
pa.set_yticks([0.1, 0.25, 0.5, 1, 2, 4, 10])
pa.set_yticklabels(["0.1", "0.25", "0.5", "1", "2", "4", "10"])
C.style_axes(pa, "proportion of males in the population x", "value of a son / value of a daughter")
pa.text(0.24, 9.0, "males rare:\nsons worth more", fontsize=FS["tiny"], color=P.ink(), va="top")
pa.text(0.62, 0.35, "males common:\ndaughters worth more", fontsize=FS["tiny"], color=P.ink(), va="top")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "The rarer sex is worth more", size="small", bold=True, ha="left")

m = np.array([0.2, 1.0])          # sex ratio produced by mothers of each genotype
F = np.array([0.99, 0.01])        # females by genotype
Mm = np.array([0.99, 0.01]) * 0.25
gens = 40
sr, freq = [], []
for g in range(gens + 1):
    sr.append(Mm.sum() / (Mm.sum() + F.sum()))
    freq.append((F[1] + Mm[1]) / (F.sum() + Mm.sum()))
    pm = Mm / Mm.sum()
    off = np.zeros(2)
    son = np.zeros(2)
    dau = np.zeros(2)
    for i in range(2):
        for j in range(2):
            n = 2 * F[i] * pm[j]
            for a in (i, j):
                son[i if False else a] += 0.5 * n * m[i]
                dau[a] += 0.5 * n * (1 - m[i])
    tot = son.sum() + dau.sum()
    Mm, F = son / tot, dau / tot
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
t = np.arange(gens + 1)
pb.plot(t, sr, color=P.ink(), lw=2.0, label="population sex ratio x")
pb.plot(t, freq, color=C.line("rna"), lw=1.8, ls=(0, (4, 2)), label="frequency of the sons-only allele")
pb.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, gens)
pb.set_ylim(0, 0.6)
C.style_axes(pb, "generation", "proportion")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "A sex-ratio mutant spreads until x = 1/2", size="small", bold=True, ha="left")
