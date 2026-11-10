"""Kolmogorov distance between an EDF and a CDF, and its distribution-free null distribution."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(10)
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))

# Left: an exponential sample of size 100 against the Exp(1) CDF
n = 100
x = np.sort(rng.exponential(size=n))
F = stats.expon.cdf(x)
up = np.arange(1, n + 1) / n - F          # F_n(x_(i)) - F(x_(i))
down = F - np.arange(0, n) / n            # F(x_(i)) - F_n(x_(i)-)
i_up, i_down = np.argmax(up), np.argmax(down)
dn = max(up[i_up], down[i_down])
ax = axes[0]
ax.step(np.r_[0, x], np.r_[0, np.arange(1, n + 1) / n], where="post", color="C0", lw=1.5,
        label="EDF F_n")
xx = np.linspace(0, x.max() * 1.02, 400)
ax.plot(xx, stats.expon.cdf(xx), color="C3", lw=1.5, label="CDF of Exp(1)")
if up[i_up] >= down[i_down]:
    x0, lo, hi = x[i_up], F[i_up], (i_up + 1) / n
else:
    x0, lo, hi = x[i_down], i_down / n, F[i_down]
ax.plot([x0, x0], [lo, hi], color="C2", lw=3, label=f"largest gap D_n = {dn:.3f}")
ax.set_xlabel("x")
ax.set_ylabel("probability")
ax.set_title("Kolmogorov distance, exponential sample, n = 100", fontsize=10)
ax.legend(fontsize=8, loc="lower right")
ax.grid(alpha=0.3)

# Right: null distribution of sqrt(n) D_n for four continuous populations
n, nrep = 20, 10000
dists = {"normal": stats.norm(), "exponential": stats.expon(), "Beta(2, 5)": stats.beta(2, 5),
         "Gamma(3)": stats.gamma(3)}
ax = axes[1]
grid = np.linspace(0, 2.2, 300)
for k, (name, d) in enumerate(dists.items()):
    s = np.sort(d.rvs(size=(nrep, n), random_state=rng), axis=1)
    u = d.cdf(s)
    i = np.arange(1, n + 1)
    dnk = np.maximum((i / n - u).max(axis=1), (u - (i - 1) / n).max(axis=1))
    ax.plot(np.sort(np.sqrt(n) * dnk), np.arange(1, nrep + 1) / nrep, color=f"C{k}", lw=1.5,
            label=name)
ax.plot(grid, stats.kstwobign.cdf(grid), color="gray", lw=2, ls="--",
        label="limit as n grows (Kolmogorov)")
ax.set_xlabel("sqrt(n) D_n")
ax.set_ylabel("cumulative proportion")
ax.set_title("Null distribution of sqrt(n) D_n, n = 20, 10000 samples each", fontsize=10)
ax.legend(fontsize=8, loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()
