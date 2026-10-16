"""w = exp(z) maps the strip -pi < Im z <= pi onto the punctured plane."""

import numpy as np
import matplotlib.pyplot as plt

fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 5))
ys = np.linspace(-np.pi, np.pi, 400)
xs = np.linspace(-1.5, 1, 400)

for c in np.linspace(-1.5, 1, 6):  # vertical lines -> circles
    a1.plot(np.full_like(ys, c), ys, color="C0", lw=1.1)
    w = np.exp(c + 1j * ys)
    a2.plot(w.real, w.imag, color="C0", lw=1.1)
for c in np.linspace(-np.pi, np.pi, 13)[1:-1]:  # horizontal lines -> rays
    a1.plot(xs, np.full_like(xs, c), color="C3", lw=1.1)
    w = np.exp(xs + 1j * c)
    a2.plot(w.real, w.imag, color="C3", lw=1.1)

# the edges Im z = pi and Im z = -pi both go to the negative real axis
for y0 in [np.pi, -np.pi]:
    a1.plot(xs, np.full_like(xs, y0), color="C1", lw=2.5)
w = np.exp(xs + 1j * np.pi)
a2.plot(w.real, w.imag, color="C1", lw=2.5)
a1.fill_between(xs, 0, np.pi / 6, color="C2", alpha=0.35)
arc = np.linspace(0, np.pi / 6, 50)
r = np.exp(xs)
sector = np.concatenate([r, r[-1] * np.exp(1j * arc), r[::-1] * np.exp(1j * np.pi / 6), r[0] * np.exp(1j * arc[::-1])])
a2.fill(sector.real, sector.imag, color="C2", alpha=0.35)

a1.set_title("z-plane: strip of height 2 pi")
a2.set_title("w = exp(z): circles |w| = e^x and rays arg w = y")
a1.set_xlim(-1.7, 1.2)
a1.set_ylim(-3.5, 3.5)
a2.set_xlim(-3, 3)
a2.set_ylim(-3, 3)
for ax, lab in [(a1, "z"), (a2, "w")]:
    ax.set_aspect("equal")
    ax.set_xlabel(f"Re {lab}")
    ax.set_ylabel(f"Im {lab}")
fig.tight_layout()
