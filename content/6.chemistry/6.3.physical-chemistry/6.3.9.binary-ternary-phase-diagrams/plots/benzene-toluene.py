"""Vapor-liquid equilibrium of the nearly ideal mixture benzene (B) + toluene (A), computed
from Raoult's law with Antoine vapor pressures. Left: p-x diagram at 90 C. Right: T-x
diagram at 101.325 kPa with a tie line and the lever rule."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

MMHG = 0.133322368  # kPa


def antoine(A, B, C):
    return lambda T: 10 ** (A - B / (C + T - 273.15)) * MMHG


pB = antoine(6.90565, 1211.033, 220.790)   # benzene
pA = antoine(6.95464, 1344.800, 219.482)   # toluene
x = np.linspace(0, 1, 201)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.9))

T0 = 363.15
pl = pA(T0) + (pB(T0) - pA(T0)) * x                 # bubble (liquid) line
pv = 1 / ((1 - x) / pA(T0) + x / pB(T0))            # dew (vapor) line, x read as y_B
ax1.plot(x, pl, color="C0", lw=1.8, label="liquid line")
ax1.plot(x, pv, color="C3", lw=1.8, label="vapor line")
ax1.plot(x, x * pB(T0), color="0.6", lw=0.9, ls="--")
ax1.plot(x, (1 - x) * pA(T0), color="0.6", lw=0.9, ls="--")
ax1.text(0.62, 0.48 * pB(T0), r"$p_\mathrm{B}$", fontsize=9, color="0.45")
ax1.text(0.12, 0.72 * pA(T0), r"$p_\mathrm{A}$", fontsize=9, color="0.45")
ax1.text(0.18, 120, "l", fontsize=11)
ax1.text(0.72, 72, "g", fontsize=11)
ax1.text(0.40, 80, "l + g", fontsize=9)
ax1.set_xlabel(r"$x_\mathrm{B}$ or $y_\mathrm{B}$ (benzene)")
ax1.set_ylabel(r"$p\,/\,\mathrm{kPa}$")
ax1.set_title(r"$t = 90\,^\circ\mathrm{C}$", fontsize=10)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 150)
ax1.legend(frameon=False, fontsize=8, loc="upper left")

P = 101.325
Tb = np.array([brentq(lambda T: (1 - xi) * pA(T) + xi * pB(T) - P, 340, 400) for xi in x])
y = x * pB(Tb) / P
t = Tb - 273.15
ax2.plot(x, t, color="C0", lw=1.8, label="boiling-point (bubble) line")
ax2.plot(y, t, color="C3", lw=1.8, label="dew-point line")
# tie line through the system point X = 0.5 at 95 C
Ttie = 95 + 273.15
xl = (P - pA(Ttie)) / (pB(Ttie) - pA(Ttie))
yv = xl * pB(Ttie) / P
X = 0.5
ax2.plot([xl, yv], [95, 95], color="0.4", lw=1.0)
ax2.plot([xl, X, yv], [95, 95, 95], "o", color="0.3", ms=4)
ax2.text(xl - 0.02, 96.2, "a", ha="right", fontsize=9)
ax2.text(X, 96.2, "O", ha="center", fontsize=9)
ax2.text(yv + 0.02, 96.2, "b", fontsize=9)
ax2.axvline(X, color="0.7", lw=0.8, ls=":")
ax2.text(0.12, 82, "l", fontsize=11)
ax2.text(0.85, 108, "g", fontsize=11)
ax2.set_xlabel(r"$x_\mathrm{B}$ or $y_\mathrm{B}$ (benzene)")
ax2.set_ylabel(r"$t\,/\,^\circ\mathrm{C}$")
ax2.set_title(r"$p = 101.325\,\mathrm{kPa}$", fontsize=10)
ax2.set_xlim(0, 1)
ax2.set_ylim(75, 115)
ax2.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
