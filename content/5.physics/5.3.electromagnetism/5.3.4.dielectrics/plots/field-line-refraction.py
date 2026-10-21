"""Refraction of E and D lines at a charge-free interface between two dielectrics:
tan(theta1) / tan(theta2) = eps1 / eps2, with theta measured from the normal."""

import numpy as np
import matplotlib.pyplot as plt

eps1, eps2 = 4.0, 1.0  # medium 1 above (y > 0), medium 2 below
theta2 = np.deg2rad(30.0)
theta1 = np.arctan(np.tan(theta2) * eps1 / eps2)

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.axhspan(0, 1.6, color="C0", alpha=0.10, lw=0)
ax.axhline(0, color="0.3", lw=1)
for x0 in np.linspace(-2.4, 0.4, 5):
    # line comes up through medium 2 and continues into medium 1
    y2 = np.array([-1.6, 0.0])
    x2 = x0 + (y2 - 0.0) * np.tan(theta2)
    y1 = np.array([0.0, 1.6])
    x1 = x0 + y1 * np.tan(theta1)
    ax.plot(x2, y2, color="C1", lw=1.6)
    ax.plot(x1, y1, color="C1", lw=1.6)
    ax.annotate("", xy=(x1[0] + 0.55 * np.sin(theta1), 0.55 * np.cos(theta1)), xytext=(x1[0], 0),
                arrowprops=dict(arrowstyle="->", color="C1", lw=1.6))
ax.plot([0.4, 0.4], [-1.6, 1.6], color="0.5", ls=":", lw=1)
ax.text(0.45, 1.25, r"$\theta_1$", fontsize=11)
ax.text(0.2, -0.9, r"$\theta_2$", fontsize=11)
ax.text(1.4, 1.2, rf"medium 1, $\varepsilon_1 = {eps1:g}\,\varepsilon_0$", fontsize=10)
ax.text(1.4, -1.3, rf"medium 2, $\varepsilon_2 = {eps2:g}\,\varepsilon_0$", fontsize=10)
ax.set_title(r"$\tan\theta_1 / \tan\theta_2 = \varepsilon_1/\varepsilon_2$" + rf"  ($\theta_2 = 30^\circ$, $\theta_1 \approx {np.rad2deg(theta1):.0f}^\circ$)", fontsize=10)
ax.set_xlim(-2.6, 4.2)
ax.set_ylim(-1.6, 1.6)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
