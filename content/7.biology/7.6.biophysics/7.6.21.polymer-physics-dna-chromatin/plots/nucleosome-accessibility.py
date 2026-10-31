"""Energetics of the nucleosome and the accessibility of wrapped DNA.

A: free-energy budget per base pair of wrapped DNA (147 bp in 1.65 turns at a radius of 4.2 nm,
lp = 50 nm): the bending cost lp kBT/(2 R^2) x 0.34 nm, about +0.48 kBT per bp (70 kBT for the whole
core particle), the histone-DNA adhesion (about -0.6 kBT per bp) and their small net difference.
B: the site-exposure model: a site x base pairs inside the nucleosome becomes accessible when the
DNA unwraps spontaneously from the nearer end up to the site, with equilibrium constant
K_exp(x) = K_0 exp(-g x) (g = net wrapping free energy per bp, K_0 = 0.1 for the outermost
contacts); curves for g = 0.1, 0.15 and 0.2 kBT per bp, with the band of measured equilibrium
constants (about 10^-2 near the entry to 10^-5 near the dyad). C: fraction of nucleosomal sites bound
by a protein of dissociation constant Kd for naked DNA, p = K_exp c / (Kd + K_exp c), at three
positions (g = 0.15 kBT per bp): wrapping raises the apparent Kd by the factor 1/K_exp."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
LP, R, RISE = 50.0, 4.2, 0.34
bend = LP / (2 * R ** 2) * RISE

fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.4))
fig.subplots_adjust(wspace=0.4, left=0.07, right=0.98, bottom=0.18, top=0.87)
ax = axs[0]
vals = [bend, -0.63, bend - 0.63]
names = ["bending", "adhesion", "net"]
toks = ["negative", "positive", "dna"]
ax.bar(range(3), vals, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=0.8)
for i, v in enumerate(vals):
    ax.text(i, v + (0.03 if v > 0 else -0.03), f"{v:+.2f}", ha="center", va="bottom" if v > 0 else "top",
            fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_xticks(range(3))
ax.set_xticklabels(names, fontsize=bio.core.FONT["tiny"])
ax.set_ylim(-0.85, 0.7)
charts.style_axes(ax, None, r"free energy / ($k_{\mathrm{B}}T$ per bp)")
charts.title(ax, "A  Budget per base pair")

ax = axs[1]
x = np.linspace(0, 73, 200)
ax.fill_between([5, 70], [1e-2, 1e-5], [3e-2, 3e-5], color=P.fill("neutral"), alpha=0.5, lw=0,
                label="measured range")
for g, tok in ((0.1, "rna"), (0.15, "dna"), (0.2, "protein")):
    ax.plot(x, 0.1 * np.exp(-g * x), color=charts.line(tok), lw=1.3, label=f"g = {g} " + r"$k_{\mathrm{B}}T$/bp")
ax.set_yscale("log")
ax.set_ylim(1e-7, 0.3)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "site position from the entry / bp", r"$K_{\mathrm{exp}}$")
charts.title(ax, "B  Site exposure")

ax = axs[2]
c = np.logspace(-2, 6, 300)  # c / Kd
for xs, tok in ((10, "rna"), (30, "dna"), (60, "protein")):
    K = 0.1 * np.exp(-0.15 * xs)
    ax.plot(c, K * c / (1 + K * c), color=charts.line(tok), lw=1.3, label=f"site at {xs} bp")
ax.plot(c, c / (1 + c), color=P.muted(), lw=1.0, ls="--", label="naked DNA")
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"protein concentration $c/K_{\mathrm{d}}$", "fraction of sites bound")
charts.title(ax, "C  Occlusion raises the apparent Kd")
