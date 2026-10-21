"""Standing wave snapshots and the first normal modes of a string fixed at both ends."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))

x = np.linspace(0, 2.0, 800)  # in units of the wavelength
for i, frac in enumerate([0, 1 / 8, 1 / 4, 3 / 8, 1 / 2]):
    y = 2 * np.cos(2 * np.pi * x) * np.cos(2 * np.pi * frac)
    ax1.plot(x, y, color=f"C{i}", lw=1.5, label=f"t = {frac:g} T")
for xn in [0.25, 0.75, 1.25, 1.75]:
    ax1.plot([xn], [0], "ko", ms=4)
    ax1.text(xn, -0.45, "N", ha="center", fontsize=9)
for xa in [0, 0.5, 1.0, 1.5, 2.0]:
    ax1.text(xa, 2.25, "A", ha="center", fontsize=9)
ax1.set_ylim(-2.5, 2.6)
ax1.set_xlabel("x / λ")
ax1.set_ylabel("y / A")
ax1.set_title("Standing wave over half a period")
ax1.legend(loc="lower right", fontsize=7, ncol=2)

L = 1.0
s = np.linspace(0, L, 400)
for n in [1, 2, 3]:
    off = -3.0 * (n - 1)
    for ph in np.linspace(-1, 1, 5):
        ax2.plot(s, off + ph * np.sin(n * np.pi * s / L), color=f"C{n - 1}", lw=1.0, alpha=0.35 + 0.65 * (abs(ph) == 1))
    ax2.text(1.04, off, f"n = {n}\nλ = 2L/{n}" if n > 1 else "n = 1\nλ = 2L", va="center", fontsize=9)
ax2.plot([0, 0], [-8, 1.5], color="0.4", lw=3)
ax2.plot([L, L], [-8, 1.5], color="0.4", lw=3)
ax2.set_xlim(-0.05, 1.3)
ax2.set_ylim(-7.5, 1.5)
ax2.set_yticks([])
ax2.set_xlabel("x / L")
ax2.set_title("Normal modes, both ends fixed")

fig.tight_layout()
