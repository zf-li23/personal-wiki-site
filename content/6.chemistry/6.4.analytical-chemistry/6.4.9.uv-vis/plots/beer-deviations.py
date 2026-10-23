"""Negative deviations from the Beer-Lambert law. Left: polychromatic light made of two
equally intense wavelengths with molar absorption coefficients eps1 and eps2 (path 1 cm).
Right: monochromatic light with a fraction s of stray light reaching the detector,
A_obs = lg[(1 + s)/(10^(-A) + s)], which levels off at lg(1 + 1/s)."""

import numpy as np
import matplotlib.pyplot as plt

c = np.linspace(0, 2.0e-4, 200)              # mol L^-1
eps1 = 1.0e4                                  # L mol^-1 cm^-1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.0))

for eps2, col in [(1.0e4, "k"), (0.75e4, "C0"), (0.5e4, "C1"), (0.25e4, "C3")]:
    A = -np.log10(0.5 * (10 ** (-eps1 * c) + 10 ** (-eps2 * c)))
    lab = r"$\varepsilon_2 = \varepsilon_1$" if eps2 == eps1 else rf"$\varepsilon_2 = {eps2 / eps1:.2f}\,\varepsilon_1$"
    ax1.plot(c * 1e4, A, color=col, lw=1.4, ls="--" if eps2 == eps1 else "-", label=lab)
ax1.set_xlabel(r"$c$ / ($10^{-4}$ mol L$^{-1}$)")
ax1.set_ylabel(r"observed absorbance $A$")
ax1.set_title("two wavelengths in the band pass", fontsize=10)
ax1.legend(frameon=False, fontsize=8)

At = np.linspace(0, 4, 200)                   # true absorbance eps*b*c
for s, col in [(0.0, "k"), (1e-4, "C0"), (1e-3, "C1"), (1e-2, "C3")]:
    Aobs = At if s == 0 else np.log10((1 + s) / (10 ** (-At) + s))
    lab = "no stray light" if s == 0 else f"stray light {s * 100:g} %"
    ax2.plot(At, Aobs, color=col, lw=1.4, ls="--" if s == 0 else "-", label=lab)
ax2.set_xlabel(r"true absorbance $\varepsilon b c$")
ax2.set_ylabel(r"observed absorbance $A$")
ax2.set_title("stray light", fontsize=10)
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 4)
ax2.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
