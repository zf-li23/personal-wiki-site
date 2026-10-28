"""The Wahlund effect. A: two subpopulations of equal size, each in Hardy-Weinberg proportions, with allele
frequencies p = 0.2 and p = 0.8. Pooled, the sample has the genotype frequencies 0.34, 0.32, 0.34, whereas
Hardy-Weinberg proportions for the pooled allele frequency 0.5 would be 0.25, 0.50, 0.25: heterozygotes are
missing by 2 Var(p) = 0.18, and F_ST = Var(p)/(p(1 - p)) = 0.36. B: the heterozygote deficit of a pooled
sample of two equal subpopulations with frequencies 0.5 - x and 0.5 + x."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.8), gridspec_kw={"width_ratios": [1.5, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.88, wspace=0.25)
a = axs[0]


def hw(p):
    return np.array([p * p, 2 * p * (1 - p), (1 - p) ** 2])


groups = [("subpop. 1\n$p = 0.2$", hw(0.2)), ("subpop. 2\n$p = 0.8$", hw(0.8)),
          ("pooled\nobserved", (hw(0.2) + hw(0.8)) / 2), ("pooled, HW\nexpected", hw(0.5))]
w = 0.25
toks = ("dna", "enzyme", "rna")
for k, (lab, fr) in enumerate(groups):
    for j in range(3):
        a.bar(k + (j - 1) * w, fr[j], w * 0.92, color=P.fill(toks[j]), edgecolor=P.edge(toks[j]), lw=0.8,
              label=("$AA$", "$Aa$", "$aa$")[j] if k == 0 else None)
        a.text(k + (j - 1) * w, fr[j] + 0.01, f"{fr[j]:.2f}", ha="center", va="bottom", fontsize=FT["tiny"] * 0.9,
               color=P.ink())
a.set_xticks(range(4), [g[0] for g in groups])
a.set_ylim(0, 0.75)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), ncol=3, loc="upper left")
charts.style_axes(a, None, "genotype frequency")
charts.title(a, "A  Pooling hides heterozygotes")
b = axs[1]
x = np.linspace(0, 0.5, 200)
b.plot(x, 2 * x**2, color=charts.line("negative"), lw=2, label="deficit $2\\operatorname{Var}(p) = 2x^2$")
b.plot(x, 4 * x**2, color=charts.line("dna"), lw=2, label="$F_{\\mathrm{ST}} = 4x^2$")
b.scatter([0.3, 0.3], [0.18, 0.36], s=16, color=P.ink(), zorder=4)
b.set_xlim(0, 0.5)
b.set_ylim(0, 1)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "half-difference $x$ of allele frequencies", None)
charts.title(b, "B  Deficit grows with divergence")
