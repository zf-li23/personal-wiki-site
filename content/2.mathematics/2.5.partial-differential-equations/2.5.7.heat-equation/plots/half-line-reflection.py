"""Method of reflection: u_t = u_xx on x > 0 with u(0, t) = 0 and u(x, 0) = 1, via the odd extension."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

x = np.linspace(-3, 3, 1201)
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.plot(x, np.sign(x), color="0.5", lw=1.4, ls="--", label="odd extension of the initial data")
for i, t in enumerate([0.01, 0.1, 0.5, 2.0]):
    u = erf(x / np.sqrt(4 * t))
    ax.plot(x[x >= 0], u[x >= 0], color=f"C{i}", lw=2.0, label=f"t = {t}")
    ax.plot(x[x <= 0], u[x <= 0], color=f"C{i}", lw=1.0, alpha=0.5)
ax.axvline(0, color="0.3", lw=1)
ax.axhline(0, color="0.6", lw=0.8)
ax.set_xlim(-3, 3)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("x")
ax.set_title("u = erf(x / (2 sqrt(t))): the whole-line solution is odd, so u(0, t) = 0")
ax.legend(fontsize=8, loc="lower right")
fig.tight_layout()
