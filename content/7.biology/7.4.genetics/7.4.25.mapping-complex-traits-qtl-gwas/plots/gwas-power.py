"""Power of a genome-wide association test (1 df, significance 5e-8) for a quantitative trait, as a function
of sample size, for variants explaining a fraction q^2 = 2pq beta^2 / sigma^2 of the trait variance (the
noncentrality is N q^2). A variant explaining 0.1 % of the variance needs about 40 000 individuals for 80 %
power, one explaining 0.01 % about 400 000. Dashed: the same variant tested through a tag SNP with r^2 = 0.5,
which halves the effective sample size."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, gwas

P = bio.P
FT = bio.core.FONT
N = np.logspace(3, 6.7, 300)
fig, ax = plt.subplots(figsize=(6.8, 4.0))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.14, top=0.9)
for q2, tok in ((0.005, "rna"), (0.001, "enzyme"), (0.0002, "dna"), (0.0001, "protein")):
    beta = np.sqrt(q2 / (2 * 0.3 * 0.7))
    ax.semilogx(N, gwas.power_quantitative(N, 0.3, beta), color=charts.line(tok), lw=2, label=f"$q^2 = {q2 * 100:g}\\%$")
    ax.semilogx(N, gwas.power_quantitative(N * 0.5, 0.3, beta), color=charts.line(tok), lw=1.1, ls="--")
ax.axhline(0.8, color=P.muted(), lw=0.8, ls=":")
ax.text(1.1e3, 0.82, "80% power", fontsize=FT["tiny"], color=P.muted())
ax.set_ylim(0, 1.02)
ax.set_xlim(1e3, 5e6)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right", title="variance explained",
          title_fontsize=FT["tiny"])
charts.style_axes(ax, "sample size $N$", "power at $p < 5 \\times 10^{-8}$")
charts.title(ax, "Sample size needed for GWAS discovery")
