"""Karplus relations for vicinal coupling constants.
Left: 3J(H-C-C-H) = A cos^2(phi) + B cos(phi) + C with typical parameters A = 7.8,
B = -1.0, C = 1.4 Hz, with the dihedral angles of axial-axial and axial-equatorial protons
in a cyclohexane chair. Right: 3J(HN-Halpha) of a peptide as a function of the backbone
angle phi (Vuister and Bax 1993: A = 6.51, B = -1.76, C = 1.60 Hz, theta = phi - 60 deg),
with the typical phi of the alpha helix and the beta sheet."""

import numpy as np
import matplotlib.pyplot as plt


def karplus(theta_deg, A, B, C):
    t = np.radians(theta_deg)
    return A * np.cos(t)**2 + B * np.cos(t) + C


fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax = axes[0]
phi = np.linspace(0, 180, 361)
ax.plot(phi, karplus(phi, 7.8, -1.0, 1.4), color="k", lw=1.8)
for ang, lab in [(60, "ax-eq / eq-eq\n(60 deg)"), (180, "ax-ax\n(180 deg)")]:
    ax.plot(ang, karplus(ang, 7.8, -1.0, 1.4), "o", color="C3")
    ax.text(ang - (8 if ang == 180 else -6), karplus(ang, 7.8, -1.0, 1.4) + 0.6, lab,
            fontsize=8, ha="right" if ang == 180 else "left", color="C3")
ax.set_xlim(0, 180)
ax.set_ylim(0, 12)
ax.set_xticks(range(0, 181, 30))
ax.set_xlabel(r"H-C-C-H dihedral angle $\phi$ / deg")
ax.set_ylabel(r"$^3J_{\mathrm{HH}}$ / Hz")
ax.set_title("vicinal H-C-C-H coupling", fontsize=10)

ax = axes[1]
p = np.linspace(-180, 180, 721)
J = karplus(p - 60, 6.51, -1.76, 1.60)
ax.plot(p, J, color="k", lw=1.8)
ax.axvspan(-70, -50, color="C0", alpha=0.18, lw=0)
ax.axvspan(-140, -110, color="C3", alpha=0.18, lw=0)
ax.text(-60, 10.4, "alpha\nhelix", ha="center", fontsize=8, color="C0")
ax.text(-125, 10.4, "beta\nsheet", ha="center", fontsize=8, color="C3")
for ph, col in [(-57, "C0"), (-120, "C3")]:
    ax.plot(ph, karplus(ph - 60, 6.51, -1.76, 1.60), "o", color=col)
    ax.text(ph + 9, karplus(ph - 60, 6.51, -1.76, 1.60) - 0.9,
            f"{karplus(ph - 60, 6.51, -1.76, 1.60):.1f} Hz", fontsize=8, color=col)
ax.set_xlim(-180, 180)
ax.set_ylim(0, 12)
ax.set_xticks(range(-180, 181, 60))
ax.set_xlabel(r"backbone dihedral angle $\phi$ / deg")
ax.set_ylabel(r"$^3J_{\mathrm{HN,H\alpha}}$ / Hz")
ax.set_title("peptide backbone", fontsize=10)
fig.tight_layout()
