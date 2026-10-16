"""The argument principle for p(z) = z^7 - 5z^3 + z - 2: the zeros of p, and the images
of the circles |z| = 1 and |z| = 2, which wind 3 and 7 times around the origin."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

coef = [1, 0, 0, 0, -5, 0, 1, -2]


def p(z):
    return np.polyval(coef, z)


L = 2.4
x = np.linspace(-L, L, 800)
X, Y = np.meshgrid(x, x)
W = p(X + 1j * Y)
hue = (np.angle(W) / (2 * np.pi)) % 1.0
lm = np.log2(np.abs(W) + 1e-300)
val = 0.62 + 0.38 * (lm - np.floor(lm))
rgb = hsv_to_rgb(np.stack([hue, 0.85 * np.ones_like(hue), val], axis=-1))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5.4))
ax1.imshow(rgb, extent=[-L, L, -L, L], origin="lower")
t = np.linspace(0, 2 * np.pi, 2000)
for r, col in ((1, "white"), (2, "black")):
    ax1.plot(r * np.cos(t), r * np.sin(t), color=col, lw=1.5, ls="--")
roots = np.roots(coef)
ax1.plot(roots.real, roots.imag, "o", color="white", mec="black", ms=6)
ax1.set_title(r"zeros of $p(z) = z^7 - 5z^3 + z - 2$")
ax1.set_xlabel("Re z")
ax1.set_ylabel("Im z")

for ax, r, n in ((ax2, 1, 3), (ax3, 2, 7)):
    w = p(r * np.exp(1j * t))
    ax.plot(w.real, w.imag, color="C0", lw=1.2)
    ax.plot(0, 0, "r+", ms=12, mew=2)
    ax.set_aspect("equal")
    ax.axhline(0, color="gray", lw=0.6)
    ax.axvline(0, color="gray", lw=0.6)
    ax.set_title(f"image of |z| = {r}: winding number {n}")
    ax.set_xlabel("Re w")
    ax.set_ylabel("Im w")
fig.tight_layout()
