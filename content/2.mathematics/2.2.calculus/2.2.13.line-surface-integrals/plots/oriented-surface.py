import numpy as np
import matplotlib.pyplot as plt

# Surface z = xy over |x|, |y| <= 1 with its upward unit normal field
g = np.linspace(-1, 1, 41)
X, Y = np.meshgrid(g, g)
Z = X * Y

fig = plt.figure(figsize=(8, 6.5))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.6, linewidth=0)

q = np.linspace(-0.9, 0.9, 6)
QX, QY = np.meshgrid(q, q)
QZ = QX * QY
N = np.stack([-QY, -QX, np.ones_like(QX)])
N = N / np.linalg.norm(N, axis=0)
ax.quiver(QX, QY, QZ, N[0], N[1], N[2], length=0.35, color="tab:red", linewidth=1.2, arrow_length_ratio=0.3)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("z = xy, upper side: n = (-y, -x, 1) / sqrt(1 + x^2 + y^2)")
ax.view_init(elev=24, azim=-55)
fig.tight_layout()
