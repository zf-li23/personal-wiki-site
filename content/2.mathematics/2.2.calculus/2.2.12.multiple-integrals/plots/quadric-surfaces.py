import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 9))
u = np.linspace(0, 2 * np.pi, 60)


def setup(ax, title):
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.view_init(elev=22, azim=-60)


# Ellipsoid x^2/4 + y^2 + z^2/2.25 = 1
ax = fig.add_subplot(2, 3, 1, projection="3d")
v = np.linspace(0, np.pi, 40)
U, V = np.meshgrid(u, v)
ax.plot_surface(2 * np.sin(V) * np.cos(U), np.sin(V) * np.sin(U), 1.5 * np.cos(V), cmap="viridis", alpha=0.85, linewidth=0)
ax.set_box_aspect((2, 1, 1.5))
setup(ax, "Ellipsoid  x^2/a^2 + y^2/b^2 + z^2/c^2 = 1")

# Elliptic paraboloid z = x^2/4 + y^2
ax = fig.add_subplot(2, 3, 2, projection="3d")
r = np.linspace(0, 1, 30)
U, Rr = np.meshgrid(u, r)
ax.plot_surface(2 * Rr * np.cos(U), Rr * np.sin(U), Rr**2, cmap="viridis", alpha=0.85, linewidth=0)
setup(ax, "Elliptic paraboloid  z = x^2/a^2 + y^2/b^2")

# Hyperbolic paraboloid z = x^2 - y^2
ax = fig.add_subplot(2, 3, 3, projection="3d")
g = np.linspace(-1, 1, 40)
X, Y = np.meshgrid(g, g)
ax.plot_surface(X, Y, X**2 - Y**2, cmap="viridis", alpha=0.85, linewidth=0)
setup(ax, "Hyperbolic paraboloid  z = x^2/a^2 - y^2/b^2")

# Hyperboloid of one sheet x^2 + y^2 - z^2 = 1
ax = fig.add_subplot(2, 3, 4, projection="3d")
w = np.linspace(-1.3, 1.3, 40)
U, W = np.meshgrid(u, w)
ax.plot_surface(np.cosh(W) * np.cos(U), np.cosh(W) * np.sin(U), np.sinh(W), cmap="viridis", alpha=0.85, linewidth=0)
setup(ax, "One sheet  x^2/a^2 + y^2/b^2 - z^2/c^2 = 1")

# Hyperboloid of two sheets x^2 + y^2 - z^2 = -1
ax = fig.add_subplot(2, 3, 5, projection="3d")
w = np.linspace(0, 1.4, 30)
U, W = np.meshgrid(u, w)
for sgn in (1, -1):
    ax.plot_surface(np.sinh(W) * np.cos(U), np.sinh(W) * np.sin(U), sgn * np.cosh(W), cmap="viridis", alpha=0.85, linewidth=0)
setup(ax, "Two sheets  x^2/a^2 + y^2/b^2 - z^2/c^2 = -1")

# Cone x^2 + y^2 = z^2
ax = fig.add_subplot(2, 3, 6, projection="3d")
w = np.linspace(-1.5, 1.5, 40)
U, W = np.meshgrid(u, w)
ax.plot_surface(W * np.cos(U), W * np.sin(U), W, cmap="viridis", alpha=0.85, linewidth=0)
setup(ax, "Cone  x^2/a^2 + y^2/b^2 = z^2/c^2")
fig.tight_layout()
