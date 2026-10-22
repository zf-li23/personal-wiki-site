"""DLVO interaction energy between two equal spheres (radius 100 nm, Hamaker constant
2e-20 J, surface potential 35 mV) in a 1:1 electrolyte at 25 C, for several concentrations:
V = 64 pi r n k_B T gamma_0^2 lambda_D^2 exp(-H/lambda_D) - A_H r / (12 H), gamma_0 =
tanh(e psi_0 / 4 k_B T) (weak-overlap repulsion, Derjaguin approximation). The barrier disappears
near the critical coagulation concentration, where V = 0 and dV/dH = 0 at H = lambda_D."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

kB, T, e, NA = 1.380649e-23, 298.15, 1.602176634e-19, 6.02214076e23
eps = 78.4 * 8.8541878128e-12
kT = kB * T
r, A, psi0 = 100e-9, 2e-20, 0.035
g0 = np.tanh(e * psi0 / (4 * kT))


def kappa(c):
    return np.sqrt(2 * c * 1e3 * NA * e**2 / (eps * kT))


def V(H, c):
    n, k = c * 1e3 * NA, kappa(c)
    return (64 * np.pi * r * n * kT * g0**2 / k**2 * np.exp(-k * H) - A * r / (12 * H)) / kT


ccc = 10 ** brentq(lambda lc: 64 * np.pi * 10**lc * 1e3 * NA * kT * g0**2 / np.e
                   - A * kappa(10**lc) ** 3 / 12, -5, 1)
H = np.linspace(0.2e-9, 20e-9, 1500)
fig, ax = plt.subplots(figsize=(6.2, 3.9))
for c, col in [(0.001, "C0"), (0.01, "C1"), (0.05, "C2"), (ccc, "C3"), (0.3, "C4")]:
    lab = f"{c*1e3:.0f} mmol/L" + (" (critical)" if c == ccc else "")
    ax.plot(H * 1e9, V(H, c), color=col, lw=1.8, label=lab)
ax.axhline(0, color="0.6", lw=0.8)
ax.set_xlim(0, 20)
ax.set_ylim(-40, 60)
ax.set_xlabel(r"surface separation $H\,/\,\mathrm{nm}$")
ax.set_ylabel(r"$V/k_\mathrm{B}T$")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
