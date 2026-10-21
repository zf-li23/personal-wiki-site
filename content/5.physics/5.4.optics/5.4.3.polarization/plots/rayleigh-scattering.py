"""Angular distribution of Rayleigh-scattered light and its degree of polarization."""

import numpy as np
import matplotlib.pyplot as plt

ang = np.linspace(0, 2 * np.pi, 721)

fig = plt.figure(figsize=(10.0, 3.6))
ax1 = fig.add_subplot(1, 3, 1, projection="polar")
ax1.plot(ang, np.sin(ang) ** 2, color="C0", lw=1.6)
ax1.set_theta_zero_location("N")
ax1.set_title("linearly polarized along y\nI ∝ sin²ψ (ψ from y, drawn up)", fontsize=8.5, pad=16)
ax1.set_rticks([0.5, 1.0])
ax1.tick_params(labelsize=7)

ax2 = fig.add_subplot(1, 3, 2, projection="polar")
ax2.plot(ang, 1 + np.cos(ang) ** 2, color="C1", lw=1.6)
ax2.set_title("unpolarized, incident along z (0°)\nI ∝ 1 + cos²θ", fontsize=8.5, pad=16)
ax2.set_rticks([1.0, 2.0])
ax2.tick_params(labelsize=7)

ax3 = fig.add_subplot(1, 3, 3)
th = np.linspace(0, 180, 361)
P = np.sin(np.radians(th)) ** 2 / (1 + np.cos(np.radians(th)) ** 2)
ax3.plot(th, P, color="C2", lw=1.6)
ax3.set_xlabel("scattering angle θ (degrees)")
ax3.set_ylabel("degree of polarization P")
ax3.set_xlim(0, 180)
ax3.set_ylim(0, 1.05)
ax3.set_xticks([0, 45, 90, 135, 180])
ax3.grid(alpha=0.25)
fig.tight_layout()
