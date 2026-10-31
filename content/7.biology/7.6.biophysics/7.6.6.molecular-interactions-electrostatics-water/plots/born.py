"""Why charges stay in water. A: Born free energy of transferring a monovalent ion of radius a
from water (relative permittivity 78.4) into a medium of permittivity 2 (hydrocarbon core of a
membrane), 4 and 10 (protein interior, effective values), in kBT at 25 C; for a divalent ion
multiply by 4. B: the shift of the pKa of an ionizable group moved from water into a medium of
permittivity eps (charge radius 0.25 nm), for an acid (pKa rises: the neutral form is
favoured) and a base (pKa falls), estimated from the Born energy alone; real proteins
compensate part of this cost with hydrogen bonds, nearby charges and water penetration, so
measured shifts are smaller."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
lB0 = 56.0  # nm, Bjerrum length in vacuum at 25 C
eps_w = 78.4


def born(a, eps, z=1):
    return z ** 2 * lB0 / (2 * a) * (1 / eps - 1 / eps_w)


fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.4))
fig.subplots_adjust(wspace=0.35, left=0.08, right=0.98, bottom=0.16, top=0.88)

ax = axs[0]
a = np.linspace(0.1, 1.0, 300)
for eps, tok in ((2, "lipid_tail"), (4, "protein"), (10, "enzyme")):
    ax.plot(a, born(a, eps), color=charts.line(tok), lw=1.8, label=rf"$\varepsilon_\mathrm{{r}} = {eps}$")
for ai, txt, yt in ((0.18, r"Na$^+$", 200), (0.23, r"Cl$^-$", 130)):
    ax.axvline(ai, color=P.muted(), lw=0.5, ls=":")
    ax.text(ai + 0.01, yt, txt, fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_yscale("log")
ax.set_ylim(1, 300)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "ion radius $a$ / nm", r"$\Delta G_\mathrm{transfer}$ / $k_\mathrm{B}T$")
charts.title(ax, "A  Born energy of burial")

ax = axs[1]
eps = np.linspace(2, 78.4, 300)
dpk = born(0.25, eps) / np.log(10)
ax.plot(eps, dpk, color=charts.line("blood"), lw=1.8, label="acid (e.g. Asp, Glu): pKa rises")
ax.plot(eps, -dpk, color=charts.line("dna"), lw=1.8, label="base (e.g. Lys): pKa falls")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.set_xscale("log")
ax.set_xticks([2, 4, 10, 20, 40, 80])
ax.set_xticklabels(["2", "4", "10", "20", "40", "80"])
ax.set_ylim(-25, 25)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"relative permittivity of the site $\varepsilon_\mathrm{r}$", r"$\Delta\mathrm{p}K_\mathrm{a}$ (Born estimate)")
charts.title(ax, "B  pKa shifts of buried groups")
