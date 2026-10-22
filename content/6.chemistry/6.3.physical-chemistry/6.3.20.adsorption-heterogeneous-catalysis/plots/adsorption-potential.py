"""One-dimensional potential energy curves (Lennard-Jones picture) for H2 approaching a metal
surface: a shallow physisorption well for the intact molecule, and a deep chemisorption well
for two H atoms whose asymptote lies at the H-H bond energy (436 kJ/mol). Where the two curves
cross above zero energy, dissociative chemisorption is activated with barrier E_a; a crossing
below zero would make it non-activated."""

import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0.08, 0.8, 800)          # nm from the surface


def morse(z, D, a, z0):
    return D * ((1 - np.exp(-a * (z - z0))) ** 2 - 1)


phys = morse(z, 8.0, 14.0, 0.32)
chem = 436.0 + morse(z, 526.0, 11.0, 0.16)
k = np.argmin(np.abs(phys - chem) + (z < 0.2) * 1e3)
fig, ax = plt.subplots(figsize=(6.0, 3.9))
ax.plot(z, phys, color="C0", lw=1.8, label=r"physisorbed $\mathrm{H_2}$")
ax.plot(z, chem, color="C3", lw=1.8, label=r"chemisorbed $2\mathrm{H}$")
ax.axhline(0, color="0.6", lw=0.8)
ax.plot(z[k], phys[k], "o", color="k", ms=4)
ax.annotate(r"$E_\mathrm{a}$", (z[k], phys[k]), (z[k] + 0.08, phys[k] + 40), fontsize=9,
            arrowprops=dict(arrowstyle="-", lw=0.7))
ax.set_xlim(0.08, 0.8)
ax.set_ylim(-120, 200)
ax.set_xlabel(r"distance from surface $z\,/\,\mathrm{nm}$")
ax.set_ylabel(r"$E\,/\,\mathrm{kJ\,mol^{-1}}$")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
