"""Simulation: 1000 samples of size 100 from N(1, 4); distributions of the sample mean, S^2 and the t statistic."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n, reps, a, sigma = 100, 1000, 1.0, 2.0
y = np.random.normal(a, sigma, size=(reps, n))
xbar = y.mean(axis=1)
s2 = y.var(axis=1, ddof=1)
tstat = np.sqrt(n) * (xbar - a) / np.sqrt(s2)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))

ax = axes[0]
ax.hist(xbar, bins=30, density=True, color="C0", alpha=0.6)
g = np.linspace(xbar.min(), xbar.max(), 300)
ax.plot(g, stats.norm.pdf(g, a, sigma / np.sqrt(n)), color="C3", lw=1.5, label="N(a, sigma^2/n)")
ax.axvline(a, color="C2", lw=1.2)
ax.set_title("sample mean")
ax.legend()

ax = axes[1]
ax.hist(s2, bins=30, density=True, color="C0", alpha=0.6)
g = np.linspace(s2.min(), s2.max(), 300)
ax.plot(g, stats.chi2.pdf((n - 1) * g / sigma**2, n - 1) * (n - 1) / sigma**2, color="C3", lw=1.5,
        label="sigma^2 chi2(n-1)/(n-1)")
ax.axvline(sigma**2, color="C2", lw=1.2)
ax.set_title("sample variance S^2")
ax.legend()

ax = axes[2]
ax.hist(tstat, bins=30, density=True, color="C0", alpha=0.6)
g = np.linspace(-4, 4, 300)
ax.plot(g, stats.t.pdf(g, n - 1), color="C3", lw=1.5, label="t(n-1)")
ax.set_title("sqrt(n)(mean - a)/S")
ax.legend()

for ax in axes:
    ax.grid(alpha=0.3)
fig.suptitle("1000 samples of size n = 100 from N(1, 4)")
fig.tight_layout()
