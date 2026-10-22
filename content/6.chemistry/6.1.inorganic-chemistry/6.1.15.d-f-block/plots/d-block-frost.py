"""Frost diagrams (N E0 against oxidation number N) of the 3d elements at pH 0, from Latimer diagrams
(E0 from the CRC Handbook; Mn values as in the Frost diagram of 6.1.12). The O2/H2O line (slope 1.229 V)
is drawn through the origin for comparison: a couple steeper than it can oxidize water."""

import numpy as np
import matplotlib.pyplot as plt

# (N, label, E0 of the couple joining this species to the previous one)
series = {
    "V": [(0, "V", None), (2, r"V$^{2+}$", -1.175), (3, r"V$^{3+}$", -0.255), (4, r"VO$^{2+}$", 0.337),
          (5, r"VO$_2^+$", 0.991)],
    "Cr": [(0, "Cr", None), (2, r"Cr$^{2+}$", -0.913), (3, r"Cr$^{3+}$", -0.407), (6, r"Cr$_2$O$_7^{2-}$", 1.36)],
    "Mn": [(0, "Mn", None), (2, r"Mn$^{2+}$", -1.18), (3, r"Mn$^{3+}$", 1.51), (4, r"MnO$_2$", 0.95),
           (6, r"MnO$_4^{2-}$", 2.26), (7, r"MnO$_4^-$", 0.56)],
    "Fe": [(0, "Fe", None), (2, r"Fe$^{2+}$", -0.447), (3, r"Fe$^{3+}$", 0.771), (6, r"FeO$_4^{2-}$", 2.20)],
    "Co": [(0, "Co", None), (2, r"Co$^{2+}$", -0.28), (3, r"Co$^{3+}$", 1.92)],
    "Ni": [(0, "Ni", None), (2, r"Ni$^{2+}$", -0.257), (4, r"NiO$_2$", 1.678)],
    "Cu": [(0, "Cu", None), (1, r"Cu$^+$", 0.521), (2, r"Cu$^{2+}$", 0.153)],
    "Zn": [(0, "Zn", None), (2, r"Zn$^{2+}$", -0.762)],
}


OFF = {"V": (6, -12), "Cr": (6, 4), "Mn": (-6, -13), "Fe": (-6, 6),
       "Co": (-6, 5), "Ni": (6, -12), "Cu": (-4, 6), "Zn": (6, -12)}


def frost(chain):
    pts, y, n0 = [], 0.0, 0
    for n, lab, e in chain:
        if e is not None:
            y += (n - n0) * e
        pts.append((n, y, lab))
        n0 = n
    return pts


fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), sharey=True)
for ax, names in zip(axes, [["V", "Cr", "Mn", "Fe"], ["Co", "Ni", "Cu", "Zn"]]):
    for k, el in enumerate(names):
        pts = frost(series[el])
        col = f"C{k}"
        ax.plot([p[0] for p in pts], [p[1] for p in pts], "o-", color=col, lw=1.5, label=el)
        for n, y, lab in pts[1:]:
            ax.annotate(lab, (n, y), xytext=OFF[el], textcoords="offset points", fontsize=8, color=col,
                        ha="right" if OFF[el][0] < 0 else "left")
    x = np.array([0, 7])
    ax.plot(x, 1.229 * x, color="0.6", lw=0.9, ls="--", label=r"slope of O$_2$/H$_2$O")
    ax.axhline(0, color="0.6", lw=0.7, ls=":")
    ax.set_xlabel("oxidation number $N$")
    ax.set_xticks(range(0, 8))
    ax.set_ylim(-3.2, 7.2)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
axes[0].set_ylabel(r"$N E^\circ$ / V")
fig.tight_layout()
