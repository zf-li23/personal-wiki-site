"""Exact coverage of nominal 95% Wald, Wilson, Agresti-Coull and Clopper-Pearson intervals for a
binomial proportion with n = 20, as a function of the true p (all outcomes summed exactly)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n, alpha = 20, 0.05
z = stats.norm.isf(alpha / 2)
xs = np.arange(n + 1)
ph = xs / n

wald = (ph - z * np.sqrt(ph * (1 - ph) / n), ph + z * np.sqrt(ph * (1 - ph) / n))
center = (ph + z**2 / (2 * n)) / (1 + z**2 / n)
half = z / (1 + z**2 / n) * np.sqrt(ph * (1 - ph) / n + z**2 / (4 * n**2))
wilson = (center - half, center + half)
nt = n + z**2
pt = (xs + z**2 / 2) / nt
ac = (pt - z * np.sqrt(pt * (1 - pt) / nt), pt + z * np.sqrt(pt * (1 - pt) / nt))
cp_lo = np.where(xs == 0, 0.0, stats.beta.ppf(alpha / 2, np.maximum(xs, 1), n - xs + 1))
cp_hi = np.where(xs == n, 1.0, stats.beta.ppf(1 - alpha / 2, xs + 1, np.maximum(n - xs, 1)))
methods = {
    "Wald": (wald, "C3"),
    "Wilson": (wilson, "C0"),
    "Agresti–Coull": (ac, "C2"),
    "Clopper–Pearson": ((cp_lo, cp_hi), "C1"),
}

grid = np.linspace(0.005, 0.995, 991)
fig, ax = plt.subplots(figsize=(8.2, 4.6))
for label, ((lo, hi), color) in methods.items():
    cover = [stats.binom.pmf(xs, n, p)[(lo <= p) & (p <= hi)].sum() for p in grid]
    ax.plot(grid, cover, color=color, lw=1.2, label=label)
ax.axhline(1 - alpha, color="0.3", ls="--", lw=1)
ax.set_xlim(0, 1)
ax.set_ylim(0.5, 1.0)
ax.set_xlabel("true proportion $p$")
ax.set_ylabel("coverage probability ($n = 20$)")
ax.grid(alpha=0.3)
ax.legend(loc="lower center", ncol=4, fontsize=9)
fig.tight_layout()
