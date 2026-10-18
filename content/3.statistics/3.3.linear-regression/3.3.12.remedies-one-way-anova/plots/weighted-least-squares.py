"""WLS versus OLS for simulated data whose error standard deviation grows linearly with X."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 54
x = np.sort(rng.uniform(20, 60, n))
sd = 0.25 * x - 2.0
y = 56 + 0.58 * x + rng.normal(0, sd)

X = np.column_stack([np.ones(n), x])
b_ols = np.linalg.lstsq(X, y, rcond=None)[0]
e = y - X @ b_ols

# stage 2: regress |e| on x to estimate the standard deviation of each case
g = np.linalg.lstsq(X, np.abs(e), rcond=None)[0]
shat = X @ g
w = 1 / shat**2
W = np.diag(w)
b_wls = np.linalg.solve(X.T @ W @ X, X.T @ W @ y)

grid = np.linspace(18, 62, 100)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
ax.scatter(x, y, s=16, color="C0", alpha=0.8, zorder=3, label="data")
ax.plot(grid, b_ols[0] + b_ols[1] * grid, color="C1", lw=1.6, label=f"OLS: slope {b_ols[1]:.3f}")
ax.plot(grid, b_wls[0] + b_wls[1] * grid, color="C3", lw=1.6, ls="--", label=f"WLS: slope {b_wls[1]:.3f}")
ax.set_xlabel("X (age)")
ax.set_ylabel("Y")
ax.set_title("OLS and WLS fits")
ax.legend(loc="upper left")
ax.grid(alpha=0.3)

ax = axes[1]
ax.scatter(x, np.abs(e), s=16, color="C0", alpha=0.8, zorder=3, label="|OLS residual|")
ax.plot(grid, g[0] + g[1] * grid, color="C3", lw=1.6, label="fitted sigma_hat(X)")
ax.set_xlabel("X (age)")
ax.set_ylabel("absolute residual")
ax.set_title("Estimating the standard deviation")
ax.legend(loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
