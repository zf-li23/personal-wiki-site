"""Null distribution of the KS statistic D_n (n = 30) for normal samples when mu and sigma are known
and when they are estimated from the same sample (the Lilliefors statistic)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, reps = 30, 20000
i = np.arange(1, n + 1)


def ks_stat(z):
    p = stats.norm.cdf(np.sort(z, axis=1))
    return np.maximum((i / n - p).max(axis=1), (p - (i - 1) / n).max(axis=1))


x = rng.standard_normal((reps, n))
d_known = ks_stat(x)
z = (x - x.mean(axis=1, keepdims=True)) / x.std(axis=1, ddof=1, keepdims=True)
d_est = ks_stat(z)

fig, ax = plt.subplots(figsize=(7.6, 4.4))
bins = np.linspace(0, 0.35, 71)
ax.hist(d_known, bins=bins, density=True, alpha=0.45, color="C0", label="$\\mu, \\sigma$ known (Kolmogorov)")
ax.hist(d_est, bins=bins, density=True, alpha=0.45, color="C1", label="$\\mu, \\sigma$ estimated (Lilliefors)")
for d, color in [(np.quantile(d_known, 0.95), "C0"), (np.quantile(d_est, 0.95), "C1")]:
    ax.axvline(d, color=color, ls="--", lw=1.4)
ax.axvline(0.192, color="C3", lw=1.6)
ax.text(0.195, ax.get_ylim()[1] * 0.85, "observed 0.192", color="C3", fontsize=9)
ax.set_xlabel("$D_n$ ($n = 30$); dashed lines: 95% quantiles")
ax.set_ylabel("density")
ax.grid(alpha=0.3)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
