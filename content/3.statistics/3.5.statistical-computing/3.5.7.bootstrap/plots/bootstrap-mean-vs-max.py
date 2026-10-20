"""Bootstrap distributions of the sample mean and the sample maximum for one sample of size
n = 50 from U(0, 1): the first is smooth and bell-shaped, the second breaks into isolated
clumps at the largest order statistics."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n, B = 50, 2000
x = rng.uniform(0, 1, n)
idx = rng.integers(0, n, (B, n))
means = x[idx].mean(axis=1)
maxima = x[idx].max(axis=1)

fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
ax = axes[0]
ax.hist(means, bins=40, color="C0", alpha=0.6, density=True)
ax.axvline(x.mean(), color="C3", lw=2, label="sample mean")
ax.set_title("Sample mean: smooth functional", fontsize=10)
ax.set_xlabel("bootstrap mean")
ax.set_ylabel("density")
ax.legend(fontsize=8)

ax = axes[1]
values, counts = np.unique(maxima, return_counts=True)
ax.vlines(values, 0, counts / B, color="C1", lw=3)
ax.axvline(x.max(), color="C3", lw=1, ls="--", label="sample maximum")
share = np.mean(maxima == x.max())
ax.set_title(f"Sample maximum: P(max* = max) = {share:.2f}", fontsize=10)
ax.set_xlabel("bootstrap maximum")
ax.set_ylabel("relative frequency")
ax.set_xlim(np.sort(x)[-8] - 0.01, x.max() + 0.01)
ax.legend(fontsize=8, loc="upper left")
for a in axes:
    a.grid(alpha=0.3)
fig.tight_layout()
