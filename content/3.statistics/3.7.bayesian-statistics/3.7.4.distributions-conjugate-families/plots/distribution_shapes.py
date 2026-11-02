"""Shapes of standard distributions: symmetric families with unit variance (linear and log scale)
and positive families with mean 1 and variance 1/4."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

nu = 5
symmetric = [
    ("normal", stats.norm(0, 1), "C0"),
    (rf"$t_{nu}$ (scaled to variance 1)", stats.t(nu, scale=np.sqrt((nu - 2) / nu)), "C3"),
    ("Laplace", stats.laplace(scale=1 / np.sqrt(2)), "C2"),
    ("logistic", stats.logistic(scale=np.sqrt(3) / np.pi), "C1"),
]
s2 = np.log(1.25)  # lognormal with mean 1 and variance 1/4
positive = [
    ("Gamma(4, 4)", stats.gamma(4, scale=1 / 4), "C0"),
    ("Inv-Gamma(6, 5)", stats.invgamma(6, scale=5), "C3"),
    ("lognormal", stats.lognorm(np.sqrt(s2), scale=np.exp(-s2 / 2)), "C2"),
]

fig, axes = plt.subplots(1, 3, figsize=(13, 3.9))
x = np.linspace(-4, 4, 800)
for label, d, c in symmetric:
    axes[0].plot(x, d.pdf(x), color=c, lw=1.7, label=label)
    axes[1].semilogy(np.linspace(0, 8, 800), d.pdf(np.linspace(0, 8, 800)), color=c, lw=1.7, label=label)
axes[0].set_title("mean 0, variance 1", fontsize=11)
axes[1].set_title("right tails (log scale)", fontsize=11)
axes[1].set_ylim(1e-7, 1)
x = np.linspace(1e-3, 3, 800)
for label, d, c in positive:
    axes[2].plot(x, d.pdf(x), color=c, lw=1.7, label=label)
axes[2].set_title("mean 1, variance 1/4", fontsize=11)
for ax in axes:
    ax.set_xlabel("x")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("density")
fig.tight_layout()
