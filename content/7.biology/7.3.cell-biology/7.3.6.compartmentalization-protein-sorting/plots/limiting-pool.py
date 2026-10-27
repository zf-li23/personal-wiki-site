"""Organelle size set by a limiting pool of building blocks (Goehring and Hyman 2012).

Subunits are made in proportion to cell volume (total amount N = rho V). The organelle grows by
assembly at a rate k_on c, where c = (N - S)/V is the free subunit concentration, and loses subunits
at a constant rate k_off, so dS/dt = k_on (N - S)/V - k_off. At steady state c = c* = k_off / k_on
and S* = (rho - c*) V: organelle size scales with cell volume. Units: rho = 1, c* = 0.4 (arbitrary
units per unit volume); k_on = 1, so that the time to steady state is of order V / k_on.
A: growth from S = 0 in cells of volume 1, 2 and 4 (concentrations equal, amounts proportional to V).
B: steady-state size against cell volume for the limiting-pool model, with 8 % noise in expression
(points); dashed: lower expression per volume (rho = 0.7) lowers the slope, a test of the model;
compared with an organelle whose size is set by an intrinsic ruler (constant).
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(22.0, 8.0)
rho, cstar, kon = 1.0, 0.4, 1.0
koff = kon * cstar

bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.7, 1.3, 8.2, 5.8))
t = np.linspace(0, 15, 400)
for V, tok in ((1, "dna"), (2, "protein"), (4, "negative")):
    N = rho * V
    S = (N - cstar * V) * (1 - np.exp(-kon * t / V))
    pa.plot(t, S, color=charts.line(tok), lw=1.9, label=f"cell volume V = {V}")
    pa.axhline((rho - cstar) * V, color=charts.line(tok), lw=0.6, ls=(0, (2, 2)))
pa.set_xlim(0, 15)
pa.set_ylim(0, 2.6)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "time (a.u.)", "organelle size S (subunits)")
charts.title(pa, "Growth until the pool is depleted to c*")

bio.panel(ax, "B", (11.3, 7.8))
pb = charts.axes_at(ax, (12.9, 1.3, 7.6, 5.8))
V = np.linspace(0.5, 5, 200)
pb.plot(V, (rho - cstar) * V, color=charts.line("protein"), lw=2.0, label="limiting pool, ρ = 1")
pb.plot(V, (0.7 - cstar) * V, color=charts.line("protein"), lw=1.2, ls=(0, (3, 2)), label="limiting pool, ρ = 0.7")
Vs = rng.uniform(0.6, 5, 60)
Ss = (rho * Vs * (1 + 0.08 * rng.standard_normal(60)) - cstar * Vs)
pb.plot(Vs, Ss, "o", ms=3.2, color=charts.line("protein"), alpha=0.8)
pb.axhline(1.2, color=charts.line("neutral"), lw=2.0, ls=(0, (5, 2)), label="intrinsic ruler")
pb.set_xlim(0, 5.2)
pb.set_ylim(0, 3.5)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, "cell volume V (a.u.)", "steady-state size S*")
charts.title(pb, "Size scales with cell volume")
