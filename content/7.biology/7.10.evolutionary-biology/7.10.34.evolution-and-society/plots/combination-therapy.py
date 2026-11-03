"""Why combination therapy delays resistance (Section 34.6.5). If resistance to each drug arises by a
single mutation with probability 10^-8 per cell division, the probability that a population of N
pathogen cells already contains at least one cell resistant to the treatment is 1 - exp(-N u), with
u = 10^-8 for one drug and u = 10^-16 for two drugs requiring independent mutations. The shaded band
marks an illustrative range for the number of bacteria in a serious infection (10^9 to 10^11 cells). Combination therapy works because no pre-existing variant is resistant
to all drugs at once."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
N = np.logspace(4, 18, 300)
fig, ax = plt.subplots(figsize=(6.4, 3.4))
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.17, top=0.95)
for u, tok, lab in ((1e-8, "rna", "one drug"), (1e-16, "dna", "two drugs"), (1e-24, "plant", "three drugs")):
    ax.semilogx(N, 1 - np.exp(-N * u), color=charts.line(tok), lw=2, label=lab)
ax.axvspan(1e9, 1e11, color=P.fill("neutral"), alpha=0.5, lw=0)
ax.text(1e10, 0.55, "bacterial\ninfection", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(1e4, 1e18)
charts.style_axes(ax, "pathogen population size, N", "P(resistant cell present)")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
