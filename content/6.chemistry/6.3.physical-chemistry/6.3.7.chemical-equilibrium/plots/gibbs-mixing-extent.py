"""Gibbs energy of an ideal-gas isomerisation A(g) <=> B(g) at 298.15 K and p = p0, starting from 1 mol A,
split into its two parts: the straight line xi * Delta_r G0 (pure, unmixed components) and the Gibbs
energy of mixing RT[(1 - xi) ln(1 - xi) + xi ln xi]. Delta_r G0 = -3.0 kJ/mol (illustrative value)."""

import numpy as np
import matplotlib.pyplot as plt

R, T = 8.314, 298.15
dG0 = -3.0e3
K = np.exp(-dG0 / (R * T))
xi = np.linspace(1e-6, 1 - 1e-6, 2000)
line = xi * dG0
mix = R * T * ((1 - xi) * np.log(1 - xi) + xi * np.log(xi))
G = line + mix
xi_eq = K / (1 + K)
G_eq = xi_eq * dG0 + R * T * ((1 - xi_eq) * np.log(1 - xi_eq) + xi_eq * np.log(xi_eq))

fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(xi, line / 1e3, color="0.5", lw=1.3, ls="--", label=r"no mixing: $\xi\,\Delta_\mathrm{r}G^\circ_\mathrm{m}$")
ax.plot(xi, mix / 1e3, color="C1", lw=1.4, ls=":", label=r"$\Delta_\mathrm{mix}G$")
ax.plot(xi, G / 1e3, color="C0", lw=2.0, label=r"$G(\xi) - G^\circ_\mathrm{m}(\mathrm{A})$")
ax.plot([xi_eq], [G_eq / 1e3], "o", color="C3")
ax.annotate(rf"minimum at $\xi_\mathrm{{eq}} = K^\circ/(1+K^\circ)$ = {xi_eq:.3f} mol", (0.40, G_eq / 1e3 - 0.75), color="C3", fontsize=9.5)
ax.annotate(r"slope $\to -\infty$ as $\xi \to 0$", (0.03, 0.2), fontsize=9)
ax.annotate(r"slope $\to +\infty$ as $\xi \to 1$", (0.70, -2.9), fontsize=9)
ax.set_xlabel(r"extent of reaction $\xi$ / mol")
ax.set_ylabel("G / kJ")
ax.set_xlim(0, 1)
ax.set_ylim(-4.8, 0.6)
ax.legend(frameon=False, fontsize=9, loc="lower left")
fig.tight_layout()
