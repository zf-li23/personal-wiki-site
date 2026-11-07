# Oxygen supply along a root by gas diffusion through aerenchyma (Fick's law). Steady state along a root of
# length L with gas-filled porosity phi, gas-phase diffusion coefficient D = 2.0e-5 m2/s and uniform O2 demand Q
# (respiration plus radial O2 loss, mol O2 per m3 of root per s): D phi C'' = Q with C(0) = C0 (8.6 mol/m3, air
# at 21 kPa O2, 25 C) and no flux at the tip, so C(z) = C0 - (Q/(D phi)) (L z - z^2/2), and the longest root that
# keeps the tip above a critical concentration Cc = 0.4 mol/m3 is L_max = sqrt(2 D phi (C0 - Cc)/Q).
# A: profiles of roots of length L_max for three porosities, Q = 7.5e-4 (tight barrier to radial O2 loss).
# B: L_max against porosity for a tight barrier and for a leaky root (Q = 2.25e-3). Values are order-of-magnitude illustrations.
import matplotlib.pyplot as plt
import numpy as np

D, C0, Cc = 2.0e-5, 8.6, 0.4
fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.3))
Q = 7.5e-4
for phi, col in [(0.02, "#d9463b"), (0.10, "#d9a400"), (0.30, "#2e9e5b")]:
    L = np.sqrt(2 * D * phi * (C0 - Cc) / Q)
    z = np.linspace(0, L, 300)
    c = C0 - Q / (D * phi) * (L * z - z**2 / 2)
    a.plot(100 * z, c, color=col, lw=2.2, label=f"$\\varphi$ = {phi:.2f}: $L_{{\\max}}$ = {100 * L:.0f} cm")
    a.plot([100 * L], [Cc], "o", color=col, ms=5)
a.axhline(Cc, color="0.5", lw=0.8, ls=":")
a.text(1, Cc + 0.25, "critical O₂ for aerobic respiration (assumed)", fontsize=8, color="0.4")
a.set_xlabel("Distance from the root base / cm")
a.set_ylabel("O₂ concentration in the gas phase / (mol m$^{-3}$)")
a.set_ylim(0, 9.2)
a.set_xlim(0, 40)
a.legend(frameon=False, fontsize=8.5, loc="upper right")
a.set_title("A   O₂ profiles of roots of maximal length", loc="left", fontsize=10)

phi = np.linspace(0.005, 0.45, 300)
for Qx, col, name in [(7.5e-4, "#2e9e5b", "barrier to radial O₂ loss (rice-like)"), (2.25e-3, "#d9463b", "leaky root (3× demand)")]:
    lm = np.sqrt(2 * D * phi * (C0 - Cc) / Qx)
    b.plot(phi, 100 * lm, color=col, lw=2.2, label=name)
b.set_xlabel("Gas-filled porosity $\\varphi$")
b.set_ylabel("Maximum aerated root length / cm")
b.legend(frameon=False, fontsize=8.5, loc="upper left")
b.set_title("B   $L_{\\max} = \\sqrt{2D\\varphi(C_0 - C_{\\mathrm{c}})/Q}$", loc="left", fontsize=10)
b.set_xlim(0, 0.45)
b.set_ylim(0, 50)
fig.tight_layout()
