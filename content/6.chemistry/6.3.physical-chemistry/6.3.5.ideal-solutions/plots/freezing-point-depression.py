"""Freezing-point depression of water by a non-electrolyte, treated as an ideal solution:
the linear law Delta T_f = K_f b, the integrated form ln x_A = -(Delta_fus H/R)(1/T_f - 1/T*_f)
with constant Delta_fus H, and the same with Delta_fus C_p = C_p(l) - C_p(s) included (solved numerically)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

R = 8.314
M = 18.015e-3          # kg mol^-1
Tf0 = 273.15           # K
dH = 6009.5            # J mol^-1, enthalpy of fusion at Tf0
dCp = 75.3 - 38.0      # J K^-1 mol^-1, C_p(l) - C_p(s) near 0 degC
Kf = R * Tf0**2 * M / dH

b = np.linspace(0, 4, 81)
xA = 1 / (1 + b * M)


def tf_const(x):
    return 1 / (1 / Tf0 - R * np.log(x) / dH)


def tf_cp(x):
    # ln x_A = -(1/R) * integral_{Tf0}^{T} ... from d ln x_A/dT = dH(T)/(R T^2), dH(T) = dH + dCp (T - Tf0)
    def g(T):
        lhs = (dH - dCp * Tf0) * (1 / Tf0 - 1 / T) + dCp * np.log(T / Tf0)
        return lhs / R - np.log(x)
    return brentq(g, 150, Tf0)


fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(b, Kf * b, color="C0", lw=1.6, ls="--", label=rf"$K_\mathrm{{f}}b_\mathrm{{B}}$, $K_\mathrm{{f}}$ = {Kf:.3f} K kg mol$^{{-1}}$")
ax.plot(b, Tf0 - tf_const(xA), color="C1", lw=1.8, label=r"integrated, $\Delta_\mathrm{fus}H$ constant")
ax.plot(b, [Tf0 - tf_cp(x) if x < 1 else 0 for x in xA], color="C2", lw=1.8, label=r"integrated, with $\Delta_\mathrm{fus}C_p$")
ax.set_xlabel(r"$b_\mathrm{B}$ / (mol kg$^{-1}$)")
ax.set_ylabel(r"$\Delta T_\mathrm{f}$ / K")
ax.set_xlim(0, 4)
ax.set_ylim(0, 8)
ax.legend(frameon=False, fontsize=9, loc="upper left")
ax.set_title("ideal solution in water: linear law vs exact forms", fontsize=10)
fig.tight_layout()
