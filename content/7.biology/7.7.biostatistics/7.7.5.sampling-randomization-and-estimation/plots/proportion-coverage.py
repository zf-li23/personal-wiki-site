"""Actual coverage of three nominal 95 % confidence intervals for a binomial proportion with n = 30,
computed exactly (sum of binomial probabilities of all outcomes whose interval covers p) on a fine grid
of true proportions p. The Wald interval p_hat +/- 1.96 sqrt(p_hat (1 - p_hat) / n) falls far below 95 %
near 0 and 1 and oscillates; the Wilson score interval stays close to 95 %; the Clopper-Pearson exact
interval never falls below 95 % but is conservative.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
n = 30
z = stats.norm.isf(0.025)
k = np.arange(n + 1)
ph = k / n
wald = (ph - z * np.sqrt(ph * (1 - ph) / n), ph + z * np.sqrt(ph * (1 - ph) / n))
c = (ph + z * z / (2 * n)) / (1 + z * z / n)
h = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / (1 + z * z / n)
wilson = (c - h, c + h)
cp_lo = np.where(k == 0, 0.0, stats.beta.ppf(0.025, np.maximum(k, 1), n - k + 1))
cp_hi = np.where(k == n, 1.0, stats.beta.ppf(0.975, k + 1, np.maximum(n - k, 1)))
cp = (cp_lo, cp_hi)

p = np.linspace(0.005, 0.995, 991)
fig, ax = plt.subplots(figsize=(10.0, 3.4))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.90)
for (lo, hi), name, tok, lw in [(wald, "Wald", "rna", 1.0), (wilson, "Wilson", "dna", 1.3), (cp, "Clopper-Pearson", "enzyme", 1.3)]:
    cov = np.array([np.sum(stats.binom.pmf(k, n, pp) * ((lo <= pp) & (pp <= hi))) for pp in p])
    ax.plot(p, cov, color=charts.line(tok), lw=lw, label=f"{name} (mean coverage {cov.mean():.3f})")
ax.axhline(0.95, color=P.ink(), lw=0.8, ls="--")
ax.set_ylim(0.6, 1.005)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower center")
charts.style_axes(ax, "true proportion p", "actual coverage")
charts.title(ax, "Coverage of nominal 95 % intervals for a proportion, n = 30")
