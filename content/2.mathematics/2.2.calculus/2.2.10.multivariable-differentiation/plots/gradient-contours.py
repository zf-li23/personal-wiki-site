import numpy as np
import matplotlib.pyplot as plt

# f(x, y) = x exp(-x^2 - y^2): level curves and the gradient field
g = np.linspace(-2, 2, 401)
X, Y = np.meshgrid(g, g)
F = X * np.exp(-X**2 - Y**2)

fig, ax = plt.subplots(figsize=(7, 6))
cs = ax.contour(X, Y, F, levels=np.linspace(-0.4, 0.4, 17), cmap="coolwarm", linewidths=1.2)
ax.clabel(cs, fmt="%.2f", fontsize=7)

q = np.linspace(-1.8, 1.8, 15)
QX, QY = np.meshgrid(q, q)
E = np.exp(-QX**2 - QY**2)
U = (1 - 2 * QX**2) * E
V = -2 * QX * QY * E
ax.quiver(QX, QY, U, V, color="tab:green", angles="xy", scale_units="xy", scale=1.6, width=0.004)

ax.plot([1 / np.sqrt(2)], [0], "^", color="tab:red", ms=9, label="maximum (1/sqrt 2, 0)")
ax.plot([-1 / np.sqrt(2)], [0], "v", color="tab:blue", ms=9, label="minimum (-1/sqrt 2, 0)")
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Level curves of x exp(-x^2 - y^2) and gradient vectors")
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()
