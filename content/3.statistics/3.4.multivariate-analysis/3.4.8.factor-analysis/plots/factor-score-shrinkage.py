"""Bartlett (WLS) versus regression factor scores in a simulated two-factor model."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
p, m, n = 6, 2, 400
L = np.array([[0.9, 0.0], [0.8, 0.1], [0.7, 0.0], [0.1, 0.6], [0.0, 0.5], [0.0, 0.4]])
psi = 1 - (L**2).sum(axis=1)
F = rng.standard_normal((n, m))
X = F @ L.T + rng.standard_normal((n, p)) * np.sqrt(psi)
Pinv = np.diag(1 / psi)
Delta = L.T @ Pinv @ L
f_wls = X @ (Pinv @ L @ np.linalg.inv(Delta))
f_reg = X @ np.linalg.solve(L @ L.T + np.diag(psi), L)
fig, axes = plt.subplots(1, 2, figsize=(11, 5), sharex=True, sharey=True)
grid = np.array([-3.5, 3.5])
for j, ax in enumerate(axes):
    mse_w = np.mean((f_wls[:, j] - F[:, j]) ** 2)
    mse_r = np.mean((f_reg[:, j] - F[:, j]) ** 2)
    ax.plot(F[:, j], f_wls[:, j], "o", ms=3, alpha=0.5, color="C0", label=f"Bartlett (WLS), MSE {mse_w:.2f}")
    ax.plot(F[:, j], f_reg[:, j], "o", ms=3, alpha=0.5, color="C3", label=f"regression, MSE {mse_r:.2f}")
    ax.plot(grid, grid, color="0.3", lw=1, ls="--", label="45-degree line")
    d = Delta[j, j]
    ax.set_title(f"factor {j + 1}  (delta = {d:.2f})")
    ax.set_xlabel("true factor value")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("estimated factor score")
fig.tight_layout()
