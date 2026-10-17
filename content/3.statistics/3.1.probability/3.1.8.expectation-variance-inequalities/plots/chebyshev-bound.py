"""Chebyshev bound 1/k^2 versus exact two-sided tail probabilities of standardized distributions."""

import numpy as np
import matplotlib.pyplot as plt
from math import erf, sqrt, exp

k = np.linspace(1.0, 4.0, 300)
normal = np.array([1 - erf(v / sqrt(2)) for v in k])
# Exp(1): mean 1, sd 1; |X - 1| >= k means X >= 1 + k (the left side needs X <= 1 - k < 0 for k >= 1)
expo = np.exp(-(1 + k))
# uniform on [-sqrt(3), sqrt(3)]
uni = np.clip(1 - k / np.sqrt(3), 0, None)
# Laplace with variance 1: scale b = 1/sqrt(2)
lap = np.exp(-k * np.sqrt(2))
# two-point extreme case attaining the bound at a single k: P(X = +-k0) = 1/(2 k0^2), P(X = 0) = 1 - 1/k0^2
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(k, 1 / k**2, color="C3", lw=2, label="Chebyshev bound 1/k^2")
ax.plot(k, normal, color="C0", lw=1.6, label="normal")
ax.plot(k, lap, color="C4", lw=1.6, label="Laplace")
ax.plot(k, expo, color="C1", lw=1.6, label="exponential")
ax.plot(k, uni, color="C2", lw=1.6, label="uniform")
k0 = 2.0
ax.plot([k0], [1 / k0**2], "o", color="C3")
ax.annotate("attained by a three-point law", (k0, 0.25), (2.3, 0.45), fontsize=8,
            arrowprops=dict(arrowstyle="->", lw=0.8))
ax.set_yscale("log")
ax.set_ylim(1e-4, 1.2)
ax.set_xlabel("k")
ax.set_ylabel("P(|X - mu| >= k sigma)")
ax.set_title("Chebyshev's inequality is valid for every distribution but often loose")
ax.legend(fontsize=8)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
