"""d'Alembert's formula: a plucked string on the line, and reflection at a fixed end."""

import numpy as np
import matplotlib.pyplot as plt


def tri(x, a=1.0):
    return np.clip(1 - np.abs(x) / a, 0, None)


def pulse(x):
    return np.exp(-6 * (x - 4.0) ** 2)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.6))
c = 1.0
gap = 1.0  # vertical offset between snapshots

x = np.linspace(-5, 5, 1001)
for i, t in enumerate([0, 0.5, 1.0, 2.0, 3.0]):
    u = 0.5 * (tri(x + c * t) + tri(x - c * t))
    ax1.plot(x, u + gap * i, color=f"C{i}", lw=1.8)
    ax1.text(4.9, gap * i + 0.15, f"t = {t}", ha="right", fontsize=9)
ax1.set_xlim(-5, 5)
ax1.set_xlabel("x")
ax1.set_yticks([])
ax1.set_title("Plucked string on the line")

x = np.linspace(0, 7, 1001)


def odd(f, x):
    return np.where(x >= 0, f(np.abs(x)), -f(np.abs(x)))


for i, t in enumerate([0, 1.5, 3.5, 4.0, 4.5, 6.0]):
    u = 0.5 * (odd(pulse, x + c * t) + odd(pulse, x - c * t))
    ax2.plot(x, 0.8 * u + 1.6 * i, color=f"C{i}", lw=1.8)
    ax2.axhline(1.6 * i, color="0.75", lw=0.6)
    ax2.text(6.9, 1.6 * i + 0.25, f"t = {t}", ha="right", fontsize=9)
ax2.axvline(0, color="0.3", lw=3)
ax2.set_xlim(-0.2, 7)
ax2.set_xlabel("x")
ax2.set_yticks([])
ax2.set_title("Fixed end at x = 0: inverted reflection")

fig.tight_layout()
