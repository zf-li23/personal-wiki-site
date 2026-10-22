"""van 't Hoff plot for 1/2 N2(g) + 3/2 H2(g) <=> NH3(g), 300-1000 K.
Data at 298.15 K: Delta_f H0(NH3) = -45.9 kJ/mol; S0_m: NH3 192.8, N2 191.6, H2 130.7 J/(K mol).
Heat capacities C_p,m = a + bT + c/T^2 (J/(K mol)): NH3 (29.75, 25.10e-3, -1.55e5),
N2 (28.58, 3.77e-3, -0.50e5), H2 (27.28, 3.26e-3, 0.50e5).
Compared: Delta_r C_p = 0 (straight line) and the integrated Kirchhoff corrections."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

R = 8.314
dH0, dS0 = -45.9e3, 192.8 - 0.5 * 191.6 - 1.5 * 130.7
cp = {"NH3": (29.75, 25.10e-3, -1.55e5), "N2": (28.58, 3.77e-3, -0.50e5), "H2": (27.28, 3.26e-3, 0.50e5)}
nu = {"NH3": 1.0, "N2": -0.5, "H2": -1.5}


def dcp(T):
    return sum(nu[s] * (a + b * T + c / T**2) for s, (a, b, c) in cp.items())


def lnK(T, with_cp=True):
    H, S = dH0, dS0
    if with_cp:
        H += quad(dcp, 298.15, T)[0]
        S += quad(lambda t: dcp(t) / t, 298.15, T)[0]
    return -(H - T * S) / (R * T)


T = np.linspace(300, 1000, 120)
l1 = np.array([lnK(t, False) for t in T])
l2 = np.array([lnK(t) for t in T])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(1000 / T, l1, color="C0", lw=1.4, ls="--", label=r"$\Delta_\mathrm{r}C_p = 0$")
ax1.plot(1000 / T, l2, color="C1", lw=1.8, label=r"$\Delta_\mathrm{r}C_p(T)$ included")
ax1.plot([1000 / 723], [lnK(723)], "o", color="C3", ms=4)
ax1.annotate(rf"723 K: $K^\circ$ = {np.exp(lnK(723)):.1e}" + "\n" + rf"(with $\Delta_\mathrm{{r}}C_p = 0$: {np.exp(lnK(723, False)):.1e})", (1.45, -6.2), fontsize=8.5)
ax1.set_xlabel(r"$10^3\,\mathrm{K}/T$")
ax1.set_ylabel(r"$\ln K^\circ$")
ax1.legend(frameon=False, fontsize=9)
ax1.set_title(r"$\frac{1}{2}\mathrm{N_2} + \frac{3}{2}\mathrm{H_2} \rightleftharpoons \mathrm{NH_3}$", fontsize=10)

ax2.plot(T, [dcp(t) for t in T], color="C2", lw=1.8)
ax2.set_xlabel("T / K")
ax2.set_ylabel(r"$\Delta_\mathrm{r}C_{p,\mathrm{m}}$ / (J K$^{-1}$ mol$^{-1}$)")
ax2.set_title("reaction heat capacity", fontsize=10)
fig.tight_layout()
