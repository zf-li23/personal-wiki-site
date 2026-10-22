"""Primary kinetic salt effect in water at 25 C: lg(k/k0) = 2 A zA zB sqrt(I) with
A = 0.509 (kg/mol)^(1/2) (Bronsted-Bjerrum equation with the Debye-Hueckel limiting law)."""

import numpy as np
import matplotlib.pyplot as plt

A = 0.509
sI = np.linspace(0, 0.3, 50)
fig, ax = plt.subplots(figsize=(6, 4))
for i, z in enumerate([4, 2, 1, 0, -1, -2]):
    ax.plot(sI, 2 * A * z * sI, color=f"C{i}", label=rf"$z_{{\mathrm{{A}}}}z_{{\mathrm{{B}}}} = {z}$")
ax.axvspan(0.1, 0.3, color="0.5", alpha=0.12, lw=0)
ax.text(0.2, -0.55, "limiting law\nunreliable", ha="center", fontsize=8, color="0.4")
ax.set_xlabel(r"$\sqrt{I_b/b^\circ}$")
ax.set_ylabel(r"$\lg(k/k_0)$")
ax.legend(frameon=False, fontsize=8, ncol=2)
fig.tight_layout()
