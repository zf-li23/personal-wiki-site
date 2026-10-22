"""Activity coefficients (Raoult convention) of the one-parameter Margules model,
ln gamma_A = (W/RT) x_B^2 and ln gamma_B = (W/RT) x_A^2, for W/RT = +1.2 and -1.2."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 301)          # x_B
xa = 1 - x

fig, ax = plt.subplots(figsize=(6.2, 3.8))
for w, c in [(1.2, "C3"), (-1.2, "C0")]:
    ax.plot(x, w * x**2, color=c, lw=1.7, label=rf"$\ln\gamma_\mathrm{{A}}$, $W/RT$ = {w:+.1f}")
    ax.plot(x, w * xa**2, color=c, lw=1.7, ls="--", label=rf"$\ln\gamma_\mathrm{{B}}$, $W/RT$ = {w:+.1f}")
ax.axhline(0, color="0.6", lw=0.7)
ax.set_xlabel(r"$x_\mathrm{B}$")
ax.set_ylabel(r"$\ln\gamma$ (Raoult convention)")
ax.set_xlim(0, 1)
ax.set_ylim(-1.8, 1.35)
ax.legend(frameon=False, fontsize=8.5, ncol=2, loc="lower center")
fig.tight_layout()
