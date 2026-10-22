"""Potential-pH (Pourbaix) diagram of the Fe-H2O system at 298.15 K, dissolved Fe species at
activity 1e-6. Data: E0(Fe2+/Fe) = -0.447 V and E0(Fe3+/Fe2+) = 0.771 V (CRC electrochemical series)
fix the Gibbs energies of formation of the ions; hematite Fe2O3 and magnetite Fe3O4 from the CRC
thermodynamic tables. Every boundary is computed from these Gibbs energies, so the lines meet
consistently at the triple points. Dashed: water stability lines a and b (p = p0)."""

import numpy as np
import matplotlib.pyplot as plt

F, R, T = 96485.33212, 8.314462618, 298.15
s = R * T * np.log(10) / F                       # 0.05916 V
G = {"Fe": 0.0, "H2O": -237.13e3, "Fe2O3": -742.2e3, "Fe3O4": -1015.4e3}
G["Fe2+"] = -2 * F * 0.447
G["Fe3+"] = G["Fe2+"] + F * 0.771
la = -6.0                                        # lg a of dissolved iron

# Each couple: ox + m H+ + z e- -> red; returns E(pH) = E0 - (s/z)[lg Q] with Q = a_red/(a_ox a_H^m)
def line(z, m, dG0, lq_species):
    E0 = -dG0 / (z * F)
    return lambda pH: E0 - (s / z) * (lq_species + m * pH)

L = {
    "Fe2+/Fe": line(2, 0, G["Fe"] - G["Fe2+"], -la),
    "Fe3+/Fe2+": line(1, 0, G["Fe2+"] - G["Fe3+"], 0.0),
    "Fe2O3/Fe2+": line(2, 6, 2 * G["Fe2+"] + 3 * G["H2O"] - G["Fe2O3"], 2 * la),
    "Fe3O4/Fe2+": line(2, 8, 3 * G["Fe2+"] + 4 * G["H2O"] - G["Fe3O4"], 3 * la),
    "Fe2O3/Fe3O4": line(2, 2, 2 * G["Fe3O4"] + G["H2O"] - 3 * G["Fe2O3"], 0.0),
    "Fe3O4/Fe": line(8, 8, 3 * G["Fe"] + 4 * G["H2O"] - G["Fe3O4"], 0.0),
}
# vertical line Fe2O3 + 6H+ = 2Fe3+ + 3H2O
dGc = 2 * G["Fe3+"] + 3 * G["H2O"] - G["Fe2O3"]
pH_c = (-dGc / (R * T * np.log(10)) - 2 * la) / 6


def cross(f, g, lo=-2, hi=16):
    from scipy.optimize import brentq
    return brentq(lambda p: f(p) - g(p), lo, hi)

p1 = cross(L["Fe2O3/Fe2+"], L["Fe3O4/Fe2+"])     # Fe2+/Fe2O3/Fe3O4
p2 = cross(L["Fe3O4/Fe2+"], L["Fe2+/Fe"])        # Fe2+/Fe3O4/Fe

fig, ax = plt.subplots(figsize=(7.2, 5.4))
pH = np.linspace(-1, 14, 400)
seg = lambda key, a, b, **kw: ax.plot(np.linspace(a, b, 50), L[key](np.linspace(a, b, 50)), color="k", lw=1.6, **kw)
seg("Fe3+/Fe2+", -1, pH_c)
ax.plot([pH_c, pH_c], [L["Fe3+/Fe2+"](pH_c), 2.0], color="k", lw=1.6)
seg("Fe2O3/Fe2+", pH_c, p1)
seg("Fe3O4/Fe2+", p1, p2)
seg("Fe2+/Fe", -1, p2)
seg("Fe2O3/Fe3O4", p1, 14)
seg("Fe3O4/Fe", p2, 14)
ax.plot(pH, -s * pH, color="C0", lw=1.0, ls="--")
ax.plot(pH, 1.229 - s * pH, color="C3", lw=1.0, ls="--")
ax.text(13.3, -s * 13.3 + 0.05, "a", color="C0")
ax.text(13.3, 1.229 - s * 13.3 + 0.05, "b", color="C3")
ax.text(-0.7, 1.35, r"Fe$^{3+}$", fontsize=11)
ax.text(1.5, 0.1, r"Fe$^{2+}$", fontsize=11)
ax.text(8.5, 0.55, r"Fe$_2$O$_3$", fontsize=11)
ax.text(11.6, -0.60, r"Fe$_3$O$_4$", fontsize=10)
ax.text(5.0, -1.05, "Fe", fontsize=11)
ax.text(-0.8, -1.32, "immunity", fontsize=9, color="0.4")
ax.text(2.0, 0.42, "corrosion", fontsize=9, color="0.4")
ax.text(9.0, 1.15, "passivation", fontsize=9, color="0.4")
ax.set_xlim(-1, 14)
ax.set_ylim(-1.4, 1.6)
ax.set_xlabel("pH")
ax.set_ylabel(r"$E$ / V (vs SHE)")
ax.set_title(rf"$a$(Fe ions) = $10^{{-6}}$: $E$(Fe$^{{2+}}$/Fe) = {L['Fe2+/Fe'](0):.3f} V, Fe$_2$O$_3$/Fe$^{{3+}}$ at pH {pH_c:.2f}", fontsize=10)
fig.tight_layout()
