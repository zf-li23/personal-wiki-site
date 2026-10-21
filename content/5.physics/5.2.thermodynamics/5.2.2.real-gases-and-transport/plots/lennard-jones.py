"""Intermolecular potential and force: Lennard-Jones model and the attracting hard-sphere model of van der Waals."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.88, 2.6, 800)  # r / r0
U = x**-12 - 2 * x**-6  # E_p / E_0
F = 12 * (x**-13 - x**-7)  # F r0 / E_0, positive = repulsive

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, U, color="C0", lw=1.6, label=r"potential energy $E_{\mathrm{p}}/E_0$")
ax1.plot(x, F, color="C1", lw=1.6, label=r"force $F r_0/E_0$ (positive = repulsive)")
ax1.axhline(0, color="0.5", lw=0.8)
ax1.axvline(1, color="0.5", lw=0.8, ls=":")
ax1.set_xlim(0.88, 2.6)
ax1.set_ylim(-3, 4)
ax1.set_xlabel(r"$r/r_0$")
ax1.set_title("Lennard-Jones 12-6 model")
ax1.legend(fontsize=9, loc="upper right")

d, s, f0 = 1.0, 2.0, 0.6
ax2.plot([d, d], [0, 3], color="C1", lw=1.6)
ax2.plot([d, s, s, 3], [-f0, -f0, 0, 0], color="C1", lw=1.6, label="force")
ax2.axhline(0, color="0.5", lw=0.8)
ax2.fill_between([0.85, d], -2.5, 3, color="0.6", alpha=0.3)
ax2.annotate("hard core", (0.87, 2.4), fontsize=9)
ax2.annotate("constant attraction", (1.1, -0.9), fontsize=9)
ax2.set_xticks([d, s])
ax2.set_xticklabels([r"$d$", r"$s$"])
ax2.set_yticks([0])
ax2.set_xlim(0.85, 3)
ax2.set_ylim(-2.5, 3)
ax2.set_xlabel(r"$r$")
ax2.set_ylabel(r"$F$")
ax2.set_title("Attracting hard spheres (van der Waals)")
ax2.legend(fontsize=9)
fig.tight_layout()
