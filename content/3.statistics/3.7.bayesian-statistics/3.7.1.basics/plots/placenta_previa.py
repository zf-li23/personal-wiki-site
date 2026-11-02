"""Placenta previa example: 437 girls in 980 births under a uniform, a non-conjugate and conjugate priors."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

y, n = 437, 980
t = np.linspace(0, 1, 20001)

# non-conjugate prior: half of the mass uniform on [0, 1], half triangular on [0.385, 0.585]
tri = np.clip(1 - np.abs(t - 0.485) / 0.1, 0, None)
tri /= np.trapezoid(tri, t)
prior = 0.5 + 0.5 * tri
post = prior * stats.binom.pmf(y, n, t)
post /= np.trapezoid(post, t)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
axes[0].plot(t, prior, color="C1", lw=1.6)
axes[0].set_title("non-conjugate prior", fontsize=11)
axes[0].set_xlabel(r"$\theta$")
axes[0].set_ylabel("density")

zoom = (t > 0.38) & (t < 0.52)
axes[1].plot(t[zoom], stats.beta(y + 1, n - y + 1).pdf(t[zoom]), color="C0", lw=1.6, label="uniform prior")
axes[1].plot(t[zoom], post[zoom], color="C1", lw=1.6, ls="--", label="non-conjugate prior")
axes[1].axvline(0.485, color="0.5", ls=":", lw=1)
axes[1].set_title("posteriors", fontsize=11)
axes[1].set_xlabel(r"$\theta$")
axes[1].legend(fontsize=9)

for s, c in zip([2, 20, 100, 200, 1000], ["C0", "C2", "C3", "C4", "C5"]):
    d = stats.beta(0.485 * s + y, 0.515 * s + n - y)
    axes[2].plot(t[zoom], d.pdf(t[zoom]), color=c, lw=1.5, label=rf"$\alpha+\beta$ = {s}")
axes[2].axvline(0.485, color="0.5", ls=":", lw=1)
axes[2].set_title("conjugate priors with mean 0.485", fontsize=11)
axes[2].set_xlabel(r"$\theta$")
axes[2].legend(fontsize=8)
for ax in axes:
    ax.grid(alpha=0.3)
fig.tight_layout()
