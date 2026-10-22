"""Molar mixing functions of an ideal liquid mixture A + B at 298.15 K and constant p:
Delta_mix H = 0, T Delta_mix S = -RT sum x ln x, Delta_mix G = RT sum x ln x (per mole of mixture)."""

import numpy as np
import matplotlib.pyplot as plt

R, T = 8.314, 298.15
x = np.linspace(1e-6, 1 - 1e-6, 400)
s = -(x * np.log(x) + (1 - x) * np.log(1 - x))       # dimensionless entropy of mixing per mole

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, R * T * s / 1e3, color="C1", lw=1.8, label=r"$T\Delta_\mathrm{mix}S_\mathrm{m}$")
ax.plot(x, 0 * x, color="C0", lw=1.8, label=r"$\Delta_\mathrm{mix}H_\mathrm{m} = \Delta_\mathrm{mix}V_\mathrm{m} = 0$")
ax.plot(x, -R * T * s / 1e3, color="C2", lw=1.8, label=r"$\Delta_\mathrm{mix}G_\mathrm{m}$")
ax.plot([0.5], [-R * T * np.log(2) / 1e3], "o", color="C2", ms=4)
ax.annotate(rf"$-RT\ln 2$ = {-R * T * np.log(2) / 1e3:.2f} kJ mol$^{{-1}}$", (0.52, -R * T * np.log(2) / 1e3 - 0.22), fontsize=9)
ax.set_xlabel(r"$x_\mathrm{B}$")
ax.set_ylabel(r"kJ mol$^{-1}$ (per mole of mixture)")
ax.set_xlim(0, 1)
ax.set_ylim(-2.2, 2.2)
ax.legend(frameon=False, fontsize=9, loc="upper right")
fig.tight_layout()
