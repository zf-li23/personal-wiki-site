"""Sampling distribution of (b1, b2) for uncorrelated and for highly correlated explanatory variables."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n, reps, sigma = 30, 2000, 1.0
fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), sharex=True, sharey=True)
for ax, rho in zip(axes, [0.0, 0.95]):
    cov = np.array([[1.0, rho], [rho, 1.0]])
    x = rng.multivariate_normal([0, 0], cov, size=n)
    X = np.column_stack([np.ones(n), x])
    XtXinv = np.linalg.inv(X.T @ X)
    est = np.empty((reps, 2))
    for r in range(reps):
        y = 2 + x[:, 0] + x[:, 1] + rng.normal(0, sigma, n)
        est[r] = (XtXinv @ X.T @ y)[1:]
    se = np.sqrt(np.diag(XtXinv)[1:]) * sigma
    ax.plot(est[:, 0], est[:, 1], ".", ms=2, alpha=0.4, color="C0")
    ax.plot(1, 1, "+", ms=14, mew=2, color="C3")
    ax.set_title(f"corr(X1, X2) = {rho}:  sd(b1) = {se[0]:.2f}, sd(b2) = {se[1]:.2f}", fontsize=10)
    ax.set_xlabel("b1")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("b2")
axes[0].set_xlim(-1.5, 3.5)
axes[0].set_ylim(-1.5, 3.5)
fig.suptitle("Same true coefficients (1, 1), same n = 30: collinearity inflates the variances", fontsize=11)
fig.tight_layout()
