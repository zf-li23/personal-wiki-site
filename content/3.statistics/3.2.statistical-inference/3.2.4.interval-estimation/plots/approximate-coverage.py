"""Coverage of approximate and exact 95% confidence intervals."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

z = stats.norm.ppf(0.975)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))

# Bernoulli proportion: exact coverage of the Wald and Wilson intervals
ax = axes[0]
theta = 0.03
ns = np.arange(20, 501)
wald, wilson = [], []
for n in ns:
    k = np.arange(n + 1)
    p = stats.binom.pmf(k, n, theta)
    ph = k / n
    half = z * np.sqrt(ph * (1 - ph) / n)
    wald.append(p[(ph - half <= theta) & (theta <= ph + half)].sum())
    centre = (ph + z**2 / (2 * n)) * n / (n + z**2)
    hw = n / (n + z**2) * z * np.sqrt(ph * (1 - ph) / n + z**2 / (4 * n**2))
    wilson.append(p[(centre - hw <= theta) & (theta <= centre + hw)].sum())
ax.plot(ns, wald, lw=1, label="Wald")
ax.plot(ns, wilson, lw=1, label="Wilson")
ax.axhline(0.95, color="0.5", lw=1, ls="--")
ax.set_ylim(0.5, 1.0)
ax.set_xlabel("sample size n")
ax.set_ylabel("coverage probability")
ax.set_title("Bernoulli, theta = 0.03")
ax.legend(frameon=False, loc="lower right")

# Exponential mean: simulated coverage of the approximate and exact intervals
ax = axes[1]
rng = np.random.default_rng(0)
reps = 4000
ns2 = np.array([5, 10, 15, 20, 30, 40, 60, 80, 100, 150, 200, 300])
approx, exact = [], []
for n in ns2:
    xbar = rng.exponential(1.0, size=(reps, n)).mean(axis=1)
    approx.append(np.mean(np.abs(xbar - 1.0) <= z * xbar / np.sqrt(n)))
    lo = 2 * n * xbar / stats.chi2.ppf(0.975, 2 * n)
    hi = 2 * n * xbar / stats.chi2.ppf(0.025, 2 * n)
    exact.append(np.mean((lo <= 1.0) & (1.0 <= hi)))
ax.plot(ns2, approx, "o-", ms=4, label="x_bar +- z x_bar / sqrt(n)")
ax.plot(ns2, exact, "s-", ms=4, label="exact chi-square interval")
ax.axhline(0.95, color="0.5", lw=1, ls="--")
ax.set_xscale("log")
ax.set_ylim(0.85, 1.0)
ax.set_xlabel("sample size n")
ax.set_title("Exponential mean, theta = 1")
ax.legend(frameon=False, loc="lower right")

fig.tight_layout()
