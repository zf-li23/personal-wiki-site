"""Formal potential of As(V)/As(III) (H3AsO4 + 2H+ + 2e- -> HAsO2 + 2H2O, E = 0.560 V) versus pH, including the
acid dissociation of H3AsO4 (pKa 2.25, 6.98, 11.5) and HAsO2 (pKa 9.2), compared with I3-/I- (0.536 V,
independent of pH up to about pH 9)."""

import numpy as np
import matplotlib.pyplot as plt

S = 0.05916
pH = np.linspace(0, 9, 500)
h = 10.0 ** -pH
k1, k2, k3 = 10 ** -2.25, 10 ** -6.98, 10 ** -11.5
d_ox = h ** 3 / (h ** 3 + k1 * h ** 2 + k1 * k2 * h + k1 * k2 * k3)
d_red = h / (h + 10 ** -9.2)
E_As = 0.560 - S * pH + S / 2 * np.log10(d_ox / d_red)

fig, ax = plt.subplots(figsize=(6.4, 4))
ax.plot(pH, E_As, color="C0", lw=1.8, label="As(V)/As(III)")
ax.plot(pH, np.full_like(pH, 0.536), color="C1", lw=1.8, label="I$_3^-$/I$^-$")
ax.fill_between(pH, E_As, 0.536, where=E_As > 0.536, color="C0", alpha=0.15, lw=0)
ax.fill_between(pH, E_As, 0.536, where=E_As < 0.536, color="C1", alpha=0.15, lw=0)
ax.annotate("As(V) oxidises I$^-$", (0.15, 0.55), xytext=(1.0, 0.64), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6))
ax.text(4.5, 0.40, "I$_3^-$ oxidises As(III)", fontsize=8)
ax.axvline(8, color="0.6", lw=0.8, ls=":")
ax.text(7.9, 0.30, "NaHCO$_3$ (pH 8)", fontsize=8, ha="right")
ax.set_xlabel("pH")
ax.set_ylabel(r"$E^{\circ\prime}$ / V")
ax.set_xlim(0, 9)
ax.set_ylim(-0.3, 0.72)
ax.legend(frameon=False, fontsize=9, loc="lower left")
fig.tight_layout()
