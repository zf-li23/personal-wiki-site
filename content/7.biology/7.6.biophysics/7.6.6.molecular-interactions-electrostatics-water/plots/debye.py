"""Electrostatic screening by salt. A: Debye length lambda_D = 0.304 nm / sqrt(I / M) of a 1:1
electrolyte in water at 25 C against ionic strength, with typical media marked. B: interaction
energy of two opposite unit charges in water, -kBT l_B e^{-r/lambda_D}/r, for no salt, 10 mM and
150 mM; the Bjerrum length l_B = 0.71 nm is where the unscreened energy equals kBT. C: the same
energies as ratios to the unscreened Coulomb energy: salt removes most of the interaction beyond
one Debye length."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
lB = 0.715
lam = lambda I: 0.304 / np.sqrt(I)

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.4, left=0.07, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
I = np.logspace(-6, 0.3, 300)
ax.plot(I, lam(I), color=charts.line("dna"), lw=1.8)
for Ii, txt in ((1e-3, "fresh water"), (0.01, "10 mM buffer"), (0.15, "cytoplasm,\nplasma"), (0.7, "seawater")):
    ax.plot([Ii], [lam(Ii)], "o", color=charts.line("blood"), ms=4)
    ax.text(Ii * 1.3, lam(Ii) * 1.25, f"{txt}\n{lam(Ii):.2g} nm", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-6, 3)
charts.style_axes(ax, "ionic strength / M", r"$\lambda_\mathrm{D}$ / nm")
charts.title(ax, "A  Debye length")

r = np.linspace(0.3, 5, 400)
cases = ((None, "neutral", "no salt"), (0.01, "enzyme", "10 mM"), (0.15, "blood", "150 mM"))
ax = axs[1]
for Ii, tok, lab in cases:
    u = -lB / r * (1 if Ii is None else np.exp(-r / lam(Ii)))
    ax.plot(r, u, color=charts.line(tok), lw=1.7, label=lab)
ax.axhline(-1, color=P.muted(), lw=0.6, ls=":")
ax.axvline(lB, color=P.muted(), lw=0.5, ls=":")
ax.text(lB + 0.05, -2.2, r"$\ell_\mathrm{B}$", fontsize=bio.core.FONT["small"], color=P.ink())
ax.set_ylim(-2.5, 0.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"$r$ / nm", r"$U$ / $k_\mathrm{B}T$")
charts.title(ax, "B  Opposite charges in water")

ax = axs[2]
for Ii, tok, lab in cases[1:]:
    ax.plot(r, np.exp(-r / lam(Ii)), color=charts.line(tok), lw=1.7, label=lab)
    ax.axvline(lam(Ii), color=charts.line(tok), lw=0.5, ls=":")
ax.set_yscale("log")
ax.set_ylim(1e-3, 1.1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"$r$ / nm", r"$U/U_\mathrm{Coulomb} = \mathrm{e}^{-r/\lambda_\mathrm{D}}$")
charts.title(ax, "C  Screening factor")
