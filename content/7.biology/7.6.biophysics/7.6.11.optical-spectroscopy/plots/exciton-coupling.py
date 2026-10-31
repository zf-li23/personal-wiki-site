# Exciton coupling of two identical chromophores with transition dipoles of 5 D at R = 1 nm (point-dipole).
# A: energies E0 +/- V of the two exciton states for parallel dipoles as a function of the angle theta between
#    the dipoles and the line joining them, V = mu^2 (1 - 3 cos^2 theta) / (4 pi eps0 n^2 R^3), n^2 = 1.77;
#    the allowed (in-phase) state is drawn thick: H aggregates (theta = 90 deg) shift blue, J aggregates
#    (theta = 0) shift red, and the splitting vanishes at the magic angle 54.7 deg.
# B: absorption of the monomer and of H and J dimers (Gaussian bands, 260 cm^-1 coupling exaggerated x10 so
#    the shifts are visible), normalized per chromophore.
# C: a twisted dimer (dipoles at 60 deg to each other): both exciton bands are allowed, and they carry equal and
#    opposite rotational strengths, giving a conservative CD couplet whose sign encodes the handedness.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
D = 3.33564e-30
mu, R, n2 = 5 * D, 1e-9, 1.77
V0 = mu**2 / (1.11265e-10 * n2 * R**3) / 1.98645e-23     # cm^-1
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
ax = axs[0]
th = np.linspace(0, 90, 300)
V = V0 * (1 - 3 * np.cos(np.radians(th)) ** 2)
ax.plot(th, V, color=charts.line("dna"), lw=2.6, label="in-phase (allowed)")
ax.plot(th, -V, color=charts.line("dna"), lw=0.9, ls="--", label="out-of-phase (forbidden)")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(54.7, color=P.muted(), lw=0.7, ls=":")
ax.text(56, -120, "54.7°", fontsize=8, color=P.muted())
ax.text(3, -125, "J (head-to-tail): red shift", fontsize=8, color=P.ink())
ax.text(55, 90, "H (side-by-side):\nblue shift", fontsize=8, color=P.ink())
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "angle θ between dipoles and axis / °", "E - E₀ / cm⁻¹")
charts.title(ax, f"A   Exciton splitting, |V| ≤ {2 * V0:.0f} cm⁻¹")

ax = axs[1]
nu = np.linspace(33000, 45000, 800)
nu0, w = 38500.0, 900.0
g = lambda c: np.exp(-((nu - c) ** 2) / (2 * w**2))
Vx = 10 * V0
ax.plot(nu / 1e3, g(nu0), color=P.muted(), lw=1.4, ls="--", label="monomer")
ax.plot(nu / 1e3, 0.85 * g(nu0 + Vx), color=charts.line("rna"), lw=1.8, label="H dimer (hypochromic)")
ax.plot(nu / 1e3, 1.1 * g(nu0 - 2 * Vx), color=charts.line("dna"), lw=1.8, label="J dimer")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "wavenumber / (10³ cm⁻¹)", "ε per chromophore (rel.)")
charts.title(ax, "B   H and J aggregates (V × 10)")

ax = axs[2]
Vt = 6 * V0
ax.plot(nu / 1e3, g(nu0 - Vt) - g(nu0 + Vt), color=charts.line("positive"), lw=1.8, label="right-handed twist")
ax.plot(nu / 1e3, -(g(nu0 - Vt) - g(nu0 + Vt)), color=charts.line("negative"), lw=1.2, ls="--", label="mirror image")
ax.plot(nu / 1e3, 0.5 * (g(nu0 - Vt) + g(nu0 + Vt)), color=P.muted(), lw=1.0, ls=":", label="absorption")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(nu0 / 1e3, color=P.muted(), lw=0.6, ls=":")
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "wavenumber / (10³ cm⁻¹)", "Δε (rel.)")
charts.title(ax, "C   Exciton CD couplet")
fig.tight_layout()
