"""Schematic T-x diagrams of solid-liquid equilibria, built from ideal-solubility liquidus
curves (fully dissociated liquid for the compounds). (a) A compound C = AB with a congruent
melting point. (b) A compound with an incongruent melting point (peritectic). (c) Complete
solid solubility, computed for Cu-Ni as an ideal solid and liquid solution. (d) Partial
solid solubility with a eutectic (schematic solvus)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

R = 8.314462618


def T_ideal(a, Tm, H):
    """Liquidus temperature at which the pure solid with (Tm, H) is in equilibrium with activity a."""
    return 1 / (1 / Tm - R * np.log(a) / H)


def cross(f, g, lo, hi):
    return brentq(lambda x: f(x) - g(x), lo, hi)


fig, axes = plt.subplots(2, 2, figsize=(8.8, 7.0))
lw = 1.6

# (a) congruent compound AB
ax = axes[0, 0]
TA = lambda x: T_ideal(1 - x, 600, 15e3)
TB = lambda x: T_ideal(x, 560, 14e3)
TC = lambda x: T_ideal(4 * x * (1 - x), 680, 25e3)
x1 = cross(TA, TC, 0.05, 0.5)
x2 = cross(TC, TB, 0.5, 0.95)
for f, a, b in [(TA, 0, x1), (TC, x1, x2), (TB, x2, 1)]:
    xx = np.linspace(a, b, 200)
    ax.plot(xx, f(xx), color="C0", lw=lw)
E1, E2 = TA(x1), TB(x2)
ax.plot([0, 0.5], [E1, E1], color="C0", lw=lw)
ax.plot([0.5, 1], [E2, E2], color="C0", lw=lw)
ax.plot([0.5, 0.5], [400, 680], color="C0", lw=lw)
ax.plot([0.5], [680], "o", color="C3", ms=4)
ax.text(0.5, 688, "D (congruent m.p.)", ha="center", fontsize=8)
ax.text(x1, E1 - 14, r"$\mathrm{E}_1$", ha="center", fontsize=8)
ax.text(x2, E2 - 14, r"$\mathrm{E}_2$", ha="center", fontsize=8)
ax.text(0.45, 650, "l", fontsize=10)
ax.text(0.31, 600, "l + C(s)", fontsize=7.5)
ax.text(0.53, 590, "l + C(s)", fontsize=7.5)
ax.text(0.1, 440, "A(s) + C(s)", fontsize=7.5)
ax.text(0.6, 440, "C(s) + B(s)", fontsize=7.5)
ax.set_title("(a) compound with a congruent melting point", fontsize=9)
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(["A", "AB", "B"])
ax.set_ylim(400, 710)

# (b) incongruent compound AB (peritectic)
ax = axes[0, 1]
TA = lambda x: T_ideal(1 - x, 900, 25e3)
TB = lambda x: T_ideal(x, 620, 15e3)
TC = lambda x: T_ideal(4 * x * (1 - x), 700, 50e3)
xM = cross(TA, TC, 0.5, 0.75)
xE = cross(TC, TB, xM, 0.99)
TM, TE = TA(xM), TB(xE)
for f, a, b in [(TA, 0, xM), (TC, xM, xE), (TB, xE, 1)]:
    xx = np.linspace(a, b, 200)
    ax.plot(xx, f(xx), color="C0", lw=lw)
ax.plot(np.linspace(0.42, 0.5, 30), TC(np.linspace(0.42, 0.5, 30)), color="C0", lw=0.9, ls=":")
ax.plot([0, xM], [TM, TM], color="C0", lw=lw)
ax.plot([0.5, 1], [TE, TE], color="C0", lw=lw)
ax.plot([0.5, 0.5], [450, TM], color="C0", lw=lw)
ax.plot([0.5, xM], [TM, TM], "o", color="C3", ms=4)
ax.text(0.47, TM + 8, "D", ha="right", fontsize=8)
ax.text(xM + 0.01, TM + 8, "M", fontsize=8)
ax.text(xE, TE - 16, "E", ha="center", fontsize=8)
ax.text(0.7, 800, "l", fontsize=10)
ax.text(0.08, 720, "l + A(s)", fontsize=7.5)
ax.text(0.52, 618, "l + C(s)", fontsize=7.5)
ax.text(0.08, 560, "A(s) + C(s)", fontsize=7.5)
ax.text(0.62, 500, "C(s) + B(s)", fontsize=7.5)
ax.set_title("(b) compound with an incongruent melting point", fontsize=9)
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(["A", "AB", "B"])
ax.set_ylim(450, 920)

# (c) complete solid solution: ideal Cu-Ni
ax = axes[1, 0]
TCu, HCu, TNi, HNi = 1357.77, 13.26e3, 1728.0, 17.48e3
T = np.linspace(TCu, TNi, 300)
kCu = np.exp(-HCu / R * (1 / T - 1 / TCu))
kNi = np.exp(-HNi / R * (1 / T - 1 / TNi))
xs_ni = (1 - kCu) / (kNi - kCu)
xl_ni = kNi * xs_ni
ax.plot(xl_ni, T, color="C0", lw=lw, label="liquidus")
ax.plot(xs_ni, T, color="C3", lw=lw, label="solidus")
ax.text(0.25, 1650, "l", fontsize=10)
ax.annotate("l + s", (0.5, 1548), xytext=(0.58, 1490), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax.text(0.75, 1450, "s (solid solution)", fontsize=8, ha="center")
ax.set_title("(c) complete solid solubility (ideal Cu-Ni)", fontsize=9)
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(["Cu", "0.5", "Ni"])
ax.set_ylabel(r"$T\,/\,\mathrm{K}$")
ax.set_ylim(1300, 1780)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")

# (d) partial solid solubility with a eutectic (schematic)
ax = axes[1, 1]
TA = lambda x: T_ideal(1 - x, 1235, 11.3e3)
TB = lambda x: T_ideal(x, 1358, 13.3e3)
xE = cross(TA, TB, 0.05, 0.95)
TE = TA(xE)
xa_E, xb_E = 0.14, 0.95
xl = np.linspace(0, xE, 200)
ax.plot(xl, TA(xl), color="C0", lw=lw)
ax.plot(xl * xa_E / xE, TA(xl), color="C3", lw=lw)
xl = np.linspace(xE, 1, 200)
ax.plot(xl, TB(xl), color="C0", lw=lw)
ax.plot(1 - (1 - xl) * (1 - xb_E) / (1 - xE), TB(xl), color="C3", lw=lw)
ax.plot([xa_E, xb_E], [TE, TE], color="C0", lw=lw)
T = np.linspace(700, TE, 100)
ax.plot(xa_E * np.exp(-6000 * (1 / T - 1 / TE)), T, color="C2", lw=1.2)
ax.plot(1 - (1 - xb_E) * np.exp(-6000 * (1 / T - 1 / TE)), T, color="C2", lw=1.2)
ax.plot([xE], [TE], "o", color="C3", ms=4)
ax.text(xE, TE - 30, "E", ha="center", fontsize=8)
ax.text(0.45, 1250, "l", fontsize=10)
ax.text(0.01, 950, r"$\alpha$", fontsize=10)
ax.text(0.965, 950, r"$\beta$", fontsize=10)
ax.text(0.45, 745, r"$\alpha + \beta$", fontsize=9)
ax.text(0.1, 1130, r"l + $\alpha$", fontsize=8)
ax.text(0.72, 1130, r"l + $\beta$", fontsize=8)
ax.set_title("(d) partial solid solubility, eutectic", fontsize=9)
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(["A", "0.5", "B"])
ax.set_ylim(700, 1400)

for ax in axes.flat:
    ax.set_xlim(0, 1)
    ax.set_xlabel(r"$x_\mathrm{B}$")
for ax in axes[:, 0]:
    ax.set_ylabel(r"$T\,/\,\mathrm{K}$")
fig.tight_layout()
