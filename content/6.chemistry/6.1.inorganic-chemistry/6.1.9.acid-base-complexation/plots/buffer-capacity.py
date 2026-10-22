"""Buffer capacity of acetic acid/acetate solutions (total 0.10 and 0.050 mol/L) and of pure water,
beta = 2.303 ([H+] + [OH-] + c Ka [H+] / (Ka + [H+])^2), as a function of pH."""

import numpy as np
import matplotlib.pyplot as plt

Kw, Ka = 1.0e-14, 1.75e-5
pKa = -np.log10(Ka)
pH = np.linspace(1, 13, 800)
h = 10.0 ** -pH

fig, ax = plt.subplots(figsize=(6.4, 3.8))
for c, col in [(0.10, "C0"), (0.050, "C2")]:
    beta = np.log(10) * (h + Kw / h + c * Ka * h / (Ka + h) ** 2)
    ax.plot(pH, beta, color=col, lw=1.8, label=f"HAc + Ac$^-$, c = {c:.2f} M")
ax.plot(pH, np.log(10) * (h + Kw / h), color="0.5", lw=1.2, ls="--", label="water only")
ax.axvspan(pKa - 1, pKa + 1, color="C1", alpha=0.12, lw=0)
ax.text(pKa, 0.064, r"p$K_a \pm 1$", ha="center", fontsize=9)
ax.axvline(pKa, color="0.6", lw=0.8, ls=":")
ax.set_ylim(0, 0.07)
ax.set_xlabel("pH")
ax.set_ylabel(r"buffer capacity $\beta$ / (mol L$^{-1}$)")
ax.legend(frameon=False, fontsize=9, loc="upper right")
fig.tight_layout()
