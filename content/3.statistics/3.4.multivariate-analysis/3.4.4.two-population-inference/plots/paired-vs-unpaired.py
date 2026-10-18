"""Paired data: overlapping marginal samples, but within-pair differences clearly shifted from zero."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 16
size = rng.normal(17.5, 2.0, n)              # person-to-person variation
left = size + rng.normal(0, 0.15, n)
right = size + 0.25 + rng.normal(0, 0.15, n)  # small systematic shift
diff = left - right

fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))

ax = axes[0]
ax.boxplot([left, right], tick_labels=["Left", "Right"], widths=0.5)
ax.set_ylabel("hand size")
ax.set_title("marginal samples (unpaired view)")
ax.grid(alpha=0.3)

ax = axes[1]
ax.scatter(left, right, color="C0", zorder=3)
lim = [min(left.min(), right.min()) - 0.5, max(left.max(), right.max()) + 0.5]
ax.plot(lim, lim, color="C3", lw=1.2, label="y = x")
ax.set_xlim(lim)
ax.set_ylim(lim)
ax.set_aspect("equal")
ax.set_xlabel("left")
ax.set_ylabel("right")
ax.set_title("paired observations")
ax.legend(loc="upper left")
ax.grid(alpha=0.3)

ax = axes[2]
ax.axvline(0, color="C3", lw=1.2)
ax.scatter(diff, np.zeros(n) + rng.uniform(-0.1, 0.1, n), color="C1", zorder=3)
ax.set_ylim(-1, 1)
ax.set_yticks([])
ax.set_xlabel("left - right")
ax.set_title("within-pair differences")
ax.grid(alpha=0.3)

fig.tight_layout()
