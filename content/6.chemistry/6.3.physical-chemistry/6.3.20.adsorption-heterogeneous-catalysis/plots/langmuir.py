"""Langmuir isotherms. Left: fractional coverage theta = a p / (1 + a p) for three adsorption
coefficients. Right: on log-log axes the low-pressure slope is 1 for molecular adsorption and
1/2 for dissociative adsorption (theta = (a p)^(1/2) / (1 + (a p)^(1/2)))."""

import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0, 20, 400)              # kPa
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
for a, col in [(0.1, "C0"), (1.0, "C1"), (10.0, "C3")]:
    ax1.plot(p, a * p / (1 + a * p), color=col, lw=1.8, label=rf"$a$ = {a:g} kPa$^{{-1}}$")
ax1.axhline(1, color="0.6", lw=0.8, ls="--")
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 1.08)
ax1.set_xlabel(r"$p\,/\,\mathrm{kPa}$")
ax1.set_ylabel(r"$\theta$")
ax1.legend(frameon=False, fontsize=8, loc="lower right")

x = np.logspace(-4, 3, 400)              # a p
ax2.loglog(x, x / (1 + x), color="C0", lw=1.8, label="molecular")
s = np.sqrt(x)
ax2.loglog(x, s / (1 + s), color="C3", lw=1.8, label="dissociative")
ax2.loglog(x[:150], x[:150], color="C0", lw=0.9, ls=":")
ax2.loglog(x[:150], np.sqrt(x[:150]), color="C3", lw=0.9, ls=":")
ax2.text(2e-3, 6e-4, "slope 1", fontsize=8, color="C0")
ax2.text(3e-4, 4e-2, "slope 1/2", fontsize=8, color="C3")
ax2.set_xlabel(r"$a p$")
ax2.set_ylabel(r"$\theta$")
ax2.set_ylim(1e-4, 2)
ax2.legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
