"""How the solvent changes the barriers of SN1 and SN2 reactions (schematic free-energy profiles).
SN1: charge develops in the transition state (R...X becoming R+ and X-); a polar protic solvent
stabilizes the ions and the polar transition state more than the neutral substrate, so the barrier
falls. SN2 with an anionic nucleophile: the charge is concentrated in the small reactant anion and
spread over the transition state; hydrogen bonding in a protic solvent stabilizes the reactants
more than the transition state, so the barrier rises compared with a polar aprotic solvent."""

import matplotlib.pyplot as plt
import numpy as np


def profile(levels, xs, n=400):
    """Smooth curve through stationary points (x, G) using cosine segments."""
    x_all, g_all = [], []
    for (x0, g0), (x1, g1) in zip(zip(xs, levels), zip(xs[1:], levels[1:])):
        t = np.linspace(0, 1, n)
        x_all.append(x0 + (x1 - x0) * t)
        g_all.append(g0 + (g1 - g0) * (1 - np.cos(np.pi * t)) / 2)
    return np.concatenate(x_all), np.concatenate(g_all)


fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6))

ax = axes[0]
xs = [0, 1, 2, 3, 4]
nonpolar = [0, 100, 80, 88, -10]
protic = [0, 70, 35, 45, -25]
for lv, style, name in ((nonpolar, "--", "less polar solvent"), (protic, "-", "polar protic solvent")):
    x, g = profile(lv, xs)
    ax.plot(x, g, style, lw=1.6, label=name)
ax.annotate(r"R$^+$ + X$^-$", (2, 35), (2, 12), ha="center", fontsize=9)
ax.text(0.05, -12, "RX", ha="left", fontsize=9)
ax.text(3.95, -38, "ROH", ha="right", fontsize=9)
ax.set_title("(a) SN1: ionization is helped", fontsize=10)

ax = axes[1]
xs = [0, 1, 2]
aprotic = [0, 60, -40]
protic = [-35, 75, -55]
for lv, style, name in ((aprotic, "--", "polar aprotic (DMF, DMSO)"), (protic, "-", "polar protic (MeOH, H$_2$O)")):
    x, g = profile(lv, xs)
    ax.plot(x, g, style, lw=1.6, label=name)
ax.annotate("", xy=(0.12, 0), xytext=(0.12, -35), arrowprops=dict(arrowstyle="<->", lw=0.9))
ax.text(0.2, -20, "H-bonded\nanion", fontsize=8, va="center")
ax.text(0.05, 6, r"Nu$^-$ + RX", ha="left", fontsize=9)
ax.set_title("(b) SN2 with an anion: protic solvent slows it", fontsize=10)

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("reaction coordinate")
    ax.set_ylabel("G")
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
fig.tight_layout()
