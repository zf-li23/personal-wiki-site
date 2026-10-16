"""Non-uniqueness for y' = 3 y^(2/3), y(0) = 0: y = 0 and y = (x - c)^3 for x >= c."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5, 3, 600)
fig, ax = plt.subplots(figsize=(7, 4.8))
for c, col in zip([0.0, 0.5, 1.0, 1.5, 2.0], ["C0", "C1", "C2", "C4", "C5"]):
    y = np.where(x < c, 0.0, (x - c) ** 3)
    ax.plot(x, y, color=col, lw=1.8, label=f"c = {c:g}")
ax.axhline(0, color="C3", lw=2.6, alpha=0.6, label="y = 0")
ax.plot([0], [0], "o", color="k", ms=6)
ax.annotate("initial point (0, 0)", xy=(0, 0), xytext=(-1.4, 1.6),
            arrowprops=dict(arrowstyle="->", color="0.4"))
ax.set_xlim(-1.5, 3)
ax.set_ylim(-0.4, 4)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y' = 3 y^(2/3), y(0) = 0: infinitely many solutions")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
