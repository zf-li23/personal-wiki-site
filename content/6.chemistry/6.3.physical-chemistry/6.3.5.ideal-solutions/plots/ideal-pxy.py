"""Vapour-liquid equilibrium of an ideal liquid mixture at constant T (p*_A = 40 kPa, p*_B = 120 kPa).
Left: partial and total pressures against the liquid composition (Raoult's law).
Right: the liquid (bubble-point) line and the vapour (dew-point) line; a vapour with y_A = 0.4 is
compressed isothermally: it starts to condense at the dew point and is fully liquid at the bubble point."""

import numpy as np
import matplotlib.pyplot as plt

pA, pB = 40.0, 120.0
x = np.linspace(0, 1, 201)          # mole fraction of B in the liquid
p_liq = pA * (1 - x) + pB * x
y = pB * x / p_liq                  # mole fraction of B in the vapour

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, pA * (1 - x), color="C0", lw=1.6, label=r"$p_\mathrm{A} = p^*_\mathrm{A}x_\mathrm{A}$")
ax1.plot(x, pB * x, color="C1", lw=1.6, label=r"$p_\mathrm{B} = p^*_\mathrm{B}x_\mathrm{B}$")
ax1.plot(x, p_liq, color="C2", lw=2.0, label=r"$p = p_\mathrm{A} + p_\mathrm{B}$")
ax1.set_xlabel(r"$x_\mathrm{B}$ (liquid)")
ax1.set_ylabel(r"$p$ / kPa")
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 130)
ax1.set_title("Raoult's law for both components", fontsize=10)
ax1.legend(frameon=False, fontsize=9, loc="upper left")

ax2.plot(x, p_liq, color="C2", lw=2.0, label="liquid line $p(x_\\mathrm{B})$")
ax2.plot(y, p_liq, color="C3", lw=2.0, label="vapour line $p(y_\\mathrm{B})$")
yB = 0.6
p_dew = 1 / ((1 - yB) / pA + yB / pB)
p_bub = pA * (1 - yB) + pB * yB
ax2.plot([yB, yB], [30, p_bub + 15], color="0.45", lw=1.0, ls="--")
ax2.annotate("", xy=(yB, p_bub + 8), xytext=(yB, 35), arrowprops=dict(arrowstyle="->", color="0.45"))
x_dew = yB * p_dew / pB
y_bub = pB * yB / p_bub
ax2.plot([x_dew, yB], [p_dew, p_dew], color="C0", lw=1.0)
ax2.plot([yB, y_bub], [p_bub, p_bub], color="C0", lw=1.0)
ax2.plot([x_dew, yB], [p_dew, p_dew], "o", color="C0", ms=4)
ax2.plot([yB, y_bub], [p_bub, p_bub], "o", color="C0", ms=4)
ax2.annotate(f"dew point {p_dew:.1f} kPa:\nfirst liquid $x_\\mathrm{{B}}$ = {x_dew:.3f}", (0.02, p_dew + 6), fontsize=8.5)
ax2.annotate(f"bubble point {p_bub:.0f} kPa:\nlast vapour $y_\\mathrm{{B}}$ = {y_bub:.3f}", (0.36, p_bub + 10), fontsize=8.5)
ax2.text(0.86, 64, "vapour", fontsize=10)
ax2.text(0.08, 110, "liquid", fontsize=10)
ax2.set_xlabel(r"$x_\mathrm{B}$ or $y_\mathrm{B}$")
ax2.set_ylabel(r"$p$ / kPa")
ax2.set_xlim(0, 1)
ax2.set_ylim(30, 130)
ax2.set_title("isothermal compression of a vapour with $y_\\mathrm{B}$ = 0.6", fontsize=10)
ax2.legend(frameon=False, fontsize=9, loc="lower right")
fig.tight_layout()
