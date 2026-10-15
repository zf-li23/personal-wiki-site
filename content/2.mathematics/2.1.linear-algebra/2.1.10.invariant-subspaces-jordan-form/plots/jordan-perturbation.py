"""Eigenvalues of the nilpotent Jordan block J_{0,n} after changing its
bottom-left entry to eps: they jump from 0 to the n-th roots of eps."""

import numpy as np
import matplotlib.pyplot as plt

n = 10
J = np.diag(np.ones(n - 1), k=1)
epsilons = [1e-10, 1e-6, 1e-3]
markers = ["o", "s", "^"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))

# Left: eigenvalues in the complex plane for three perturbation sizes
theta = np.linspace(0, 2 * np.pi, 400)
for eps, mk in zip(epsilons, markers):
    Jp = J.copy()
    Jp[-1, 0] = eps
    lam = np.linalg.eigvals(Jp)
    r = eps ** (1 / n)
    line, = ax1.plot(lam.real, lam.imag, mk, markersize=7, linestyle="none",
                     label=rf"$\varepsilon = 10^{{{int(np.log10(eps))}}}$, radius {r:.3f}")
    ax1.plot(r * np.cos(theta), r * np.sin(theta), color=line.get_color(),
             linewidth=0.8, alpha=0.6)
ax1.plot([0], [0], "x", color="gray", markersize=9, label=r"$\varepsilon = 0$: all at $0$")
ax1.set_aspect("equal")
ax1.set_xlabel("Re")
ax1.set_ylabel("Im")
ax1.set_title(rf"Eigenvalues of $J_{{0,{n}}}$ with entry $(n, 1)$ set to $\varepsilon$")
ax1.legend(loc="upper left", fontsize=8, bbox_to_anchor=(1.0, 1.0))
ax1.grid(True, alpha=0.3)

# Right: spread of the eigenvalues versus eps for several block sizes
eps_grid = np.logspace(-16, -1, 61)
for size in [2, 5, 10, 20]:
    ax2.loglog(eps_grid, eps_grid ** (1 / size), linewidth=1.8,
               label=rf"$k = {size}$: $\varepsilon^{{1/{size}}}$")
ax2.loglog(eps_grid, eps_grid, color="gray", linestyle="--", linewidth=1,
           label=r"normal matrix: at most $\varepsilon$")
ax2.set_xlabel(r"perturbation $\varepsilon$")
ax2.set_ylabel(r"$|\lambda|$ after perturbation")
ax2.set_title(r"Eigenvalue change for a Jordan block of order $k$")
ax2.grid(True, which="both", alpha=0.3)
ax2.legend(fontsize=8)
fig.tight_layout()
