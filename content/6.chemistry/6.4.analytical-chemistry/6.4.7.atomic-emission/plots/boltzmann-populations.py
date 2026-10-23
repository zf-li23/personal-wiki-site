"""Fraction of atoms in the upper level of the first resonance line,
N_j/N_0 = (g_j/g_0) exp(-E_j/(k_B T)), for Cs 852.1 nm, Na 589.0 nm, Ca 422.7 nm and
Zn 213.9 nm between 2000 and 10000 K (typical flame, arc and ICP temperatures marked)."""

import numpy as np
import matplotlib.pyplot as plt

h, c, kB = 6.62607015e-34, 2.99792458e8, 1.380649e-23
lines = [("Cs 852.1 nm", 852.1, 2), ("Na 589.0 nm", 589.0, 2),
         ("Ca 422.7 nm", 422.7, 3), ("Zn 213.9 nm", 213.9, 3)]
T = np.linspace(2000, 10000, 400)

fig, ax = plt.subplots(figsize=(7, 4.6))
for (lab, lam, g), col in zip(lines, ["C0", "C1", "C2", "C3"]):
    E = h * c / (lam * 1e-9)
    ax.semilogy(T, g * np.exp(-E / (kB * T)), color=col, lw=1.8,
                label=f"{lab} ($E_j$ = {E / 1.602176634e-19:.2f} eV)")
for x, txt in [(2500, "flame"), (5000, "arc"), (7000, "ICP")]:
    ax.axvline(x, color="0.6", lw=0.7, ls=":")
    ax.text(x + 60, 2e-11, txt, fontsize=9, color="0.4")
ax.set_xlim(2000, 10000)
ax.set_ylim(1e-11, 1)
ax.set_xlabel(r"$T$ / K")
ax.set_ylabel(r"$N_j/N_0$")
ax.legend(frameon=False, fontsize=9, loc="lower right")
fig.tight_layout()
