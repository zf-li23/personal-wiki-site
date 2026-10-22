"""Arrhenius plots ln k vs 1/T for three activation energies (same k at 300 K):
the larger Ea, the steeper the line and the stronger the temperature dependence."""

import numpy as np
import matplotlib.pyplot as plt

R = 8.314
T = np.linspace(280, 420, 200)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
for Ea, col in [(50e3, "C0"), (100e3, "C1"), (200e3, "C3")]:
    lnk = -Ea / R * (1 / T - 1 / 300)          # ln[k(T)/k(300 K)]
    ax1.plot(1000 / T, lnk, color=col, lw=1.6, label=rf"$E_\mathrm{{a}}$ = {Ea / 1e3:.0f} kJ mol$^{{-1}}$")
    ratio = np.exp(Ea / R * (1 / 300 - 1 / 310))
    ax2.semilogy(T, np.exp(lnk), color=col, lw=1.6, label=rf"$k(310)/k(300)$ = {ratio:.1f}")
ax1.set_xlabel(r"$10^3\,\mathrm{K}/T$")
ax1.set_ylabel(r"$\ln[k(T)/k(300\,\mathrm{K})]$")
ax1.set_title(r"slope $= -E_\mathrm{a}/R$", fontsize=10)
ax1.legend(frameon=False, fontsize=9)
ax2.set_xlabel("T / K")
ax2.set_ylabel(r"$k(T)/k(300\,\mathrm{K})$")
ax2.set_title("temperature sensitivity", fontsize=10)
ax2.legend(frameon=False, fontsize=9)
fig.tight_layout()
