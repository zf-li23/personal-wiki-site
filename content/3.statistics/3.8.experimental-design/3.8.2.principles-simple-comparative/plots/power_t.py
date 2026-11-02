"""Two-sample t-test: null and alternative distributions, and power against n."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

alpha = 0.05
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))

# Left: n = 10 per group, standardized difference d = 1.2
n, d = 10, 1.2
df = 2 * n - 2
ncp = d / np.sqrt(2 / n)
c = stats.t.ppf(1 - alpha / 2, df)
x = np.linspace(-4.5, 8, 800)
f0 = stats.t.pdf(x, df)
f1 = stats.nct.pdf(x, df, ncp)
ax = axes[0]
ax.plot(x, f0, color="C0", lw=2, label="H0: central t, df 18")
ax.plot(x, f1, color="C3", lw=2, label=f"H1: noncentral t, ncp {ncp:.2f}")
ax.fill_between(x, f0, where=np.abs(x) > c, color="C0", alpha=0.35, label="alpha (two tails)")
ax.fill_between(x, f1, where=np.abs(x) <= c, color="C3", alpha=0.25, label="beta")
for s in (-c, c):
    ax.axvline(s, color="gray", ls="--", lw=1)
power = stats.nct.sf(c, df, ncp) + stats.nct.cdf(-c, df, ncp)
ax.set_title(f"n = 10 per group, d = 1.2: power = {power:.2f}", fontsize=10)
ax.set_xlabel("t statistic")
ax.set_ylabel("density")
ax.legend(fontsize=8, loc="upper right")
ax.grid(alpha=0.3)

# Right: power curves against n per group
ns = np.arange(2, 61)
ax = axes[1]
for k, dd in enumerate([0.5, 1.0, 1.5]):
    dfs = 2 * ns - 2
    cs = stats.t.ppf(1 - alpha / 2, dfs)
    nc = dd / np.sqrt(2 / ns)
    pw = stats.nct.sf(cs, dfs, nc) + stats.nct.cdf(-cs, dfs, nc)
    ax.plot(ns, pw, color=f"C{k}", lw=2, label=f"d = {dd}")
ax.axhline(0.8, color="gray", ls=":", lw=1)
ax.set_xlabel("n per group")
ax.set_ylabel("power")
ax.set_ylim(0, 1.02)
ax.set_title("Power curves, two-sided two-sample t-test, alpha = 0.05", fontsize=10)
ax.legend(fontsize=9, loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()
