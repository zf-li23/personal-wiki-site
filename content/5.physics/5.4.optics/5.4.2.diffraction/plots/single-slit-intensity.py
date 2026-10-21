"""Single-slit Fraunhofer diffraction: I/I0 = (sin a / a)^2 with a = pi a sin(theta) / lambda."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

s = np.linspace(-4.0, 4.0, 4001)          # a sin(theta) / lambda
alpha = np.pi * s
I = np.sinc(s) ** 2                        # numpy sinc(x) = sin(pi x)/(pi x)

# secondary maxima: tan(alpha) = alpha
roots = [brentq(lambda x: np.tan(x) - x, (k + 0.5) * np.pi - 0.9, (k + 0.5) * np.pi - 1e-6)
         for k in range(1, 4)]

fig, ax = plt.subplots(figsize=(8.0, 3.8))
ax.plot(s, I, color="C0", lw=1.6, label="I / I0")
ax.plot(s, 10 * I, color="C1", lw=1.0, ls="--", label="10 × I / I0")
for r in roots:
    x = r / np.pi
    val = np.sinc(x) ** 2
    for sign in (-1, 1):
        ax.plot(sign * x, 10 * val, "o", color="C1", ms=4)
    ax.annotate(f"{x:.3f}\n{val:.4f}", (x, 10 * val), xytext=(0, 8),
                textcoords="offset points", ha="center", fontsize=7.5, color="C1")
ax.set_xlabel("a sin θ / λ")
ax.set_ylabel("relative intensity")
ax.set_xticks(np.arange(-4, 5, 1))
ax.set_xlim(-4, 4)
ax.set_ylim(0, 1.15)
ax.legend(loc="upper left", fontsize=8, frameon=False)
ax.grid(alpha=0.25)
fig.tight_layout()
