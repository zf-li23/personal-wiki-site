"""Distance dependence of the two mechanisms of electronic energy transfer. Forster (dipole-dipole)
transfer falls off as 1/r^6 and is efficient up to several nm (R0 = 5 nm here); Dexter (electron
exchange) transfer needs orbital overlap and falls off exponentially, k = K J exp(-2r/L), with
L about 0.1 nm, so it only works at contact (below about 1 nm). The Dexter curve is scaled to
10^10 s^-1 at r = 0.5 nm (diffusion-controlled contact); the dashed line marks a typical triplet
decay rate of 10^6 s^-1, so transfer competes with decay only where a curve lies above it."""

import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.4, 8, 400)  # nm
tau = 1e-6  # s, a triplet-like donor lifetime
R0 = 5.0
k_forster = (1 / tau) * (R0 / r) ** 6
L = 0.1
k_dexter = 1e10 * np.exp(-2 * (r - 0.5) / L)

fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.semilogy(r, k_forster, color="C0", lw=2, label=r"F$\ddot{\rm o}$rster, $k \propto r^{-6}$")
ax.semilogy(r, k_dexter, color="C3", lw=2, label=r"Dexter, $k \propto \mathrm{e}^{-2r/L}$")
ax.axhline(1 / tau, color="0.5", ls="--", lw=1)
ax.text(7.9, 1.6 / tau, "donor decay rate", ha="right", fontsize=8, color="0.4")
ax.set_ylim(1e2, 1e14)
ax.set_xlim(0.4, 8)
ax.set_xlabel(r"donor-acceptor distance $r$ / nm")
ax.set_ylabel(r"transfer rate constant $k$ / s$^{-1}$")
ax.legend(frameon=False, fontsize=9)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
