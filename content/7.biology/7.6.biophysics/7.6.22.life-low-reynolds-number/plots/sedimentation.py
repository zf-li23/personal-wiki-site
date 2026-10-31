"""Gravity, buoyancy and thermal motion. A: the sedimentation length l_g = kB T / (Delta rho V g)
of spheres with a density excess Delta rho = 100 kg/m^3 (a protein, a bacterium, a yeast cell),
compared with their radius: below a radius of about 1 um, thermal motion keeps particles
suspended over heights larger than themselves. B: Stokes settling speed v = 2 Delta rho g a^2 /
(9 eta) of a cyanobacterial cell (radius 2.5 um) and of a colony (radius 50 um) as a function of
the volume fraction of gas vesicles (effective density about 120 kg/m^3, cytoplasm 1050 kg/m^3,
water 998 kg/m^3); negative speeds mean floating. Neutral buoyancy at about 5.6 %."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
kT, g, eta = 4.1e-21, 9.8, 1e-3
fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.2))
fig.subplots_adjust(wspace=0.4, left=0.09, right=0.97, bottom=0.18, top=0.87)

ax = axs[0]
a = np.logspace(-9, -4.5, 300)
lg = kT / (100 * 4 / 3 * np.pi * a**3 * g)
ax.plot(a * 1e6, lg * 1e6, color=charts.line("dna"), lw=1.7, label=r"$\ell_g = k_{\mathrm{B}}T/\Delta m\,g$")
ax.plot(a * 1e6, a * 1e6, color=P.muted(), lw=1.0, ls="--", label=r"$\ell_g = a$")
astar = (3 * kT / (4 * np.pi * 100 * g)) ** 0.25
ax.plot(astar * 1e6, astar * 1e6, "o", color=charts.line("negative"), ms=5)
for r, txt in ((2.5e-9, "protein"), (0.7e-6, "bacterium"), (2.5e-6, "yeast")):
    ax.axvline(r * 1e6, color=P.muted(), lw=0.5, ls=":")
    ax.text(r * 1e6 * 1.15, 1e9, txt, rotation=90, fontsize=bio.core.FONT["tiny"], color=P.ink(), va="top")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"radius a / $\mu$m", r"sedimentation length / $\mu$m")
charts.title(ax, "A  Where gravity starts to matter")

ax = axs[1]
fv = np.linspace(0, 0.12, 200)
rho = (1 - fv) * 1050 + fv * 120
for rad, tok, lab in ((2.5e-6, "bacterium", r"single cell, a = 2.5 $\mu$m"), (50e-6, "dna", r"colony, a = 50 $\mu$m")):
    v = 2 * (rho - 998) * g * rad**2 / (9 * eta)
    ax.plot(fv * 100, v * 1e6 * 3600 / 1e3, color=charts.line(tok), lw=1.7, label=lab)
ax.axhline(0, color=P.muted(), lw=0.7)
ax.axvline(52 / 930 * 100, color=P.muted(), lw=0.7, ls=":")
ax.set_yscale("symlog", linthresh=0.01)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "gas vesicle volume / %", r"settling speed / mm h$^{-1}$")
charts.title(ax, "B  Floating with gas vesicles")
