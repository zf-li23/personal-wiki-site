"""Hueckel pi molecular orbitals of ethylene, the allyl system, buta-1,3-diene and hexa-1,3,5-triene.
Each orbital is drawn at its energy E = alpha + x*beta (beta < 0, so larger x is lower): the circles
are the p orbitals seen from above, their area proportional to the squared coefficient and their
colour giving the sign. Filled pairs of dots mark the electrons of the neutral molecule (allyl: the
radical). The number of nodes grows by one per level, and the lowest orbital has no node."""

import numpy as np
import matplotlib.pyplot as plt


def huckel_chain(n):
    """Eigenvalues x (descending) and coefficients of the n-atom chain in units of beta (alpha = 0)."""
    h = np.diag(np.ones(n - 1), 1) + np.diag(np.ones(n - 1), -1)
    x, c = np.linalg.eigh(h)
    return x[::-1], c[:, ::-1]


systems = [("ethylene", 2, 2), ("allyl", 3, 3), ("butadiene", 4, 4), ("hexatriene", 6, 6)]
pos, neg = "#2563eb", "#f97316"
fig, ax = plt.subplots(figsize=(10, 5.6))
x0 = 0.0
for name, n, electrons in systems:
    x, c = huckel_chain(n)
    width = 0.55 * (n - 1)
    left = 0.0 if n == 1 else x0
    remaining = electrons
    for k in range(n):
        y = -x[k]  # plot energy upward: E - alpha in units of |beta|
        ax.plot([left - 0.25, left + width + 0.25], [y, y], color="0.6", lw=0.8, zorder=1)
        for r in range(n):
            coef = c[r, k]
            if abs(coef) < 1e-9:
                continue
            radius = 0.32 * abs(coef)
            ax.add_patch(plt.Circle((left + 0.55 * r, y), radius, color=pos if coef > 0 else neg, alpha=0.85, zorder=2))
        occ = min(2, remaining)
        remaining -= occ
        for e in range(occ):
            ax.plot(left - 0.45 - 0.12 * e, y, marker="o", ms=3.5, color=plt.rcParams["text.color"])
        ax.text(left + width + 0.35, y, f"{x[k]:+.3f}".replace("+0.000", " 0.000").replace("-0.000", " 0.000"), va="center", fontsize=8)
    ax.text(left + width / 2, -2.35, name, ha="center", fontsize=11)
    x0 += width + 2.2

ax.set_ylim(-2.55, 2.1)
ax.set_xlim(-1.0, x0 - 1.2)
ax.set_ylabel(r"$(E-\alpha)/|\beta|$")
ax.set_xticks([])
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
ax.set_aspect("equal")
fig.tight_layout()
