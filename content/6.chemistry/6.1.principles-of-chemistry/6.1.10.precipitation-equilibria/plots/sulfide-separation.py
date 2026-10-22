"""Metal sulfides (CuS, Kspa = 6e-16, lies far below the plotted range) in a solution saturated with H2S ([H2S] = 0.10 mol/L):
MS(s) + 2 H+ <=> M2+ + H2S(aq), Kspa = [M2+][H2S]/[H+]^2, so lg[M2+] = lg Kspa + 1 - 2 pH.
Kspa values for freshly precipitated sulfides as tabulated in general-chemistry texts (after Myers,
J. Chem. Educ. 1986); they are uncertain by an order of magnitude or more."""

import numpy as np
import matplotlib.pyplot as plt

data = [("PbS", 3e-7), ("CdS", 8e-7), ("ZnS", 3e-2), ("FeS", 6e2), ("MnS", 3e10)]
pH = np.linspace(-1, 8, 400)

fig, ax = plt.subplots(figsize=(7, 4.4))
for i, (name, K) in enumerate(data):
    lgM = np.log10(K) + 1 - 2 * pH
    m = (lgM < 1) & (lgM > -9)
    ax.plot(pH[m], lgM[m], color=f"C{i}", lw=1.8, label=name)
ax.axhline(-1, color="0.6", lw=0.8, ls=":")
ax.axhline(-5, color="0.6", lw=0.8, ls=":")
ax.text(5.6, -0.85, "0.10 M", fontsize=8)
ax.text(5.6, -4.85, r"$10^{-5}$ M", fontsize=8)
# Zn/Mn window: ZnS complete (pH 2.24) to MnS start (pH 6.24)
ax.axvspan(2.24, 6.24, ymin=0.0, ymax=0.05, color="C3", alpha=0.5, lw=0)
ax.text(2.4, -8.3, "Zn2+ / Mn2+ separation window", fontsize=8)
ax.set_xlim(-1, 8)
ax.set_ylim(-9, 1)
ax.set_xlabel("pH")
ax.set_ylabel(r"$\lg[\mathrm{M}^{2+}]$ in equilibrium with MS(s)")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
