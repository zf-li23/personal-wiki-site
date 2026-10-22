"""Polar cross sections (xz plane) of the angular functions Y and |Y|^2."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1441)  # angle from the z axis, in the xz plane (phi = 0 or pi)
sx, cz = np.sin(t), np.cos(t)        # unit vector (x, z)
ORBITALS = [
    ("s", np.full_like(t, np.sqrt(1 / (4 * np.pi)))),
    ("p$_z$", np.sqrt(3 / (4 * np.pi)) * cz),
    ("d$_{z^2}$", np.sqrt(5 / (16 * np.pi)) * (3 * cz**2 - 1)),
    ("d$_{xz}$", np.sqrt(15 / (4 * np.pi)) * sx * cz),
]

fig, axes = plt.subplots(2, 4, figsize=(11, 5.8))
for j, (name, Y) in enumerate(ORBITALS):
    for i, (vals, title) in enumerate([(Y, f"{name}: Y"), (Y**2, f"{name}: |Y|$^2$")]):
        ax = axes[i, j]
        if i == 0:
            pos, neg = np.maximum(vals, 0), np.maximum(-vals, 0)
            ax.fill(pos * sx, pos * cz, color="C3", alpha=0.35, lw=0)
            ax.fill(neg * sx, neg * cz, color="C0", alpha=0.35, lw=0)
            ax.plot(np.abs(vals) * sx, np.abs(vals) * cz, color="0.3", lw=1.0)
            for r, sign in [(pos, "+"), (neg, "\u2212")]:
                # label every lobe at its local maximum
                peaks = [k for k in range(len(t) - 1)
                         if r[k] > 0.3 * np.abs(vals).max() and r[k] >= r[k - 1] and r[k] > r[k + 1]]
                if np.ptp(r) == 0 and r[0] > 0:
                    peaks = [len(t) // 8]
                for k in peaks:
                    ax.text(0.55 * r[k] * sx[k], 0.55 * r[k] * cz[k], sign, ha="center",
                            va="center", fontsize=13, fontweight="bold")
        else:
            ax.fill(vals * sx, vals * cz, color="C2", alpha=0.35, lw=0)
            ax.plot(vals * sx, vals * cz, color="0.3", lw=1.0)
        m = 1.1 * np.abs(vals).max()
        ax.set_xlim(-m, m)
        ax.set_ylim(-m, m)
        ax.axhline(0, color="0.6", lw=0.6)
        ax.axvline(0, color="0.6", lw=0.6)
        ax.text(0.97, 0.5, "x", transform=ax.transAxes, ha="right", va="bottom", fontsize=9)
        ax.text(0.5, 0.97, "z", transform=ax.transAxes, ha="left", va="top", fontsize=9)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(title, fontsize=10)
fig.tight_layout()
