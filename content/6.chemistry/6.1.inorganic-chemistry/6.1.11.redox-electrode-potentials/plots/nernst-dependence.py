"""Nernst equation at 298.15 K, three cases: the Fe3+/Fe2+ electrode against lg([Fe3+]/[Fe2+]);
the emf of the Cu-Zn cell against lg([Zn2+]/[Cu2+]) (it vanishes at lg K0); the Cr2O7(2-)/Cr3+
electrode against pH with [Cr2O7(2-)] = [Cr3+] = 1 mol/L. Standard potentials: CRC Handbook."""

import numpy as np
import matplotlib.pyplot as plt

R, F, T = 8.314, 96485.0, 298.15
s = R * T * np.log(10) / F          # 0.05916 V

fig, axes = plt.subplots(1, 3, figsize=(12, 3.8))

ax = axes[0]
x = np.linspace(-3, 3, 100)
ax.plot(x, 0.771 + s * x, color="C0", lw=1.8)
ax.axhline(0.771, color="0.6", lw=0.8, ls=":")
ax.axvline(0, color="0.6", lw=0.8, ls=":")
ax.annotate(r"slope $0.0592$ V per decade", (-2.8, 0.88), fontsize=9)
ax.set_xlabel(r"$\lg([\mathrm{Fe^{3+}}]/[\mathrm{Fe^{2+}}])$")
ax.set_ylabel(r"$E$ / V")
ax.set_title(r"$\mathrm{Fe^{3+} + e^- \rightleftharpoons Fe^{2+}}$", fontsize=10)

ax = axes[1]
E0 = 0.342 - (-0.762)
lgK = 2 * E0 / s
x = np.linspace(-5, 45, 200)
ax.plot(x, E0 - s / 2 * x, color="C1", lw=1.8)
ax.axhline(0, color="0.6", lw=0.8, ls=":")
ax.plot([lgK], [0], "o", color="C3")
ax.annotate(rf"equilibrium: $\lg K^\circ = {lgK:.1f}$", (lgK, 0), xytext=(0, 0.12),
            fontsize=9, arrowprops=dict(arrowstyle="->", color="0.4"))
ax.plot([0], [E0], "o", color="C0")
ax.annotate(rf"$E^\circ_\mathrm{{cell}} = {E0:.3f}$ V", (0, E0), xytext=(5, 1.05), fontsize=9)
ax.set_xlabel(r"$\lg([\mathrm{Zn^{2+}}]/[\mathrm{Cu^{2+}}])$")
ax.set_ylabel(r"$E_\mathrm{cell}$ / V")
ax.set_title("Cu-Zn cell: emf falls as the reaction proceeds", fontsize=10)

ax = axes[2]
pH = np.linspace(0, 7, 100)
ax.plot(pH, 1.36 - 14 * s / 6 * pH, color="C2", lw=1.8, label=r"$\mathrm{Cr_2O_7^{2-}/Cr^{3+}}$")
ax.axhline(1.066, color="C4", lw=1.2, ls="--", label=r"$\mathrm{Br_2/Br^-}$")
ax.axhline(0.5355, color="C5", lw=1.2, ls="--", label=r"$\mathrm{I_2/I^-}$")
ax.set_xlabel("pH")
ax.set_ylabel(r"$E$ / V")
ax.set_title(r"slope $-\frac{14}{6}\times 0.0592$ V per pH", fontsize=10)
ax.legend(frameon=False, fontsize=8.5)
fig.tight_layout()
