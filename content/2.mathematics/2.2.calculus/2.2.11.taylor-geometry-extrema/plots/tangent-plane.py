import numpy as np
import matplotlib.pyplot as plt

# Paraboloid z = 1 - x^2 - y^2 and its tangent plane / normal line at (0.4, -0.5, 0.59)
x0, y0 = 0.4, -0.5
z0 = 1 - x0**2 - y0**2
fx, fy = -2 * x0, -2 * y0

g = np.linspace(-1.2, 1.2, 61)
X, Y = np.meshgrid(g, g)
Z = 1 - X**2 - Y**2

fig = plt.figure(figsize=(8, 6.5))
ax = fig.add_subplot(1, 1, 1, projection="3d", computed_zorder=False)
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.75, linewidth=0, antialiased=True)

p = np.linspace(-0.45, 0.45, 10)
PX, PY = np.meshgrid(x0 + p, y0 + p)
PZ = z0 + fx * (PX - x0) + fy * (PY - y0)
ax.plot_surface(PX, PY, PZ, color="tab:orange", alpha=0.45, linewidth=0)

n = np.array([fx, fy, -1.0])
n = -n / np.linalg.norm(n)
s = np.linspace(-0.3, 0.9, 2)
ax.plot(x0 + s * n[0], y0 + s * n[1], z0 + s * n[2], color="tab:red", lw=2.5, zorder=10, label="normal line, n = (f_x, f_y, -1)")
ax.scatter([x0], [y0], [z0], color="tab:red", s=40, depthshade=False, zorder=11)
ax.plot([], [], color="tab:orange", lw=6, alpha=0.6, label="tangent plane")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_zlim(-1.5, 1.5)
ax.view_init(elev=15, azim=40)
ax.set_title("z = 1 - x^2 - y^2 at (0.4, -0.5, 0.59)")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
