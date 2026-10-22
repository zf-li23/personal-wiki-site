"""Schematic of how solution properties of an ionic surfactant (sodium dodecyl sulfate, CMC
about 8.2 mmol/L at 25 C) change at the critical micelle concentration: surface tension levels
off, the slope of conductivity drops (micelles bind counterions and move slowly), the osmotic
pressure nearly stops rising, and the solubility of a hydrophobic dye starts to increase.
Pseudo-phase model: the monomer concentration stays at the CMC above it."""

import numpy as np
import matplotlib.pyplot as plt

cmc = 8.2
c = np.linspace(0.01, 20, 800)                 # mmol L^-1
free = np.minimum(c, cmc)
mic = np.maximum(c - cmc, 0)

gamma = 72.0 - 13.0 * np.log1p(free / 0.6)
kappa = 0.072 * free + 0.030 * mic             # mS cm^-1, slopes roughly as for SDS
osm = 2 * free + 0.25 * mic                    # arbitrary scale
dye = 0.06 * mic                               # arbitrary scale

fig, axes = plt.subplots(2, 2, figsize=(7.6, 5.2), sharex=True)
data = [(gamma, r"$\gamma\,/\,\mathrm{mN\,m^{-1}}$", "surface tension"),
        (kappa, r"$\sigma\,/\,\mathrm{mS\,cm^{-1}}$", "conductivity"),
        (osm, "osmotic pressure (a.u.)", "osmotic pressure"),
        (dye, "solubilized dye (a.u.)", "solubilization")]
for ax, (y, lab, title), col in zip(axes.flat, data, ["C0", "C1", "C2", "C3"]):
    ax.plot(c, y, color=col, lw=1.8)
    ax.axvline(cmc, color="0.6", lw=0.9, ls="--")
    ax.set_ylabel(lab, fontsize=9)
    ax.set_title(title, fontsize=9)
    ax.set_xlim(0, 20)
for ax in axes[1]:
    ax.set_xlabel(r"$c\,/\,\mathrm{mmol\,L^{-1}}$")
ylo, yhi = axes[0, 0].get_ylim()
axes[0, 0].text(cmc + 0.4, yhi - 0.05 * (yhi - ylo), "CMC", va="top", fontsize=9)
fig.tight_layout()
