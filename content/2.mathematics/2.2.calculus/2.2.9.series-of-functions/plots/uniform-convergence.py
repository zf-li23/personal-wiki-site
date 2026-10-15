"""x^n converges pointwise on [0, 1] to a discontinuous limit, but never stays
inside an epsilon band around it; x^n (1 - x)^n is dominated by 4^{-n}."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))
x = np.linspace(0, 1, 800)
eps = 0.2

ax = axes[0]
ax.fill_between(x[:-1], -eps, eps, color="gray", alpha=0.2, label=rf"band $|y - S(x)| < {eps}$")
for k, n in enumerate([1, 2, 5, 10, 30, 100]):
    ax.plot(x, x**n, color=f"C{k}", linewidth=1.2, label=rf"$S_n(x) = x^{{{n}}}$")
ax.plot([0, 1], [0, 0], color="black", linewidth=2)
ax.plot([1], [1], "o", color="black", markersize=5)
ax.plot([1], [0], "o", markerfacecolor="white", color="black", markersize=5)
ax.set_title(r"$x^n \to 0$ on $[0,1)$, $\to 1$ at $x=1$: not uniform", fontsize=10)
ax.set_xlabel(r"$x$")
ax.legend(fontsize=8, loc="upper left")
ax.grid(True, alpha=0.3)

ax = axes[1]
for k, n in enumerate([1, 2, 3, 5]):
    ax.plot(x, (x * (1 - x)) ** n, color=f"C{k}", linewidth=1.4, label=rf"$x^{{{n}}}(1-x)^{{{n}}}$")
    ax.axhline(0.25**n, color=f"C{k}", linewidth=0.8, linestyle="--")
ax.set_title(r"Weierstrass M-test: $0 \leq x^n(1-x)^n \leq 4^{-n}$ (dashed)", fontsize=10)
ax.set_xlabel(r"$x$")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
