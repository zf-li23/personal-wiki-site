"""Surface tension and surface excess of three homologous surface-active solutes in water at
298 K from the Szyszkowski equation gamma = gamma_0 [1 - b ln(1 + c/K)] (b = 0.179, the same
for the series) combined with the Gibbs adsorption isotherm Gamma = -(c/RT) d gamma/dc, which
gives Gamma = Gamma_inf c/(K + c) with Gamma_inf = b gamma_0 / RT. Each extra CH2 lowers K by
a factor of about 3 (Traube's rule)."""

import numpy as np
import matplotlib.pyplot as plt

R, T = 8.314462618, 298.15
g0, b = 72.0e-3, 0.179
c = np.linspace(0, 0.5, 500)            # mol L^-1
Ks = [0.09, 0.03, 0.01]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
for K, col in zip(Ks, ["C0", "C1", "C3"]):
    g = g0 * (1 - b * np.log1p(c / K))
    G = b * g0 / (R * T) * c / (K + c)
    ax1.plot(c, g * 1e3, color=col, lw=1.8, label=rf"$K$ = {K} mol/L")
    ax2.plot(c, G * 1e6, color=col, lw=1.8, label=rf"$K$ = {K} mol/L")
Ginf = b * g0 / (R * T)
ax2.axhline(Ginf * 1e6, color="0.6", lw=0.9, ls="--")
ax2.text(0.5, Ginf * 1e6 * 1.02, r"$\Gamma_\infty$", ha="right", va="bottom", fontsize=9)
ax1.set_xlabel(r"$c\,/\,\mathrm{mol\,L^{-1}}$")
ax1.set_ylabel(r"$\gamma\,/\,\mathrm{mN\,m^{-1}}$")
ax2.set_xlabel(r"$c\,/\,\mathrm{mol\,L^{-1}}$")
ax2.set_ylabel(r"$\Gamma\,/\,\mu\mathrm{mol\,m^{-2}}$")
ax2.set_ylim(0, Ginf * 1e6 * 1.15)
for ax in (ax1, ax2):
    ax.set_xlim(0, 0.5)
    ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
