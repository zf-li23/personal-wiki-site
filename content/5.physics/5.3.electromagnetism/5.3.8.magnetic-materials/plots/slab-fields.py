"""H and B across an infinite slab of linear magnetic material carrying a uniform current density."""

import numpy as np
import matplotlib.pyplot as plt

h = 1.0      # half thickness
J0 = 1.0     # free current density along +z
y = np.linspace(-3, 3, 1201)
inside = np.abs(y) <= h

# x components (field along -x above the slab for current along +z)
H = np.where(inside, -J0 * y, -J0 * h * np.sign(y))

fig, ax = plt.subplots(figsize=(7, 4.2))
for mur, c in [(1.0, "C0"), (3.0, "C1"), (6.0, "C3")]:
    B = np.where(inside, mur * H, H)  # in units of mu0 J0 h
    ax.plot(y, B, color=c, lw=1.8, label=f"mu_r = {mur:g}" + (" (B = mu0 H everywhere)" if mur == 1 else ""))
ax.axvspan(-h, h, color="0.85", alpha=0.5, lw=0)
ax.axhline(0, color="0.6", lw=0.7)
ax.set_xlabel("y / h")
ax.set_ylabel("B_x / (mu0 J0 h)")
ax.set_title("H is fixed by the free current; B jumps at the faces (H_t continuous)", fontsize=10)
ax.legend(fontsize=8)
fig.tight_layout()
