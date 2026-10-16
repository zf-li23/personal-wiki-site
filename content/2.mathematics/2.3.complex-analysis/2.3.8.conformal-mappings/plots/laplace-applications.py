"""Two applications of conformal mapping to Laplace's equation.
Left: steady temperature in the unit disk with u = 1 on the upper semicircle and u = 0
on the lower one, u = 1/2 + arctan(2y/(1 - x^2 - y^2))/pi.
Right: streamlines Im F = const of the ideal flow past a cylinder, F(z) = z + 1/z."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.6))

x = np.linspace(-1, 1, 700)
X, Y = np.meshgrid(x, x)
inside = X**2 + Y**2 < 1
U = 0.5 + np.arctan2(2 * Y, 1 - X**2 - Y**2) / np.pi
U = np.where(inside, U, np.nan)
cf = ax1.contourf(X, Y, U, levels=np.linspace(0, 1, 21), cmap="coolwarm")
ax1.contour(X, Y, U, levels=np.linspace(0.1, 0.9, 9), colors="k", linewidths=0.7)
t = np.linspace(0, np.pi, 200)
ax1.plot(np.cos(t), np.sin(t), color="C3", lw=3, label="u = 1")
ax1.plot(np.cos(t), -np.sin(t), color="C0", lw=3, label="u = 0")
ax1.set_aspect("equal")
ax1.set_title("isotherms in the disk")
ax1.legend(loc="upper right", fontsize=9)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
fig.colorbar(cf, ax=ax1, shrink=0.8)

x = np.linspace(-3, 3, 800)
X, Y = np.meshgrid(x, x)
Z = X + 1j * Y
with np.errstate(all="ignore"):
    F = Z + 1 / Z
psi = np.where(np.abs(Z) >= 1, F.imag, np.nan)
ax2.contour(X, Y, psi, levels=np.linspace(-3, 3, 25), colors="C0", linewidths=1.0, linestyles="solid")
ax2.fill(np.cos(2 * t), np.sin(2 * t), color="gray", alpha=0.5)
ax2.set_aspect("equal")
ax2.set_title(r"streamlines of $F(z) = z + 1/z$")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
fig.tight_layout()
