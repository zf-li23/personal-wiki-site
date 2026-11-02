"""Lindley's paradox: data with z = 1.96 (two-sided p = 0.05) increasingly favor H0 as n grows."""

import numpy as np
import matplotlib.pyplot as plt

n = np.logspace(0, 6, 300)
fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))
for z, color in [(1.96, "C3"), (2.58, "C0"), (3.29, "C2")]:
    # y_i ~ N(mu, 1); H0: mu = 0; H1: mu ~ N(0, 1); z = sqrt(n) * ybar
    bf01 = np.sqrt(n + 1) * np.exp(-z**2 * n / (2 * (n + 1)))
    label = f"z = {z} (p = {dict([(1.96, '0.05'), (2.58, '0.01'), (3.29, '0.001')])[z]})"
    axes[0].plot(n, bf01, color=color, lw=1.8, label=label)
    axes[1].plot(n, bf01 / (1 + bf01), color=color, lw=1.8, label=label)
axes[0].axhline(1, color="0.5", lw=1, ls="--")
axes[0].set_xscale("log")
axes[0].set_yscale("log")
axes[0].set_ylabel(r"$\mathrm{BF}_{01}$")
axes[0].set_title("Bayes factor for H0 at fixed z", fontsize=11)
axes[1].set_xscale("log")
axes[1].set_ylim(0, 1)
axes[1].set_ylabel(r"$\mathbb{P}(H_0\mid y)$ with prior 1/2")
axes[1].set_title("posterior probability of H0", fontsize=11)
for ax in axes:
    ax.set_xlabel("sample size n")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
fig.tight_layout()
