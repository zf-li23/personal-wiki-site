"""Mean ionic activity coefficients in water at 25 C (CRC Handbook / Robinson-Stokes values) against
sqrt(I_b / b0), compared with the Debye-Hueckel limiting law lg g = -A |z+ z-| sqrt(I), the extended
form with B a = 1 (kg/mol)^(1/2), and the Davies equation; A = 0.509 (kg/mol)^(1/2)."""

import numpy as np
import matplotlib.pyplot as plt

A = 0.509
sets = {
    "HCl (1-1)": (1, 1, [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0],
                  [0.965, 0.929, 0.905, 0.830, 0.796, 0.757, 0.809], "C3"),
    r"CaCl$_2$ (2-1)": (2, 3, [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0],
                        [0.888, 0.789, 0.732, 0.584, 0.518, 0.448, 0.500], "C0"),
    r"CuSO$_4$ (2-2)": (4, 4, [0.001, 0.005, 0.01, 0.1, 0.5, 1.0],
                        [0.74, 0.53, 0.44, 0.150, 0.062, 0.042], "C2"),
}
x = np.linspace(0, 2.0, 300)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
for ax, xmax in [(axes[0], 0.36), (axes[1], 2.0)]:
    for name, (zz, ifac, b, g, col) in sets.items():
        sI = np.sqrt(ifac * np.array(b))
        m = sI <= xmax
        ax.plot(sI[m], np.log10(np.array(g))[m], "o", color=col, ms=5, label=name)
        xx = x[x <= xmax]
        ax.plot(xx, -A * zz * xx, color=col, lw=0.9, ls=":")
        ax.plot(xx, -A * zz * xx / (1 + xx), color=col, lw=1.0, ls="--")
        ax.plot(xx, -A * zz * (xx / (1 + xx) - 0.30 * xx**2), color=col, lw=1.3)
    ax.set_xlim(0, xmax)
    ax.set_xlabel(r"$\sqrt{I_b/b^\circ}$")
    ax.set_ylabel(r"$\lg\gamma_\pm$")
axes[0].set_ylim(-0.75, 0.02)
axes[1].set_ylim(-1.6, 0.05)
axes[0].set_title("dilute range: points approach the limiting slopes", fontsize=10)
axes[1].set_title("dotted: limiting law; dashed: extended; solid: Davies", fontsize=10)
axes[0].legend(frameon=False, fontsize=9, loc="lower left")
fig.tight_layout()
