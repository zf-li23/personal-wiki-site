"""Schematic free-energy profiles for SNAr of 1-halo-2,4-dinitrobenzenes (qualitative energy scale).
The addition step (TS1) is rate-determining. Fluorine, the most electronegative halogen, lowers TS1
and the Meisenheimer complex most; the strong C-F bond only raises TS2, which stays below TS1.
For iodine TS1 is highest, so ArF reacts fastest: F >> Cl ~ Br > I, the reverse of SN2."""

import numpy as np
import matplotlib.pyplot as plt


def profile(xs, ys):
    """Smooth curve through stationary points (xs, ys): cosine segments with zero slope at each point."""
    px, py = [], []
    for (x0, x1), (y0, y1) in zip(zip(xs, xs[1:]), zip(ys, ys[1:])):
        x = np.linspace(x0, x1, 50)
        px.append(x)
        py.append(y0 + (y1 - y0) * (1 - np.cos(np.pi * (x - x0) / (x1 - x0))) / 2)
    return np.concatenate(px), np.concatenate(py)


fig, ax = plt.subplots(figsize=(6.4, 4.2))
for ts1, mc, ts2, color, name in ((12, 4, 9, "C2", "X = F"), (16, 8, 10, "C0", "X = Cl"), (17.5, 9.5, 10.5, "C3", "X = I")):
    x, y = profile([0, 0.7, 1.15, 1.5, 2.2], [0, ts1, mc, ts2, -8])
    ax.plot(x, y, color=color, lw=2, label=name)
ax.text(0, -1.2, "ArX + Nu$^-$", ha="center", va="top", fontsize=9)
ax.text(0.7, 18.6, "TS1: addition (slow)", ha="center", fontsize=9)
ax.text(1.15, 2.6, "Meisenheimer\ncomplex", ha="center", va="top", fontsize=9)
ax.text(1.62, 12.0, "TS2: loss of X$^-$", ha="left", fontsize=9)
ax.text(2.25, -8, "ArNu + X$^-$", va="center", fontsize=9)
ax.legend(fontsize=8, loc="lower left", frameon=False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel("reaction coordinate")
ax.set_ylabel("G")
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.set_xlim(-0.3, 2.9)
ax.set_ylim(-11, 21)
fig.tight_layout()
