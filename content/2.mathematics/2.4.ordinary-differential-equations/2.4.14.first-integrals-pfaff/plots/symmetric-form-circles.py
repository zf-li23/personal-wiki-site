"""Integral curves of dx/(y - z) = dy/(z - x) = dz/(x - y): circles around the axis x = y = z."""

import numpy as np
import matplotlib.pyplot as plt

axis = np.array([1.0, 1.0, 1.0]) / np.sqrt(3)
e1 = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)
e2 = np.cross(axis, e1)
t = np.linspace(0, 2 * np.pi, 300)

fig = plt.figure(figsize=(6.5, 6))
ax = fig.add_subplot(projection="3d")

# reference sphere x^2 + y^2 + z^2 = 4
u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 20))
ax.plot_wireframe(2 * np.cos(u) * np.sin(v), 2 * np.sin(u) * np.sin(v), 2 * np.cos(v),
                  color="0.75", linewidth=0.4)

for i, h in enumerate(np.linspace(-1.6, 1.6, 7)):
    rho = np.sqrt(4 - h**2)  # circle on the sphere of radius 2, plane at signed distance h
    c = h * axis
    pts = c[:, None] + rho * (np.outer(e1, np.cos(t)) + np.outer(e2, np.sin(t)))
    ax.plot(pts[0], pts[1], pts[2], color=f"C{i % 10}", lw=1.8)

s = np.linspace(-2.5, 2.5, 2)
ax.plot(s * axis[0], s * axis[1], s * axis[2], color="0.3", lw=1.2, ls="--", label="axis x = y = z")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_box_aspect((1, 1, 1))
ax.set_title("x + y + z = C1 intersected with x^2 + y^2 + z^2 = C2")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
