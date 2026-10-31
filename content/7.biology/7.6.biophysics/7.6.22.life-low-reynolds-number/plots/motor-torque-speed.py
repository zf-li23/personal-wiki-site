"""Torque-speed curve of the bacterial flagellar motor (E. coli, about 23 degC; schematic of the
measurements of Chen and Berg 2000 with beads and filament stubs of different sizes). The torque is
nearly constant, about 1300 pN nm, up to a knee near 170 Hz and then falls linearly to zero near
300 Hz. Each load is a line through the origin, torque = zeta omega, with zeta the rotational drag
coefficient (8 pi eta r^3 for a bead of radius r (diameters given), plus the drag of the stub); the motor runs where
the line meets the curve. Large loads (beads, a swimming cell's flagellar bundle) operate on the
plateau, where speed is set by the load and the motor is near stall; small beads probe the
steep, rate-limited region. B: mechanical power output tau omega along the curve."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
tau0, fk, f0 = 1300.0, 170.0, 300.0
f = np.linspace(0, f0, 400)
tau = np.where(f < fk, tau0 * (1 - 0.1 * f / fk), tau0 * 0.9 * (f0 - f) / (f0 - fk))
eta = 1e-3

fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.18, top=0.87)
ax = axs[0]
ax.plot(f, tau, color=charts.line("bacterium"), lw=2)
for r, lab in ((0.5e-6, r"1 $\mu$m bead"), (0.25e-6, r"0.5 $\mu$m bead"), (0.15e-6, r"0.3 $\mu$m bead"), (30e-9, "60 nm gold")):
    zeta = 8 * np.pi * eta * r**3 + 2e-22  # N m s; second term: drag of the hook and stub
    w = 2 * np.pi * f
    load = zeta * w * 1e21  # pN nm
    ax.plot(f, load, color=P.muted(), lw=0.8, ls="--")
    i = np.argmin(np.abs(load - tau))
    ax.plot(f[i], tau[i], "o", color=charts.line("blood"), ms=4)
    ax.text(f[i] + 4, tau[i] + 40, lab, fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axvspan(90, 130, color=P.fill("dna"), alpha=0.3, lw=0)
ax.text(92, 200, "swimming\ncells", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_ylim(0, 1600); ax.set_xlim(0, 320)
charts.style_axes(ax, "rotation rate / Hz", "torque / pN nm")
charts.title(ax, "A  Plateau, knee and linear fall")

ax = axs[1]
Pw = tau * 1e-21 * 2 * np.pi * f
ax.plot(f, Pw * 1e15, color=charts.line("bacterium"), lw=1.8)
ax.axhline(6 * np.pi * eta * 1e-6 * (25e-6) ** 2 * 1e15, color=charts.line("negative"), lw=0.9, ls=":")
ax.text(5, 0.06, "useful power: dragging the body at 25 $\\mu$m/s", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(ax, "rotation rate / Hz", "power output / fW")
charts.title(ax, "B  About 1 fW per motor")
