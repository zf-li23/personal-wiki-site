"""Equilibrium NH3 mole fraction at 723 K for a stoichiometric 1:3 feed, K0 = 6.4e-3 for
1/2 N2 + 3/2 H2 <=> NH3, as a function of total pressure: ideal gases vs fugacity-corrected.
Fugacity coefficients at 30 MPa (generalized charts): phi(N2) = 1.15, phi(H2) = 1.09, phi(NH3) = 0.87;
at other pressures ln phi is scaled linearly with p (second-virial approximation), so the corrected
curve is only indicative."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

K = 6.4e-3
phi30 = {"N2": 1.15, "H2": 1.09, "NH3": 0.87}


def y_nh3(p_bar, corrected):
    if corrected:
        s = p_bar / 300.0
        kphi = phi30["NH3"] ** s / (phi30["N2"] ** (0.5 * s) * phi30["H2"] ** (1.5 * s))
    else:
        kphi = 1.0
    f = lambda x: 2 * x * (4 - 2 * x) / (3**1.5 * (1 - x) ** 2) / p_bar * kphi - K
    x = brentq(f, 1e-12, 1 - 1e-12)
    return 2 * x / (4 - 2 * x)


p = np.linspace(1, 350, 200)       # bar
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(p / 10, [y_nh3(q, False) for q in p], color="C0", lw=1.8, label="ideal gases")
ax.plot(p / 10, [y_nh3(q, True) for q in p], color="C1", lw=1.8, label="fugacity-corrected (approx.)")
for corr, c in [(False, "C0"), (True, "C1")]:
    yv = y_nh3(300, corr)
    ax.plot([30], [yv], "o", color=c, ms=4)
    ax.annotate(f"{yv:.3f}", (30.5, yv - 0.02), color=c, fontsize=9)
ax.set_xlabel("total pressure / MPa")
ax.set_ylabel(r"equilibrium $y(\mathrm{NH_3})$")
ax.set_xlim(0, 35)
ax.set_ylim(0, 0.42)
ax.set_title("723 K, N2 : H2 = 1 : 3", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
