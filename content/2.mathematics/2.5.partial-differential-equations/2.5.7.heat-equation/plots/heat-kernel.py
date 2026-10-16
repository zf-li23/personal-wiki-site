"""Heat kernel at several times, and the smoothing of a rectangular initial temperature (k = 1)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

x = np.linspace(-3, 3, 1201)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
for i, t in enumerate([0.01, 0.05, 0.2, 1.0]):
    ax.plot(x, np.exp(-x**2 / (4 * t)) / np.sqrt(4 * np.pi * t), color=f"C{i}", lw=1.8, label=f"t = {t}")
ax.set_xlim(-3, 3)
ax.set_ylim(0, 3)
ax.set_xlabel("x")
ax.set_title("Heat kernel Phi(x, t): mass 1, width ~ sqrt(t)")
ax.legend(fontsize=9)

ax = axes[1]
ax.plot(x, (np.abs(x) < 1).astype(float), color="0.5", lw=1.4, ls="--", label="t = 0")
for i, t in enumerate([0.005, 0.05, 0.25, 1.0]):
    u = 0.5 * (erf((1 - x) / np.sqrt(4 * t)) + erf((1 + x) / np.sqrt(4 * t)))
    ax.plot(x, u, color=f"C{i}", lw=1.8, label=f"t = {t}")
ax.set_xlim(-3, 3)
ax.set_ylim(0, 1.1)
ax.set_xlabel("x")
ax.set_title("u_t = u_xx with u(x, 0) = 1 for |x| < 1")
ax.legend(fontsize=9)
fig.tight_layout()
