"""Genotypic values at one locus and their decomposition (Falconer's scale), for homozygotes at -a and +a
(a = 1), heterozygote at d = 0.6 and allele frequency p = 0.3 of the increasing allele A2. The genotypic
values (large dots, area proportional to genotype frequency) are regressed on the number of A2 alleles with
weights equal to the Hardy-Weinberg frequencies: the slope of the least-squares line is the average effect
alpha = a + d(q - p) = 1.24, the fitted values are the breeding values, and the vertical deviations of the
genotypic values from the line are the dominance deviations. V_A = 2pq alpha^2 is the variance of the
fitted values, V_D = (2pqd)^2 that of the deviations."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
a, d, p = 1.0, 0.6, 0.3
q = 1 - p
k = np.array([0, 1, 2])
G = np.array([-a, d, a])
f = np.array([q * q, 2 * p * q, p * p])
M = (f * G).sum()
alpha = a + d * (q - p)
kbar = (f * k).sum()
fit = M + alpha * (k - kbar)
fig, ax = plt.subplots(figsize=(6.6, 4.2))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.14, top=0.9)
xx = np.linspace(-0.3, 2.3, 10)
ax.plot(xx, M + alpha * (xx - kbar), color=charts.line("dna"), lw=1.8, label=f"slope $\\alpha = {alpha:.2f}$ (breeding values)")
for ki, gi, fi, bi in zip(k, G, f, fit):
    ax.plot([ki, ki], [bi, gi], color=charts.line("negative"), lw=1.2, ls="--")
    ax.scatter([ki], [gi], s=900 * fi, color=P.fill("rna"), edgecolor=P.edge("rna"), zorder=4)
    ax.scatter([ki], [bi], s=18, color=charts.line("dna"), zorder=5)
ax.axhline(0, color=P.muted(), lw=0.6, ls=":")
ax.axhline(M, color=P.muted(), lw=0.8)
ax.text(2.28, M + 0.03, f"mean $M = {M:.3f}$", ha="right", va="bottom", fontsize=FT["tiny"], color=P.muted())
ax.text(1.05, (d + fit[1]) / 2, "dominance\ndeviation", fontsize=FT["tiny"], color=charts.line("negative"), va="center")
for ki, lab in zip(k, ("$A_1A_1$: $-a$", "$A_1A_2$: $d$", "$A_2A_2$: $+a$")):
    ax.text(ki, G[ki] + 0.17 if ki != 0 else G[ki] - 0.25, lab, ha="center", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks(k, ["0", "1", "2"])
ax.set_xlim(-0.3, 2.3)
ax.set_ylim(-1.5, 2.0)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "number of $A_2$ alleles", "genotypic value")
charts.title(ax, f"Average effect and dominance deviation ($a = 1$, $d = {d}$, $p = {p}$)")
