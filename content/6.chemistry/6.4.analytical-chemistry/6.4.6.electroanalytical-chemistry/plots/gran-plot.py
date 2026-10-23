"""Potentiometric titration of 50.00 mL of 0.0500 mol/L NaCl with 0.1000 mol/L AgNO3 at 25 C,
silver indicator electrode against a saturated calomel electrode
(E(Ag+/Ag) = 0.7996 V, Ksp(AgCl) = 1.77e-10, E(SCE) = 0.2412 V; activities taken as concentrations).
Panels: E-V curve, first and second derivatives, and Gran plots before and after the
equivalence point (both extrapolate to Ve = 25.00 mL)."""

import numpy as np
import matplotlib.pyplot as plt

S = 0.05916
E0, Ksp, Eref = 0.7996, 1.77e-10, 0.2412
c0, V0, ct = 0.0500, 50.00, 0.1000
Ve = c0 * V0 / ct


def silver(V):
    # charge/material balance with AgCl(s) present: [Ag+] - [Cl-] = (ct V - c0 V0)/(V0 + V)
    d = (ct * V - c0 * V0) / (V0 + V)
    return (d + np.sqrt(d * d + 4 * Ksp)) / 2


def cell(V):
    return E0 + S * np.log10(silver(V)) - Eref


V = np.linspace(1, 40, 2000)
E = cell(V)
Vd = np.arange(1.0, 40.0, 0.1)  # "measured" points every 0.10 mL
Ed = cell(Vd)
d1 = np.diff(Ed) / np.diff(Vd)
Vm = (Vd[1:] + Vd[:-1]) / 2
d2 = np.diff(d1) / np.diff(Vm)
Vmm = (Vm[1:] + Vm[:-1]) / 2

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
ax = axes[0, 0]
ax.plot(V, E * 1e3, color="k", lw=1.6)
ax.axvline(Ve, color="0.6", lw=0.7, ls=":")
ax.set_xlabel(r"$V$(AgNO$_3$) / mL")
ax.set_ylabel(r"$E$ (Ag vs SCE) / mV")
ax.set_title("titration curve", fontsize=10)

ax = axes[0, 1]
ax.plot(Vm, d1, color="C0", lw=1.4)
ax.set_xlim(23, 27)
ax.set_xlabel(r"$V$ / mL")
ax.set_ylabel(r"$\Delta E/\Delta V$ / (V mL$^{-1}$)")
ax.set_title("first derivative: maximum at end point", fontsize=10)

ax = axes[1, 0]
ax.plot(Vmm, d2, color="C3", lw=1.4)
ax.axhline(0, color="0.6", lw=0.6)
ax.set_xlim(23, 27)
ax.set_xlabel(r"$V$ / mL")
ax.set_ylabel(r"$\Delta^2 E/\Delta V^2$ / (V mL$^{-2}$)")
ax.set_title("second derivative: zero crossing at end point", fontsize=10)

ax = axes[1, 1]
Vb = np.linspace(5, 22, 12)
Va = np.linspace(28, 40, 10)
gb = (V0 + Vb) * 10 ** (-cell(Vb) / S)
ga = (V0 + Va) * 10 ** (cell(Va) / S)
gb, ga = gb / gb.max(), ga / ga.max()
for Vx, g, col, lab in [(Vb, gb, "C0", r"before: $(V_0+V)\,10^{-E/S}$"),
                        (Va, ga, "C3", r"after: $(V_0+V)\,10^{E/S}$")]:
    p = np.polyfit(Vx, g, 1)
    xx = np.linspace(min(Vx.min(), Ve), max(Vx.max(), Ve), 50)
    ax.plot(Vx, g, "o", color=col, ms=4, label=lab)
    ax.plot(xx, np.polyval(p, xx), color=col, lw=1)
ax.axvline(Ve, color="0.6", lw=0.7, ls=":")
ax.set_ylim(0, 1.1)
ax.set_xlabel(r"$V$ / mL")
ax.set_ylabel("Gran function (scaled)")
ax.set_title(r"Gran plots extrapolate to $V_{\mathrm{e}}$ = 25.00 mL", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper center")
fig.tight_layout()
