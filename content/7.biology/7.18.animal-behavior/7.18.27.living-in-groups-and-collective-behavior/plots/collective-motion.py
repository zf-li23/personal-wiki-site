"""The zone model of collective motion (Couzin et al. 2002), in two dimensions.

A: the three zones around an individual: repulsion (avoid collisions), orientation (align with neighbours) and
attraction (approach neighbours), with a blind sector behind. B-D: groups of 40 after 500 steps for three widths of
the orientation zone (repulsion radius 1, attraction radius 14): a swarm without alignment, a rotating torus
(mill) and a polarized group moving in one direction; P is the polarization |mean heading| and M the normalized
angular momentum about the centroid at the final step. E: P and M over the last 50 of 500 steps (mean of 6 runs
each, random starts) against the radius of the orientation zone: the group changes state abruptly as a single
individual-level parameter changes.
"""

import numpy as np
import wikibio as bio
import wikibehav as wb
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(36.0, 11.0)
bio.panel(ax, "A", (0.2, 10.8))
wb.zones(ax, (3.9, 5.0), 0.8, 2.0, 3.4, heading=90, blind=90)
for k, (name, x) in enumerate((("swarm", 8.2), ("torus", 14.4), ("parallel", 20.6))):
    pos, head = wb.couzin(n=40, steps=500, seed=k, **wb.COUZIN_REGIMES[name])
    to = wb.fit(pos[-25:], (x, 1.4, 5.4, 8.0))
    wb.school(ax, pos, head, to, tail=25, token=["dna", "rna", "protein"][k], size=0.3)
    bio.panel(ax, "BCD"[k], (x - 0.6, 10.8))
    bio.label(ax, (x + 0.4, 10.5), name.capitalize(), size="small", bold=True, ha="left")
    bio.label(ax, (x + 2.7, 0.7), f"P = {wb.polarization(head)[-1]:.2f}, M = {wb.milling(pos, head)[-1]:.2f}",
              size="tiny", color=P.muted())

pe = Ch.axes_at(ax, (28.6, 1.8, 6.8, 7.6))
ros = [1.05, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 9.0, 12.0]
Pm, Mm = [], []
for ro in ros:
    pv, mv = [], []
    for seed in range(6):
        pos, head = wb.couzin(n=40, steps=500, ro=ro, ra=14.0, seed=100 + seed)
        pv.append(wb.polarization(head)[-50:].mean())
        mv.append(wb.milling(pos, head)[-50:].mean())
    Pm.append(np.mean(pv))
    Mm.append(np.mean(mv))
pe.plot(ros, Pm, "o-", ms=3.5, lw=1.5, color=Ch.line("protein"))
pe.plot(ros, Mm, "o-", ms=3.5, lw=1.5, color=Ch.line("rna"))
pe.text(ros[-1], Pm[-1] - 0.06, "polarization P", fontsize=FS["tiny"], color=Ch.line("protein"), ha="right", va="top")
pe.text(ros[3], max(Mm) + 0.06, "milling M", fontsize=FS["tiny"], color=Ch.line("rna"), ha="center", va="bottom")
pe.set_ylim(0, 1.1)
pe.set_xlim(0.8, 12.5)
Ch.style_axes(pe, "radius of orientation zone", "order parameter")
bio.panel(ax, "E", (26.8, 10.8))
