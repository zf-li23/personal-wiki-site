"""Maxwell-Boltzmann distribution of translational energy (per mole) at two temperatures."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

R = 8.314462618e-3  # kJ mol^-1 K^-1
E0 = 50.0  # threshold energy, kJ/mol
E = np.linspace(0, 60, 3000)


def f(E, T):
    RT = R * T
    return 2 / np.sqrt(np.pi) * RT**-1.5 * np.sqrt(E) * np.exp(-E / RT)


def tail(E0, T):
    x = E0 / (R * T)
    return erfc(np.sqrt(x)) + 2 * np.sqrt(x / np.pi) * np.exp(-x)


fig, ax = plt.subplots(figsize=(7.2, 4.2))
for T, color in [(298.15, "C0"), (308.15, "C3")]:
    ax.plot(E, f(E, T), color=color, lw=1.8, label=f"T = {T:.0f} K")
ax.axvline(E0, color="0.5", lw=0.9, ls="--")
ax.text(E0 + 0.6, 0.02, r"$E_0$", fontsize=11)
ax.set_xlabel(r"$E\,/\,(\mathrm{kJ\,mol^{-1}})$")
ax.set_ylabel(r"$f(E)\,/\,(\mathrm{kJ^{-1}\,mol})$")
ax.set_xlim(0, 60)
ax.set_ylim(0, 0.3)
ax.legend(loc="upper right")

# inset: the tail beyond E0 on a magnified scale
ins = ax.inset_axes([0.42, 0.30, 0.45, 0.45])
Et = np.linspace(45, 60, 500)
for T, color in [(298.15, "C0"), (308.15, "C3")]:
    y = f(Et, T) * 1e9
    ins.plot(Et, y, color=color, lw=1.5)
    mask = Et >= E0
    ins.fill_between(Et[mask], y[mask], color=color, alpha=0.25)
ins.axvline(E0, color="0.5", lw=0.8, ls="--")
ins.set_xlabel(r"$E$", fontsize=8)
ins.set_ylabel(r"$10^{9}\,f(E)$", fontsize=8)
ins.tick_params(labelsize=7)
ratio = tail(E0, 308.15) / tail(E0, 298.15)
ins.text(0.97, 0.92, rf"$N(E \geq E_0)$ ratio 308 K / 298 K = {ratio:.2f}", transform=ins.transAxes,
         ha="right", va="top", fontsize=8)

fig.tight_layout()
