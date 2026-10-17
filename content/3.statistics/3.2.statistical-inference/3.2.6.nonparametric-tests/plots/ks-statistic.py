"""Empirical distribution function of a sample versus a hypothesized normal CDF, with the KS statistic marked."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
x = np.sort(rng.normal(0.5, 1.0, size=30))   # true distribution N(0.5, 1)
n = len(x)
f0 = stats.norm.cdf(x)                          # hypothesized F0 = N(0, 1)

# KS statistic: largest gap just after or just before a jump of F_n
upper = np.arange(1, n + 1) / n - f0
lower = f0 - np.arange(0, n) / n
i_up, i_lo = np.argmax(upper), np.argmax(lower)
if upper[i_up] >= lower[i_lo]:
    xk, y_emp, y_0 = x[i_up], (i_up + 1) / n, f0[i_up]
else:
    xk, y_emp, y_0 = x[i_lo], i_lo / n, f0[i_lo]
d = abs(y_emp - y_0)

grid = np.linspace(-3, 4, 400)
fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.plot(grid, stats.norm.cdf(grid), color="C0", lw=2, label="hypothesized $F_0 = N(0,1)$")
ax.step(np.concatenate([[-3], x, [4]]), np.concatenate([[0], np.arange(1, n + 1) / n, [1]]),
        where="post", color="C1", lw=1.8, label="empirical $F_n$ ($n = 30$)")
ax.annotate("", xy=(xk, y_emp), xytext=(xk, y_0),
            arrowprops=dict(arrowstyle="<->", color="C3", lw=1.8, shrinkA=0, shrinkB=0))
ax.text(xk + 0.12, (y_emp + y_0) / 2, f"$D_n = {d:.3f}$", color="C3", fontsize=11, va="center")
ax.set_xlim(-3, 4)
ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("$x$")
ax.set_ylabel("cumulative probability")
ax.grid(alpha=0.3)
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
