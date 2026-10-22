"""Molar conductivity of aqueous electrolytes at 25 C versus sqrt(c).
Left: strong electrolytes, normalised by the extrapolated limit (CRC Handbook / Robinson-Stokes data); a least-squares line through the
points with c <= 0.01 mol/L is extrapolated to c -> 0 (Kohlrausch), and the Onsager limiting slope
Lambda0 - (60.20 + 0.2289 Lambda0) sqrt(c) is drawn dashed.
Right: acetic acid, Lambda = alpha * Lambda0 with alpha from Ostwald's dilution law
(Ka = 1.75e-5, Lambda0 = 390.6 S cm2/mol); extrapolation to c -> 0 is impossible."""

import numpy as np
import matplotlib.pyplot as plt

c = np.array([0.0005, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1])          # mol/L
data = {
    "HCl": (np.array([422.6, 421.2, 415.7, 411.9, 407.0, 399.0, 391.1]), "C3"),
    "KCl": (np.array([147.74, 146.88, 143.48, 141.20, 138.27, 133.30, 128.90]), "C0"),
    "NaCl": (np.array([124.44, 123.68, 120.59, 118.45, 115.70, 111.01, 106.69]), "C2"),
}
sc = np.sqrt(c)
xs = np.linspace(0, 0.34, 100)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
for name, (lam, col) in data.items():
    m = c <= 0.0101
    slope, icpt = np.polyfit(sc[m], lam[m], 1)
    ax.plot(sc, lam / icpt, "o", color=col, ms=5, label=rf"{name}: $\Lambda^\infty_\mathrm{{m}}$ = {icpt:.1f} S cm$^2$ mol$^{{-1}}$")
    ax.plot(xs, 1 + slope / icpt * xs, color=col, lw=1.1)
    ax.plot(xs[xs < 0.15], 1 - (60.20 + 0.2289 * icpt) / icpt * xs[xs < 0.15], color=col, lw=1.0, ls="--")
ax.set_xlim(0, 0.34)
ax.set_ylim(0.82, 1.01)
ax.set_xlabel(r"$\sqrt{c\,/\,(\mathrm{mol\,L^{-1}})}$")
ax.set_ylabel(r"$\Lambda_\mathrm{m}/\Lambda^\infty_\mathrm{m}$")
ax.set_title("strong electrolytes: linear in $\\sqrt{c}$ (dashed: Onsager slope)", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="lower left")

ax = axes[1]
Ka, L0 = 1.75e-5, 390.6
cc = np.logspace(-6, -1, 400)
alpha = (-Ka + np.sqrt(Ka**2 + 4 * Ka * cc)) / (2 * cc)
ax.plot(np.sqrt(cc), alpha * L0, color="C1", lw=1.8, label="CH$_3$COOH (Ostwald)")
ax.axhline(L0, color="C1", lw=0.9, ls=":")
ax.text(0.15, L0 - 25, r"$\Lambda^\infty_\mathrm{m} = \lambda^\infty(\mathrm{H^+}) + \lambda^\infty(\mathrm{Ac^-})$ = 390.6", fontsize=9, color="C1")
ax.plot(sc, data["KCl"][0], "o-", color="C0", ms=4, lw=0.9, label="KCl")
ax.set_xlim(0, 0.32)
ax.set_ylim(0, 420)
ax.set_xlabel(r"$\sqrt{c\,/\,(\mathrm{mol\,L^{-1}})}$")
ax.set_ylabel(r"$\Lambda_\mathrm{m}$ / (S cm$^2$ mol$^{-1}$)")
ax.set_title("weak electrolyte: $\\Lambda_\\mathrm{m}$ falls steeply as $c$ grows", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="center right")
fig.tight_layout()
