"""Randomization test for correlation: Monte Carlo null distribution of r under permutations of the prices."""

import numpy as np
import matplotlib.pyplot as plt

price = np.array([5.0, 4.8, 4.7, 4.0, 5.3, 4.1, 5.5, 4.7, 3.3, 4.0,
                  4.0, 4.6, 5.3, 3.0, 3.5, 3.9, 4.7, 5.0, 5.2, 4.6])
quantity = np.array([60, 59, 58, 47, 65, 48, 67, 70, 55, 63,
                     62, 65, 71, 56, 59, 60, 74, 77, 78, 62], dtype=float)
n, nrep = len(price), 50_000
rng = np.random.default_rng(0)

r_obs = np.corrcoef(price, quantity)[0, 1]

# Each row of idx is a random permutation of 0..n-1
idx = np.argsort(rng.random((nrep, n)), axis=1)
p_perm = price[idx]
pc = p_perm - p_perm.mean(axis=1, keepdims=True)
qc = quantity - quantity.mean()
r_perm = pc @ qc / (np.sqrt((pc ** 2).sum(axis=1)) * np.sqrt((qc ** 2).sum()))

p_one = np.mean(r_perm >= r_obs)
p_two = np.mean(np.abs(r_perm) >= abs(r_obs))

fig, ax = plt.subplots(figsize=(7.5, 4.2))
ax.hist(r_perm, bins=60, density=True, color="C0", alpha=0.6, edgecolor="none",
        label="r over 50,000 random permutations")
ax.axvline(r_obs, color="C3", lw=2, label=f"observed r = {r_obs:.4f}")
ax.axvline(-r_obs, color="C3", lw=1.2, ls="--", label="-|observed r| (two-sided)")
ax.set_xlabel("sample correlation of permuted prices with quantities")
ax.set_ylabel("density")
ax.set_title(f"Permutation null distribution: one-sided p = {p_one:.4f}, two-sided p = {p_two:.4f}",
             fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
