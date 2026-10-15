import numpy as np
import matplotlib.pyplot as plt

# f(x, y) = x y / (x^2 + y^2) = sin(2 theta) / 2 depends only on the direction
r = np.linspace(0.02, 1.0, 40)
t = np.linspace(0, 2 * np.pi, 121)
R, T = np.meshgrid(r, t)
X, Y = R * np.cos(T), R * np.sin(T)
Z = 0.5 * np.sin(2 * T)

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
ax1.plot_surface(X, Y, Z, cmap="coolwarm", linewidth=0, antialiased=True, alpha=0.75, rstride=2, cstride=2)
for k, color in [(0.0, "tab:green"), (1.0, "tab:red"), (-1.0, "tab:blue")]:
    s = np.linspace(0.02, 1, 50) / np.sqrt(1 + k**2)
    z = np.full_like(s, k / (1 + k**2))
    ax1.plot(s, k * s, z + 0.02, color=color, lw=3, label=f"along y = {k:g} x: f = {k / (1 + k**2):g}")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
ax1.set_zlim(-0.6, 0.6)
ax1.view_init(elev=40, azim=-35)
ax1.set_title("z = xy / (x^2 + y^2)")
ax1.legend(loc="upper left", fontsize=8)

ax2 = fig.add_subplot(1, 2, 2)
g = np.linspace(-1, 1, 401)
GX, GY = np.meshgrid(g, g)
with np.errstate(invalid="ignore", divide="ignore"):
    GZ = GX * GY / (GX**2 + GY**2)
cs = ax2.contourf(GX, GY, GZ, levels=np.linspace(-0.5, 0.5, 11), cmap="coolwarm")
ax2.contour(GX, GY, GZ, levels=np.linspace(-0.4, 0.4, 9), colors="k", linewidths=0.5)
fig.colorbar(cs, ax=ax2, shrink=0.85, label="f(x, y)")
ax2.plot(0, 0, "o", color="gold", ms=7, mec="k")
ax2.set_aspect("equal")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("Level curves are rays through the origin")
fig.tight_layout()
