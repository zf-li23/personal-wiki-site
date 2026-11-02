"""Same level means, different within-group scatter: the F statistic of two simulated experiments."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
means = np.array([10.0, 9.0, 12.0, 14.0, 7.0])
a, n = len(means), 10
noise = rng.standard_normal((a, n))
noise -= noise.mean(axis=1, keepdims=True)
noise /= noise.std(axis=1, ddof=1, keepdims=True)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
for ax, sd in zip(axes, [1.0, 6.0]):
    y = means[:, None] + sd * noise
    grand = y.mean()
    sstr = n * ((y.mean(axis=1) - grand) ** 2).sum()
    sse = ((y - y.mean(axis=1, keepdims=True)) ** 2).sum()
    f0 = (sstr / (a - 1)) / (sse / (a * n - a))
    p = stats.f.sf(f0, a - 1, a * n - a)
    ax.boxplot(list(y), positions=range(a), widths=0.5)
    ax.plot(range(a), y.mean(axis=1), "D", color="C3", label="level mean")
    ax.axhline(grand, color="gray", ls="--")
    ax.set_xticks(range(a))
    ax.set_xticklabels(["A", "B", "C", "D", "E"])
    ax.set_title(f"within-group SD = {sd:.0f}:  F0 = {f0:.1f}, p = {p:.2g}")
    ax.set_xlabel("level")
    ax.grid(alpha=0.3, axis="y")
axes[0].set_ylabel("response")
axes[0].legend(frameon=False, loc="upper left")
fig.tight_layout()
