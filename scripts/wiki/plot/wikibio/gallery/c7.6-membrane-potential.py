# Resting membrane potential from ion gradients: typical mammalian concentrations across a membrane with
# K+, Na+, Cl- and Ca2+ channels, the Nernst potential of each ion, the GHK resting potential, and the
# dependence of V_rest on extracellular K+ (Nernst slope versus GHK).
import math

import numpy as np

import wikibio as bio
from wikibio import neuro, quant

P = bio.P
fig, ax = bio.canvas(24.5, 11.2)

# ---- physics: 37 C, typical mammalian neuron ----------------------------------------------------
RT_F = 8.314462618 * 310.15 / 96485.33212 * 1000  # mV
ions = [  # token, symbol, z, outside mM, inside mM
    ("k", "K⁺", 1, 5.0, 140.0),
    ("na", "Na⁺", 1, 145.0, 15.0),
    ("cl", "Cl⁻", -1, 110.0, 10.0),
    ("ca", "Ca²⁺", 2, 2.0, 1e-4),
]
E = {tok: RT_F / z * math.log(o / i) for tok, _, z, o, i in ions}
pK, pNa, pCl = 1.0, 0.05, 0.45


def ghk(Ko, Ki=140.0, Nao=145.0, Nai=15.0, Clo=110.0, Cli=10.0):
    return RT_F * np.log((pK * Ko + pNa * Nao + pCl * Cli) / (pK * Ki + pNa * Nai + pCl * Clo))


Vrest = float(ghk(5.0))


def conc(c):
    return f"{c * 1e6:.0f} nM" if c < 0.01 else f"{c:g} mM"


# ---- A: the membrane and the concentrations -----------------------------------------------------
bio.panel(ax, "A", (0.1, 11.1))
my = 5.4
neuro.patch(ax, 0.9, 11.7, my, depth=4.3, labels=False)
bio.label(ax, (0.55, my + 2.15), "Outside", size="small", rotation=90, color=P.muted())
bio.label(ax, (0.55, my - 2.15), "Inside", size="small", rotation=90, color=P.muted())
cols = [2.2, 4.85, 7.5, 10.15]
for x, (tok, sym, z, co, ci) in zip(cols, ions):
    neuro.channel(ax, x, my, tok, open=True, show_ion=False)
    for c, (y0, seed) in ((co, (my + 1.05, 1)), (ci, (my - 3.45, 2))):
        n = 0 if c < 0.5 else max(1, round(c / 12))
        neuro.ions(ax, (x - 1.05, y0, 2.1, 2.4), tok, n, r=0.13, seed=seed)
    bio.label(ax, (x, 10.4), sym, size="title", bold=True, color=quant.line_color(tok))
    bio.label(ax, (x, my + 3.85), conc(co), size="small")
    bio.label(ax, (x, my - 3.85), conc(ci), size="small")
    sub = sym.rstrip("⁺⁻²")
    bio.label(ax, (x, 0.45), f"$E_{{\\mathrm{{{sub}}}}}$ = {E[tok]:+.0f} mV".replace("-", "−"), size="small",
              color=quant.line_color(tok))

# ---- B: the potentials on one voltage scale -------------------------------------------------------
bio.panel(ax, "B", (12.7, 11.1))
pv = quant.Plot(ax, (14.0, 1.4, 0.01, 8.6), (0, 1), (-100, 140), ylabel="$V$ / mV",
                yticks=[-100, -50, 0, 50, 100], frame="l")
ax.plot([14.0, 14.0], [pv.Y(-100), pv.Y(140)], color=P.muted(), lw=0.8, zorder=6)
marks = [("ca", E["ca"], E["ca"], "$E_{\\mathrm{Ca}}$"), ("na", E["na"], E["na"], "$E_{\\mathrm{Na}}$"),
         ("cl", E["cl"], -50, "$E_{\\mathrm{Cl}}$"), ("neuron", Vrest, -70, "$V_{\\mathrm{rest}}$ (GHK)"),
         ("k", E["k"], -92, "$E_{\\mathrm{K}}$")]
for tok, v, ylab, text in marks:
    c = quant.line_color(tok)
    y, yl = float(pv.Y(v)), float(pv.Y(ylab))
    ax.plot([14.0, 14.45], [y, y], color=c, lw=2.2, solid_capstyle="butt", zorder=8)
    ax.plot([14.45, 14.75], [y, yl], color=c, lw=0.8, zorder=8)
    bio.label(ax, (14.85, yl), f"{text}  {v:+.0f}".replace("-", "−"), size="small", ha="left", color=c)

# ---- C: V_rest against extracellular K+ ---------------------------------------------------------------
X1, W1 = 19.4, 4.6
Ko = np.logspace(0, np.log10(300), 200)
pc = quant.Plot(ax, (X1, 4.3, W1, 5.7), (1, 300), (-140, 40), xlog=True, xlabel="$[\\mathrm{K}^+]_{\\mathrm{o}}$ / mM",
                ylabel="$V$ / mV", xticks=[1, 10, 100], yticks=[-120, -80, -40, 0, 40], grid=True)
bio.panel(ax, "C", (X1 - 1.5, 11.1))
pc.line(Ko, RT_F * np.log(Ko / 140.0), "k", dashed=True, lw=1.6)
pc.line(Ko, ghk(Ko), "neuron", lw=2.0)
pc.points([5.0], [Vrest], "neuron", r=0.09)
pc.text(4.6, Vrest + 7, "physiological", ha="right", va="bottom", size="tiny")
pc.text(7, -112, "Nernst $E_{\\mathrm{K}}$:\n61.5 mV per decade", ha="left", va="center", token="k")
pc.text(1.15, -35, "GHK", ha="left", va="center", token="neuron", size="small")
pc.vline(140, "muted")
pc.text(125, 30, "$[\\mathrm{K}^+]_{\\mathrm{o}} = [\\mathrm{K}^+]_{\\mathrm{i}}$", ha="right", va="center", color=P.muted())

# equations
bio.box(ax, (X1 + W1 / 2 - 0.9, 1.55), 7.0, 2.6, "neutral")
bio.label(ax, (X1 + W1 / 2 - 0.9, 2.3),
          "$E_X = \\dfrac{RT}{zF}\\ln\\dfrac{[X]_{\\mathrm{o}}}{[X]_{\\mathrm{i}}}$", size="small", color=P.on_fill())
bio.label(ax, (X1 + W1 / 2 - 0.9, 1.3),
          "$V_{\\mathrm{rest}} = \\dfrac{RT}{F}\\ln\\dfrac{p_{\\mathrm{K}}[\\mathrm{K}]_{\\mathrm{o}} + p_{\\mathrm{Na}}[\\mathrm{Na}]_{\\mathrm{o}}"
          " + p_{\\mathrm{Cl}}[\\mathrm{Cl}]_{\\mathrm{i}}}{p_{\\mathrm{K}}[\\mathrm{K}]_{\\mathrm{i}} + p_{\\mathrm{Na}}[\\mathrm{Na}]_{\\mathrm{i}}"
          " + p_{\\mathrm{Cl}}[\\mathrm{Cl}]_{\\mathrm{o}}}$", size="small", color=P.on_fill())
bio.label(ax, (X1 + W1 / 2 - 0.9, 0.65), "37 °C;  $p_{\\mathrm{K}} : p_{\\mathrm{Na}} : p_{\\mathrm{Cl}}$ = 1 : 0.05 : 0.45",
          size="tiny", color=P.on_fill(), va="top")
