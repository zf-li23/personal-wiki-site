"""The Joukowski map w = (z + 1/z)/2. Left: on |z| > 1, circles |z| = r map to ellipses
with foci -1 and 1, and rays arg z = const map to hyperbolas with the same foci.
Right: a circle through z = 1 that encloses z = -1 maps to an airfoil."""

import numpy as np
import matplotlib.pyplot as plt


def jk(z):
    return 0.5 * (z + 1 / z)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.4))
t = np.linspace(0, 2 * np.pi, 800)
for r in (1.0, 1.2, 1.5, 2.0, 2.7):
    w = jk(r * np.exp(1j * t))
    ax1.plot(w.real, w.imag, color="C0", lw=1.6 if r == 1.0 else 1.1)
rho = np.linspace(1, 4, 400)
for k in range(16):
    th = k * np.pi / 8 + np.pi / 16
    w = jk(rho * np.exp(1j * th))
    ax1.plot(w.real, w.imag, color="C1", lw=1.1)
ax1.plot([-1, 1], [0, 0], "k.", ms=8)
ax1.set_xlim(-2.2, 2.2)
ax1.set_ylim(-1.7, 1.7)
ax1.set_aspect("equal")
ax1.set_title("images of circles (ellipses) and rays (hyperbolas)")
ax1.set_xlabel("Re w")
ax1.set_ylabel("Im w")

c = -0.09 + 0.09j
R = abs(1 - c)
circ = c + R * np.exp(1j * t)
ax2.plot(circ.real, circ.imag, color="gray", ls="--", lw=1.2, label="circle in the z-plane")
w = jk(circ)
ax2.fill(w.real, w.imag, color="C0", alpha=0.35)
ax2.plot(w.real, w.imag, color="C0", lw=1.8, label="its image: Joukowski airfoil")
ax2.plot([1], [0], "k.", ms=8)
ax2.set_aspect("equal")
ax2.set_xlim(-1.5, 1.4)
ax2.set_ylim(-1.3, 1.4)
ax2.legend(loc="lower right", fontsize=9)
ax2.set_title("airfoil")
ax2.set_xlabel("Re")
ax2.set_ylabel("Im")
fig.tight_layout()
