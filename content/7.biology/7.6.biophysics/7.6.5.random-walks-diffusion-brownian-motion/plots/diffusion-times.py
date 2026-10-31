"""Spreading by diffusion. A: concentration profiles c(x, t) of molecules released at x = 0 at
t = 0 in one dimension with D = 25 um^2/s (a GFP-sized protein in eukaryotic cytoplasm), at
t = 0.1, 1, 10 and 30 s; the width grows as sqrt(2Dt). B: time to diffuse a distance L,
t = L^2/(6D) in three dimensions, for a small molecule (D = 1000 um^2/s), a protein in cytoplasm
(25), a protein in the bacterial cytoplasm (7.7) and a membrane protein (0.1, t = L^2/4D in two
dimensions), compared with directed transport at 1 um/s (kinesin) and 30 um/s (a swimming
bacterium); diffusion wins below L = 6D/v and loses above."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.6), gridspec_kw=dict(width_ratios=(1, 1.35)))
fig.subplots_adjust(wspace=0.3, left=0.07, right=0.95, bottom=0.15, top=0.9)

ax = axs[0]
D = 25.0
x = np.linspace(-50, 50, 800)
for t, tok in ((0.1, "blood"), (1.0, "drug"), (10.0, "enzyme"), (30.0, "dna")):
    c = np.exp(-x ** 2 / (4 * D * t)) / np.sqrt(4 * np.pi * D * t)
    ax.plot(x, c, color=charts.line(tok), lw=1.6, label=f"t = {t:g} s")
    w = np.sqrt(2 * D * t)
    if True:
        ax.annotate("", (w, c.max() * np.exp(-0.5)), (-w, c.max() * np.exp(-0.5)),
                    arrowprops=dict(arrowstyle="<->", color=charts.line(tok), lw=0.7))
ax.set_ylim(0, 0.2)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
ax.text(-48, 0.165, r"$D = 25\,\mu\mathrm{m^2\,s^{-1}}$" + "\narrows: $\\pm\\sqrt{2Dt}$", fontsize=bio.core.FONT["tiny"],
        color=P.ink())
charts.style_axes(ax, r"$x$ / $\mu$m", r"$c$ / $\mu\mathrm{m}^{-1}$ (per molecule)")
charts.title(ax, "A  Gaussian spreading")

ax = axs[1]
L = np.logspace(-3, 6, 300)  # um
for Dk, dim, tok, lab in ((1000, 3, "dna", "small molecule, 1000"), (25, 3, "protein", "protein in cytoplasm, 25"),
                          (7.7, 3, "bacterium", r"protein in $\it{E.\ coli}$, 7.7"), (0.1, 2, "lipid_head", "membrane protein, 0.1")):
    ax.plot(L, L ** 2 / (2 * dim * Dk), color=charts.line(tok), lw=1.6, label=lab)
for v, ls, lab in ((1.0, "--", r"motor, 1 $\mu$m/s"), (30.0, ":", r"swimming, 30 $\mu$m/s")):
    ax.plot(L, L / v, color=P.ink(), lw=1.0, ls=ls, label=lab)
for Lm, txt in ((5e-3, "protein"), (1.0, "bacterium"), (20.0, "eukaryotic\ncell"), (1e6, "1 m axon")):
    ax.axvline(Lm, color=P.muted(), lw=0.5, ls=":")
    ax.text(Lm * 1.15, 3e-11, txt, fontsize=bio.core.FONT["tiny"], color=P.ink(), va="bottom")
for tt, txt in ((1.0, "1 s"), (3600.0, "1 h"), (3.15e7, "1 yr")):
    ax.axhline(tt, color=P.muted(), lw=0.4, ls=":")
    ax.text(2.5e6, tt, txt, fontsize=bio.core.FONT["tiny"], color=P.muted(), va="center", clip_on=False)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-11, 1e13)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"] - 0.5, labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"distance $L$ / $\mu$m", "time / s")
charts.title(ax, r"B  Diffusion time $t \sim L^2/D$")
