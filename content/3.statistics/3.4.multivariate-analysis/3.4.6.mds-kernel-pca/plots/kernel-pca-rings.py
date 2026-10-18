"""Linear PCA versus Gaussian-kernel PCA on two concentric rings."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n_per = 150
t = rng.uniform(0, 2 * np.pi, 2 * n_per)
r = np.r_[rng.normal(1.0, 0.1, n_per), rng.normal(3.0, 0.15, n_per)]
x = np.c_[r * np.cos(t), r * np.sin(t)]
label = np.r_[np.zeros(n_per), np.ones(n_per)]
n = len(x)
H = np.eye(n) - np.ones((n, n)) / n

# linear PCA
xc = x - x.mean(0)
_, _, Vt = np.linalg.svd(xc, full_matrices=False)
lin = xc @ Vt.T

# Gaussian kernel PCA
sigma = 1.0
sq = np.sum(x**2, 1)
K = np.exp(-(sq[:, None] + sq[None, :] - 2 * x @ x.T) / (2 * sigma**2))
Kc = H @ K @ H
lam, A = np.linalg.eigh(Kc)
order = np.argsort(lam)[::-1]
lam, A = lam[order], A[:, order]
kp = A[:, :2] * np.sqrt(lam[:2])

fig, axes = plt.subplots(1, 3, figsize=(14, 4.4))
for ax, data, title, xl, yl in [
    (axes[0], x, "original data", "x_1", "x_2"),
    (axes[1], lin, "linear PCA", "PC 1", "PC 2"),
    (axes[2], kp, "Gaussian kernel PCA (sigma = 1)", "kernel PC 1", "kernel PC 2"),
]:
    for k, color, name in [(0, "C0", "inner ring"), (1, "C1", "outer ring")]:
        m = label == k
        ax.scatter(data[m, 0], data[m, 1], s=10, color=color, label=name, alpha=0.8)
    ax.set_title(title)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.grid(alpha=0.3)
axes[0].set_aspect("equal")
axes[1].set_aspect("equal")
axes[0].legend(loc="upper right", fontsize=8)
fig.tight_layout()
