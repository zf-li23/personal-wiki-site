"""Exact null distribution of the Mann-Whitney U for n1 = 10, n2 = 11, with the normal approximation."""

import numpy as np
import matplotlib.pyplot as plt
from functools import lru_cache
from math import comb
from scipy import stats

n1, n2 = 10, 11


@lru_cache(maxsize=None)
def count(u, m, n):
    # number of arrangements of m x's and n y's with U_x = u
    if u < 0:
        return 0
    if m == 0 or n == 0:
        return 1 if u == 0 else 0
    return count(u - n, m - 1, n) + count(u, m, n - 1)


u = np.arange(n1 * n2 + 1)
p = np.array([count(int(k), n1, n2) for k in u]) / comb(n1 + n2, n1)
mean, var = n1 * n2 / 2, n1 * n2 * (n1 + n2 + 1) / 12
crit = 26
fig, ax = plt.subplots(figsize=(8, 4.2))
tail = (u <= crit) | (u >= n1 * n2 - crit)
ax.bar(u[~tail], p[~tail], width=1, color="C0", alpha=0.7, label="exact null distribution")
ax.bar(u[tail], p[tail], width=1, color="C3", alpha=0.8,
       label=f"rejection region U <= {crit} or U >= {n1 * n2 - crit} (size 0.043)")
grid = np.linspace(0, n1 * n2, 400)
ax.plot(grid, stats.norm.pdf(grid, mean, np.sqrt(var)), color="C1", lw=2,
        label=f"normal approximation, mean {mean:.0f}, sd {np.sqrt(var):.1f}")
ax.annotate("calculator data: U = 21", xy=(21, p[21]), xytext=(4, 0.03),
            arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("U")
ax.set_ylabel("probability")
ax.set_title("Wilcoxon-Mann-Whitney test, n1 = 10, n2 = 11")
ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.grid(alpha=0.3, axis="y")
fig.tight_layout()
