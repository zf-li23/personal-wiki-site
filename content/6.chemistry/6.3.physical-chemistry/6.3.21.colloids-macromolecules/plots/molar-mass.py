"""A Schulz-Zimm (gamma-shaped) molar-mass distribution of a polymer sample with number-average
molar mass 50 kg/mol and dispersity 2 (most probable distribution), shown as the mass fraction
per unit M, with the four averages M_n <= M_eta <= M_w <= M_z marked (Mark-Houwink exponent
alpha = 0.7 for M_eta)."""

import numpy as np
import matplotlib.pyplot as plt

Mn0, k = 50.0, 1.0                    # kg/mol; k = 1/(D - 1)
M = np.linspace(0.05, 1500, 20000)
num = M ** (k - 1) * np.exp(-k * M / Mn0)      # number distribution (unnormalized)
num /= np.trapezoid(num, M)
w = num * M / np.trapezoid(num * M, M)          # mass distribution

def moment(j):
    return np.trapezoid(num * M**j, M)

Mn = moment(1) / moment(0)
Mw = moment(2) / moment(1)
Mz = moment(3) / moment(2)
alpha = 0.7
Meta = (np.trapezoid(num * M ** (1 + alpha), M) / moment(1)) ** (1 / alpha)

fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.plot(M, w * 1e3, color="C0", lw=1.8, label="mass fraction density")
for val, name, col in [(Mn, r"$M_\mathrm{n}$", "C1"), (Meta, r"$M_\eta$", "C2"),
                       (Mw, r"$M_\mathrm{w}$", "C3"), (Mz, r"$M_z$", "C4")]:
    ax.axvline(val, color=col, lw=1.2, ls="--", label=f"{name} = {val:.0f} kg/mol")
ax.set_xlim(0, 400)
ax.set_ylim(0, None)
ax.set_xlabel(r"$M\,/\,\mathrm{kg\,mol^{-1}}$")
ax.set_ylabel(r"$w(M)\,/\,10^{-3}\,\mathrm{mol\,kg^{-1}}$")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
