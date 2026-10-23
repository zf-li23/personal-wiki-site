"""Atomic fluorescence intensity versus concentration (log-log, illustrative units).
I_f = Phi * I0 * (1 - exp(-k c)) is linear (slope 1) while k c << 1 and saturates when the
exciting radiation is completely absorbed; re-absorption of the fluorescence on its way out
of the atom cloud (self-absorption) makes the curve bend over at high concentration
(slope -1 in the limit)."""

import numpy as np
import matplotlib.pyplot as plt

c = np.logspace(-4, 2, 400)
k = 1.0
lin = k * c
sat = 1 - np.exp(-k * c)
selfabs = sat / (1 + 0.5 * k * c)  # escape factor of the re-absorbed fluorescence

fig, ax = plt.subplots(figsize=(6.2, 4.4))
ax.loglog(c, lin, color="0.5", lw=1.2, ls="--", label=r"$\Phi I_0 k'c$ (linear)")
ax.loglog(c, sat, color="C0", lw=1.8, label=r"$\Phi I_0(1-\mathrm{e}^{-k'c})$")
ax.loglog(c, selfabs, color="C3", lw=1.8, label="with self-absorption of the fluorescence")
ax.axvline(0.1, color="0.6", lw=0.7, ls=":")
ax.text(0.11, 1.5, r"$k'c = 0.1$", fontsize=8)
ax.set_xlim(1e-4, 1e2)
ax.set_ylim(1e-4, 3)
ax.set_xlabel(r"$k'c$ (concentration, arbitrary units)")
ax.set_ylabel(r"$I_{\mathrm{f}}/(\Phi I_0)$")
ax.legend(fontsize=8, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.92))
fig.tight_layout()
