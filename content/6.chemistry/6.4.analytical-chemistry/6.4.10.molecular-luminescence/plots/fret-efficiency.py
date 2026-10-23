"""FRET efficiency E = 1 / (1 + (r/R0)^6) against donor-acceptor distance for three
Forster radii. The shaded band 0.5 R0 - 1.5 R0 (for R0 = 5 nm) is where E changes
measurably and FRET works as a molecular ruler."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.5, 14, 500)              # nm
fig, ax = plt.subplots(figsize=(6.6, 4.2))
for R0, col in [(2.5, "C0"), (5.0, "C3"), (7.5, "C2")]:
    ax.plot(r, 1 / (1 + (r / R0) ** 6), color=col, lw=1.6, label=rf"$R_0$ = {R0} nm")
    ax.plot([R0], [0.5], "o", color=col, ms=4)
ax.axvspan(2.5, 7.5, color="C3", alpha=0.08, lw=0)
ax.axhline(0.5, color="0.5", lw=0.7, ls=":")
ax.text(2.6, 0.03, r"0.5 $R_0$ - 1.5 $R_0$ for $R_0$ = 5 nm", fontsize=8)
ax.set_xlabel(r"donor-acceptor distance $r$ / nm")
ax.set_ylabel(r"transfer efficiency $E$")
ax.set_xlim(0.5, 14)
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
