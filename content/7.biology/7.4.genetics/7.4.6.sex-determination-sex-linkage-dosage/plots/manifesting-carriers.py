"""When does a carrier of an X-linked recessive disease show it? If a tissue descends from n precursor cells
that inactivated their X chromosomes independently (Proposition 17.1.1 of 7.3.17), the fraction F of cells
expressing the normal allele satisfies nF ~ Bin(n, 1/2). A: probability that F falls below a threshold t at
which the tissue fails, as a function of n. B: the same with a selective disadvantage: cells expressing the
mutant allele grow to a fraction (1 - s) of the size of normal clones (s = 0.3), which pushes F up and
protects carriers."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8), sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.12)
ns = np.arange(2, 81)
for ax, s, title in ((axs[0], 0.0, "A  Random inactivation only"), (axs[1], 0.3, "B  Selection against mutant clones (s = 0.3)")):
    for t, tok in ((0.1, "dna"), (0.2, "enzyme"), (0.3, "negative")):
        pr = []
        for n in ns:
            k = np.arange(n + 1)  # precursors with the normal X active
            F = k / (k + (n - k) * (1 - s))
            pr.append(binom.pmf(k, n, 0.5)[F < t].sum())
        ax.semilogy(ns, np.maximum(pr, 1e-12), "o-", color=charts.line(tok), lw=0.8, ms=2.5, label=f"threshold t = {t:g}")
    ax.set_ylim(1e-6, 1)
    charts.style_axes(ax, "number of precursor cells n", "P(F < t)" if s == 0 else None)
    charts.title(ax, title)
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
