"""Posterior predictive checks: switches in a binary sequence, and the minimum of Newcomb's data."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

# binary sequence: uniform prior, posterior Beta(8, 14), T = number of switches
y = np.array([1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
L = 10000
theta = rng.beta(1 + y.sum(), 1 + len(y) - y.sum(), L)
rep = (rng.random((L, len(y))) < theta[:, None]).astype(int)
t_rep = np.sum(rep[:, 1:] != rep[:, :-1], axis=1)
t_obs = np.sum(y[1:] != y[:-1])
ax = axes[0]
counts = np.bincount(t_rep, minlength=20)
ax.bar(np.arange(len(counts)), counts, width=0.8, color="C0", alpha=0.75)
ax.axvline(t_obs, color="C3", lw=2)
ax.text(t_obs + 0.3, counts.max() * 0.92, f"T(y) = {t_obs}", color="C3", fontsize=10)
ax.set_title(f"switches in 10,000 replications; Pr(T(y_rep) >= 3 | y) = {np.mean(t_rep >= t_obs):.3f}", fontsize=10)
ax.set_xlabel("number of switches T(y_rep)")
ax.set_ylabel("count")
ax.grid(alpha=0.3)

# Newcomb's 66 measurements (deviations from 24,800 ns), normal model, p(mu, log sigma) ∝ 1
nc = np.array([28, -44, 29, 30, 24, 28, 37, 32, 36, 27, 26, 28, 29, 26, 27, 22, 23, 20, 25, 25, 36, 23,
               31, 32, 24, 27, 33, 16, 24, 29, 36, 21, 28, 26, 27, 27, 32, 25, 28, 24, 40, 21, 31, 32,
               28, 26, 30, 27, 26, 24, 32, 29, 34, -2, 25, 19, 36, 29, 30, 22, 28, 33, 39, 25, 16, 23])
n = len(nc)
L = 5000
sigma2 = (n - 1) * nc.var(ddof=1) / rng.chisquare(n - 1, L)
mu = nc.mean() + np.sqrt(sigma2 / n) * rng.standard_normal(L)
rep = mu[:, None] + np.sqrt(sigma2)[:, None] * rng.standard_normal((L, n))
ax = axes[1]
ax.hist(rep.min(axis=1), bins=40, color="C0", alpha=0.75)
ax.axvline(nc.min(), color="C3", lw=2)
ax.text(nc.min() + 1, ax.get_ylim()[1] * 0.9, f"min y = {nc.min()}", color="C3", fontsize=10)
ax.set_title("smallest observation: 5,000 replications vs Newcomb's data", fontsize=10)
ax.set_xlabel("min y_rep")
ax.set_xlim(-50, 20)
ax.grid(alpha=0.3)
fig.tight_layout()
