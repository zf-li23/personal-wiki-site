"""One case with high leverage and a large residual: the fit with and without it, and Cook's distances."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 25
x = np.append(rng.uniform(0, 10, n - 1), 18.0)
y = 2 + 0.5 * x + rng.normal(0, 1, n)
y[-1] = 2 + 0.5 * 18 - 6.0
X = np.column_stack([np.ones(n), x])
XtXinv = np.linalg.inv(X.T @ X)
b = XtXinv @ X.T @ y
e = y - X @ b
h = np.einsum("ij,jk,ik->i", X, XtXinv, X)
p = 2
mse = e @ e / (n - p)
cook = e ** 2 / (p * mse) * h / (1 - h) ** 2
b_del = np.linalg.lstsq(X[:-1], y[:-1], rcond=None)[0]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
ax = axes[0]
grid = np.array([0, 19])
ax.plot(x[:-1], y[:-1], "o", color="C0", alpha=0.8)
ax.plot(x[-1], y[-1], "s", color="C3", ms=8, label=f"case {n}: h = {h[-1]:.2f}")
ax.plot(grid, b[0] + b[1] * grid, color="C3", lw=2, label="fit with all cases")
ax.plot(grid, b_del[0] + b_del[1] * grid, color="C2", lw=2, ls="--", label=f"fit without case {n}")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
ax = axes[1]
idx = np.arange(1, n + 1)
ax.vlines(idx, 0, cook, color="C0", lw=2)
ax.axhline(4 / n, color="C1", ls="--", lw=1.2, label="cutoff 4/n")
ax.set_xlabel("case number")
ax.set_ylabel("Cook's distance")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
