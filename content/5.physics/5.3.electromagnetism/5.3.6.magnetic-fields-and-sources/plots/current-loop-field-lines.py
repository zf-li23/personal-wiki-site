"""Magnetic field lines of a circular current loop (radius a) in a plane containing its axis.
Field lines are contours of the flux function Psi = rho * A_phi, computed exactly with complete
elliptic integrals; far from the loop they approach the field lines of a magnetic dipole."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipk, ellipe

a = 1.0
x = np.linspace(-3, 3, 601)
z = np.linspace(-3, 3, 601)
X, Z = np.meshgrid(x, z)
rho = np.abs(X) + 1e-12

# A_phi in units of mu0 I / pi; parameter m = k^2
m = 4 * a * rho / ((a + rho) ** 2 + Z**2)
k = np.sqrt(m)
A_phi = np.sqrt(a / rho) / k * ((1 - m / 2) * ellipk(m) - ellipe(m))
Psi = rho * A_phi

fig, ax = plt.subplots(figsize=(6, 6))
levels = np.geomspace(0.02, 1.2, 14)
ax.contour(X, Z, Psi, levels=levels, colors="C0", linewidths=1.1)
# current out of the page at x = -a and into the page at x = +a (seen with x to the right, z up)
# arrows: the field points along +z inside the loop and turns back outside
for xa in (-0.5, 0.0, 0.5):
    ax.annotate("", xy=(xa, 0.25), xytext=(xa, -0.05), arrowprops=dict(arrowstyle="-|>", color="C0", lw=1.2))
for xa in (-2.2, 2.2):
    ax.annotate("", xy=(xa, -0.25), xytext=(xa, 0.05), arrowprops=dict(arrowstyle="-|>", color="C0", lw=1.2))
ax.plot(-a, 0, marker="$\\odot$", ms=12, color="C3", ls="none")
ax.plot(a, 0, marker="$\\otimes$", ms=12, color="C3", ls="none")
ax.set_aspect("equal")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel(r"$x / a$")
ax.set_ylabel(r"$z / a$ (axis of the loop)")
ax.set_title("Field lines of a current loop", fontsize=10)
fig.tight_layout()
