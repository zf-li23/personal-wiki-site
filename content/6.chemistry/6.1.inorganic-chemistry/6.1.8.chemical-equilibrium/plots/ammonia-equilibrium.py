"""Ammonia synthesis N2 + 3 H2 <=> 2 NH3: van 't Hoff plot of ln K0 against 1/T, and the equilibrium
mole fraction of NH3 for a 1:3 feed at several total pressures. Ideal gases; Delta_r H0 and Delta_r S0
taken as constant at their 298.15 K values (CRC Handbook data), so the numbers are estimates."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

R = 8.314
dH = 2 * -45.9e3                       # J mol^-1
dS = 2 * 192.8 - 191.6 - 3 * 130.7     # J mol^-1 K^-1


def K(T):
    return np.exp(-(dH - T * dS) / (R * T))


def x_nh3(T, p):
    """Equilibrium NH3 mole fraction; p in units of p0 = 1 bar; feed 1 mol N2 + 3 mol H2."""
    f = lambda a: (2 * a) ** 2 * (4 - 2 * a) ** 2 / ((1 - a) * (3 - 3 * a) ** 3) / p**2 - K(T)
    a = brentq(f, 1e-14, 1 - 1e-12)
    return 2 * a / (4 - 2 * a)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
T = np.linspace(300, 900, 300)
ax1.plot(1000 / T, np.log(K(T)), color="C0", lw=1.8)
ax1.axhline(0, color="0.6", lw=0.8, ls=":")
ax1.annotate(r"slope $= -\Delta_\mathrm{r}H^\circ_\mathrm{m}/R > 0$", (1.6, 4), fontsize=10)
ax1.annotate(rf"$K^\circ = 1$ at $T \approx$ {dH / dS:.0f} K", (2.2, -2.5), fontsize=9)
ax1.set_xlabel(r"$10^3\,\mathrm{K}/T$")
ax1.set_ylabel(r"$\ln K^\circ$")
ax1.set_title("van 't Hoff plot (exothermic reaction)", fontsize=10)

T2 = np.linspace(500, 900, 200)
for p, col in [(1, "C0"), (10, "C1"), (100, "C2"), (300, "C3")]:
    ax2.plot(T2, [x_nh3(t, p) for t in T2], color=col, lw=1.6, label=f"p = {p} bar")
ax2.set_xlabel("T / K")
ax2.set_ylabel(r"equilibrium $x(\mathrm{NH_3})$")
ax2.set_title("lower T and higher p favour NH3", fontsize=10)
ax2.legend(frameon=False, fontsize=9)
fig.tight_layout()
