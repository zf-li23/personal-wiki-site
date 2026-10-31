"""The J factor of DNA looping.

A: J factor (effective concentration of one end of a DNA segment at the other) against the length
of the segment, for DNA with lp = 50 nm (Kuhn length b = 100 nm) and 0.34 nm per base pair. Gaussian
chain: J = (3/(2 pi L b))^(3/2)/N_A, falling as L^(-3/2). Toy model: the Gaussian value times the
Boltzmann factor of bending a circle, exp(-2 pi^2 lp/L), with its maximum at L = 4 pi^2 lp/3
(about 1900 bp). Worm-like chain: Rippe's interpolation J = 0.53 uM n^(-3/2) exp(-2.66/n^2) with
n = L/b, which reproduces simulations of semiflexible chains with a capture radius of about 10 nm and
peaks near 550 bp at about 0.1 uM (drawn for L > 150 bp, where the interpolation is reliable). B: the effect of helical phasing for loops that must bring two
sites to the same face of the helix: the WLC value multiplied by exp(-2 pi^2 C delta^2/L), where
delta is the fractional excess of a helical turn (helical repeat 10.5 bp) and C = 100 nm the twist
persistence length; looping oscillates with a 10.5 bp period that fades for long loops."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
NA = 6.022e23
LP, B, RISE = 50.0, 100.0, 0.34  # nm


def j_gauss(L):
    """Molar J of a Gaussian chain of contour length L (nm)."""
    p = (3.0 / (2 * np.pi * L * B)) ** 1.5  # nm^-3
    return p * 1e24 / NA  # nm^-3 -> L^-1 -> mol/L


def j_wlc(L):
    n = L / B
    return 0.53e-6 * n ** -1.5 * np.exp(-2.66 / n ** 2)


bp = np.logspace(np.log10(60), np.log10(3e4), 500)
L = bp * RISE
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.97, bottom=0.16, top=0.88)
ax = axs[0]
ax.plot(bp, j_gauss(L), color=charts.line("neutral"), lw=1.0, ls="--", label=r"Gaussian chain, $\propto L^{-3/2}$")
ax.plot(bp, j_gauss(L) * np.exp(-2 * np.pi ** 2 * LP / L), color=charts.line("protein"), lw=1.2,
        label="toy model: Gaussian x bending of a circle")
w = bp >= 150
ax.plot(bp[w], j_wlc(L[w]), color=charts.line("dna"), lw=1.6, label="worm-like chain (interpolation)")
i = np.argmax(j_wlc(L))
ax.plot(bp[i], j_wlc(L)[i], "o", color=charts.line("dna"), ms=4)
ax.annotate(f"maximum near {bp[i]:.0f} bp", (bp[i], j_wlc(L)[i]), xytext=(bp[i] * 2.2, 3e-7),
            fontsize=bio.core.FONT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
k = np.argmax(j_gauss(L) * np.exp(-2 * np.pi ** 2 * LP / L))
ax.plot(bp[k], (j_gauss(L) * np.exp(-2 * np.pi ** 2 * LP / L))[k], "o", color=charts.line("protein"), ms=4)
for b0, name in ((92, "lac O1-O3"), (401, "lac O1-O2")):
    ax.axvline(b0, color=P.muted(), lw=0.6, ls=":")
    ax.text(b0 * 1.06, 2e-10, name, rotation=90, fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-10, 3e-6)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "loop length / bp", "J / M")
charts.title(ax, "A  Bending versus entropy")

ax = axs[1]
bp2 = np.arange(150, 801)
L2 = bp2 * RISE
turns = bp2 / 10.5
delta = turns - np.round(turns)
C = 100.0
jt = j_wlc(L2) * np.exp(-2 * np.pi ** 2 * C * delta ** 2 / L2)
ax.plot(bp2, j_wlc(L2) * 1e9, color=charts.line("dna"), lw=1.0, ls="--", label="no phasing requirement")
ax.plot(bp2, jt * 1e9, color=charts.line("dna"), lw=1.4, label="sites on the same face")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right", bbox_to_anchor=(1.0, 0.3))
charts.style_axes(ax, "loop length / bp", "J / nM")
charts.title(ax, "B  Helical phasing")
