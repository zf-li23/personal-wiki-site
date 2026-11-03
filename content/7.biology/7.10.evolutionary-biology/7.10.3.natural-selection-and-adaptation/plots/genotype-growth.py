"""Natural selection as differential reproduction (Example 3.2.1). Two asexual genotypes of an annual
plant start with 10 individuals each; genotype A leaves 3 offspring per individual, genotype B leaves 4.
A: numbers of individuals (log scale); both grow, B faster. B: the frequency of B rises from 0.5 to 0.88
in 7 generations, following p_t = 1 / (1 + (w_A / w_B)^t (1 - p_0) / p_0) (Formula 3.2.1)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
t = np.arange(0, 8)
NA, NB = 10 * 3.0 ** t, 10 * 4.0 ** t
fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.3))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.17, top=0.88, wspace=0.3)
a.semilogy(t, NB, "o-", color=charts.line("positive"), lw=1.4, ms=4, label="genotype B ($w = 4$)")
a.semilogy(t, NA, "o-", color=charts.line("negative"), lw=1.4, ms=4, label="genotype A ($w = 3$)")
charts.style_axes(a, "generation $t$", "number of individuals")
charts.title(a, "A  Numbers")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
tc = np.linspace(0, 7, 200)
b.plot(tc, 1 / (1 + (3 / 4) ** tc), color=charts.line("positive"), lw=1.4)
b.plot(t, NB / (NA + NB), "o", color=charts.line("positive"), ms=4, label="genotype B")
b.plot(t, NA / (NA + NB), "o", color=charts.line("negative"), ms=4, label="genotype A")
b.plot(tc, 1 - 1 / (1 + (3 / 4) ** tc), color=charts.line("negative"), lw=1.4)
b.set_ylim(0, 1)
b.text(7, NB[-1] / (NA[-1] + NB[-1]) - 0.06, f"{NB[-1] / (NA[-1] + NB[-1]):.2f}", ha="right", va="top", fontsize=FT["tiny"],
       color=P.ink())
charts.style_axes(b, "generation $t$", "frequency")
charts.title(b, "B  Frequencies")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
