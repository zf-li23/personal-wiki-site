"""Orbit change by a small radial velocity kick on a circular orbit (G M = 1, r0 = 1)."""

import numpy as np
import matplotlib.pyplot as plt

alpha = 0.3
r0, v0 = 1.0, 1.0
L = r0 * v0  # unchanged by a radial kick
p = L**2
# after the kick: E = (v0^2 (1 + alpha^2))/2 - 1/r0, eccentricity from E and L
E = 0.5 * v0**2 * (1 + alpha**2) - 1 / r0
e = np.sqrt(1 + 2 * E * L**2)

th = np.linspace(0, 2 * np.pi, 1000)
fig, ax = plt.subplots(figsize=(6.2, 6))
ax.plot(r0 * np.cos(th), r0 * np.sin(th), color="0.4", lw=1.5, label="circular orbit")

# kick point at theta = 90 deg (top). r(theta) = p / (1 + e cos(theta - w))
# r = r0 at the kick point gives cos(theta_k - w) = 0; the sign of the radial velocity fixes w.
thk = np.pi / 2
for sign, ls, lab in [(-1, "--", "inward kick"), (1, ":", "outward kick")]:
    # radial velocity dr/dt is proportional to e sin(theta - w); positive for outward kick
    w = thk - sign * np.pi / 2
    r = p / (1 + e * np.cos(th - w))
    ax.plot(r * np.cos(th), r * np.sin(th), ls=ls, lw=2, label=lab)
ax.plot([0], [0], "*", color="k", ms=12)
ax.plot([0], [r0], "o", color="C3", ms=7, label="kick point")
ax.annotate("", (0, r0 - 0.25), (0, r0), arrowprops=dict(arrowstyle="->", color="C0"))
ax.annotate("", (0, r0 + 0.25), (0, r0), arrowprops=dict(arrowstyle="->", color="C1"))
ax.annotate("", (-0.35, r0), (0, r0), arrowprops=dict(arrowstyle="->", color="0.3"))
ax.text(-0.45, r0 + 0.06, "v0", color="0.3")
ax.set_aspect("equal")
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)
ax.set_title("Radial kick: same L, larger E")
ax.legend(fontsize=8, loc="lower right")
fig.tight_layout()
