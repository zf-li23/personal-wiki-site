"""Image of a Cartesian grid under w = z^2: right angles survive except at z = 0."""

import numpy as np
import matplotlib.pyplot as plt

fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 5))
s = np.linspace(0, 2, 400)
levels = np.linspace(0.25, 2, 8)

for c in levels:
    for ax, f in [(a1, lambda z: z), (a2, lambda z: z**2)]:
        w = f(c + 1j * s)  # vertical line x = c
        ax.plot(w.real, w.imag, color="C0", lw=1.1)
        w = f(s + 1j * c)  # horizontal line y = c
        ax.plot(w.real, w.imag, color="C3", lw=1.1)

# a small square at z0 = 1 + 0.75i and its image
z0, h = 1.0 + 0.75j, 0.25
sq = z0 + h * np.array([0, 1, 1 + 1j, 1j, 0])
a1.fill(sq.real, sq.imag, color="C2", alpha=0.5)
zz = np.concatenate([z0 + h * np.linspace(0, 1, 30), z0 + h + 1j * h * np.linspace(0, 1, 30),
                     z0 + h * (1 + 1j) - h * np.linspace(0, 1, 30), z0 + 1j * h - 1j * h * np.linspace(0, 1, 30)])
a2.fill((zz**2).real, (zz**2).imag, color="C2", alpha=0.5)

# the right angle at 0 between the positive axes becomes a straight angle
a1.plot([0, 2], [0, 0], color="C1", lw=2.5)
a1.plot([0, 0], [0, 2], color="C1", lw=2.5)
a2.plot([-4, 4], [0, 0], color="C1", lw=2.5)

a1.set_title("z-plane: lines x = c (blue) and y = c (red)")
a2.set_title("w = z^2: orthogonal parabolas; angle at 0 doubled")
a1.set_xlim(-0.1, 2.1)
a1.set_ylim(-0.1, 2.1)
a2.set_xlim(-4.2, 4.2)
a2.set_ylim(-0.2, 8.2)
for ax, lab in [(a1, "z"), (a2, "w")]:
    ax.set_aspect("equal")
    ax.set_xlabel(f"Re {lab}")
    ax.set_ylabel(f"Im {lab}")
fig.tight_layout()
