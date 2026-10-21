"""Fresnel reflectances Rs, Rp for air to glass (n = 1.5) and the degree of polarization of reflected natural light."""

import numpy as np
import matplotlib.pyplot as plt

n1, n2 = 1.0, 1.5
i = np.radians(np.linspace(0.01, 89.99, 2000))
r = np.arcsin(n1 * np.sin(i) / n2)
Rs = (np.sin(i - r) / np.sin(i + r)) ** 2
Rp = (np.tan(i - r) / np.tan(i + r)) ** 2
P = (Rs - Rp) / (Rs + Rp)
iB = np.degrees(np.arctan(n2 / n1))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 3.6))
deg = np.degrees(i)
ax1.plot(deg, Rs, color="C0", lw=1.6, label="Rs (s component)")
ax1.plot(deg, Rp, color="C1", lw=1.6, label="Rp (p component)")
ax1.plot(deg, (Rs + Rp) / 2, color="0.5", lw=1.0, ls="--", label="natural light")
ax1.axvline(iB, color="C3", lw=0.8, ls=":")
ax1.text(iB - 1, 0.85, f"iB = {iB:.1f}°", color="C3", fontsize=8, ha="right")
ax1.set_xlabel("angle of incidence  i  (degrees)")
ax1.set_ylabel("reflectance")
ax1.set_xlim(0, 90)
ax1.set_ylim(0, 1)
ax1.legend(loc="upper left", fontsize=8, frameon=False)
ax1.grid(alpha=0.25)

ax2.plot(deg, P, color="C2", lw=1.6)
ax2.axvline(iB, color="C3", lw=0.8, ls=":")
ax2.set_xlabel("angle of incidence  i  (degrees)")
ax2.set_ylabel("degree of polarization of reflected light")
ax2.set_xlim(0, 90)
ax2.set_ylim(0, 1.05)
ax2.grid(alpha=0.25)
fig.tight_layout()
