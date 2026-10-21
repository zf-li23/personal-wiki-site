"""Electric field lines of an oscillating electric dipole and its far-field radiation pattern."""

import numpy as np
import matplotlib.pyplot as plt

# field lines in a meridian plane are level curves of
# psi = sin^2(theta) * [cos(k r - w t) / (k r) - sin(k r - w t)]
k = 2 * np.pi            # wavelength = 1
wt = 0.0
n = 800
xs = np.linspace(-2.2, 2.2, n)   # x is the transverse coordinate, z is the dipole axis
X, Z = np.meshgrid(xs, xs)
R = np.hypot(X, Z)
R[R < 1e-3] = 1e-3
sin2 = (X / R) ** 2
psi = sin2 * (np.cos(k * R - wt) / (k * R) - np.sin(k * R - wt))
psi[R < 0.05] = np.nan

fig = plt.figure(figsize=(10, 4.6))
ax1 = fig.add_subplot(1, 2, 1)
levels = [-3, -1.5, -0.8, -0.5, -0.25, 0.25, 0.5, 0.8, 1.5, 3]
ax1.contour(X, Z, psi, levels=levels, colors="C0", linewidths=0.8, linestyles="solid")
ax1.plot([0, 0], [-0.06, 0.06], color="C3", lw=3)
ax1.set_aspect("equal")
ax1.set_xlabel("x / wavelength")
ax1.set_ylabel("z / wavelength (dipole axis)")
ax1.set_title("E field lines at one instant: closed loops detach and travel outward", fontsize=9)

th = np.linspace(0, 2 * np.pi, 721)
ax2 = fig.add_subplot(1, 2, 2, projection="polar")
ax2.plot(th, np.sin(th) ** 2, color="C3", lw=2)
ax2.set_theta_zero_location("N")
ax2.set_rticks([0.5, 1.0])
ax2.set_title("radiated intensity ~ sin^2(theta), theta from the dipole axis", fontsize=9)
fig.tight_layout()
