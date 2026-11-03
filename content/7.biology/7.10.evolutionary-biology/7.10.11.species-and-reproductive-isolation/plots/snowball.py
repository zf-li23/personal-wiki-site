"""The Dobzhansky-Muller model and the snowball effect.
A: two-locus scheme. An ancestral population aabb splits; allele A is fixed in one lineage and B in the other.
Every genotype that ever exists in either lineage is fit, but the F1 hybrid AaBb combines A and B, which
have never been tested together by selection.
B: simulation of the accumulation of incompatibilities (seed 0, 300 replicate pairs of lineages): substitutions
occur alternately in the two lineages; each new derived allele is incompatible with probability
p = 0.002 with each derived allele of the other lineage and with each ancestral allele that the other
lineage still carries at loci where its own lineage has substituted (the pairs that were never tested
together). Dots: mean number of hybrid incompatibilities against the total number K of substitutions;
line: Orr's (1995) expectation p K (K - 1) / 2; dashed: a linear increase with the same value at K = 20.
C: probability that a hybrid is free of incompatibilities, exp(-p K (K - 1) / 2), against K: isolation
appears suddenly after a long period of compatibility."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.9), gridspec_kw={"width_ratios": [1.15, 1, 1]})
fig.subplots_adjust(left=0.03, right=0.98, bottom=0.15, top=0.9, wspace=0.3)

a = axs[0]
a.set_xlim(0, 10)
a.set_ylim(0, 10)
a.axis("off")


def gbox(x, y, text, tok):
    bio.box(a, (x, y), 2.4, 0.9, tok, text=text, size="small", italic=True)


gbox(5, 9, "aabb", "neutral")
gbox(2.2, 6.6, "Aabb", "dna")
gbox(7.8, 6.6, "aaBb", "rna")
gbox(2.2, 4.4, "AAbb", "dna")
gbox(7.8, 4.4, "aaBB", "rna")
gbox(5, 1.5, "AaBb", "negative")
for p0, p1 in (((4.2, 8.6), (2.8, 7.1)), ((5.8, 8.6), (7.2, 7.1)), ((2.2, 6.1), (2.2, 4.9)), ((7.8, 6.1), (7.8, 4.9)),
               ((2.6, 3.9), (4.2, 2.0)), ((7.4, 3.9), (5.8, 2.0))):
    bio.arrow(a, p0, p1, kind="process", head=0.18)
bio.label(a, (5, 6.6), "geographic\nseparation", size="tiny", color=P.muted())
bio.label(a, (5, 0.45), "F$_1$ hybrid: A and B meet for the first time", size="tiny")
charts.title(a, "A  Dobzhansky–Muller incompatibility")

rng = np.random.default_rng(0)
Kmax, p, reps = 60, 0.002, 300
counts = np.zeros((reps, Kmax + 1))
for r in range(reps):
    n1 = n2 = 0
    inc = 0
    for k in range(1, Kmax + 1):
        if k % 2:
            # new substitution in lineage 1: untested with all derived alleles of lineage 2 and the
            # ancestral alleles of lineage 2 at the n1 loci already substituted in lineage 1
            inc += rng.binomial(n2 + n1, p)
            n1 += 1
        else:
            inc += rng.binomial(n1 + n2, p)
            n2 += 1
        counts[r, k] = inc
K = np.arange(Kmax + 1)
b = axs[1]
b.scatter(K[::3], counts.mean(0)[::3], s=14, color=charts.line("dna"), zorder=3, label="simulation")
b.plot(K, p * K * (K - 1) / 2, color=charts.line("rna"), lw=2, label="$pK(K-1)/2$")
b.plot(K, p * 20 * 19 / 2 / 20 * K, color=P.muted(), lw=1.2, ls="--", label="linear")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "substitutions $K$", "incompatibilities")
charts.title(b, "B  The snowball effect")

c = axs[2]
for pp, tok in ((0.0005, "plant"), (0.002, "dna"), (0.01, "rna")):
    c.plot(K, np.exp(-pp * K * (K - 1) / 2), color=charts.line(tok), lw=2, label=f"$p = {pp:g}$")
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
c.set_ylim(0, 1.03)
charts.style_axes(c, "substitutions $K$", "P(hybrid compatible)")
charts.title(c, "C  Isolation arises abruptly")
