"""Titration of Fe2+ with KMnO4 (MnO4- + 5Fe2+ + 8H+ -> Mn2+ + 5Fe3+ + 4H2O) in media that give different
formal potentials of Fe(III)/Fe(II): 0.73 V (1 mol/L HClO4), 0.68 V (1 mol/L H2SO4), 0.46 V (2 mol/L H3PO4).
The permanganate branch uses E = 1.51 V with [H+] taken as 1 mol/L (idealised Nernstian behaviour).
The equivalence point lies close to the permanganate potential: E_sp = (5 E_Mn + E_Fe)/6."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

S = 0.05916
E_Mn = 1.51


def potential(f, E_Fe):
    def g(E):
        fe3 = 1 / (1 + 10 ** ((E_Fe - E) / S))
        mn2 = 1 / (1 + 10 ** (5 * (E - E_Mn) / S))     # fraction of added Mn present as Mn2+
        return fe3 - f * mn2                            # f in units of the equivalent amount
    return brentq(g, -0.5, 2.0)


f = np.linspace(0.01, 2.0, 2000)
fig, ax = plt.subplots(figsize=(6.4, 4.2))
for i, (E_Fe, lab) in enumerate([(0.73, "1 mol L$^{-1}$ HClO$_4$"), (0.68, "1 mol L$^{-1}$ H$_2$SO$_4$"),
                                 (0.46, "2 mol L$^{-1}$ H$_3$PO$_4$")]):
    ax.plot(f * 100, [potential(x, E_Fe) for x in f], color=f"C{i}", lw=1.8,
            label=f"{lab}: $E^{{\\circ\\prime}}$ = {E_Fe} V")
    esp = (5 * E_Mn + E_Fe) / 6
    ax.plot(100, esp, "o", color=f"C{i}", ms=4)
ax.axvline(100, color="0.6", lw=0.8, ls=":")
ax.axhspan(0.85 - S / 2, 0.85 + S / 2, color="0.5", alpha=0.15, lw=0)
ax.text(5, 0.87, "diphenylamine sulfonate", fontsize=8, va="bottom")
ax.set_xlabel("fraction titrated / %")
ax.set_ylabel("E / V (vs. SHE)")
ax.set_xlim(0, 200)
ax.set_ylim(0.3, 1.6)
ax.legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
