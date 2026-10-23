"""Mirror-image rule and Stokes shift. Absorption S0 -> S1 and fluorescence S1 -> S0 are
built from the same vibronic progression (0-0 band at 26 400 cm^-1, vibrational spacing
1400 cm^-1 in both states, Poisson Franck-Condon factors with Huang-Rhys factor S = 0.9,
Gaussian band width 450 cm^-1); solvent relaxation shifts the emission 0-0 band by
700 cm^-1. Spectra are normalized and plotted against wavelength."""

import numpy as np
import matplotlib.pyplot as plt
from math import factorial

nu = np.linspace(19000, 33000, 2000)       # wavenumber, cm^-1
E00, hv, S, w, relax = 26400.0, 1400.0, 0.9, 450.0, 700.0
abs_ = np.zeros_like(nu)
em = np.zeros_like(nu)
for n in range(7):
    fc = np.exp(-S) * S ** n / factorial(n)
    abs_ += fc * np.exp(-0.5 * ((nu - (E00 + n * hv)) / w) ** 2)
    em += fc * np.exp(-0.5 * ((nu - (E00 - relax - n * hv)) / w) ** 2)
abs_ /= abs_.max()
em /= em.max()
lam = 1e7 / nu

fig, ax = plt.subplots(figsize=(6.8, 4.2))
ax.plot(lam, abs_, color="C0", lw=1.6, label="absorption (excitation)")
ax.plot(lam, em, color="C3", lw=1.6, label="fluorescence emission")
la, le = lam[np.argmax(abs_)], lam[np.argmax(em)]
ax.annotate("", xy=(le, 1.04), xytext=(la, 1.04), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax.text((la + le) / 2, 1.07, "Stokes shift", ha="center", fontsize=8)
l00 = 1e7 / E00
ax.axvline(l00, color="0.5", lw=0.7, ls=":")
ax.text(l00 - 9, 0.15, "0-0", fontsize=8, color="0.4")
ax.set_xlim(300, 500)
ax.set_ylim(0, 1.18)
ax.set_xlabel(r"$\lambda$ / nm")
ax.set_ylabel("normalized intensity")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
