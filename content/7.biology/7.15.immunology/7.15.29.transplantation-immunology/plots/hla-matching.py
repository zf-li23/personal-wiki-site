# Probabilities behind donor selection (illustrative haplotype frequencies; Hardy-Weinberg proportions, 7.4).
# A: for a patient with n full siblings, probability that at least one sibling is HLA-identical, 1 - (3/4)^n
#    (each sibling inherits the same pair of parental haplotypes with probability 1/4).
# B: probability that an unrelated registry of N donors holds at least one genotype-matched donor, 1 - (1 - P)^N, where
#    P = 2 h1 h2 is the chance that one random donor carries the patient's two haplotypes (h1 != h2).
#    Common haplotypes (h = 3%), uncommon (h = 0.3%) and rare (h = 0.03%) pairs.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.6))
n = np.arange(1, 9)
axs[0].plot(n, 1 - 0.75 ** n, "o-", ms=4, color=charts.line("enzyme"), lw=1.5)
for k in (1, 2, 3, 4):
    axs[0].text(k, 1 - 0.75 ** k - 0.07, f"{1 - 0.75 ** k:.2f}", ha="center", fontsize=6.5, color=P.ink())
axs[0].set_ylim(0, 1.0)
charts.style_axes(axs[0], "number of siblings", "P(at least one HLA-identical sibling)")
charts.title(axs[0], "A")

N = np.logspace(2, 8, 200)
for h, tok in ((0.03, "protein"), (0.003, "enzyme"), (0.0003, "negative")):
    p = 2 * h * h
    axs[1].plot(N, 1 - (1 - p) ** N, color=charts.line(tok), lw=1.6, label=f"haplotypes at {100 * h:g}% each (P = {p:.1e})")
axs[1].set_xscale("log")
axs[1].set_ylim(0, 1.02)
axs[1].legend(frameon=False, fontsize=6.5, labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[1], "number of registered donors N", "P(at least one matched donor)")
charts.title(axs[1], "B")
fig.tight_layout()
