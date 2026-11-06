# Arrangement of florets on a sunflower head (Vogel 1979): floret k at radius proportional to sqrt(k) and
# angle k x 137.5 degrees (the golden angle). The two families of contact parastichies (every 21st and
# every 34th floret joined) and the divergence angle between successive florets are marked. Right: the same
# rule with a slightly different angle (137.0 and 138.0 degrees) leaves gaps and straight spokes.
import wikibio as bio
from wikibio import botany

P = bio.P
fig, ax = bio.canvas(30, 12.5)
bio.panel(ax, "A", (0.4, 12.2))
bio.label(ax, (8.0, 12.0), r"Golden angle $137.5^\circ$", size="title")
botany.phyllotaxis(ax, (8.0, 6.0), 5.6, n=420, parastichies=(21, 34), numbers=0, angle_arc=False)
bio.panel(ax, "B", (16.6, 12.2))
bio.label(ax, (20.0, 12.0), r"$137.0^\circ$", size="title")
botany.phyllotaxis(ax, (20.0, 6.6), 3.2, n=260, divergence=137.0, parastichies=(), angle_arc=False)
bio.panel(ax, "C", (24.2, 12.2))
bio.label(ax, (26.8, 12.0), r"$138.0^\circ$", size="title")
botany.phyllotaxis(ax, (26.8, 6.6), 3.2, n=260, divergence=138.0, parastichies=(), angle_arc=False)
bio.label(ax, (23.4, 1.8), "Small departures from the golden angle\nleave gaps and straight spokes", size="small")
