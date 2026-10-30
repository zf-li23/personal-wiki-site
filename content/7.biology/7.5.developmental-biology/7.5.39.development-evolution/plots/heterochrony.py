"""Heterochrony in the growth-trajectory model of Alberch, Gould, Oster and Wake (1979) (Formula 39.4.1).

A trait grows linearly from onset time alpha to offset time beta at rate k: z(t) = k (t - alpha) for
alpha <= t <= beta, so the adult value is z* = k (beta - alpha). Ancestor: alpha = 2, beta = 10, k = 1.
A: paedomorphosis (a smaller, juvenile-like adult value): neoteny (k = 0.7), progenesis (beta = 7.6),
postdisplacement (alpha = 4.4); peramorphosis (an exaggerated adult value): acceleration (k = 1.3),
hypermorphosis (beta = 12.4), predisplacement (alpha = -0.4). Each change alters z* by 30 % (+/-2.4 units).
B: shape changes with size. If a part grows allometrically, y = a x^b with b = 1.4 (Definition 34.6.1),
the proportion y / x = a x^(b - 1) rises with body size x. A descendant whose growth stops at a smaller
size (progenesis) keeps the proportions of the ancestor's juvenile (ontogenetic scaling); one that grows
longer exaggerates them. Proportions are relative to the ancestral adult.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def traj(alpha, beta, k, t):
    return np.clip(k * (np.clip(t, alpha, beta) - alpha), 0, None)


t = np.linspace(-1, 14, 600)
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.0), gridspec_kw={"width_ratios": [1.25, 1.0]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.28)
a = axs[0]
cases = [("ancestor", (2, 10, 1.0), P.ink(), "-"),
         ("neoteny (slower rate)", (2, 10, 0.7), charts.line("dna"), "-"),
         ("progenesis (earlier offset)", (2, 7.6, 1.0), charts.line("dna"), (0, (4, 2))),
         ("postdisplacement (later onset)", (4.4, 10, 1.0), charts.line("dna"), (0, (1, 1.5))),
         ("acceleration (faster rate)", (2, 10, 1.3), charts.line("drug"), "-"),
         ("hypermorphosis (later offset)", (2, 12.4, 1.0), charts.line("drug"), (0, (4, 2))),
         ("predisplacement (earlier onset)", (-0.4, 10, 1.0), charts.line("drug"), (0, (1, 1.5)))]
for name, (al, be, k), col, ls in cases:
    a.plot(t, traj(al, be, k, t), color=col, lw=1.8 if name == "ancestor" else 1.4, ls=ls, label=name)
a.axhline(8, color=P.muted(), lw=0.6, ls=(0, (2, 2)))
a.text(13.8, 8.25, "ancestor", fontsize=FT["tiny"], color=P.muted(), ha="right")
a.text(13.8, 6.0, "paedomorphic", fontsize=FT["tiny"], color=charts.line("dna"), ha="right")
a.text(13.8, 11.0, "peramorphic", fontsize=FT["tiny"], color=charts.line("drug"), ha="right")
a.set_xlim(-1, 14)
a.set_ylim(0, 12)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(a, "developmental time t", "trait value z")
charts.title(a, "A  Six ways to change an adult trait")

b = axs[1]
x = np.linspace(0.15, 1.5, 300)
bb = 1.4
ratio = x ** (bb - 1)
b.plot(x, ratio, color=P.ink(), lw=1.6)
for xe, col, txt in ((1.0, P.ink(), "ancestral adult"), (0.45, charts.line("dna"), "progenetic descendant"),
                     (1.35, charts.line("drug"), "hypermorphic descendant")):
    b.plot(xe, xe ** (bb - 1), "o", color=col, ms=6)
    b.text(xe + 0.03, xe ** (bb - 1) - 0.07, txt, fontsize=FT["tiny"], color=col, va="top")
b.set_xlim(0.1, 1.6)
b.set_ylim(0.4, 1.25)
charts.style_axes(b, "body size x (ancestral adult = 1)", "proportion y / x (relative)")
charts.title(b, "B  Stopping growth early keeps juvenile proportions")
