"""Lattice-gas (regular-solution) model of an intercalation electrode Li_x[H] at 25 C:
E = E0 - (RT/F) ln(x / (1 - x)) + f (x - 1/2), with f = 2 Omega / F and Omega the interaction
parameter. For f > 4RT/F = 0.103 V the curve is no longer monotonic; the host separates into
two phases and the equilibrium potential is a plateau at E0 (equal-area construction, symmetric here).
Left: E against x. Right: differential capacity dx/dE against E (the plateau gives a spike)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

kT = 8.314462618 * 298.15 / 96485.33212      # RT/F in V
x = np.linspace(1e-4, 1 - 1e-4, 2000)
E0 = 0.0

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
for fpar, col in [(-0.10, "C0"), (0.0, "C2"), (0.08, "C1"), (0.20, "C3")]:
    E = E0 - kT * np.log(x / (1 - x)) + fpar * (x - 0.5)
    lab = f"f = {fpar:+.2f} V"
    if fpar > 4 * kT:
        x1 = brentq(lambda y: -kT * np.log(y / (1 - y)) + fpar * (y - 0.5), 1e-6, 0.45)
        x2 = 1 - x1
        out = (x < x1) | (x > x2)
        axes[0].plot(x[x < x1], E[x < x1], color=col, lw=1.8, label=lab + " (two phases)")
        axes[0].plot(x[x > x2], E[x > x2], color=col, lw=1.8)
        axes[0].plot([x1, x2], [E0, E0], color=col, lw=1.8)
        axes[0].plot(x[~out], E[~out], color=col, lw=0.8, ls=":")
        dEdx = -kT / (x * (1 - x)) + fpar
        axes[1].plot(E[out & (x < 0.5)], -1 / dEdx[out & (x < 0.5)], color=col, lw=1.6)
        axes[1].plot(E[out & (x > 0.5)], -1 / dEdx[out & (x > 0.5)], color=col, lw=1.6)
        axes[1].plot([E0, E0], [0, 30], color=col, lw=1.6)
    else:
        axes[0].plot(x, E, color=col, lw=1.8, label=lab)
        dEdx = -kT / (x * (1 - x)) + fpar
        axes[1].plot(E, -1 / dEdx, color=col, lw=1.6)
axes[0].set_xlim(0, 1)
axes[0].set_ylim(-0.2, 0.2)
axes[0].set_xlabel(r"$x$ in Li$_x$[H]")
axes[0].set_ylabel(r"$(E - E^\circ)$ / V")
axes[0].legend(frameon=False, fontsize=8.5, loc="upper right")
axes[0].set_title("equilibrium potential against composition", fontsize=10)
axes[1].set_xlim(-0.2, 0.2)
axes[1].set_ylim(0, 20)
axes[1].set_xlabel(r"$(E - E^\circ)$ / V")
axes[1].set_ylabel(r"$-\mathrm{d}x/\mathrm{d}E$ / V$^{-1}$")
axes[1].set_title("differential capacity: peak width shrinks as f grows", fontsize=10)
fig.tight_layout()
