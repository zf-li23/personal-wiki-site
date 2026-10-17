"""Normal Q-Q plots for a normal sample, a sample with an outlier, a right-skewed sample and a heavy-tailed sample."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n = 50
normal = rng.normal(size=n)
outlier = np.append(rng.normal(size=n - 1), 4.5)
skewed = rng.exponential(size=n) * 1.5 - 1.5
heavy = rng.standard_t(df=2.5, size=n)
samples = [("Normal", normal), ("Outlier", outlier), ("Right-skewed", skewed), ("Heavy tails", heavy)]

theo = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)
q = stats.norm.ppf([0.25, 0.75])
fig, axes = plt.subplots(1, 4, figsize=(12, 3.4))
for ax, (title, s) in zip(axes, samples):
    s = np.sort(s)
    ax.plot(theo, s, "o", ms=4.5, color="C0", alpha=0.8)
    # reference line through the quartiles
    sq = np.quantile(s, [0.25, 0.75])
    slope = (sq[1] - sq[0]) / (q[1] - q[0])
    t = np.array([-2.6, 2.6])
    ax.plot(t, sq[0] + slope * (t - q[0]), color="C3", lw=1.5)
    ax.set_title(title, fontsize=11)
    ax.set_xlabel("theoretical quantiles")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("sample quantiles")
fig.tight_layout()
