"""Power functions of Z tests for a normal mean (mu0 = 1, sigma^2 = 4, alpha = 0.05)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

alpha, mu0, sigma = 0.05, 1.0, 2.0
mu = np.linspace(-1, 3, 400)
Phi = stats.norm.cdf
za2 = stats.norm.ppf(1 - alpha / 2)
za = stats.norm.ppf(1 - alpha)


def two_sided(n):
    d = np.sqrt(n) * (mu0 - mu) / sigma
    return 1 - Phi(za2 + d) + Phi(-za2 + d)


def one_sided(n):
    return 1 - Phi(za + np.sqrt(n) * (mu0 - mu) / sigma)


fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
ax = axes[0]
for k, n in enumerate([20, 50, 200]):
    ax.plot(mu, two_sided(n), color=f"C{k}", lw=1.8, label=f"n = {n}")
ax.set_title(r"Two-sided test $|Z| > z_{\alpha/2}$", fontsize=11)
ax.set_ylabel("power")
ax = axes[1]
ax.plot(mu, two_sided(50), color="C3", lw=1.8, label=r"$D$: $|Z| > z_{\alpha/2}$")
ax.plot(mu, one_sided(50), color="C0", lw=1.8, label=r"$D_2$: $Z > z_\alpha$")
ax.set_title("Two-sided versus one-sided region, n = 50", fontsize=11)
for ax in axes:
    ax.axhline(alpha, color="0.5", lw=0.9, ls="--")
    ax.axvline(mu0, color="0.5", lw=0.9, ls=":")
    ax.set_xlabel(r"$\mu$")
    ax.set_xlim(mu[0], mu[-1])
    ax.set_ylim(-0.02, 1.03)
    ax.text(-0.95, alpha + 0.02, r"$\alpha = 0.05$", fontsize=9)
    ax.legend(loc="center left", fontsize=9, frameon=False)
fig.tight_layout()
