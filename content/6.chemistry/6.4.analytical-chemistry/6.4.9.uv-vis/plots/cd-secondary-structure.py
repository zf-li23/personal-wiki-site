"""Schematic far-UV circular dichroism spectra (mean residue ellipticity) of the three
basic protein secondary structures, built from Gaussian bands at the characteristic
positions: alpha helix (+192, -208, -222 nm), beta sheet (+196, -217 nm) and random
coil (-198, weak +218 nm). Illustrative shapes, not measured data."""

import numpy as np
import matplotlib.pyplot as plt

lam = np.linspace(185, 250, 400)
def g(l0, h, w):
    return h * np.exp(-0.5 * ((lam - l0) / w) ** 2)

helix = g(192, 7.0e4, 6.0) + g(207, -3.2e4, 4.5) + g(222, -3.5e4, 6.0)
sheet = g(196, 3.0e4, 6.0) + g(217, -1.8e4, 8.0)
coil = g(198, -4.0e4, 6.0) + g(218, 0.4e4, 6.0)

fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.plot(lam, helix / 1e3, color="C0", lw=1.6, label=r"$\alpha$ helix")
ax.plot(lam, sheet / 1e3, color="C1", lw=1.6, label=r"$\beta$ sheet")
ax.plot(lam, coil / 1e3, color="C3", lw=1.6, label="random coil")
ax.axhline(0, color="k", lw=0.6)
for l0 in (208, 222):
    ax.axvline(l0, color="C0", lw=0.6, ls=":")
ax.set_xlabel(r"$\lambda$ / nm")
ax.set_ylabel(r"$[\theta]$ / ($10^3$ deg cm$^2$ dmol$^{-1}$)")
ax.set_xlim(185, 250)
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
