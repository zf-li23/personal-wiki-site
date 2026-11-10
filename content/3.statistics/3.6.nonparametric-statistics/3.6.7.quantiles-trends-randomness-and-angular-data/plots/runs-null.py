"""Exact null distribution of the number of runs for m = n = 10, with the normal approximation."""

import numpy as np
import matplotlib.pyplot as plt
from math import comb
from scipy import stats


def runs_pmf(m, n):
    total = comb(m + n, m)
    r = np.arange(2, m + n + 1)
    p = np.zeros(len(r))
    for k, rr in enumerate(r):
        s = rr // 2
        if rr % 2 == 0:
            p[k] = 2 * comb(m - 1, s - 1) * comb(n - 1, s - 1)
        else:
            p[k] = comb(m - 1, s - 1) * comb(n - 1, s) + comb(m - 1, s) * comb(n - 1, s - 1)
    return r, p / total


m = n = 10
N = m + n
r, p = runs_pmf(m, n)
mean = 1 + 2 * m * n / N
var = 2 * m * n * (2 * m * n - N) / (N**2 * (N - 1))

fig, ax = plt.subplots(figsize=(8, 4.2))
reject = (r <= 6) | (r >= 16)
ax.bar(r[~reject], p[~reject], color="C0", alpha=0.7, label="acceptance region 7 <= R <= 15")
ax.bar(r[reject], p[reject], color="C3", alpha=0.8, label="rejection region (size 0.037)")
grid = np.linspace(1.5, N + 0.5, 300)
ax.plot(grid, stats.norm.pdf(grid, mean, np.sqrt(var)), color="C1", lw=2,
        label=f"normal approximation, mean {mean:.0f}, var {var:.2f}")
for obs, lab in [(3, "sequence I"), (20, "sequence II")]:
    ax.annotate(f"{lab}: R = {obs}", xy=(obs, 0.004), xytext=(obs, 0.06),
                ha="center", arrowprops=dict(arrowstyle="->"))
ax.annotate("sequence III: R = 13", xy=(13, p[r == 13][0]), xytext=(16.5, 0.15),
            arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("number of runs R")
ax.set_ylabel("probability")
ax.set_title("Runs test, m = n = 10")
ax.set_xticks(r)
ax.legend(frameon=False, loc="upper left", fontsize=9)
ax.grid(alpha=0.3, axis="y")
fig.tight_layout()
