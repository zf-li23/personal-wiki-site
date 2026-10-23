"""Approximate wavenumber ranges of important group frequencies in the mid-infrared,
with the functional group region (4000-1300 cm-1) and the fingerprint region (below 1300 cm-1)."""

import matplotlib.pyplot as plt

# (label, low, high, color index); intensity is not encoded
bands = [
    ("O-H free (alcohols)", 3590, 3650, 0),
    ("O-H hydrogen-bonded", 3200, 3550, 0),
    ("O-H of carboxylic acids", 2500, 3300, 0),
    ("N-H stretch", 3300, 3500, 0),
    ("$\\equiv$C-H stretch", 3260, 3330, 1),
    ("=C-H and Ar-H stretch", 3000, 3100, 1),
    ("C-H stretch (sp3)", 2850, 2970, 1),
    ("aldehyde C-H (Fermi doublet)", 2700, 2850, 1),
    ("C$\\equiv$N", 2210, 2260, 2),
    ("C$\\equiv$C", 2100, 2260, 2),
    ("cumulated X=C=Y", 1950, 2275, 2),
    ("C=O (anhydrides to amides)", 1630, 1850, 3),
    ("C=C (alkenes)", 1620, 1680, 3),
    ("aromatic ring", 1450, 1610, 3),
    ("N-H bend", 1550, 1650, 3),
    ("C-H bend (CH3, CH2)", 1350, 1470, 4),
    ("C-O stretch", 1000, 1300, 5),
    ("C-N stretch", 1020, 1340, 5),
    ("=C-H out-of-plane bend", 650, 1000, 5),
    ("Ar-H out-of-plane bend", 680, 900, 5),
    ("(CH2)n rock, n >= 4", 715, 730, 5),
    ("C-Cl stretch", 600, 800, 5),
]

fig, ax = plt.subplots(figsize=(9.5, 6.4))
ax.axvspan(1300, 4000, color="C0", alpha=0.06, lw=0)
ax.axvspan(600, 1300, color="C3", alpha=0.06, lw=0)
for i, (lab, lo, hi, ci) in enumerate(bands):
    y = len(bands) - i
    ax.barh(y, hi - lo, left=lo, height=0.6, color=f"C{ci}", alpha=0.85)
    if lo > 2300:  # label to the right of the bar (axis is reversed)
        ax.text(lo - 40, y, lab, va="center", ha="left", fontsize=8)
    else:
        ax.text(hi + 40, y, lab, va="center", ha="right", fontsize=8)
ax.set_xlim(4000, 600)
ax.set_ylim(0.2, len(bands) + 1.6)
ax.set_yticks([])
ax.text(2650, len(bands) + 1.0, "functional group region", ha="center", fontsize=10, color="C0")
ax.text(950, len(bands) + 1.0, "fingerprint region", ha="center", fontsize=10, color="C3")
for x, txt in [(2500, "X-H"), (2000, "triple bonds"), (1500, "double bonds")]:
    ax.axvline(x, color="0.6", lw=0.6, ls=":")
ax.set_xlabel(r"wavenumber $\tilde\nu$ / cm$^{-1}$")
fig.tight_layout()
