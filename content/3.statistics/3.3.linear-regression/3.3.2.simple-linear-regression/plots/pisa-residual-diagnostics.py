"""Residual plot and normal Q-Q plot of the residuals for the Pisa regression."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

year = np.arange(75, 88, dtype=float)
lean = np.array([642, 644, 656, 667, 673, 688, 696, 698, 713, 717, 725, 742, 757], dtype=float)
sxx = np.sum((year - year.mean()) ** 2)
b1 = np.sum((year - year.mean()) * (lean - lean.mean())) / sxx
b0 = lean.mean() - b1 * year.mean()
resid = lean - (b0 + b1 * year)
n = len(resid)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
ax.plot(year, resid, "o", color="C0")
ax.axhline(0, color="black", lw=1)
ax.set_xlabel("year (19xx)")
ax.set_ylabel("residual")
ax.set_title("Residuals against the predictor", fontsize=10)
ax.grid(alpha=0.3)

ax = axes[1]
q = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)
r = np.sort(resid)
ax.plot(q, r, "o", color="C0")
q1, q3 = np.percentile(resid, [25, 75])
z1, z3 = stats.norm.ppf([0.25, 0.75])
slope = (q3 - q1) / (z3 - z1)
t = np.array([-2, 2])
ax.plot(t, q1 + slope * (t - z1), color="C3", lw=1.5, label="line through the quartiles")
ax.set_xlabel("standard normal quantile")
ax.set_ylabel("ordered residual")
ax.set_title("Normal Q-Q plot of the residuals", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
