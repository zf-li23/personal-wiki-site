"""Radial probability densities r^2 R_nl^2 of hydrogen for n = 1, 2, 3."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre

rho = np.linspace(0, 30, 3000)  # r / a0
dr = rho[1] - rho[0]


def radial_density(n, l):
    x = 2 * rho / n
    R = x**l * np.exp(-x / 2) * genlaguerre(n - l - 1, 2 * l + 1)(x)
    P = rho**2 * R**2
    return P / (P.sum() * dr)  # normalize numerically


labels = "spd"
fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.8), sharey=True)
for n, ax in zip([1, 2, 3], axes):
    for l in range(n):
        ax.plot(rho, radial_density(n, l), color=f"C{l}", lw=1.7, label=f"{n}{labels[l]}")
    ax.axvline(n**2, color="0.6", lw=0.8, ls=":")
    ax.text(n**2 + 0.3, 0.52, rf"$r = {n * n}\,a_0$" if n > 1 else r"$r = a_0$", fontsize=8)
    ax.set_xlim(0, [6, 16, 28][n - 1])
    ax.set_ylim(0, 0.58)
    ax.set_xlabel(r"$r\,/\,a_0$")
    ax.set_title(f"n = {n}")
    ax.legend(fontsize=9)
axes[0].set_ylabel(r"$P_{nl}(r)\,a_0 = r^2 R_{nl}^2\,a_0$")

fig.tight_layout()
