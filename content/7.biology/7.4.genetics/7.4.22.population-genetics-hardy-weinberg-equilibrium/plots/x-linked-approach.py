"""Approach to equilibrium at an X-linked locus. A population founded with the allele at frequency
0.3 in females and absent in males: each generation males inherit the frequency of the previous females,
q_m' = q_f, and females the mean of both sexes, q_f' = (q_m + q_f)/2. The difference between the sexes
changes sign and halves every generation, while the weighted mean (2 q_f + q_m)/3 = 0.2 stays constant."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
T = 10
qm, qf = [0.0], [0.3]
for _ in range(T):
    qm.append(qf[-1])
    qf.append((qm[-2] + qf[-1]) / 2)
t = np.arange(T + 1)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.15, top=0.9)
ax.plot(t, qf, "o-", color=charts.line("rna"), lw=1.8, ms=4, label="females $q_f$")
ax.plot(t, qm, "s-", color=charts.line("dna"), lw=1.8, ms=4, label="males $q_m$")
ax.axhline(0.2, color=P.muted(), lw=0.9, ls="--")
ax.text(T, 0.205, "$\\bar q = (2q_f + q_m)/3 = 0.2$", ha="right", va="bottom", fontsize=FT["tiny"], color=P.muted())
ax.set_ylim(-0.01, 0.32)
ax.set_xticks(t)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "generation", "allele frequency")
charts.title(ax, "Oscillating approach at an X-linked locus")
