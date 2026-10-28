"""Expected accuracy of a polygenic score. Lines: the Daetwyler formula R^2 = h^2 / (1 + M_e / (N h^2)) for
SNP heritability h^2 = 0.5 and 0.2 with M_e = 60 000 independent effective segments, and for h^2 = 0.5 with
M_e = 20 000. Dots: simulations (seed 1) with M_e independent standardized SNPs carrying normal effects; the
GWAS estimates are the true effects plus sampling noise of variance 1/N, and the score's R^2 in a new sample
is (beta-hat . beta)^2 / |beta-hat|^2. Accuracy approaches the heritability only when N greatly exceeds
M_e / h^2."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, gwas

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)
N = np.logspace(3.5, 7, 300)
fig, ax = plt.subplots(figsize=(6.8, 4.0))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.14, top=0.9)
for h2, Me, tok in ((0.5, 60000, "dna"), (0.2, 60000, "rna"), (0.5, 20000, "enzyme")):
    ax.semilogx(N, gwas.pgs_r2(N, h2, Me), color=charts.line(tok), lw=2, label=f"$h^2 = {h2}$, $M_e = {Me:,}$")
    beta = rng.normal(0, np.sqrt(h2 / Me), Me)
    for n in (1e4, 1e5, 1e6, 5e6):
        bh = beta + rng.normal(0, np.sqrt(1 / n), Me)
        r2 = (bh @ beta) ** 2 / (bh @ bh)
        ax.scatter([n], [r2], s=16, color=charts.line(tok), edgecolor=P.ink(), lw=0.5, zorder=4)
    ax.axhline(h2, color=charts.line(tok), lw=0.6, ls=":")
ax.set_ylim(0, 0.55)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "GWAS sample size $N$", "expected $R^2$ of the score")
charts.title(ax, "Polygenic score accuracy (dotted: the ceiling $h^2$)")
