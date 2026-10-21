"""A puck sliding without friction on a turntable rotating counterclockwise.
In the inertial frame its path is a straight line; seen from the turntable the path curves to the right,
which is the combined effect of the centrifugal and Coriolis forces."""

import numpy as np
import matplotlib.pyplot as plt

omega = 1.0  # angular velocity of the turntable (counterclockwise), rad/s
R = 1.0
t = np.linspace(0, 2.0, 400)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.4))
cases = [((-1.0, 0.0), (1.0, 0.0)), ((-1.0, -0.4), (0.9, 0.5))]  # initial position and velocity (inertial)
for i, (r0, v0) in enumerate(cases):
    x = r0[0] + v0[0] * t
    y = r0[1] + v0[1] * t
    keep = np.hypot(x, y) <= R + 1e-9
    x, y, tt = x[keep], y[keep], t[keep]
    ax1.plot(x, y, color=f"C{i}", lw=1.8)
    ax1.plot(x[0], y[0], "o", color=f"C{i}", ms=4)
    # coordinates in the rotating frame: rotate by -omega t
    c, s = np.cos(omega * tt), np.sin(omega * tt)
    xr, yr = c * x + s * y, -s * x + c * y
    ax2.plot(xr, yr, color=f"C{i}", lw=1.8)
    ax2.plot(xr[0], yr[0], "o", color=f"C{i}", ms=4)

phi = np.linspace(0, 2 * np.pi, 300)
for ax, title in [(ax1, "Inertial frame: straight lines"), (ax2, "Rotating frame: paths bend to the right")]:
    ax.plot(R * np.cos(phi), R * np.sin(phi), color="0.5", lw=1)
    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xlabel("x / R")
    ax.set_ylabel("y / R")
    ax.set_title(title, fontsize=10)
ax1.annotate("", xy=(0.55, 0.85), xytext=(0.85, 0.55),
             arrowprops=dict(arrowstyle="->", color="0.4", connectionstyle="arc3,rad=0.25"))
ax1.text(0.62, 0.45, "omega", fontsize=9, color="0.4")
fig.suptitle("Puck on a turntable rotating counterclockwise (omega R / v0 = 1)", fontsize=11)
fig.tight_layout()
