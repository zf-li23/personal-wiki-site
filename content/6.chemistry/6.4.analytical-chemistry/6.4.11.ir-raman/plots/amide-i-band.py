"""Synthetic amide I bands (in D2O) of a mostly alpha-helical and a mostly beta-sheet
protein, built from Gaussian components at typical positions (helix ~1652, beta sheet
~1632 and ~1685 (antiparallel), random coil ~1645, turns ~1668 cm-1). Lower panels: the
negative second derivative, which resolves the overlapping components."""

import numpy as np
import matplotlib.pyplot as plt

nu = np.linspace(1590, 1710, 1201)


def g(center, height, fwhm):
    s = fwhm / 2.3548
    return height * np.exp(-0.5 * ((nu - center) / s)**2)


comp = {
    "alpha helix": (1652, "C0"),
    "beta sheet": (1632, "C3"),
    "beta sheet (antiparallel)": (1685, "C3"),
    "random coil": (1645, "C2"),
    "turns": (1668, "C1"),
}
proteins = [
    ("mostly alpha-helical", {"alpha helix": (1.0, 18), "random coil": (0.25, 22),
                              "turns": (0.2, 15), "beta sheet": (0.08, 14)}),
    ("mostly beta-sheet", {"beta sheet": (1.0, 16), "beta sheet (antiparallel)": (0.22, 10),
                           "turns": (0.3, 15), "random coil": (0.3, 22),
                           "alpha helix": (0.1, 18)}),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 6), sharex=True,
                         gridspec_kw=dict(height_ratios=[1.6, 1]))
for j, (title, parts) in enumerate(proteins):
    ax = axes[0, j]
    total = np.zeros_like(nu)
    for name, (hgt, w) in parts.items():
        center, col = comp[name]
        y = g(center, hgt, w)
        total += y
        ax.fill_between(nu, 0, y, color=col, alpha=0.25, lw=0)
        ax.plot(nu, y, color=col, lw=0.8)
    ax.plot(nu, total, color="k", lw=1.8)
    ax.set_title(title, fontsize=10)
    ax.set_yticks([])
    ax.set_ylabel("absorbance (a.u.)" if j == 0 else "")
    d2 = -np.gradient(np.gradient(total, nu), nu)
    ax2 = axes[1, j]
    ax2.plot(nu, d2, color="0.3", lw=1.2)
    ax2.axhline(0, color="0.6", lw=0.6)
    ax2.set_yticks([])
    ax2.set_ylabel("$-\\mathrm{d}^2A/\\mathrm{d}\\tilde\\nu^2$" if j == 0 else "")
    ax2.set_xlabel(r"wavenumber $\tilde\nu$ / cm$^{-1}$")
    for name, (center, col) in comp.items():
        if name in parts:
            ax2.axvline(center, color=col, lw=0.8, ls=":")
    ax2.set_xlim(1710, 1590)
handles = [plt.Line2D([], [], color=col, lw=4, alpha=0.5) for _, (_, col) in
           list(comp.items())[:2] + list(comp.items())[3:]]
axes[0, 1].legend(handles, ["alpha helix", "beta sheet", "random coil", "turns"],
                  frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
