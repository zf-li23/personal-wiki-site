"""Type regions and characteristic curves of the Tricomi equation y u_xx + u_yy = 0."""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.5, 5))
ax.axhspan(0, 1.2, color="C0", alpha=0.12, lw=0)
ax.axhspan(-1.2, 0, color="C3", alpha=0.08, lw=0)
ax.axhline(0, color="0.3", lw=1.2)

y = np.linspace(-1.2, 0, 300)
s = (2 / 3) * (-y) ** 1.5
for c in np.arange(-3.0, 3.01, 0.4):
    ax.plot(c - s, y, color="C3", lw=1.1)
    ax.plot(c + s, y, color="C2", lw=1.1)

ax.text(0, 0.6, "elliptic (y > 0): no real characteristics", ha="center", va="center", fontsize=11)
ax.text(-2.4, -0.15, "hyperbolic (y < 0)", ha="left", va="top", fontsize=11)
ax.text(2.45, 0.06, "parabolic line y = 0", ha="right", va="bottom", fontsize=9)
ax.plot([], [], color="C2", label="x - (2/3)(-y)^(3/2) = const")
ax.plot([], [], color="C3", label="x + (2/3)(-y)^(3/2) = const")
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Tricomi equation y u_xx + u_yy = 0")
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
