# The terms of a classical (class I) force field, with representative parameters in kJ/mol.
# A: bond stretching of a C-C bond: harmonic term k_b (b - b0)^2 (b0 = 0.153 nm, k_b = 1.3e5 kJ mol^-1
#    nm^-2, in the convention without a factor 1/2) and a Morse potential with the same curvature and a
#    dissociation energy of 350 kJ/mol; the harmonic form cannot describe bond breaking but is accurate
#    for the thermal fluctuations (k_B T = 2.5 kJ/mol, dotted).
# B: angle bending, k_theta (theta - theta0)^2 with theta0 = 111 degrees, k_theta = 260 kJ mol^-1 rad^-2.
# C: torsion about the central C-C bond of butane, sum_n (V_n / 2)[1 + (-1)^(n+1) cos(n phi)] with
#    V1 = 4.6, V2 = -0.6, V3 = 6.6 kJ/mol (illustrative values close to common fits): trans minimum at
#    180 degrees, gauche minima near +-65 degrees about 3 kJ/mol higher, cis barrier about 11 kJ/mol.
# D: non-bonded terms between two atoms: Lennard-Jones 4 eps [(s/r)^12 - (s/r)^6] (eps = 0.36 kJ/mol,
#    s = 0.34 nm) and Coulomb q1 q2 / (4 pi eps0 eps_r r) for partial charges +0.25 e and -0.25 e, in vacuum
#    (eps_r = 1) and screened by water (eps_r = 80); the sum with eps_r = 1 is the usual explicit-solvent
#    form, in which the screening is provided by the water molecules themselves.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
kT = 2.48

fig, axs = plt.subplots(1, 4, figsize=(14, 3.7))
ax = axs[0]
b = np.linspace(0.11, 0.30, 300)
b0, kb, De = 0.153, 1.3e5, 350.0
a = np.sqrt(kb / De)
ax.plot(b, kb * (b - b0) ** 2, color=charts.line("protein"), lw=1.8, label="harmonic")
ax.plot(b, De * (1 - np.exp(-a * (b - b0))) ** 2, color=charts.line("negative"), lw=1.4, ls="--", label="Morse")
ax.axhline(kT, color=P.muted(), lw=0.7, ls=":")
ax.set_ylim(0, 450)
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "bond length b / nm", "energy / (kJ mol⁻¹)")
charts.title(ax, "A   Bond stretching")

ax = axs[1]
th = np.linspace(80, 140, 200)
ax.plot(th, 260 * np.deg2rad(th - 111) ** 2, color=charts.line("protein"), lw=1.8)
ax.axhline(kT, color=P.muted(), lw=0.7, ls=":")
ax.text(82, kT + 2, "k_B T", fontsize=7, color=P.muted())
charts.style_axes(ax, "bond angle θ / °", "energy / (kJ mol⁻¹)")
charts.title(ax, "B   Angle bending")

ax = axs[2]
phi = np.linspace(-180, 180, 400)
r = np.deg2rad(phi)
V1, V2, V3 = 4.6, -0.6, 6.6
U = V1 / 2 * (1 + np.cos(r)) + V2 / 2 * (1 - np.cos(2 * r)) + V3 / 2 * (1 + np.cos(3 * r))
U -= U.min()
ax.plot(phi, U, color=charts.line("protein"), lw=1.8)
for x0, name in ((180, "trans"), (-65, "gauche−"), (65, "gauche+")):
    i = np.argmin(abs(phi - x0)) if x0 != 180 else -1
    ax.annotate(name, (phi[i] if x0 != 180 else 175, U[i]), xytext=(0, 12), textcoords="offset points",
                ha="center", fontsize=7, color=P.ink())
ax.set_xticks([-180, -90, 0, 90, 180])
charts.style_axes(ax, "dihedral φ / °", "energy / (kJ mol⁻¹)")
charts.title(ax, "C   Torsion (butane)")

ax = axs[3]
rr = np.linspace(0.28, 1.2, 400)
eps, s = 0.36, 0.34
lj = 4 * eps * ((s / rr) ** 12 - (s / rr) ** 6)
ke = 138.935                                  # kJ mol^-1 nm e^-2 = 1 / (4 pi eps0)
coul = ke * 0.25 * (-0.25) / rr
ax.plot(rr, lj, color=charts.line("protein"), lw=1.6, label="Lennard-Jones")
ax.plot(rr, coul, color=charts.line("dna"), lw=1.4, label="Coulomb, ε_r = 1")
ax.plot(rr, coul / 80, color=charts.line("dna"), lw=1.2, ls=":", label="Coulomb, ε_r = 80")
ax.plot(rr, lj + coul, color=charts.line("negative"), lw=1.2, ls=(0, (4, 3)), label="LJ + Coulomb (ε_r = 1)")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-30, 10)
ax.legend(fontsize=6.8, frameon=False, loc="lower right")
charts.style_axes(ax, "distance r / nm", "energy / (kJ mol⁻¹)")
charts.title(ax, "D   Non-bonded terms")
fig.tight_layout()
