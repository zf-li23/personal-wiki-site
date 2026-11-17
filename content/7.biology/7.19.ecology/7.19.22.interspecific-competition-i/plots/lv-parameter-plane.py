"""Outcomes of Lotka-Volterra competition in the plane of the scaled competition coefficients.

With x = N1/K1, y = N2/K2 the model has two parameters that decide the outcome: a = a12 K2/K1 (the
effect of species 2 at its carrying capacity on species 1, relative to species 1 at its own) and
b = a21 K1/K2. A: species 1 can invade a population of species 2 iff a < 1, species 2 can invade
species 1 iff b < 1; the four quadrants are the four outcomes, and the curve ab = 1 is where the
interior equilibrium moves to infinity (it exists, with positive densities, only in the
coexistence and bistable quadrants). Points: the parameters of the phase portraits of Figure 1.
B: equilibrium densities for K1 = K2 = 100 and a12 = 0.5 as the effect of species 1 on species 2,
a21, increases: N1* = (K1 - a12 K2)/(1 - a12 a21) and N2* = (K2 - a21 K1)/(1 - a12 a21) while a21 < 1;
species 2 is excluded beyond a21 = K2/K1 = 1 (b = 1), where the interior equilibrium collides with
(K1, 0) in a transcritical bifurcation.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

pa = C.axes_at(ax, (2.4, 1.8, 9.5, 8.6))
m = 2.0
shade = lambda tok: P.mix(P.fill(tok), P.surface(), 0.55)
pa.fill_between([0, 1], 0, 1, color=shade("positive"), lw=0)
pa.fill_between([1, m], 1, m, color=shade("neutral"), lw=0)
pa.fill_between([0, 1], 1, m, color=shade("dna2"), lw=0)
pa.fill_between([1, m], 0, 1, color=shade("rna"), lw=0)
pa.axvline(1, color=P.ink(), lw=1.0)
pa.axhline(1, color=P.ink(), lw=1.0)
aa = np.linspace(0.5, m, 200)
pa.plot(aa, 1 / aa, color=P.muted(), lw=1.0, ls=(0, (3, 2)))
pa.text(0.5, 0.5, "stable\ncoexistence", ha="center", va="center", fontsize=FS["small"], color=P.ink())
pa.text(1.5, 1.5, "bistable:\nprior residence wins", ha="center", va="center", fontsize=FS["small"], color=P.ink())
pa.text(0.32, 1.82, "species 1 wins", ha="center", va="center", fontsize=FS["small"], color=P.ink())
pa.text(1.55, 0.2, "species 2 wins", ha="center", va="center", fontsize=FS["small"], color=P.ink())
pa.text(1.62, 0.66, "ab = 1", fontsize=FS["tiny"], color=P.muted())
for a, b, tag in [(0.6, 1.4, "A"), (1.4, 0.6, "B"), (1.5, 1.3, "C"), (0.5, 0.6, "D")]:
    pa.plot(a, b, "o", ms=4.5, color=P.ink())
    pa.text(a + 0.04, b + 0.04, tag, fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, m)
pa.set_ylim(0, m)
C.style_axes(pa, r"$a = \alpha_{12}K_2/K_1$ (effect of species 2 on 1)", r"$b = \alpha_{21}K_1/K_2$")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Four outcomes", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
K1 = K2 = 100.0
a12 = 0.5
a21 = np.linspace(0, 1.6, 400)
det = 1 - a12 * a21
n1 = np.where(a21 < 1, (K1 - a12 * K2) / det, K1)
n2 = np.where(a21 < 1, (K2 - a21 * K1) / det, 0)
pb.plot(a21, n1, color=Q.line_color("dna"), lw=1.8, label="species 1, $N_1^*$")
pb.plot(a21, n2, color=Q.line_color("rna"), lw=1.8, label="species 2, $N_2^*$")
pb.plot(a21, n1 + n2, color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="total")
pb.axvline(1, color=P.muted(), lw=0.8)
pb.text(1.02, 140, "species 2\nexcluded", fontsize=FS["tiny"], color=P.muted(), va="center")
pb.set_xlim(0, 1.6)
pb.set_ylim(0, 160)
C.style_axes(pb, r"effect of species 1 on species 2, $\alpha_{21}$", "equilibrium density")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), r"Equilibria for $K_1 = K_2 = 100$, $\alpha_{12} = 0.5$", size="small", bold=True, ha="left")
