"""Homogeneous nucleation of ice in supercooled water: Delta G(r) = 4 pi r^2 gamma_sl +
(4/3) pi r^3 Delta G_V with Delta G_V = -Delta_fus H_m Delta T / (T_m V_m(s)), for three
degrees of supercooling. The maximum sits at the critical radius r_c = 2 gamma_sl / |Delta G_V|."""

import numpy as np
import matplotlib.pyplot as plt

gamma = 0.030              # ice-water interfacial tension, J m^-2 (approximate)
dH, Tm, Vm = 6010.0, 273.15, 1.963e-5   # J mol^-1, K, m^3 mol^-1 (ice Ih)

r = np.linspace(0, 10e-9, 600)
fig, ax = plt.subplots(figsize=(6.0, 3.8))
for dT, col in [(10, "C0"), (20, "C1"), (40, "C3")]:
    dGv = -dH * dT / (Tm * Vm)
    G = 4 * np.pi * r**2 * gamma + 4 / 3 * np.pi * r**3 * dGv
    rc = 2 * gamma / abs(dGv)
    Gc = 16 * np.pi * gamma**3 / (3 * dGv**2)
    ax.plot(r * 1e9, G * 1e18, color=col, lw=1.8, label=rf"$\Delta T$ = {dT} K, $r_\mathrm{{c}}$ = {rc*1e9:.1f} nm")
    ax.plot(rc * 1e9, Gc * 1e18, "o", color=col, ms=4)
ax.plot(r * 1e9, 4 * np.pi * r**2 * gamma * 1e18, color="0.6", lw=1, ls="--", label=r"surface term $4\pi r^2\gamma_\mathrm{sl}$")
ax.axhline(0, color="0.6", lw=0.8)
ax.set_xlim(0, 10)
ax.set_ylim(-3, 6)
ax.set_xlabel(r"$r\,/\,\mathrm{nm}$")
ax.set_ylabel(r"$\Delta G\,/\,10^{-18}\,\mathrm{J}$")
ax.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
