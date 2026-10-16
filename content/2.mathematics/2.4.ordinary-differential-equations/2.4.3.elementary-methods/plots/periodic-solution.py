"""Solutions of y' + y = sin x approach the unique periodic solution (sin x - cos x)/2."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5, 12, 800)
ystar = (np.sin(x) - np.cos(x)) / 2

fig, ax = plt.subplots(figsize=(8, 4.5))
for y0 in np.linspace(-3, 3, 9):
    C = y0 + 0.5  # y(0) = -1/2 + C
    ax.plot(x, ystar + C * np.exp(-x), color="0.6", lw=1.0)
ax.plot(x, ystar, color="C0", lw=2.4, label="periodic solution y* = (sin x - cos x)/2")
ax.plot(x, np.sin(x), color="C3", lw=1.0, ls="--", label="forcing q(x) = sin x")
ax.set_xlim(-1.5, 12)
ax.set_ylim(-3.5, 3.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y' + y = sin x: all solutions y* + C e^(-x) converge to y*")
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
