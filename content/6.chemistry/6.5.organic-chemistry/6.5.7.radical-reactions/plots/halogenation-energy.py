"""Schematic energy profiles for the hydrogen-abstraction step R-H + X. -> R. + H-X, for a primary
and a tertiary C-H bond. Reaction enthalpies from bond dissociation enthalpies (298 K, kJ/mol):
D(1-C-H) = 423, D(3-C-H) = 404, D(H-F) = 570, D(H-Br) = 366. Fluorination is strongly exothermic
with an early, reactant-like transition state, so the two barriers hardly differ; bromination is
endothermic with a late, product-like transition state, so the barriers differ by nearly as much
as the radical energies. Barrier heights are illustrative."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)


def profile(dH, Ea, xts):
    """Smooth curve from 0 (reactants) through a maximum Ea at xts to dH (products)."""
    left = Ea * np.exp(-((x - xts) / (0.55 * xts)) ** 2 * 2.2)
    right = dH + (Ea - dH) * np.exp(-((x - xts) / (0.55 * (1 - xts))) ** 2 * 2.2)
    y = np.where(x < xts, left, right)
    return y


cases = [
    ("X = F (early transition state)", [(-147, 5, 0.25, "primary C-H"), (-166, 4, 0.23, "tertiary C-H")], (-200, 40)),
    ("X = Br (late transition state)", [(57, 66, 0.72, "primary C-H"), (38, 48, 0.75, "tertiary C-H")], (-20, 90)),
]
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
for ax, (title, curves, ylim) in zip(axes, cases):
    for (dH, Ea, xts, name), style in zip(curves, ["-", "--"]):
        ax.plot(x, profile(dH, Ea, xts), style, color="C0" if style == "-" else "C3", lw=2, label=f"{name}: $\\Delta H$ = {dH:+d}")
        ax.plot(xts, Ea, "o", color="C0" if style == "-" else "C3", ms=4)
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set_title(title, fontsize=11)
    ax.set_ylim(*ylim)
    ax.set_xticks([0.05, 0.95])
    ax.set_xticklabels(["R-H + X$\\bullet$", "R$\\bullet$ + H-X"])
    ax.set_xlabel("reaction coordinate")
    ax.set_ylabel(r"$H$ / (kJ mol$^{-1}$)")
    ax.legend(fontsize=8, loc="lower left" if "F" in title else "upper left", frameon=False)
fig.tight_layout()
