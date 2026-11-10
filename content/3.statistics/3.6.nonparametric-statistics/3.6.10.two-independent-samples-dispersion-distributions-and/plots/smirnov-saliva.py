"""Empirical distribution functions of saliva production for 7 women and 21 men, and the Smirnov distance."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fe = np.array([0.45, 0.60, 0.80, 0.85, 0.95, 1.00, 1.75])
ma = np.array([0.40, 0.50, 0.55, 0.65, 0.70, 0.75, 0.90, 1.05, 1.15, 1.25, 1.30,
               1.35, 1.45, 1.50, 1.85, 1.90, 2.30, 2.55, 2.70, 2.85, 3.85])


def edf(sample, t):
    return np.searchsorted(np.sort(sample), t, side="right") / len(sample)


grid = np.sort(np.concatenate([fe, ma]))
diff = edf(fe, grid) - edf(ma, grid)
k = np.argmax(np.abs(diff))
res = stats.ks_2samp(fe, ma, method="exact")

fig, ax = plt.subplots(figsize=(8, 4.4))
t = np.linspace(0.2, 4.0, 2000)
ax.step(t, edf(fe, t), where="post", color="C3", lw=2, label="women (m = 7)")
ax.step(t, edf(ma, t), where="post", color="C0", lw=2, label="men (n = 21)")
x0 = grid[k]
ax.vlines(x0, edf(ma, x0), edf(fe, x0), color="k", lw=2.5)
ax.annotate(f"D = {abs(diff[k]):.3f} at x = {x0:.2f}", xy=(x0, (edf(ma, x0) + edf(fe, x0)) / 2),
            xytext=(1.6, 0.45), arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("saliva production (ml/min)")
ax.set_ylabel("empirical distribution function")
ax.set_title(f"Smirnov test: exact two-sided p = {res.pvalue:.3f}")
ax.legend(frameon=False, loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()
