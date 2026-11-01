"""Three binomial distributions from the course. A: infants with chronic bronchitis among 20 families
whose parents have bronchitis, if each infant had the national risk of 5 %. B: low-birth-weight babies
among the 74 smoking mothers of the birthwt data, if smokers had the risk of the non-smokers (29/115).
C: neutrophils among 100 white blood cells (p = 0.6) with its normal approximation N(60, 24); the bars
of the normal range 50-75 are filled. All probabilities are computed exactly.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.3))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.86, wspace=0.28)


def bars(ax, n, p, hi, kmax):
    k = np.arange(0, kmax + 1)
    pmf = stats.binom.pmf(k, n, p)
    col = [P.fill("rna") if h else P.fill("neutral") for h in hi(k)]
    edg = [P.edge("rna") if h else P.edge("neutral") for h in hi(k)]
    ax.bar(k, pmf, width=0.8, color=col, edgecolor=edg, lw=0.6)
    return k, pmf


# A: bronchitis, X ~ Bin(20, 0.05), observed 3
bars(axs[0], 20, 0.05, lambda k: k >= 3, 8)
pa = stats.binom.sf(2, 20, 0.05)
axs[0].text(3.2, 0.25, f"observed 3 families\nP(X >= 3) = {pa:.3f}", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(axs[0], "families with an affected infant", "probability")
charts.title(axs[0], "A  Bin(20, 0.05)")

# B: low birth weight among smokers, X ~ Bin(74, 29/115), observed 30
p0 = 29 / 115
bars(axs[1], 74, p0, lambda k: k >= 30, 40)
pb = stats.binom.sf(29, 74, p0)
axs[1].annotate(f"observed 30\nP(X >= 30) = {pb:.4f}", (30, 0.004), xytext=(25, 0.07), fontsize=FT["tiny"],
                color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
axs[1].text(1, 0.095, f"mean np = {74 * p0:.1f}", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(axs[1], "low-birth-weight babies among 74", None)
charts.title(axs[1], "B  Bin(74, 0.252)")

# C: neutrophils, X ~ Bin(100, 0.6) and N(60, 24)
n, p = 100, 0.6
k = np.arange(35, 86)
pmf = stats.binom.pmf(k, n, p)
inside = (k >= 50) & (k <= 75)
axs[2].bar(k, pmf, width=0.85, color=[P.fill("dna") if i else P.fill("neutral") for i in inside],
           edgecolor=[P.edge("dna") if i else P.edge("neutral") for i in inside], lw=0.4)
x = np.linspace(35, 85, 400)
mu, sd = n * p, np.sqrt(n * p * (1 - p))
axs[2].plot(x, stats.norm.pdf(x, mu, sd), color=charts.line("enzyme"), lw=1.6, label="N(60, 24)")
exact = stats.binom.cdf(75, n, p) - stats.binom.cdf(49, n, p)
approx = stats.norm.cdf(75.5, mu, sd) - stats.norm.cdf(49.5, mu, sd)
axs[2].text(36, 0.075, f"P(50 <= X <= 75)\nexact {exact:.4f}\nnormal, corrected {approx:.4f}", fontsize=FT["tiny"],
            color=P.ink())
axs[2].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(axs[2], "neutrophils among 100 white cells", None)
charts.title(axs[2], "C  Bin(100, 0.6)")
