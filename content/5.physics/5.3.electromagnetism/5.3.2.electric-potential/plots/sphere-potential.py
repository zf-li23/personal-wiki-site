"""Field E(r) and potential phi(r) of a uniformly charged ball and a uniformly charged spherical surface."""

import numpy as np
import matplotlib.pyplot as plt

R = 1.0
r = np.linspace(1e-3, 3.0, 1200)
inside = r < R

# units: E in Q / (4 pi eps0 R^2), phi in Q / (4 pi eps0 R)
E_ball = np.where(inside, r / R, R**2 / r**2)
phi_ball = np.where(inside, (3 * R**2 - r**2) / (2 * R**2), R / r)
E_surf = np.where(inside, 0.0, R**2 / r**2)
phi_surf = np.where(inside, 1.0, R / r)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))
ax1.plot(r, E_ball, lw=2, label="uniform ball")
ax1.plot(r[inside], E_surf[inside], lw=2, color="C1", label="charged spherical surface")
ax1.plot(r[~inside], E_surf[~inside], lw=2, color="C1")
ax1.plot([R, R], [0, 1], color="C1", lw=1, ls=":")
ax1.set_xlabel(r"$r\,/\,R$")
ax1.set_ylabel(r"$E\,/\,[Q/(4\pi\varepsilon_0 R^2)]$")
ax1.set_title("Field: jumps across a surface charge")
ax1.set_ylim(0, 1.6)

ax2.plot(r, phi_ball, lw=2, label="uniform ball")
ax2.plot(r, phi_surf, lw=2, color="C1", label="charged spherical surface")
ax2.plot([0], [1.5], "o", color="C0")
ax2.annotate(r"center: $\varphi = 1.5\,\varphi(R)$", xy=(0.02, 1.5), xytext=(0.5, 1.6),
             fontsize=9, arrowprops=dict(arrowstyle="->", lw=0.8))
ax2.set_xlabel(r"$r\,/\,R$")
ax2.set_ylabel(r"$\varphi\,/\,[Q/(4\pi\varepsilon_0 R)]$")
ax2.set_title("Potential: continuous everywhere")
ax2.set_ylim(0, 1.8)
for ax in (ax1, ax2):
    ax.axvline(R, color="0.6", lw=0.8)
    ax.set_xlim(0, 3)
    ax.legend(fontsize=9)
fig.tight_layout()
