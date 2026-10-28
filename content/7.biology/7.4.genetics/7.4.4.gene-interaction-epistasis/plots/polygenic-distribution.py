"""Additive polygenic inheritance (Formula 4.6.1). For n = 1, 2, 3 and 6 unlinked additive loci, the number of
contributing alleles in the F2 of the n-fold heterozygote is Bin(2n, 1/2) (bars, as fractions of the range
0..2n). Curves: the same distribution blurred by an environmental normal deviation with standard deviation 0.5
allele-equivalents (mixture density), which turns the steps into a continuous curve."""
import numpy as np
from scipy import stats

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(26.0, 7.6)
for k, n in enumerate((1, 2, 3, 6)):
    a = charts.axes_at(ax, (1.4 + k * 6.3, 1.5, 5.0, 5.0))
    kk = np.arange(0, 2 * n + 1)
    pm = stats.binom.pmf(kk, 2 * n, 0.5)
    a.bar(kk, pm, width=0.7, color=P.fill("trna"), edgecolor=P.edge("trna"), lw=0.6)
    x = np.linspace(-1.5, 2 * n + 1.5, 400)
    dens = sum(p * stats.norm.pdf(x, m, 0.5) for m, p in zip(kk, pm))
    a.plot(x, dens, color=charts.line("dna"), lw=1.5)
    a.set_xlim(-1.2, 2 * n + 1.2)
    a.set_xticks(kk if n < 6 else kk[::2])
    charts.style_axes(a, "contributing alleles", "frequency" if k == 0 else None)
    ratio = ":".join(str(int(round(p * 4 ** n))) for p in pm) if n <= 3 else "Bin(12, 1/2)"
    charts.title(a, f"n = {n}:  {ratio}")
