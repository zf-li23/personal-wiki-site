"""Fisher's exact test for hypertension and low birth weight in birthwt (12 hypertensive mothers, 7 low
birth weight; 59 low among all 189). With all margins fixed, the number of low-birth-weight infants among
the 12 hypertensive mothers follows a hypergeometric distribution under H0 (bars; expected 3.75). The
two-sided p-value sums the probabilities of all tables no more probable than the observed one (shaded):
p = 0.052. The uncorrected Pearson chi-square gives 0.036, the Yates-corrected one 0.076.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
N, K, n, obs = 189, 59, 12, 7
x = np.arange(0, n + 1)
pm = stats.hypergeom.pmf(x, N, K, n)
extreme = pm <= pm[obs] * (1 + 1e-7)
fig, ax = plt.subplots(figsize=(7.4, 3.3))
fig.subplots_adjust(left=0.1, right=0.98, bottom=0.16, top=0.88)
ax.bar(x[~extreme], pm[~extreme], 0.75, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6)
ax.bar(x[extreme], pm[extreme], 0.75, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.6)
ax.axvline(n * K / N, color=P.muted(), lw=0.8, ls=":")
ax.annotate("observed 7", (obs, pm[obs]), (obs + 1.2, pm[obs] + 0.08), fontsize=FT["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.7))
ax.text(8.8, 0.2, f"two-sided p = {pm[extreme].sum():.3f}", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks(x)
charts.style_axes(ax, "low-birth-weight infants among the 12 hypertensive mothers", "probability under H0")
charts.title(ax, "Hypergeometric null distribution, margins fixed")
