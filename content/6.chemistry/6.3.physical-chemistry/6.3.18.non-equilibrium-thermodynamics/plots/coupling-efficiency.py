"""Efficiency of a linear two-flux energy converter (Kedem-Caplan):
eta = -x (x + q) / (q x + 1) versus the reduced force ratio x, for several degrees of coupling q."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
ax = axes[0]
for q, c in zip([0.5, 0.8, 0.95, 0.99, 1.0], ["C0", "C1", "C2", "C3", "C4"]):
    x = np.linspace(-q, 0, 400)[1:]
    eta = -x * (x + q) / (q * x + 1)
    ax.plot(x, eta, color=c, lw=2, label=f"q = {q:g}")
ax.set_xlabel("reduced force ratio  x = (L22/L11)^(1/2) X2/X1")
ax.set_ylabel("efficiency  η = -J2 X2 / (J1 X1)")
ax.set_xlim(-1, 0)
ax.set_ylim(0, 1)
ax.legend(loc="upper right")
ax.set_title("output is produced only for -q < x < 0")

ax = axes[1]
q = np.linspace(0, 1, 400)
eta_max = q**2 / (1 + np.sqrt(1 - q**2)) ** 2
ax.plot(q, eta_max, color="C0", lw=2)
ax.set_xlabel("degree of coupling q")
ax.set_ylabel("maximum efficiency")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("η_max = q² / (1 + (1 - q²)^(1/2))²")
ax.grid(alpha=0.3)
fig.tight_layout()
