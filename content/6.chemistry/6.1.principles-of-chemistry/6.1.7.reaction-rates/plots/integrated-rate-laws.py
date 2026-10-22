"""Zero-, first- and second-order reactions with the same initial concentration and initial rate:
c-t curves and the three linearized plots."""

import numpy as np
import matplotlib.pyplot as plt

c0 = 1.0
v0 = 0.1           # common initial rate, mol L^-1 s^-1
k0, k1, k2 = v0, v0 / c0, v0 / c0**2
t = np.linspace(0, 30, 400)

cz = np.clip(c0 - k0 * t, 0, None)
c1 = c0 * np.exp(-k1 * t)
c2 = c0 / (1 + k2 * c0 * t)

fig, axs = plt.subplots(1, 4, figsize=(13, 3.4))
axs[0].plot(t, cz, color="C0", label="zero order")
axs[0].plot(t, c1, color="C1", label="first order")
axs[0].plot(t, c2, color="C2", label="second order")
axs[0].axhline(c0 / 2, color="0.6", ls=":", lw=1)
axs[0].set_xlabel("t / s")
axs[0].set_ylabel(r"$c$ / (mol L$^{-1}$)")
axs[0].set_title("same $c_0$ and initial rate", fontsize=10)
axs[0].legend(frameon=False, fontsize=8)

tz = t[cz > 0]
axs[1].plot(tz, cz[cz > 0], color="C0")
axs[1].set_title(r"zero order: $c$ vs $t$", fontsize=10)
axs[1].set_ylabel(r"$c$")
axs[2].plot(t, np.log(c1), color="C1")
axs[2].set_title(r"first order: $\ln c$ vs $t$", fontsize=10)
axs[2].set_ylabel(r"$\ln c$")
axs[3].plot(t, 1 / c2, color="C2")
axs[3].set_title(r"second order: $1/c$ vs $t$", fontsize=10)
axs[3].set_ylabel(r"$1/c$")
for ax in axs[1:]:
    ax.set_xlabel("t / s")
fig.tight_layout()
