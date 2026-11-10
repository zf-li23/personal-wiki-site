"""Pulse rates of seven students on three occasions: raw profiles and within-block ranks for the Friedman test."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

pr = np.array([[72, 120, 76], [96, 120, 95], [88, 132, 104], [92, 120, 96],
               [74, 101, 84], [76, 96, 72], [82, 112, 76]], float)
ranks = np.apply_along_axis(stats.rankdata, 1, pr)
T, p = stats.friedmanchisquare(*pr.T)
occ = ["I: before", "II: just after", "III: 5 min after"]
jit = np.linspace(-0.12, 0.12, len(pr))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for i in range(len(pr)):
    axes[0].plot(range(3), pr[i], "o-", color="C0", alpha=0.6)
    axes[1].plot(np.arange(3) + jit[i], ranks[i], "o-", color="C1", alpha=0.6)
for ax in axes:
    ax.set_xticks(range(3))
    ax.set_xticklabels(occ)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("pulse rate (per minute)")
axes[0].set_title("Seven students (blocks)")
axes[1].set_ylabel("rank within student")
axes[1].set_yticks([1, 2, 3])
s = ranks.sum(0)
axes[1].set_title(f"Rank sums {s[0]:g}, {s[1]:g}, {s[2]:g}: T = {T:.2f}, p = {p:.4f}")
fig.tight_layout()
