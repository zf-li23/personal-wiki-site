"""Two-level system: ground level (g0 = 1, energy 0) and excited level (g1, energy e).
Fraction in the upper level, mean energy per particle and heat capacity per particle
(Schottky anomaly) as functions of the reduced temperature kT / e."""

import numpy as np
import matplotlib.pyplot as plt

tau = np.linspace(0.02, 5, 600)          # kT / e
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
for g1, c in zip([1, 3], ["C0", "C1"]):
    b = 1 / tau                          # e / kT
    q = 1 + g1 * np.exp(-b)
    p1 = g1 * np.exp(-b) / q
    u = p1                               # mean energy in units of e
    cv = b**2 * p1 * (1 - p1)            # C / k = (e/kT)^2 p1 (1 - p1)
    a1.plot(tau, p1, color=c, lw=1.6, label=rf"$g_1/g_0$ = {g1}")
    a1.axhline(g1 / (1 + g1), color=c, ls=":", lw=1)
    a2.plot(tau, cv, color=c, lw=1.6, label=rf"$g_1/g_0$ = {g1}")
a1.set_xlabel(r"$k_\mathrm{B}T/\varepsilon$")
a1.set_ylabel(r"$N_1/N = \langle\varepsilon\rangle/\varepsilon$")
a1.set_ylim(0, 0.8)
a1.legend(frameon=False, fontsize=9)
a2.set_xlabel(r"$k_\mathrm{B}T/\varepsilon$")
a2.set_ylabel(r"$C_V/(Nk_\mathrm{B})$")
a2.legend(frameon=False, fontsize=9)
fig.tight_layout()
