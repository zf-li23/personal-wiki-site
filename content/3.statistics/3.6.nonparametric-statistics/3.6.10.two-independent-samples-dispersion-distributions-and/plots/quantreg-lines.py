"""Quantile regression lines and the slope as a function of tau, for simulated heteroscedastic expenditure data."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

rng = np.random.default_rng(0)
n = 235
income = np.exp(rng.normal(np.log(900), 0.45, n))
# spread grows with income and the errors are right-skewed
food = 80 + 0.5 * income + 0.12 * income * (rng.gamma(3, 1, n) - 3) / np.sqrt(3)
X = np.column_stack([np.ones(n), income])


def rq(X, y, tau):
    # min tau 1'u + (1 - tau) 1'v  s.t.  X(l - m) + u - v = y,  all variables >= 0
    n, p = X.shape
    cost = np.concatenate([np.zeros(2 * p), tau * np.ones(n), (1 - tau) * np.ones(n)])
    A = np.hstack([X, -X, np.eye(n), -np.eye(n)])
    sol = linprog(cost, A_eq=A, b_eq=y, bounds=(0, None), method="highs")
    return sol.x[:p] - sol.x[p:2 * p]


ols = np.linalg.lstsq(X, food, rcond=None)[0]
taus = np.round(np.arange(0.05, 0.96, 0.05), 2)
coef = np.array([rq(X, food, t) for t in taus])

# bootstrap band for the slopes (pairs bootstrap, small number of replicates)
B = 60
boot = np.empty((B, len(taus)))
for b in range(B):
    idx = rng.integers(0, n, n)
    boot[b] = [rq(X[idx], food[idx], t)[1] for t in taus]
lo, hi = np.percentile(boot, [5, 95], axis=0)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
ax.scatter(income, food, s=10, color="gray", alpha=0.6)
grid = np.linspace(income.min(), income.max(), 50)
for t, col in [(0.1, "C0"), (0.25, "C9"), (0.5, "C2"), (0.75, "C1"), (0.9, "C4")]:
    b = coef[np.argmin(np.abs(taus - t))]
    ax.plot(grid, b[0] + b[1] * grid, color=col, lw=1.8, label=f"tau = {t}")
ax.plot(grid, ols[0] + ols[1] * grid, color="C3", ls="--", lw=2, label="least squares")
ax.set_xlabel("household income")
ax.set_ylabel("food expenditure")
ax.set_title("Simulated data (n = 235): fanning out")
ax.legend(frameon=False, fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
ax.fill_between(taus, lo, hi, color="C0", alpha=0.25, label="90% bootstrap band")
ax.plot(taus, coef[:, 1], "o-", color="C0", lw=1.8, ms=4, label="quantile regression slope")
ax.axhline(ols[1], color="C3", ls="--", lw=2, label="least squares slope")
ax.set_xlabel("tau")
ax.set_ylabel("slope on income")
ax.set_title("The slope depends on the quantile")
ax.legend(frameon=False, fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
