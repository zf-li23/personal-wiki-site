"""Ecosystem development (Odum 1969) in a minimal carbon-balance model.

Autotrophic succession: biomass B (kg C m^-2) grows by gross production P = Pmax B/(B + K), which saturates
as the canopy closes (Pmax = 2 kg C m^-2 per year, K = 1), and loses carbon by community respiration
R = rho B (rho = 0.1 per year, maintenance and decomposition of litter); dB/dt = P - R, starting from
B = 0.02. Heterotrophic succession: a pulse of dead organic matter O = 10 (a whale carcass or an organic
effluent) is respired at rate k O (k = 0.15 per year) while autotrophs A colonize as in the first model
with a lower ceiling (Pmax = 0.6); R = k O + rho A. A: P, R and B in autotrophic succession. B: P/R on a
log scale for both types: it starts above 1 (autotrophic) or below 1 (heterotrophic) and tends to 1 at
maturity; in the heterotrophic case P/R briefly exceeds 1 once the carcass is consumed and the autotrophs are still accumulating biomass. C: net ecosystem production P - R and the biomass supported per unit of production B/P in
autotrophic succession: NEP peaks early and declines to zero while B/P keeps rising.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT

Pmax, K, rho = 2.0, 1.0, 0.1
t = np.linspace(0, 120, 1201)
sa = solve_ivp(lambda tt, y: [Pmax * y[0] / (y[0] + K) - rho * y[0]], (0, 120), [0.02], t_eval=t, rtol=1e-8)
Ba = sa.y[0]
Pa = Pmax * Ba / (Ba + K)
Ra = rho * Ba

Pmh, kO = 0.6, 0.15


def het(tt, y):
    O, A = y
    return [-kO * O, Pmh * A / (A + K) - rho * A]


sh = solve_ivp(het, (0, 120), [10.0, 0.02], t_eval=t, rtol=1e-8)
O, A = sh.y
Ph = Pmh * A / (A + K)
Rh = kO * O + rho * A

fig, ax = bio.canvas(31.0, 10.0)

pa = C.axes_at(ax, (2.2, 1.6, 7.0, 6.8))
pa.plot(t, Pa, color=Q.line_color("plant"), lw=1.7, label="gross production P")
pa.plot(t, Ra, color=Q.line_color("negative"), lw=1.7, label="community respiration R")
pa.set_xlim(0, 120)
pa.set_ylim(0, 2.1)
C.style_axes(pa, "years", "flux (kg C m⁻² yr⁻¹)")
pa2 = pa.twinx()
pa2.plot(t, Ba, color=Q.line_color("dna"), lw=1.4, ls=(0, (4, 2)))
pa2.set_ylim(0, 30)
C.style_axes(pa2, None, "biomass B (kg C m⁻²)")
pa2.spines["right"].set_visible(True)
pa.plot([], [], color=Q.line_color("dna"), lw=1.4, ls=(0, (4, 2)), label="biomass B (right axis)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Autotrophic succession", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.4, 1.6, 7.0, 6.8))
pb.semilogy(t, Pa / Ra, color=Q.line_color("plant"), lw=1.7, label="autotrophic (bare rock, old field)")
pb.semilogy(t, Ph / Rh, color=Q.line_color("enzyme"), lw=1.7, label="heterotrophic (carcass, organic effluent)")
pb.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(118, 1.12, "P/R = 1 (mature)", fontsize=FS["tiny"], color=P.muted(), ha="right")
pb.set_xlim(0, 120)
pb.set_ylim(0.005, 50)
C.style_axes(pb, "years", "P/R")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (10.9, 9.6))
bio.label(ax, (12.4, 9.2), "P/R tends to 1", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.6, 1.6, 7.0, 6.8))
pc.plot(t, Pa - Ra, color=Q.line_color("protein"), lw=1.7, label="net ecosystem production P − R")
pc.set_xlim(0, 120)
pc.set_ylim(0, 1.9)
C.style_axes(pc, "years", "P − R (kg C m⁻² yr⁻¹)")
pc2 = pc.twinx()
pc2.plot(t, Ba / Pa, color=Q.line_color("dna"), lw=1.4, ls=(0, (4, 2)))
pc2.set_ylim(0, 11)
C.style_axes(pc2, None, "B/P (years)")
pc2.spines["right"].set_visible(True)
pc.plot([], [], color=Q.line_color("dna"), lw=1.4, ls=(0, (4, 2)), label="B/P (right axis)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "C", (21.1, 9.6))
bio.label(ax, (22.6, 9.2), "Production and biomass", size="small", bold=True, ha="left")
