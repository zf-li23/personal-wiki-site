"""Potential step to the diffusion-limited plateau at a planar electrode (semi-infinite linear
diffusion, D = 1.0e-9 m2/s, bulk concentration 1.0 mol/m3, z = 1).
Left: concentration profiles c/c* = erf(x / (2 sqrt(D t))) at several times.
Right: Cottrell current j = z F c* sqrt(D / (pi t)), which falls as t^(-1/2) (inset: j against
t^(-1/2) is a straight line through the origin)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

D, c0, F = 1.0e-9, 1.0, 96485.33212
x = np.linspace(0, 300e-6, 400)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
for t, col in [(0.1, "C0"), (1.0, "C1"), (10.0, "C3"), (60.0, "C4")]:
    ax.plot(x * 1e6, erf(x / (2 * np.sqrt(D * t))), color=col, lw=1.7, label=f"t = {t:g} s")
    ax.plot([0, np.sqrt(np.pi * D * t) * 1e6], [0, 1], color=col, lw=0.8, ls=":")
ax.set_xlim(0, 300)
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"distance from electrode $x$ / $\mu$m")
ax.set_ylabel(r"$c/c^*$")
ax.set_title(r"dotted: tangent at $x=0$ reaches $c^*$ at $\delta = \sqrt{\pi D t}$", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="lower right")

ax = axes[1]
t = np.linspace(0.05, 10, 400)
j = F * c0 * np.sqrt(D / (np.pi * t))
ax.plot(t, j, color="k", lw=1.8)
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_xlabel(r"$t$ / s")
ax.set_ylabel(r"$|j|$ / (A m$^{-2}$)")
ax.set_title(r"Cottrell: $|j| = zFc^*\sqrt{D/(\pi t)}$", fontsize=10)
ins = ax.inset_axes([0.45, 0.42, 0.5, 0.5])
ins.plot(t**-0.5, j, color="C0", lw=1.4)
ins.set_xlabel(r"$t^{-1/2}$ / s$^{-1/2}$", fontsize=8)
ins.set_ylabel(r"$|j|$", fontsize=8)
ins.tick_params(labelsize=7)
ins.set_xlim(0, 4.6)
ins.set_ylim(0, 8)
fig.tight_layout()
