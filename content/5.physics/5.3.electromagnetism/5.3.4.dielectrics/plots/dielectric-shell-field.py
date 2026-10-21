"""Conducting sphere (radius R1, free charge q0) inside a dielectric shell (R1 < r < R2, relative permittivity eps_r).
D is continuous; E and P jump at the dielectric surfaces because of the bound surface charges."""

import numpy as np
import matplotlib.pyplot as plt

R1, R2, eps_r = 1.0, 2.0, 3.0
r = np.linspace(0.01, 4.0, 2000)

# fields in units of q0 / (4 pi eps0 R1^2) for E, q0 / (4 pi R1^2) for D and P
D = np.where(r > R1, 1.0 / r**2, 0.0)
E = np.where(r > R2, 1.0 / r**2, np.where(r > R1, 1.0 / (eps_r * r**2), 0.0))
P = np.where((r > R1) & (r < R2), (1 - 1 / eps_r) / r**2, 0.0)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(r, D, lw=2, label=r"$D \,/\, (q_0/4\pi R_1^2)$")
ax.plot(r, E, lw=2, ls="--", label=r"$E \,/\, (q_0/4\pi\varepsilon_0 R_1^2)$")
ax.plot(r, P, lw=1.6, ls=":", label=r"$P \,/\, (q_0/4\pi R_1^2)$")
ax.axvspan(R1, R2, color="C2", alpha=0.12, lw=0)
ax.text((R1 + R2) / 2, 0.55, rf"dielectric, $\varepsilon_{{\mathrm{{r}}}} = {eps_r:g}$", ha="center", fontsize=9)
ax.axvspan(0, R1, color="0.5", alpha=0.15, lw=0)
ax.text(R1 / 2, 0.55, "conductor", ha="center", fontsize=9)
ax.set_xlim(0, 4)
ax.set_ylim(0, 1.05)
ax.set_xticks([0, R1, R2, 3, 4], ["0", r"$R_1$", r"$R_2$", r"$3R_1$", r"$4R_1$"])
ax.set_xlabel(r"$r$")
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
