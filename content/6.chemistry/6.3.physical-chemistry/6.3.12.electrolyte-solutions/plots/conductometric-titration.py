"""Conductometric titration curves at 25 C: 100 mL of 0.0100 mol/L HCl or CH3COOH titrated with
0.100 mol/L NaOH. Conductivity is computed from limiting ionic molar conductivities (CRC) and the
equilibrium composition (Ka = 1.75e-5, Kw = 1.0e-14); it is multiplied by (V0 + V)/V0 to remove
the effect of dilution, as is done in practice."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

lam = {"H": 349.65, "Na": 50.08, "Cl": 76.31, "OH": 198.0, "Ac": 40.9}   # S cm2 / mol
Ka, Kw = 1.75e-5, 1.0e-14
V0, c0, cb = 100.0, 0.0100, 0.100
V = np.linspace(0, 20, 401)


def sigma(conc):
    # conc in mol/L -> sigma in mS/cm: sum(lambda c) * 1e-3 (L/cm3) * 1e3 (mS/S)
    return sum(lam[k] * conc[k] for k in conc)


def strong(v):
    n_a, n_b, vt = c0 * V0, cb * v, V0 + v
    na, cl = n_b / vt, n_a / vt
    d = na - cl
    h = (-d + np.sqrt(d * d + 4 * Kw)) / 2
    return sigma({"H": h, "Na": na, "Cl": cl, "OH": Kw / h})


def weak(v):
    n_a, n_b, vt = c0 * V0, cb * v, V0 + v
    na, ca = n_b / vt, n_a / vt

    def balance(logh):
        h = 10.0**logh
        return h + na - Kw / h - ca * Ka / (Ka + h)

    h = 10.0 ** brentq(balance, -14, 0)
    return sigma({"H": h, "Na": na, "Ac": ca * Ka / (Ka + h), "OH": Kw / h})


fig, ax = plt.subplots(figsize=(7, 4.4))
for f, col, name in [(strong, "C3", "HCl + NaOH"), (weak, "C0", r"CH$_3$COOH + NaOH")]:
    s = np.array([f(v) for v in V]) * (V0 + V) / V0
    ax.plot(V, s, color=col, lw=1.8, label=name)
ax.axvline(10, color="0.5", lw=0.8, ls=":")
ax.text(10.2, 0.3, "equivalence point", fontsize=9, color="0.4")
ax.set_xlim(0, 20)
ax.set_ylim(0, 4.6)
ax.set_xlabel(r"$V$(NaOH) / mL")
ax.set_ylabel(r"$\sigma\,(V_0+V)/V_0$ / (mS cm$^{-1}$)")
ax.legend(frameon=False, fontsize=9, loc="upper center")
fig.tight_layout()
