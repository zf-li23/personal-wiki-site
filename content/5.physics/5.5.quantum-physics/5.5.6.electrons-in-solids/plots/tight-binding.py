"""Tight-binding chain: eigenvalues of the tridiagonal Hamiltonian as the chain grows, and the band dispersion."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

eps, t = 0.0, 1.0  # on-site energy and hopping (units of t)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))

# Left: open chains of N atoms, H = eps on the diagonal and -t on the off-diagonals
Ns = [1, 2, 3, 4, 6, 10, 20, 50]
for i, N in enumerate(Ns):
    E = eigh_tridiagonal(np.full(N, eps), np.full(N - 1, -t), eigvals_only=True)
    ax1.hlines(E, i - 0.3, i + 0.3, color="C0", lw=1)
ax1.axhspan(eps - 2 * t, eps + 2 * t, color="C0", alpha=0.08)
ax1.set_xticks(range(len(Ns)))
ax1.set_xticklabels([str(N) for N in Ns])
ax1.set_xlabel("number of atoms N")
ax1.set_ylabel(r"$E\,/\,t$")
ax1.set_ylim(-2.4, 2.4)
ax1.set_title(r"N levels fill the band $[\varepsilon_0 - 2t,\ \varepsilon_0 + 2t]$")

# Right: two atomic levels give two bands separated by a gap; dots are the N = 20 ring
k = np.linspace(-np.pi, np.pi, 400)  # ka
bands = [(-6.0, 1.0, "s band"), (2.0, -1.5, "p band")]
for i, (e0, tt, name) in enumerate(bands):
    ax2.plot(k, e0 - 2 * tt * np.cos(k), color=f"C{i}", lw=1.8, label=name)
    kj = 2 * np.pi * np.arange(-9, 11) / 20
    ax2.plot(kj, e0 - 2 * tt * np.cos(kj), "o", color=f"C{i}", ms=3.5)
ax2.axhspan(-4.0, -1.0, color="0.6", alpha=0.25)
ax2.text(0, -2.5, "band gap", ha="center", va="center", fontsize=9)
ax2.set_xlim(-np.pi, np.pi)
ax2.set_xticks([-np.pi, 0, np.pi])
ax2.set_xticklabels([r"$-\pi/a$", "0", r"$\pi/a$"])
ax2.set_xlabel("wave number k")
ax2.set_ylabel(r"$E\,/\,t$")
ax2.set_title(r"$E(k) = \varepsilon_0 - 2t\cos ka$")
ax2.legend(fontsize=8, loc="center right")
fig.tight_layout()
