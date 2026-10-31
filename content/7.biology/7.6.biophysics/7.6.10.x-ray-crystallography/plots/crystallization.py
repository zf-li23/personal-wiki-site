# Protein crystallization: the phase diagram and classical nucleation theory.
# A: schematic phase diagram at constant temperature, protein concentration c against precipitant
#    concentration. Solubility curve c_s = 25 exp(-x / 6) mg/mL (x in % w/v) and the supersolubility
#    (spontaneous nucleation) boundary at about 3.5 c_s; above about 9 c_s the protein precipitates as
#    an amorphous solid. A vapor-diffusion drop starts below saturation (protein 8 mg/mL and precipitant
#    6 % after mixing 1:1 with a 12 % reservoir); as water leaves, both concentrations rise in
#    proportion (path through the origin) until the drop reaches the reservoir precipitant concentration,
#    here inside the nucleation zone; crystals then nucleate and grow, and the protein concentration in
#    solution falls toward the solubility curve. Seeding a drop in the metastable zone gives growth
#    without new nuclei.
# B: free energy of a spherical nucleus, Delta G(n) = -n k_B T ln S + gamma' n^(2/3), with
#    gamma' = 6 k_B T per (molecule)^(2/3) and supersaturations S = 2, 3, 5; the maximum gives the
#    critical nucleus n* = (2 gamma' / (3 ln S))^3 and the barrier Delta G* = 4 gamma'^3 / (27 (ln S)^2).
# C: relative nucleation rate J ~ exp(-Delta G* / k_B T) against S on a log scale: it rises by many
#    orders of magnitude over a small range of S, which is why a metastable zone exists.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.3), gridspec_kw={"width_ratios": [1.35, 1, 1]})

ax = axs[0]
x = np.linspace(0, 20, 400)
cs = 25 * np.exp(-x / 6)
cn = 3.5 * cs
cp = 9 * cs
top = 40
ax.fill_between(x, 0, cs, color=P.fill("neutral"), alpha=0.25, lw=0)
ax.fill_between(x, cs, cn, color=P.fill("positive"), alpha=0.3, lw=0)
ax.fill_between(x, cn, np.minimum(cp, top), color=P.fill("highlight"), alpha=0.35, lw=0)
ax.fill_between(x, np.minimum(cp, top), top, color=P.fill("negative"), alpha=0.3, lw=0)
ax.plot(x, cs, color=charts.line("dna"), lw=1.8)
ax.plot(x, cn, color=charts.line("highlight"), lw=1.2, ls=(0, (4, 2)))
ax.plot(x, cp, color=charts.line("negative"), lw=1.0, ls=(0, (1, 1.5)))
ax.text(1.0, 4.0, "undersaturated", fontsize=8, color=ink)
ax.text(14.3, 3.4, "metastable", fontsize=8, color=ink)
ax.text(13.0, 17.5, "nucleation", fontsize=8, color=ink)
ax.text(14.5, 33.0, "precipitation", fontsize=8, color=ink)
ax.text(17.2, 1.55, "solubility", fontsize=7.5, color=charts.line("dna"), rotation=-6)
# vapor diffusion path: from (6, 8) to (12, 16), then down to the solubility curve
p0, p1 = np.array([6.0, 8.0]), np.array([12.0, 16.0])
ax.plot(*p0, "o", color=ink, ms=5)
ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle="-|>", mutation_scale=11, color=ink, lw=1.5))
c_end = 25 * np.exp(-12 / 6) * 1.05
ax.add_patch(FancyArrowPatch(tuple(p1), (12.0, c_end), arrowstyle="-|>", mutation_scale=11, color=ink,
                             lw=1.5, ls=(0, (3, 2))))
ax.text(4.6, 8.6, "drop", fontsize=8, color=ink)
ax.text(6.0, 13.6, "vapor\ndiffusion", fontsize=8, color=ink)
ax.text(12.3, 6.0, "crystal\ngrowth", fontsize=8, color=ink)
ax.set_xlim(0, 20)
ax.set_ylim(0, top)
ax.set_title("A  phase diagram", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "precipitant / % (w/v)", "protein / (mg mL$^{-1}$)")

ax = axs[1]
n = np.linspace(0, 400, 600)
g = 6.0
for S, tok in ((2, "dna"), (3, "protein"), (5, "highlight")):
    dG = -n * np.log(S) + g * n ** (2 / 3)
    ns = (2 * g / (3 * np.log(S))) ** 3
    gs = 4 * g**3 / (27 * np.log(S) ** 2)
    ax.plot(n, dG, color=charts.line(tok), lw=1.7, label=f"S = {S}")
    ax.plot(ns, gs, "o", color=charts.line(tok), ms=5)
ax.axhline(0, color=muted, lw=0.7)
ax.set_ylim(-60, 130)
ax.legend(fontsize=8, frameon=False)
ax.text(200, 75, r"maximum: $n^*$, $\Delta G^*$", fontsize=8, color=ink)
ax.set_title("B  nucleation barrier", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "molecules in nucleus n", r"$\Delta G$ / $k_{\mathrm{B}}T$")

ax = axs[2]
S = np.linspace(1.6, 8, 300)
dGs = 4 * g**3 / (27 * np.log(S) ** 2)
J = np.exp(-dGs)
ax.semilogy(S, J / J[-1], color=charts.line("protein"), lw=1.8)
ax.set_ylim(1e-30, 3)
ax.set_title("C  nucleation rate", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "supersaturation S = c / c$_s$", r"$J / J(S = 8)$")
fig.tight_layout()
