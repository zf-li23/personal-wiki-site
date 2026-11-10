"""Exact null distribution for six units and a simulated randomization distribution for 72 units."""

from itertools import combinations

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(4)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

# Left: six honey units, all 20 assignments under the sharp null
y = np.array([3, 5, 0, 4, 0, 1], dtype=float)
t_obs = abs(y[:3].mean() - y[3:].mean())
values = []
for treated in combinations(range(6), 3):
    w = np.zeros(6, dtype=bool)
    w[list(treated)] = True
    values.append(abs(y[w].mean() - y[~w].mean()))
values = np.round(values, 6)
support, counts = np.unique(values, return_counts=True)
colors = ["C3" if v >= t_obs - 1e-9 else "C0" for v in support]
ax = axes[0]
ax.bar(support, counts, width=0.25, color=colors, edgecolor="black")
ax.axvline(t_obs, color="black", ls="--", lw=1.2)
ax.set_xticks(support)
ax.set_xticklabels(["1/3", "1", "5/3", "7/3", "11/3"])
ax.set_xlabel("absolute difference in means")
ax.set_ylabel("number of assignments (of 20)")
ax.set_title(f"Six units: observed value 1, exact p = {(values >= t_obs - 1e-9).mean():.2f}",
             fontsize=10)

# Right: simulated 72-unit experiment with outcomes on a 0-6 scale
n, n_t = 72, 35
y0 = rng.binomial(6, 0.45, n).astype(float)
y1 = np.clip(y0 - rng.binomial(1, 0.7, n), 0, 6)
w_obs = np.zeros(n, dtype=bool)
w_obs[rng.choice(n, n_t, replace=False)] = True
y_obs = np.where(w_obs, y1, y0)
d_obs = y_obs[w_obs].mean() - y_obs[~w_obs].mean()

k = 100_000
diffs = np.empty(k)
for j in range(k):
    w = np.zeros(n, dtype=bool)
    w[rng.choice(n, n_t, replace=False)] = True
    diffs[j] = y_obs[w].mean() - y_obs[~w].mean()
p_sim = np.mean(np.abs(diffs) >= abs(d_obs) - 1e-12)
sd_null = np.sqrt(n / (n_t * (n - n_t)) * y_obs.var(ddof=1))

ax = axes[1]
ax.hist(diffs, bins=45, density=True, color="C0", alpha=0.6, label="randomization distribution")
grid = np.linspace(diffs.min(), diffs.max(), 300)
ax.plot(grid, stats.norm.pdf(grid, 0, sd_null), color="C1", lw=2, label="normal approximation")
ax.axvline(d_obs, color="black", ls="--", lw=1.2, label="observed")
ax.axvline(-d_obs, color="black", ls=":", lw=1.0)
ax.set_xlabel("difference in means (treated minus control)")
ax.set_ylabel("density")
ax.set_title(f"72 units (simulated): simulated p = {p_sim:.3f}", fontsize=10)
ax.legend(fontsize=8)
fig.tight_layout()
