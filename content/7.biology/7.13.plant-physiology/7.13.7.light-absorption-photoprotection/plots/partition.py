"""Fate of the light absorbed by PSII antennae as photon flux increases (Kramer et al. 2004 partition).

Model: linear electron transport J follows a non-rectangular hyperbola in absorbed light
(J = smaller root of 0.7 J^2 - (a I + Jmax) J + a I Jmax = 0, a = 0.84 x 0.5 x 0.83, Jmax = 200 umol m-2 s-1),
so Phi_PSII = J / (0.84 x 0.5 x I); NPQ rises with light as a Hill function (NPQmax = 2.5, K = 500, n = 2).
From the fluorescence definitions, Phi_NO = (1 - Phi_PSII)/(1 + NPQ) and Phi_NPQ = (1 - Phi_PSII) NPQ/(1 + NPQ),
so Phi_PSII + Phi_NPQ + Phi_NO = 1. A: the three fractions; B: the same partition as fluxes of photons
absorbed by PSII (0.5 x 0.84 x I). Illustrative parameters for a sun leaf.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
I = np.linspace(1, 2000, 400)
alpha = 0.84 * 0.5 * 0.83
jmax, th = 200.0, 0.7
s = alpha * I + jmax
J = (s - np.sqrt(s * s - 4 * th * alpha * I * jmax)) / (2 * th)
phi = J / (0.84 * 0.5 * I)
npq = 2.5 * I ** 2 / (I ** 2 + 500.0 ** 2)
pno = (1 - phi) / (1 + npq)
pnpq = (1 - phi) * npq / (1 + npq)
cols = [P.fill("plant"), P.fill("rna"), P.fill("negative")]
names = ["$\\Phi_{\\mathrm{PSII}}$ photochemistry", "$\\Phi_{\\mathrm{NPQ}}$ regulated heat dissipation",
         "$\\Phi_{\\mathrm{NO}}$ non-regulated losses"]

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
a.stackplot(I, phi, pnpq, pno, colors=cols, labels=names, edgecolor=P.surface(), lw=0.5)
a.set_ylim(0, 1)
a.set_xlim(0, 2000)
a.set_xlabel("PPFD / µmol m$^{-2}$ s$^{-1}$")
a.set_ylabel("Fraction of light absorbed by PSII")
a.legend(frameon=False, fontsize=8, loc="upper right", labelcolor=P.ink())
a.set_title("A  Quantum yields", loc="left", fontsize=10)

absII = 0.5 * 0.84 * I
b.stackplot(I, phi * absII, pnpq * absII, pno * absII, colors=cols, edgecolor=P.surface(), lw=0.5)
b.set_xlim(0, 2000)
b.set_xlabel("PPFD / µmol m$^{-2}$ s$^{-1}$")
b.set_ylabel("Photon flux to PSII / µmol m$^{-2}$ s$^{-1}$")
b.text(1500, 90, "photochemistry\n(ETR)", ha="center", fontsize=8, color=P.on_fill())
b.text(1500, 380, "heat (NPQ)", ha="center", fontsize=8, color=P.on_fill())
b.text(1500, 548, "fluorescence + other", ha="center", fontsize=8, color=P.on_fill())
b.set_title("B  Absolute fluxes", loc="left", fontsize=10)
for ax in (a, b):
    ax.grid(True, alpha=0.3)
fig.tight_layout()
