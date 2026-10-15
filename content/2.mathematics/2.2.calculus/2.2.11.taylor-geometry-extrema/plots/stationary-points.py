import numpy as np
import matplotlib.pyplot as plt

# z = x^3 + y^3 - 3xy: minimum at (1, 1), saddle at (0, 0)
g = np.linspace(-1.2, 1.8, 241)
X, Y = np.meshgrid(g, g)
Z = X**3 + Y**3 - 3 * X * Y

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
Zc = np.where((Z > -1.5) & (Z < 3), Z, np.nan)
ax1.plot_surface(X, Y, Zc, cmap="viridis", linewidth=0, antialiased=True, alpha=0.6, rstride=4, cstride=4)
ax1.scatter([1], [1], [-1], color="tab:red", s=40, depthshade=False, label="minimum (1, 1, -1)")
ax1.scatter([0], [0], [0], color="tab:orange", s=40, depthshade=False, label="saddle (0, 0, 0)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
ax1.set_zlim(-1.5, 3)
ax1.view_init(elev=30, azim=-120)
ax1.set_title("z = x^3 + y^3 - 3xy")
ax1.legend(loc="upper left", fontsize=8)

ax2 = fig.add_subplot(1, 2, 2)
levels = np.concatenate([np.linspace(-0.9, -0.1, 5), [0.0], np.linspace(0.3, 3, 7)])
cs = ax2.contour(X, Y, Z, levels=levels, cmap="viridis", linewidths=1.1)
ax2.clabel(cs, fmt="%.1f", fontsize=7)
ax2.plot(1, 1, "o", color="tab:red", ms=8, label="minimum")
ax2.plot(0, 0, "X", color="tab:orange", ms=9, label="saddle point")
ax2.set_aspect("equal")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("Level curves: closed loops around the minimum, a cross at the saddle")
ax2.legend(loc="upper right", fontsize=8)
fig.tight_layout()
