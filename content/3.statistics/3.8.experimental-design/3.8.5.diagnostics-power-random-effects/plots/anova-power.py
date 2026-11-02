"""Power of the one-way ANOVA F-test from the noncentral F-distribution, etching example."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a, sigma = 4, 25.0
means = np.array([575, 600, 650, 675], float)
tau = means - means.mean()
ns = np.arange(2, 9)
grid = np.linspace(2, 8, 200)


def power(n, ss_tau, alpha):
    lam = n * ss_tau / sigma ** 2
    df2 = a * (n - 1)
    crit = stats.f.ppf(1 - alpha, a - 1, df2)
    return stats.ncf.sf(crit, a - 1, df2, lam)


fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axes[0]
for alpha, ls in [(0.05, "-"), (0.01, "--")]:
    ax.plot(grid, power(grid, (tau ** 2).sum(), alpha), ls=ls, color="C0",
            label=f"means 575, 600, 650, 675; alpha = {alpha}")
    ax.plot(grid, power(grid, 75 ** 2 / 2, alpha), ls=ls, color="C1",
            label=f"only max difference 75; alpha = {alpha}")
ax.axhline(0.9, color="gray", lw=1)
ax.axvline(3.52, color="C0", lw=0.8, ls=":")
ax.set_xlabel("replicates per level n")
ax.set_ylabel("power")
ax.set_title("Power of the F-test (a = 4, sigma = 25)")
ax.legend(fontsize=8, loc="lower right")

ax = axes[1]
x = np.linspace(0.01, 14, 400)
n = 4
df2 = a * (n - 1)
lam = n * (tau ** 2).sum() / sigma ** 2
crit = stats.f.ppf(0.99, a - 1, df2)
ax.plot(x, stats.f.pdf(x, a - 1, df2), label="central F(3, 12): H0 true")
ax.plot(x, stats.ncf.pdf(x, a - 1, df2, lam), label=f"noncentral F(3, 12, lambda = {lam:.0f})")
xs = x[x > crit]
ax.fill_between(xs, stats.ncf.pdf(xs, a - 1, df2, lam), alpha=0.3, color="C1", label="power")
ax.axvline(crit, color="gray", ls="--", lw=1, label=f"critical value {crit:.2f} (alpha = 0.01)")
ax.set_xlabel("F")
ax.set_ylabel("density")
ax.set_title("Null and alternative distributions, n = 4")
ax.legend(fontsize=8)
for ax in axes:
    ax.grid(alpha=0.3)
fig.tight_layout()
