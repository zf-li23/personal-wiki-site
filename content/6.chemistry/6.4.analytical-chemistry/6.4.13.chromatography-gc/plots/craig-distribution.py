"""Craig counter-current model of the plate theory. At every transfer the mobile phase moves
one plate; a solute with retention factor k keeps the fraction q = k/(1+k) in the stationary
phase and moves the fraction p = 1/(1+k). After n transfers the amount on plate r is the
binomial probability C(n, r) p^r q^(n-r). Two solutes, kA = 2 and kB = 0.5, after 4, 20 and
100 transfers; for n = 100 the normal approximation (central limit theorem) is overlaid."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

solutes = [("A", 2.0, "C0"), ("B", 0.5, "C3")]
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.4))
for ax, N in zip(axes, [4, 20, 100]):
    r = np.arange(N + 1)
    w = 0.42 if N < 30 else 0.9
    for i, (name, k, col) in enumerate(solutes):
        p = 1 / (1 + k)
        frac = stats.binom.pmf(r, N, p)
        if N < 30:
            ax.bar(r + (i - 0.5) * w, frac, width=w, color=col, alpha=0.8,
                   label=rf"{name}: $k$ = {k:g}")
        else:
            ax.bar(r, frac, width=w, color=col, alpha=0.55, label=rf"{name}: $k$ = {k:g}")
            x = np.linspace(0, N, 400)
            ax.plot(x, stats.norm.pdf(x, N * p, np.sqrt(N * p * (1 - p))), color=col, lw=1.3)
    ax.set_title(rf"$n$ = {N} transfers", fontsize=10)
    ax.set_xlabel(r"plate number $r$")
    ax.set_xlim(-0.8, N + 0.8)
axes[0].set_ylabel("fraction of solute on plate")
axes[0].legend(frameon=False, fontsize=8)
axes[2].text(0.98, 0.95, "curves: normal\napproximation", transform=axes[2].transAxes,
             ha="right", va="top", fontsize=8)
fig.tight_layout()
