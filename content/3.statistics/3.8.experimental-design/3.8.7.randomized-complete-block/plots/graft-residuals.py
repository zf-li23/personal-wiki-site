"""Residual diagnostics for the vascular graft RCBD (additive model)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

psi = np.array([8500, 8700, 8900, 9100])
y = np.array([[90.3, 89.2, 98.2, 93.9, 87.4, 97.9],
              [92.5, 89.5, 90.6, 94.7, 87.0, 95.8],
              [85.5, 90.8, 89.6, 86.2, 88.0, 93.4],
              [82.5, 89.5, 85.6, 87.4, 78.9, 90.7]])
a, b = y.shape
fitted = y.mean(axis=1, keepdims=True) + y.mean(axis=0, keepdims=True) - y.mean()
resid = y - fitted
mse = (resid ** 2).sum() / ((a - 1) * (b - 1))
d = resid / np.sqrt(mse)
level = np.repeat(psi, b).reshape(a, b)
block = np.tile(np.arange(1, b + 1), (a, 1))

fig, axes = plt.subplots(2, 2, figsize=(10, 7.5))
ax = axes[0, 0]
ax.scatter(fitted.ravel(), resid.ravel(), s=22)
ax.axhline(0, color="gray", lw=1)
ax.set_xlabel("fitted value")
ax.set_ylabel("residual")
ax.set_title("Residuals vs fitted")

ax = axes[0, 1]
(osm, osr), (slope, icpt, _) = stats.probplot(d.ravel())
ax.scatter(osm, osr, s=22)
ax.plot(osm, icpt + slope * osm, color="C1", lw=1.5)
ax.set_xlabel("theoretical normal quantile")
ax.set_ylabel("standardized residual")
ax.set_title("Normal probability plot")

ax = axes[1, 0]
ax.scatter(level.ravel(), resid.ravel(), s=22)
ax.axhline(0, color="gray", lw=1)
ax.set_xticks(psi)
ax.set_xlabel("extrusion pressure (psi)")
ax.set_ylabel("residual")
ax.set_title("Residuals by treatment")

ax = axes[1, 1]
ax.scatter(block.ravel(), resid.ravel(), s=22)
ax.axhline(0, color="gray", lw=1)
ax.set_xticks(np.arange(1, b + 1))
ax.set_xlabel("batch of resin (block)")
ax.set_ylabel("residual")
ax.set_title("Residuals by block")
for ax in axes.ravel():
    ax.grid(alpha=0.3)
fig.tight_layout()
