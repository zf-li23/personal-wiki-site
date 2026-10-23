"""Plate height against linear velocity in HPLC for packings of 5, 3 and 1.7 um, written in
reduced form h = H/dp = A + B/nu + C nu with nu = u dp/Dm (A = 1, B = 2, C = 0.1; Dm = 1e-9
m^2/s, a small molecule in water-acetonitrile). The minimum plate height is about 1.9 dp
and the optimum velocity scales as 1/dp; smaller particles also make the curve flatter at
high velocity, so they can be run fast without losing efficiency (the basis of UHPLC)."""

import numpy as np
import matplotlib.pyplot as plt

A, B, C, Dm = 1.0, 2.0, 0.1, 1.0e-9
u = np.linspace(0.05, 10, 500) * 1e-3          # m/s
fig, ax = plt.subplots(figsize=(6.6, 4.2))
for dp, col in [(5e-6, "C0"), (3e-6, "C2"), (1.7e-6, "C3")]:
    nu = u * dp / Dm
    H = dp * (A + B / nu + C * nu)
    ax.plot(u * 1e3, H * 1e6, color=col, lw=1.7, label=rf"$d_\mathrm{{p}}$ = {dp * 1e6:g} $\mu$m")
    uo = Dm / dp * np.sqrt(B / C)
    ax.plot([uo * 1e3], [dp * (A + 2 * np.sqrt(B * C)) * 1e6], "o", color=col, ms=4)
ax.set_xlim(0, 10)
ax.set_ylim(0, 25)
ax.set_xlabel(r"linear velocity $u$ / (mm s$^{-1}$)")
ax.set_ylabel(r"plate height $H$ / $\mu$m")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
