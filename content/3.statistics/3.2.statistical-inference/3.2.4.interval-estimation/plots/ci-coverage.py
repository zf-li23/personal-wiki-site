"""One hundred simulated confidence intervals for a normal mean with k = 1.96 and k = 0.5."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
mu, sigma, n, reps = 68.0, np.sqrt(3.6), 100, 100
x = rng.normal(mu, sigma, size=(reps, n))
xbar = x.mean(axis=1)
s = x.std(axis=1, ddof=1)

fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), sharey=True)
for ax, k in zip(axes, [1.96, 0.5]):
    lo, hi = xbar - k * s / np.sqrt(n), xbar + k * s / np.sqrt(n)
    cover = (lo <= mu) & (mu <= hi)
    for i in range(reps):
        if cover[i]:
            ax.plot([lo[i], hi[i]], [i, i], color="0.65", lw=1.2)
        else:
            ax.plot([lo[i], hi[i]], [i, i], color="C3", lw=1.8)
    ax.plot(xbar, np.arange(reps), ".", color="0.35", ms=2.5)
    ax.axvline(mu, color="C0", lw=1.5)
    ax.set_title(f"k = {k}: {cover.mean():.0%} of the intervals cover mu")
    ax.set_xlabel("height (in)")
    ax.set_xlim(67.0, 69.0)
axes[0].set_ylabel("replication")
fig.tight_layout()
