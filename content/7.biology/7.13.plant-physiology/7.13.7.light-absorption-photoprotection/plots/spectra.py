"""Absorption spectra of the photosynthetic pigments and the action spectrum of a leaf.

A: schematic absorption spectra of chlorophyll a and b and of two carotenoids in organic solvent,
built from Gaussian bands at the absorption maxima in diethyl ether (chlorophyll a 430/662 nm,
chlorophyll b 453/642 nm, beta-carotene 425/450/478 nm, lutein 422/445/474 nm), each scaled to its
own maximum. B: leaf absorptance and the action spectrum of CO2 uptake per incident photon
(approximate shape of the mean curve for crop leaves measured by McCree 1972), and the quantum yield
per absorbed photon (their ratio). Curves are approximations for illustration, not data.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
lam = np.linspace(380, 750, 741)


def band(c, w, h=1.0):
    return h * np.exp(-0.5 * ((lam - c) / w) ** 2)


chla = band(430, 13, 1.0) + band(410, 18, 0.45) + band(662, 9, 1.05) + band(615, 14, 0.12) + band(580, 20, 0.05)
chlb = band(453, 13, 1.0) + band(430, 15, 0.35) + band(642, 9, 0.36) + band(595, 15, 0.07)
car = band(425, 9, 0.72) + band(450, 10, 1.0) + band(478, 10, 0.86) + band(400, 14, 0.25)
lut = band(422, 9, 0.75) + band(445, 10, 1.0) + band(474, 10, 0.88) + band(398, 14, 0.25)
spectra = [("Chlorophyll a", chla, P.edge("plant")), ("Chlorophyll b", chlb, P.edge("enzyme")),
           ("β-Carotene", car, P.edge("rna")), ("Lutein", lut, P.edge("highlight"))]

# leaf absorptance and action spectrum (approximate)
pts = [400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 690, 700, 710, 720, 740, 750]
act = [0.55, 0.66, 0.72, 0.70, 0.66, 0.66, 0.68, 0.70, 0.74, 0.84, 0.95, 1.0, 0.97, 0.95, 0.88, 0.70, 0.45,
       0.25, 0.12, 0.03, 0.02]
absp = [0.90, 0.91, 0.92, 0.92, 0.91, 0.90, 0.84, 0.79, 0.76, 0.79, 0.86, 0.89, 0.91, 0.92, 0.91, 0.86, 0.62,
        0.32, 0.13, 0.05, 0.04]
lam2 = np.linspace(400, 750, 351)
A = np.interp(lam2, pts, absp)
Y = np.interp(lam2, pts, act)
Q = Y / A
Q = Q / Q[(lam2 > 550) & (lam2 < 690)].max()

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
for name, s, col in spectra:
    a.plot(lam, s / s.max(), color=col, lw=2, label=name)
a.set_xlim(380, 750)
a.set_ylim(0, 1.08)
a.set_xlabel("Wavelength $\\lambda$ / nm")
a.set_ylabel("Relative absorbance (in solvent)")
a.legend(frameon=False, fontsize=8, loc="upper right")
a.set_title("A  Pigments in organic solvent", loc="left", fontsize=10)

b.plot(lam2, A, color=P.edge("plant"), lw=2, label="Leaf absorptance")
b.plot(lam2, Y, color=P.edge("rna"), lw=2, label="Action spectrum (per incident photon)")
m = lam2 < 705
b.plot(lam2[m], Q[m], color=P.edge("dna"), lw=1.6, ls="--", label="Quantum yield (per absorbed photon)")
b.axvspan(400, 700, color=P.mix(P.fill("highlight"), P.surface(), 0.75), lw=0, zorder=0)
b.text(550, 0.08, "PAR 400–700 nm", ha="center", fontsize=8, color=P.muted())
b.set_xlim(400, 750)
b.set_ylim(0, 1.08)
b.set_xlabel("Wavelength $\\lambda$ / nm")
b.set_ylabel("Relative value")
b.legend(frameon=False, fontsize=8, loc="lower left", bbox_to_anchor=(0.0, 0.12))
b.set_title("B  Intact leaf", loc="left", fontsize=10)
for ax in (a, b):
    ax.grid(True, alpha=0.3)
fig.tight_layout()
