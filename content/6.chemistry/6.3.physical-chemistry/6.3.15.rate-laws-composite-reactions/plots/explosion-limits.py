"""Schematic explosion limits of a stoichiometric H2 + O2 mixture (log pressure versus
temperature): the explosion peninsula between the first and second limits, and the
thermal explosion region above the third limit. Shapes only; no measured data."""

import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(730, 880, 300)
s = (T - 730) / 150
lnp1 = 0.6 - 1.2 * s + 0.8 * s**2            # first (lower) limit, falls slowly with T
lnp2 = 0.6 + 4.5 * np.sqrt(s) + 0.6 * s      # second (upper) limit, rises steeply
lnp3 = 9.5 - 3.5 * s                         # third limit (thermal explosion)

fig, ax = plt.subplots(figsize=(6.2, 4.2))
ax.fill_between(T, lnp1, lnp2, color="C3", alpha=0.25, lw=0)
ax.fill_between(T, np.maximum(lnp3, lnp2), 11, color="C1", alpha=0.25, lw=0)
ax.plot(T, lnp1, color="C3")
ax.plot(T, lnp2, color="C3")
ax.plot(T, lnp3, color="C1")
ax.text(820, 2.4, "chain-branching\nexplosion", ha="center", fontsize=9)
ax.text(860, 10.0, "thermal\nexplosion", ha="center", fontsize=9)
ax.text(760, 6.2, "slow reaction", ha="center", fontsize=9)
ax.text(855, -0.3, "slow reaction", ha="center", fontsize=9)
ax.text(880, lnp1[-1] + 0.15, " first limit", fontsize=8, va="bottom")
ax.text(880, lnp2[-1], " second limit", fontsize=8, va="center")
ax.text(880, lnp3[-1], " third limit", fontsize=8, va="center")
ax.set_xlim(715, 930)
ax.set_ylim(-1, 11)
ax.set_yticks([])
ax.set_xlabel(r"$T$ / K")
ax.set_ylabel(r"$\ln p$ (schematic)")
fig.tight_layout()
