"""One-dimensional profiles of STED microscopy. Confocal excitation spot: Gaussian with
FWHM 250 nm. Depletion beam: doughnut with zero at the centre and peak intensity
zeta times the saturation intensity Is. Molecules that survive depletion fluoresce with
probability exp(-ln2 I/Is), so the effective PSF narrows roughly as 1/sqrt(1 + zeta)."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-400, 400, 4001)           # nm
fwhm0 = 250.0
s = fwhm0 / (2 * np.sqrt(2 * np.log(2)))
exc = np.exp(-0.5 * (x / s) ** 2)
x0 = 200.0                                   # radius of the doughnut maximum, nm
dough = np.e * (x / x0) ** 2 * np.exp(-((x / x0) ** 2))

def fwhm(y):
    above = x[y >= 0.5 * y.max()]
    return above.max() - above.min()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.0))
ax1.plot(x, exc, color="C0", lw=1.6, label="excitation spot")
ax1.plot(x, dough, color="C3", lw=1.6, label="STED doughnut (normalized)")
ax1.set_xlabel(r"$x$ / nm")
ax1.set_ylabel("relative intensity")
ax1.set_ylim(0, 1.15)
ax1.legend(frameon=False, fontsize=8, loc="upper right")
ax1.set_title("beam profiles", fontsize=10)

cmap = plt.get_cmap("viridis")
for i, zeta in enumerate([0, 10, 50, 200]):
    eff = exc * np.exp(-np.log(2) * zeta * dough)
    ax2.plot(x, eff, color=cmap(i / 3 * 0.85), lw=1.5,
             label=rf"$I_{{max}}/I_s$ = {zeta}: FWHM {fwhm(eff):.0f} nm")
ax2.set_xlabel(r"$x$ / nm")
ax2.set_ylabel("effective PSF")
ax2.set_ylim(0, 1.15)
ax2.set_xlim(-300, 300)
ax2.legend(frameon=False, fontsize=8, loc="upper right")
ax2.set_title("fluorescence that survives depletion", fontsize=10)
fig.tight_layout()
