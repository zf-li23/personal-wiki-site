"""Normal approximation to the binomial distribution: one example and the error against np."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))

# Left: Bin(20, 0.2) and its normal approximation
n, p = 20, 0.2
k = np.arange(0, 13)
mu, sd = n * p, np.sqrt(n * p * (1 - p))
ax = axes[0]
ax.bar(k, stats.binom.pmf(k, n, p), width=0.8, color="C0", alpha=0.6, label="Bin(20, 0.2)")
approx = stats.norm.cdf(k + 0.5, mu, sd) - stats.norm.cdf(k - 0.5, mu, sd)
ax.plot(k, approx, "o", color="C3", ms=5, label="normal, P(k - 1/2 < Y < k + 1/2)")
xx = np.linspace(-1, 12.5, 300)
ax.plot(xx, stats.norm.pdf(xx, mu, sd), color="C3", lw=1.2, alpha=0.7)
ax.set_xlabel("number of successes k")
ax.set_ylabel("probability")
ax.set_title("n = 20, p = 0.2 (np = 4): the binomial is skewed", fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Right: largest error of the continuity-corrected approximation against np
ax = axes[1]
for c, p in enumerate([0.5, 0.2, 0.05]):
    nps = np.arange(1, 21)
    errs = []
    for m in nps:
        n = int(round(m / p))
        k = np.arange(n + 1)
        mu, sd = n * p, np.sqrt(n * p * (1 - p))
        cdf_b = stats.binom.cdf(k, n, p)
        cdf_n = stats.norm.cdf(k + 0.5, mu, sd)
        errs.append(np.abs(cdf_b - cdf_n).max())
    ax.plot(nps, errs, "o-", color=f"C{c}", ms=3.5, lw=1.5, label=f"p = {p}")
ax.axvline(5, color="gray", ls="--", lw=1)
ax.text(5.3, 0.92, "np = 5", fontsize=8, color="gray", transform=ax.get_xaxis_transform())
ax.set_xlabel("np")
ax.set_ylabel("max |P(X <= k) - normal approximation|")
ax.set_title("Error of the continuity-corrected normal approximation", fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
