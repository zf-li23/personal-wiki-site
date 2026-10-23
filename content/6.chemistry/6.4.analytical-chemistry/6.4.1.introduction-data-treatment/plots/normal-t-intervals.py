"""Left: standard normal density with the probabilities of |u| < 1, 2, 3 and the t densities
with 2 and 5 degrees of freedom (heavier tails). Right: half-width of the 95 % confidence
interval of the mean, in units of the standard deviation, as a function of the number of
replicates n: t_{n-1,0.025}/sqrt(n) (sigma estimated by s) versus 1.96/sqrt(n) (sigma known)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

u = np.linspace(-4.5, 4.5, 600)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.0))
phi = stats.norm.pdf(u)
for k, alpha in [(3, 0.12), (2, 0.20), (1, 0.30)]:
    m = np.abs(u) <= k
    ax1.fill_between(u[m], 0, phi[m], color="C0", alpha=alpha, lw=0)
for k, p in [(1, 0.683), (2, 0.954), (3, 0.997)]:
    ax1.annotate(f"{p:.1%}", xy=(0, 0), xytext=(0, 0.02 + 0.075 * (3 - k)), ha="center", fontsize=8.5)
    ax1.plot([-k, k], [0.012 + 0.075 * (3 - k)] * 2, color="C0", lw=0.8)
ax1.plot(u, phi, color="C0", lw=2, label="normal")
ax1.plot(u, stats.t.pdf(u, 5), color="C1", lw=1.5, ls="--", label=r"$t_5$")
ax1.plot(u, stats.t.pdf(u, 2), color="C3", lw=1.5, ls=":", label=r"$t_2$")
ax1.set_xlabel(r"$u = (x-\mu)/\sigma$  or  $t = (\bar{x}-\mu)/(s/\sqrt{n})$")
ax1.set_ylabel("probability density")
ax1.set_ylim(0, 0.45)
ax1.legend(frameon=False, fontsize=9)

n = np.arange(2, 21)
ax2.plot(n, stats.t.ppf(0.975, n - 1) / np.sqrt(n), "o-", color="C3", ms=4, label=r"$t_{n-1,0.025}/\sqrt{n}$ ($\sigma$ unknown)")
ax2.plot(n, 1.96 / np.sqrt(n), "s--", color="C0", ms=3.5, label=r"$1.96/\sqrt{n}$ ($\sigma$ known)")
ax2.set_yscale("log")
ax2.set_yticks([0.5, 1, 2, 5, 10])
ax2.set_yticklabels(["0.5", "1", "2", "5", "10"])
ax2.set_xlabel("number of replicates $n$")
ax2.set_ylabel("half-width of 95 % CI / standard deviation")
ax2.set_xticks([2, 4, 6, 8, 10, 15, 20])
ax2.legend(frameon=False, fontsize=9)
fig.tight_layout()
