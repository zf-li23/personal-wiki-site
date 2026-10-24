"""Schematic free-energy profile for the deprotonation of 2-methylcyclohexanone by a base on the two
sides. Removing the less hindered C6-H has the lower barrier (kinetic enolate, less substituted
C=C); the more substituted C1=C2 enolate is lower in energy (thermodynamic enolate). With LDA both deprotonations are strongly downhill. Energies are
illustrative, not measured values."""

import matplotlib.pyplot as plt
import numpy as np


def path(x0, x1, y0, ymax, y1, n=200):
    """A smooth one-barrier profile from (x0, y0) over a maximum ymax to (x1, y1)."""
    t = np.linspace(0, 1, n)
    xs = x0 + (x1 - x0) * t
    base = y0 + (y1 - y0) * (3 * t**2 - 2 * t**3)
    bump = (ymax - (y0 + y1) / 2) * np.sin(np.pi * t) ** 2
    return xs, base + bump


fig, ax = plt.subplots(figsize=(7.2, 4.4))
# left: kinetic side (lower barrier, higher product); right: thermodynamic side
xk, yk = path(0, -3, 0, 40, -25)
xt, yt = path(0, 3, 0, 52, -36)
ax.plot(xk, yk, color="C0", lw=2.2, label="C6-H removed: kinetic enolate")
ax.plot(xt, yt, color="C3", lw=2.2, label="C2-H removed: thermodynamic enolate")
ax.hlines(0, -0.4, 0.4, color="black", lw=2.2)
ax.annotate("ketone + base", (0, -3), ha="center", va="top", fontsize=11)
ax.annotate("less substituted\nenolate", (-3, -28), ha="center", va="top", fontsize=11)
ax.annotate("more substituted\nenolate", (3, -39), ha="center", va="top", fontsize=11)
ax.annotate("", xy=(-1.5, 40), xytext=(-1.5, 0), arrowprops=dict(arrowstyle="<->", color="C0"))
ax.text(-1.4, 20, r"$\Delta G^\ddagger$ smaller", color="C0", fontsize=10)
ax.annotate("", xy=(1.5, 52), xytext=(1.5, 0), arrowprops=dict(arrowstyle="<->", color="C3"))
ax.text(1.6, 26, r"$\Delta G^\ddagger$ larger", color="C3", fontsize=10)
ax.annotate("", xy=(3.6, -36), xytext=(3.6, -25), arrowprops=dict(arrowstyle="<->", color="gray"))
ax.hlines(-25, -3, 3.7, color="gray", lw=0.8, ls=":")
ax.text(3.7, -30.5, r"$\Delta G^\circ$", color="gray", fontsize=10, va="center")
ax.set_xlim(-4.2, 4.6)
ax.set_ylim(-52, 78)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel("reaction coordinate")
ax.set_ylabel("Gibbs energy (schematic)")
ax.legend(loc="upper center", fontsize=9, frameon=False, ncol=1)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
