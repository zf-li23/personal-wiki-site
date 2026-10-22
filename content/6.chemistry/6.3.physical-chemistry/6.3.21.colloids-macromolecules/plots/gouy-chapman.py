"""Potential in the diffuse double layer next to a flat surface with psi_0 = 100 mV in a 1:1
electrolyte at 25 C, from the nonlinear Gouy-Chapman solution
tanh(e psi / 4 k_B T) = tanh(e psi_0 / 4 k_B T) exp(-x / lambda_D),
for three concentrations. Dotted lines: the linearized (Debye-Hueckel) result psi_0 exp(-x/lambda_D)."""

import numpy as np
import matplotlib.pyplot as plt

kB, T, e, NA = 1.380649e-23, 298.15, 1.602176634e-19, 6.02214076e23
eps = 78.4 * 8.8541878128e-12
kT = kB * T
psi0 = 0.100
x = np.linspace(0, 30e-9, 600)
fig, ax = plt.subplots(figsize=(6.0, 3.8))
for c, col in [(1e-3, "C0"), (1e-2, "C1"), (1e-1, "C3")]:
    n = c * 1e3 * NA
    lam = np.sqrt(eps * kT / (2 * n * e**2))
    g = np.tanh(e * psi0 / (4 * kT)) * np.exp(-x / lam)
    psi = 4 * kT / e * np.arctanh(g)
    ax.plot(x * 1e9, psi * 1e3, color=col, lw=1.8, label=rf"{c*1e3:g} mmol/L, $\lambda_\mathrm{{D}}$ = {lam*1e9:.2f} nm")
    ax.plot(x * 1e9, psi0 * np.exp(-x / lam) * 1e3, color=col, lw=0.9, ls=":")
ax.set_xlim(0, 30)
ax.set_ylim(0, 105)
ax.set_xlabel(r"distance from surface $x\,/\,\mathrm{nm}$")
ax.set_ylabel(r"$\psi\,/\,\mathrm{mV}$")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
