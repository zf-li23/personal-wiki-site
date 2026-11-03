"""Background selection along a hypothetical 30 Mb chromosome. A: local recombination rate (cM/Mb), low near
the telomeres and around a centromere at 15 Mb. B: B(x) = exp(-sum_j u_j hs / (hs + r(x, j))^2) (Eq. (8.5)),
with deleterious mutations at rate u per bp at every site (density uniform), heterozygous effect hs = 0.02,
and r(x, j) the map distance (in Morgans, capped at 0.5) between the neutral site and selected site j;
u = 2e-9 (solid) and 4e-9 (dashed) per bp per generation, sites summed in 10 kb bins."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
Lmb = 30
xb = np.arange(0, Lmb, 0.01) + 0.005                  # 10 kb bins (Mb)
rate = 2.5 * (1 - np.exp(-xb / 2)) * (1 - np.exp(-(Lmb - xb) / 2)) * (1 - 0.95 * np.exp(-((xb - 15) / 1.5) ** 2))
M = np.concatenate([[0], np.cumsum(rate * 0.01)]) / 100   # Morgans
Mmid = (M[:-1] + M[1:]) / 2
fig, (a, b) = plt.subplots(2, 1, figsize=(8.0, 4.8), sharex=True, gridspec_kw={"height_ratios": [0.7, 1]})
fig.subplots_adjust(left=0.1, right=0.97, bottom=0.11, top=0.93, hspace=0.25)
a.plot(xb, rate, color=charts.line("dna"), lw=1.6)
a.set_ylim(0, 3)
charts.style_axes(a, None, "cM / Mb")
charts.title(a, "A  Recombination rate")
hs = 0.02
for u, ls in ((2e-9, "-"), (4e-9, "--")):
    uj = u * 1e4
    B = []
    for k in range(len(xb)):
        r = np.minimum(np.abs(Mmid - Mmid[k]), 0.5)
        B.append(np.exp(-np.sum(uj * hs / (hs + r) ** 2)))
    b.plot(xb, B, color=charts.line("rna"), lw=1.6, ls=ls, label=f"$u = {u * 1e9:.0f}\\times10^{{-9}}$ per bp")
b.set_ylim(0, 1.02)
b.set_xlim(0, Lmb)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(b, "position (Mb)", "$B = N_{\\mathrm{e}}/N$")
charts.title(b, "B  Reduction of neutral diversity")
