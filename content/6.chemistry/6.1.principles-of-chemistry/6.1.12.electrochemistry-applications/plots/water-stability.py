"""Potential-pH diagram for water at 298.15 K with p(H2) = p(O2) = p0: lines a (H+/H2) and b (O2/H2O);
dashed lines c and d sketch the region widened by overpotential (taken as 0.5 V for illustration).
Horizontal lines: the pH-independent couples F2/F- and Na+/Na."""

import numpy as np
import matplotlib.pyplot as plt

s = 0.05916
pH = np.linspace(0, 14, 50)
a = -s * pH
b = 1.229 - s * pH

fig, ax = plt.subplots(figsize=(7, 5))
ax.fill_between(pH, a, b, color="C0", alpha=0.12)
ax.plot(pH, a, color="C0", lw=1.8)
ax.plot(pH, b, color="C3", lw=1.8)
ax.plot(pH, a - 0.5, color="C0", lw=1.0, ls="--")
ax.plot(pH, b + 0.5, color="C3", lw=1.0, ls="--")
ax.axhline(2.866, color="C2", lw=1.4)
ax.axhline(-2.71, color="C4", lw=1.4)
ax.text(0.3, 2.95, r"$\mathrm{F_2 + 2e^- \rightleftharpoons 2F^-}$, $E^\circ = 2.87$ V", fontsize=9, color="C2")
ax.text(0.3, -2.62, r"$\mathrm{Na^+ + e^- \rightleftharpoons Na}$, $E^\circ = -2.71$ V", fontsize=9, color="C4")
ax.text(12.6, b[-1] + 0.2, "b", fontsize=11, color="C3")
ax.text(12.6, a[-1] + 0.2, "a", fontsize=11, color="C0")
ax.text(0.5, 1.229 + 0.55, "d", fontsize=11, color="C3")
ax.text(0.5, -0.5 - 0.3, "c", fontsize=11, color="C0")
ax.text(5.5, 0.15, r"H$_2$O stable", fontsize=10)
ax.text(6.5, 1.95, r"O$_2$ evolved", fontsize=10, color="C3")
ax.text(1.5, -1.35, r"H$_2$ evolved", fontsize=10, color="C0")
ax.set_xlim(0, 14)
ax.set_ylim(-3.1, 3.3)
ax.set_xlabel("pH")
ax.set_ylabel(r"$E$ / V")
ax.set_title(r"a: $E = -0.0592\,\mathrm{pH}$;  b: $E = 1.229 - 0.0592\,\mathrm{pH}$", fontsize=10)
fig.tight_layout()
