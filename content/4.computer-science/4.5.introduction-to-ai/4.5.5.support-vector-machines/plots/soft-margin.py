"""Linear soft-margin SVM on overlapping classes for three values of the penalty C."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

rng = np.random.default_rng(1)
pos = rng.normal([1.6, 1.6], 0.9, (30, 2))
neg = rng.normal([0.0, 0.0], 0.9, (30, 2))
X = np.r_[pos, neg]
y = np.r_[np.ones(30), -np.ones(30)]
G = (y[:, None] * y[None, :]) * (X @ X.T)


def fit(C):
    res = minimize(lambda a: 0.5 * a @ G @ a - a.sum(), np.zeros(len(y)), jac=lambda a: G @ a - 1,
                   bounds=[(0, C)] * len(y), method="SLSQP", options={"ftol": 1e-12, "maxiter": 1000},
                   constraints=[{"type": "eq", "fun": lambda a: a @ y, "jac": lambda a: y}])
    alpha = res.x
    w = (alpha * y) @ X
    free = (alpha > 1e-6 * C) & (alpha < C * (1 - 1e-6))
    b = np.mean(y[free] - X[free] @ w) if free.any() else 0.0
    return alpha, w, b


fig, axes = plt.subplots(1, 3, figsize=(14, 4.6), sharey=True)
xs = np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 2)
for ax, C in zip(axes, [0.02, 1.0, 100.0]):
    alpha, w, b = fit(C)
    sv = alpha > 1e-6 * C
    ax.scatter(pos[:, 0], pos[:, 1], color="C0", s=18)
    ax.scatter(neg[:, 0], neg[:, 1], color="C1", marker="s", s=18)
    ax.scatter(X[sv, 0], X[sv, 1], s=90, facecolors="none", edgecolors="black", linewidths=1.0)
    for level, style in [(0, "-"), (1, "--"), (-1, "--")]:
        ax.plot(xs, (level - b - w[0] * xs) / w[1], color="black", linestyle=style, linewidth=1.2)
    errors = int(np.sum(np.sign(X @ w + b) != y))
    ax.set_title(f"C = {C:g}: {int(sv.sum())} support vectors, {errors} training errors")
    ax.set_xlabel("x_1")
    ax.set_xlim(xs[0], xs[1])
    ax.set_ylim(X[:, 1].min() - 0.8, X[:, 1].max() + 0.8)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("x_2")
fig.tight_layout()
