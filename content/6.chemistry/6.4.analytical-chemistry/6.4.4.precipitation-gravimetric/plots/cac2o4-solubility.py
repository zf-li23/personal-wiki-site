"""Solubility of CaC2O4 versus pH: in water with no excess oxalate (s = sqrt(Ksp alpha)) and with 0.010 or
0.10 mol/L excess total oxalate (s = Ksp alpha / c). Ksp = 2.32e-9; oxalic acid pKa = 1.25, 3.81."""

import numpy as np
import matplotlib.pyplot as plt

Ksp = 2.32e-9
Ka1, Ka2 = 10 ** -1.25, 10 ** -3.81
pH = np.linspace(0, 8, 400)
h = 10.0 ** -pH
alpha = 1 + h / Ka2 + h * h / (Ka1 * Ka2)

fig, ax = plt.subplots(figsize=(6.4, 4))
ax.semilogy(pH, np.sqrt(Ksp * alpha), color="C0", lw=1.8, label="no excess oxalate")
for i, c in enumerate([0.010, 0.10]):
    ax.semilogy(pH, Ksp * alpha / c, color=f"C{i + 1}", lw=1.8, label=f"{c} mol L$^{{-1}}$ excess oxalate")
ax.axhline(1e-5, color="0.5", lw=0.8, ls=":")
ax.text(7.9, 1.3e-5, r"10$^{-5}$ mol L$^{-1}$", ha="right", fontsize=8)
ax.set_xlabel("pH")
ax.set_ylabel(r"solubility of CaC$_2$O$_4$ / (mol L$^{-1}$)")
ax.set_xlim(0, 8)
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
