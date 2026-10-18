"""Toluca data: pointwise confidence intervals, Working-Hotelling band and prediction intervals."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([80, 30, 50, 90, 70, 60, 120, 80, 100, 50, 40, 70, 90, 20, 110, 100, 30, 50, 90, 110, 30, 90, 40, 80, 70], float)
y = np.array([399, 121, 221, 376, 361, 224, 546, 352, 353, 157, 160, 252, 389, 113, 435, 420, 212, 268, 377, 421, 273,
              468, 244, 342, 323], float)
n = len(x)
sxx = np.sum((x - x.mean()) ** 2)
b1 = np.sum((x - x.mean()) * (y - y.mean())) / sxx
b0 = y.mean() - b1 * x.mean()
mse = np.sum((y - b0 - b1 * x) ** 2) / (n - 2)

g = np.linspace(15, 125, 300)
fit = b0 + b1 * g
se_mean = np.sqrt(mse * (1 / n + (g - x.mean()) ** 2 / sxx))
se_pred = np.sqrt(mse * (1 + 1 / n + (g - x.mean()) ** 2 / sxx))
t = stats.t.ppf(0.975, n - 2)
w = np.sqrt(2 * stats.f.ppf(0.95, 2, n - 2))

fig, ax = plt.subplots(figsize=(8, 5))
ax.fill_between(g, fit - t * se_pred, fit + t * se_pred, color="C2", alpha=0.15, label="95% prediction intervals")
ax.plot(g, fit - w * se_mean, color="C1", lw=1.5, ls="--", label=f"95% Working-Hotelling band (W = {w:.3f})")
ax.plot(g, fit + w * se_mean, color="C1", lw=1.5, ls="--")
ax.plot(g, fit - t * se_mean, color="C3", lw=1.2, label=f"95% pointwise confidence intervals (t = {t:.3f})")
ax.plot(g, fit + t * se_mean, color="C3", lw=1.2)
ax.plot(g, fit, color="black", lw=1.5, label=f"Y_hat = {b0:.2f} + {b1:.3f} X")
ax.plot(x, y, "o", color="C0", ms=5, zorder=3)
ax.axvline(x.mean(), color="gray", lw=0.8, ls=":")
ax.set_xlabel("lot size")
ax.set_ylabel("work hours")
ax.set_title("Toluca Company: intervals for the mean, the line and new observations", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
