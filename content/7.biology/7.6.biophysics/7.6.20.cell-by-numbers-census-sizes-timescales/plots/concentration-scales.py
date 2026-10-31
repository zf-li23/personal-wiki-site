"""Three readings of a concentration in a cell.

Bottom axis: molar concentration from 1 nM to 10 mM; top axis: the same concentration as copies per
E. coli cell (V = 1 fL, one copy = 1.66 nM). A: mean spacing d = c^(-1/3) between molecules arranged
on a cubic lattice, against the diameters of a small protein (5 nm) and a ribosome (25 nm); the total
protein of the cytoplasm (about 3 x 10^6 molecules per fL, about 5 mM) is marked, where the spacing
(7 nm) is close to the size of the molecules. B: time for a given molecule to meet a partner present
at concentration c, in two estimates: the diffusion time over the mean spacing, d^2/(6D), and the
mean time to a diffusion-limited encounter, 1/(k c) with k = 4 pi D a (D = 10 um^2/s for a protein in
cytoplasm, a = 5 nm encounter radius, so k = 3.8 x 10^8 M^-1 s^-1). The second is the correct one: at
1 nM (one copy per E. coli) a meeting takes seconds, at 1 uM milliseconds."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
NA = 6.022e23
c = np.logspace(-9, -2, 300)  # M
n_per_nm3 = c * NA * 1e-24  # molecules per nm^3
d = n_per_nm3 ** (-1 / 3)

fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.7))
fig.subplots_adjust(wspace=0.32, left=0.08, right=0.97, bottom=0.15, top=0.8)


def top_axis(ax):
    t = ax.secondary_xaxis("top", functions=(lambda x: x / 1.66e-9, lambda n: n * 1.66e-9))
    t.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
    t.set_xlabel(r"copies per $\it{E.\ coli}$ (1 fL)", fontsize=bio.core.FONT["tiny"], color=P.ink())


ax = axs[0]
ax.plot(c, d, color=charts.line("protein"), lw=1.5, label=r"mean spacing $d = c^{-1/3}$")
ax.axhline(5, color=charts.line("enzyme"), lw=0.8, ls="--")
ax.text(1.5e-9, 5.6, "protein diameter (5 nm)", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axhline(25, color=charts.line("rrna"), lw=0.8, ls="--")
ax.text(1.5e-9, 28, "ribosome (25 nm)", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axvline(5e-3, color=P.muted(), lw=0.7, ls=":")
ax.text(4e-3, 300, "all cytoplasmic\nprotein", ha="right", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
charts.style_axes(ax, "concentration / M", "mean spacing / nm")
charts.title(ax, "A  Spacing")
top_axis(ax)

ax = axs[1]
D = 10e-12  # m^2/s
a = 5e-9
k = 4 * np.pi * D * a * NA * 1e3  # M^-1 s^-1
ax.plot(c, 1 / (k * c), color=charts.line("dna"), lw=1.5, label=r"encounter time $1/(4\pi Dac)$")
ax.plot(c, (d * 1e-9) ** 2 / (6 * D), color=charts.line("neutral"), lw=1.0, ls="--",
        label=r"diffusion over the spacing $d^2/6D$")
for t, lab in ((1, "1 s"), (1e-3, "1 ms"), (1e-6, "1 µs")):
    ax.axhline(t, color=P.muted(), lw=0.5, ls=":")
    ax.text(2e-3, t * 1.3, lab, fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="right")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "concentration of the partner / M", "time / s")
charts.title(ax, "B  Time to meet a partner")
top_axis(ax)
