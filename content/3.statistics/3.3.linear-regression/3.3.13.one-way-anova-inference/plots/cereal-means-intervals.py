"""Cereal sales by package design: data with level means, and pooled versus unpooled 95% intervals."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = [[11, 17, 16, 14, 15], [12, 10, 15, 19, 11], [23, 20, 18, 17], [27, 33, 22, 26, 28]]
data = [np.array(v, float) for v in data]
r = len(data)
n = np.array([len(v) for v in data])
means = np.array([v.mean() for v in data])
sds = np.array([v.std(ddof=1) for v in data])
nT = n.sum()
s = np.sqrt(sum(((v - v.mean()) ** 2).sum() for v in data) / (nT - r))

rng = np.random.default_rng(0)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), sharey=True)
ax = axes[0]
for i, v in enumerate(data):
    ax.scatter(np.full(len(v), i + 1) + rng.uniform(-0.08, 0.08, len(v)), v, s=22, color="C0", zorder=3)
ax.plot(np.arange(1, r + 1), means, "D-", color="C3", ms=7, lw=1.4, label="level mean")
ax.set_xticks(range(1, r + 1))
ax.set_xlabel("package design")
ax.set_ylabel("cases sold")
ax.set_title("Data and level means")
ax.legend(loc="upper left")
ax.grid(alpha=0.3)

ax = axes[1]
t_pool = stats.t.ppf(0.975, nT - r)
for i in range(r):
    h1 = t_pool * s / np.sqrt(n[i])
    h2 = stats.t.ppf(0.975, n[i] - 1) * sds[i] / np.sqrt(n[i])
    ax.errorbar(i + 1 - 0.1, means[i], yerr=h1, fmt="o", color="C0", capsize=4, lw=1.6,
                label="pooled s, 15 d.f." if i == 0 else None)
    ax.errorbar(i + 1 + 0.1, means[i], yerr=h2, fmt="s", color="C1", capsize=4, lw=1.6,
                label="own s_i, n_i - 1 d.f." if i == 0 else None)
ax.set_xticks(range(1, r + 1))
ax.set_xlabel("package design")
ax.set_title("95% confidence intervals for the means")
ax.legend(loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
