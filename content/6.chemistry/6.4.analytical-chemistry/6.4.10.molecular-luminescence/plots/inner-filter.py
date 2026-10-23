"""Fluorescence intensity against concentration (expressed as the absorbance A of the
1 cm cell at the excitation wavelength). Ideal: F = 2.303 Phi I0 A. Total absorbed light:
F ~ 1 - 10^(-A). Right-angle instrument viewing only the central slab 0.4-0.6 cm
(primary inner filter): F ~ 10^(-0.4 A) - 10^(-0.6 A); adding reabsorption of the
emitted light over 0.5 cm (absorbance at the emission wavelength 0.3 A) gives the
secondary inner filter. All curves share the same low-concentration slope."""

import numpy as np
import matplotlib.pyplot as plt

A = np.linspace(0, 2.0, 400)
ln10 = np.log(10)
ideal = A
total = (1 - 10 ** (-A)) / ln10
x1, x2 = 0.4, 0.6
primary = (10 ** (-x1 * A) - 10 ** (-x2 * A)) / (ln10 * (x2 - x1))
secondary = primary * 10 ** (-0.3 * A * 0.5)

fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.plot(A, ideal, color="k", lw=1, ls="--", label=r"linear law $F = 2.303\,\Phi I_0 \varepsilon b c$")
ax.plot(A, total, color="C0", lw=1.5, label=r"all absorbed light, $1 - 10^{-A}$")
ax.plot(A, primary, color="C1", lw=1.5, label="central viewing zone (primary inner filter)")
ax.plot(A, secondary, color="C3", lw=1.5, label="plus reabsorption (secondary inner filter)")
ax.axvspan(0, 0.05, color="0.5", alpha=0.2, lw=0)
ax.text(0.06, 0.62, "A < 0.05", fontsize=8)
ax.set_xlabel(r"absorbance at the excitation wavelength $A = \varepsilon b c$")
ax.set_ylabel(r"fluorescence intensity (units of $2.303\,\Phi I_0$)")
ax.set_xlim(0, 2)
ax.set_ylim(0, 0.7)
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
