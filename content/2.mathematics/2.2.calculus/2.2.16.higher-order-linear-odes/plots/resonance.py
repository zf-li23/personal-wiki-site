"""Steady-state amplitude of x'' + 2k x' + w^2 x = H sin(pt), and undamped resonance."""

import numpy as np
import matplotlib.pyplot as plt

w, H = 1.0, 1.0
p = np.linspace(0.01, 2.5, 800)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6))
for k, col in [(0.05, "C3"), (0.1, "C1"), (0.2, "C2"), (0.4, "C0"), (0.8, "C4")]:
    A = H / np.sqrt((w**2 - p**2) ** 2 + 4 * k**2 * p**2)
    ax1.plot(p, A, color=col, lw=1.8, label=f"k = {k:g}")
    if k < w / np.sqrt(2):
        pm = np.sqrt(w**2 - 2 * k**2)
        ax1.plot([pm], [H / (2 * k * np.sqrt(w**2 - k**2))], "o", color=col, ms=4)
ax1.axvline(w, color="0.5", lw=0.8, ls="--")
ax1.set_ylim(0, 10.5)
ax1.set_xlim(0, 2.5)
ax1.set_xlabel("driving frequency p")
ax1.set_ylabel("steady-state amplitude A(p)")
ax1.set_title("A(p) = H / sqrt((w^2 - p^2)^2 + 4k^2 p^2),  w = 1")
ax1.legend()

t = np.linspace(0, 40, 2000)
x = -t * np.cos(t) / 2
ax2.plot(t, x, color="C3", lw=1.4, label="x = -(t cos t)/2")
ax2.plot(t, t / 2, color="0.5", lw=0.9, ls="--", label="envelope +- t/2")
ax2.plot(t, -t / 2, color="0.5", lw=0.9, ls="--")
ax2.set_xlim(0, 40)
ax2.set_xlabel("t")
ax2.set_ylabel("x(t)")
ax2.set_title("Undamped resonance: x'' + x = sin t")
ax2.legend(loc="upper left")
fig.tight_layout()
