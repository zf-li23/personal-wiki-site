"""Spread of a driving allele D that is lethal (or sterile) when homozygous (Formula 17.6.2). A: frequency
of carriers (Dd) among adults over generations when heterozygous males transmit D to a fraction k of their
sperm and females are Mendelian (as for t haplotypes of the house mouse), for three values of k; dashed:
drive in both sexes with k = 0.8. B: equilibrium carrier frequency as a function of k for male-only drive
(iteration; closed form 1 - sqrt((1 - k)/k)) and for drive in both sexes ((2k - 1)/k)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P


def step(h, km, kf):
    """h: fraction of Dd among adults (DD die). Return h in the next generation."""
    pm, pf = h * km, h * kf
    dd_ = pm * pf
    het = pm * (1 - pf) + pf * (1 - pm)
    return het / (1 - dd_)


def run(km, kf, h0=0.01, g=60):
    hs = [h0]
    for _ in range(g):
        hs.append(step(hs[-1], km, kf))
    return np.array(hs)


fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
ax = axs[0]
for k, tok in ((0.6, "enzyme"), (0.8, "dna"), (0.95, "receptor")):
    ax.plot(run(k, 0.5), color=charts.line(tok), lw=1.5, label=f"male drive, k = {k}")
ax.plot(run(0.8, 0.8), color=charts.line("dna"), lw=1.2, ls="--", label="both sexes, k = 0.8")
ax.set_ylim(0, 1)
charts.style_axes(ax, "generations", "carriers Dd among adults")
charts.title(ax, "A  Spread from 1 % carriers")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
ax = axs[1]
ks = np.linspace(0.5, 1.0, 101)
eq_m = [run(k, 0.5, h0=0.3, g=2000)[-1] for k in ks]
pstar = np.clip(2 * ks - 1, 0, 1)
eq_b = [2 * p * (1 - p) / (1 - p * p) if p < 1 else 1 for p in pstar]
ax.plot(ks, eq_m, color=charts.line("receptor"), lw=1.5, label="male-only drive")
ax.plot(ks, eq_b, color=charts.line("dna"), lw=1.5, ls="--", label="drive in both sexes")
ax.set_ylim(0, 1)
charts.style_axes(ax, "transmission ratio k", "equilibrium carriers")
charts.title(ax, "B  Equilibrium")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
