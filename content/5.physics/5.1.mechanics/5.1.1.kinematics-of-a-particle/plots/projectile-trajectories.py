"""Projectile trajectories without air resistance for one launch speed and several angles,
with the envelope of all trajectories (the safety parabola)."""

import numpy as np
import matplotlib.pyplot as plt

g = 9.8
v0 = 20.0  # launch speed in m/s
angles = [15, 30, 45, 60, 75]

fig, ax = plt.subplots(figsize=(8.5, 4.2))
for i, deg in enumerate(angles):
    th = np.radians(deg)
    t_flight = 2 * v0 * np.sin(th) / g
    t = np.linspace(0, t_flight, 300)
    x = v0 * np.cos(th) * t
    y = v0 * np.sin(th) * t - 0.5 * g * t**2
    ax.plot(x, y, color=f"C{i}", lw=1.8, label=f"theta = {deg} deg")
    # mark the top of each trajectory
    ax.plot(v0**2 * np.sin(2 * th) / (2 * g), (v0 * np.sin(th))**2 / (2 * g), "o", color=f"C{i}", ms=4)

xe = np.linspace(0, v0**2 / g, 300)
ax.plot(xe, v0**2 / (2 * g) - g * xe**2 / (2 * v0**2), color="0.45", ls="--", lw=1.4,
        label="envelope (safety parabola)")
ax.set_xlim(0, 44)
ax.set_ylim(0, 22)
ax.set_aspect("equal")
ax.set_xlabel("x / m")
ax.set_ylabel("y / m")
ax.set_title("Projectiles with v0 = 20 m/s (no air resistance)")
ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(1.02, 1.0))
fig.tight_layout()
