"""Phase portrait of the pendulum x' = y, y' = -sin x as level curves of H = y^2/2 - cos x."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 600)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
H = 0.5 * Y**2 - np.cos(X)

fig, ax = plt.subplots(figsize=(9, 4.5))
levels = [-0.9, -0.6, -0.2, 0.3, 0.7, 1.5, 2.2, 3.0]
cs = ax.contour(X, Y, H, levels=levels, colors="C0", linewidths=1.2)
ax.contour(X, Y, H, levels=[1.0], colors="C3", linewidths=2)
# direction arrows from the vector field
xs, ys = np.meshgrid(np.linspace(-6, 6, 17), np.linspace(-2.6, 2.6, 9))
ax.quiver(xs, ys, ys, -np.sin(xs), color="0.55", angles="xy", width=0.0025)
ax.plot([-2 * np.pi, 0, 2 * np.pi], [0, 0, 0], "o", color="C2", label="centres (H = -1)")
ax.plot([-np.pi, np.pi], [0, 0], "s", color="C3", label="saddles, separatrix H = 1")
ax.set_xlabel("x = theta")
ax.set_ylabel("y = theta'")
ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.set_ylim(-3, 3)
ax.set_title("Orbits lie on level curves of the first integral H = y^2/2 - cos x")
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
