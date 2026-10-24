"""Origin of the primary kinetic isotope effect. Along the reaction coordinate the reactant well
holds the C-H (or C-D) stretch with its zero-point energy, (1/2)hc*nu: about 17.3 kJ/mol for C-H at
2900 cm^-1 and 12.7 kJ/mol for C-D at 2130 cm^-1. At the transition state that stretch has become
the reaction coordinate, so (to a first approximation) the two isotopologues reach the same top:
the C-D compound needs about 4.6 kJ/mol more activation energy, k_H/k_D about 6.4 at 298 K."""

import matplotlib.pyplot as plt
import numpy as np

zh, zd = 17.3, 12.7  # zero-point energies / (kJ/mol)
top = 75.0  # transition state above the well bottom



def energy(x):
    """Reactant well (harmonic wall on the left), rise to the transition state at x = 2, product below."""
    rise = top * (1 - np.cos(np.pi * x / 2)) / 2
    fall = top - (top + 15) * (1 - np.cos(np.pi * (x - 2) / 2)) / 2
    return np.where(x < 0, 140 * x**2, np.where(x <= 2, rise, fall))


x = np.linspace(-0.75, 4.0, 500)
profile = energy(x)

fig, ax = plt.subplots(figsize=(6.4, 4.0))
ax.plot(x, profile, lw=1.8, color="black")
for z, name, c in ((zh, "C–H", "C0"), (zd, "C–D", "C1")):
    left, right = -np.sqrt(z / 140), (2 / np.pi) * np.arccos(1 - 2 * z / top)
    ax.plot([left, right], [z, z], color=c, lw=2)
    ax.text(left - 0.08, z, f"ZPE {name}: {z}", ha="right", va="center", color=c, fontsize=9)
ax.annotate("", xy=(1.45, top), xytext=(1.45, zh), arrowprops=dict(arrowstyle="<->", color="C0"))
ax.text(1.38, 45, r"$E_{\mathrm{a}}$(H)", ha="right", color="C0", fontsize=10)
ax.annotate("", xy=(2.55, top), xytext=(2.55, zd), arrowprops=dict(arrowstyle="<->", color="C1"))
ax.text(2.63, 45, r"$E_{\mathrm{a}}$(D) = $E_{\mathrm{a}}$(H) + 4.6", color="C1", fontsize=10)
ax.plot([0.6, 2.55], [zd, zd], color="C1", lw=0.8, ls="--")
ax.plot([0.7, 1.45], [zh, zh], color="C0", lw=0.8, ls="--")
ax.plot([1.45, 2.55], [top, top], color="gray", lw=0.8, ls=":")
ax.text(2.0, top + 4, "transition state: the C–H stretch has become the reaction coordinate", ha="center", fontsize=9)
ax.set_xlim(-2.1, 4.1)
ax.set_ylim(-18, 88)
ax.set_xlabel("reaction coordinate")
ax.set_ylabel(r"$E$ / (kJ mol$^{-1}$)")
ax.set_xticks([])
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
