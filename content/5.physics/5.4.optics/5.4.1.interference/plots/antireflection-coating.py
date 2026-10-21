"""Reflectance of glass (n = 1.52) at normal incidence, bare and with a single
quarter-wave layer designed for 550 nm (MgF2, n = 1.38, and the ideal n = sqrt(1.52))."""

import numpy as np
import matplotlib.pyplot as plt

n0, ns = 1.0, 1.52
lam0 = 550e-9
lam = np.linspace(380e-9, 780e-9, 600)


def reflectance(n1):
    """Exact single-layer reflectance including all multiple reflections."""
    e = lam0 / (4 * n1)
    r01 = (n0 - n1) / (n0 + n1)
    r12 = (n1 - ns) / (n1 + ns)
    beta = 2 * np.pi * n1 * e / lam
    r = (r01 + r12 * np.exp(-2j * beta)) / (1 + r01 * r12 * np.exp(-2j * beta))
    return np.abs(r) ** 2


fig, ax = plt.subplots(figsize=(7.5, 3.8))
R_bare = ((n0 - ns) / (n0 + ns)) ** 2
ax.plot(lam * 1e9, np.full_like(lam, R_bare) * 100, color="0.45", lw=1.2, label="bare glass")
ax.plot(lam * 1e9, reflectance(1.38) * 100, color="C0", lw=1.4, label="MgF2 layer, n = 1.38")
ax.plot(lam * 1e9, reflectance(np.sqrt(ns)) * 100, color="C1", lw=1.4, ls="--",
        label="ideal layer, n = sqrt(1.52) = 1.23")
ax.axvline(550, color="0.7", lw=0.8, ls=":")
ax.set_xlabel("wavelength / nm")
ax.set_ylabel("reflectance / %")
ax.set_xlim(380, 780)
ax.set_ylim(0, 5)
ax.legend(fontsize=8, loc="center right", frameon=False)
fig.tight_layout()
