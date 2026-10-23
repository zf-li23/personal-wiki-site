"""Titration of 20.00 mL of 0.1000 mol/L Cl-, Br-, I- with 0.1000 mol/L AgNO3: pAg versus fraction
titrated, from the charge balance [Ag+] - [X-] = (n_Ag - n_X)/V and [Ag+][X-] = Ksp
(Ksp: AgCl 1.77e-10, AgBr 5.35e-13, AgI 8.52e-17)."""

import numpy as np
import matplotlib.pyplot as plt

c, V0 = 0.1000, 20.00
f = np.linspace(0.001, 2, 4000)
fig, ax = plt.subplots(figsize=(6.4, 4))
for i, (name, Ksp) in enumerate([("Cl$^-$", 1.77e-10), ("Br$^-$", 5.35e-13), ("I$^-$", 8.52e-17)]):
    V = f * V0
    d = c * (V - V0) / (V0 + V)
    ag = (d + np.sqrt(d * d + 4 * Ksp)) / 2
    ax.plot(f * 100, -np.log10(ag), color=f"C{i}", lw=1.8, label=name)
ax.axvline(100, color="0.6", lw=0.8, ls=":")
ax.set_xlabel("fraction titrated / %")
ax.set_ylabel("pAg")
ax.set_xlim(0, 200)
ax.legend(frameon=False, fontsize=9, loc="upper right")
fig.tight_layout()
