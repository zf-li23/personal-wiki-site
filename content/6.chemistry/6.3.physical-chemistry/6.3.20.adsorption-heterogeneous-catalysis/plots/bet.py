"""BET isotherms and the BET plot. Left: amount adsorbed (in monolayers) against relative
pressure for several values of the BET constant c; c >> 1 gives a type II isotherm with a knee,
c < 1 a type III isotherm. Right: the linear BET form x / (V (1 - x)) against x for N2 data at
77 K (the worked example in the text) with the least-squares line."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001, 0.9, 500)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
for c, col in [(0.5, "C2"), (2, "C1"), (10, "C0"), (100, "C3")]:
    ax1.plot(x, c * x / ((1 - x) * (1 + (c - 1) * x)), color=col, lw=1.8, label=rf"$c_\mathrm{{BET}}$ = {c:g}")
ax1.axhline(1, color="0.6", lw=0.8, ls="--")
ax1.axvspan(0.05, 0.35, color="0.85", alpha=0.5, lw=0)
ax1.set_xlim(0, 0.9)
ax1.set_ylim(0, 5)
ax1.set_xlabel(r"$x = p/p^*$")
ax1.set_ylabel(r"$V^\mathrm{a}/V^\mathrm{a}_\mathrm{mono}$")
ax1.legend(frameon=False, fontsize=8, loc="upper left")

xd = np.array([0.05, 0.08, 0.11, 0.14, 0.17, 0.20, 0.25, 0.30])
V = np.array([22.38, 24.00, 26.05, 27.29, 28.64, 30.01, 31.97, 34.85])
y = xd / (V * (1 - xd))
s, i = np.polyfit(xd, y, 1)
xx = np.linspace(0, 0.32, 50)
ax2.plot(xd, y * 1e3, "o", color="C0", ms=5, label="data")
ax2.plot(xx, (s * xx + i) * 1e3, color="C3", lw=1.4,
         label=rf"fit: $V^\mathrm{{a}}_\mathrm{{mono}}$ = {1/(s+i):.1f} cm$^3$ g$^{{-1}}$, $c_\mathrm{{BET}}$ = {1+s/i:.0f}")
ax2.set_xlim(0, 0.32)
ax2.set_ylim(0, 14)
ax2.set_xlabel(r"$x = p/p^*$")
ax2.set_ylabel(r"$x/[V^\mathrm{a}(1-x)]\,/\,10^{-3}\,\mathrm{g\,cm^{-3}}$")
ax2.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
