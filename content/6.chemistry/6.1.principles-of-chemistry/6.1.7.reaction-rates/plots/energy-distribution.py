"""Maxwell-Boltzmann distribution of molecular translational kinetic energy at 300 K and 310 K,
on linear and logarithmic axes; the shaded tails are the fractions of molecules with E >= Ea."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaincc

R = 8.314e-3  # kJ mol^-1 K^-1
Ea = 50.0     # kJ mol^-1, illustrative

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
E = np.linspace(1e-3, 70, 800)
for T, col in [(300, "C0"), (310, "C3")]:
    f = 2 / np.sqrt(np.pi) * np.sqrt(E) / (R * T) ** 1.5 * np.exp(-E / (R * T))
    frac = gammaincc(1.5, Ea / (R * T))   # exact tail of the 3D energy distribution
    ax1.plot(E[E < 20], f[E < 20], color=col, lw=1.6, label=f"T = {T} K")
    ax2.semilogy(E, f, color=col, lw=1.6, label=f"T = {T} K: fraction above Ea = {frac:.1e}")
    mask = E >= Ea
    ax2.fill_between(E[mask], 1e-14, f[mask], color=col, alpha=0.25)
ax1.set_xlabel(r"molar energy $E$ / (kJ mol$^{-1}$)")
ax1.set_ylabel("probability density / (mol kJ$^{-1}$)")
ax1.set_title("bulk of the distribution", fontsize=10)
ax1.legend(frameon=False, fontsize=9)
ax2.axvline(Ea, color="0.4", ls="--", lw=1)
ax2.annotate(r"$E_\mathrm{a}$", (Ea + 0.8, 1e-4), fontsize=11)
ax2.set_xlabel(r"molar energy $E$ / (kJ mol$^{-1}$)")
ax2.set_ylim(1e-12, 1)
ax2.set_xlim(0, 70)
ax2.set_title("log scale: the tail roughly doubles for +10 K", fontsize=10)
ax2.legend(frameon=False, fontsize=8, loc="lower left")
fig.tight_layout()
