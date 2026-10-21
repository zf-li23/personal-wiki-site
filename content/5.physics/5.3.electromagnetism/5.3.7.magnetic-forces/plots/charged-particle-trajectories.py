"""Charged particle in a uniform magnetic field (helix) and in a magnetic bottle (mirror bounce)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# units: q/m = 1, B0 = 1, so the cyclotron frequency in the uniform field is 1


def rhs(t, y, field):
    r, v = y[:3], y[3:]
    return np.concatenate([v, np.cross(v, field(r))])


def uniform(r):
    return np.array([0.0, 0.0, 1.0])


L = 12.0


def bottle(r):
    # paraxial mirror field B_z = 1 + (z/L)^2, B_x, B_y chosen so that div B = 0
    x, y, z = r
    return np.array([-x * z / L**2, -y * z / L**2, 1.0 + (z / L) ** 2])


def run(field, v0, t_end):
    y0 = np.concatenate([[0.0, 0.0, 0.0], v0])
    t = np.linspace(0, t_end, 6000)
    sol = solve_ivp(rhs, (0, t_end), y0, t_eval=t, args=(field,), rtol=1e-9, atol=1e-11)
    return sol.y[:3]


theta = np.deg2rad(20)
helix = run(uniform, np.array([np.sin(theta), 0.0, np.cos(theta)]), 6 * np.pi)

alpha = np.deg2rad(50)  # pitch angle at the center; mirror point where B = 1 / sin^2(alpha)
mirror = run(bottle, np.array([np.sin(alpha), 0.0, np.cos(alpha)]), 110.0)
z_turn = L * np.sqrt(1 / np.sin(alpha) ** 2 - 1)

fig = plt.figure(figsize=(10, 4.6))

ax1 = fig.add_subplot(1, 2, 1, projection="3d")
ax1.plot(*helix, lw=1.4)
ax1.set_box_aspect((1, 1, 1.6))
ax1.set_title("uniform B along +z: helix of constant pitch", fontsize=9)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

ax2 = fig.add_subplot(1, 2, 2, projection="3d")
ax2.plot(mirror[0], mirror[1], mirror[2], lw=0.8, color="C1")
zs = np.linspace(-1.3 * z_turn, 1.3 * z_turn, 200)
for phi in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    # field lines of the paraxial bottle: r * sqrt(B_z) = const
    r_line = 1.4 / np.sqrt(1 + (zs / L) ** 2)
    ax2.plot(r_line * np.cos(phi), r_line * np.sin(phi), zs, color="0.6", lw=0.6)
ax2.set_box_aspect((1, 1, 2))
ax2.set_title("magnetic bottle (field lines in gray): reflection where B is strong", fontsize=9)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")
fig.tight_layout()
