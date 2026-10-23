"""Acid-effect coefficient of EDTA, lg alpha_Y(H), versus pH, and the Ringbom curve: the lowest pH at
which a metal ion (c_sp = 0.01 mol/L) can be titrated with lg(c K') >= 6, i.e. lg alpha_Y(H) = lg K_MY - 8.
Stability constants: 25 C, I = 0.1 (NIST critical values)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

pKa = [0.0, 1.5, 2.00, 2.69, 6.13, 10.37]


def lg_alpha(pH):
    h = 10.0 ** -pH
    s, term = 1.0, 1.0
    for p in pKa[::-1]:
        term = term * h / 10.0 ** -p
        s = s + term
    return np.log10(s)


metals = {"Bi$^{3+}$": 27.8, "Fe$^{3+}$": 25.1, "Hg$^{2+}$": 21.5, "Cu$^{2+}$": 18.78, "Ni$^{2+}$": 18.4,
          "Pb$^{2+}$": 18.0, "Zn$^{2+}$": 16.50, "Al$^{3+}$": 16.4, "Fe$^{2+}$": 14.30, "Mn$^{2+}$": 13.89,
          "Ca$^{2+}$": 10.65, "Mg$^{2+}$": 8.79}

LEFT = {"Ni$^{2+}$", "Al$^{3+}$", "Fe$^{2+}$"}
pH = np.linspace(0, 13, 600)
fig, ax = plt.subplots(figsize=(6.8, 4.4))
ax.plot(pH, lg_alpha(pH), color="C0", lw=1.8, label=r"lg $\alpha_{\mathrm{Y(H)}}$")
for name, lgK in metals.items():
    pmin = brentq(lambda p: lg_alpha(p) - (lgK - 8), -1, 14)
    ax.plot(pmin, lgK - 8, "o", color="C3", ms=4)
    dx, ha = (-6, "right") if name in LEFT else (6, "left")
    ax.annotate(name, (pmin, lgK - 8), xytext=(dx, -3), textcoords="offset points", fontsize=8, ha=ha)
ax.set_xlabel("pH")
ax.set_ylabel(r"lg $\alpha_{\mathrm{Y(H)}}$")
ax.set_xlim(0, 13)
ax.set_ylim(0, 22)
sec = ax.secondary_yaxis("right", functions=(lambda y: y + 8, lambda y: y - 8))
sec.set_ylabel(r"lg $K_{\mathrm{MY}}$ (minimum pH at $c_{\mathrm{sp}}$ = 0.01 mol L$^{-1}$)")
ax.legend(frameon=False, fontsize=9, loc="upper right")
fig.tight_layout()
