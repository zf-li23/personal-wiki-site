"""Gaussian-kernel SVM decision boundaries for a large, a moderate and a small kernel width sigma."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

rng = np.random.default_rng(0)
n = 120
t = rng.uniform(0, np.pi, n)
lab = rng.integers(0, 2, n)
X = np.c_[np.where(lab == 0, np.cos(t), 1 - np.cos(t)), np.where(lab == 0, np.sin(t), 0.5 - np.sin(t))]
X += rng.normal(0, 0.18, X.shape)
y = np.where(lab == 0, 1.0, -1.0)
C = 10.0


def gauss(A, B, sigma):
    d2 = np.sum(A**2, 1)[:, None] + np.sum(B**2, 1)[None, :] - 2 * A @ B.T
    return np.exp(-d2 / (2 * sigma**2))


g = np.linspace(-1.6, 2.6, 181)
h = np.linspace(-1.2, 1.7, 131)
gx, gy = np.meshgrid(g, h)
grid = np.c_[gx.ravel(), gy.ravel()]

fig, axes = plt.subplots(1, 3, figsize=(14, 4.0), sharey=True)
for ax, sigma, name in zip(axes, [3.0, 0.4, 0.05], ["too large: underfitting", "moderate", "too small: overfitting"]):
    K = gauss(X, X, sigma)
    G = (y[:, None] * y[None, :]) * K
    res = minimize(lambda a: 0.5 * a @ G @ a - a.sum(), np.zeros(n), jac=lambda a: G @ a - 1,
                   bounds=[(0, C)] * n, method="SLSQP", options={"ftol": 1e-10, "maxiter": 1000},
                   constraints=[{"type": "eq", "fun": lambda a: a @ y, "jac": lambda a: y}])
    alpha = res.x
    free = (alpha > 1e-5) & (alpha < C - 1e-5)
    f_train = (alpha * y) @ K
    b = np.mean(y[free] - f_train[free]) if free.any() else 0.0
    f = ((alpha * y) @ gauss(X, grid, sigma) + b).reshape(gx.shape)
    ax.contourf(gx, gy, np.sign(f), levels=[-2, 0, 2], colors=["C1", "C0"], alpha=0.18)
    ax.contour(gx, gy, f, levels=[0], colors="black", linewidths=1.3)
    ax.scatter(X[y > 0, 0], X[y > 0, 1], color="C0", s=14)
    ax.scatter(X[y < 0, 0], X[y < 0, 1], color="C1", marker="s", s=14)
    acc = np.mean(np.sign(f_train + b) == y)
    ax.set_title(f"sigma = {sigma:g} ({name})\ntraining accuracy {acc:.2f}, {int(np.sum(alpha > 1e-5))} SVs")
    ax.set_xlabel("x_1")
axes[0].set_ylabel("x_2")
fig.tight_layout()
