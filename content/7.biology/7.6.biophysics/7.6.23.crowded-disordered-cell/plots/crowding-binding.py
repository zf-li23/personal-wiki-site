"""Crowding shifts binding equilibria. A: lattice model of a receptor in a volume of Omega = 1000
lattice cells holding L ligands and C inert crowders of the same size (binding energy -5 kB T):
p_bound = 1 / (1 + (Omega - L - C)/L * exp(beta eps)); crowders occupy volume the ligands could
otherwise explore and raise the occupancy. B: dissociation constant of a complex relative to its
dilute value against the crowder volume fraction phi: lattice model (1 - phi)^r for a ligand r
times larger than a crowder (r = 15, the mass ratio of the T4 clamp loader and PEG 12000, and
r = 45, the value fitted to the measurements), and scaled-particle theory for the dimerization
of two hard spheres of radius 2.5 nm in hard-sphere crowders of radius 2 or 5 nm. Small crowders
at the same volume fraction exclude more volume and stabilize complexes more."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.17, top=0.87)

ax = axs[0]
Om, eps = 1000, -5.0
L = np.arange(1, 101)
for C, tok in ((0, "neutral"), (400, "dna"), (800, "blood")):
    pb = 1 / (1 + (Om - L - C) / L * np.exp(eps))
    ax.plot(L, pb, color=charts.line(tok), lw=1.7, label=f"C = {C}")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "number of ligands L", r"$p_{\mathrm{bound}}$")
charts.title(ax, r"A  Lattice model, $\Omega = 1000$")


def ln_gamma(z, phi):
    """Scaled-particle theory: excess chemical potential / kT of a hard sphere of radius z (in
    units of the crowder radius) in a hard-sphere fluid of volume fraction phi."""
    y = phi / (1 - phi)
    return -np.log(1 - phi) + (3 * z + 3 * z**2 + z**3) * y + (4.5 * z**2 + 3 * z**3) * y**2 + 3 * z**3 * y**3


ax = axs[1]
phi = np.linspace(0, 0.3, 200)
for r, ls in ((15, "--"), (45, ":")):
    ax.plot(phi, (1 - phi) ** r, color=P.muted(), lw=1.2, ls=ls, label=f"lattice, r = {r}")
Ra = 2.5
Rab = Ra * 2 ** (1 / 3)
for rc, tok in ((2.0, "blood"), (5.0, "dna")):
    lnK = ln_gamma(Rab / rc, phi) - 2 * ln_gamma(Ra / rc, phi)
    ax.plot(phi, np.exp(lnK), color=charts.line(tok), lw=1.7, label=f"hard spheres, crowder {rc:g} nm")
ax.set_yscale("log"); ax.set_ylim(1e-3, 1.5)
ax.axvspan(0.2, 0.3, color=P.fill("cytoplasm"), alpha=0.35, lw=0)
ax.text(0.205, 1.1e-3, "cytoplasm", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"crowder volume fraction $\varphi$", r"$K_{\mathrm{d}}(\varphi)/K_{\mathrm{d}}(0)$")
charts.title(ax, "B  Complexes are stabilized")
