"""Saturated solutions of y' = y^2: y = y0 / (1 - y0 x) blows up at x = 1/y0."""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4.8))
for i, y0 in enumerate([0.5, 1.0, 2.0, -0.5, -1.0, -2.0]):
    xb = 1.0 / y0
    if y0 > 0:
        x = np.linspace(-4, xb - 1e-3, 600)
    else:
        x = np.linspace(xb + 1e-3, 4, 600)
    y = y0 / (1 - y0 * x)
    ax.plot(x, y, lw=1.7, color=f"C{i}", label=f"y0 = {y0:g}")
    ax.axvline(xb, color=f"C{i}", lw=0.9, ls="--", alpha=0.7)
ax.axhline(0, color="0.3", lw=1.8, label="y0 = 0")
ax.set_xlim(-4, 4)
ax.set_ylim(-8, 8)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y' = y^2: maximal intervals depend on the initial value")
ax.legend(loc="upper left", fontsize=8, ncol=2)
fig.tight_layout()
