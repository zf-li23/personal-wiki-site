"""Importance sampling estimates of a known area (= 1) with proposals of different shapes and tails."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
R, n = 5000, 1000                         # 5000 estimates, each from n = 1000 proposal draws
lo, hi = -50.0, 50.0
z_cauchy = stats.cauchy.cdf(hi) - stats.cauchy.cdf(lo)
cases = [
    ("N(0,1) target, U(-50,50) proposal", stats.norm.pdf, stats.uniform(lo, hi - lo)),
    ("N(0,1) target, t1 proposal", stats.norm.pdf, stats.t(1)),
    ("N(0,1) target, t30 proposal", stats.norm.pdf, stats.t(30)),
    ("Cauchy target, N(0,1) proposal", lambda x: stats.cauchy.pdf(x) / z_cauchy, stats.norm()),
]

fig, axes = plt.subplots(2, 4, figsize=(14, 6.0))
grid = np.linspace(-6, 6, 400)
bins = np.linspace(0.4, 1.6, 49)
for j, (title, target, prop) in enumerate(cases):
    ax = axes[0, j]
    ax.plot(grid, target(grid), color="C0", lw=1.6, label="target")
    ax.plot(grid, prop.pdf(grid), color="C3", lw=1.4, ls="--", label="proposal")
    ax.set_title(title, fontsize=10)
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 0.45)
    ax.legend(fontsize=8)
    # each estimate is the average importance weight over n draws, restricted to (lo, hi)
    x = prop.rvs(size=(R, n), random_state=rng)
    w = np.where((x > lo) & (x < hi), target(x) / prop.pdf(x), 0.0)
    est = w.mean(axis=1)
    over = int(np.sum(est > bins[-1]))
    ax = axes[1, j]
    ax.hist(np.clip(est, bins[0], bins[-1] - 1e-9), bins=bins, color="C2")
    ax.axvline(1, color="0.4", lw=1, ls="--")
    ax.set_xlabel("estimated area")
    ax.set_title(f"sd = {est.std():.4f}; {over} estimates > {bins[-1]}", fontsize=10)
for ax in axes.ravel():
    ax.grid(alpha=0.3)
axes[1, 0].set_ylabel(f"count out of {R}")
fig.tight_layout()
