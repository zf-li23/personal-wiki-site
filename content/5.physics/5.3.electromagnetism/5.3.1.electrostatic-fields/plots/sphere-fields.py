"""Field magnitude E(r) of a uniformly charged ball, thick shell and thin shell (same total charge Q)."""

import numpy as np
import matplotlib.pyplot as plt

R2 = 1.0
r = np.linspace(0.0, 3.0, 1201)


def shell(r, R1, R2):
    """E(r) in units of Q / (4 pi eps0 R2^2) for charge Q spread uniformly over R1 < r < R2."""
    frac = np.clip((r**3 - R1**3) / (R2**3 - R1**3), 0.0, 1.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        E = np.where(r > 0, frac * R2**2 / r**2, 0.0)
    return E


fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(r, shell(r, 0.0, R2), lw=2, label=r"uniform ball ($R_1 = 0$)")
ax.plot(r, shell(r, 0.5, R2), lw=2, label=r"thick shell ($R_1 = 0.5R_2$)")
# thin shell: zero inside, jump at r = R2
inside = r < R2
ax.plot(r[inside], np.zeros(inside.sum()), lw=2, color="C2", label=r"thin shell ($R_1 = R_2$)")
ax.plot(r[~inside], R2**2 / r[~inside] ** 2, lw=2, color="C2")
ax.plot([R2, R2], [0, 1], color="C2", lw=1, ls=":")
ax.plot(r[r > 0.3], 1 / r[r > 0.3] ** 2, color="0.5", lw=1, ls="--", label="point charge Q at the center")
ax.axvline(R2, color="0.6", lw=0.8)
ax.set_xlim(0, 3)
ax.set_ylim(0, 1.6)
ax.set_xlabel(r"$r\,/\,R_2$")
ax.set_ylabel(r"$E\,/\,[Q/(4\pi\varepsilon_0 R_2^2)]$")
ax.set_title("Gauss's law for spherically symmetric charge")
ax.legend(fontsize=9)
fig.tight_layout()
