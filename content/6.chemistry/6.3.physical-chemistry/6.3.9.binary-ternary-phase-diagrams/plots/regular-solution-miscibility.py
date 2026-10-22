"""Liquid-liquid phase separation of a symmetric regular solution,
Delta_mix G_m / RT = x ln x + (1-x) ln(1-x) + (W/RT) x (1-x).
Left: Delta_mix G_m against x for several W/RT; above W/RT = 2 the curve has two minima and
the common tangent picks out the conjugate compositions. Right: the coexistence (binodal)
curve and the spinodal in reduced temperature T/T_c with T_c = W/(2R)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

x = np.linspace(1e-4, 1 - 1e-4, 1000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.9))

for w, c in [(0.0, "C0"), (1.5, "C2"), (2.0, "C1"), (2.8, "C3")]:
    g = x * np.log(x) + (1 - x) * np.log(1 - x) + w * x * (1 - x)
    ax1.plot(x, g, color=c, lw=1.6, label=rf"$W/RT = {w:g}$")
w = 2.8
xb = brentq(lambda z: np.log(z / (1 - z)) - w * (2 * z - 1), 1e-6, 0.4999)
gb = xb * np.log(xb) + (1 - xb) * np.log(1 - xb) + w * xb * (1 - xb)
ax1.plot([xb, 1 - xb], [gb, gb], color="0.4", lw=1.0, ls="--")
ax1.plot([xb, 1 - xb], [gb, gb], "o", color="C3", ms=4)
ax1.text(0.5, gb - 0.035, "common tangent", ha="center", fontsize=8, color="0.4")
ax1.set_xlabel(r"$x_\mathrm{B}$")
ax1.set_ylabel(r"$\Delta_\mathrm{mix}G_\mathrm{m}\,/\,RT$")
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.75, 0.15)
ax1.legend(frameon=False, fontsize=7.5, loc="lower right")

xs = np.linspace(0.001, 0.4999, 400)
tb = 2 * (2 * xs - 1) / np.log(xs / (1 - xs))     # binodal T/Tc
ts = 4 * xs * (1 - xs)                              # spinodal T/Tc
ax2.plot(np.r_[xs, 1 - xs[::-1]], np.r_[tb, tb[::-1]], color="C0", lw=1.8, label="coexistence curve")
ax2.plot(np.r_[xs, 1 - xs[::-1]], np.r_[ts, ts[::-1]], color="C3", lw=1.2, ls="--", label="spinodal")
ax2.plot([0.5], [1.0], "o", color="C2", ms=5)
ax2.annotate("upper critical solution\ntemperature", (0.5, 1.0), xytext=(0.6, 1.08), fontsize=8,
             arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
t1 = 0.8
x1 = brentq(lambda z: 2 * (2 * z - 1) / np.log(z / (1 - z)) - t1, 1e-6, 0.4999)
ax2.plot([x1, 1 - x1], [t1, t1], color="0.4", lw=1.0)
ax2.plot([x1, 1 - x1], [t1, t1], "o", color="0.3", ms=4)
ax2.text(x1 - 0.02, t1 + 0.02, r"$\mathrm{l}_1$", ha="right", fontsize=9)
ax2.text(1 - x1 + 0.02, t1 + 0.02, r"$\mathrm{l}_2$", fontsize=9)
ax2.text(0.5, 0.45, "two liquid phases", ha="center", fontsize=9)
ax2.text(0.04, 1.12, "one liquid phase", fontsize=9)
ax2.set_xlabel(r"$x_\mathrm{B}$")
ax2.set_ylabel(r"$T\,/\,T_\mathrm{c}$")
ax2.set_xlim(0, 1)
ax2.set_ylim(0.3, 1.2)
ax2.legend(frameon=False, fontsize=8, loc="lower left")
fig.tight_layout()
