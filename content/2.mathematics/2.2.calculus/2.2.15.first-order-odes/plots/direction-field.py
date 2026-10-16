"""Direction field of y' = x - y with integral curves y = x - 1 + C exp(-x)."""

import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-2, 4, 25)
ys = np.linspace(-3, 4, 25)
X, Y = np.meshgrid(xs, ys)
S = X - Y
# unit segments of slope S
L = np.sqrt(1 + S**2)
U, V = 1 / L, S / L

fig, ax = plt.subplots(figsize=(7, 5.5))
ax.quiver(X, Y, U, V, angles="xy", headwidth=0, headlength=0, headaxislength=0,
          pivot="middle", scale=38, width=0.003, color="0.55")
x = np.linspace(-2, 4, 400)
for C in [-6, -3, -1.5, -0.5, 0.5, 1.5, 3, 6]:
    ax.plot(x, x - 1 + C * np.exp(-x), color="C0", lw=1.4)
ax.plot(x, x - 1, color="C3", lw=2.2, label="C = 0:  y = x - 1")
ax.set_xlim(-2, 4)
ax.set_ylim(-3, 4)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Direction field of y' = x - y and integral curves y = x - 1 + C e^(-x)")
ax.legend(loc="upper left")
fig.tight_layout()
