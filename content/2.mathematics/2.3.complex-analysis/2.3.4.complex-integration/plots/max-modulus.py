"""|f| for f(z) = z^2 + 2z - 1 over the closed unit disc: the maximum sits on the boundary."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 1, 60)
t = np.linspace(0, 2 * np.pi, 181)
R, T = np.meshgrid(r, t)
Z = R * np.exp(1j * T)
F = np.abs(Z**2 + 2 * Z - 1)

fig = plt.figure(figsize=(11, 5))
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.plot_surface(Z.real, Z.imag, F, cmap="viridis", linewidth=0, alpha=0.9, rstride=2, cstride=2)
b = np.exp(1j * t)
ax.plot(b.real, b.imag, np.abs(b**2 + 2 * b - 1), color="C3", lw=2)
for z in [1j, -1j]:
    ax.scatter([z.real], [z.imag], [abs(z**2 + 2 * z - 1)], color="C1", s=40)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("|f(z)|")
ax.view_init(elev=28, azim=-50)
ax.set_title("surface |f| over |z| <= 1")

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(t, np.abs(b**2 + 2 * b - 1), color="C3", lw=2, label="|f(e^{it})| = 2 sqrt(1 + sin^2 t)")
ax2.axhline(2 * np.sqrt(2), color="C1", ls="--", lw=1.2, label="max = 2 sqrt 2 at z = i, -i")
ax2.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax2.set_xticklabels(["0", "pi/2", "pi", "3pi/2", "2pi"])
ax2.set_xlabel("t")
ax2.set_ylabel("|f|")
ax2.set_ylim(1.5, 3.2)
ax2.legend(fontsize=8)
ax2.set_title("modulus on the boundary circle")
fig.tight_layout()
