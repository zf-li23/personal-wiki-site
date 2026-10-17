"""Confidence region for (mu, sigma^2) of a normal sample."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, alpha = 30, 0.05
x = rng.standard_normal(n)
xbar = x.mean()
ss = np.sum((x - xbar) ** 2)
gamma = (1 - np.sqrt(1 - alpha)) / 2
c = stats.norm.ppf(1 - gamma)
s2_lo = ss / stats.chi2.ppf(1 - gamma, n - 1)
s2_hi = ss / stats.chi2.ppf(gamma, n - 1)

fig, ax = plt.subplots(figsize=(9, 4.8))
s2 = np.linspace(0, s2_hi * 1.25, 400)
half = c * np.sqrt(s2 / n)
ax.plot(xbar - half, s2, color="C0", lw=1.5)
ax.plot(xbar + half, s2, color="C0", lw=1.5, label="(mu - x_bar)^2 = c^2 sigma^2 / n")
band = np.linspace(s2_lo, s2_hi, 200)
hb = c * np.sqrt(band / n)
ax.fill_betweenx(band, xbar - hb, xbar + hb, color="C0", alpha=0.3, label="confidence region")
for v in (s2_lo, s2_hi):
    ax.axhline(v, color="C2", lw=1, ls="--")
ax.plot([0], [1], "x", color="C3", ms=10, mew=2, label="true (mu, sigma^2) = (0, 1)")
ax.plot([xbar], [ss / (n - 1)], "o", color="0.3", ms=4, label="(x_bar, s^2)")
ax.set_xlabel("mu")
ax.set_ylabel("sigma^2")
ax.set_ylim(0, s2_hi * 1.25)
ax.set_title(f"95% confidence region, n = {n}")
ax.legend(frameon=False, loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=9)
fig.tight_layout()
