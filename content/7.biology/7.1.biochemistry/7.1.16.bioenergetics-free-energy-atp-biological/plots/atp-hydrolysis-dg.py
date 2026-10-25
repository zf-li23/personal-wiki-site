"""Phosphorylation potential: actual Gibbs energy of ATP hydrolysis at 37 C.

A: dG = dG'0 + RT ln Q with dG'0 = -30.5 kJ/mol and Q = [ADP][Pi]/[ATP] (M), against log10 Q.
Equilibrium at Q = K' = exp(30.5/RT) = 1.4e5 M. Points: total nucleotide concentrations of
four cell types (Lehninger 8e, Table 13-5; Veech et al. 1979).
B: the same phosphorylation potentials as bars, plus resting muscle with free ADP = 25 uM."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
RT = 8.314462618e-3 * 310.15
G0 = -30.5
cells = [("Hepatocyte", 3.38, 1.32, 4.8), ("Myocyte", 8.05, 0.93, 8.05),
         ("Neuron", 2.59, 0.73, 2.72), ("Erythrocyte", 2.25, 0.25, 1.65)]

fig, ax = bio.canvas(22.0, 8.6)
bio.panel(ax, "A", (0.1, 8.4))
a = charts.axes_at(ax, (1.6, 1.2, 10.4, 6.4))
lq = np.linspace(-10, 7, 300)
a.plot(lq, G0 + RT * np.log(10) * lq, color=charts.line("atp"), lw=2.0)
a.axhline(0, color=P.muted(), lw=0.8)
lk = -G0 / (RT * np.log(10))
a.plot([lk], [0], "o", ms=6, color=charts.line("neutral"))
a.annotate("equilibrium\nQ = K′", (lk, 0), (lk - 3.2, 9), fontsize=bio.core.FONT["tiny"], color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
a.plot([0], [G0], "s", ms=6, color=charts.line("neutral"))
a.annotate("standard state\nQ = 1 M", (0, G0), (0.6, -40), fontsize=bio.core.FONT["tiny"], color=P.ink())
toks = ["enzyme", "muscle", "neuron", "blood"]
for (name, atp, adp, pi), t in zip(cells, toks):
    q = np.log10(adp * 1e-3 * pi * 1e-3 / (atp * 1e-3))
    a.plot([q], [G0 + RT * np.log(10) * q], "o", ms=7, color=charts.line(t))
    yv = G0 + RT * np.log(10) * q
    ty = {"Hepatocyte": -40, "Myocyte": -48, "Neuron": -56, "Erythrocyte": -64}[name]
    a.annotate(name, (q, yv), (-9.2, ty), fontsize=bio.core.FONT["tiny"], color=P.ink(), va="center",
               arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
a.set_xlim(-10, 7)
a.set_ylim(-80, 25)
charts.style_axes(a, r"$\log_{10}(Q/\mathrm{M})$,  $Q = [\mathrm{ADP}][\mathrm{P_i}]/[\mathrm{ATP}]$",
                  r"$\Delta G_{\mathrm{p}}$ / (kJ mol$^{-1}$)")
charts.title(a, "ATP hydrolysis at 37 °C")

bio.panel(ax, "B", (13.0, 8.4))
b = charts.axes_at(ax, (14.6, 1.2, 7.0, 6.4))
names = ["Standard"] + [c[0] for c in cells] + ["Muscle,\nfree ADP"]
vals = [G0] + [G0 + RT * np.log(adp * 1e-3 * pi * 1e-3 / (atp * 1e-3)) for _, atp, adp, pi in cells]
vals.append(G0 + RT * np.log(25e-6 * 8.05e-3 / 8.05e-3))
cols = ["neutral"] + toks + ["muscle"]
y = np.arange(len(vals))[::-1]
b.barh(y, vals, color=[P.fill(c) for c in cols], edgecolor=[P.edge(c) for c in cols], lw=0.8)
for yy, v in zip(y, vals):
    b.text(v - 1, yy, f"{v:.1f}", ha="right", va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_yticks(y)
b.set_yticklabels(names)
b.set_xlim(-70, 0)
charts.style_axes(b, r"$\Delta G_{\mathrm{p}}$ / (kJ mol$^{-1}$)")
charts.title(b, "Phosphorylation potential in cells")
