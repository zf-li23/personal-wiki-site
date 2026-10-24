"""Tolman map of common phosphorus ligands: cone angle against the Tolman electronic parameter,
the A1 C-O stretching wavenumber of Ni(CO)3L (lower = stronger net donor). Values from
C. A. Tolman, Chem. Rev. 1977, 77, 313."""

import matplotlib.pyplot as plt

DATA = [  # ligand, cone angle / degree, TEP / cm^-1
    ("PF$_3$", 104, 2110.8),
    ("PCl$_3$", 124, 2097.0),
    ("P(OPh)$_3$", 128, 2085.3),
    ("P(OMe)$_3$", 107, 2079.5),
    ("P(OEt)$_3$", 109, 2076.3),
    ("P(O$i$Pr)$_3$", 130, 2075.9),
    ("PPh$_3$", 145, 2068.9),
    ("PMePh$_2$", 136, 2067.0),
    ("PMe$_2$Ph", 122, 2065.3),
    ("PMe$_3$", 118, 2064.1),
    ("PEt$_3$", 132, 2061.7),
    ("PCy$_3$", 170, 2056.4),
    ("P$t$Bu$_3$", 182, 2056.1),
    ("P($o$-tolyl)$_3$", 194, 2066.6),
]
OFFSET = {"PEt$_3$": (6, -12), "PMe$_3$": (-34, -12), "PMe$_2$Ph": (-58, 2), "P(OEt)$_3$": (6, -10),
          "P(OMe)$_3$": (6, 4), "PCy$_3$": (-20, 8), "P$t$Bu$_3$": (-52, 4)}

fig, ax = plt.subplots(figsize=(6.6, 4.4))
for name, theta, tep in DATA:
    ax.plot(theta, tep, "o", color="tab:blue", ms=6)
    dx, dy = OFFSET.get(name, (6, 2))
    ax.annotate(name, (theta, tep), xytext=(dx, dy), textcoords="offset points", fontsize=10)
ax.set_xlabel("cone angle $\\theta$ / degree")
ax.set_ylabel("$\\tilde{\\nu}$(CO) of Ni(CO)$_3$L / cm$^{-1}$")
ax.set_xlim(95, 205)
ax.grid(alpha=0.3)
ax.text(198, 2108, "weaker donor,\nstronger $\\pi$ acid", ha="right", va="top", fontsize=9)
ax.text(100, 2054, "stronger donor", ha="left", va="bottom", fontsize=9)
fig.tight_layout()
