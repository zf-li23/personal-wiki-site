"""Left: van Deemter curve H = A + B/u + C u of a packed GC column and its three terms
(A = 0.30 mm, B = 6.0 mm cm/s, C = 0.030 mm s/cm, illustrative values); the minimum lies at
u_opt = sqrt(B/C) with H_min = A + 2 sqrt(BC). Right: Golay curves (A = 0) of a 0.25 mm i.d.
open-tubular column for N2, He and H2 carrier gas. The diffusion coefficient of the solute
in the gas, D_m = 0.063, 0.13 and 0.20 cm^2/s, scales B up and the mobile-phase mass-transfer
term down, so the optimum moves to higher velocity and the curve becomes flatter."""

import numpy as np
import matplotlib.pyplot as plt

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 3.8))

A, B, C = 0.30, 6.0, 0.030           # mm, mm cm/s, mm s/cm
u = np.linspace(0.8, 40, 400)        # cm/s
a1.plot(u, A + B / u + C * u, color="0.1", lw=1.8, label=r"$H = A + B/u + Cu$")
a1.plot(u, A + 0 * u, color="C0", lw=1.2, ls="--", label=r"$A$ (eddy diffusion)")
a1.plot(u, B / u, color="C2", lw=1.2, ls="--", label=r"$B/u$ (longitudinal diffusion)")
a1.plot(u, C * u, color="C3", lw=1.2, ls="--", label=r"$Cu$ (mass transfer)")
uo = np.sqrt(B / C)
Hm = A + 2 * np.sqrt(B * C)
a1.plot([uo], [Hm], "o", color="0.1", ms=5)
a1.annotate(rf"$u_\mathrm{{opt}}$ = {uo:.1f} cm/s, $H_\mathrm{{min}}$ = {Hm:.2f} mm", (uo, Hm),
            xytext=(uo + 3, Hm - 0.45), fontsize=8, arrowprops=dict(arrowstyle="-", color="0.5"))
a1.set_ylim(0, 2.4)
a1.set_xlim(0, 40)
a1.set_xlabel(r"linear velocity $u$ / (cm s$^{-1}$)")
a1.set_ylabel(r"plate height $H$ / mm")
a1.set_title("packed column", fontsize=10)
a1.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 1.0))

dc, k = 0.025, 5.0                    # column diameter (cm), retention factor
f = (1 + 6 * k + 11 * k ** 2) / (96 * (1 + k) ** 2)
Cs = 2.0e-4                           # stationary-phase term, s (thin film)
u = np.linspace(2, 100, 500)
for gas, Dm, col in [("N$_2$", 0.063, "C0"), ("He", 0.13, "C2"), ("H$_2$", 0.20, "C3")]:
    Bg, Cg = 2 * Dm, f * dc ** 2 / Dm + Cs
    H = (Bg / u + Cg * u) * 10        # mm
    a2.plot(u, H, color=col, lw=1.6, label=gas)
    uo = np.sqrt(Bg / Cg)
    a2.plot([uo], [2 * np.sqrt(Bg * Cg) * 10], "o", color=col, ms=4)
a2.set_ylim(0, 1.0)
a2.set_xlim(0, 100)
a2.set_xlabel(r"linear velocity $u$ / (cm s$^{-1}$)")
a2.set_ylabel(r"plate height $H$ / mm")
a2.set_title("open-tubular column, 0.25 mm i.d.", fontsize=10)
a2.legend(frameon=False, fontsize=9)
fig.tight_layout()
