"""A harmonic function on the unit disk attains its extreme values on the boundary circle."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 1, 60)
t = np.linspace(0, 2 * np.pi, 181)
R, T = np.meshgrid(r, t)
X, Y = R * np.cos(T), R * np.sin(T)
U = X**3 - 3 * X * Y**2 + 0.5 * (X**2 - Y**2)  # Re(z^3 + z^2 / 2)

fig = plt.figure(figsize=(10, 4.4))
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.plot_surface(X, Y, U, cmap="coolwarm", rstride=2, cstride=2, linewidth=0, antialiased=True, alpha=0.9)
tb = np.linspace(0, 2 * np.pi, 400)
ub = np.cos(3 * tb) + 0.5 * np.cos(2 * tb)
ax.plot(np.cos(tb), np.sin(tb), ub, color="k", lw=2)
ax.view_init(elev=28, azim=-60)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("u = Re(z^3 + z^2 / 2) over the unit disk")

ax = fig.add_subplot(1, 2, 2)
cs = ax.contourf(X, Y, U, levels=21, cmap="coolwarm")
ax.contour(X, Y, U, levels=[0], colors="k", linewidths=0.8)
ax.plot(np.cos(tb), np.sin(tb), color="k", lw=1.5)
i = np.argmax(ub)
j = np.argmin(ub)
ax.plot(np.cos(tb[i]), np.sin(tb[i]), "^", color="k", ms=8)
ax.plot(np.cos(tb[j]), np.sin(tb[j]), "v", color="k", ms=8)
ax.plot(0, 0, "o", color="k", ms=5)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("max (^) and min (v) lie on the circle; u(0) = 0 is the mean")
fig.colorbar(cs, ax=ax, shrink=0.8)
fig.tight_layout()
