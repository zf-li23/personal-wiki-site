"""Isotope patterns of the molecular-ion region for one or two Cl and Br atoms, ClBr, Cl3
and twenty carbon atoms (relative to the most intense peak = 100), from the binomial
expansion of the isotopic abundances (IUPAC: 35Cl 75.76 %, 79Br 50.69 %, 13C 1.07 %)."""

import numpy as np
import matplotlib.pyplot as plt

cl = np.array([0.7576, 0, 0.2424])
br = np.array([0.5069, 0, 0.4931])
c = np.array([0.9893, 0.0107])


def power(p, k):
    out = np.array([1.0])
    for _ in range(k):
        out = np.convolve(out, p)
    return out


cases = [
    ("Cl", cl),
    ("Cl$_2$", power(cl, 2)),
    ("Cl$_3$", power(cl, 3)),
    ("Br", br),
    ("Br$_2$", power(br, 2)),
    ("ClBr", np.convolve(cl, br)),
    ("C$_{20}$", power(c, 20)[:4]),
]
fig, axes = plt.subplots(1, len(cases), figsize=(10.5, 2.9), sharey=True)
for ax, (name, p) in zip(axes, cases):
    y = 100 * p / p.max()
    k = np.arange(len(y))
    keep = y > 0.05
    ax.vlines(k[keep], 0, y[keep], color="C0", lw=3.5)
    for kk, yy in zip(k[keep], y[keep]):
        ax.text(kk, yy + 3, f"{yy:.0f}" if yy >= 10 else f"{yy:.1f}", ha="center", fontsize=7)
    ax.set_xticks(k[keep])
    ax.set_xticklabels(["M" if kk == 0 else f"+{kk}" for kk in k[keep]], fontsize=7)
    ax.set_xlim(-0.8, max(k[keep]) + 0.8)
    ax.set_title(name, fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylim(0, 115)
axes[0].set_ylabel("relative intensity")
fig.tight_layout()
