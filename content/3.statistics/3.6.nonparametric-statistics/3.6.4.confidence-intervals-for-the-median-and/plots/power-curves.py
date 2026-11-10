"""Simulated power of the sign, Wilcoxon signed-rank and t tests (n = 20, one-sided, level 0.05)
against a shift theta, for normal data and for heavy-tailed t_3 data scaled to unit variance."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, alpha, reps = 20, 0.05, 4000
shifts = np.linspace(0, 1.0, 11)

# sign test randomized to exact level alpha: reject if K > c, with probability g if K = c
binom = stats.binom(n, 0.5)
c_sign = int(binom.isf(alpha))
g_sign = (alpha - binom.sf(c_sign)) / binom.pmf(c_sign)

# exact null distribution of S+, randomized to exact level alpha in the same way
counts = np.zeros(n * (n + 1) // 2 + 1)
counts[0] = 1
for k in range(1, n + 1):
    shifted = np.zeros_like(counts)
    shifted[k:] = counts[:-k]
    counts = counts + shifted
pmf = counts / 2**n
sf = 1 - np.cumsum(pmf)                 # sf[s] = P(S+ > s)
c_wil = int(np.argmax(sf <= alpha))
g_wil = (alpha - sf[c_wil]) / pmf[c_wil]
t_crit = stats.t.isf(alpha, n - 1)


def power(sampler):
    out = {"sign": [], "wilcoxon": [], "t": []}
    for theta in shifts:
        z = sampler((reps, n)) + theta
        k = (z > 0).sum(axis=1)
        out["sign"].append(np.mean((k > c_sign) + g_sign * (k == c_sign)))
        ranks = stats.rankdata(np.abs(z), axis=1)
        s = (ranks * (z > 0)).sum(axis=1).round().astype(int)
        out["wilcoxon"].append(np.mean((s > c_wil) + g_wil * (s == c_wil)))
        t = z.mean(axis=1) / (z.std(axis=1, ddof=1) / np.sqrt(n))
        out["t"].append(np.mean(t > t_crit))
    return out


samplers = {
    "normal data": lambda size: rng.standard_normal(size),
    "$t_3$ data (unit variance)": lambda size: rng.standard_t(3, size) / np.sqrt(3),
}
labels = {"sign": ("sign test", "C0"), "wilcoxon": ("Wilcoxon signed-rank", "C1"), "t": ("$t$ test", "C2")}

fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2), sharey=True)
for ax, (title, sampler) in zip(axes, samplers.items()):
    res = power(sampler)
    for key, (label, color) in labels.items():
        ax.plot(shifts, res[key], "o-", color=color, ms=3.5, lw=1.6, label=label)
    ax.axhline(alpha, color="0.5", ls=":", lw=1)
    ax.set_title(title, fontsize=11)
    ax.set_xlabel("shift $\\theta$ (in standard deviations)")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("power")
axes[0].legend(loc="upper left", fontsize=9)
fig.tight_layout()
