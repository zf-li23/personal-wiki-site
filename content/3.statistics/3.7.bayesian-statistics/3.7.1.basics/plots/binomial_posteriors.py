"""Posteriors Beta(y+1, n-y+1) of a binomial proportion under the uniform prior."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

t = np.linspace(0, 1, 801)
fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

ax = axes[0]
n = 10
ax.plot(t, np.ones_like(t), color="0.5", ls="--", lw=1.2, label="prior U(0, 1)")
for y, c in zip([0, 2, 5, 8, 10], ["C0", "C1", "C2", "C3", "C4"]):
    ax.plot(t, stats.beta(y + 1, n - y + 1).pdf(t), color=c, lw=1.6, label=f"y = {y}")
ax.set_title("n = 10, different y", fontsize=11)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("posterior density")
ax.set_ylim(0, 6)
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

ax = axes[1]
for n, c in zip([5, 20, 100, 500], ["C0", "C1", "C2", "C3"]):
    a, b = 0.3 * n + 1, 0.7 * n + 1
    ax.plot(t, stats.beta(a, b).pdf(t), color=c, lw=1.6, label=f"n = {n}")
ax.axvline(0.3, color="0.5", ls=":", lw=1)
ax.set_title("observed proportion y/n = 0.3, growing n", fontsize=11)
ax.set_xlabel(r"$\theta$")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
