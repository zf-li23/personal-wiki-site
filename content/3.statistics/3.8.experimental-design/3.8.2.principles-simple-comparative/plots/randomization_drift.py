"""Run-order drift confounded with group: cancers first versus random order."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n_cancer, n_control = 100, 100
n = n_cancer + n_control
order = np.arange(1, n + 1)
# Measurement quality drifts downward over the run order; no true group difference
drift = 6.0 - 2.5 * (order / n) ** 2
noise = rng.normal(0, 0.8, n)
signal = drift + noise

groups_first = np.array([1] * n_cancer + [0] * n_control)   # cancers run first
groups_random = rng.permutation(groups_first)                 # randomized run order

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
for ax, g, title in zip(axes, [groups_first, groups_random],
                        ["Cancers run first, controls later", "Randomized run order"]):
    ax.plot(order, drift, color="gray", lw=1.5, ls="--", label="drift")
    ax.scatter(order[g == 1], signal[g == 1], s=12, color="C3", label="cancer")
    ax.scatter(order[g == 0], signal[g == 0], s=12, color="C0", marker="s", label="control")
    res = stats.ttest_ind(signal[g == 1], signal[g == 0])
    diff = signal[g == 1].mean() - signal[g == 0].mean()
    ax.set_title(f"{title}\nmean difference = {diff:.2f}, p = {res.pvalue:.1e}", fontsize=10)
    ax.set_xlabel("run order (sample number)")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("measured intensity")
axes[0].legend(fontsize=9, loc="lower left")
fig.tight_layout()
