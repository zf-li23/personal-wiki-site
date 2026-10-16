"""The Cayley map w = (z - i)/(z + i) sends the upper half-plane onto the unit disk:
horizontal lines become circles tangent to the unit circle at w = 1, vertical lines
become arcs through w = 1 orthogonal to the unit circle."""

import numpy as np
import matplotlib.pyplot as plt


def cayley(z):
    return (z - 1j) / (z + 1j)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.6))
s = np.linspace(-60, 60, 6000)
ys = [0.25, 0.5, 1, 2, 4]
xs = [-3, -2, -1, -0.5, 0, 0.5, 1, 2, 3]
for k, y in enumerate(ys):
    z = s + 1j * y
    ax1.plot(z.real, z.imag, color="C0", lw=1.2)
    w = cayley(z)
    ax2.plot(w.real, w.imag, color="C0", lw=1.2)
yy = np.linspace(1e-3, 400, 20000)
for x in xs:
    z = x + 1j * yy
    ax1.plot(z.real, z.imag, color="C1", lw=1.2)
    w = cayley(z)
    ax2.plot(w.real, w.imag, color="C1", lw=1.2)

ax1.plot(0, 1, "ko", ms=5)
ax1.text(0.08, 1.08, "i", fontsize=12)
ax1.set_xlim(-3.5, 3.5)
ax1.set_ylim(-0.3, 4.5)
ax1.axhline(0, color="gray", lw=1.5)
ax1.set_aspect("equal")
ax1.set_title("upper half-plane Im z > 0")
ax1.set_xlabel("Re z")
ax1.set_ylabel("Im z")

t = np.linspace(0, 2 * np.pi, 400)
ax2.plot(np.cos(t), np.sin(t), color="gray", lw=1.5)
ax2.plot(0, 0, "ko", ms=5)
ax2.text(0.04, 0.05, "0 = image of i", fontsize=10)
ax2.set_xlim(-1.15, 1.15)
ax2.set_ylim(-1.15, 1.15)
ax2.set_aspect("equal")
ax2.set_title(r"unit disk: $w = (z - i)/(z + i)$")
ax2.set_xlabel("Re w")
ax2.set_ylabel("Im w")
fig.tight_layout()
