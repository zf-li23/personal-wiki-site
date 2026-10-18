"""Typical residual plots: no problem, nonlinearity, nonconstant variance, dependence over time."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)


def fit_resid(x, y):
    b1, b0 = np.polyfit(x, y, 1)
    return y - (b0 + b1 * x)


fig, axes = plt.subplots(2, 2, figsize=(9, 6.6))

x = np.linspace(1, 30, 30)
e = fit_resid(x, 30 + 5 * x + 25 * rng.normal(size=x.size))
axes[0, 0].plot(x, e, "o", color="C0", ms=4)
axes[0, 0].set_title("(a) no violation: a horizontal band", fontsize=10)
axes[0, 0].set_xlabel("X")

e = fit_resid(x, x**2 - 10 * x + 30 + 25 * rng.normal(size=x.size))
axes[0, 1].plot(x, e, "o", color="C1", ms=4)
axes[0, 1].set_title("(b) nonlinearity: Y = X^2 - 10X + 30 + error", fontsize=10)
axes[0, 1].set_xlabel("X")

x2 = np.arange(1, 101)
e = fit_resid(x2, 30 + 100 * x2 + 10 * x2 * rng.normal(size=x2.size))
axes[1, 0].plot(x2, e, "o", color="C2", ms=3.5)
axes[1, 0].set_title("(c) nonconstant variance: SD of error = 10X", fontsize=10)
axes[1, 0].set_xlabel("X")

t = np.arange(1, 41)
u = rng.normal(size=t.size)
eps = np.zeros(t.size)
for i in range(t.size):
    eps[i] = (0.85 * eps[i - 1] if i else 0.0) + u[i]
xt = rng.uniform(0, 10, t.size)
e = fit_resid(xt, 2 + 0.5 * xt + eps)
axes[1, 1].plot(t, e, "o-", color="C4", ms=3.5, lw=0.8)
axes[1, 1].set_title("(d) dependence: AR(1) errors, rho = 0.85", fontsize=10)
axes[1, 1].set_xlabel("time order")

for ax in axes.flat:
    ax.axhline(0, color="0.5", lw=1)
    ax.set_ylabel("residual e_i")
    ax.grid(alpha=0.3)
fig.tight_layout()
