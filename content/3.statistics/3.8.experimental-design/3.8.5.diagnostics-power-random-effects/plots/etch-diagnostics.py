"""Residual diagnostics for the plasma etching experiment (one-way fixed-effects model)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

power = [160, 180, 200, 220]
rate = {160: [575, 542, 530, 539, 570], 180: [565, 593, 590, 579, 610],
        200: [600, 651, 610, 637, 629], 220: [725, 700, 715, 685, 710]}
order = {160: [13, 14, 8, 5, 4], 180: [18, 9, 6, 16, 17],
         200: [7, 19, 10, 20, 1], 220: [2, 3, 15, 11, 12]}

fitted, resid, runs, level = [], [], [], []
for p in power:
    y = np.array(rate[p], float)
    fitted += [y.mean()] * len(y)
    resid += list(y - y.mean())
    runs += order[p]
    level += [p] * len(y)
fitted, resid, runs, level = map(np.array, (fitted, resid, runs, level))
mse = (resid ** 2).sum() / (len(resid) - len(power))
d = resid / np.sqrt(mse)

fig, axes = plt.subplots(2, 2, figsize=(10, 7.5))
ax = axes[0, 0]
ax.scatter(fitted, resid, s=22)
ax.axhline(0, color="gray", lw=1)
ax.set_xlabel("fitted value (level mean)")
ax.set_ylabel("residual")
ax.set_title("Residuals vs fitted")

ax = axes[0, 1]
(osm, osr), (slope, icpt, _) = stats.probplot(d)
ax.scatter(osm, osr, s=22)
ax.plot(osm, icpt + slope * osm, color="C1", lw=1.5)
ax.set_xlabel("theoretical normal quantile")
ax.set_ylabel("standardized residual")
ax.set_title("Normal probability plot")

ax = axes[1, 0]
idx = np.argsort(runs)
ax.plot(runs[idx], resid[idx], "o-", ms=4, lw=1)
ax.axhline(0, color="gray", lw=1)
ax.set_xlabel("run order")
ax.set_ylabel("residual")
ax.set_title("Residuals vs run order")

ax = axes[1, 1]
ax.scatter(level, d, s=22)
for k in (-3, 3):
    ax.axhline(k, color="C3", ls="--", lw=1)
ax.axhline(0, color="gray", lw=1)
ax.set_xticks(power)
ax.set_ylim(-3.6, 3.6)
ax.set_xlabel("RF power (W)")
ax.set_ylabel("standardized residual")
ax.set_title("Standardized residuals by level")
for ax in axes.ravel():
    ax.grid(alpha=0.3)
fig.tight_layout()
