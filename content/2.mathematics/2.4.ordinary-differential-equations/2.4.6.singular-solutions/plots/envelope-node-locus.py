"""Integral curves (x - C)^2 = y (y - 3)^2: envelope y = 0 and node locus y = 3."""

import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(0, 4.6, 600)
branch = (y - 3) * np.sqrt(y)
fig, ax = plt.subplots(figsize=(7, 4.8))
for i, C in enumerate(np.arange(-6, 7, 2.0)):
    ax.plot(C + branch, y, color="C0", lw=1.2)
    ax.plot(C - branch, y, color="C0", lw=1.2)
ax.axhline(0, color="C3", lw=2.6, label="envelope y = 0 (singular solution)")
ax.axhline(3, color="C1", lw=1.8, ls="--", label="node locus y = 3 (not a solution)")
ax.plot([], [], color="C0", lw=1.2, label="integral curves")
ax.set_xlim(-6, 6)
ax.set_ylim(-0.5, 5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("(y - 1)^2 (y')^2 = 4y/9: C-discriminant curves")
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
