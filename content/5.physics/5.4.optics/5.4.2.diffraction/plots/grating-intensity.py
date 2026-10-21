"""Grating with N = 4 slits and d = 4a: single-slit factor, multi-beam factor, and their product."""

import numpy as np
import matplotlib.pyplot as plt

N, ratio = 4, 4.0                 # d = 4a
u = np.linspace(-9.0, 9.0, 18001)  # d sin(theta) / lambda
alpha = np.pi * u / ratio
beta = np.pi * u

single = np.sinc(u / ratio) ** 2
with np.errstate(divide="ignore", invalid="ignore"):
    multi = (np.sin(N * beta) / np.sin(beta)) ** 2
multi = np.where(np.isfinite(multi), multi, N ** 2)
total = single * multi

fig, axes = plt.subplots(3, 1, figsize=(8.0, 6.4), sharex=True)
axes[0].plot(u, single, color="C0", lw=1.4)
axes[0].set_ylabel("(sin α / α)²")
axes[1].plot(u, multi, color="C2", lw=1.0)
axes[1].set_ylabel("(sin Nβ / sin β)²")
axes[2].plot(u, total, color="C1", lw=1.2)
axes[2].plot(u, N ** 2 * single, color="0.55", lw=0.9, ls="--", label="envelope N² (sin α / α)²")
for k in (-8, -4, 4, 8):
    axes[2].annotate("missing", (k, 0.4), xytext=(0, 12), textcoords="offset points",
                     ha="center", fontsize=7.5, color="C3",
                     arrowprops=dict(arrowstyle="->", color="C3", lw=0.8))
axes[2].set_ylabel("I / I10")
axes[2].legend(loc="upper right", fontsize=8, frameon=False)
axes[2].set_xlabel("d sin θ / λ   (N = 4, d = 4a)")
for ax in axes:
    ax.set_xticks(np.arange(-8, 9, 2))
    ax.set_xlim(-9, 9)
    ax.grid(alpha=0.25)
fig.tight_layout()
