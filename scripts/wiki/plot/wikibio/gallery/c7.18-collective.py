# wikibehav sample (7.18): collective. Rendered with render_plot.py like any plot script.
import numpy as np
import wikibio as bio
import wikibehav as wb

P = bio.P
fig, ax = bio.canvas(34, 11)
bio.panel(ax, "A", (0.2, 10.8)); bio.label(ax, (1.2, 10.5), "Zones", size="small", bold=True, ha="left")
wb.zones(ax, (4.2, 5.0), 0.8, 2.0, 3.4, heading=90, blind=90)
for k, (name, x) in enumerate((("swarm", 9.0), ("torus", 15.5), ("parallel", 22.0))):
    pos, head = wb.couzin(n=40, steps=500, seed=k, **wb.COUZIN_REGIMES[name])
    to = wb.fit(pos[-25:], (x, 1.2, 5.8, 8.2))
    wb.school(ax, pos, head, to, tail=25, token=["dna", "rna", "protein"][k], size=0.3)
    bio.panel(ax, "BCD"[k], (x - 0.6, 10.8)); bio.label(ax, (x + 0.4, 10.5), name.capitalize(), size="small", bold=True, ha="left")
    bio.label(ax, (x + 2.9, 0.6), f"P = {wb.polarization(head)[-1]:.2f}, M = {wb.milling(pos, head)[-1]:.2f}", size="tiny", color=P.muted())
pi = wb.path_integration(steps=220, seed=3, error=0.0, displace=(14, -6))
bio.panel(ax, "E", (28.0, 10.8)); bio.label(ax, (29.0, 10.5), "Path integration", size="small", bold=True, ha="left")
to = wb.fit([pi["outbound"], pi["search"], pi["homing"]], (28.4, 0.8, 5.4, 9.2))
wb.trail(ax, to(pi["outbound"]), token="dna", lw=1.0, arrows=3, start="o")
wb.trail(ax, to(pi["homing"]), token="rna", lw=1.4, fade=False, arrows=1)
wb.trail(ax, to(pi["search"]), token="rna", lw=0.8, fade=False)
nest = to(pi["nest"])
bio.label(ax, (nest[0], nest[1] - 0.35), "nest", size="tiny", va="top")
