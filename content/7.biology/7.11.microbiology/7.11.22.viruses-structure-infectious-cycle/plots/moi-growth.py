# Multiplicity of infection and the one-step growth curve.
# A: the Poisson distribution of particles per cell at MOI = 0.1, 1 and 5.
# B: the fractions of cells receiving none, exactly one and more than one particle as functions of the
#    multiplicity m, with the fraction infected 1 - exp(-m) and the value m = 4.6 needed to infect 99 %.
# C: a schematic one-step growth curve (model: eclipse 10 min; intracellular particles accumulate
#    linearly to a burst of 100; lysis times normal, mean 25 min, s.d. 3 min), showing the total
#    infectious virus in the culture, the free virus in the medium, and for comparison the gradual
#    curve of a virus released continuously by budding.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial
from scipy.stats import norm

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(13.6, 4.2))
gs = fig.add_gridspec(1, 3, width_ratios=[1.1, 1.0, 1.25], wspace=0.32)

# ---------------------------------------------------------------- A: Poisson
ax = fig.add_subplot(gs[0, 0])
k = np.arange(0, 11)
w = 0.26
for i, (m, tok) in enumerate(((0.1, "dna"), (1.0, "drug"), (5.0, "enzyme"))):
    p = np.exp(-m) * m ** k / factorial(k)
    ax.bar(k + (i - 1) * w, p, width=w, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6,
           label=f"MOI $m$ = {m:g}")
ax.set_xticks(k)
ax.set_ylim(0, 1.0)
ax.legend(fontsize=7, frameon=False, labelcolor=P.ink())
charts.style_axes(ax, "particles entering a cell, $k$", "$\\mathbb{P}(k)$")
charts.title(ax, "A   Particles per cell are Poisson")
ax.annotate("at $m$ = 1: 37 % get none,\n37 % one, 26 % two or more", (2.6, 0.62), fontsize=7, color=P.muted())

# ---------------------------------------------------------------- B: fractions infected
ax = fig.add_subplot(gs[0, 1])
m = np.linspace(0, 6, 400)
ax.plot(m, np.exp(-m), color=charts.line("neutral"), lw=2.0, label="none: $\\mathrm{e}^{-m}$")
ax.plot(m, m * np.exp(-m), color=charts.line("dna"), lw=2.0, label="exactly one: $m\\mathrm{e}^{-m}$")
ax.plot(m, 1 - (1 + m) * np.exp(-m), color=charts.line("drug"), lw=2.0, label="more than one")
ax.plot(m, 1 - np.exp(-m), color=charts.line("positive"), lw=2.0, ls=(0, (4, 2.2)), label="infected: $1-\\mathrm{e}^{-m}$")
ax.axvline(4.6, color=P.muted(), lw=0.8, ls=":")
ax.text(4.72, 0.06, "$m$ = 4.6 infects 99 %", fontsize=7, color=P.muted(), va="bottom", ha="left")
ax.set_xlim(0, 6)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False, loc="center right", labelcolor=P.ink())
charts.style_axes(ax, "multiplicity of infection $m$", "fraction of cells")
charts.title(ax, "B   What a multiplicity means")

# ---------------------------------------------------------------- C: one-step growth
ax = fig.add_subplot(gs[0, 2])
t = np.linspace(0, 45, 600)
eclipse, mean_lysis, sd, burst = 10.0, 25.0, 3.0, 100.0
F = norm.cdf(t, mean_lysis, sd)                       # fraction of cells that have lysed
inside = np.clip((t - eclipse) / (mean_lysis - eclipse), 0, None) * burst   # particles per unlysed cell
total = (1 - F) * np.maximum(1, inside) + F * burst   # infective centres: unlysed cells count as one each
free = F * burst
budding = burst * np.clip((t - eclipse) / 30.0, 0, None) ** 1.3
ax.plot(t, total, color=charts.line("dna"), lw=2.0, label="total infectious virus (artificially lysed)")
ax.plot(t, free, color=charts.line("drug"), lw=2.0, ls=(0, (4, 2.2)), label="free virus in the medium")
ax.plot(t, budding, color=charts.line("neutral"), lw=1.6, ls=(0, (1, 1.8)), label="a virus released by budding")
ax.set_yscale("log")
ax.set_ylim(0.45, 300)
ax.set_xlim(0, 45)
for x0, x1, txt, tok in ((0, eclipse, "eclipse", "highlight"), (eclipse, mean_lysis - 3.5, "maturation", "neutral"),
                         (mean_lysis - 3.5, mean_lysis + 6, "rise", "positive")):
    ax.axvspan(x0, x1, color=P.mix(P.fill(tok), P.surface(), 0.78 if not P.is_dark() else 0.86), zorder=0)
    ax.text((x0 + x1) / 2, 215, txt, fontsize=7, color=P.muted(), ha="center", va="top")
ax.annotate("", xy=(mean_lysis + 8, 1), xytext=(mean_lysis + 8, burst),
            arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9))
ax.text(mean_lysis + 8.6, 10, "burst size\n= 100", fontsize=7, color=P.muted(), va="center")
ax.annotate("", xy=(0.3, 0.62), xytext=(mean_lysis - 3.2, 0.62),
            arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9))
ax.text(10.5, 0.55, "latent period", fontsize=7, color=P.muted(), ha="center", va="top")
ax.legend(fontsize=7, frameon=False, loc="center left", labelcolor=P.ink())
charts.style_axes(ax, "time after infection / min", "infectious units per infected cell")
charts.title(ax, "C   One-step growth")
