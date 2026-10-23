"""Resolution equation Rs = (sqrt(N)/4) ((alpha - 1)/alpha) (k/(1 + k)). Each panel varies one
factor and keeps the other two at N = 10 000, alpha = 1.05, k = 5. The dotted line is
Rs = 1.5 (baseline separation)."""

import numpy as np
import matplotlib.pyplot as plt


def rs(N, a, k):
    return np.sqrt(N) / 4 * (a - 1) / a * k / (1 + k)


fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.2), sharey=True)
N = np.linspace(500, 60000, 300)
axes[0].plot(N / 1000, rs(N, 1.05, 5), color="C0", lw=1.8)
axes[0].set_xlabel(r"plate number $N$ / 1000")
a = np.linspace(1.0, 1.15, 300)
axes[1].plot(a, rs(1e4, a, 5), color="C3", lw=1.8)
axes[1].set_xlabel(r"separation factor $\alpha$")
k = np.linspace(0, 20, 300)
axes[2].plot(k, rs(1e4, 1.05, k), color="C2", lw=1.8)
axes[2].set_xlabel(r"retention factor $k$")
for ax in axes:
    ax.axhline(1.5, color="0.5", lw=0.8, ls=":")
    ax.set_ylim(0, 3.2)
axes[0].set_ylabel(r"resolution $R_\mathrm{s}$")
axes[0].text(2, 1.58, r"$R_\mathrm{s}$ = 1.5", fontsize=8)
axes[0].set_title(r"$\alpha$ = 1.05, $k$ = 5", fontsize=9)
axes[1].set_title(r"$N$ = 10 000, $k$ = 5", fontsize=9)
axes[2].set_title(r"$N$ = 10 000, $\alpha$ = 1.05", fontsize=9)
fig.tight_layout()
