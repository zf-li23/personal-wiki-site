"""Deterministic selection at one locus (infinite population, random mating). A: a favored allele A with
fitnesses 1 + s (AA), 1 + hs (Aa), 1 (aa), s = 0.05, starting at p = 0.01. A dominant allele (h = 1) spreads
fast while rare but slowly near fixation, because the last a alleles hide in heterozygotes; a recessive
favored allele (h = 0) is almost invisible to selection while rare and needs hundreds of generations to take
off; the additive case (h = 1/2) is the symmetric logistic. B: decline of a deleterious recessive allele
from q = 0.1 under complete selection (s = 1: q_t = q_0/(1 + t q_0), dashed) and under s = 0.2: halving the
frequency of a rare recessive takes about 1/q generations."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def run(p0, w11, w12, w22, T):
    p = np.empty(T + 1)
    p[0] = p0
    for t in range(T):
        x = p[t]
        q = 1 - x
        wb = x * x * w11 + 2 * x * q * w12 + q * q * w22
        p[t + 1] = (x * x * w11 + x * q * w12) / wb
    return p


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.25)
a = axs[0]
s, T = 0.05, 800
t = np.arange(T + 1)
for h, lab, tok in ((1.0, "dominant, $h = 1$", "rna"), (0.5, "additive, $h = 1/2$", "enzyme"), (0.0, "recessive, $h = 0$", "dna")):
    a.plot(t, run(0.01, 1 + s, 1 + h * s, 1.0, T), color=charts.line(tok), lw=2, label=lab)
a.set_xlim(0, T)
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, "generation", "frequency $p$ of the favored allele")
charts.title(a, "A  Spread of a favored allele, $s = 0.05$")
b = axs[1]
T = 200
t = np.arange(T + 1)
q1 = 1 - run(0.9, 1, 1, 0.0, T)
q2 = 1 - run(0.9, 1, 1, 0.8, T)
b.plot(t, q1, color=charts.line("negative"), lw=2, label="lethal, $s = 1$")
b.plot(t, 0.1 / (1 + t * 0.1), color=P.ink(), lw=1, ls="--", label="$q_0/(1 + tq_0)$")
b.plot(t, q2, color=charts.line("protein"), lw=2, label="$s = 0.2$")
b.set_xlim(0, T)
b.set_ylim(0, 0.105)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "generation", "frequency $q$ of the recessive allele")
charts.title(b, "B  Selection against a recessive allele")
