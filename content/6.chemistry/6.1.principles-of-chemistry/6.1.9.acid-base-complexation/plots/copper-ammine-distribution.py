"""Fractions of Cu(II) present as [Cu(NH3)n]2+ (n = 0..4) against the free ammonia concentration,
from the stepwise stability constants lg K1..K4 = 4.31, 3.67, 3.04, 2.30 (25 C)."""

import numpy as np
import matplotlib.pyplot as plt

lgK = np.array([4.31, 3.67, 3.04, 2.30])
lgbeta = np.concatenate([[0.0], np.cumsum(lgK)])
pL = np.linspace(0, 6, 600)                      # -lg [NH3]
L = 10.0 ** -pL
terms = np.array([10.0 ** lgbeta[n] * L**n for n in range(5)])
frac = terms / terms.sum(axis=0)

fig, ax = plt.subplots(figsize=(6.4, 3.8))
for n in range(5):
    if n == 0:
        lab = r"Cu$^{2+}$"
    elif n == 1:
        lab = r"[Cu(NH$_3$)]$^{2+}$"
    else:
        lab = rf"[Cu(NH$_3$)$_{n}$]$^{{2+}}$"
    ax.plot(pL, frac[n], lw=1.8, color=f"C{n}", label=lab)
for k in lgK:
    ax.axvline(k, color="0.6", lw=0.8, ls=":")
ax.set_xlim(6, 0)
ax.set_xlabel(r"$-\lg[\mathrm{NH_3}]$ (free ammonia; increases to the right)")
ax.set_ylabel("fraction of Cu(II)")
ax.legend(frameon=False, fontsize=8, loc="center left")
fig.tight_layout()
