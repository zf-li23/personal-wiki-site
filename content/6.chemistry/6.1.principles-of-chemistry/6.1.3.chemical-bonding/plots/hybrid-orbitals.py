"""sp, sp2 and sp3 hybrids built from hydrogen-like 2s and 2p orbitals: contours of each hybrid in one plane."""

import numpy as np
import matplotlib.pyplot as plt

g = np.linspace(-9, 9, 500)
X, Y = np.meshgrid(g, g)
R = np.hypot(X, Y)  # in units of a0 / Z
radial = np.exp(-R / 2)
s2 = (R - 2) * radial  # 2s with the sign chosen positive outside its radial node; common factor dropped


def p2(direction_deg):
    t = np.radians(direction_deg)
    return (X * np.cos(t) + Y * np.sin(t)) * radial  # 2p along the given direction


def hybrid(direction_deg, lam2):
    return (s2 + np.sqrt(lam2) * p2(direction_deg)) / np.sqrt(1 + lam2)


cases = [
    ("sp: 2 hybrids at 180°", 1, [0, 180]),
    ("sp$^2$: 3 hybrids at 120°", 2, [90, 210, 330]),
    ("sp$^3$: 2 of the 4 hybrids, 109.5°", 3, [90 + 54.74, 90 - 54.74]),
]
level = 0.4
fig, axes = plt.subplots(1, 3, figsize=(11, 4))
for ax, (title, lam2, dirs) in zip(axes, cases):
    for k, d in enumerate(dirs):
        h = hybrid(d, lam2)
        color = f"C{k}"
        ax.contourf(X, Y, h, levels=[level, 10], colors=[color], alpha=0.35)
        ax.contour(X, Y, h, levels=[level], colors=[color], linewidths=1.4)
    ax.plot(0, 0, "o", color="0.2", ms=4)
    ax.set_aspect("equal")
    ax.set_xlim(-9, 9)
    ax.set_ylim(-9, 9)
    ax.axis("off")
    ax.set_title(title, fontsize=11)
fig.text(0.5, 0.03, "Contour of each hybrid at 0.4 of a common scale; the small opposite-sign lobe behind the nucleus is not drawn.",
         ha="center", fontsize=9)
fig.tight_layout(rect=(0, 0.06, 1, 1))
