"""Same mean structure, different noise: a significant slope does not imply a large R^2."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n = 200
x = rng.uniform(0, 200, n)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
for ax, sd in zip(axes, [50, 280]):
    y = 45 + 2.1 * x + rng.normal(0, sd, n)
    res = stats.linregress(x, y)
    grid = np.array([0, 200])
    ax.plot(x, y, "o", ms=3.5, alpha=0.7, color="C0")
    ax.plot(grid, res.intercept + res.slope * grid, color="C3", lw=2)
    ax.set_title(f"slope p-value = {res.pvalue:.1e},  R^2 = {res.rvalue ** 2:.2f}", fontsize=10)
    ax.set_xlabel("x")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("y")
fig.suptitle("Both slopes are highly significant; only the scatter around the line differs", fontsize=11)
fig.tight_layout()
