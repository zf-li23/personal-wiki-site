"""Sampling distributions of OLS and WLS estimates when the error SD is proportional to X."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = np.arange(1.0, 101.0)
X = np.column_stack([np.ones_like(x), x])
w = 1 / x**2
Xw = X * np.sqrt(w)[:, None]
reps = 4000
ols = np.empty((reps, 2))
wls = np.empty((reps, 2))
for r in range(reps):
    y = 30 + 100 * x + 10 * x * rng.normal(size=x.size)
    ols[r] = np.linalg.lstsq(X, y, rcond=None)[0]
    wls[r] = np.linalg.lstsq(Xw, y * np.sqrt(w), rcond=None)[0]

fig, axes = plt.subplots(1, 2, figsize=(10, 4.0))
for j, (ax, name, truth) in enumerate(zip(axes, ["intercept b0", "slope b1"], [30, 100])):
    lo, hi = np.quantile(np.concatenate([ols[:, j], wls[:, j]]), [0.002, 0.998])
    bins = np.linspace(lo, hi, 60)
    ax.hist(ols[:, j], bins=bins, density=True, alpha=0.5, color="C0", label=f"OLS, SD = {ols[:, j].std():.2f}")
    ax.hist(wls[:, j], bins=bins, density=True, alpha=0.5, color="C3", label=f"WLS (w = 1/X^2), SD = {wls[:, j].std():.2f}")
    ax.axvline(truth, color="0.4", ls="--", lw=1)
    ax.set_title(f"{name}: true value {truth}", fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
fig.suptitle("Y = 30 + 100 X + 10 X eps, 4000 simulated data sets: both unbiased, WLS far more precise", fontsize=10)
fig.tight_layout()
