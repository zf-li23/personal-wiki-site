"""Descent times from A = (0, 0) to B = (pi, 2) (y downward, g = 1): cycloid, line, circular arc."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

g = 1.0
xB, yB = np.pi, 2.0

# cycloid with R = 1, theta in [0, pi]
th = np.linspace(0, np.pi, 400)
cx, cy = th - np.sin(th), 1 - np.cos(th)
T_cyc = np.pi * np.sqrt(1.0 / g)

# straight line
L = np.hypot(xB, yB)
T_line = np.sqrt(2 * L / (g * yB / L))

# circular arc through A and B with vertical tangent at A: centre (r, 0)
r = (xB**2 + yB**2) / (2 * xB)
phi_B = np.arctan2(yB, xB - r)  # angle of B seen from the centre, measured from +x axis
phi = np.linspace(np.pi, phi_B, 400)
ax_, ay_ = r + r * np.cos(phi), r * np.sin(phi)
# time: ds = r dphi, y = r sin(phi), v = sqrt(2 g y)
T_arc = quad(lambda p: r / np.sqrt(2 * g * r * np.sin(p)), phi_B, np.pi)[0]

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(cx, cy, color="C0", lw=2, label=f"cycloid, T = {T_cyc:.3f}")
ax.plot([0, xB], [0, yB], color="C1", lw=1.8, label=f"straight line, T = {T_line:.3f}")
ax.plot(ax_, ay_, color="C2", lw=1.8, label=f"circular arc, T = {T_arc:.3f}")
ax.plot([0, xB], [0, yB], "o", color="0.3")
ax.annotate("A", (0, 0), textcoords="offset points", xytext=(-12, -4))
ax.annotate("B", (xB, yB), textcoords="offset points", xytext=(6, -2))
ax.invert_yaxis()
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y (downward)")
ax.set_title("Brachistochrone: times with g = 1")
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
