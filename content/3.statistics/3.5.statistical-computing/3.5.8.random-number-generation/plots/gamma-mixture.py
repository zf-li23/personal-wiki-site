"""Sampling from a mixture of five gamma distributions Gamma(3, rate 1/i) with weights i/15:
first draw the component label, then draw from that component."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n = 5000
weights = np.arange(1, 6) / 15
k = rng.choice(np.arange(1, 6), size=n, p=weights)
x = rng.gamma(shape=3, scale=k)   # rate 1/k means scale k

grid = np.linspace(0, 40, 500)
fig, ax = plt.subplots(figsize=(7.5, 4.4))
ax.hist(x, bins=80, range=(0, 40), density=True, color="C0", alpha=0.45, label=f"mixture sample (n = {n})")
mix = np.zeros_like(grid)
for i, w in zip(range(1, 6), weights):
    comp = stats.gamma.pdf(grid, a=3, scale=i)
    mix += w * comp
    ax.plot(grid, comp, color="C7", lw=1, ls="--", label="components Gamma(3, 1/i)" if i == 1 else None)
ax.plot(grid, mix, color="C3", lw=2.5, label="mixture density")
ax.set_xlim(0, 40)
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.set_title("Mixture of Gamma(3, 1/i), weights i/15, i = 1, ..., 5", fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
