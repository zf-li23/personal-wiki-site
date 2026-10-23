"""Reversed-phase retention against the volume fraction phi of organic modifier,
lg k = lg kw - S phi (linear-solvent-strength model; illustrative lg kw and S). Small
molecules have S = 3-5, so k falls by roughly a factor of 2-3 per 10 % of modifier; a peptide
(S about 15) and a protein (S about 50) switch from fully retained to unretained within a
few per cent of modifier, which is why biomolecules are eluted with gradients. The band is
the useful window 1 < k < 10."""

import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 1, 400)
solutes = [("phenol", 1.6, 3.2, "C0"), ("toluene", 3.0, 4.2, "C2"),
           ("anthracene", 4.6, 5.4, "C1"), ("peptide (S = 15)", 6.0, 15.0, "C3"),
           ("protein (S = 50)", 22.0, 50.0, "C4")]
fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.axhspan(0, 1, color="0.5", alpha=0.12, lw=0)
for name, lkw, S, col in solutes:
    ax.plot(phi * 100, lkw - S * phi, color=col, lw=1.6, label=name)
ax.set_xlim(0, 100)
ax.set_ylim(-1, 3)
ax.set_xlabel(r"organic modifier $\varphi$ / % (v/v)")
ax.set_ylabel(r"$\lg k$")
ax.text(2, 0.45, r"$1 < k < 10$", fontsize=8)
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
