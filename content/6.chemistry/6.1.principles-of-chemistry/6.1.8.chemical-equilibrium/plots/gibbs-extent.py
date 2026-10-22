"""Gibbs energy of the system N2O4(g) <=> 2 NO2(g) at 298.15 K and total pressure p = p0,
starting from 1 mol N2O4, as a function of the extent of reaction xi. The straight line is the
sum of the pure-component standard Gibbs energies; the curvature comes from the RT ln(x p/p0) terms."""

import numpy as np
import matplotlib.pyplot as plt

R, T = 8.314, 298.15
dG0 = 4.73e3   # J mol^-1, Delta_r G0 (NBS/NIST data)
K = np.exp(-dG0 / (R * T))

xi = np.linspace(1e-6, 1 - 1e-6, 2000)
x_a = (1 - xi) / (1 + xi)
x_b = 2 * xi / (1 + xi)
G = xi * dG0 + R * T * ((1 - xi) * np.log(x_a) + 2 * xi * np.log(x_b))   # relative to G0(N2O4)
xi_eq = np.sqrt(K / (4 + K))
G_eq = np.interp(xi_eq, xi, G)

fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(xi, G / 1e3, color="C0", lw=1.8, label=r"$G(\xi) - G^\circ_\mathrm{m}(\mathrm{N_2O_4})$")
ax.plot([0, 1], [0, dG0 / 1e3], color="0.5", ls="--", lw=1.2, label="pure components, no mixing")
ax.plot([xi_eq], [G_eq / 1e3], "o", color="C3")
ax.annotate(rf"equilibrium $\xi_\mathrm{{eq}}$ = {xi_eq:.3f} mol", (xi_eq + 0.03, G_eq / 1e3 - 0.35), color="C3", fontsize=10)
ax.annotate(r"$\Delta_\mathrm{r}G^\circ_\mathrm{m}$ = 4.73 kJ mol$^{-1}$", (0.52, 4.6), fontsize=10)
ax.annotate(r"slope $=\Delta_\mathrm{r}G_\mathrm{m} < 0$", (0.01, -1.45), fontsize=9)
ax.annotate(r"slope $=\Delta_\mathrm{r}G_\mathrm{m} > 0$", (0.55, 1.2), fontsize=9)
ax.set_xlabel(r"extent of reaction $\xi$ / mol")
ax.set_ylabel("G / kJ")
ax.set_xlim(0, 1)
ax.set_ylim(-1.7, 5.3)
ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
