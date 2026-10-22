"""Debye-Hueckel ionic atmosphere of a univalent ion in water at 25 C (point-ion model).
Left: screened potential psi = q exp(-kappa r) / (4 pi eps r) compared with the bare Coulomb potential.
Right: charge of the atmosphere in a spherical shell, -4 pi r^2 rho(r) / (z e) = kappa^2 r exp(-kappa r),
which peaks at r = lambda_D = 0.304 nm / sqrt(I_b / b0)."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.05, 15, 600)                 # nm
lB = 0.7152                                     # Bjerrum length in water at 25 C, nm
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

ax = axes[0]
ax.plot(r, lB / r, color="0.4", lw=1.2, ls="--", label="bare Coulomb")
for I, col in [(0.001, "C0"), (0.01, "C1"), (0.1, "C3")]:
    lD = 0.304 / np.sqrt(I)
    ax.plot(r, lB * np.exp(-r / lD) / r, color=col, lw=1.7, label=rf"$I_b$ = {I} mol/kg, $\lambda_\mathrm{{D}}$ = {lD:.2f} nm")
ax.set_xlim(0, 15)
ax.set_ylim(0, 1.0)
ax.set_xlabel(r"$r$ / nm")
ax.set_ylabel(r"$e\psi/(k_\mathrm{B}T)$")
ax.set_title("potential around a central cation", fontsize=10)
ax.legend(frameon=False, fontsize=8.5)

ax = axes[1]
for I, col in [(0.001, "C0"), (0.01, "C1"), (0.1, "C3")]:
    lD = 0.304 / np.sqrt(I)
    k = 1 / lD
    ax.plot(r, k * k * r * np.exp(-k * r), color=col, lw=1.7)
    ax.axvline(lD, color=col, lw=0.8, ls=":")
ax.set_xlim(0, 15)
ax.set_ylim(0, 0.45)
ax.set_xlabel(r"$r$ / nm")
ax.set_ylabel(r"$-4\pi r^2\rho(r)/(z e)$ / nm$^{-1}$")
ax.set_title(r"atmosphere charge per shell (area = 1), peak at $r = \lambda_\mathrm{D}$", fontsize=10)
fig.tight_layout()
