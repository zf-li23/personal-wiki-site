"""De Broglie wavelength versus kinetic energy for electrons and neutrons: relativistic and non-relativistic formulas."""

import numpy as np
import matplotlib.pyplot as plt

hc = 1239.841984  # eV nm
particles = [("electron", 0.51099895e6, "C0"), ("neutron", 939.56542e6, "C3")]

Ek = np.logspace(-3, 10, 650)  # eV
fig, ax = plt.subplots(figsize=(8.0, 4.4))
for name, mc2, col in particles:
    lam_rel = hc / np.sqrt(Ek ** 2 + 2 * Ek * mc2)
    lam_nr = hc / np.sqrt(2 * Ek * mc2)
    ax.loglog(Ek, lam_rel, color=col, lw=1.8, label=f"{name}, relativistic")
    ax.loglog(Ek, lam_nr, color=col, lw=1.0, ls="--", label=f"{name}, non-relativistic")
    ax.axvline(mc2, color=col, lw=0.6, ls=":")
ax.loglog(Ek, hc / Ek, color="0.5", lw=0.8, ls="-.", label="photon  λ = hc / E")
ax.axhspan(0.1, 0.5, color="0.5", alpha=0.12, lw=0)
ax.text(2e-3, 0.13, "interatomic spacing", fontsize=8, color="0.4")
ax.text(0.6e6, 3e2, "m_e c²", fontsize=8, color="C0", ha="right")
ax.text(0.8e9, 3e2, "m_n c²", fontsize=8, color="C3", ha="right")
ax.set_xlim(1e-3, 1e10)
ax.set_ylim(1e-7, 1e4)
ax.set_xlabel("kinetic energy  E_k / eV")
ax.set_ylabel("wavelength  λ / nm")
ax.legend(loc="lower left", fontsize=8, frameon=False)
fig.tight_layout()
