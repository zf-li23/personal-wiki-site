"""Two-sided p-value functions of the sign, Wilcoxon signed-rank and t tests for H0: theta = theta0,
for the 12 heart-rate differences; the 95% intervals are the theta0 values with p > 0.05."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([-2, 4, 8, 25, -5, 16, 3, 1, 12, 17, 20, 9], dtype=float)
n = len(x)

# exact null distribution of the signed-rank statistic S+ for n observations
counts = np.zeros(n * (n + 1) // 2 + 1)
counts[0] = 1
for k in range(1, n + 1):
    shifted = np.zeros_like(counts)
    shifted[k:] = counts[:-k]
    counts = counts + shifted
sr_cdf = np.cumsum(counts) / 2**n


def p_sign(theta0):
    d = x - theta0
    k = min((d > 0).sum(), (d < 0).sum())
    return min(1.0, 2 * stats.binom.cdf(k, n, 0.5))


def p_wilcoxon(theta0):
    d = x - theta0
    ranks = stats.rankdata(np.abs(d))
    s_plus = ranks[d > 0].sum()
    s_min = min(s_plus, n * (n + 1) / 2 - s_plus)
    return min(1.0, 2 * sr_cdf[int(s_min)])


def p_t(theta0):
    t = (x.mean() - theta0) / (x.std(ddof=1) / np.sqrt(n))
    return 2 * stats.t.sf(abs(t), n - 1)


# a grid that avoids the data values and the Walsh averages, where the statistics jump
grid = np.arange(-8.0, 28.0, 0.01) + 0.0037
curves = {
    "sign test": ([p_sign(g) for g in grid], "C0"),
    "Wilcoxon signed-rank test": ([p_wilcoxon(g) for g in grid], "C1"),
    "$t$ test": ([p_t(g) for g in grid], "C2"),
}

fig, ax = plt.subplots(figsize=(7.8, 4.6))
for label, (p, color) in curves.items():
    ax.plot(grid, p, color=color, lw=1.8, label=label)
ax.axhline(0.05, color="0.4", ls="--", lw=1)
ax.text(27.5, 0.065, "$\\alpha = 0.05$", ha="right", color="0.4", fontsize=9)
# the three intervals as bars below the curves
intervals = [((1, 17), "C0"), ((2.5, 16), "C1"), ((3.12, 14.88), "C2")]
for j, ((lo, hi), color) in enumerate(intervals):
    y = -0.06 - 0.035 * j
    ax.plot([lo, hi], [y, y], color=color, lw=4, solid_capstyle="butt")
ax.plot(x, np.full(n, -0.18), "|", color="0.2", ms=10)
ax.text(-7.5, -0.18, "data", va="center", fontsize=8, color="0.2")
ax.set_xlim(-8, 28)
ax.set_ylim(-0.21, 1.03)
ax.set_xlabel("hypothesized median $\\theta_0$")
ax.set_ylabel("two-sided $p$-value")
ax.grid(alpha=0.3)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
