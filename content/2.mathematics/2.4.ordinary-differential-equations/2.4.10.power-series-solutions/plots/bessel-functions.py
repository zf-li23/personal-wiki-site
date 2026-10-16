"""Bessel functions of the first kind J_0, J_1, J_2 (with the asymptotic form of J_0)
and of the second kind Y_0, Y_1."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, yv

x = np.linspace(0.001, 20, 2000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4.4))
for n in range(3):
    ax1.plot(x, jv(n, x), label=f"$J_{n}$")
xa = np.linspace(1.0, 20, 800)
ax1.plot(xa, np.sqrt(2 / (np.pi * xa)) * np.cos(xa - np.pi / 4), "k--", lw=1,
         label=r"$\sqrt{2/(\pi x)}\cos(x - \pi/4)$")
ax1.axhline(0, color="gray", lw=0.8)
ax1.set_ylim(-0.7, 1.05)
ax1.set_xlabel("x")
ax1.set_title("Bessel functions of the first kind")
ax1.legend(fontsize=9)
ax1.grid(alpha=0.3)

for n in range(2):
    ax2.plot(x, yv(n, x), label=f"$Y_{n}$", color=f"C{n + 3}")
ax2.axhline(0, color="gray", lw=0.8)
ax2.set_ylim(-1.6, 0.8)
ax2.set_xlabel("x")
ax2.set_title("Bessel functions of the second kind")
ax2.legend()
ax2.grid(alpha=0.3)
fig.tight_layout()
