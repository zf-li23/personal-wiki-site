"""Fundamental vibration-rotation absorption band of H35Cl at 300 K (rigid-rotor line positions with band constants)."""

import numpy as np
import matplotlib.pyplot as plt

h, c, kB = 6.62607015e-34, 2.99792458e10, 1.380649e-23  # c in cm/s so that energies come from cm^-1
nu0, B0, B1 = 2885.9, 10.44, 10.14  # band origin and rotational constants (cm^-1) of the v = 0 and v = 1 levels
T = 300.0

fig, ax = plt.subplots(figsize=(9.5, 4.0))
J = np.arange(0, 13)
pop = (2 * J + 1) * np.exp(-h * c * B0 * J * (J + 1) / (kB * T))
pop /= pop.max()
for Jl in J:
    # R branch: J -> J + 1
    m = Jl + 1
    nuR = nu0 + (B1 + B0) * m + (B1 - B0) * m**2
    sR = pop[Jl] * (Jl + 1) / (2 * Jl + 1)
    ax.plot([nuR, nuR], [0, sR], color="C0", lw=2)
    if Jl >= 1:
        # P branch: J -> J - 1
        m = -Jl
        nuP = nu0 + (B1 + B0) * m + (B1 - B0) * m**2
        sP = pop[Jl] * Jl / (2 * Jl + 1)
        ax.plot([nuP, nuP], [0, sP], color="C1", lw=2)
    if Jl in (0, 3):
        ax.annotate(f"R({Jl})", (nuR, sR), textcoords="offset points", xytext=(-8, 4), fontsize=8)
    if Jl in (1, 3):
        ax.annotate(f"P({Jl})", (nuP, sP), textcoords="offset points", xytext=(-8, 4), fontsize=8)
ax.axvline(nu0, color="0.5", ls=":", lw=1)
ax.text(nu0, 0.62, "band origin\n(no line)", ha="center", fontsize=8, color="0.4")
ax.text(2610, 0.52, r"P branch ($\Delta J = -1$)", color="C1", fontsize=9)
ax.text(3010, 0.52, r"R branch ($\Delta J = +1$)", color="C0", fontsize=9)
ax.set_xlim(2600, 3150)
ax.set_ylim(0, 0.75)
ax.set_xlabel(r"wavenumber $\tilde\nu$ / cm$^{-1}$")
ax.set_ylabel("relative intensity")
ax.set_title(r"HCl fundamental band at 300 K")
fig.tight_layout()
