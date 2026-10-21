"""Images of two incoherent point sources of equal intensity (Airy patterns) at three separations."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j1

def airy(u):
    u = np.asarray(u, dtype=float)
    out = np.ones_like(u)
    nz = np.abs(u) > 1e-9
    out[nz] = (2 * j1(u[nz]) / u[nz]) ** 2
    return out

u0 = 3.8317                    # first zero of J1: theta_min = 1.22 lambda / D
u = np.linspace(-12, 12, 4001)
cases = [(1.6, "separation 1.6 θmin: resolved"), (1.0, "separation θmin: just resolved"),
         (0.6, "separation 0.6 θmin: not resolved")]

fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.2), sharey=True)
for ax, (f, title) in zip(axes, cases):
    s = f * u0
    I1, I2 = airy(u + s / 2), airy(u - s / 2)
    ax.plot(u / u0, I1, color="C0", lw=0.9, ls="--")
    ax.plot(u / u0, I2, color="C2", lw=0.9, ls="--")
    ax.plot(u / u0, I1 + I2, color="C1", lw=1.6)
    if f == 1.0:
        mid = 2 * airy(np.array([s / 2]))[0]
        ax.axhline(mid, color="0.6", lw=0.7, ls=":")
        ax.text(1.4, mid + 0.03, f"dip {mid:.3f}", fontsize=7.5, color="0.4")
    ax.set_title(title, fontsize=8.5)
    ax.set_xlabel("θ / θmin")
    ax.set_xlim(-3, 3)
    ax.grid(alpha=0.25)
axes[0].set_ylabel("intensity (peak of one source = 1)")
fig.tight_layout()
