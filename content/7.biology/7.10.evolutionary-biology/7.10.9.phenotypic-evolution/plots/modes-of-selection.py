"""Modes of selection on a normally distributed trait (standardized: mean 0, SD 1 before selection).
Top row: the fitness function w(z) (relative survival). Bottom row: the trait density before selection
(grey) and among survivors (coloured), computed exactly on a grid; S is the change in mean and the ratio
gives the variance among survivors relative to before. A: directional (logistic), B: stabilizing
(Gaussian peak at the mean), C: disruptive (Gaussian dip at the mean). D: a two-peaked fitness function
(as for bill depth in crossbills feeding on two kinds of cones) imposes directional, disruptive or
stabilizing selection depending on where the population lies relative to it."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
z = np.linspace(-4, 4, 801)
f0 = evo.normal_pdf(z)

cases = [
    ("A  Directional", evo.fitness(z, "directional", theta=0.3, strength=1.5)),
    ("B  Stabilizing", evo.fitness(z, "stabilizing", theta=0.0, width=1.0)),
    ("C  Disruptive", evo.fitness(z, "disruptive", theta=0.0, width=0.8, strength=0.85)),
]

fig, axs = plt.subplots(2, 4, figsize=(12.5, 5.0), gridspec_kw={"height_ratios": [1, 1.25]})
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.11, top=0.92, wspace=0.28, hspace=0.35)
for k, (title, w) in enumerate(cases):
    a, b = axs[0, k], axs[1, k]
    a.plot(z, w, color=charts.line("enzyme"), lw=2)
    a.set_ylim(0, 1.08)
    a.set_xlim(-3.5, 3.5)
    charts.style_axes(a, None, "fitness $w(z)$" if k == 0 else None)
    charts.title(a, title)
    m = evo.selected_moments(z, f0, w)
    b.fill_between(z, f0, color=P.fill("neutral"), lw=0, alpha=0.6)
    b.plot(z, f0, color=P.muted(), lw=1.2)
    b.plot(z, m["density_sel"], color=charts.line("positive"), lw=2)
    b.axvline(0, color=P.muted(), lw=0.8, ls=":")
    b.axvline(m["mean_sel"], color=charts.line("positive"), lw=0.8, ls=":")
    b.text(-3.4, 0.62, f"$S = {m['S']:.2f}$".replace("-", "−"), fontsize=FT["tiny"], color=P.ink())
    b.text(-3.4, 0.55, f"variance $\\times {m['var_sel']:.2f}$", fontsize=FT["tiny"], color=P.ink())
    b.set_ylim(0, 0.7)
    b.set_xlim(-3.5, 3.5)
    charts.style_axes(b, "trait $z$ (SD units)", "density" if k == 0 else None)

# D: a two-peaked fitness function and three populations
a, b = axs[0, 3], axs[1, 3]
x = np.linspace(-4, 8, 1201)
w2 = 0.15 + 0.8 * np.exp(-0.5 * ((x - 0.0) / 0.9) ** 2) + 0.75 * np.exp(-0.5 * ((x - 4.0) / 0.9) ** 2)
w2 = w2 / w2.max()
a.plot(x, w2, color=charts.line("enzyme"), lw=2)
a.text(0.0, 1.03, "cone type 1", ha="center", fontsize=FT["tiny"], color=P.muted())
a.text(4.0, 0.98, "cone type 2", ha="center", fontsize=FT["tiny"], color=P.muted())
a.set_ylim(0, 1.15)
a.set_xlim(-2.5, 6.5)
charts.style_axes(a, None, None)
charts.title(a, "D  Two-peaked fitness function")
pops = [(1.0, "1", "dna", 0.88), (2.0, "2", "rna", 0.30), (4.0, "3", "plant", 0.88)]
for mu, lab, tok, ty in pops:
    f = evo.normal_pdf(x, mu, 0.55)
    m = evo.selected_moments(x, f, w2)
    b.plot(x, f, color=charts.line(tok), lw=1.1, ls="--")
    b.plot(x, m["density_sel"], color=charts.line(tok), lw=2)
    kind = "directional" if lab == "1" else ("disruptive" if lab == "2" else "stabilizing")
    b.text(mu, ty, f"{lab}: {kind}", ha="center", fontsize=FT["tiny"], color=charts.line(tok))
    b.text(mu, ty - 0.065, f"var $\\times{m['var_sel'] / m['var']:.2f}$", ha="center",
           fontsize=FT["tiny"], color=charts.line(tok))
b.set_ylim(0, 0.95)
b.set_xlim(-2.5, 6.5)
charts.style_axes(b, "trait $z$", None)
