"""Left: solubility of CaF2 (Ksp = 3.45e-11) in solutions of Ca(NO3)2 or NaF, ideal solution.
Right: solubility of BaSO4 (Ksp = 1.08e-10) in KNO3 solutions relative to pure water, with activity
coefficients estimated by the Davies equation (salt effect; qualitative above about 0.1 mol/L)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

Ksp = 3.45e-11
c = np.logspace(-6, 0, 300)
S_ca = [brentq(lambda s: (cc + s) * (2 * s) ** 2 - Ksp, 0, 1) for cc in c]
S_f = [brentq(lambda s: s * (cc + 2 * s) ** 2 - Ksp, 0, 1) for cc in c]
ax1.loglog(c, S_ca, color="C0", lw=1.8, label=r"added Ca$^{2+}$: $S \propto c^{-1/2}$")
ax1.loglog(c, S_f, color="C1", lw=1.8, label=r"added F$^-$: $S \propto c^{-2}$")
ax1.axhline((Ksp / 4) ** (1 / 3), color="0.6", lw=0.8, ls=":")
ax1.text(1.5e-6, 2.6e-4, "pure water", fontsize=8)
ax1.set_xlabel(r"concentration of the added common ion / (mol L$^{-1}$)")
ax1.set_ylabel(r"solubility of CaF$_2$ / (mol L$^{-1}$)")
ax1.set_title("common-ion effect", fontsize=10)
ax1.legend(frameon=False, fontsize=9, loc="lower left")

Kb = 1.08e-10


def gamma2(I):
    """Davies estimate of the activity coefficient of a doubly charged ion at 25 C."""
    r = np.sqrt(I)
    return 10 ** (-0.509 * 4 * (r / (1 + r) - 0.3 * I))


ck = np.linspace(0, 0.1, 300)
S0 = np.sqrt(Kb)
real = [brentq(lambda s: gamma2(4 * s + x) ** 2 * s * s - Kb, 0, 1) for x in ck]
ax2.plot(ck, np.array(real) / S0, color="C3", lw=1.8, label="with activity coefficients (Davies)")
ax2.axhline(1, color="C0", lw=1.4, ls="--", label=r"ideal: $S = \sqrt{K_{sp}}$")
ax2.set_ylim(0.8, 3.0)
ax2.set_xlabel(r"$c$(KNO$_3$) / (mol L$^{-1}$)")
ax2.set_ylabel(r"$S$(BaSO$_4$) / $S$(pure water)")
ax2.set_title("salt effect: BaSO4 in KNO3", fontsize=10)
ax2.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
