"""Mechanics of kinesin-1: hand-over-hand stepping, force-velocity relation and run lengths.

A: hand-over-hand walking (schematic): the rear head detaches, moves 16 nm forward past the bound head,
and binds the next tubulin dimer; the stalk advances 8 nm per step, one ATP per step.
B: force-velocity curves from a simple two-step kinetic model fitted to optical-trap data
(Visscher, Schnitzer and Block 1999, in outline): forward stepping rate k_f = 1 / (1/(k_b [ATP]) + 1/k_2(F)),
with ATP binding k_b = 2 per uM per s and a load-dependent mechanical step k_2(F) = k_2 exp(-F x / k_B T)
(k_2 = 110 per s, x = 3 nm); backward steps make the velocity v = d (k_f - k_r) vanish at the stall force
F_s = 6 pN, with k_r = k_f exp(-(F_s - F) d / k_B T) (d = 8.2 nm, k_B T = 4.1 pN nm).
C: run lengths of 2000 simulated single molecules that detach with probability 1/125 per step: an
exponential distribution with mean of about 1 um, as measured.
"""

import math

import numpy as np

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import charts, quant
from wikibio import cytoskel as C
from wikibio import physiology as phys

P = bio.P
rng = np.random.default_rng(3)
fig, ax = bio.canvas(27.0, 8.6)

bio.panel(ax, "A", (0.1, 8.5))
for row, (rear, front, lab) in enumerate(((2.0, 3.0, "both heads bound (ADP leaves the front head, ATP binds)"),
                                           (3.0, 4.0, "rear head swung forward by 16 nm: stalk moved 8 nm"))):
    y = 5.0 - row * 3.6
    C.tube(ax, (0.6, y), (9.4, y), width=0.38)
    for x in np.arange(0.9, 9.2, 1.0):
        ax.plot([x, x], [y - 0.19, y + 0.19], color=P.edge("channel"), lw=0.6, zorder=8.5)
    neck = phys.kinesin(ax, (rear, y + 0.45), (front, y + 0.45), ((rear + front) / 2 + 0.5, y + 2.2), head=0.48)
    bio.label(ax, (5.2, y + 2.5), lab, size="tiny")
    ax.add_patch(Circle((rear if row == 0 else front, y + 0.45), 0.09, color=P.fill("highlight"), zorder=20))
bio.arrow(ax, (2.0, 4.3), (4.0, 2.2), kind="process", bend=-0.25, color=P.muted())
bio.label(ax, (0.6, 6.95), "−", size="small", bold=True)
bio.label(ax, (9.6, 6.95), "+", size="small", bold=True)

bio.panel(ax, "B", (10.4, 8.5))
pb = charts.axes_at(ax, (12.1, 1.4, 6.4, 6.0))
d, kT, x, k2, kb, Fs = 8.2, 4.1, 3.0, 110.0, 2.0, 6.0
F = np.linspace(0, 6.5, 200)
for atp, tk in ((1000.0, "enzyme"), (10.0, "protein")):
    kf = 1 / (1 / (kb * atp) + 1 / (k2 * np.exp(-F * x / kT)))
    kr = kf * np.exp(-(Fs - F) * d / kT)
    v = d * (kf - kr)
    pb.plot(F, v, color=quant.line_color(tk), lw=1.8, label=f"[ATP] = {atp:g} µM")
pb.axhline(0, color=P.muted(), lw=0.7)
pb.set_xlim(0, 6.5)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
pb.text(5.0, 60, "stall\n≈ 6 pN", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(pb, "load / pN", "velocity / (nm s⁻¹)")
charts.title(pb, "Force–velocity relation")

bio.panel(ax, "C", (19.6, 8.5))
pc = charts.axes_at(ax, (21.3, 1.4, 5.3, 6.0))
steps = rng.geometric(1 / 125, size=2000)
runs = steps * d / 1000
pc.hist(runs, bins=np.linspace(0, 5, 26), density=True, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.5)
xx = np.linspace(0, 5, 200)
m = runs.mean()
pc.plot(xx, np.exp(-xx / m) / m, color=quant.line_color("ink"), lw=1.4, label=f"exponential, mean {m:.2f} µm")
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pc, "run length / µm", "probability density / µm⁻¹")
charts.title(pc, "Processivity")
