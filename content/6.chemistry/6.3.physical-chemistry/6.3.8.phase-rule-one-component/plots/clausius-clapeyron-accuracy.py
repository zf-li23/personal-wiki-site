"""Vapor pressure of water between 0 and 100 C: the reference curve (IAPWS saturation
correlation) against Clausius-Clapeyron integrated from the normal boiling point with a
constant enthalpy of vaporization, and with Delta_vap H_m(T) linear in T (Kirchhoff's law,
Delta C_p,m = -41.7 J/(K mol))."""

import numpy as np
import matplotlib.pyplot as plt

R = 8.314462618
Tc, pc = 647.096, 22.064e6


def p_sat(T):
    tau = 1 - T / Tc
    a = [-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502]
    e = [1, 1.5, 3, 3.5, 4, 7.5]
    return pc * np.exp(Tc / T * sum(ai * tau**ei for ai, ei in zip(a, e)))


T1, p1, H1 = 373.124, 101325.0, 40.65e3     # normal boiling point, Delta_vap H_m there
dCp = 33.58 - 75.33                          # C_p,m(g) - C_p,m(l)
T = np.linspace(273.16, 373.124, 300)
p_ref = p_sat(T)
p_const = p1 * np.exp(-H1 / R * (1 / T - 1 / T1))
H0 = H1 - dCp * T1
p_kirch = p1 * np.exp(-H0 / R * (1 / T - 1 / T1) + dCp / R * np.log(T / T1))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.8))
t = T - 273.15
ax1.plot(t, p_ref / 1e3, color="C0", lw=2.2, label="reference (IAPWS)")
ax1.plot(t, p_const / 1e3, color="C3", lw=1.4, ls="--", label=r"constant $\Delta_\mathrm{vap}H_\mathrm{m}$")
ax1.plot(t, p_kirch / 1e3, color="C2", lw=1.4, ls="-.", label=r"$\Delta_\mathrm{vap}H_\mathrm{m}(T)$, Kirchhoff")
ax1.set_xlabel(r"$t\,/\,^\circ\mathrm{C}$")
ax1.set_ylabel(r"$p\,/\,\mathrm{kPa}$")
ax1.set_xlim(0, 100)
ax1.set_yscale("log")
ax1.set_ylim(0.5, 150)
ax1.legend(frameon=False, fontsize=8, loc="upper left")

ax2.plot(t, 100 * (p_const / p_ref - 1), color="C3", lw=1.4, ls="--", label=r"constant $\Delta_\mathrm{vap}H_\mathrm{m}$")
ax2.plot(t, 100 * (p_kirch / p_ref - 1), color="C2", lw=1.4, ls="-.", label="Kirchhoff")
ax2.axhline(0, color="0.6", lw=0.8)
ax2.set_xlabel(r"$t\,/\,^\circ\mathrm{C}$")
ax2.set_ylabel("relative error / %")
ax2.set_xlim(0, 100)
ax2.legend(frameon=False, fontsize=8)
fig.tight_layout()
