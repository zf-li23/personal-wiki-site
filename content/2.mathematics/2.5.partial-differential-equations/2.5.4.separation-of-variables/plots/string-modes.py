"""Normal modes of a string with fixed ends, and the plucked string summed from its Fourier series."""

import numpy as np
import matplotlib.pyplot as plt

l, c = 1.0, 1.0
x = np.linspace(0, l, 801)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.6))

for n in range(1, 5):
    base = 2.6 * (4 - n)
    for j, ph in enumerate(np.linspace(0, np.pi, 7)):
        ax1.plot(x, base + np.sin(n * np.pi * x / l) * np.cos(ph), color=f"C{n - 1}",
                 lw=1.6 if j == 0 else 0.7, alpha=1.0 if j == 0 else 0.5)
    ax1.axhline(base, color="0.75", lw=0.6)
    ax1.text(1.02, base, f"n = {n}", va="center", fontsize=9)
ax1.set_xlim(0, 1.12)
ax1.set_yticks([])
ax1.set_xlabel("x / l")
ax1.set_title("Standing waves sin(nπx/l) cos(ω_n t)")

b, h = 0.25, 1.0
n = np.arange(1, 401)
A = 2 * h * l**2 / (np.pi**2 * n**2 * b * (l - b)) * np.sin(n * np.pi * b / l)
modes = np.sin(np.outer(n, x) * np.pi / l)
period = 2 * l / c
for i, frac in enumerate([0, 0.125, 0.25, 0.375, 0.5]):
    t = frac * period
    u = (A * np.cos(n * np.pi * c * t / l)) @ modes
    ax2.plot(x, u - 1.25 * i, color=f"C{i}", lw=1.7)
    ax2.axhline(-1.25 * i, color="0.75", lw=0.6)
    ax2.text(1.02, -1.25 * i, f"t = {frac:g} T", va="center", fontsize=9)
ax2.set_xlim(0, 1.15)
ax2.set_yticks([])
ax2.set_xlabel("x / l")
ax2.set_title("Plucked string at b = l/4 (period T = 2l/c)")

fig.tight_layout()
