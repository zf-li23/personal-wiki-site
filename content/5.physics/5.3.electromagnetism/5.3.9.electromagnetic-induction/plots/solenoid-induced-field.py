"""Induced electric field inside and outside a long solenoid whose field grows at a constant rate."""

import numpy as np
import matplotlib.pyplot as plt

R = 1.0
r = np.linspace(0, 4, 801)
# in units of (R / 2) dB/dt
E = np.where(r <= R, r / R, R / np.maximum(r, R))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1, 1.2]})

# left: field lines of E_ind (circles) and the solenoid cross-section
th = np.linspace(0, 2 * np.pi, 400)
ax1.fill(R * np.cos(th), R * np.sin(th), color="C0", alpha=0.15, lw=0)
ax1.plot(R * np.cos(th), R * np.sin(th), color="C0", lw=1.2)
for rr in [0.35, 0.7, 1.4, 2.1, 2.8]:
    ax1.plot(rr * np.cos(th), rr * np.sin(th), color="C3", lw=0.9)
    e = rr / R if rr <= R else R / rr
    # arrows: counterclockwise circulation drawn for dB/dt pointing into the page
    for phi in [0.3, 0.3 + 2 * np.pi / 3, 0.3 + 4 * np.pi / 3]:
        x, y = rr * np.cos(phi), rr * np.sin(phi)
        ax1.annotate("", xy=(x - 0.25 * e * np.sin(phi), y + 0.25 * e * np.cos(phi)), xytext=(x, y),
                     arrowprops=dict(arrowstyle="->", color="C3", lw=1.2))
for x, y in [(-0.4, -0.4), (0.4, -0.4), (-0.4, 0.4), (0.4, 0.4), (0, 0)]:
    ax1.plot(x, y, marker="x", color="C0", ms=6)
ax1.set_aspect("equal")
ax1.set_xlim(-3.2, 3.2)
ax1.set_ylim(-3.2, 3.2)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title("B into the page and increasing: closed E_ind lines", fontsize=10)

ax2.plot(r, E, lw=2, color="C3")
ax2.axvline(R, color="0.6", lw=0.8, ls="--")
ax2.text(0.35, 0.5, "E = (r/2) dB/dt", fontsize=9)
ax2.text(1.7, 0.75, "E = (R^2 / 2r) dB/dt", fontsize=9)
ax2.set_xlabel("r / R")
ax2.set_ylabel("E_ind / [(R/2) dB/dt]")
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 1.15)
ax2.set_title("magnitude of the induced field", fontsize=10)
fig.tight_layout()
