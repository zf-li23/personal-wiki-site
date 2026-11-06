"""Quantum yield of CO2 fixation of C3 and C4 leaves against leaf temperature.

C3: in light-limited photosynthesis A = (J/4)(ci - Gamma*)/(ci + 2 Gamma*), so the yield per absorbed photon is
phi_C3 = phi0 (ci - Gamma*)/(ci + 2 Gamma*) with phi0 = 0.093 (the yield without photorespiration) and
Gamma*(T) from Bernacchi et al. (2001), ci = 0.7 ca. In 2 % O2, Gamma* is about one tenth.
C4: about 0.054, independent of temperature, because the CO2 pump suppresses photorespiration.
The pattern follows the measurements of Ehleringer and Bjorkman (1977); parameters chosen to match their
values (about 0.052 for both near 30 C at the CO2 of that time). Crossover temperatures are marked.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
R = 8.314
T = np.linspace(10, 42, 321)
gs = 42.75 * np.exp(37830 * (T - 25) / (298.15 * R * (T + 273.15)))
phi0, phi4 = 0.093, 0.054

fig, ax = plt.subplots(figsize=(6.8, 4.4))
cols = {280: P.edge("rna"), 420: P.edge("dna"), 700: P.edge("plant")}
for ca, col in cols.items():
    ci = 0.7 * ca
    y = phi0 * (ci - gs) / (ci + 2 * gs)
    ax.plot(T, y, color=col, lw=2, label=f"C3, $c_{{\\mathrm{{a}}}}$ = {ca} µmol mol$^{{-1}}$")
    k = np.argmin(np.abs(y - phi4))
    if 0 < k < len(T) - 1:
        ax.plot([T[k]], [phi4], "o", color=col, ms=6)
        ax.text(T[k], phi4 - 0.006, f"{T[k]:.0f} °C", ha="center", fontsize=8, color=col)
y2 = phi0 * (0.7 * 420 - gs / 10) / (0.7 * 420 + 2 * gs / 10)
ax.plot(T, y2, color=P.muted(), lw=1.6, ls=":", label="C3, 2 % O$_2$")
ax.axhline(phi4, color=P.ink(), lw=2.4, label="C4 (all CO$_2$ levels)")
ax.set_xlim(10, 42)
ax.set_ylim(0.02, 0.1)
ax.set_xlabel("Leaf temperature $T$ / °C")
ax.set_ylabel("Quantum yield / mol CO$_2$ mol$^{-1}$ photons")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.grid(True, alpha=0.3)
fig.tight_layout()
