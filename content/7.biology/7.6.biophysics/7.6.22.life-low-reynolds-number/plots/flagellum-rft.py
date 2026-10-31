"""Resistive-force theory of a rotating helical flagellum. A filament segment with tangent at
pitch angle theta to the helix axis moves sideways at v = omega R (R: helix radius); because the
drag coefficient per length is larger across the filament than along it (gamma_perp = 2
gamma_par for a slender rod), the drag on each segment has a component along the axis: thrust.
A: swimming speed U of a cell (body: sphere of radius 0.8 um; helix: R = 0.2 um, length
7 um, filament diameter 20 nm, rotating at 100 Hz relative to the fluid), as a function of
theta, for gamma_perp/gamma_par = 1 (no thrust), 1.5 and 2. B: propulsive efficiency, the power
needed to drag the body at U divided by the power dissipated by the helix: at most about 2 %.
Body counter-rotation and hydrodynamic interactions are neglected."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
eta = 1e-3
Rh, Lh, d, a, f = 0.2e-6, 7e-6, 20e-9, 0.8e-6, 100.0
omega = 2 * np.pi * f
lam = 2.3e-6
gpar0 = 2 * np.pi * eta / (np.log(2 * 0.09 * lam / (d / 2)) - 0.5)  # Lighthill-type coefficient per length
th = np.linspace(0.02, np.pi / 2 - 0.02, 300)


def swim(ratio):
    gpar, gper = gpar0, ratio * gpar0
    c, s = np.cos(th), np.sin(th)
    v = omega * Rh
    # axial force per length on a segment moving with azimuthal speed v and axial speed U:
    # thrust (gper - gpar) v s c minus axial drag (gpar c^2 + gper s^2) U
    thrust = Lh * (gper - gpar) * v * s * c
    drag_h = Lh * (gpar * c**2 + gper * s**2)
    U = thrust / (drag_h + 6 * np.pi * eta * a)
    # relative velocity of a segment: azimuthal v, axial -U; split into tangential and normal parts
    wt = v * s - U * c
    wn2 = v**2 + U**2 - wt**2
    Pw = Lh * (gpar * wt**2 + gper * wn2)
    return U, 6 * np.pi * eta * a * U**2 / Pw


fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.18, top=0.87)
cols = {1.0: "neutral", 1.5: "dna", 2.0: "blood"}
for ratio in (1.0, 1.5, 2.0):
    U, eff = swim(ratio)
    lab = rf"$\gamma_\perp/\gamma_\parallel = {ratio:g}$"
    axs[0].plot(np.degrees(th), U * 1e6, color=charts.line(cols[ratio]), lw=1.7, label=lab)
    axs[1].plot(np.degrees(th), eff * 100, color=charts.line(cols[ratio]), lw=1.7, label=lab)
th_ecoli = np.degrees(np.arctan(2 * np.pi * Rh / lam))
for ax in axs:
    ax.axvline(th_ecoli, color=P.muted(), lw=0.7, ls=":")
axs[0].text(th_ecoli + 1, 2, r"$E.\ coli$", fontsize=bio.core.FONT["tiny"], color=P.ink())
axs[0].legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(axs[0], r"pitch angle $\theta$ / degree", r"swimming speed U / $\mu$m s$^{-1}$")
charts.title(axs[0], "A  Thrust needs anisotropic drag")
charts.style_axes(axs[1], r"pitch angle $\theta$ / degree", "efficiency / %")
charts.title(axs[1], "B  Swimming is wasteful")
