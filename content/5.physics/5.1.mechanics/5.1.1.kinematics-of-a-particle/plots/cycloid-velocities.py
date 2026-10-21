"""A point on the rim of a wheel rolling without slipping traces a cycloid.
Its velocity at each instant is perpendicular to the line joining it to the contact point."""

import numpy as np
import matplotlib.pyplot as plt

R = 1.0
vC = 1.0
omega = vC / R

fig, ax = plt.subplots(figsize=(7.5, 4.0))
phi = np.linspace(0, 4 * np.pi, 600)  # rolling angle
ax.plot(R * (phi - np.sin(phi)), R * (1 - np.cos(phi)), color="C0", lw=1.8, label="path of a rim point (cycloid)")
ax.axhline(0, color="0.5", lw=1)

phi0 = 2.2  # snapshot of the wheel
xc = R * phi0
circle = np.linspace(0, 2 * np.pi, 200)
ax.plot(xc + R * np.cos(circle), R + R * np.sin(circle), color="0.55", lw=1.2)
ax.plot(xc, R, "o", color="0.3", ms=4)
ax.plot(xc, 0, "o", color="C3", ms=5, label="contact point P (instantaneously at rest)")
ax.annotate("", xy=(xc + 0.6, R), xytext=(xc, R), arrowprops=dict(arrowstyle="->", color="0.3", lw=1.4))
ax.text(xc + 0.25, R + 0.12, "vC", fontsize=9)

# velocities of several rim points of this snapshot: v = omega x (r - rP)
for psi in np.linspace(0, 2 * np.pi, 9)[:-1]:
    px, py = xc + R * np.sin(psi), R - R * np.cos(psi)
    rx, ry = px - xc, py  # vector from contact point to the rim point
    vx, vy = omega * ry, -omega * rx
    ax.plot([xc, px], [0, py], color="C3", lw=0.6, ls=":")
    ax.annotate("", xy=(px + 0.3 * vx, py + 0.3 * vy), xytext=(px, py),
                arrowprops=dict(arrowstyle="->", color="C1", lw=1.4))
ax.plot(R * (phi0 - np.sin(phi0)), R * (1 - np.cos(phi0)), "o", color="C0", ms=5)
ax.text(R * (phi0 - np.sin(phi0)) - 0.35, R * (1 - np.cos(phi0)) + 0.1, "A", fontsize=9)
ax.plot([], [], color="C1", lw=1.4, label="velocities of rim points (scaled)")

ax.set_aspect("equal")
ax.set_xlim(-0.3, 4 * np.pi * R + 0.3)
ax.set_ylim(-0.3, 2.4)
ax.set_xlabel("x / R")
ax.set_ylabel("y / R")
ax.set_title("Rolling without slipping: v = 2 vC sin(theta/2), directed perpendicular to PA")
ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2)
fig.tight_layout()
