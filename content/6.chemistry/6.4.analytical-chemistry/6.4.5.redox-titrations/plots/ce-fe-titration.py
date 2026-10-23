"""Titration of Fe2+ with Ce4+ in 1 mol/L H2SO4 (formal potentials 0.68 V and 1.44 V, 25 C):
potential versus fraction titrated from the Nernst equation of either couple (equal at equilibrium),
with the 0.1 % jump and the transition ranges of two redox indicators."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

S = 0.05916
E_Fe, E_Ce = 0.68, 1.44
c = 0.1000


def potential(f):
    # electron balance: fraction of Fe oxidised = fraction of Ce reduced (per mole of Fe)
    def g(E):
        fe3 = 1 / (1 + 10 ** ((E_Fe - E) / S))          # [Fe3+]/c_Fe
        ce3 = 1 / (1 + 10 ** ((E - E_Ce) / S))          # [Ce3+]/c_Ce
        return fe3 - f * ce3
    return brentq(g, 0.0, 2.0)


f = np.linspace(0.01, 2.0, 2000)
E = np.array([potential(x) for x in f])
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(f * 100, E, color="C0", lw=1.8)
ax.axvline(100, color="0.6", lw=0.8, ls=":")
for x in (0.999, 1.001):
    ax.plot(x * 100, potential(x), "o", color="C3", ms=4)
ax.text(103, 0.86, "99.9 %: 0.86 V", fontsize=8, va="center")
ax.text(103, 1.26, "100.1 %: 1.26 V", fontsize=8, va="center")
for (E0, name, col) in [(0.85, "diphenylamine sulfonate", "C1"), (1.06, "ferroin", "C2")]:
    ax.axhspan(E0 - S, E0 + S, color=col, alpha=0.18, lw=0)
    ax.text(195, E0, name, fontsize=8, ha="right", va="center", color=col)
ax.set_xlabel("fraction titrated / %")
ax.set_ylabel("E / V (vs. SHE)")
ax.set_xlim(0, 200)
ax.set_ylim(0.5, 1.55)
fig.tight_layout()
