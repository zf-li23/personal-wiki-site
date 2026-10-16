"""Level curves of u = Re(1/z) and v = Im(1/z): two orthogonal families of circles."""

import numpy as np
import matplotlib.pyplot as plt

g = np.linspace(-2, 2, 801)
X, Y = np.meshgrid(g, g)
R2 = X**2 + Y**2
with np.errstate(divide="ignore", invalid="ignore"):
    U = X / R2
    V = -Y / R2

lv = np.array([-2, -1, -0.6, -0.35, -0.2, 0.2, 0.35, 0.6, 1, 2])
fig, ax = plt.subplots(figsize=(6.4, 6))
ax.contour(X, Y, U, levels=lv, colors="C0", linewidths=1.1, linestyles="solid")
ax.contour(X, Y, V, levels=lv, colors="C3", linewidths=1.1, linestyles="solid")
ax.plot([], [], color="C0", label="u = x / (x^2 + y^2) = const")
ax.plot([], [], color="C3", label="v = -y / (x^2 + y^2) = const")
ax.plot(0, 0, "o", color="C1", ms=6)
ax.set_aspect("equal")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc="upper right", fontsize=8)
ax.set_title("f(z) = 1/z: level curves of u and v meet at right angles")
fig.tight_layout()
