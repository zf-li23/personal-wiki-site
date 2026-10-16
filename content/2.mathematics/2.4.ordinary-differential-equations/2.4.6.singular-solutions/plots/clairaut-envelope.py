"""Clairaut equation y = x p - p^2/4: the lines y = C x - C^2/4 and their envelope y = x^2."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5, 2.5, 400)
fig, ax = plt.subplots(figsize=(7, 4.8))
for C in np.linspace(-4, 4, 17):
    ax.plot(x, C * x - C ** 2 / 4, color="C0", lw=0.9, alpha=0.7)
ax.plot(x, x ** 2, color="C3", lw=2.6, label="singular solution y = x^2")
ax.plot([], [], color="C0", lw=0.9, label="general solution y = C x - C^2/4")
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-3, 5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Clairaut equation: a family of lines and its envelope")
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
