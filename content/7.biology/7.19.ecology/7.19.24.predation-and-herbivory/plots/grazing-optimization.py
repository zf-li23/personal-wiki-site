"""A mechanistic model of the grazing optimization hypothesis (McNaughton 1979), with simulated parameters.

Leaf area L of a sward: dL/dt = f(L) - (m + mu + g) L, where f(L) = a (1 - exp(-k L)) is canopy
photosynthesis with self-shading (a = 10, k = 0.5), m = 1 the maintenance cost, mu = 0.3 the senescence
(turnover) rate and g the grazing rate. Net primary production NPP = f(L*) - m L* at the steady state
L*(g). A: NPP and the offtake by grazers g L* against the grazing rate: because the ungrazed canopy is
denser than the leaf area L_opt = ln(a k / m) / k at which NPP is maximal, moderate grazing removes
shaded, unproductive leaves and increases NPP (overcompensation at the scale of the sward); heavy
grazing decreases it. Offtake is maximal at an intermediate grazing rate, as in harvesting theory.
B: the steady-state leaf area L*(g) with L_opt marked.
"""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
a, k, m, mu = 10.0, 0.5, 1.0, 0.3
f = lambda L: a * (1 - np.exp(-k * L))
gs = np.linspace(0, 3.4, 300)
Ls = []
for g in gs:
    h = lambda L: f(L) - (m + mu + g) * L
    Ls.append(brentq(h, 1e-6, 50) if h(1e-6) > 0 and a * k > (m + mu + g) else 0.0)
Ls = np.array(Ls)
npp = f(Ls) - m * Ls
off = gs * Ls
Lopt = np.log(a * k / m) / k

pa = C.axes_at(ax, (2.4, 1.8, 11.5, 8.6))
pa.plot(gs, npp, color=Q.line_color("plant"), lw=1.9, label="net primary production")
pa.plot(gs, off, color=Q.line_color("rna"), lw=1.6, ls=(0, (4, 2)), label="offtake by grazers")
pa.axhline(npp[0], color=P.muted(), lw=0.7, ls=(0, (2, 2)))
pa.text(3.3, npp[0] + 0.12, "ungrazed NPP", fontsize=FS["tiny"], color=P.muted(), ha="right")
pa.set_xlim(0, 3.4)
pa.set_ylim(0, None)
C.style_axes(pa, "grazing rate g (per unit time)", "rate (biomass per unit area and time)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Production and offtake", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
pb.plot(gs, Ls, color=Q.line_color("plant"), lw=1.9)
pb.axhline(Lopt, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(3.3, Lopt + 0.2, "leaf area maximizing NPP", fontsize=FS["tiny"], color=P.muted(), ha="right")
pb.set_xlim(0, 3.4)
pb.set_ylim(0, None)
C.style_axes(pb, "grazing rate g (per unit time)", "steady-state leaf area L*")
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "Canopy density", size="small", bold=True, ha="left")
