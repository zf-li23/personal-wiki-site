"""Falling and projectile motion with air resistance.
Left: speed of a body dropped from rest with linear and quadratic drag, in units of the terminal speed.
Right: trajectories of a projectile with quadratic drag, integrated numerically with solve_ivp."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g = 9.8

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.0))

# Left panel: dimensionless time g t / vT
s = np.linspace(0, 4, 300)
ax1.plot(s, 1 - np.exp(-s), color="C0", lw=1.8, label="linear drag: 1 - exp(-g t / vT)")
ax1.plot(s, np.tanh(s), color="C1", lw=1.8, label="quadratic drag: tanh(g t / vT)")
ax1.plot(s, s, color="0.5", ls=":", lw=1.2, label="no drag: g t")
ax1.axhline(1, color="0.4", ls="--", lw=1)
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 1.25)
ax1.set_xlabel("g t / vT")
ax1.set_ylabel("v / vT")
ax1.set_title("Falling from rest")
ax1.legend(fontsize=8, loc="lower right")

# Right panel: projectile with drag force -k |v| v per unit mass, k = 1/(2 m) * C rho A
v0 = 50.0
theta = np.radians(45)


def rhs(t, y, k):
    x, z, vx, vz = y
    sp = np.hypot(vx, vz)
    return [vx, vz, -k * sp * vx, -g - k * sp * vz]


def hit_ground(t, y, k):
    return y[1]


hit_ground.terminal = True
hit_ground.direction = -1

for i, vT in enumerate([np.inf, 60.0, 30.0, 15.0]):
    k = 0.0 if np.isinf(vT) else g / vT**2  # terminal speed vT = sqrt(g / k)
    sol = solve_ivp(rhs, (0, 20), [0, 0, v0 * np.cos(theta), v0 * np.sin(theta)],
                    args=(k,), events=hit_ground, max_step=0.02, rtol=1e-8)
    label = "no drag" if np.isinf(vT) else f"vT = {vT:.0f} m/s"
    ax2.plot(sol.y[0], sol.y[1], color=f"C{i}", lw=1.8, label=label)
ax2.set_xlim(0, 270)
ax2.set_ylim(0, 70)
ax2.set_xlabel("x / m")
ax2.set_ylabel("y / m")
ax2.set_title("Projectile, v0 = 50 m/s at 45 deg, quadratic drag")
ax2.legend(fontsize=8, loc="upper right")
fig.tight_layout()
