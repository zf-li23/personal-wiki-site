"""Determination of E(AgCl/Ag) from the cell Pt | H2(p0) | HCl(b) | AgCl | Ag at 25 C.
Cell emfs are generated from CRC mean activity coefficients of HCl through
E = E0 - (2RT/F) ln(gamma b / b0) with E0 = 0.22233 V. The quantity E' = E + (2RT/F) ln(b/b0)
is plotted against sqrt(b): the Debye-Hueckel limiting law predicts a straight line of slope
(2RT ln10 / F) A = 0.0602 V near b -> 0, so the intercept gives E0. A least-squares fit of the
extended form E' = E0 + 0.1183 A sqrt(b) / (1 + sqrt(b)) + C b to the points recovers E0."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

s, A, E0 = 0.05916, 0.509, 0.22233
b = np.array([0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1])
g = np.array([0.965, 0.952, 0.929, 0.905, 0.876, 0.830, 0.796])
E = E0 - 2 * s * np.log10(g * b)
Ep = E + 2 * s * np.log10(b)
x = np.sqrt(b)


def model(x, e0, C):
    return e0 + 2 * s * A * x / (1 + x) - 2 * s * C * x**2


p, _ = curve_fit(model, x, Ep, p0=[0.22, 0.1])
xx = np.linspace(0, 0.33, 200)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
ax.plot(b, E, "o-", color="C0", ms=5, lw=1.0)
ax.set_xscale("log")
ax.set_xlabel(r"$b$ / (mol kg$^{-1}$)")
ax.set_ylabel(r"$E_\mathrm{cell}$ / V")
ax.set_title("measured cell emf rises as HCl is diluted", fontsize=10)

ax = axes[1]
ax.plot(x, Ep, "o", color="C0", ms=6, label=r"$E' = E_\mathrm{cell} + (2RT/F)\ln(b/b^\circ)$")
ax.plot(xx[xx < 0.15], E0 + 2 * s * A * xx[xx < 0.15], color="C3", lw=1.2, ls="--", label="Debye-Hückel limiting slope")
ax.plot(xx, model(xx, *p), color="C2", lw=1.4, label=rf"extended fit, intercept {p[0]:.4f} V")
ax.plot([0], [E0], "*", color="C3", ms=12)
ax.set_xlim(0, 0.33)
ax.set_ylim(0.220, 0.236)
ax.set_xlabel(r"$\sqrt{b\,/\,b^\circ}$")
ax.set_ylabel(r"$E'$ / V")
ax.set_title(r"extrapolation to $b \to 0$ gives $E^\circ(\mathrm{AgCl/Ag})$", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="lower right")
fig.tight_layout()
