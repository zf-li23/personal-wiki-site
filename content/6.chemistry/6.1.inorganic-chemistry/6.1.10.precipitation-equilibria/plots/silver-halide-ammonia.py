"""Solubility of AgCl, AgBr and AgI in aqueous ammonia, from Ksp (CRC Handbook) and the stability
constants of Ag(NH3)+ and Ag(NH3)2+ (lg K1 = 3.31, lg beta2 = 7.22); total ammonia on the x axis."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

b1, b2 = 10**3.31, 10**7.22
cN = np.logspace(-3, 1, 300)

fig, ax = plt.subplots(figsize=(6.4, 4))
for i, (name, Ksp) in enumerate([("AgCl", 1.8e-10), ("AgBr", 5.4e-13), ("AgI", 8.5e-17)]):
    S = []
    for c in cN:
        def f(s):
            # free ammonia L from the ammonia balance, given total dissolved silver s = [X-]
            ag = Ksp / s
            L = brentq(lambda L: L + ag * (b1 * L + 2 * b2 * L * L) - c, 0, c)
            return ag * (1 + b1 * L + b2 * L * L) - s
        S.append(brentq(f, np.sqrt(Ksp) * 0.999, c))
    ax.loglog(cN, S, color=f"C{i}", lw=1.8, label=name)
ax.set_xlabel(r"total NH$_3$ / (mol L$^{-1}$)")
ax.set_ylabel(r"solubility / (mol L$^{-1}$)")
ax.legend(frameon=False, fontsize=9, loc="lower right")
fig.tight_layout()
