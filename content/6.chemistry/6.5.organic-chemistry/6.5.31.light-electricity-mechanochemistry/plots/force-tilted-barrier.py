"""How a mechanical force lowers a barrier (Bell model). A pulling force F adds -F x to the potential
energy along the bond coordinate x, tilting the profile: the barrier drops by about F dx, where dx
is the distance from the minimum to the transition state, and k(F) = k0 exp(F dx / kB T).
A force of 1 nN acting over 0.1 nm does 1e-19 J of work per molecule, 60 kJ/mol."""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.05, 0.30, 400)  # nm
NA = 6.02214076e23


fig, ax = plt.subplots(figsize=(6.6, 4.2))
base = 160 * (x / 0.1) ** 2 * np.exp(1 - (x / 0.1) ** 2)  # minimum at 0, top at x = 0.1 nm
for F, c in [(0.0, "C0"), (0.5, "C1"), (1.0, "C3")]:
    work = F * 1e-9 * x * 1e-9 * NA / 1000  # kJ/mol
    u = base - work
    ax.plot(x, u, color=c, lw=2, label=f"F = {F:.1f} nN")
    i = np.argmax(np.where(x < 0.2, u, -1e9))
    ax.plot(x[i], u[i], "o", color=c, ms=4)
ax.set_xlabel("extension of the scissile bond $x$ / nm")
ax.set_ylabel(r"energy / kJ mol$^{-1}$")
ax.axhline(0, color="0.8", lw=0.8)
ax.legend(frameon=False, fontsize=9)
ax.set_xlim(-0.05, 0.3)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
