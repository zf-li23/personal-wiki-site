"""Nonlinear regression: conditional mean E(X | Y = y) versus the best linear predictor."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 1500
y = rng.uniform(-2, 2, n)
m = np.sin(1.5 * y) + 0.3 * y**2
x = m + rng.normal(0, 0.35, n)

grid = np.linspace(-2, 2, 400)
m_grid = np.sin(1.5 * grid) + 0.3 * grid**2
b = np.cov(y, x)[0, 1] / np.var(y, ddof=1)
a = x.mean() - b * y.mean()

fig, ax = plt.subplots(figsize=(7, 4.3))
ax.scatter(y, x, s=5, alpha=0.3, color="C0", label="sample of (Y, X)")
ax.plot(grid, m_grid, color="C3", lw=2.2, label="E(X | Y = y): best predictor")
ax.plot(grid, a + b * grid, color="C1", lw=1.8, ls="--", label="best linear predictor")
ax.set_xlabel("y")
ax.set_ylabel("x")
ax.set_title("conditional expectation as the best mean-square prediction")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
