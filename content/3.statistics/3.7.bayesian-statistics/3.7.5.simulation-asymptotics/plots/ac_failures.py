"""Air conditioning failures (plane 7910): exponential model with gamma priors."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

y = np.array([74, 57, 48, 29, 502, 12, 70, 21, 29, 386, 59, 27, 153, 26, 326])
n, total = len(y), y.sum()

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
t = np.linspace(0, 0.025, 801)
# the normalized likelihood theta^n exp(-total theta) is the Gamma(n + 1, total) density
lik = stats.gamma(n + 1, scale=1 / total).pdf(t)
for ax, (a, b, name) in zip(axes[:2], [(9, 1000, "strong prior"), (5, 500, "weak prior")]):
    ax.plot(t, stats.gamma(a, scale=1 / b).pdf(t), color="0.5", ls="--", lw=1.5, label=f"prior Gamma({a}, {b})")
    ax.plot(t, lik, color="C0", ls=":", lw=1.5, label="normalized likelihood")
    ax.plot(t, stats.gamma(a + n, scale=1 / (b + total)).pdf(t), color="C3", lw=1.8,
            label=f"posterior Gamma({a + n}, {b + total})")
    ax.set_title(name, fontsize=11)
    ax.set_xlabel(r"failure rate $\theta$ (per hour)")
    ax.legend(fontsize=8.5)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("density")

# lambda = 1/theta under the strong prior: simulation versus the exact inverse-gamma density
rng = np.random.default_rng(0)
theta = rng.gamma(9 + n, 1 / (1000 + total), size=10000)
lam = 1 / theta
ax = axes[2]
ax.hist(lam, bins=60, density=True, color="C0", alpha=0.45, label="1/theta of 10000 draws")
grid = np.linspace(40, 260, 500)
ax.plot(grid, stats.invgamma(9 + n, scale=1000 + total).pdf(grid), color="C3", lw=1.8,
        label=f"Inv-Gamma({9 + n}, {1000 + total})")
ax.set_title("mean time between failures (strong prior)", fontsize=11)
ax.set_xlabel(r"$\lambda = 1/\theta$ (hours)")
ax.legend(fontsize=8.5)
ax.grid(alpha=0.3)
fig.tight_layout()
