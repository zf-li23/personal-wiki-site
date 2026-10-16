"""Green's function of -y'' = f, y(0) = y(1) = 0: G(x, t) = min(x, t) (1 - max(x, t))."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 501)
fig, ax = plt.subplots(figsize=(7.5, 4.2))
for i, t in enumerate([0.2, 0.4, 0.6, 0.85]):
    G = np.minimum(x, t) * (1 - np.maximum(x, t))
    ax.plot(x, G, color=f"C{i}", lw=1.8, label=f"t = {t}")
    ax.plot([t], [t * (1 - t)], "o", color=f"C{i}", ms=5)
ax.plot(x, x * (1 - x) / 2, color="0.4", lw=1.4, ls="--", label="y = x(1 - x)/2  (f = 1)")
ax.set_xlabel("x")
ax.set_ylabel("G(x, t)")
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.3)
ax.set_title("Green's function: response to a unit point load at t")
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
