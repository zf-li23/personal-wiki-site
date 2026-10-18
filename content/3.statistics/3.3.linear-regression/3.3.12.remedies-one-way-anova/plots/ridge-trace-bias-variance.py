"""Ridge trace and Monte Carlo bias-variance decomposition of the ridge estimator for collinear predictors."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n, p = 20, 3
z = rng.standard_normal(n)
X = np.column_stack([z + 0.08 * rng.standard_normal(n),
                     z + 0.08 * rng.standard_normal(n),
                     rng.standard_normal(n)])
X = (X - X.mean(0)) / X.std(0)
beta = np.array([1.0, 0.5, -0.5])
sigma = 1.0
lams = np.logspace(-3, 2, 201)


def ridge(y, lam):
    return np.linalg.solve(X.T @ X + lam * np.eye(p), X.T @ y)


y0 = X @ beta + sigma * rng.standard_normal(n)
y0 = y0 - y0.mean()
path = np.array([ridge(y0, lam) for lam in lams])

# exact bias and variance for the fixed design
XtX = X.T @ X
bias2, var = [], []
for lam in lams:
    A = np.linalg.solve(XtX + lam * np.eye(p), XtX)
    bias2.append(np.sum((A @ beta - beta) ** 2))
    M = np.linalg.solve(XtX + lam * np.eye(p), np.eye(p))
    var.append(sigma**2 * np.trace(M @ XtX @ M))
bias2, var = np.array(bias2), np.array(var)
mse = bias2 + var

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
for j, name in enumerate(["x1", "x2 (nearly equal to x1)", "x3"]):
    ax.plot(lams, path[:, j], lw=1.6, label=name)
ax.axhline(0, color="gray", lw=0.8)
ax.set_xscale("log")
ax.set_xlabel("lambda (log scale)")
ax.set_ylabel("standardized coefficient")
ax.set_title("Ridge trace")
ax.legend(loc="upper right")
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(lams, bias2, lw=1.6, label="squared bias")
ax.plot(lams, var, lw=1.6, label="variance")
ax.plot(lams, mse, lw=2.0, color="C3", label="MSE = bias^2 + variance")
mse_ols = sigma**2 * np.trace(np.linalg.inv(XtX))
ax.axhline(mse_ols, color="gray", ls="--", lw=1.0, label="MSE of OLS")
k = np.argmin(mse)
ax.plot(lams[k], mse[k], "o", color="C3")
ax.set_ylim(0, mse_ols * 1.15)
ax.set_xscale("log")
ax.set_xlabel("lambda (log scale)")
ax.set_ylabel("E ||b_R - beta||^2 components")
ax.set_title("Bias-variance trade-off")
ax.legend(loc="upper right")
ax.grid(alpha=0.3)
fig.tight_layout()
