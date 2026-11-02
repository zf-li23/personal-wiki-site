"""Densities of the inverse-chi-square and scaled inverse-chi-square distributions."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))
x = np.linspace(1e-3, 1.5, 1000)
for nu, c in zip([1, 2, 3, 5, 10], ["C0", "C1", "C2", "C3", "C4"]):
    # Inv-chi2_nu = Inv-Gamma(nu/2, 1/2)
    axes[0].plot(x, stats.invgamma(nu / 2, scale=0.5).pdf(x), color=c, lw=1.6, label=rf"$\nu$ = {nu}")
axes[0].set_title(r"inverse-$\chi^2_\nu$", fontsize=11)
axes[0].set_ylim(0, 4)

x = np.linspace(1e-3, 4, 1000)
nu = 5
for s2, c in zip([0.25, 0.5, 1, 2], ["C0", "C1", "C2", "C3"]):
    # scaled Inv-chi2(nu, s2) = Inv-Gamma(nu/2, nu s2/2)
    axes[1].plot(x, stats.invgamma(nu / 2, scale=nu * s2 / 2).pdf(x), color=c, lw=1.6, label=rf"$s^2$ = {s2}")
axes[1].set_title(r"scaled inverse-$\chi^2(\nu = 5, s^2)$", fontsize=11)
for ax in axes:
    ax.set_xlabel("x")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("density")
fig.tight_layout()
