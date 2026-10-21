"""Lennard-Jones potential and force in reduced units (epsilon = sigma = 1)."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.92, 3.0, 600)
Ep = 4 * (r**-12 - r**-6)
f = 4 * (12 * r**-13 - 6 * r**-7)  # f = -dEp/dr
r0 = 2 ** (1 / 6)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6), sharex=True)
ax1.plot(r, Ep, color="C0", lw=2)
ax1.axhline(0, color="0.5", lw=0.8)
ax1.axvline(r0, color="0.5", lw=0.8, ls=":")
ax1.plot([r0], [-1], "o", color="C3")
ax1.annotate("equilibrium r0, depth epsilon", (r0, -1), (1.6, -0.6),
             arrowprops=dict(arrowstyle="->", color="0.4"))
ax1.set_ylim(-1.3, 1.5)
ax1.set_ylabel("E_p / epsilon")
ax1.set_title("Lennard-Jones potential  E_p = 4 epsilon [(sigma/r)^12 - (sigma/r)^6]")

ax2.plot(r, f, color="C1", lw=2)
ax2.axhline(0, color="0.5", lw=0.8)
ax2.axvline(r0, color="0.5", lw=0.8, ls=":")
ax2.text(1.0, 2.0, "repulsive (f > 0)")
ax2.text(1.7, -1.6, "attractive (f < 0)")
ax2.set_ylim(-3, 4)
ax2.set_xlabel("r / sigma")
ax2.set_ylabel("f sigma / epsilon")
fig.tight_layout()
