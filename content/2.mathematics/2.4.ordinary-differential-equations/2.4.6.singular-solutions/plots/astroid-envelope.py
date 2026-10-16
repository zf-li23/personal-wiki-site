"""Segments of length a with ends on the two axes; their envelope is the astroid."""

import numpy as np
import matplotlib.pyplot as plt

a = 1.0
fig, ax = plt.subplots(figsize=(5.6, 5.6))
for th in np.linspace(0, 2 * np.pi, 49, endpoint=False):
    ax.plot([a * np.cos(th), 0], [0, a * np.sin(th)], color="C0", lw=0.8, alpha=0.7)
t = np.linspace(0, 2 * np.pi, 600)
ax.plot(a * np.cos(t) ** 3, a * np.sin(t) ** 3, color="C3", lw=2.4,
        label="astroid x^(2/3) + y^(2/3) = a^(2/3)")
ax.plot([], [], color="C0", lw=0.8, label="segments of length a")
ax.set_aspect("equal")
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.15, 1.15)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("The astroid as an envelope (a = 1)")
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
