"""Schematic chemical potential of the solvent against temperature at constant pressure.
Each line has slope -S_m (S_gas > S_liquid > S_solid). A non-volatile solute that does not enter the
solid lowers the liquid line by RT ln x_A (exaggerated here), so the liquid line meets the solid
line at a lower T (freezing-point depression) and the vapour line at a higher T (boiling-point elevation)."""

import numpy as np
import matplotlib.pyplot as plt

Tf, Tb = 1.0, 2.0          # pure-solvent transition temperatures (arbitrary units)
S_s, S_l, S_g = 1.0, 2.0, 4.0
T = np.linspace(0.45, 2.55, 400)
mu_l = -S_l * (T - Tf)                  # liquid, zero at Tf
mu_s = -S_s * (T - Tf)                  # solid meets liquid at Tf
mu_g = mu_l[np.argmin(abs(T - Tb))] - S_g * (T - Tb)   # gas meets liquid at Tb
d = 0.35                                # lowering of the liquid line (exaggerated)
mu_sln = mu_l - d

Tf2 = Tf - d / (S_l - S_s)
Tb2 = Tb + d / (S_g - S_l)

fig, ax = plt.subplots(figsize=(7, 4.4))
ms = T < 1.45
mg = T > 1.55
ax.plot(T[ms], mu_s[ms], color="C0", lw=1.8, label="solid (pure solvent)")
ax.plot(T, mu_l, color="C2", lw=1.8, label="liquid (pure solvent)")
ax.plot(T, mu_sln, color="C2", lw=1.8, ls="--", label="solvent in solution")
ax.plot(T[mg], mu_g[mg], color="C3", lw=1.8, label="vapour (pure solvent)")
for t, c in [(Tf, "C2"), (Tb, "C2")]:
    ax.axvline(t, color="0.6", lw=0.7, ls=":")
for t in [Tf2, Tb2]:
    ax.axvline(t, color="0.35", lw=0.7, ls=":")
ax.annotate(r"$T_\mathrm{f}$", (Tf2 - 0.1, 1.6), fontsize=10)
ax.annotate(r"$T^*_\mathrm{f}$", (Tf + 0.02, 1.6), fontsize=10)
ax.annotate(r"$T^*_\mathrm{b}$", (Tb - 0.13, 1.6), fontsize=10)
ax.annotate(r"$T_\mathrm{b}$", (Tb2 + 0.02, 1.6), fontsize=10)
ax.annotate("", xy=(0.62, -d + 0.76), xytext=(0.62, 0.76), arrowprops=dict(arrowstyle="->", color="0.4"))
ax.annotate(r"$RT\ln x_\mathrm{A}$", (0.65, 0.55), fontsize=9)
ax.set_xlabel("T (schematic)")
ax.set_ylabel(r"$\mu_\mathrm{A}$ (schematic)")
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0.45, 2.55)
ax.set_ylim(-3.2, 1.9)
ax.legend(frameon=False, fontsize=9, loc="lower left")
fig.tight_layout()
